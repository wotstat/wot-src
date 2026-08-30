from __future__ import absolute_import, division
import logging
from copy import copy
from math import fabs
from constants import ExtraShotClipStates, STATIONARY_RELOAD_STATE
from helpers.CallbackDelayer import CallbackDelayer
from helpers import gEffectsDisabled, dependency
from debug_utils import LOG_DEBUG
import SoundGroups, BigWorld
from skeletons.gui.battle_session import IBattleSessionProvider
_logger = logging.getLogger(__name__)
BARREL_DEBUG_ENABLED = False
GUN_RAMMER_TIME = 1.5
GUN_RAMMER_EFFECT_NAME = b'cons_gun_rammer_start'
_CALIBER_RELOAD_SOUND_SWITCH = b'SWITCH_ext_rld_autoloader_caliber'

class ReloadEffectsType(object):
    SIMPLE_RELOAD = b'SimpleReload'
    BARREL_RELOAD = b'BarrelReload'
    AUTO_RELOAD = b'AutoReload'
    DUALGUN_RELOAD = b'DualGunReload'
    TWINGUN_RELOAD = b'TwinGunReload'
    EXTRASHOTCLIP_RELOAD = b'ExtraShotClipReload'
    CHARGEABLEBURST_RELOAD = b'ChargeableBurstReload'
    STATIONARY_RELOAD = b'StationaryReloadReload'


def _createReloadEffectDesc(eType, dataSection, parentSection):
    if not dataSection.values():
        return
    else:
        if eType == ReloadEffectsType.SIMPLE_RELOAD:
            return _SimpleReloadDesc(dataSection, eType)
        if eType == ReloadEffectsType.BARREL_RELOAD:
            return _BarrelReloadDesc(dataSection, eType)
        if eType == ReloadEffectsType.AUTO_RELOAD:
            return _AutoReloadDesc(dataSection, eType)
        if eType == ReloadEffectsType.DUALGUN_RELOAD:
            return _DualGunReloadDesc(dataSection, eType)
        if eType == ReloadEffectsType.TWINGUN_RELOAD:
            return _TwinGunReloadDesc(dataSection, eType)
        if eType == ReloadEffectsType.EXTRASHOTCLIP_RELOAD:
            return _ExtraShotClipReloadDesc(dataSection, eType, parentSection)
        if eType == ReloadEffectsType.CHARGEABLEBURST_RELOAD:
            return _ChargeableBurstReloadDesc(dataSection, eType)
        if eType == ReloadEffectsType.STATIONARY_RELOAD:
            return _StationaryReloadDesc(dataSection, eType, parentSection)
        return


class _ReloadDesc(object):
    __slots__ = (b'_intuitionOverrides',)

    def __init__(self):
        self._intuitionOverrides = {}
        return

    def create(self):
        return

    def createIntuitionReload(self):
        return

    def hasUniqueIntuitionReload(self):
        return bool(self._intuitionOverrides)


class _SimpleReloadDesc(_ReloadDesc):
    __slots__ = (b'duration', b'soundEvent', b'effectType')

    def __init__(self, dataSection, eType):
        super(_SimpleReloadDesc, self).__init__()
        self.duration = dataSection.readFloat(b'duration', 0.0) / 1000.0
        self.soundEvent = dataSection.readString(b'sound', b'')
        self.effectType = eType
        intuitionOverrides = dataSection[b'intuition_overrides']
        if intuitionOverrides is not None:
            self._intuitionOverrides[b'duration'] = intuitionOverrides.readFloat(b'duration', self.duration * 1000.0) / 1000.0
            self._intuitionOverrides[b'sound'] = intuitionOverrides.readString(b'sound', self.soundEvent)
        return

    def create(self):
        return SimpleReload(self)

    def createIntuitionReload(self):
        decr = copy(self)
        decr.duration = self._intuitionOverrides.get(b'duration', self.duration)
        decr.soundEvent = self._intuitionOverrides.get(b'sound', self.soundEvent)
        return decr.create()


class _DualGunReloadDesc(_SimpleReloadDesc):
    __slots__ = (b'ammoLowSound', b'runTimeDelta', b'runTimeDeltaAmmoLow', b'caliber')

    def __init__(self, dataSection, eType):
        super(_DualGunReloadDesc, self).__init__(dataSection, eType)
        self.ammoLowSound = dataSection.readString(b'ammoLowSound', b'')
        self.runTimeDelta = dataSection.readFloat(b'runTimeDelta', 0.0)
        self.runTimeDeltaAmmoLow = dataSection.readFloat(b'runTimeDeltaAmmoLow', 0.0)
        self.caliber = dataSection.readString(b'caliber', b'')
        return

    def create(self):
        return DualGunReload(self)

    def createIntuitionReload(self):
        return DualGunReload(self)


class _TwinGunReloadDesc(_SimpleReloadDesc):
    __slots__ = (b'twinGunSound', b'runTimeDeltaOneGun', b'runTimeDeltaTwinGun', b'caliber')

    def __init__(self, dataSection, eType):
        super(_TwinGunReloadDesc, self).__init__(dataSection, eType)
        self.twinGunSound = dataSection.readString(b'twinGunSound', b'')
        self.runTimeDeltaOneGun = dataSection.readFloat(b'runTimeDeltaOneGun', 0.0)
        self.runTimeDeltaTwinGun = dataSection.readFloat(b'runTimeDeltaTwinGun', 0.0)
        self.caliber = dataSection.readString(b'caliber', b'')
        return

    def create(self):
        return TwinGunReload(self)

    def createIntuitionReload(self):
        return TwinGunReload(self)


class _BarrelReloadDesc(_SimpleReloadDesc):
    __slots__ = (b'lastShellAlert', b'shellDuration', b'startLong', b'startLoop', b'stopLoop', b'loopShell', b'loopShellLast', b'ammoLow', b'caliber', b'shellDt', b'shellDtLast')

    def __init__(self, dataSection, eType):
        super(_BarrelReloadDesc, self).__init__(dataSection, eType)
        self.lastShellAlert = dataSection.readString(b'lastShellAlert', b'')
        self.shellDuration = dataSection.readFloat(b'shellDuration', 0.0) / 1000.0
        self.startLong = dataSection.readString(b'startLong', b'')
        self.startLoop = dataSection.readString(b'startLoop', b'')
        self.stopLoop = dataSection.readString(b'stopLoop', b'')
        self.loopShell = dataSection.readString(b'loopShell', b'')
        self.loopShellLast = dataSection.readString(b'loopShellLast', b'')
        self.ammoLow = dataSection.readString(b'ammoLow', b'')
        self.caliber = dataSection.readString(b'caliber', b'')
        self.shellDt = dataSection.readFloat(b'loopShellDt', 0.5)
        self.shellDtLast = dataSection.readFloat(b'loopShellLastDt', 0.5)
        intuitionOverrides = dataSection[b'intuition_overrides']
        if intuitionOverrides is not None:
            self._intuitionOverrides[b'loopShell'] = intuitionOverrides.readString(b'loopShell', self.loopShell)
            self._intuitionOverrides[b'loopShellLast'] = intuitionOverrides.readString(b'loopShellLast', self.loopShellLast)
            self._intuitionOverrides[b'loopShellLastDt'] = intuitionOverrides.readFloat(b'loopShellLastDt', self.shellDtLast)
            self._intuitionOverrides[b'startLong'] = intuitionOverrides.readString(b'startLong', self.startLong)
        return

    def create(self):
        return BarrelReload(self)

    def createIntuitionReload(self):
        descr = copy(self)
        descr.duration = self._intuitionOverrides[b'duration']
        descr.loopShell = self._intuitionOverrides[b'loopShell']
        descr.loopShellLast = self._intuitionOverrides[b'loopShellLast']
        descr.shellDtLast = self._intuitionOverrides[b'loopShellLastDt']
        descr.startLong = self._intuitionOverrides[b'startLong']
        return descr.create()


class _AutoReloadDesc(_ReloadDesc):
    __slots__ = (b'duration', b'soundEvent', b'reloadStart', b'autoLoaderFull', b'lastShellAlert', b'shotFail', b'clipShellLoad', b'clipShellLoadT', b'ammoLow', b'caliber', b'almostComplete', b'almostCompleteT', b'effectType')

    def __init__(self, dataSection, eType):
        super(_AutoReloadDesc, self).__init__()
        self.duration = dataSection.readFloat(b'duration', 0.5) / 1000.0
        self.duration = max(self.duration, 0.5)
        self.soundEvent = dataSection.readString(b'sound', b'')
        self.reloadStart = dataSection.readString(b'reloadStart', b'')
        self.autoLoaderFull = dataSection.readString(b'autoLoaderFull', b'')
        self.lastShellAlert = dataSection.readString(b'lastShellAlert', b'')
        self.ammoLow = dataSection.readString(b'ammoLow', b'')
        self.caliber = dataSection.readString(b'caliber', b'')
        self.clipShellLoad = dataSection.readString(b'clipShellLoad', b'')
        self.clipShellLoadT = dataSection.readFloat(b'clipShellLoadDuration', 2000) / 1000.0
        self.clipShellLoadT = max(self.clipShellLoadT, 0.5)
        self.almostComplete = dataSection.readString(b'almostComplete', b'')
        self.almostCompleteT = dataSection.readFloat(b'almostCompleteDuration', 5000) / 1000.0
        self.almostCompleteT = max(self.almostCompleteT, 0.5)
        self.shotFail = dataSection.readString(b'shotFail', b'')
        self.effectType = eType
        intuitionOverrides = dataSection[b'intuition_overrides']
        if intuitionOverrides is not None:
            self._intuitionOverrides[b'reloadStart'] = intuitionOverrides.readString(b'reloadStart', self.reloadStart)
        return

    def create(self):
        return AutoReload(self)

    def createIntuitionReload(self):
        descr = copy(self)
        descr.reloadStart = self._intuitionOverrides[b'reloadStart']
        return AutoReload(descr)


class _ExtraShotClipReloadDesc(_BarrelReloadDesc):
    __slots__ = (b'extraShellStart', b'extraShellFinish', b'extraShellDtLast', b'extraShellduration', b'extraShellCancel', b'extraShellStopUtility')

    def __init__(self, dataSection, eType, parentSection):
        barrelSection = dataSection.readString(b'barrel_reload', b'')
        barrelSection = parentSection[barrelSection]
        super(_ExtraShotClipReloadDesc, self).__init__(barrelSection, eType)
        self.extraShellStart = dataSection.readString(b'extraShellStart', b'')
        self.extraShellFinish = dataSection.readString(b'extraShellFinish', b'')
        self.extraShellDtLast = dataSection.readFloat(b'extraShellFinishDt', 0.5)
        self.extraShellduration = dataSection.readFloat(b'extraShellduration', 0.5) / 1000.0
        self.extraShellCancel = dataSection.readString(b'extraShellCancel', b'')
        self.extraShellStopUtility = dataSection.readString(b'extraShellStopUtility', b'')
        return

    def create(self):
        return ExtraShotClipReload(self)


class _ChargeableBurstReloadDesc(_SimpleReloadDesc):
    __slots__ = (b'burstOneShellOffset', b'burstOneShell', b'burstLastShellOffset', b'burstLastShell', b'burstReady', b'nextBurstShellLoadingOffset', b'nextBurstShellLoading', b'nextBurstShellLoadedOffset', b'nextBurstShellLoaded')

    def __init__(self, dataSection, eType):
        super(_ChargeableBurstReloadDesc, self).__init__(dataSection, eType)
        self.burstReady = dataSection.readString(b'burstReady', b'')
        self.burstOneShellOffset = dataSection.readFloat(b'burstOneShellOffset', 0.0) / 1000.0
        self.burstOneShell = dataSection.readString(b'burstOneShell', b'')
        self.burstLastShellOffset = dataSection.readFloat(b'burstLastShellOffset', 0.0) / 1000.0
        self.burstLastShell = dataSection.readString(b'burstLastShell', b'')
        self.nextBurstShellLoadingOffset = dataSection.readFloat(b'nextBurstShellLoadingOffset', 0.0) / 1000.0
        self.nextBurstShellLoading = dataSection.readString(b'nextBurstShellLoading', b'')
        self.nextBurstShellLoadedOffset = dataSection.readFloat(b'nextBurstShellLoadedOffset', 0.0) / 1000.0
        self.nextBurstShellLoaded = dataSection.readString(b'nextBurstShellLoaded', b'')
        return

    def create(self):
        return ChargeableBurstReload(self)

    def createIntuitionReload(self):
        decr = copy(self)
        decr.duration = self._intuitionOverrides.get(b'duration', self.duration)
        decr.soundEvent = self._intuitionOverrides.get(b'sound', self.soundEvent)
        return SimpleReload(decr)


class _StationaryReloadDesc(_BarrelReloadDesc):

    def __init__(self, dataSection, eType, parentSection):
        barrelSection = dataSection.readString(b'barrel_reload', b'')
        barrelSection = parentSection[barrelSection]
        super(_StationaryReloadDesc, self).__init__(barrelSection, eType)
        return

    def create(self):
        return StationaryReload(self)


def effectFromSection(section, parentSection):
    eType = section.readString(b'type', b'')
    return _createReloadEffectDesc(eType, section, parentSection)


def isReplayPlayingWithTimeWarp():
    import BattleReplay
    replayCtrl = BattleReplay.g_replayCtrl
    return replayCtrl.isPlaying and replayCtrl.isTimeWarpInProgress


def playByName(soundName):
    if isReplayPlayingWithTimeWarp():
        return
    SoundGroups.g_instance.playSound2D(soundName)
    return


def playByInstance(soundInstance):
    if isReplayPlayingWithTimeWarp():
        return
    soundInstance.play()
    return


class _GunReload(CallbackDelayer):
    __slots__ = (b'_desc',)

    def __init__(self, effectDesc):
        super(_GunReload, self).__init__()
        self._desc = effectDesc
        return

    def getEffectType(self):
        return self._desc.effectType

    def onAmmoStatesInfoUpdate(self, ammoStatesInfo):
        return

    def stopSoundEffect(self):
        return

    def calculateReloadFlags(self, reloadInProgress, timeLeft, baseTime, clipCapacity, ammoStatesInfo):
        return self._calculateReloadFlags(reloadInProgress, timeLeft, baseTime, clipCapacity, ammoStatesInfo)

    @classmethod
    def _calculateReloadFlags(cls, reloadInProgress, timeLeft, baseTime, _, __):
        return (True, fabs(timeLeft - baseTime) < 0.001 and not reloadInProgress)

    def _checkAndPlayGunRammerEffect(self, reloadTime):
        if _needGunRammerEffect():
            timeToPlayEffect = reloadTime - GUN_RAMMER_TIME
            if timeToPlayEffect > 0:
                self.delayCallback(timeToPlayEffect, _playGunRammerEffect)
            else:
                _logger.warning(b'Reload time(%s) is less than gun rammer effect time(GUN_RAMMER_TIME-%s)', reloadTime, GUN_RAMMER_TIME)
        return

    def _stopGunRammerEffect(self):
        self.stopCallback(_playGunRammerEffect)
        return


class SimpleReload(_GunReload):

    def __init__(self, effectDesc):
        _GunReload.__init__(self, effectDesc)
        self._sound = None
        self._startLoopT = 0.0
        return

    def __del__(self):
        if self._sound is not None:
            self._sound.stop()
            self._sound = None
        CallbackDelayer.destroy(self)
        return

    def start(self, shellReloadTime, alert, shellCount, reloadShellCount, shellID, reloadStart, clipCapacity, ammoStatesInfo):
        if gEffectsDisabled():
            return
        else:
            time = max(shellReloadTime - self._desc.duration, 0.0)
            if self._sound is None:
                self._sound = SoundGroups.g_instance.getSound2D(self._desc.soundEvent)
            if not reloadStart and self._sound.isPlaying and time == 0.0:
                return
            self._sound.stop()
            self._checkAndPlayGunRammerEffect(shellReloadTime)
            self.delayCallback(time, self.__playSound)
            return

    def stop(self):
        if self._sound is not None:
            self._sound.stop()
            self._sound = None
        self.stopCallback(self.__playSound)
        self._stopGunRammerEffect()
        return

    def reloadEnd(self):
        self.stopCallback(self.__playSound)
        return

    def onClipLoad(self, timeLeft, shellsInClip, lastShell, canBeFull):
        return

    def updateReloadTime(self, timeLeft, shellCount, lastShell, canBeFull):
        return

    def shotFail(self):
        return

    def __playSound(self):
        if self._sound is not None:
            self._sound.stop()
            if isReplayPlayingWithTimeWarp():
                return
            self._sound.play()
        return


class BarrelReload(SimpleReload):

    def __init__(self, effectDesc):
        SimpleReload.__init__(self, effectDesc)
        self.__reloadSequence = LoopSequence(self._desc)
        self._startLongSound = None
        return

    def __del__(self):
        self.stop()
        SimpleReload.__del__(self)
        return

    def start(self, shellReloadTime, alert, shellCount, reloadShellCount, shellID, reloadStart, clipCapacity, ammoStatesInfo):
        if gEffectsDisabled():
            return
        else:
            SoundGroups.g_instance.setSwitch(b'SWITCH_ext_rld_automat_caliber', self._desc.caliber)
            currentTime = BigWorld.time()
            if shellCount == 0:
                self.stopCallback(self._startOneShoot)
                self.__reloadSequence.schedule(shellReloadTime, reloadShellCount)
                self._checkAndPlayGunRammerEffect(shellReloadTime)
                if reloadStart and shellReloadTime > self._desc.duration:
                    if self._startLongSound is not None:
                        self._startLongSound.stop()
                    self._startLongSound = SoundGroups.g_instance.getSound2D(self._desc.startLong)
                    self.__playStartLongSound()
                    if BARREL_DEBUG_ENABLED:
                        LOG_DEBUG((b'!!! Play Long  = {0} {1}').format(currentTime, self._desc.startLong))
                if alert:
                    playByName(self._desc.ammoLow)
                    if BARREL_DEBUG_ENABLED:
                        LOG_DEBUG((b'!!! Play Ammo Low  = {0} {1}').format(currentTime, self._desc.ammoLow))
            elif shellCount == 1 and clipCapacity > 2:
                if BARREL_DEBUG_ENABLED:
                    LOG_DEBUG((b'!!! Play Alert  = {0} {1}').format(currentTime, self._desc.lastShellAlert))
                playByName(self._desc.lastShellAlert)
            time = shellReloadTime - self._desc.shellDuration
            self.delayCallback(time, self._startOneShoot, currentTime + time)
            return

    def stop(self):
        if BARREL_DEBUG_ENABLED:
            LOG_DEBUG((b'!!! Stop Loop = {0}').format(self._desc.stopLoop))
        self.stopCallback(self._startOneShoot)
        self._stopGunRammerEffect()
        self.__reloadSequence.stop()
        return

    def reloadEnd(self):
        self.stop()
        return

    def onClipLoad(self, timeLeft, shellsInClip, lastShell, canBeFull):
        return

    def updateReloadTime(self, timeLeft, shellCount, lastShell, canBeFull):
        return

    def shotFail(self):
        return

    def _startOneShoot(self, invokeTime):
        if fabs(invokeTime - BigWorld.time()) < 0.1:
            if BARREL_DEBUG_ENABLED:
                LOG_DEBUG((b'!!!{0} Play One Shoot = {1}').format(BigWorld.time(), self._desc.soundEvent))
            playByName(self._desc.soundEvent)
        return

    def __playStartLongSound(self):
        if self._startLongSound is not None:
            self._startLongSound.stop()
            if isReplayPlayingWithTimeWarp():
                return
            self._startLongSound.play()
        return


class LoopSequence(CallbackDelayer):

    def __init__(self, desc):
        CallbackDelayer.__init__(self)
        self.lastShell = desc.loopShellLast
        self.shellTLast = desc.shellDtLast
        self.duration = desc.duration
        self.alignShellTime = 0.0
        self.__startLoop = desc.startLoop
        self.__stopLoop = desc.stopLoop
        self.__shell = desc.loopShell
        self.__shellT = desc.shellDt
        self.__sequence = []
        self.__inProgress = False
        return

    def __del__(self):
        self.stop()
        CallbackDelayer.destroy(self)
        return

    def schedule(self, reloadD, shellCount):
        self.stop()
        time = BigWorld.time()
        if BARREL_DEBUG_ENABLED:
            LOG_DEBUG((b'LoopSequence::schedule time = {0} end time = {1} duration = {2}').format(BigWorld.time(), time + reloadD, reloadD))
        loopDuration = self.duration
        if reloadD < self.duration:
            loopDuration = reloadD
            startLoopD = 0.0
            self.__inProgress = True
        else:
            startLoopD = reloadD - self.duration
            self.__inProgress = False
        self.__sequence = self.__generateTimeLine(startLoopD, loopDuration, shellCount)
        if BARREL_DEBUG_ENABLED:
            for item in self.__sequence:
                LOG_DEBUG((b'LoopSequence::schedule dt = {0} name = {1}').format(item[0], item[1]))

        self.__start()
        return

    def stop(self):
        self.stopCallback(self.__startCallback)
        if self.__inProgress:
            playByName(self.__stopLoop)
        self.__inProgress = False
        self.__sequence = []
        return

    def isPlaying(self):
        return self.__inProgress

    def __start(self):
        if self.__sequence:
            callTime, _ = self.__sequence[0]
            dt = max(callTime - BigWorld.time(), 0.0)
            self.delayCallback(dt, self.__startCallback)
        return

    def __startCallback(self):
        self.__inProgress = True
        if not self.__sequence:
            return
        else:
            invokeTime, name = self.__sequence.pop(0)
            if fabs(invokeTime - BigWorld.time()) < 0.1 or not self.__sequence:
                if BARREL_DEBUG_ENABLED:
                    LOG_DEBUG((b'LoopSequence::__startCallback time = {0} {1}').format(BigWorld.time(), name))
                playByName(name)
            if self.__sequence:
                callTime, _ = self.__sequence[0]
                return max(callTime - BigWorld.time(), 0.0)
            self.__inProgress = False
            return

    def __generateTimeLine(self, loopStartDT, loopDuration, count):
        time = BigWorld.time()
        timeLine = []
        if not self.__inProgress and not self.alignShellTime:
            time += loopStartDT
            timeLine += [(time, self.__startLoop)]
        lastDt = loopDuration - self.shellTLast
        padding = max(0.0, self.alignShellTime - self.shellTLast)
        if lastDt <= 0.0:
            timeLine += [(time, self.lastShell)] * count
            timeLine.append((time + loopDuration, self.__stopLoop))
        else:
            if count > 1:
                dt = (lastDt - padding) / (count - 1)
                time += self.alignShellTime
                for i in range(0, count - 1):
                    timeLine.append((time, self.__shell))
                    if self.alignShellTime and i == count - 2:
                        timeLine.append((time, self.__startLoop))
                    time += dt

                time -= self.alignShellTime
                timeLine.append((time + padding, self.lastShell))
            elif self.alignShellTime:
                timeLine.append((time, self.__startLoop))
            time += lastDt
            timeLine.append((time, self.lastShell))
            timeLine.append((time + self.shellTLast, self.__stopLoop))
        return timeLine


class AutoReload(_GunReload):

    def __init__(self, effectDesc):
        _GunReload.__init__(self, effectDesc)
        self._sound = None
        self._almostCompleteSnd = None
        self._startLoopT = 0.0
        return

    def __del__(self):
        if self._sound is not None:
            self._sound.stop()
            self._sound = None
        CallbackDelayer.destroy(self)
        return

    def start(self, shellReloadTime, alert, shellCount, reloadShellCount, shellID, reloadStart, _, __):
        if gEffectsDisabled():
            return
        else:
            if BARREL_DEBUG_ENABLED:
                LOG_DEBUG((b'AutoReload::start time = {0} {1} {2} {3} {4} {5} {6} ').format(BigWorld.time(), shellReloadTime, alert, shellCount, reloadShellCount, shellID, reloadStart))
            SoundGroups.g_instance.setSwitch(_CALIBER_RELOAD_SOUND_SWITCH, self._desc.caliber)
            self.stopCallback(self.__onShellInTheBarrel)
            self._almostCompleteSnd = None
            if self._sound is None:
                self._sound = SoundGroups.g_instance.getSound2D(self._desc.soundEvent)
            else:
                self._sound.stop()
            if reloadStart:
                if shellCount == 0:
                    playByName(self._desc.reloadStart)
                    if alert:
                        playByName(self._desc.ammoLow)
            time = max(shellReloadTime - self._desc.duration, 0.0)
            self.delayCallback(time, self.__onShellInTheBarrel, shellCount, reloadShellCount, BigWorld.time() + time)
            self._checkAndPlayGunRammerEffect(shellReloadTime)
            return

    def stop(self):
        if self._sound is not None:
            self._sound.stop()
            self._sound = None
        self.stopCallback(self.__onShellInTheBarrel)
        self.stopCallback(self.__onClipShellLoad)
        self.stopCallback(self.__onAlmostComplete)
        self.stopCallback(self.__onLoadComplete)
        self._stopGunRammerEffect()
        self._almostCompleteSnd = None
        return

    def reloadEnd(self):
        self.stopCallback(self.__onShellInTheBarrel)
        return

    def onClipLoad(self, timeLeft, shellCount, lastShell, canBeFull):
        if BARREL_DEBUG_ENABLED:
            LOG_DEBUG((b'AutoReload::onClipLoad time = {0} {1} {2} {3}').format(BigWorld.time(), timeLeft, shellCount, lastShell))
        self.stopCallback(self.__onAlmostComplete)
        self.stopCallback(self.__onLoadComplete)
        self.stopCallback(self.__onClipShellLoad)
        self.updateReloadTime(timeLeft, shellCount, lastShell, canBeFull)
        return

    def updateReloadTime(self, timeLeft, shellCount, lastShell, canBeFull):
        if shellCount > 0 and not lastShell:
            time = max(timeLeft - self._desc.clipShellLoadT, 0.0)
            self.delayCallback(time, self.__onClipShellLoad, BigWorld.time() + time)
        if lastShell and canBeFull:
            time = max(timeLeft - self._desc.almostCompleteT, 0.0)
            self.delayCallback(time, self.__onAlmostComplete, BigWorld.time() + time)
            self.delayCallback(timeLeft, self.__onLoadComplete, BigWorld.time() + timeLeft)
        return

    def shotFail(self):
        playByName(self._desc.shotFail)
        return

    def __onShellInTheBarrel(self, shellCount, reloadShellCount, time):
        if fabs(time - BigWorld.time()) > 0.1:
            return
        else:
            if self._sound is not None:
                self._sound.stop()
                if isReplayPlayingWithTimeWarp():
                    return
                self._sound.play()
                if shellCount == 1 and reloadShellCount > 2:
                    SoundGroups.g_instance.playSound2D(self._desc.lastShellAlert)
            return

    def __onClipShellLoad(self, time):
        if fabs(time - BigWorld.time()) > 0.1:
            return
        if BARREL_DEBUG_ENABLED:
            LOG_DEBUG(b'AutoReload::__onClipShellLoad')
        playByName(self._desc.clipShellLoad)
        return

    def __onAlmostComplete(self, time):
        if fabs(time - BigWorld.time()) > 0.1:
            return
        if BARREL_DEBUG_ENABLED:
            LOG_DEBUG(b'AutoReload::__onAlmostComplete')
        self._almostCompleteSnd = SoundGroups.g_instance.getSound2D(self._desc.almostComplete)
        self._almostCompleteSnd.play()
        return

    def __onLoadComplete(self, time):
        if fabs(time - BigWorld.time()) > 0.1:
            return
        if BARREL_DEBUG_ENABLED:
            LOG_DEBUG(b'AutoReload::__onLoadComplete')
        playByName(self._desc.autoLoaderFull)
        return


class DualGunReload(_GunReload):

    def __init__(self, effectDesc):
        _GunReload.__init__(self, effectDesc)
        self.__sound = None
        self.__ammoLowSound = None
        return

    def __del__(self):
        self.stop()
        CallbackDelayer.destroy(self)
        return

    def start(self, shellReloadTime, ammoLow, directTrigger=False):
        if gEffectsDisabled() or not directTrigger:
            return
        SoundGroups.g_instance.setSwitch(_CALIBER_RELOAD_SOUND_SWITCH, self._desc.caliber)
        self.stopCallback(self.__onReloadStart)
        timeToStart = shellReloadTime - self._desc.runTimeDelta
        if self.__sound is None:
            self.__sound = SoundGroups.g_instance.getSound2D(self._desc.soundEvent)
        if timeToStart > 0:
            self.delayCallback(timeToStart, self.__onReloadStart, BigWorld.time() + timeToStart)
        if ammoLow:
            timeToStart = shellReloadTime - self._desc.runTimeDeltaAmmoLow
            self.__ammoLowSound = SoundGroups.g_instance.getSound2D(self._desc.ammoLowSound)
            self.delayCallback(timeToStart, self.__onAmmoLow, BigWorld.time() + timeToStart)
        self._checkAndPlayGunRammerEffect(shellReloadTime)
        return

    def stopSoundEffect(self):
        for sound in (self.__sound, self.__ammoLowSound):
            if sound is not None:
                sound.stop()

        return

    def stop(self):
        self.stopSoundEffect()
        self.__sound = None
        self.__ammoLowSound = None
        self.stopCallback(self.__onReloadStart)
        self.stopCallback(self.__onAmmoLow)
        self._stopGunRammerEffect()
        return

    def reloadEnd(self):
        return

    def __onReloadStart(self, time):
        if fabs(time - BigWorld.time()) > 0.1:
            return
        else:
            if self.__sound is not None:
                if isReplayPlayingWithTimeWarp():
                    return
                self.__sound.play()
            return

    def __onAmmoLow(self, time):
        if fabs(time - BigWorld.time()) > 0.1:
            return
        else:
            if self.__ammoLowSound is not None:
                if isReplayPlayingWithTimeWarp():
                    return
                self.__ammoLowSound.play()
            return


class TwinGunReload(_GunReload):

    def __init__(self, effectDesc):
        _GunReload.__init__(self, effectDesc)
        self.__sound = None
        return

    def __del__(self):
        self.stop()
        CallbackDelayer.destroy(self)
        return

    def start(self, shellReloadTime, isTwinShot=False):
        if gEffectsDisabled():
            return
        SoundGroups.g_instance.setSwitch(_CALIBER_RELOAD_SOUND_SWITCH, self._desc.caliber)
        self.stopCallback(self.__onReloadStart)
        soundEvent = self._desc.soundEvent
        runTimeDelta = self._desc.runTimeDeltaOneGun
        if isTwinShot:
            soundEvent = self._desc.twinGunSound
            runTimeDelta = self._desc.runTimeDeltaTwinGun
        timeToStart = shellReloadTime - runTimeDelta
        if timeToStart > 0:
            self.__sound = SoundGroups.g_instance.getSound2D(soundEvent)
            self.delayCallback(timeToStart, self.__onReloadStart, BigWorld.time() + timeToStart)
        return

    def stop(self):
        if self.__sound is not None:
            self.__sound.stop()
            self.__sound = None
        self.stopCallback(self.__onReloadStart)
        return

    def reloadEnd(self):
        return

    def __onReloadStart(self, time):
        if fabs(time - BigWorld.time()) > 0.1 or self.__sound is None:
            return
        playByInstance(self.__sound)
        return


class ExtraShotClipReload(SimpleReload):

    def __init__(self, effectDesc):
        SimpleReload.__init__(self, effectDesc)
        self.__reloadSequence = LoopSequence(self._desc)
        self._startLongSound = SoundGroups.g_instance.getSound2D(self._desc.startLong)
        self._extraStartSound = SoundGroups.g_instance.getSound2D(self._desc.extraShellStart)
        return

    def __del__(self):
        self.stop()
        SimpleReload.__del__(self)
        return

    def start(self, shellReloadTime, alert, shellCount, reloadShellCount, shellID, reloadStart, clipCapacity, ammoStatesInfo):
        if gEffectsDisabled():
            return
        extraShotReloadState = ammoStatesInfo.extraShotReloadState
        SoundGroups.g_instance.setSwitch(b'SWITCH_ext_rld_automat_caliber', self._desc.caliber)
        currentTime = BigWorld.time()
        if shellCount == 1:
            if extraShotReloadState == ExtraShotClipStates.NONE:
                playByName(self._desc.lastShellAlert)
                time = shellReloadTime - self._desc.shellDuration
                self.delayCallback(time, self.__startOneShoot, currentTime + time)
            else:
                reloadShellCount = max(reloadShellCount - 1, 0)
                self.__reloadLongSound(alert, reloadShellCount, reloadStart, shellReloadTime, extraShotReloadState, isClipFull=False)
        elif shellCount == 0:
            self.stopCallback(self.__startOneShoot)
            self.__reloadLongSound(alert, reloadShellCount, reloadStart, shellReloadTime, extraShotReloadState, isClipFull=True)
        else:
            time = shellReloadTime - self._desc.shellDuration
            self.delayCallback(time, self.__startOneShoot, currentTime + time)
        return

    def stop(self):
        self.reloadEnd()
        if self._extraStartSound is not None and self._extraStartSound.isPlaying:
            playByName(self._desc.extraShellStopUtility)
        return

    def reloadEnd(self):
        self.stopCallback(self.__startOneShoot)
        self._stopGunRammerEffect()
        self.__reloadSequence.stop()
        return

    @classmethod
    def _calculateReloadFlags(cls, reloadInProgress, _, __, ___, ammoStatesInfo):
        extraShotReloadState = ammoStatesInfo.extraShotReloadState
        reloadFromStart = extraShotReloadState and not reloadInProgress
        reloadInProgress = extraShotReloadState & ExtraShotClipStates.FULL_RELOAD_WITH_EXTRA_TIME
        return (reloadInProgress, reloadFromStart)

    def __startOneShoot(self, invokeTime):
        if fabs(invokeTime - BigWorld.time()) < 0.1:
            playByName(self._desc.soundEvent)
        return

    def __reloadLongSound(self, alert, reloadShellCount, reloadStart, shellReloadTime, extraReloadState, isClipFull):
        if isClipFull:
            self.__reloadSequence.lastShell = self._desc.loopShellLast
            self.__reloadSequence.shellTLast = self._desc.shellDtLast
            self.__reloadSequence.duration = self._desc.duration
        else:
            self.__reloadSequence.lastShell = self._desc.extraShellFinish
            self.__reloadSequence.shellTLast = self._desc.extraShellDtLast
            self.__reloadSequence.duration = self._desc.extraShellduration
        self.__reloadSequence.schedule(shellReloadTime, reloadShellCount)
        self._checkAndPlayGunRammerEffect(shellReloadTime)
        if isClipFull and extraReloadState == ExtraShotClipStates.FULL_RELOAD_WITH_EXTRA_TIME | ExtraShotClipStates.EXTRA_FULL_RELOAD:
            playByName(self._desc.extraShellCancel)
        if reloadStart and shellReloadTime > self._desc.duration:
            self.__playStartLongSound(isClipFull=isClipFull)
        if alert:
            playByName(self._desc.ammoLow)
        return

    def __playStartLongSound(self, isClipFull):
        if not isClipFull:
            playByInstance(self._extraStartSound)
        if self._startLongSound is not None:
            self._startLongSound.stop()
        playByInstance(self._startLongSound)
        return


class ChargeableBurstReload(SimpleReload):

    def __init__(self, effectDesc):
        SimpleReload.__init__(self, effectDesc)
        self.__isBurstActive = False
        self.__isBurstTriggered = False
        self.__isBetweenBurstShots = False
        self.__isBurstShotTriggered = False
        self.__shellReloadTime = 0.0
        self.__reloadShellCount = 0
        self.__soundBurstReady = None
        self.__soundBurstOneShell = None
        self.__soundBurstLastShell = None
        self.__soundNextBurstShellLoading = None
        self.__soundNextBurstShellLoaded = None
        return

    def __del__(self):
        self.stop()
        SimpleReload.__del__(self)
        return

    def start(self, shellReloadTime, alert, shellCount, reloadShellCount, shellID, reloadStart, clipCapacity, ammoStatesInfo):
        if gEffectsDisabled():
            return
        self.__reloadShellCount = reloadShellCount
        hasCallback = self.hasDelayedCallback(self.__playOneShellSound) or self.hasDelayedCallback(self.__playLastShellSound)
        hasBurstShotCallback = self.hasDelayedCallback(self.__playNextShellLoadingSound) or self.hasDelayedCallback(self.__playNextShellLoadedSound)
        self.__stopCallbacks()
        self.__shellReloadTime = BigWorld.serverTime() + shellReloadTime
        isBurstActive = self.__isBurstActive or self.__isBurstTriggered
        if isBurstActive and (self.__isBetweenBurstShots or self.__isBurstShotTriggered or hasBurstShotCallback):
            self.__playDelayedReloadBetweenBurstSounds()
            self.__isBurstShotTriggered = False
        elif isBurstActive or hasCallback:
            self.__playDelayedBurstSounds()
            self.__isBurstTriggered = False
        else:
            SimpleReload.start(self, shellReloadTime, alert, shellCount, reloadShellCount, shellID, reloadStart, clipCapacity, ammoStatesInfo)
        return

    def stop(self):
        SimpleReload.stop(self)
        for sound in (self.__soundBurstReady, self.__soundBurstOneShell, self.__soundBurstLastShell,
         self.__soundNextBurstShellLoading, self.__soundNextBurstShellLoaded):
            if sound is not None:
                sound.stop()

        self.__stopCallbacks()
        return

    def reloadEnd(self):
        SimpleReload.reloadEnd(self)
        self.__stopCallbacks()
        return

    def onAmmoStatesInfoUpdate(self, ammoStatesInfo):
        burstState = ammoStatesInfo.chargeableBurstAmmoState
        self.__updateBurstActive(burstState is not None and burstState.isBurstActive)
        shots, count = (burstState.shots, burstState.burstCount) if burstState is not None else (0, 0)
        self.__updateBurstShoot(shots, count)
        return

    def __updateBurstActive(self, isActive):
        if self.__isBurstActive != isActive:
            self.__isBurstActive = isActive
        else:
            return
        if not isActive:
            return
        self.__soundBurstReady = SoundGroups.g_instance.getSound2D(self._desc.burstReady)
        self.__soundBurstReady.play()
        if self.__shellReloadTime > BigWorld.serverTime():
            SimpleReload.stop(self)
            self.__playDelayedBurstSounds()
        else:
            self.__isBurstTriggered = True
        return

    def __updateBurstShoot(self, burstShots, burstCount):
        isBetweenBurstShots = 0 < burstShots < burstCount
        if self.__isBetweenBurstShots != isBetweenBurstShots:
            self.__isBetweenBurstShots = isBetweenBurstShots
        else:
            return
        if not isBetweenBurstShots:
            return
        if self.__shellReloadTime > BigWorld.serverTime():
            SimpleReload.stop(self)
            self.__playDelayedReloadBetweenBurstSounds()
        else:
            self.__isBurstShotTriggered = True
        return

    def __playDelayedReloadBetweenBurstSounds(self):
        if isReplayPlayingWithTimeWarp():
            return
        shellReloadTime = self.__shellReloadTime - BigWorld.serverTime()
        if shellReloadTime > 0.0 and self.__reloadShellCount > 1:
            nextShellLoadingTime = shellReloadTime - self._desc.nextBurstShellLoadingOffset
            if nextShellLoadingTime > 0.0:
                self.delayCallback(nextShellLoadingTime, self.__playNextShellLoadingSound)
            nextShellLoadedTime = shellReloadTime - self._desc.nextBurstShellLoadedOffset
            if nextShellLoadedTime > 0.0:
                self.delayCallback(nextShellLoadedTime, self.__playNextShellLoadedSound)
        return

    def __playDelayedBurstSounds(self):
        if isReplayPlayingWithTimeWarp():
            return
        shellReloadTime = self.__shellReloadTime - BigWorld.serverTime()
        if shellReloadTime > 0.0:
            self._checkAndPlayGunRammerEffect(shellReloadTime)
            lastShellReloadTime = shellReloadTime - self._desc.burstLastShellOffset
            if lastShellReloadTime > 0.0:
                self.delayCallback(lastShellReloadTime, self.__playLastShellSound)
            oneShellReloadTime = shellReloadTime - self._desc.burstOneShellOffset
            if oneShellReloadTime > 0.0 and self.__reloadShellCount > 1:
                self.delayCallback(oneShellReloadTime, self.__playOneShellSound)
        return

    def __playOneShellSound(self):
        playByName(self._desc.burstOneShell)
        return

    def __playLastShellSound(self):
        playByName(self._desc.burstLastShell)
        return

    def __playNextShellLoadingSound(self):
        playByName(self._desc.nextBurstShellLoading)
        return

    def __playNextShellLoadedSound(self):
        playByName(self._desc.nextBurstShellLoaded)
        return

    def __stopCallbacks(self):
        self.__shellReloadTime = 0.0
        self.stopCallback(self.__playOneShellSound)
        self.stopCallback(self.__playLastShellSound)
        self.stopCallback(self.__playNextShellLoadingSound)
        self.stopCallback(self.__playNextShellLoadedSound)
        return


class StationaryReload(SimpleReload):
    __sessionProvider = dependency.descriptor(IBattleSessionProvider)

    def __init__(self, effectDesc):
        SimpleReload.__init__(self, effectDesc)
        self.reloadSequence = LoopSequence(self._desc)
        self.startLongSound = None
        return

    def __del__(self):
        self.stop()
        SimpleReload.__del__(self)
        return

    def start(self, shellReloadTime, alert, shellCount, reloadShellCount, shellID, reloadStart, clipCapacity, ammoStatesInfo):
        if gEffectsDisabled():
            return
        else:
            stationaryReloadState = self._getStationaryReloadState(ammoStatesInfo)
            SoundGroups.g_instance.setSwitch(b'SWITCH_ext_rld_automat_caliber', self._desc.caliber)
            currentTime = BigWorld.time()
            if stationaryReloadState == STATIONARY_RELOAD_STATE.RELOADING:
                reloadShellCount = clipCapacity - shellCount
                if reloadShellCount:
                    self.stopCallback(self._startOneShoot)
                    self._checkAndPlayGunRammerEffect(shellReloadTime)
                    avgShellTime = shellReloadTime / reloadShellCount
                    self.reloadSequence.duration = shellReloadTime - 0.001
                    self.reloadSequence.alignShellTime = avgShellTime
                    if reloadStart or not (reloadShellCount == 1 and self.reloadSequence.isPlaying()):
                        self.reloadSequence.schedule(shellReloadTime, reloadShellCount)
                    if reloadStart and shellReloadTime > self._desc.duration:
                        if self.startLongSound is not None:
                            self.startLongSound.stop()
                        self.startLongSound = SoundGroups.g_instance.getSound2D(self._desc.startLong)
                        self.__playStartLongSound()
                    if alert:
                        playByName(self._desc.ammoLow)
            elif stationaryReloadState == STATIONARY_RELOAD_STATE.FINISHING:
                self.stop()
            elif stationaryReloadState == STATIONARY_RELOAD_STATE.IDLE and not reloadStart:
                if shellCount == 1 and clipCapacity > 2:
                    playByName(self._desc.lastShellAlert)
                time = shellReloadTime - self._desc.shellDuration
                self.delayCallback(time, self._startOneShoot, currentTime + time)
            return

    def stop(self):
        self.stopCallback(self._startOneShoot)
        self._stopGunRammerEffect()
        self.reloadSequence.stop()
        return

    def reloadEnd(self):
        self.stop()
        return

    @classmethod
    def _getStationaryReloadState(cls, ammoStatesInfo):
        ammoState = ammoStatesInfo.stationaryReloadAmmoState
        if ammoState is not None:
            return ammoState.stationaryReloadState
        else:
            return STATIONARY_RELOAD_STATE.IDLE

    @classmethod
    def _calculateReloadFlags(cls, reloadInProgress, timeLeft, baseTime, clipCapacity, ammoStatesInfo):
        ammoCtrl = cls.__sessionProvider.shared.ammo
        currentShellCD = ammoCtrl.getCurrentShellCD()
        shellsToLoad = clipCapacity - ammoCtrl.getShells(currentShellCD)[1]
        misAlignment = timeLeft - baseTime / clipCapacity * shellsToLoad
        inProgress = cls._getStationaryReloadState(ammoStatesInfo) == STATIONARY_RELOAD_STATE.RELOADING
        return (inProgress, fabs(misAlignment) < 0.001 and not reloadInProgress)

    def _startOneShoot(self, invokeTime):
        if fabs(invokeTime - BigWorld.time()) < 0.1:
            playByName(self._desc.soundEvent)
        return

    def __playStartLongSound(self):
        if self.startLongSound is not None:
            self.startLongSound.stop()
            if isReplayPlayingWithTimeWarp():
                return
            self.startLongSound.play()
        return


class ReloadEffectStrategy(object):
    __sessionProvider = dependency.descriptor(IBattleSessionProvider)
    __slots__ = (b'__gunReloadEffect', b'__intuitionReloadEffect', b'__currentReloadEffect', b'__reloadInProgress')

    def __init__(self, gunReloadEffectDesc):
        self.__gunReloadEffect = gunReloadEffectDesc.create()
        if gunReloadEffectDesc.hasUniqueIntuitionReload():
            self.__intuitionReloadEffect = gunReloadEffectDesc.createIntuitionReload()
        else:
            self.__intuitionReloadEffect = None
        self.__currentReloadEffect = self.__gunReloadEffect
        self.__reloadInProgress = False
        return

    def start(self, timeLeft, baseTime, clipCapacity, ammoStatesInfo, directTrigger=False):
        self.__reloadInProgress, reloadFromStart = self.__gunReloadEffect.calculateReloadFlags(self.__reloadInProgress, timeLeft, baseTime, clipCapacity, ammoStatesInfo)
        self.__reloadStartEffect(timeLeft, clipCapacity, reloadFromStart, ammoStatesInfo, directTrigger)
        return

    def stop(self):
        self.__reloadInProgress = False
        if self.__intuitionReloadEffect is not None:
            self.__intuitionReloadEffect.stop()
        self.__gunReloadEffect.stop()
        return

    def onClipLoad(self, timeLeft, shellsInClip, lastShell, canBeFull):
        if self.__currentReloadEffect is not None:
            self.__currentReloadEffect.onClipLoad(timeLeft, shellsInClip, lastShell, canBeFull)
        return

    def updateReloadTime(self, timeLeft, shellCount, lastShell, canBeFull):
        if self.__currentReloadEffect is not None:
            self.__currentReloadEffect.updateReloadTime(timeLeft, shellCount, lastShell, canBeFull)
        return

    def shotFail(self):
        if self.__currentReloadEffect is not None:
            self.__currentReloadEffect.shotFail()
        return

    def reloadEnd(self):
        self.__reloadInProgress = False
        if self.__currentReloadEffect is not None:
            self.__currentReloadEffect.reloadEnd()
        return

    def getGunReloadType(self):
        return self.__gunReloadEffect.getEffectType()

    def onAmmoStatesInfoUpdate(self, ammoStatesInfo):
        self.__gunReloadEffect.onAmmoStatesInfoUpdate(ammoStatesInfo)
        return

    def getRelloadEffect(self):
        ammoCtrl = self.__sessionProvider.shared.ammo
        isIntuition = ammoCtrl.getIntuitionReloadInProcess()
        if isIntuition and self.__intuitionReloadEffect is not None:
            relloadEffect = self.__intuitionReloadEffect
        else:
            relloadEffect = self.__gunReloadEffect
        return relloadEffect

    def __reloadStartEffect(self, timeLeft, clipCapacity, reloadFromStart, ammoStatesInfo, directTrigger=False):
        ammoCtrl = self.__sessionProvider.shared.ammo
        currentShellCD = ammoCtrl.getCurrentShellCD()
        shellCounts = ammoCtrl.getShells(currentShellCD)
        shellsQuantityLeft = ammoCtrl.getShellsQuantityLeft()
        reloadShellCount = clipCapacity
        relloadEffect = self.getRelloadEffect()
        if self.__currentReloadEffect != relloadEffect:
            self.__currentReloadEffect.stop()
        self.__currentReloadEffect = relloadEffect
        if relloadEffect is not None:
            ammoLow = False
            gunReloadType = self.getGunReloadType()
            if gunReloadType == ReloadEffectsType.CHARGEABLEBURST_RELOAD:
                reloadShellCount = shellCounts[0]
            elif clipCapacity > shellCounts[0]:
                ammoLow = True
                reloadShellCount = shellCounts[0]
            if gunReloadType == ReloadEffectsType.DUALGUN_RELOAD:
                if shellsQuantityLeft == 1:
                    ammoLow = True
                relloadEffect.start(timeLeft, ammoLow, directTrigger)
            elif gunReloadType == ReloadEffectsType.TWINGUN_RELOAD:
                relloadEffect.start(timeLeft, ammoStatesInfo.getShotsAmount() > 1)
            if gunReloadType == ReloadEffectsType.EXTRASHOTCLIP_RELOAD:
                relloadEffect.start(timeLeft, ammoLow, shellCounts[1], reloadShellCount, currentShellCD, reloadFromStart, clipCapacity, ammoStatesInfo)
            elif gunReloadType == ReloadEffectsType.STATIONARY_RELOAD:
                relloadEffect.start(timeLeft, ammoLow, shellCounts[1], reloadShellCount, currentShellCD, reloadFromStart, clipCapacity, ammoStatesInfo)
            else:
                relloadEffect.start(timeLeft, ammoLow, shellCounts[1], reloadShellCount, currentShellCD, reloadFromStart, clipCapacity, ammoStatesInfo)
        return


@dependency.replace_none_kwargs(sessionProvider=IBattleSessionProvider)
def _needGunRammerEffect(sessionProvider=None):
    if sessionProvider is not None:
        return sessionProvider.shared.optionalDevices.soundManager.needGunRammerEffect()
    else:
        return


def _playGunRammerEffect():
    SoundGroups.g_instance.playSound2D(GUN_RAMMER_EFFECT_NAME)
    return
