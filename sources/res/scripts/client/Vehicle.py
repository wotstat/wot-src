import logging, math, random, weakref
from collections import namedtuple
import typing, BigWorld, Math
from Health import StunComponent
import AreaDestructibles, BattleReplay, DestructiblesCache, TriggersManager, constants, physics_shared
from PlayerEvents import g_playerEvents
from account_helpers.settings_core.settings_constants import GAME
from TriggersManager import TRIGGER_TYPE
from VehicleEffects import DamageFromShotDecoder
from aih_constants import ShakeReason
from cgf_components.arena_camera_manager import ArenaCameraManager
from cgf_script.entity_dyn_components import BWEntitiyComponentTracker
from constants import VEHICLE_HIT_EFFECT, VEHICLE_SIEGE_STATE, ATTACK_REASON_INDICES, ATTACK_REASON, SPT_MATKIND, DUAL_GUN
from constants import StunTypes
from debug_utils import LOG_DEBUG_DEV
from arena_bonus_type_caps import ARENA_BONUS_TYPE_CAPS as BONUS_CAPS
from gui.battle_control.arena_info.arena_vos import Comp7Keys
from visual_script.misc import ASPECT
from Event import Event
from gui.battle_control import vehicle_getter, avatar_getter
from gui.battle_control.avatar_getter import getSoundNotifications
from gui.battle_control.battle_constants import FEEDBACK_EVENT_ID as _GUI_EVENT_ID, VEHICLE_VIEW_STATE
from gun_rotation_shared import decodeGunAngles
from helpers import dependency
from helpers.EffectMaterialCalculation import calcSurfaceMaterialNearPoint
from helpers.EffectsList import SoundStartParam
from items import vehicles
from material_kinds import EFFECT_MATERIAL_INDEXES_BY_NAMES, EFFECT_MATERIALS
from skeletons.account_helpers.settings_core import ISettingsCore
from skeletons.gui.battle_session import IBattleSessionProvider
from skeletons.gui.lobby_context import ILobbyContext
from skeletons.gui.game_control import ISpecialSoundCtrl, IBattleRoyaleController
from skeletons.vehicle_appearance_cache import IAppearanceCache
from soft_exception import SoftException
from vehicle_systems.components.shot_damage_components import ShotDamageComponent
from vehicle_systems.entity_components.battle_abilities_component import BattleAbilitiesComponent
from vehicle_systems.components.vehicle_pickup_component import VehiclePickupComponent
from vehicle_systems.model_assembler import collisionIdxToTrackPairIdx
from vehicle_systems.tankStructure import TankPartNames, TankPartIndexes, TankSoundObjectsIndexes
from vehicle_systems.appearance_cache import VehicleAppearanceCacheInfo
from shared_utils.vehicle_utils import createWheelFilters
from cgf_script.component_meta_class import registerComponent
import GenericComponents, Projectiles, CGF
from helpers.styles_perf_toolset import g_stylesOverrider
if typing.TYPE_CHECKING:
    import OwnVehicle
    from items.vehicles import VehicleDescriptor
_logger = logging.getLogger(__name__)
LOW_ENERGY_COLLISION_D = 0.3
HIGH_ENERGY_COLLISION_D = 0.6
_g_respawnQueue = dict()

@registerComponent
class SpawnComponent(object):
    pass


class _Vector4Provider(object):
    __slots__ = (b'_v',)

    @property
    def value(self):
        return self._v

    def __int__(self):
        self._v = Math.Vector4(0.0, 0.0, 0.0, 0.0)
        return


class _VehicleSpeedProvider(object):
    __slots__ = (b'__value',)

    @property
    def value(self):
        return self.__value.value

    def __init__(self):
        self.__value = Math.Vector4Basic()
        return

    def set(self, val):
        self.__value = val
        return

    def reset(self):
        self.__value = Math.Vector4Basic()
        return


SegmentCollisionResultExt = namedtuple(b'SegmentCollisionResultExt', (b'dist', b'hitAngleCos', b'matInfo', b'compName'))
StunInfo = namedtuple(b'StunInfo', (b'startTime', b'endTime', b'duration', b'totalTime', b'stunType'))
DebuffInfo = namedtuple(b'DebuffInfo', (b'duration', b'animated'))
VEHICLE_COMPONENTS = {
 BattleAbilitiesComponent}

class Vehicle(BigWorld.Entity, BWEntitiyComponentTracker, BattleAbilitiesComponent):
    isEnteringWorld = property((lambda self: self.__isEnteringWorld))
    isTurretDetached = property((lambda self: constants.SPECIAL_VEHICLE_HEALTH.IS_TURRET_DETACHED(self.health) and self.__turretDetachmentConfirmed))
    isTurretMarkedForDetachment = property((lambda self: constants.SPECIAL_VEHICLE_HEALTH.IS_TURRET_DETACHED(self.health)))
    isTurretDetachmentConfirmationNeeded = property((lambda self: not self.__turretDetachmentConfirmed))
    hasMovingFlags = property((lambda self: self.engineMode is not None and self.engineMode[1] & 3))
    guiSessionProvider = dependency.descriptor(IBattleSessionProvider)
    lobbyContext = dependency.descriptor(ILobbyContext)
    __specialSounds = dependency.descriptor(ISpecialSoundCtrl)
    __appearanceCache = dependency.descriptor(IAppearanceCache)
    __battleRoyaleController = dependency.descriptor(IBattleRoyaleController)
    __settingsCore = dependency.descriptor(ISettingsCore)
    activeGunIndex = property((lambda self: self.__activeGunIndex))

    @property
    def speedInfo(self):
        return self.__speedInfo

    @property
    def isWheeledTech(self):
        return self.typeDescriptor.type.isWheeledVehicle

    @property
    def hasSpeedometer(self):
        return self.typeDescriptor.type.hasSpeedometer

    @property
    def isScout(self):
        return b'scout' in self.typeDescriptor.type.tags

    @property
    def isTrackWithinTrack(self):
        if self.typeDescriptor is None:
            return False
        else:
            return self.typeDescriptor.isTrackWithinTrack

    @property
    def isMultiTrack(self):
        return self.typeDescriptor.isMultiTrack

    @property
    def isStatTrack(self):
        style = self.appearance.outfit.style
        return style is not None and style.isStatTrackStyle

    @property
    def chassisType(self):
        return self.typeDescriptor.chassisType

    @property
    def wheelsScrollSmoothed(self):
        if self.__wheelsScrollFilter is not None:
            return [scrollFilter.output(BigWorld.time()) for scrollFilter in self.__wheelsScrollFilter]
        else:
            return

    @property
    def wheelsScrollFilters(self):
        return self.__wheelsScrollFilter

    @property
    def wheelsSteeringSmoothed(self):
        if self.__wheelsSteeringFilter is not None:
            return [steeringFilter.output(BigWorld.time()) for steeringFilter in self.__wheelsSteeringFilter]
        else:
            return

    @property
    def wheelsSteeringFilters(self):
        return self.__wheelsSteeringFilter

    @property
    def maxHealth(self):
        return self.publicInfo.maxHealth

    @property
    def team(self):
        return self.publicInfo.team

    @property
    def battleModifiers(self):
        return self.guiSessionProvider.arenaVisitor.getArenaModifiers()

    @property
    def cameraTargetMatrix(self):
        self.set_postmortemViewPointName()
        return self.__cameraTargetMatrix

    @property
    def isPostmortemViewPointDefined(self):
        return self.postmortemViewPointName is not None and self.postmortemViewPointName != b''

    def getBounds(self, partIdx):
        if self.appearance is not None:
            return self.appearance.getBounds(partIdx)
        else:
            return (
             Math.Vector3(0.0, 0.0, 0.0), Math.Vector3(0.0, 0.0, 0.0), 0)

    def getSpeed(self):
        return self.__speedInfo.value[0]

    def getMasterVehID(self):
        return self.masterVehID

    def __init__(self):
        for comp in VEHICLE_COMPONENTS:
            comp.__init__(self)

        self.proxy = weakref.proxy(self)
        self.extras = {}
        self.extrasHitPoint = dict()
        self.typeDescriptor = None
        self.appearance = None
        self.onAppearanceReady = Event()
        self.onUnderWaterSwitch = Event()
        self.isPlayerVehicle = False
        self.isStarted = False
        self.__isEnteringWorld = False
        self.__turretDetachmentConfirmed = False
        self.__speedInfo = _VehicleSpeedProvider()
        self.respawnCompactDescr = None
        self.respawnOutfitCompactDescr = None
        self.__waitingForAppearanceReload = False
        self.__cachedStunInfo = StunInfo(0.0, 0.0, 0.0, 0.0, b'')
        self.__burnoutStarted = False
        self.__handbrakeFired = False
        self.__wheelsScrollFilter = None
        self.__wheelsSteeringFilter = None
        self.isUpgrading = False
        self.isForceReloading = False
        self.__activeGunIndex = None
        self.refreshNationalVoice()
        self.__prevHealth = None
        self.__quickShellChangerIsActive = False
        self.__isInDebuff = False
        self.onEngineStateChange = Event()
        self.onAutoShootStateChange = Event()
        self.__cameraTargetMatrix = Math.AdaptiveMatrixProvider()
        self.set_postmortemViewPointName()
        return

    def reload(self):
        _logger.debug(b'reload(%d)', self.id)
        vehicles.reload()
        Vehicle.respawnVehicle(self.id, self.publicInfo.compDescr)
        return

    def __checkDelayedRespawn(self):
        global _g_respawnQueue
        pair = _g_respawnQueue.pop(self.id, None)
        if pair is not None:
            _logger.debug(b'found delayed respawn request(%d)', self.id)
            self.respawnCompactDescr = pair[0]
            self.respawnOutfitCompactDescr = pair[1]
            return True
        else:
            return False

    def onEnterWorld(self, _=None):
        _logger.debug(b'onEnterWorld(%d)', self.id)
        isDelayedRespawn = self.__checkDelayedRespawn()
        if self.respawnOutfitCompactDescr is not None:
            outfitDescr = self.respawnOutfitCompactDescr
            self.respawnOutfitCompactDescr = None
        else:
            outfitDescr = self.publicInfo.outfit
        oldTypeDescriptor = self.typeDescriptor
        self.typeDescriptor = self.getDescr(None if isDelayedRespawn else self.respawnCompactDescr)
        forceReloading = self.respawnCompactDescr is not None
        result = g_stylesOverrider.overrideStyleForVehicle(self.typeDescriptor.name)
        if result is not None:
            outfitDescr = result
        if b'battle_royale' in self.typeDescriptor.type.tags or self.respawnCompactDescr:
            from InBattleUpgrades import onBattleRoyalePrerequisites
            forceReloading = onBattleRoyalePrerequisites(self, oldTypeDescriptor, forceReloading)
            if isDelayedRespawn:
                self.respawnCompactDescr = None
        strCD = self.typeDescriptor.makeCompactDescr()
        newInfo = VehicleAppearanceCacheInfo(self.typeDescriptor, self.health, self.isCrewActive, self.isTurretDetached, outfitDescr)
        ctrl = self.guiSessionProvider.dynamic.appearanceCache
        if ctrl is not None:
            appearance = ctrl.getAppearance(self.id, newInfo, None, strCD, False)
            if BONUS_CAPS.checkAny(BigWorld.player().arenaBonusType, b'EPIC') and self.isAlive() and appearance and not appearance.isAlive:
                forceReloading = True
            if forceReloading:
                oldStrCD = oldTypeDescriptor.makeCompactDescr() if oldTypeDescriptor is not None else None
                appearance = ctrl.reloadAppearance(self.id, newInfo, self.__onAppearanceReady, strCD, oldStrCD)
                if appearance is not None:
                    self.appearance = appearance
                else:
                    self.__waitingForAppearanceReload = True
            else:
                _logger.info(b'Vehicle::onEnterWorld: vehicle(%s), teamId(%d)', self.typeDescriptor.name, self.publicInfo.team)
                self.appearance = ctrl.getAppearance(self.id, newInfo, self.__onAppearanceReady, strCD)
        else:
            _logger.error(b'Failed to load vehicle appearance. Missing AppearanceCache controller. vId=%s; vInfo=%s; strCD=%s', self.id, newInfo._asdict(), strCD)
        self.respawnCompactDescr = None
        return

    def getDescr(self, respawnCompactDescr):
        if respawnCompactDescr is not None:
            self.isCrewActive = True
            descr = vehicles.VehicleDescr(respawnCompactDescr, extData=self)
            self.__turretDetachmentConfirmed = False
            if b'battle_royale' not in descr.type.tags:
                self.health = self.publicInfo.maxHealth
                self.__prevHealth = self.publicInfo.maxHealth
            return descr
        return vehicles.VehicleDescr(compactDescr=_stripVehCompDescrIfRoaming(self.publicInfo.compDescr), extData=self)

    def deferredRespawn(self):
        if hasattr(self, b'respawnCompactDescr') and self.respawnCompactDescr:
            _logger.debug(b'respawn compact descr is still valid, request reloading of tank resources %s', self.id)
            self.respawnVehicle(self.id, self.respawnCompactDescr)
        return

    @staticmethod
    def respawnVehicle(vID, compactDescr=None, outfitCompactDescr=None):
        _logger.debug(b'respawnVehicle(%d)', vID)
        vehicle = BigWorld.entities.get(vID)
        if vehicle is not None:
            vehicle.respawnCompactDescr = compactDescr
            vehicle.respawnOutfitCompactDescr = outfitCompactDescr
            _g_respawnQueue.pop(vID, None)
            vehicle.onLeaveWorld()
            vehicle.onEnterWorld()
            if vehicle.appearance.findComponentByType(SpawnComponent) is None:
                vehicle.appearance.createComponent(SpawnComponent)
        else:
            _logger.debug(b'Delayed respawn %d', vID)
            _g_respawnQueue[vID] = [compactDescr, outfitCompactDescr]
        return

    @staticmethod
    def onArenaDestroyed():
        _logger.debug(b'onArenaDestroyed')
        _g_respawnQueue.clear()
        return

    def __initAdditionalFilters(self):
        self.__wheelsScrollFilter, self.__wheelsSteeringFilter = createWheelFilters(self.typeDescriptor)
        return

    def __onAppearanceReady(self, appearance):
        _logger.info(b'__onAppearanceReady(%d)', self.id)
        self.appearance = appearance
        self.__waitingForAppearanceReload = False
        self.__isEnteringWorld = True
        self.__prevDamageStickers = frozenset()
        self.__prevPublicStateModifiers = frozenset()
        self.targetFullBounds = True
        self.__initAdditionalFilters()
        player = BigWorld.player()
        player.vehicle_onAppearanceReady(self)
        if self.isPlayerVehicle and player.initCompleted:
            self.cell.sendStateToOwnClient()
        player.initSpace()
        self.__isEnteringWorld = False
        self.isForceReloading = False
        self.__prevHealth = self.maxHealth
        self.resetProperties()
        self.onAppearanceReady()
        if hasattr(self, b'rocketAccelerationController'):
            self.rocketAccelerationController.init()
        for component in self.dynamicComponents.values():
            if hasattr(component, b'onAppearanceReady'):
                component.onAppearanceReady()

        return

    def __onVehicleInfoAdded(self, vehID):
        if self.id != vehID:
            _logger.error(b'__onVehicleInfoAdded(): Received unexpected vehicle id %d. Waiting for %d', vehID, self.id)
            return
        _logger.debug(b'__onVehicleInfoAdded(%d)', self.id)
        player = BigWorld.player()
        player.arena.onVehicleAdded -= self.__onVehicleInfoAdded
        self.appearance.setVehicleInfo(player.arena.vehicles[vehID])
        return

    def onLeaveWorld(self):
        _logger.debug(b'onLeaveWorld %d', self.id)
        self.__appearanceCache.stopLoading(self.id, self.typeDescriptor.makeCompactDescr())
        self.__stopExtras()
        BigWorld.player().vehicle_onLeaveWorld(self)
        return

    def showShooting(self, burstCount, currentGuns, isPredictedShot=False):
        blockShooting = self.siegeState is not None and self.siegeState != VEHICLE_SIEGE_STATE.ENABLED and self.siegeState != VEHICLE_SIEGE_STATE.DISABLED and not self.typeDescriptor.hasAutoSiegeMode
        if not self.isStarted or blockShooting:
            return
        if not isPredictedShot and self.isPlayerVehicle and not BigWorld.player().isWaitingForShot:
            if not BattleReplay.g_replayCtrl.isPlaying:
                return
        extra = self.typeDescriptor.extrasDict[self.typeDescriptor.shootExtraName]
        extra.stopFor(self)
        extra.startFor(self, (burstCount, currentGuns))
        if not isPredictedShot and self.isPlayerVehicle:
            ctrl = self.guiSessionProvider.shared.feedback
            if ctrl is not None:
                ctrl.onShotDone()
            BigWorld.player().cancelWaitingForShot()
        return

    def calcMaxComponentIdx(self):
        maxComponentIdx = TankPartIndexes.ALL[-1]
        if self.appearance.typeDescriptor.chassis.tracks is not None:
            tracks = self.appearance.typeDescriptor.chassis.tracks.trackPairs
            maxComponentIdx += len(tracks) - 1
        wheelsConfig = self.appearance.typeDescriptor.chassis.generalWheelsAnimatorConfig
        if wheelsConfig:
            maxComponentIdx = maxComponentIdx + wheelsConfig.getNonTrackWheelsCount()
        return maxComponentIdx

    def showDamageFromShot(self, attackerID, points, effectsIndex, damageFactor, lastMaterialIsShield):
        if not self.isStarted:
            return
        else:
            hitsReceived = self.appearance.findComponentByType(Projectiles.ProjectileHitsReceivedComponent)
            if hitsReceived is None:
                self.appearance.createComponent(Projectiles.ProjectileHitsReceivedComponent)
            else:
                hitsReceived.addHit()
            effectsDescr = vehicles.g_cache.shotEffects[effectsIndex]
            maxComponentIdx = self.calcMaxComponentIdx()
            decodedPoints = DamageFromShotDecoder.decodeHitPoints(points, self.appearance.collisions, maxComponentIdx, self.typeDescriptor)
            if not decodedPoints:
                return
            firstHitPoint = decodedPoints[0]
            maxPriorityHitPoint = decodedPoints[-1]
            maxHitEffectCode = maxPriorityHitPoint.hitEffectCode
            hasDamageHit = DamageFromShotDecoder.hasDamaged(maxHitEffectCode)
            hasPiercedHit = maxHitEffectCode in VEHICLE_HIT_EFFECT.PIERCED_HITS
            compoundModel = self.appearance.compoundModel
            compMatrix = Math.Matrix(compoundModel.node(firstHitPoint.componentName))
            firstHitDirLocal = firstHitPoint.matrix.applyToAxis(2)
            firstHitDir = compMatrix.applyVector(firstHitDirLocal)
            physParams = effectsDescr[b'physicsParams']
            g_playerEvents.onProjectileExplosion(compMatrix.translation, firstHitDir, physParams[b'shellVelocity'], physParams[b'shellMass'], physParams[b'splashRadius'], physParams[b'splashStrength'])
            targetImpulse = effectsDescr[b'targetImpulse']
            if targetImpulse > 0.0:
                self.appearance.receiveShotImpulse(firstHitDir, targetImpulse)
            player = BigWorld.player()
            sessionProvider = self.guiSessionProvider
            shakeReason = ShakeReason.HIT if hasDamageHit else ShakeReason.HIT_NO_DAMAGE
            player.inputHandler.onVehicleShaken(self, compMatrix.translation, firstHitDir, effectsDescr[b'caliber'], effectsDescr[b'shellType'], shakeReason)
            showFriendlyFlashBang = False
            isAlly = sessionProvider.getArenaDP().isAlly(attackerID)
            if isAlly:
                isFriendlyFireMode = sessionProvider.arenaVisitor.bonus.isFriendlyFireMode()
                hasCustomAllyDamageEffect = sessionProvider.arenaVisitor.bonus.hasCustomAllyDamageEffect()
                showFriendlyFlashBang = isFriendlyFireMode and hasCustomAllyDamageEffect
            showFullscreenEffs = self.isPlayerVehicle and self.isAlive()
            keyPoints, effects, _ = effectsDescr[maxPriorityHitPoint.hitEffectGroup]
            self.appearance.boundEffects.addNewToNode(maxPriorityHitPoint.componentName, maxPriorityHitPoint.matrix, effects, keyPoints, isPlayerVehicle=self.isPlayerVehicle, showShockWave=showFullscreenEffs, showFlashBang=showFullscreenEffs and not showFriendlyFlashBang, showFriendlyFlashBang=showFullscreenEffs and showFriendlyFlashBang, entity_id=self.id, damageFactor=damageFactor, attackerID=attackerID, hitdir=firstHitDir, surfaceNormal=maxPriorityHitPoint.matrix.applyVector(Math.Vector3(0, 0, -1)))
            prefabHit = effectsDescr[b'hitPrefabs'].get(maxPriorityHitPoint.hitEffectGroup) if b'hitPrefabs' in effectsDescr else None
            if prefabHit:

                def hitLoadCallback(go):
                    if self.isAlive():
                        go.createComponent(ShotDamageComponent, firstHitPoint.componentName, compoundModel, self.appearance.collisions)
                    else:
                        CGF.removeGameObject(go)
                    return

                partGO = self.appearance.partsGameObjects.getPartGameObject(prefabHit, self.spaceID, self.appearance.gameObject)
                CGF.loadGameObjectIntoHierarchy(prefabHit, partGO, firstHitPoint.matrix, hitLoadCallback)
            if not self.isAlive():
                return
            soundNotifications = getSoundNotifications()
            needArmorScreenNotDamageSound = soundNotifications is not None and lastMaterialIsShield and not damageFactor and maxHitEffectCode not in VEHICLE_HIT_EFFECT.RICOCHETS and self.__settingsCore.getSetting(GAME.SHOW_DAMAGE_ICON)
            vehicleCtrl = self.guiSessionProvider.shared.vehicleState
            controllingVehicleID = vehicleCtrl.getControllingVehicleID() if vehicleCtrl is not None else -1
            isAttacker = attackerID == controllingVehicleID and maxHitEffectCode is not None and self.id != controllingVehicleID
            isObserverFPV = avatar_getter.isObserverSeesAll() and BigWorld.player().isObserverFPV
            if isAttacker or isObserverFPV:
                ctrl = sessionProvider.shared.feedback
                if ctrl is not None:
                    ctrl.updateMarkerHitState(self.id, maxPriorityHitPoint.componentName, maxHitEffectCode, damageFactor, lastMaterialIsShield, hasPiercedHit)
                if needArmorScreenNotDamageSound:
                    soundNotifications.play(b'ui_armor_screen_not_damage_PC_NPC')
            elif self.id == controllingVehicleID and attackerID != self.id and needArmorScreenNotDamageSound:
                soundNotifications.play(b'ui_armor_screen_not_damage_NPC_PC')
            return

    def showDamageFromExplosion(self, attackerID, center, effectsIndex, damageFactor):
        if not self.isStarted:
            return
        else:
            impulse = vehicles.g_cache.shotEffects[effectsIndex][b'targetImpulse']
            direction = self.position - center
            direction.normalise()
            self.appearance.receiveShotImpulse(direction, impulse / 4.0)
            if not self.isAlive():
                return
            self.showSplashHitEffect(effectsIndex, damageFactor)
            if self.id == attackerID:
                return
            player = BigWorld.player()
            effectsDescr = vehicles.g_cache.shotEffects[effectsIndex]
            player.inputHandler.onVehicleShaken(self, center, direction, effectsDescr[b'caliber'], effectsDescr[b'shellType'], ShakeReason.SPLASH)
            if attackerID == BigWorld.player().playerVehicleID:
                ctrl = self.guiSessionProvider.shared.feedback
                if ctrl is not None:
                    ctrl.setVehicleState(self.id, _GUI_EVENT_ID.VEHICLE_ARMOR_PIERCED)
            return

    def showVehicleCollisionEffect(self, pos, delta_spd, energy=0):
        if not self.isStarted:
            return
        else:
            if delta_spd >= 3:
                effectName = b'collisionVehicleHeavy2'
                mass = self.typeDescriptor.physics[b'weight']
                if mass < 18000:
                    effectName = b'collisionVehicleHeavy1'
                elif mass > 46000:
                    effectName = b'collisionVehicleHeavy3'
            else:
                effectName = b'collisionVehicleLight'
            self.showCollisionEffect(pos, effectName, None, False, 0, None, energy)
            return

    def showCollisionEffect(self, hitPos, collisionEffectName=b'collisionVehicle', collisionNormal=None, isTracks=False, damageFactor=0, impulse=None, pcEnergy=None):
        invWorldMatrix = Math.Matrix(self.matrix)
        invWorldMatrix.invert()
        rot = Math.Matrix()
        if collisionNormal is None:
            rot.setRotateYPR((random.uniform(-3.14, 3.14), random.uniform(-1.5, 1.5), 0.0))
        else:
            rot.setRotateYPR((0, 0, 0))
        mat = Math.Matrix()
        mat.setTranslate(hitPos)
        mat.preMultiply(rot)
        mat.postMultiply(invWorldMatrix)
        if pcEnergy is not None:
            collisionEnergy = [
             SoundStartParam(b'RTPC_ext_collision_impulse_tank', pcEnergy)]
        else:
            collisionEnergy = []
        effectsList = self.typeDescriptor.type.effects.get(collisionEffectName, [])
        if effectsList:
            keyPoints, effects, _ = random.choice(effectsList)
            self.appearance.boundEffects.addNewToNode(TankPartNames.HULL, mat, effects, keyPoints, entity=self, surfaceNormal=collisionNormal, isTracks=isTracks, impulse=impulse, damageFactor=damageFactor, hitPoint=hitPos, soundParams=collisionEnergy)
        return

    def showSplashHitEffect(self, effectsIndex, damageFactor):
        effectsList = vehicles.g_cache.shotEffects[effectsIndex].get(b'armorSplashHit', None)
        if effectsList:
            mat = Math.Matrix()
            mat.setTranslate((0.0, 0.0, 0.0))
            self.appearance.boundEffects.addNewToNode(TankPartNames.HULL, mat, effectsList[1], effectsList[0], entity=self, damageFactor=damageFactor)
        return

    def set_postmortemViewPointName(self, _=None):
        cameraManager = CGF.getManager(self.spaceID, ArenaCameraManager)
        if cameraManager is not None and self.postmortemViewPointName:
            transform = cameraManager.getCameraTransform(self.postmortemViewPointName)
            if transform is not None:
                self.__cameraTargetMatrix.target = transform
                return
        self.__cameraTargetMatrix.target = self.matrix
        return

    def set_isHidden(self, _=None):
        if self.isHidden and self.isStarted:
            self.stopVisual()
        return

    def set_burnoutLevel(self, _=None):
        attachedVehicle = BigWorld.player().getVehicleAttached()
        if attachedVehicle is None:
            return
        else:
            isAttachedVehicle = self.id == attachedVehicle.id
            if self.appearance.detailedEngineState is not None:
                self.appearance.detailedEngineState.throttle = 1 if self.burnoutLevel > 0.01 else 0
            if self.burnoutLevel > 0 and not self.__handbrakeFired:
                if self.getSpeed() > 0.5:
                    if not self.__burnoutStarted:
                        soundObject = self.appearance.engineAudition.getSoundObject(TankSoundObjectsIndexes.CHASSIS)
                        soundObject.play(b'wheel_vehicle_burnout')
                        self.__burnoutStarted = True
            else:
                self.__burnoutStarted = False
            if isAttachedVehicle:
                self.guiSessionProvider.invalidateVehicleState(VEHICLE_VIEW_STATE.BURNOUT, self.burnoutLevel)
            return

    def set_wheelsState(self, prev=0):
        if self.appearance is None:
            return
        else:
            __WHEEL_DESTROYED = 3
            wheelsConfig = self.typeDescriptor.chassis.generalWheelsAnimatorConfig
            if wheelsConfig is None:
                return
            wheelsCount = wheelsConfig.getWheelsCount()
            for i in xrange(0, wheelsCount):
                prevState = prev >> i * 2 & 3
                newState = self.wheelsState >> i * 2 & 3
                if prevState != newState:
                    if newState == __WHEEL_DESTROYED:
                        self.appearance.onChassisDestroySound(False, True, i)
                    elif prevState == __WHEEL_DESTROYED:
                        self.appearance.onChassisDestroySound(False, False, i)

            return

    def set_damageStickers(self, _=None):
        if self.isStarted:
            prev = self.__prevDamageStickers
            curr = frozenset(self.damageStickers)
            self.__prevDamageStickers = curr
            for sticker in prev.difference(curr):
                self.appearance.removeDamageSticker(sticker)

            maxComponentIdx = self.calcMaxComponentIdx()
            for sticker in curr.difference(prev):
                self.appearance.addDamageSticker(sticker, *DamageFromShotDecoder.decodeSegment(sticker, self.appearance.collisions, maxComponentIdx, self.typeDescriptor))

        return

    def set_publicStateModifiers(self, _=None):
        if self.isStarted:
            prev = self.__prevPublicStateModifiers
            curr = frozenset(self.publicStateModifiers)
            self.__prevPublicStateModifiers = curr
            self.__updateModifiers(curr.difference(prev), prev.difference(curr))
            if not self.isPlayerVehicle:
                self.updateStunInfo()
        return

    def set_engineMode(self, _=None):
        if self.isStarted and self.isAlive():
            self.appearance.changeEngineMode(self.engineMode, True)
            self.onEngineStateChange(self.engineMode)
        return

    def set_isStrafing(self, _=None):
        if hasattr(self.filter, b'isStrafing'):
            self.filter.isStrafing = self.isStrafing
        return

    def set_gunAnglesPacked(self, _=None):
        syncGunAngles = getattr(self.filter, b'syncGunAngles', None)
        if syncGunAngles:
            yaw, pitch = decodeGunAngles(self.gunAnglesPacked, self.typeDescriptor.gun.pitchLimits[b'absolute'])
            syncGunAngles(yaw, pitch)
        return

    def set_health(self, _=None):
        return

    def set_isCrewActive(self, _=None):
        if self.isStarted:
            self.appearance.onVehicleHealthChanged()
            if not self.isPlayerVehicle:
                ctrl = self.guiSessionProvider.shared.feedback
                if ctrl is not None:
                    ctrl.setVehicleNewHealth(self.id, self.health)
            if not self.isCrewActive and self.health > 0:
                self.__onVehicleDeath()
        return

    def set_isSpeedCapturing(self, _=None):
        _logger.debug(b'set_isSpeedCapturing %s', self.isSpeedCapturing)
        if not self.isPlayerVehicle:
            ctrl = self.guiSessionProvider.shared.feedback
            if ctrl is not None:
                ctrl.invalidatePassiveEngineering(self.id, (True, self.isSpeedCapturing))
        return

    def set_isBlockingCapture(self, _=None):
        _logger.debug(b'set_isBlockingCapture %s', self.isBlockingCapture)
        if not self.isPlayerVehicle:
            ctrl = self.guiSessionProvider.shared.feedback
            if ctrl is not None:
                ctrl.invalidatePassiveEngineering(self.id, (False, self.isBlockingCapture))
        return

    def set_steeringAngles(self, prev=None):
        if self.__wheelsSteeringFilter is not None:
            for packedValue, steeringFilter in zip(self.steeringAngles, self.__wheelsSteeringFilter):
                unpackedValue = BigWorld.unpackWheelSteering(packedValue)
                steeringFilter.input(BigWorld.time(), unpackedValue)

        return

    def set_wheelsScroll(self, prev=None):
        if self.__wheelsScrollFilter is not None:
            for packedValue, scrollFilter in zip(self.wheelsScroll, self.__wheelsScrollFilter):
                unpackedValue = BigWorld.unpackWheelScroll(packedValue)
                scrollFilter.input(BigWorld.time(), unpackedValue)

        return

    def set_dotEffect(self, _=None):
        attachedVehicle = BigWorld.player().getVehicleAttached()
        if attachedVehicle is None:
            return
        else:
            if self.id == attachedVehicle.id:
                self.guiSessionProvider.invalidateVehicleState(VEHICLE_VIEW_STATE.DOT_EFFECT, self.dotEffect)
            return

    def set_crewCompactDescrs(self, _=None):
        ctrl = self.guiSessionProvider.shared.prebattleSetups
        if ctrl is not None:
            ctrl.setCrew(self.id, list(self.crewCompactDescrs))
        return

    def set_customRoleSlotTypeId(self, _=None):
        ctrl = self.guiSessionProvider.shared.prebattleSetups
        if ctrl is not None:
            ctrl.setDynSlotType(self.id, self.customRoleSlotTypeId)
        return

    def set_enhancements(self, _=None):
        enhancements = self.enhancements
        ctrl = self.guiSessionProvider.shared.prebattleSetups
        if ctrl is not None and enhancements is not None:
            ctrl.setEnhancements(self.id, enhancements.copy())
        return

    def set_onRespawnReloadTimeFactor(self, _None):
        ctrl = self.guiSessionProvider.shared.prebattleSetups
        if ctrl is not None:
            ctrl.setRespawnReloadFactor(self.id, self.onRespawnReloadTimeFactor)
        return

    def set_setups(self, _=None):
        setups = self.setups
        ctrl = self.guiSessionProvider.shared.prebattleSetups
        if ctrl is not None and setups is not None:
            ctrl.setSetups(self.id, setups.copy())
        return

    def set_setupsIndexes(self, _=None):
        setupsIndexes = self.setupsIndexes
        ctrl = self.guiSessionProvider.shared.prebattleSetups
        if ctrl is not None and setupsIndexes is not None:
            ctrl.setSetupsIndexes(self.id, setupsIndexes.copy())
        return

    def set_siegeState(self, _=None):
        avatar = BigWorld.player()
        if not avatar.userSeesWorld():
            return
        else:
            ctrl = self.guiSessionProvider.shared.prebattleSetups
            if ctrl is not None:
                ctrl.setSiegeState(self.id, self.siegeState)
            if not self.isPlayerVehicle and self.typeDescriptor is not None and self.typeDescriptor.hasSiegeMode:
                self.onSiegeStateUpdated(self.siegeState, 0.0)
            return

    def set_publicInfo(self, _):
        self.refreshNationalVoice()
        return

    def set_vehPostProgression(self, _=None):
        ctrl = self.guiSessionProvider.shared.prebattleSetups
        if ctrl is not None:
            ctrl.setPostProgression(self.id, list(self.vehPostProgression))
        return

    def set_disabledSwitches(self, _=None):
        ctrl = self.guiSessionProvider.shared.prebattleSetups
        if ctrl is not None:
            ctrl.setDisabledSwitches(self.id, self.disabledSwitches)
        return

    def onVehiclePickup(self):
        self.entityGameObject.createComponent(VehiclePickupComponent, self.appearance, self.entityGameObject)
        attachedVehicle = BigWorld.player().getVehicleAttached()
        if attachedVehicle is None or self.id != attachedVehicle.id:
            return
        soundObject = self.appearance.engineAudition.getSoundObject(TankSoundObjectsIndexes.CHASSIS)
        if soundObject is not None:
            soundObject.play(b'lift_over')
        return

    def onExtraHitted(self, extraIndex, hitPoint):
        self.extrasHitPoint[extraIndex] = hitPoint
        return

    def getExtraHitPoint(self, extraIndex):
        if extraIndex is None or extraIndex not in self.extrasHitPoint:
            return Math.Vector3(0.0, 10.0, 0.0)
        else:
            return self.extrasHitPoint[extraIndex]

    def set_perks(self, _=None):
        ctrl = self.guiSessionProvider.dynamic.perks
        if ctrl is not None:
            ctrl.updatePerks(self.perks)
        return

    def set_perksRibbonNotify(self, _=None):
        ctrl = self.guiSessionProvider.dynamic.perks
        if ctrl is not None and self.perksRibbonNotify:
            ctrl.notifyRibbonChanges(self.perksRibbonNotify)
        return

    def onHealthChanged(self, newHealth, oldHealth, attackerID, attackReasonID):
        if newHealth > 0 and self.health <= 0:
            self.health = newHealth
            self.__prevHealth = newHealth
            return
        else:
            self.guiSessionProvider.setVehicleHealth(self.isPlayerVehicle, self.id, newHealth, attackerID, attackReasonID)
            if not self.isStarted:
                self.__prevHealth = newHealth
                return
            BigWorld.player().arena.onVehicleHealthChanged(self.id, attackerID, oldHealth - newHealth)
            if not self.appearance.damageState.isCurrentModelDamaged:
                self.appearance.onVehicleHealthChanged()
            if self.health <= 0:
                if self.isCrewActive:
                    self.__onVehicleDeath()
                player = BigWorld.player()
                attachedVehicle = player.getVehicleAttached()
                _logger.info(b'Vehicle::onHealthChanged: vehicleId(%d) destroyed.', self.id)
                if player.isObserver() and player.isObserverFPV and self.id == attachedVehicle.id:
                    player.switchObserverFPV()
            if self.isPlayerVehicle:
                TriggersManager.g_manager.activateTrigger(TRIGGER_TYPE.PLAYER_RECEIVE_DAMAGE, attackerId=attackerID, vehicleId=self.id, damageContext=None)
            if attackReasonID == ATTACK_REASON_INDICES[ATTACK_REASON.WORLD_COLLISION]:
                damageFactor = (self.__prevHealth - newHealth) * 100.0 / self.maxHealth
                if damageFactor > 1:
                    effectsList = self.typeDescriptor.type.effects.get(b'collisionDamage')
                    if effectsList is not None:
                        keyPoints, effects, _ = random.choice(effectsList)
                        self.appearance.boundEffects.addNewToNode(TankPartNames.HULL, None, effects, keyPoints, entity=self, damageFactor=damageFactor)
            self.__prevHealth = newHealth
            return

    def set_stunInfo(self, prev=None):
        _logger.debug(b'Set stun info(curr,~ prev): %s, %s', self.stunInfo, prev)
        if self.stunInfo.stunFinishTime > 0.0 and self.appearance.findComponentByType(StunComponent) is None:
            self.appearance.createComponent(StunComponent)
        if self.stunInfo.stunFinishTime < 0.01:
            self.appearance.removeComponentByType(StunComponent)
        self.updateStunInfo()
        return

    def __updateCachedStunInfo(self, stunInfo):
        endTime = stunInfo.stunFinishTime
        if endTime:
            cachedStartTime = self.__cachedStunInfo.startTime
            startTime = cachedStartTime if cachedStartTime > 0.0 else BigWorld.serverTime()
            totalTime = max(self.__cachedStunInfo.duration, endTime - startTime)
            duration = endTime - BigWorld.serverTime() if endTime > 0.0 else 0.0
            self.__cachedStunInfo = StunInfo(startTime, endTime, duration, totalTime, stunInfo[b'stunType'])
        else:
            self.__cachedStunInfo = StunInfo(0.0, 0.0, 0.0, 0.0, StunTypes.NONE.value)
        return

    def getStunInfo(self):
        self.__updateCachedStunInfo(self.stunInfo)
        return self.__cachedStunInfo

    def updateStunInfo(self):
        attachedVehicle = BigWorld.player().getVehicleAttached()
        if attachedVehicle is None:
            return
        else:
            self.__updateCachedStunInfo(self.stunInfo)
            if self.lobbyContext.getServerSettings().spgRedesignFeatures.isStunEnabled():
                isAttachedVehicle = self.id == attachedVehicle.id
                if isAttachedVehicle:
                    self.guiSessionProvider.invalidateVehicleState(VEHICLE_VIEW_STATE.STUN, self.__cachedStunInfo)
                if not self.isPlayerVehicle:
                    ctrl = self.guiSessionProvider.shared.feedback
                    if ctrl is not None:
                        ctrl.invalidateStun(self.id, self.__cachedStunInfo)
            else:
                _logger.warning(b'Stun features is disabled!')
            return

    def showAmmoBayEffect(self, mode, fireballVolume, projectedTurretSpeed):
        if self.isStarted:
            self.appearance.showAmmoBayEffect(mode, fireballVolume)
        return

    def onPushed(self, x, z):
        try:
            distSqr = BigWorld.player().position.distSqrTo(self.position)
            if distSqr > 1600.0:
                self.filter.setPosition(x, z)
        except Exception:
            pass

        return

    def showRammingEffect(self, energy, point):
        if not self.isStarted:
            return
        if energy < 600:
            self.showCollisionEffect(point, b'rammingCollisionLight')
        else:
            self.showCollisionEffect(point, b'rammingCollisionHeavy')
        return

    def onStaticCollision(self, energy, point, normal, miscFlags, damage, destrEffectIdx, destrMaxHealth):
        if not self.isStarted:
            return
        self.appearance.stopSwinging()
        BigWorld.player().inputHandler.onVehicleCollision(self, self.getSpeed())
        isTrackCollision = bool(miscFlags & 1)
        isSptCollision = bool(miscFlags >> 1 & 1)
        isSptDestroyed = bool(miscFlags >> 2 & 1)
        if isSptDestroyed:
            return
        hitPoint = point
        surfNormal = normal
        matKind = SPT_MATKIND.SOLID
        if destrEffectIdx < 0:
            if not isSptCollision:
                surfaceMaterial = calcSurfaceMaterialNearPoint(hitPoint, normal, self.spaceID)
                hitPoint, surfNormal, matKind, effectIdx = surfaceMaterial
            else:
                effectIdx = EFFECT_MATERIAL_INDEXES_BY_NAMES[b'wood']
            if matKind != 0:
                self.__showStaticCollisionEffect(energy, effectIdx, hitPoint, surfNormal, isTrackCollision, damage * 100.0)
        else:
            self.__showDynamicCollisionEffect(energy, destrMaxHealth, hitPoint, surfNormal)
        return

    def getAimParams(self):
        if self.appearance is not None:
            turretYaw = Math.Matrix(self.appearance.turretMatrix).yaw
            gunPitch = Math.Matrix(self.appearance.gunMatrix).pitch
            return (
             turretYaw, gunPitch)
        else:
            return (0.0, 0.0)

    def onSiegeStateUpdated(self, newState, timeToNextMode):
        if not self.isStarted:
            return
        else:
            if self.typeDescriptor is not None and self.typeDescriptor.hasSiegeMode:
                self.typeDescriptor.onSiegeStateChanged(newState)
                self.appearance.onSiegeStateChanged(newState, timeToNextMode)
                dualAccuracy = self.dynamicComponents.get(b'dualAccuracy')
                if dualAccuracy is not None:
                    dualAccuracy.onSiegeStateUpdated(self.typeDescriptor)
                if self.isPlayerVehicle or self.id == BigWorld.player().observedVehicleID:
                    inputHandler = BigWorld.player().inputHandler
                    if inputHandler.siegeModeControl:
                        inputHandler.siegeModeControl.notifySiegeModeChanged(self, newState, timeToNextMode)
            else:
                _logger.error(b'Wrong usage! Should be called only on vehicle with valid typeDescriptor and siege mode')
            return

    def getSiegeSwitchTimeLeft(self):
        ownVehicle = self.dynamicComponents.get(b'ownVehicle')
        if ownVehicle is None:
            return 0.0
        else:
            return ownVehicle.getSiegeStateTimeLeft()

    def onActiveGunChanged(self, activeGun, cooldownTimes, shotCount):
        if not self.isStarted:
            return
        else:
            if self.typeDescriptor is None or not self.typeDescriptor.isDualgunVehicle:
                return
            switchTimes = cooldownTimes[DUAL_GUN.COOLDOWNS.SWITCH]
            swElapsedTime = switchTimes[2] - switchTimes[1]
            afterShotDelay = self.typeDescriptor.gun.dualGun.afterShotDelay
            leftDelayTime = max(afterShotDelay - swElapsedTime, 0.0)
            if shotCount:
                self.updateDualAccuracyData(shotCount)
            if self.__activeGunIndex == activeGun:
                return
            self.__activeGunIndex = activeGun
            ctrl = self.guiSessionProvider.shared.feedback
            if ctrl is not None:
                ctrl.invalidateActiveGunChanges(self.id, (activeGun, leftDelayTime))
            return

    def isGunsBecomeEmpty(self, gunStates):
        isEmpty = self.guiSessionProvider.shared.ammo.isEmptyAmmo()
        return all(state == DUAL_GUN.GUN_STATE.EMPTY for state in gunStates) and isEmpty

    def updateDualAccuracyData(self, shotCount):
        dualAccuracy = self.dynamicComponents.get(b'dualAccuracy')
        if dualAccuracy is None:
            return
        else:
            dualAccuracy.setDualShotStatus(shotCount == 2)
            return

    def collideSegmentExt(self, startPoint, endPoint):
        if self.appearance.collisions is not None:
            collisions = self.appearance.collisions.collideAllWorld(startPoint, endPoint)
            if collisions:
                res = []
                for collision in collisions:
                    matInfo = self.getMatinfo(collision[3], collision[2])
                    res.append(SegmentCollisionResultExt(collision[0], collision[1], matInfo, collision[3]))

                return res
        return

    def getMatinfo(self, parIndex, matKind):
        matInfo = None
        if parIndex == TankPartIndexes.CHASSIS:
            matInfo = self.typeDescriptor.chassis.materials.get(matKind)
        elif parIndex == TankPartIndexes.HULL:
            matInfo = self.typeDescriptor.hull.materials.get(matKind)
        elif parIndex == TankPartIndexes.TURRET:
            matInfo = self.typeDescriptor.turret.materials.get(matKind)
        elif parIndex == TankPartIndexes.GUN:
            matInfo = self.typeDescriptor.gun.materials.get(matKind)
        elif parIndex > len(TankPartIndexes.ALL):
            trackPairIdx = collisionIdxToTrackPairIdx(parIndex, self.typeDescriptor)
            if trackPairIdx is not None:
                matInfo = self.typeDescriptor.chassis.tracks[trackPairIdx].materials.get(matKind)
        elif self.isWheeledTech and self.appearance.collisions is not None:
            wheelName = self.appearance.collisions.getPartName(parIndex)
            if wheelName is not None:
                matInfo = self.typeDescriptor.chassis.wheelsArmor.get(wheelName, None)
        if matInfo is None:
            commonMaterialsInfo = vehicles.g_cache.commonConfig[b'materials']
            matInfo = commonMaterialsInfo.get(matKind)
        return matInfo

    def isAlive(self):
        return self.isCrewActive and self.health > 0

    def isPitchHullAimingAvailable(self):
        return self.typeDescriptor is not None and self.typeDescriptor.isPitchHullAimingAvailable

    def getServerGunAngles(self):
        return decodeGunAngles(self.gunAnglesPacked, self.typeDescriptor.gun.pitchLimits[b'absolute'])

    def startVisual(self):
        _logger.debug(b'startVisual(%d)', self.id)
        if self.isHidden:
            _logger.info(b'Vehicle is marked as hidden: %d', self.id)
            return
        else:
            if self.__waitingForAppearanceReload:
                _logger.info(b'Waiting for appearance reload: %d', self.id)
                return
            if not self.appearance.isConstructed:
                _logger.warning(b'Vehicle appearance is not constructed: %d', self.id)
                return
            if self.isStarted:
                raise SoftException(b'Vehicle is already started')
            avatar = BigWorld.player()
            self.appearance.setVehicle(self)
            self.appearance.removeComponentByType(GenericComponents.HierarchyComponent)
            self.appearance.createComponent(GenericComponents.HierarchyComponent, self.entityGameObject)
            self.appearance.activate()
            vehInfo = avatar.arena.vehicles.get(self.id, None)
            if vehInfo is not None:
                self.appearance.setVehicleInfo(vehInfo)
            else:
                avatar.arena.onVehicleAdded += self.__onVehicleInfoAdded
            self.appearance.changeEngineMode(self.engineMode)
            if self.isPlayerVehicle or self.typeDescriptor is None or not self.typeDescriptor.hasSiegeMode:
                self.appearance.changeSiegeState(self.siegeState)
            self.appearance.onVehicleHealthChanged(self.isPlayerVehicle)
            if hasattr(self.filter, b'allowStrafeCompensation'):
                self.filter.allowStrafeCompensation = not self.isPlayerVehicle
            if hasattr(self.filter, b'gravityOnLag') and self.typeDescriptor.isAirCraft:
                self.filter.gravityOnLag = Math.Vector3(0, 0, 0)
            self.isStarted = True
            if not self.appearance.isObserver:
                self.show(True)
            self.set_publicStateModifiers()
            self.set_damageStickers()
            if TriggersManager.g_manager:
                TriggersManager.g_manager.fireTrigger(TriggersManager.TRIGGER_TYPE.VEHICLE_VISUAL_VISIBILITY_CHANGED, vehicleId=self.id, isVisible=True)
            self.startGUIVisual()
            self.refreshBuffEffects()
            if self.isSpeedCapturing:
                self.set_isSpeedCapturing()
            if self.isBlockingCapture:
                self.set_isBlockingCapture()
            if self.isTurretMarkedForDetachment:
                self.confirmTurretDetachment()
            self.__startPhysics()
            if not self.isPlayerVehicle and self.typeDescriptor is not None and self.typeDescriptor.hasSiegeMode:
                self.onSiegeStateUpdated(self.siegeState, 0.0)
            self.appearance.highlighter.setVehicleOwnership()
            progressionCtrl = self.guiSessionProvider.dynamic.progression
            if progressionCtrl is not None:
                progressionCtrl.vehicleVisualChangingFinished(self.id)
            BigWorld.callback(0.0, self.deferredRespawn)
            self.refreshNationalVoice()
            self.set_quickShellChangerFactor()
            return

    def startGUIVisual(self):
        self.guiSessionProvider.startVehicleVisual(self.proxy, True)
        if not self.isAlive():
            self.__onVehicleDeath(True)
        if self.stunInfo.stunFinishTime > 0.0:
            self.updateStunInfo()
        if self.thermalVisionFinishTime > 0.0:
            self.set_thermalVisionFinishTime()
        return

    def refreshNationalVoice(self):
        player = BigWorld.player()
        if self.id == player.observedVehicleID:
            self.__specialSounds.setPlayerVehicle(self.publicInfo, False)
        elif self.id == player.playerVehicleID:
            self.__specialSounds.setPlayerVehicle(self.publicInfo, True)
        return

    def stopVisual(self):
        _logger.debug(b'Vehicle.stopVisual(%d)', self.id)
        if not self.isStarted:
            raise SoftException(b'Vehicle is already stopped')
        self.__stopExtras()
        if TriggersManager.g_manager:
            TriggersManager.g_manager.fireTriggerInstantly(TriggersManager.TRIGGER_TYPE.VEHICLE_VISUAL_VISIBILITY_CHANGED, vehicleId=self.id, isVisible=False)
        self.appearance.removeComponentByType(GenericComponents.HierarchyComponent)
        self.appearance.deactivate()
        self.stopGUIVisual()
        self.appearance = None
        self.isStarted = False
        self.__speedInfo.reset()
        if self.__isInDebuff:
            self.onDebuffEffectApplied(False)
        return

    def stopGUIVisual(self):
        self.guiSessionProvider.stopVehicleVisual(self.id, self.isPlayerVehicle)
        return

    def show(self, show):
        if show:
            drawFlags = BigWorld.DrawAll
        else:
            drawFlags = 0
        if self.isStarted:
            va = self.appearance
            if va.tracks is not None:
                va.tracks.setPhysicalDestroyedTracksVisible(show)
            va.changeDrawPassVisibility(drawFlags)
            va.showStickers(show)
        return

    def addCameraCollider(self):
        if self.appearance is not None:
            self.appearance.addCameraCollider()
        return

    def removeCameraCollider(self):
        if self.appearance is not None:
            self.appearance.removeCameraCollider()
        return

    def changeVehicleExtrasSetting(self, extraName, newValue):
        extra = self.typeDescriptor.extrasDict[extraName]
        if self.extras.has_key(extra.index):
            extra.updateFor(self, newValue)
        return

    def getOptionalDevices(self):
        if self.isPlayerVehicle:
            return vehicle_getter.getOptionalDevices()
        return []

    def _isDestructibleMayBeBroken(self, chunkID, itemIndex, matKind, itemFilename, itemScale, vehSpeed):
        desc = AreaDestructibles.g_cache.getDescByFilename(itemFilename)
        if desc is None:
            return False
        else:
            ctrl = AreaDestructibles.g_destructiblesManager.getController(chunkID)
            if ctrl is None:
                return False
            if ctrl.isDestructibleBroken(itemIndex, matKind, desc[b'type']):
                return True
            mass = self.typeDescriptor.physics[b'weight']
            instantDamage = 0.5 * mass * vehSpeed * vehSpeed * 0.00015
            if desc[b'type'] == DestructiblesCache.DESTR_TYPE_STRUCTURE:
                moduleDesc = desc[b'modules'].get(matKind)
                if moduleDesc is None:
                    return False
                refHealth = moduleDesc[b'health']
            else:
                unitMass = AreaDestructibles.g_cache.unitVehicleMass
                instantDamage *= math.pow(mass / unitMass, desc[b'kineticDamageCorrection'])
                refHealth = desc[b'health']
            return DestructiblesCache.scaledDestructibleHealth(itemScale, refHealth) < instantDamage

    def __showStaticCollisionEffect(self, energy, effectIdx, hitPoint, normal, isTrackCollision, damageFactor):
        heavyVelocities = self.typeDescriptor.type.heavyCollisionEffectVelocities
        heavyEnergy = heavyVelocities[b'track'] if isTrackCollision else heavyVelocities[b'hull']
        heavyEnergy = 0.5 * heavyEnergy * heavyEnergy
        postfix = b'%sCollisionLight' if energy < heavyEnergy else b'%sCollisionHeavy'
        effectName = b''
        if effectIdx < len(EFFECT_MATERIALS):
            effectName = EFFECT_MATERIALS[effectIdx]
        effectName = postfix % effectName
        if effectName in self.typeDescriptor.type.effects:
            self.showCollisionEffect(hitPoint, effectName, normal, isTrackCollision, damageFactor, self.__getImpulse(self.getSpeed()))
        return

    def __showDynamicCollisionEffect(self, energy, destrMaxHealth, hitPoint, surfNormal):
        effectName = b'dynamicCollision'
        if effectName in self.typeDescriptor.type.effects:
            self.showCollisionEffect(hitPoint, effectName, surfNormal, False, 0, self.__getDynamicImpulse(self.getSpeed(), destrMaxHealth))
        return

    def __startPhysics(self):
        if not hasattr(self.filter, b'setVehiclePhysics'):
            return
        typeDescr = self.typeDescriptor
        isWheeled = self.typeDescriptor.type.isWheeledVehicle
        physics = BigWorld.WheeledPhysics() if isWheeled else BigWorld.TankPhysics()
        physics_shared.initVehiclePhysicsClient(physics, typeDescr)
        arenaMinBound, arenaMaxBound = (-10000, -10000), (10000, 10000)
        physics.setArenaBounds(arenaMinBound, arenaMaxBound)
        physics.owner = weakref.ref(self)
        physics.staticMode = False
        physics.movementSignals = 0
        self.filter.setVehiclePhysics(physics)
        yaw, pitch = decodeGunAngles(self.gunAnglesPacked, typeDescr.gun.pitchLimits[b'absolute'])
        self.filter.syncGunAngles(yaw, pitch)
        self.__speedInfo.set(self.filter.speedInfo)
        return

    def __stopPhysics(self):
        self.__speedInfo.reset()
        return

    def __getImpulse(self, speed):
        mass = self.typeDescriptor.physics[b'weight']
        maxSpeed = self.typeDescriptor.physics[b'speedLimits'][0]
        return math.fabs(speed * mass / (maxSpeed * mass))

    def __getDynamicImpulse(self, speed, maxHealth):
        maxSpeed = 20.0
        relSpeed = min(math.fabs(speed / maxSpeed), 1.0)
        relSpeed *= relSpeed
        relHeath = min(min(maxHealth, 90.0) / 90.0, 1.0)
        return 0.5 * (relSpeed + relHeath)

    def __stopExtras(self):
        extraTypes = self.typeDescriptor.extras
        for index, data in self.extras.items():
            extraTypes[index].stop(data)

        if self.extras:
            _logger.warning(b'this code point should have never been reached')
        return

    def __updateModifiers(self, addedExtras, removedExtras):
        extraTypes = self.typeDescriptor.extras
        for idx in removedExtras:
            extraTypes[idx].stopFor(self)

        for idx in addedExtras:
            try:
                extraTypes[idx].startFor(self)
            except Exception:
                _logger.exception(b'Update modifiers. Vehicle id "%d" and CD "%r"', self.id, self.typeDescriptor.makeCompactDescr())

        return

    def __onVehicleDeath(self, isDeadStarted=False):
        if not self.isPlayerVehicle:
            ctrl = self.guiSessionProvider.shared.feedback
            if ctrl is not None:
                ctrl.setVehicleState(self.id, _GUI_EVENT_ID.VEHICLE_DEAD, isDeadStarted)
        TriggersManager.g_manager.fireTrigger(TRIGGER_TYPE.VEHICLE_DESTROYED, vehicleId=self.id)
        self._removeInspire()
        self._removeHealing()
        bwfilter = self.filter
        if hasattr(bwfilter, b'velocityErrorCompensation'):
            bwfilter.velocityErrorCompensation = 100.0
        return

    def confirmTurretDetachment(self):
        self.__turretDetachmentConfirmed = True
        if self.isTurretDetached:
            self.appearance.updateTurretVisibility()
        else:
            _logger.error(b'Vehicle::confirmTurretDetachment: Confirming turret detachment, though the turret is not detached')
        return

    def updateLaserSight(self, vehicleID, isTakesAim, beamMode):
        if self.id == vehicleID and not self.isPlayerVehicle:
            extra = self.typeDescriptor.extrasDict[b'laserSight']
            if extra.isRunningFor(self):
                args = {b'isTakesAim': isTakesAim, b'beamMode': beamMode}
                extra.updateFor(self, args)
        return

    def drawEdge(self, forceSimpleEdge=False):
        if self.appearance and self.appearance.highlighter:
            self.appearance.highlighter.highlight(True, forceSimpleEdge)
        return

    def removeEdge(self, forceSimpleEdge=False):
        if self.appearance and self.appearance.highlighter:
            self.appearance.highlighter.highlight(False, forceSimpleEdge)
        return

    def addModel(self, model):
        super(Vehicle, self).addModel(model)
        highlighter = self.appearance.highlighter
        if highlighter.isOn:
            highlighter.highlight(False)
            highlighter.highlight(True)
        return

    def delModel(self, model):
        highlighter = self.appearance.highlighter
        hlOn = highlighter.isOn
        hlSimpleEdge = highlighter.isSimpleEdge
        highlighter.removeHighlight()
        super(Vehicle, self).delModel(model)
        if hlOn:
            highlighter.highlight(True, hlSimpleEdge)
        return

    def notifyInputKeysDown(self, movementDir, rotationDir, handbrakeFired):
        self.filter.notifyInputKeysDown(movementDir, rotationDir)
        self.__handbrakeFired = handbrakeFired
        if self.appearance.detailedEngineState is not None:
            self.appearance.detailedEngineState.throttle = movementDir or rotationDir
        return

    def turnoffThrottle(self):
        if self.appearance.detailedEngineState is not None:
            self.appearance.detailedEngineState.throttle = 0
        return

    def onDebuffEffectApplied(self, applied):
        self.__isInDebuff = applied
        attachedVehicle = BigWorld.player().getVehicleAttached()
        if attachedVehicle is not None and self.id == attachedVehicle.id:
            playerDebuffInfo = DebuffInfo(duration=0.1 if applied else 0, animated=applied)
            self.guiSessionProvider.invalidateVehicleState(VEHICLE_VIEW_STATE.DEBUFF, playerDebuffInfo)
        else:
            ctrl = self.guiSessionProvider.shared.feedback
            if ctrl is not None:
                enemyDebuffInfo = DebuffInfo(duration=99 if applied else 0, animated=True)
                ctrl.invalidateDebuff(self.id, enemyDebuffInfo)
        return

    def onDynamicComponentCreated(self, component):
        LOG_DEBUG_DEV(b'Component created', component)
        super(Vehicle, self).onDynamicComponentCreated(component)
        return

    def onDynamicComponentDestroyed(self, component):
        LOG_DEBUG_DEV(b'Component destroyed', component)
        super(Vehicle, self).onDynamicComponentDestroyed(component)
        return

    @property
    def label(self):
        if hasattr(self, b'labelComponent'):
            return self.labelComponent.label
        else:
            return

    def set_quickShellChangerFactor(self, _=None):
        ammoCtrl = self.guiSessionProvider.shared.ammo
        if ammoCtrl is not None and self.isMyVehicle and self.isAlive():
            shellChangefactor = self.quickShellChangerFactor
            ammoCtrl.setQuickChangerFactor(isActive=0 < shellChangefactor < 1.0, factor=shellChangefactor)
        return

    @property
    def quickShellChangerIsActive(self):
        return self.__quickShellChangerIsActive

    @quickShellChangerIsActive.setter
    def quickShellChangerIsActive(self, value):
        self.__quickShellChangerIsActive = value
        return

    def isOnFire(self):
        return b'fire' in self.dynamicComponents

    def resetProperties(self):
        self.set_burnoutLevel()
        self.set_damageStickers()
        self.set_dotEffect()
        self.set_engineMode()
        self.set_gunAnglesPacked()
        self.set_health()
        self.set_isBlockingCapture()
        self.set_isCrewActive()
        self.set_isSpeedCapturing()
        self.set_isStrafing()
        self.set_publicStateModifiers()
        self.set_siegeState()
        self.set_steeringAngles()
        self.set_stunInfo()
        self.set_wheelsScroll()
        self.set_wheelsState()
        if hasattr(self, b'remoteCamera'):
            self.set_remoteCamera()
        if hasattr(self, b'ownVehicle'):
            self.ownVehicle.initialUpdate(True)
        self.set_thermalVisionFinishTime()
        return

    def set_remoteCamera(self, _=None):
        self.ownVehicle.update_remoteCamera(self.remoteCamera)
        return

    def set_thermalVisionFinishTime(self, _=None):
        if not self.isPlayerVehicle:
            ctrl = self.guiSessionProvider.shared.feedback
            if ctrl is not None:
                ctrl.invalidateThermalVisionFinishTime(self.id, self.thermalVisionFinishTime)
        return

    def set_selectedComp7Skill(self, _=None):
        arena = avatar_getter.getArena()
        if arena:
            stats = dict()
            stats[self.id] = {(Comp7Keys.ROLE_SKILL): (self.selectedComp7Skill)}
            arena.onGameModeSpecificStats(isStatic=True, stats=stats)
        if self.isPlayerVehicle:
            ctrl = self.guiSessionProvider.dynamic.comp7PrebattleSkillController
            if ctrl is not None:
                ctrl.onVehicleSkillUpdated(self.selectedComp7Skill)
        return

    def getVseContextInstance(self, contextName):
        from visual_script.contexts.cgf_context import CGFGameObjectContext
        if contextName == CGFGameObjectContext.__name__:
            if self.entityGameObject:
                return CGFGameObjectContext(self.entityGameObject, ASPECT.CLIENT)
            _logger.error(b'Could not create CGFGameObjectContext because self.entityGameObject is None')
        return BigWorld.player().arena.getVseContextInstance(contextName)


@dependency.replace_none_kwargs(lobbyContext=ILobbyContext)
def _stripVehCompDescrIfRoaming(vehCompDescr, lobbyContext=None):
    serverSettings = lobbyContext.getServerSettings() if lobbyContext is not None else None
    if serverSettings is not None:
        if serverSettings.roaming.isInRoaming():
            vehCompDescr = vehicles.stripCustomizationFromVehicleCompactDescr(vehCompDescr, True, True, False)[0]
    return vehCompDescr
