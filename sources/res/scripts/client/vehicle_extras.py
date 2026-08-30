from __future__ import absolute_import, division, print_function
import typing, logging
from functools import partial
import BattleReplay
from future.utils import lrange, viewitems, viewvalues
import AnimationSequence, BigWorld, Math, material_kinds
from GenericComponents import findSlot
from constants import IS_EDITOR, CollisionFlags, DEFAULT_GUN_INSTALLATION_INDEX, IS_UE_EDITOR
from cgf_events import shot_event
from debug_utils import LOG_CODEPOINT_WARNING, LOG_CURRENT_EXCEPTION
from gui.impl import backport
from gui.impl.gen import R
from helpers import i18n
from helpers.EffectsList import EffectsListPlayer
from helpers.EntityExtra import EntityExtra
from helpers.prefab_effects import resolveGunPrefabEffects
from helpers.laser_sight_matrix_provider import LaserSightMatrixProvider
from items import vehicles
from items.components.component_constants import MAIN_TRACK_PAIR_IDX
from vehicle_systems.shooting_helpers import processVehicleSingleShot, processVehicleMultiShot
from vehicle_systems.stricted_loading import makeCallbackWeak
from vehicle_systems.vehicle_composition import VehicleSlots
_logger = logging.getLogger(__name__)

def reload():
    modNames = (
     reload.__module__,)
    from sys import modules
    from py2to3.moves import importLib
    for m in modNames:
        importLib.reload(modules[m])

    print(b'vehicle_extras reloaded')
    return


class NoneExtra(EntityExtra):
    __slots__ = ()

    def _start(self, data, args):
        LOG_CODEPOINT_WARNING()
        self.stop(data)
        return


class ShowShooting(EntityExtra):
    __slots__ = ()

    def _start(self, data, args):
        burstCount, _, shellType = args
        vehicle = data[b'entity']
        gunInstallationSlot = vehicle.typeDescriptor.gunInstallations[DEFAULT_GUN_INSTALLATION_INDEX]
        data[b'_gunInstallationSlot'] = gunInstallationSlot
        data[b'_effectsListPlayer'] = None
        data[b'_skipLegacyGroundWave'] = False
        gunDescr = gunInstallationSlot.gun
        gunPrefabEffects, excludeTags = resolveGunPrefabEffects(gunDescr.prefabEffects)
        if gunPrefabEffects is not None and gunPrefabEffects.groundwave.prefab:
            data[b'_skipLegacyGroundWave'] = True
        if gunDescr.effects is not None:
            stages, effects, _ = gunDescr.effects
            data[b'_effectsListPlayer'] = EffectsListPlayer(effects, stages, excludeTags, **data)
        data[b'entity_id'] = vehicle.id
        data[b'_burst'] = (
         burstCount, gunDescr.burst[1])
        data[b'_gunModel'] = vehicle.appearance.compoundModel
        data[b'_shellType'] = shellType
        self.__doShot(data)
        return

    def _cleanup(self, data):
        if data.get(b'_effectsListPlayer') is not None:
            data[b'_effectsListPlayer'].stop()
        timerID = data.get(b'_timerID')
        if timerID is not None:
            BigWorld.cancelCallback(timerID)
            data[b'_timerID'] = None
        return

    def __doShot(self, data):
        data[b'_timerID'] = None
        try:
            vehicle = data[b'entity']
            if not vehicle.isAlive():
                self.stop(data)
                return
            processVehicleSingleShot(vehicle, data[b'_gunInstallationSlot'])
            if not data[b'_gunInstallationSlot'].gun.prefabBased:
                self.__postVehicleShotEvent(vehicle, data[b'_shellType'])
            burstCount, burstInterval = data[b'_burst']
            gunModel = data[b'_gunModel']
            effPlayer = data[b'_effectsListPlayer']
            onComplete = None
            if burstCount == 1:
                onComplete = partial(self.__onComplete, data)
                if effPlayer is None:
                    data[b'_timerID'] = BigWorld.callback(0.01, onComplete)
                withShot = 1
            else:
                data[b'_burst'] = (
                 burstCount - 1, burstInterval)
                data[b'_timerID'] = BigWorld.callback(burstInterval, partial(self.__doShot, data))
                withShot = 2
            if effPlayer is not None:
                effPlayer.stop()
                effPlayer.play(gunModel, None, onComplete)
            self.__doRecoil(vehicle, gunModel)
            if not IS_EDITOR:
                avatar = BigWorld.player()
                if data[b'entity'].isPlayerVehicle or vehicle is avatar.getVehicleAttached():
                    avatar.getOwnVehicleShotDispersionAngle(avatar.gunRotator.turretRotationSpeed, withShot)
                if effPlayer is not None and not data[b'_skipLegacyGroundWave']:
                    groundWaveEff = effPlayer.effectsList.relatedEffects.get(b'groundWave')
                    if groundWaveEff is not None:
                        self._doGroundWaveEffect(data[b'entity'], groundWaveEff, gunModel)
        except Exception:
            LOG_CURRENT_EXCEPTION()
            self.stop(data)

        return

    def __onComplete(self, data):
        data[b'_timerID'] = None
        self.stop(data)
        return

    def __postVehicleShotEvent(self, vehicle, shellType):
        if BattleReplay.g_replayCtrl.isTimeWarpInProgress:
            return
        if not vehicle.appearance.isCompositionReady:
            _logger.debug(b'Composition is not ready to post VehicleShotEvent')
            return
        gunGo = findSlot(vehicle.entityGameObject, VehicleSlots.GUN.value)
        if IS_UE_EDITOR and not gunGo.valid:
            gunGo = findSlot(vehicle.appearance.gameObject, VehicleSlots.GUN.value)
        if gunGo.valid:
            shot_event.postVehicleShotEvent(vehicle.entityGameObject, gunGo, 0, shellType)
        else:
            _logger.error(b'Unable to post VehicleShotEvent: gunGo was not found')
        return

    def __doRecoil(self, vehicle, gunModel):
        appearance = vehicle.appearance
        appearance.recoil()
        return

    def _doGroundWaveEffect(self, vehicle, groundWaveEff, gunModel, gunNode=None):
        node = gunModel.node(b'HP_gunFire' if gunNode is None else gunNode)
        gunMatr = Math.Matrix(node)
        gunPos = gunMatr.translation
        gunDir = gunMatr.applyVector((0, 0, 1))
        upVec = Math.Matrix(vehicle.matrix).applyVector(Math.Vector3(0, 1, 0))
        if upVec.y != 0:
            centerToGun = gunPos - vehicle.position
            centerToGunDist = centerToGun.length
            centerToGun.normalise()
            gunHeight = centerToGunDist * centerToGun.dot(upVec) / upVec.y
            gunPos.y -= gunHeight
        distanceToWater = BigWorld.wg_collideWater(gunPos, gunPos + Math.Vector3(0, 1, 0), False)
        if distanceToWater > -1:
            position = gunPos - Math.Vector3(0, distanceToWater, 0)
            matKind = material_kinds.getWaterMatKind()
        else:
            testRes = BigWorld.wg_collideSegment(BigWorld.player().spaceID, gunPos + Math.Vector3(0, 0.5, 0), gunPos - Math.Vector3(0, 1.5, 0), 128)
            if testRes is None:
                return
            position = testRes.closestPoint
            matKind = testRes.matKind
        BigWorld.player().terrainEffects.addNew(position, groundWaveEff.effectsList, groundWaveEff.keyPoints, None, dir=gunDir, surfaceMatKind=matKind, start=position + Math.Vector3(0, 0.5, 0), end=position - Math.Vector3(0, 0.5, 0), entity_id=vehicle.id)
        return


class ShowShootingMultiGun(ShowShooting):
    _SHOT_ALL_GUNS = -1

    def _start(self, data, args):
        burstCount, currentGuns, _ = args
        vehicle = data[b'entity']
        gunInstallationSlot = vehicle.typeDescriptor.gunInstallations[DEFAULT_GUN_INSTALLATION_INDEX]
        data[b'_gunInstallationSlot'] = gunInstallationSlot
        gunDescr = vehicle.typeDescriptor.gun
        if currentGuns == self._SHOT_ALL_GUNS:
            data[b'_gunIndex'] = lrange(0, len(gunDescr.multiGun))
            data[b'_gunSequence'] = [data[b'_gunIndex']] * burstCount
        else:
            data[b'_gunIndex'] = [
             currentGuns]
            data[b'_gunSequence'] = [data[b'_gunIndex']] * burstCount
        if vehicle.typeDescriptor.isDualgunVehicle:
            positions = [
             None] * len(gunDescr.multiGun)
        else:
            positions = [(multiGunInstance.gunFire,) for multiGunInstance in gunDescr.multiGun]
        data[b'entity_id'] = vehicle.id
        effectPlayers = {}
        if gunDescr.effects is not None:
            for gunIndex in data[b'_gunIndex']:
                stages, effects, _ = gunDescr.effects[gunIndex]
                effectPlayers[gunIndex] = EffectsListPlayer(effects, stages, position=positions[gunIndex], **data)

        data[b'_effectsListPlayers'] = effectPlayers
        data[b'_burst'] = (
         burstCount, burstCount, gunDescr.burst[1])
        data[b'_gunModel'] = vehicle.appearance.compoundModel
        self.__doShot(data)
        return

    def _cleanup(self, data):
        effPlayers = data.get(b'_effectsListPlayers')
        if effPlayers is None:
            return
        else:
            for effPlayer in effPlayers.values():
                if effPlayer is not None:
                    effPlayer.stop()

            timerID = data.get(b'_timerID')
            if timerID is not None:
                BigWorld.cancelCallback(timerID)
                data[b'_timerID'] = None
            return

    def __doShot(self, data):
        data[b'_timerID'] = None
        try:
            vehicle = data[b'entity']
            if not vehicle.isAlive():
                self.stop(data)
                return
            burstSize, burstCount, burstInterval = data[b'_burst']
            gunIndexes = data[b'_gunSequence'][burstSize - burstCount]
            if len(gunIndexes) > 1:
                processVehicleMultiShot(vehicle, data[b'_gunInstallationSlot'], gunIndexes)
            else:
                processVehicleSingleShot(vehicle, data[b'_gunInstallationSlot'], gunIndexes[0])
            if burstCount == 1:
                self.__doGunEffect(data, gunIndexes, True)
                withShot = 1
            else:
                data[b'_burst'] = (
                 burstSize, burstCount - 1, burstInterval)
                data[b'_timerID'] = BigWorld.callback(burstInterval, partial(self.__doShot, data))
                self.__doGunEffect(data, gunIndexes, False)
                withShot = 2
            self.__doRecoil(data)
            if not IS_EDITOR:
                avatar = BigWorld.player()
                if data[b'entity'].isPlayerVehicle or vehicle is avatar.getVehicleAttached():
                    avatar.getOwnVehicleShotDispersionAngle(avatar.gunRotator.turretRotationSpeed, withShot=withShot)
        except Exception:
            LOG_CURRENT_EXCEPTION()
            self.stop(data)

        return

    def __doGunEffect(self, data, gunIndexes, isLastEffect):
        for gunIndex, effPlayer in data[b'_effectsListPlayers'].items():
            effPlayer.stop()

        gunModel = data[b'_gunModel']
        for gunIndex in gunIndexes:
            if gunIndex not in data[b'_effectsListPlayers']:
                continue
            effPlayer = data[b'_effectsListPlayers'][gunIndex]
            if isLastEffect:
                effPlayer.play(gunModel, None, partial(self.stop, data))
            else:
                effPlayer.play(gunModel)
            if not IS_EDITOR:
                groundWaveEff = effPlayer.effectsList.relatedEffects.get(b'groundWave')
                if groundWaveEff is not None:
                    vehicle, multiGun = data[b'entity'], data[b'_gunInstallationSlot'].gun.multiGun
                    self._doGroundWaveEffect(vehicle, groundWaveEff, gunModel, gunNode=multiGun[gunIndex].gunFire)

        return

    def __doRecoil(self, data):
        vehicle = data[b'entity']
        appearance = vehicle.appearance
        gunIndexes = data[b'_gunIndex']
        appearance.multiGunRecoil(gunIndexes)
        return


class DamageMarker(EntityExtra):
    __slots__ = (b'deviceUserString', b'sounds')

    def _readConfig(self, dataSection, containerName):
        self.deviceUserString = dataSection.readString(b'deviceUserString')
        if not self.deviceUserString:
            self._raiseWrongConfig(b'deviceUserString', containerName)
        self.deviceUserString = self._getDeviceUserString(dataSection, containerName)
        self.sounds = self._getSounds(dataSection[b'sounds'])
        return

    def _getDeviceUserString(self, dataSection, containerName):
        return i18n.makeString(dataSection.readString(b'deviceUserString'))

    def _getSounds(self, soundSection):
        sounds = {}
        if soundSection is None:
            return sounds
        else:
            for state in (b'critical', b'destroyed', b'functional', b'fixed'):
                sound = soundSection.readString(state)
                if sound:
                    sounds[state] = sound

            return sounds

    @property
    def isTankman(self):
        return False


def wheelHealths(name, index, containerName, dataSection, vehType):
    extras = []
    maxAxleCount = max(len(c[1][b'axleSteeringLockAngles']) for c in viewitems(vehType.xphysics[b'chassis']))
    template = vehicles.makeMultiExtraNameTemplate(name)
    for number in range(maxAxleCount * 2):
        extraName = template.format(number)
        wheelHealth = DamageMarker(extraName, number + index, containerName, dataSection)
        extras.append(wheelHealth)

    return extras


class TrackHealth(DamageMarker):
    __slots__ = (b'__isLeft', b'_trackPairIndex')

    def _readConfig(self, dataSection, containerName):
        self.__isLeft = dataSection.readBool(b'isLeft')
        self._trackPairIndex = dataSection.readInt(b'trackPairIdx', 0)
        DamageMarker._readConfig(self, dataSection, containerName)
        functionalCanMoveState = b'functionalCanMove'
        self.sounds[functionalCanMoveState] = dataSection.readString(b'sounds/' + functionalCanMoveState)
        return

    def _getDeviceUserString(self, dataSection, _):
        resource = R.strings.ingame_gui.devices.track
        typeTxt = backport.text(resource.left() if self.__isLeft else resource.right())
        return backport.text(resource(), type=typeTxt)

    def _start(self, data, args):
        data[b'entity'].appearance.addCrashedTrack(self.__isLeft, self._trackPairIndex, self.index)
        return

    def _cleanup(self, data):
        data[b'entity'].appearance.delCrashedTrack(self.__isLeft, self._trackPairIndex)
        return


class TrackWithinTrackHealth(TrackHealth):

    def _getDeviceUserString(self, dataSection, _):
        resource = R.strings.ingame_gui.devices.track
        typeTxt = backport.text(resource.main() if self._trackPairIndex == MAIN_TRACK_PAIR_IDX else resource.outer())
        return backport.text(resource(), type=typeTxt)


class TankmanHealth(DamageMarker):

    @property
    def isTankman(self):
        return True


class BlinkingLaserSight(EntityExtra):
    __slots__ = (b'_isEnabledBlinking', b'_shouldCollideTarget', b'_beamLength', b'_bindNode', b'_beamSeqs')
    _SEQUENCE_NAMES = (b'beamStaticSeq', b'beamReloadStartSeq', b'beamReloadFininshSeq')
    _MAX_LASER_DISTANCE = 564

    def _readConfig(self, dataSection, containerName):
        self._isEnabledBlinking = dataSection.readBool(b'isEnabledBlinking')
        self._shouldCollideTarget = dataSection.readBool(b'shouldCollideTarget')
        self._beamLength = dataSection.readFloat(b'beamLength', 1.0)
        self._bindNode = dataSection.readString(b'bindNode')
        self._beamSeqs = {name: dataSection.readString(name) for name in self._SEQUENCE_NAMES if self._isEnabledBlinking or name == b'beamStaticSeq'}
        return

    def _newData(self, entity):
        data = super(BlinkingLaserSight, self)._newData(entity)
        data.update({b'beamModelRef': None, 
           b'bindNodeRef': None, 
           b'beamMP': None, 
           b'animatorRefs': {}, b'currSeq': None, 
           b'isVehicleTakenAtGunPoint': False})
        return data

    def _start(self, data, args):
        vehicle = data[b'entity']
        data[b'bindNodeRef'] = vehicle.model.node(self._bindNode)
        if data[b'bindNodeRef'] is not None:
            data[b'beamMP'] = LaserSightMatrixProvider()
            data[b'beamMP'].beamMatrix = data[b'bindNodeRef']
            data[b'beamModelRef'] = BigWorld.Model(b'')
            data[b'beamModelRef'].addMotor(BigWorld.Servo(data[b'beamMP'].beamMatrix))
            player = BigWorld.player()
            player.addModel(data[b'beamModelRef'])
            for beamSeq in viewvalues(self._beamSeqs):
                loader = AnimationSequence.Loader(beamSeq, player.spaceID)
                data[b'animatorRefs'][beamSeq] = loader.loadSync()
                BigWorld.loadResourceListBG((loader,), makeCallbackWeak(self.__onSequenceLoaded, beamSeq, data))

        return

    def _update(self, data, args):
        vehicle = data[b'entity']
        if not (vehicle.health > 0 and vehicle.isCrewActive):
            self.stop(data)
            return
        else:
            if args is None or data[b'bindNodeRef'] is None:
                return
            gunMatr = Math.Matrix(data[b'bindNodeRef'])
            gunPos = gunMatr.applyToOrigin()
            gunDir = gunMatr.applyToAxis(2)
            endPos = gunPos + gunDir * self._MAX_LASER_DISTANCE
            collidePos = BigWorld.wg_collideDynamicStatic(vehicle.spaceID, gunPos, endPos, CollisionFlags.TRIANGLE_PROJECTILENOCOLLIDE, vehicle.id, -1, 0)
            data[b'isVehicleTakenAtGunPoint'] = args[b'isTakesAim'] or not self._shouldCollideTarget or collidePos[1]
            distanceToTarget = gunPos.distTo(collidePos[0]) if collidePos is not None else self._MAX_LASER_DISTANCE
            beamMode = args[b'beamMode']
            if beamMode not in self._beamSeqs:
                beamMode = b'beamStaticSeq'
            requestedSeq = self._beamSeqs[beamMode]
            if data[b'isVehicleTakenAtGunPoint']:
                data[b'beamMP'].beamLength = distanceToTarget / self._beamLength
                if data[b'currSeq'] != requestedSeq:
                    self.__stopAnimator(data)
                data[b'currSeq'] = requestedSeq
                data[b'animatorRefs'][data[b'currSeq']].setEnabled(True)
                data[b'animatorRefs'][data[b'currSeq']].start()
            elif data[b'currSeq'] is not None:
                self.__stopAnimator(data)
            return

    def _cleanup(self, data):
        self.__stopAnimator(data)
        self.__stopModel(data)
        data[b'bindNodeRef'] = None
        data[b'beamMP'] = None
        for animator in viewvalues(data[b'animatorRefs']):
            animator.unbind()

        data[b'animatorRefs'] = {}
        return

    @staticmethod
    def __onSequenceLoaded(seqName, data, resourceRefs):
        if seqName not in resourceRefs.failedIDs and data[b'beamModelRef'] is not None:
            data[b'animatorRefs'][seqName].bindTo(AnimationSequence.ModelWrapperContainer(data[b'beamModelRef'], BigWorld.player().spaceID))
        return

    @staticmethod
    def __stopAnimator(data):
        if data[b'currSeq'] is None:
            return
        else:
            data[b'animatorRefs'][data[b'currSeq']].stop()
            data[b'animatorRefs'][data[b'currSeq']].setEnabled(False)
            data[b'currSeq'] = None
            return

    @staticmethod
    def __stopModel(data):
        if data[b'beamModelRef'] is None:
            return
        else:
            BigWorld.player().delModel(data[b'beamModelRef'])
            data[b'beamModelRef'] = None
            return
