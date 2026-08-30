from __future__ import absolute_import, division
import logging, math, GUI, BigWorld, typing
from constants import IMPACT_TYPES, BATTLE_LOG_MECHANIC_SHOT
import Math
from frameworks.wulf.view.submodel_presenter import SubModelPresenter
from gui.battle_control.controllers.kill_cam_ctrl import KillCamInfoMarkerType, ImpactMarkerData, GunMarkerData, DistanceMarkerData
from gui.impl.gen.view_models.common.vehicle_mechanic_model import MechanicsEnum
from gui.impl.gen.view_models.views.battle.death_cam.death_cam_hud_view_model import DeathCamHudViewModel, ShellType, Phase, DeathReason, ImpactMode, CaliberRule
from gui.prb_control.entities.listener import IGlobalListener
from gui.shared.events import DeathCamEvent
from helpers import dependency
from helpers.CallbackDelayer import CallbackDelayer
from math_common import round_py2_style, round_py2_style_int
from skeletons.gui.battle_session import IBattleSessionProvider
from items import vehicles
if typing.TYPE_CHECKING:
    from typing import Optional, Dict
_logger = logging.getLogger(__name__)
_MODE_SHELL_ICON = {(BATTLE_LOG_MECHANIC_SHOT.BUSTLE_FEED_ACTIVE): (MechanicsEnum.BUSTLE_FEED.value)}

def hasShellPenetrationDistanceLoss(shellType):
    return shellType in (
     ShellType.ARMORPIERCING,
     ShellType.ARMORPIERCINGPREMIUM,
     ShellType.ARMORPIERCINGCR,
     ShellType.ARMORPIERCINGCRPREMIUM)


class DeathCamMarkerView(SubModelPresenter, IGlobalListener):
    __guiSessionProvider = dependency.descriptor(IBattleSessionProvider)
    _HIDE_MARKERS_DURING_PAUSE = False
    shellIconMap = {b'ARMOR_PIERCING': (ShellType.ARMORPIERCING), 
       b'ARMOR_PIERCING_CR': (ShellType.ARMORPIERCINGCR), 
       b'ARMOR_PIERCING_CR_GOLD': (ShellType.ARMORPIERCINGCRPREMIUM), 
       b'ARMOR_PIERCING_GOLD': (ShellType.ARMORPIERCINGPREMIUM), 
       b'HIGH_EXPLOSIVE': (ShellType.HIGHEXPLOSIVE), 
       b'HIGH_EXPLOSIVE_MODERN': (ShellType.HIGHEXPLOSIVEMODERN), 
       b'HIGH_EXPLOSIVE_MODERN_GOLD': (ShellType.HIGHEXPLOSIVEMODERNPREMIUM), 
       b'HIGH_EXPLOSIVE_GOLD': (ShellType.HIGHEXPLOSIVEPREMIUM), 
       b'HIGH_EXPLOSIVE_LEGACY_NO_STUN': (ShellType.HIGHEXPLOSIVESPG), 
       b'HIGH_EXPLOSIVE_LEGACY_STUN': (ShellType.HIGHEXPLOSIVESPGSTUN), 
       b'HOLLOW_CHARGE': (ShellType.HOLLOWCHARGE), 
       b'HOLLOW_CHARGE_GOLD': (ShellType.HOLLOWCHARGEPREMIUM)}
    __DEATH_REASONS = {b'hp': (DeathReason.HP), 
       b'crew': (DeathReason.CREW), 
       b'ignition': (DeathReason.IGNITION), 
       b'detonation': (DeathReason.DETONATION)}
    __IMPACT_MODES = {(IMPACT_TYPES.PENETRATION): (ImpactMode.PENETRATION), 
       (IMPACT_TYPES.LEGACY_HE): (ImpactMode.LEGACYHE), 
       (IMPACT_TYPES.MODERN_HE): (ImpactMode.MODERNHE), 
       (IMPACT_TYPES.NON_PENETRATION_DAMAGE): (ImpactMode.NONPENETRATIONDAMAGE)}

    def __init__(self, viewModel, parentView):
        super(DeathCamMarkerView, self).__init__(viewModel, parentView)
        self.__gunPosConfig = 0.5
        self.__markerMatrix = None
        self.__callbackDelayer = CallbackDelayer()
        self.__positionController = GUI.WGMarkerPositionController()
        return

    @property
    def viewModel(self):
        return self.getViewModel()

    @staticmethod
    def __getMechanicShotModeIcon(attackerMechanicInfo):
        if attackerMechanicInfo is None:
            return b''
        else:
            return _MODE_SHELL_ICON.get(attackerMechanicInfo.get(b'mechanicShotMode'), b'')

    def initialize(self):
        super(DeathCamMarkerView, self).initialize()
        self.__addListeners()
        self.__initializeModel()
        return

    def finalize(self):
        self.__removeListeners()
        super(DeathCamMarkerView, self).finalize()
        return

    def __addListeners(self):
        killCamCtrl = self.__guiSessionProvider.shared.killCamCtrl
        if killCamCtrl:
            killCamCtrl.onKillCamModeStateChanged += self.__onKillCamStateChanged
            killCamCtrl.onMarkerDisplayChanged += self.__onMarkerDisplayChanged
        return

    def __removeListeners(self):
        killCamCtrl = self.__guiSessionProvider.shared.killCamCtrl
        if killCamCtrl:
            killCamCtrl.onKillCamModeStateChanged -= self.__onKillCamStateChanged
            killCamCtrl.onMarkerDisplayChanged -= self.__onMarkerDisplayChanged
        return

    def __onKillCamStateChanged(self, killCamState, _):
        if killCamState is DeathCamEvent.State.PREPARING:
            self.viewModel.setIsSimplified(self.__isSimplifiedView())
        elif killCamState is DeathCamEvent.State.PAUSE:
            self.viewModel.setIsAdvanced(True)
        elif killCamState is DeathCamEvent.State.RESUME:
            self.viewModel.setIsAdvanced(False)
        elif killCamState in [DeathCamEvent.State.ENDING, DeathCamEvent.State.FINISHED]:
            self.viewModel.setIsMarkerVisible(False)
            self.viewModel.setIsAdvanced(False)
            if killCamState is DeathCamEvent.State.FINISHED:
                self.__positionController.remove(self.viewModel.marker.proxy)
        return

    def __onMarkerDisplayChanged(self, markerType, ctx):
        if markerType is KillCamInfoMarkerType.HIDDEN:
            self.viewModel.setIsMarkerVisible(False)
        if markerType is KillCamInfoMarkerType.IMPACT:
            markerData = ctx[b'markerData']
            self.__showImpactMarker(markerData)
        if markerType is KillCamInfoMarkerType.GUN:
            markerData = ctx[b'markerData']
            if not self.__isSimplifiedView():
                self.__showGunMarker(markerData)
        if markerType is KillCamInfoMarkerType.DISTANCE:
            markerData = ctx[b'markerData']
            self.__showDistanceMarker(markerData)
        return

    def __showDistanceMarker(self, distanceMarkerData):
        self.__updateDistanceMarkerModel(distanceMarkerData)
        projectileHitPos = distanceMarkerData.impactPoint
        if projectileHitPos is None:
            return
        else:
            self.__markerMatrix = Math.createTranslationMatrix(projectileHitPos)
            self.__updateMarkerPosition()
            return

    def __showImpactMarker(self, impactMarkerData):
        phaseDuration = impactMarkerData.phaseDuration
        projectileData = impactMarkerData.projectile
        relativeArmor = impactMarkerData.relativeArmor
        causeOfDeath = impactMarkerData.causeOfDeath
        shellKind = projectileData[b'shellKind']
        self.__updateImpactMarkerModel(phaseDuration, projectileData, relativeArmor, shellKind, causeOfDeath)
        self.__updateMarkerPosition()
        return

    def __showGunMarker(self, gunMarkerData):
        phaseDuration = gunMarkerData.phaseDuration
        projectileData = gunMarkerData.projectile
        shellType = self.shellIconMap[projectileData[b'shellType']]
        attackerMechanicInfo = gunMarkerData.mechanicsInfo[b'attacker']
        self.__updateGunMarkerModel(phaseDuration, projectileData, shellType, attackerMechanicInfo)
        self.__markerMatrix, markerOffsetMatrix = self.__getCaliberMarkerPositions(gunMarkerData)
        if self.viewModel is not None:
            gunMatrixProvider = BigWorld.LerpPositionMatrixProvider(self.__markerMatrix, markerOffsetMatrix, self.__gunPosConfig)
            self.__positionController.add(self.viewModel.marker.proxy, gunMatrixProvider)
            self.__showMarker()
        return

    def __updateGunMarkerModel(self, phaseDuration, projectileData, shellType, attackerMechanicInfo):
        self.__updateGunMarkerParameters(projectileData, shellType, attackerMechanicInfo)
        self.__updateViewModelSettings(Phase.KILLER, 0, phaseDuration, True)
        return

    def __updateImpactMarkerModel(self, phaseDuration, projectileData, relativeArmor, shellKind, causeOfDeath):
        self.__updateImpactMarkerParameters(projectileData, relativeArmor, shellKind, causeOfDeath)
        self.__updateViewModelSettings(Phase.IMPACT, 0, phaseDuration, True)
        return

    def __updateDistanceMarkerModel(self, distanceMarkerData):
        phaseDuration = distanceMarkerData.phaseDuration
        projectileData = distanceMarkerData.projectile
        shellType = self.shellIconMap[projectileData[b'shellType']]
        isAttackerSpotted = distanceMarkerData.isAttackerSpotted
        attackerMechanicInfo = distanceMarkerData.mechanicsInfo[b'attacker']
        self.__updateDistanceMarkerParameters(projectileData, shellType, isAttackerSpotted, attackerMechanicInfo)
        self.__updateViewModelSettings(Phase.TRAJECTORY, 0, phaseDuration, True)
        return

    def __updateGunMarkerParameters(self, projectileData, shellType, attackerMechanicInfo):
        impactType = self.__IMPACT_MODES[projectileData[b'impactType']]
        self.viewModel.setImpactMode(impactType)
        self.viewModel.setShellType(shellType)
        self.viewModel.setShellIcon(projectileData[b'shellIcon'])
        self.viewModel.setModeShellIcon(self.__getMechanicShotModeIcon(attackerMechanicInfo))
        self.viewModel.setShellCaliber(projectileData[b'shellCaliber'])
        averageDamageOfShell = projectileData[b'averageDamageOfShell']
        self.viewModel.setShellDamageBasic(averageDamageOfShell)
        velocity = projectileData[b'velocity']
        projSpeedFactor = vehicles.g_cache.commonConfig[b'miscParams'][b'projectileSpeedFactor']
        self.viewModel.setShellVelocityBasic(round_py2_style_int(velocity.length / projSpeedFactor))
        caliberRule = CaliberRule.NONE
        if projectileData[b'is3CaliberRuleActive']:
            caliberRule = CaliberRule.THREECALIBER
        elif projectileData[b'is2CaliberRuleActive']:
            caliberRule = CaliberRule.TWOCALIBER
        self.viewModel.setCaliberRule(caliberRule)
        return

    def __updateDistanceMarkerParameters(self, projectileData, shellType, isAttackerSpotted, attackerMechanicInfo):
        impactType = self.__IMPACT_MODES[projectileData[b'impactType']]
        self.viewModel.setImpactMode(impactType)
        if self.__isSimplifiedView():
            self.viewModel.setShellType(shellType)
            self.viewModel.setShellIcon(projectileData[b'shellIcon'])
            self.viewModel.setModeShellIcon(self.__getMechanicShotModeIcon(attackerMechanicInfo))
        if isAttackerSpotted and b'distanceOfShot' in projectileData:
            self.viewModel.setIsKillerUnspotted(False)
            self.viewModel.setShootDistance(projectileData[b'distanceOfShot'])
        else:
            self.viewModel.setIsKillerUnspotted(True)
        self.viewModel.setShellPenetrationBasic(projectileData[b'nominalPiercingPower'])
        effectivePenetration = int(projectileData[b'piercingPower'])
        self.viewModel.setShellPenetrationEffective(effectivePenetration)
        return

    def __updateImpactMarkerParameters(self, projectileData, relativeArmor, shellKind, causeOfDeath):
        impactType = self.__IMPACT_MODES[projectileData[b'impactType']]
        effectiveShellDamage = projectileData[b'effectiveShellDamage']
        averageDamageOfShell = projectileData[b'averageDamageOfShell']
        self.viewModel.setShellDamageBasic(averageDamageOfShell)
        self.viewModel.setShellDamageEffective(effectiveShellDamage)
        self.viewModel.setArmorNominal(projectileData[b'nominalArmor'])
        self.viewModel.setArmorRelative(relativeArmor)
        self.viewModel.setShellArmorAngleGain(projectileData[b'angleGain'])
        self.viewModel.setShellDamageRandomizationFactor(projectileData[b'damageRandomizationFactor'])
        self.viewModel.setHasDistanceFalloff(projectileData[b'hasDistanceFalloff'])
        if b'damageDistanceModifier' in projectileData:
            self.viewModel.setDamageDistanceModifier(projectileData[b'damageDistanceModifier'])
        hitAngleDegree = round_py2_style_int(math.degrees(math.acos(projectileData[b'hitAngleCos'])))
        self.viewModel.setAngleImpact(hitAngleDegree)
        if projectileData[b'is3CaliberRuleActive']:
            ricochetAngle = maxPenetrationAngle = 90
        else:
            ricochetAngle = round_py2_style(math.degrees(math.acos(projectileData[b'ricochetAngleCos'])))
            maxPenetrationAngle = min(projectileData[b'maxPenetrationAngle'], ricochetAngle)
        self.viewModel.setAngleFailure(maxPenetrationAngle)
        self.viewModel.setAngleRicochet(ricochetAngle)
        nominalBurst = projectileData[b'shellDamageBurstHE']
        armorProtectionHE = -abs(round_py2_style_int(projectileData[b'armorProtectionHE']))
        spallLinerProtectionHE = -abs(round_py2_style_int(projectileData[b'spallLinerProtectionHE']))
        distanceLossHE = -abs(round_py2_style_int(projectileData[b'distanceLossHE']))
        randomization = -(nominalBurst - effectiveShellDamage + armorProtectionHE + spallLinerProtectionHE)
        self.viewModel.setShellDamageBurst(nominalBurst)
        self.viewModel.setShellDamageLossProtectionHe(armorProtectionHE)
        self.viewModel.setShellDamageLossProtectionSpallLiner(spallLinerProtectionHE)
        self.viewModel.setShellDamageLossDistance(distanceLossHE)
        self.viewModel.setImpactMode(impactType)
        if impactType == ImpactMode.LEGACYHE:
            randomization -= distanceLossHE
            self.viewModel.setShellDamageRandomizationFactor(randomization)
        elif impactType == ImpactMode.MODERNHE:
            self.viewModel.setShellDamageBasic(averageDamageOfShell / 2)
            self.viewModel.setShellDamageRandomizationFactor(randomization)
        self.viewModel.setDeathReason(self.__DEATH_REASONS.get(causeOfDeath, DeathReason.HP))
        return

    def __updateViewModelSettings(self, phase, phaseTimePassed, phaseDuration, isVisible):
        self.viewModel.setPhase(phase)
        self.viewModel.setPhaseTimePassed(phaseTimePassed)
        self.viewModel.setPhaseDuration(phaseDuration)
        self.viewModel.setIsMarkerVisible(isVisible)
        return

    def __initializeModel(self):
        self.viewModel.setPhase(Phase.KILLER)
        self.viewModel.setImpactMode(ImpactMode.PENETRATION)
        self.viewModel.setShellType(ShellType.ARMORPIERCING)
        self.viewModel.setShellIcon(ShellType.ARMORPIERCING.value)
        self.viewModel.setDeathReason(DeathReason.HP)
        return

    def __updateMarkerPosition(self):
        if self.viewModel is not None:
            self.__positionController.add(self.viewModel.marker.proxy, self.__markerMatrix)
            self.__showMarker()
        return

    def __getCaliberMarkerPositions(self, markerData):
        simulatedKillerGunInfo = markerData.simulatedKillerGunInfo
        if simulatedKillerGunInfo:
            return simulatedKillerGunInfo
        caliberMarkerMatrix = Math.createTranslationMatrix(markerData.projectileOrigin)
        return (caliberMarkerMatrix, caliberMarkerMatrix)

    def __showMarker(self):
        if not self.viewModel.getIsMarkerVisible():
            self.viewModel.setIsMarkerVisible(True)
        return

    def __hideMarker(self):
        if self.viewModel.getIsMarkerVisible():
            self.viewModel.setIsMarkerVisible(False)
        return

    def __isSimplifiedView(self):
        avatar = BigWorld.player()
        if not avatar:
            return False
        return avatar.isSimpleDeathCam()
