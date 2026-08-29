import logging, SoundGroups, BigWorld
from copy import copy
from math import fabs
from constants import DUAL_GUN
from helpers.CallbackDelayer import CallbackDelayer, CallbacksSetByID
from helpers import gEffectsDisabled, dependency
from debug_utils import LOG_DEBUG
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
    AUTO_SHOOT_CHANGE_SHELL_RELOAD = b'AutoShootChangeShellReload'
    AUTO_SHOOT_RELOAD = b'AutoShootGunReload'
    DUALGUN_AUTORELOAD = b'DualGunAutoReload'
    DUALGUN_BARREL = b'DualGunBarrelReload'


class ReloadType(object):
    ANY = 0
    CLIP = 1
    DUALGUN = 2


def _createReloadEffectDesc(eType, dataSection):
    if not dataSection.values():
        return
    else:
        reloadDescr = RELOAD_EFFECTS_DESCR_MAP.get(eType, None)
        if reloadDescr is not None:
            return reloadDescr(dataSection, eType)
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
    __slots__ = (b'ammoLowSound', b'soundEvent', b'runTimeDelta', b'runTimeDeltaAmmoLow', b'caliber')

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
        if self.duration < 0.5:
            self.duration = 0.5
        self.soundEvent = dataSection.readString(b'sound', b'')
        self.reloadStart = dataSection.readString(b'reloadStart', b'')
        self.autoLoaderFull = dataSection.readString(b'autoLoaderFull', b'')
        self.lastShellAlert = dataSection.readString(b'lastShellAlert', b'')
        self.ammoLow = dataSection.readString(b'ammoLow', b'')
        self.caliber = dataSection.readString(b'caliber', b'')
        self.clipShellLoad = dataSection.readString(b'clipShellLoad', b'')
        self.clipShellLoadT = dataSection.readFloat(b'clipShellLoadDuration', 2000) / 1000.0
        if self.clipShellLoadT < 0.5:
            self.clipShellLoadT = 0.5
        self.almostComplete = dataSection.readString(b'almostComplete', b'')
        self.almostCompleteT = dataSection.readFloat(b'almostCompleteDuration', 5000) / 1000.0
        if self.almostCompleteT < 0.5:
            self.almostCompleteT = 0.5
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


class _DualGunAutoReloadDesc(_ReloadDesc):

    def __init__(self, dataSection, eType):
        super(_DualGunAutoReloadDesc, self).__init__()
        self.dualGunDesc = _DualGunReloadDesc(dataSection, eType)
        self.autoReloadDesc = _AutoReloadDesc(dataSection, eType)
        self.dualGunDesc.soundEvent = dataSection.readString(b'dualGunSound', b'')
        self.autoReloadDesc.soundEvent = dataSection.readString(b'autoReloadSound', b'')
        self.effectType = eType
        return

    def create(self):
        return DualGunAutoReload(self)

    def createIntuitionReload(self):
        return self.autoReloadDesc.createIntuitionReload()


class _DualGunBarrelReloadDesc(_ReloadDesc):

    def __init__(self, dataSection, eType):
        super(_DualGunBarrelReloadDesc, self).__init__()
        self.dualGunDesc = _DualGunReloadDesc(dataSection, eType)
        self.barrelReloadDesc = _BarrelReloadDesc(dataSection, eType)
        self.dualGunDesc.soundEvent = dataSection.readString(b'dualGunSound', b'')
        self.barrelReloadDesc.soundEvent = dataSection.readString(b'barrelReloadSound', b'')
        self.effectType = eType
        return

    def create(self):
        return DualGunBarrelReload(self)

    def createIntuitionReload(self):
        return self.barrelReloadDesc.createIntuitionReload()


class _AutoShootChangeShellGunReloadDescr(_SimpleReloadDesc):
    __slots__ = (b'duration', b'soundEvent', b'effectType', b'startSoundEvent')

    def __init__(self, dataSection, eType):
        super(_AutoShootChangeShellGunReloadDescr, self).__init__(dataSection, eType)
        self.startSoundEvent = dataSection.readString(b'startSound', b'')
        return

    def create(self):
        return AutoShootChangeShellReload(self)

    def createIntuitionReload(self):
        decr = copy(self)
        decr.duration = self._intuitionOverrides.get(b'duration', self.duration)
        decr.soundEvent = self._intuitionOverrides.get(b'sound', self.soundEvent)
        return decr.create()


class _AutoShootGunReloadDescr(_SimpleReloadDesc):
    __slots__ = (b'clipReloadStart', b'clipReloadEnd', b'ammoLow', b'caliber', b'lastShell')

    def __init__(self, dataSection, eType):
        super(_AutoShootGunReloadDescr, self).__init__(dataSection, eType)
        self.clipReloadStart = dataSection.readString(b'clipReloadStart', b'')
        self.clipReloadEnd = dataSection.readString(b'clipReloadEnd', b'')
        self.ammoLow = dataSection.readString(b'ammoLow', b'')
        self.lastShell = dataSection.readString(b'lastShell', b'')
        self.caliber = dataSection.readString(b'caliber', b'')
        return

    def create(self):
        return AutoShootReload(self)

    def createIntuitionReload(self):
        decr = copy(self)
        decr.duration = self._intuitionOverrides.get(b'duration', self.duration)
        decr.clipReloadEnd = self._intuitionOverrides.get(b'sound', self.clipReloadEnd)
        return decr.create()


def effectFromSection(section):
    eType = section.readString(b'type', b'')
    return _createReloadEffectDesc(eType, section)


def playByName(soundName):
    import BattleReplay
    replayCtrl = BattleReplay.g_replayCtrl
    if replayCtrl.isPlaying and replayCtrl.isTimeWarpInProgress:
        return
    SoundGroups.g_instance.playSound2D(soundName)
    return


def _isReplayWarping():
    import BattleReplay
    replayCtrl = BattleReplay.g_replayCtrl
    return replayCtrl.isPlaying and replayCtrl.isTimeWarpInProgress


class _GunReload(CallbackDelayer):
    __slots__ = (b'_desc',)

    def __init__(self, effectDesc):
        super(_GunReload, self).__init__()
        self._desc = effectDesc
        return

    def getEffectType(self):
        return self._desc.effectType

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

    def start(self, shellReloadTime, alert, shellCount, reloadShellCount, shellID, reloadStart, clipCapacity):
        if gEffectsDisabled():
            return
        else:
            if self._sound is None:
                self._sound = SoundGroups.g_instance.getSound2D(self._desc.soundEvent)
            else:
                self._sound.stop()
            time = shellReloadTime - self._desc.duration
            if time < 0.0:
                time = 0.0
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

    def onFull(self):
        return

    def shotFail(self):
        return

    def __playSound(self):
        if self._sound is not None:
            self._sound.stop()
            import BattleReplay
            replayCtrl = BattleReplay.g_replayCtrl
            if replayCtrl.isPlaying and replayCtrl.isTimeWarpInProgress:
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

    def start(self, shellReloadTime, alert, shellCount, reloadShellCount, shellID, reloadStart, clipCapacity):
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

    def onFull(self):
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
            import BattleReplay
            replayCtrl = BattleReplay.g_replayCtrl
            if replayCtrl.isPlaying and replayCtrl.isTimeWarpInProgress:
                return
            self._startLongSound.play()
        return


class LoopSequence(CallbackDelayer):

    def __init__(self, desc):
        CallbackDelayer.__init__(self)
        self.__startLoop = desc.startLoop
        self.__stopLoop = desc.stopLoop
        self.__shell = desc.loopShell
        self.__lastShell = desc.loopShellLast
        self.__duration = desc.duration
        self.__shellT = desc.shellDt
        self.__shellTLast = desc.shellDtLast
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
        loopDuration = self.__duration
        if reloadD < self.__duration:
            loopDuration = reloadD
            startLoopD = 0.0
            self.__inProgress = True
        else:
            startLoopD = reloadD - self.__duration
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

    def __start(self):
        if self.__sequence:
            callTime, _ = self.__sequence[0]
            dt = callTime - BigWorld.time()
            if dt < 0.0:
                dt = 0.0
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
                dt = callTime - BigWorld.time()
                if dt < 0.0:
                    dt = 0.0
                return dt
            self.__inProgress = False
            return
            return

    def __generateTimeLine(self, loopStartDT, loopDuration, count):
        time = BigWorld.time()
        timeLine = []
        if not self.__inProgress:
            time += loopStartDT
            timeLine += [(time, self.__startLoop)]
        lastDt = loopDuration - self.__shellTLast
        if lastDt <= 0.0:
            timeLine += [(time, self.__lastShell)] * count
            timeLine.append((time + loopDuration, self.__stopLoop))
        else:
            if count > 1:
                dt = lastDt / (count - 1)
                for _ in xrange(0, count - 1):
                    timeLine.append((time, self.__shell))
                    time += dt

                timeLine.append((time, self.__lastShell))
            else:
                time += lastDt
                timeLine.append((time, self.__lastShell))
            timeLine.append((time + self.__shellTLast, self.__stopLoop))
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

    def start(self, shellReloadTime, alert, shellCount, reloadShellCount, shellID, reloadStart, clipCapacity):
        if gEffectsDisabled():
            return
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
                if self._desc.reloadStart:
                    playByName(self._desc.reloadStart)
                if alert and self._desc.ammoLow:
                    playByName(self._desc.ammoLow)
        time = shellReloadTime - self._desc.duration
        if time < 0.0:
            time = 0.0
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
        self.stopCallback(self.__onClipShellLoad)
        if self._desc.clipShellLoad:
            if shellCount > 0 and not lastShell:
                time = timeLeft - self._desc.clipShellLoadT
                if time < 0.0:
                    time = 0.0
                self.delayCallback(time, self.__onClipShellLoad, BigWorld.time() + time)
        if self._desc.almostComplete:
            if lastShell and canBeFull:
                time = timeLeft - self._desc.almostCompleteT
                if time < 0.0:
                    time = 0.0
                self.delayCallback(time, self.__onAlmostComplete, BigWorld.time() + time)
        return

    def onFull(self):
        if self._desc.autoLoaderFull:
            if BARREL_DEBUG_ENABLED:
                LOG_DEBUG(b'AutoReload::onFull')
            playByName(self._desc.autoLoaderFull)
        return

    def shotFail(self):
        if self._desc.shotFail:
            playByName(self._desc.shotFail)
        return

    def __onShellInTheBarrel(self, shellCount, reloadShellCount, time):
        if fabs(time - BigWorld.time()) > 0.1:
            return
        else:
            if self._sound is not None:
                self._sound.stop()
                import BattleReplay
                replayCtrl = BattleReplay.g_replayCtrl
                if replayCtrl.isPlaying and replayCtrl.isTimeWarpInProgress:
                    return
                self._sound.play()
                if shellCount == 1 and reloadShellCount > 2 and self._desc.lastShellAlert:
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


class DualGunReload(_GunReload):
    _CB_RELOAD = (0, 1)
    _CB_LAST = (2, 3)

    def __init__(self, effectDesc):
        _GunReload.__init__(self, effectDesc)
        self.__oneShellReloadSounds = [None, None]
        self.__oneShellLastSounds = [None, None]
        self.__gunSoundCallbacks = CallbacksSetByID()
        return

    def __del__(self):
        self.stop()
        self.__gunSoundCallbacks.clear()
        CallbackDelayer.destroy(self)
        return

    def start(self, shellReloadTime, ammoLow, directTrigger=False, gunIndex=DUAL_GUN.ACTIVE_GUN.LEFT):
        if gEffectsDisabled() or not directTrigger:
            return
        SoundGroups.g_instance.setSwitch(_CALIBER_RELOAD_SOUND_SWITCH, self._desc.caliber)
        timeToStart = shellReloadTime - self._desc.runTimeDelta
        self.__scheduleGunSound(gunIndex, self.__oneShellReloadSounds, self._CB_RELOAD[gunIndex], self._desc.soundEvent, self.__playOneshellReloadSound, timeToStart)
        if ammoLow and self._desc.ammoLowSound:
            timeToStartAmmoLow = shellReloadTime - self._desc.runTimeDeltaAmmoLow
            self.__scheduleGunSound(gunIndex, self.__oneShellLastSounds, self._CB_LAST[gunIndex], self._desc.ammoLowSound, self.__playOneshellLastSound, timeToStartAmmoLow)
        self._checkAndPlayGunRammerEffect(shellReloadTime)
        return

    def __scheduleGunSound(self, gunIndex, sounds, callbackId, soundEvent, playCallback, timeToStart):
        self.__gunSoundCallbacks.stopCallback(callbackId)
        if sounds[gunIndex] is not None:
            sounds[gunIndex].stop()
        sounds[gunIndex] = SoundGroups.g_instance.getSound2D(soundEvent)
        if timeToStart > 0:
            self.__gunSoundCallbacks.delayCallback(callbackId, timeToStart, playCallback, gunIndex, BigWorld.time() + timeToStart)
        else:
            playCallback(gunIndex, BigWorld.time())
        return

    def stopActiveSounds(self):
        for sounds in (self.__oneShellReloadSounds, self.__oneShellLastSounds):
            for gunIndex in (DUAL_GUN.ACTIVE_GUN.LEFT, DUAL_GUN.ACTIVE_GUN.RIGHT):
                if sounds[gunIndex] is not None:
                    sounds[gunIndex].stop()
                    sounds[gunIndex] = None

        self.__gunSoundCallbacks.clear()
        return

    def stop(self):
        self.stopActiveSounds()
        self._stopGunRammerEffect()
        return

    def reloadEnd(self):
        return

    def __playOneshellReloadSound(self, gunIndex, time):
        if fabs(time - BigWorld.time()) > 0.1:
            return
        else:
            oneShellReloadSound = self.__oneShellReloadSounds[gunIndex]
            if oneShellReloadSound is None or _isReplayWarping():
                return
            oneShellReloadSound.play()
            return

    def __playOneshellLastSound(self, gunIndex, time):
        if fabs(time - BigWorld.time()) > 0.1:
            return
        else:
            oneShellLastSound = self.__oneShellLastSounds[gunIndex]
            if oneShellLastSound is None or _isReplayWarping():
                return
            oneShellLastSound.play()
            return

    def onClipLoad(self, _, __, ___, ____):
        _logger.error(b'onClipLoad called for DualGun. You may need to change <reloadEffect>.')
        return

    def onFull(self):
        _logger.error(b'onFull called for DualGun. You may need to change <reloadEffect>.')
        return

    def shotFail(self):
        _logger.error(b'shotFail called for DualGun. You may need to change <reloadEffect>.')
        return


class _DualGunCompositeReload(_GunReload):

    def __init__(self, effectDesc, clipReloadEffect):
        super(_DualGunCompositeReload, self).__init__(effectDesc)
        self.__dualGunReload = DualGunReload(effectDesc.dualGunDesc)
        self.__clipReload = clipReloadEffect
        return

    def start(self, shellReloadTime, ammoLowMask, shellCount, reloadShellCount, shellID, reloadStart, clipCapacity, reloadType, gunIndex=DUAL_GUN.ACTIVE_GUN.LEFT):
        if reloadType in (ReloadType.DUALGUN, ReloadType.ANY):
            isAmmoLow = ammoLowMask & 1 << ReloadType.DUALGUN
            self.__dualGunReload.start(shellReloadTime, isAmmoLow, directTrigger=reloadType == ReloadType.DUALGUN, gunIndex=gunIndex)
        elif reloadType == ReloadType.CLIP:
            isAmmoLow = ammoLowMask & 1 << ReloadType.CLIP
            self.__clipReload.start(shellReloadTime, isAmmoLow, shellCount, reloadShellCount, shellID, reloadStart, clipCapacity)
        return

    def stopActiveDualGunSounds(self):
        self.__dualGunReload.stopActiveSounds()
        return

    def stop(self):
        self.__dualGunReload.stop()
        self.__clipReload.stop()
        return

    def reloadEnd(self):
        self.__clipReload.reloadEnd()
        return

    def onClipLoad(self, timeLeft, shellCount, lastShell, canBeFull):
        self.__clipReload.onClipLoad(timeLeft, shellCount, lastShell, canBeFull)
        return

    def onFull(self):
        self.__clipReload.onFull()
        return

    def shotFail(self):
        self.__clipReload.shotFail()
        return


class DualGunAutoReload(_DualGunCompositeReload):

    def __init__(self, effectDesc):
        super(DualGunAutoReload, self).__init__(effectDesc, AutoReload(effectDesc.autoReloadDesc))
        return


class DualGunBarrelReload(_DualGunCompositeReload):

    def __init__(self, effectDesc):
        super(DualGunBarrelReload, self).__init__(effectDesc, BarrelReload(effectDesc.barrelReloadDesc))
        return


class AutoShootChangeShellReload(_GunReload):

    def __init__(self, effectDesc):
        super(AutoShootChangeShellReload, self).__init__(effectDesc)
        self._startSound = None
        self._finishSound = None
        return

    def __del__(self):
        self.stop()
        CallbackDelayer.destroy(self)
        return

    def start(self, shellReloadTime, alert, shellCount, reloadShellCount, shellID, reloadStart, clipCapacity):
        if gEffectsDisabled():
            return
        self._finishSound = self._finishSound or SoundGroups.g_instance.getSound2D(self._desc.soundEvent)
        self._startSound = self._startSound or SoundGroups.g_instance.getSound2D(self._desc.startSoundEvent)
        self._checkAndPlayGunRammerEffect(shellReloadTime)
        if reloadStart:
            self.__playSoundObject(self._startSound)
        self.delayCallback(max(0.0, shellReloadTime - self._desc.duration), self.__playSoundObject, self._finishSound)
        return

    def stop(self):
        if self._startSound is not None:
            self._startSound.stop()
            self._startSound = None
        if self._finishSound is not None:
            self._finishSound.stop()
            self._finishSound = None
        self.stopCallback(self.__playSoundObject)
        self._stopGunRammerEffect()
        return

    def reloadEnd(self):
        self.stopCallback(self.__playSoundObject)
        return

    @staticmethod
    def __playSoundObject(sound):
        if sound is None:
            return
        else:
            sound.stop()
            if _isReplayWarping():
                return
            sound.play()
            return


class AutoShootReload(_GunReload):

    def __init__(self, effectDesc):
        super(AutoShootReload, self).__init__(effectDesc)
        self._finishSound = None
        self._startSound = None
        return

    def __del__(self):
        self.stop()
        CallbackDelayer.destroy(self)
        return

    def start(self, shellReloadTime, alert, shellCount, reloadShellCount, shellID, reloadStart, clipCapacity):
        if gEffectsDisabled():
            return
        SoundGroups.g_instance.setSwitch(b'SWITCH_ext_rld_autoshoot_caliber', self._desc.caliber)
        self._startSound = self._startSound or SoundGroups.g_instance.getSound2D(self._desc.clipReloadStart)
        self._finishSound = self._finishSound or SoundGroups.g_instance.getSound2D(self._desc.clipReloadEnd)
        if reloadStart:
            self.__playSoundObject(self._startSound)
            if alert and self._desc.ammoLow:
                playByName(self._desc.ammoLow)
        self.delayCallback(max(0.0, shellReloadTime - self._desc.duration), self.__playSoundObject, self._finishSound)
        return

    def stop(self):
        self.__cleanSounds()
        self.stopCallback(self.__playSoundObject)
        self._stopGunRammerEffect()
        return

    def reloadEnd(self):
        self.stopCallback(self.__playSoundObject)
        return

    def __cleanSounds(self):
        if self._startSound is not None:
            self._startSound.stop()
            self._startSound = None
        if self._finishSound is not None:
            self._finishSound.stop()
            self._finishSound = None
        return

    @staticmethod
    def __playSoundObject(sound):
        if sound is None:
            return
        else:
            sound.stop()
            if _isReplayWarping():
                return
            sound.play()
            return


class ReloadEffectStrategy(object):
    __sessionProvider = dependency.descriptor(IBattleSessionProvider)
    __slots__ = (b'__gunReloadEffect', b'__intuitionReloadEffect', b'__currentReloadEffect', b'__reloadInProgress', b'__lastShellCD')

    def __init__(self, gunReloadEffectDesc):
        self.__gunReloadEffect = gunReloadEffectDesc.create()
        if gunReloadEffectDesc.hasUniqueIntuitionReload():
            self.__intuitionReloadEffect = gunReloadEffectDesc.createIntuitionReload()
        else:
            self.__intuitionReloadEffect = None
        self.__currentReloadEffect = self.__gunReloadEffect
        self.__reloadInProgress = False
        self.__lastShellCD = None
        return

    def start(self, timeLeft, baseTime, clipCapacity, reloadType=ReloadType.ANY, gunIndex=DUAL_GUN.ACTIVE_GUN.LEFT):
        reloadFromStart = (self.__reloadInProgress or fabs(timeLeft - baseTime)) < 0.001 if 1 else False
        self.__reloadInProgress = True
        self.__reloadStartEffect(timeLeft, clipCapacity, reloadFromStart, reloadType, gunIndex)
        return

    def stop(self):
        self.__reloadInProgress = False
        self.__lastShellCD = None
        if self.__intuitionReloadEffect is not None:
            self.__intuitionReloadEffect.stop()
        self.__gunReloadEffect.stop()
        return

    def onClipLoad(self, timeLeft, shellsInClip, lastShell, canBeFull):
        if self.__currentReloadEffect is not None:
            self.__currentReloadEffect.onClipLoad(timeLeft, shellsInClip, lastShell, canBeFull)
        return

    def onFull(self):
        if self.__currentReloadEffect is not None:
            self.__currentReloadEffect.onFull()
        return

    def shotFail(self):
        if self.__currentReloadEffect is not None:
            self.__currentReloadEffect.shotFail()
        return

    def reloadEnd(self):
        self.__reloadInProgress = False
        self.__lastShellCD = None
        if self.__currentReloadEffect is not None:
            self.__currentReloadEffect.reloadEnd()
        return

    def getGunReloadType(self):
        return self.__gunReloadEffect.getEffectType()

    def stopActiveDualGunSounds(self):
        gunReloadType = self.getGunReloadType()
        if gunReloadType == ReloadEffectsType.DUALGUN_RELOAD:
            self.__gunReloadEffect.stopActiveSounds()
            if self.__intuitionReloadEffect is not None:
                self.__intuitionReloadEffect.stopActiveSounds()
        elif gunReloadType in (ReloadEffectsType.DUALGUN_AUTORELOAD, ReloadEffectsType.DUALGUN_BARREL):
            self.__gunReloadEffect.stopActiveDualGunSounds()
        return

    def __reloadStartEffect(self, timeLeft, clipCapacity, reloadFromStart, reloadType, gunIndex):
        ammoCtrl = self.__sessionProvider.shared.ammo
        currentShellCD = ammoCtrl.getCurrentShellCD()
        quantity, quantityInClip = ammoCtrl.getShells(currentShellCD)
        isIntuition = ammoCtrl.getIntuitionReloadInProcess()
        reloadShellCount = clipCapacity
        gunReloadType = self.getGunReloadType()
        if gunReloadType in (ReloadEffectsType.DUALGUN_RELOAD, ReloadEffectsType.DUALGUN_AUTORELOAD,
         ReloadEffectsType.DUALGUN_BARREL):
            if self.__lastShellCD is not None and self.__lastShellCD != currentShellCD:
                self.stopActiveDualGunSounds()
        self.__lastShellCD = currentShellCD
        if isIntuition and self.__intuitionReloadEffect is not None:
            reloadEffect = self.__intuitionReloadEffect
        else:
            reloadEffect = self.__gunReloadEffect
        if self.__currentReloadEffect != reloadEffect:
            self.__currentReloadEffect.stop()
        self.__currentReloadEffect = reloadEffect
        if reloadEffect is not None:
            ammoLowMask = self.__getAmmoLowMask(gunReloadType, clipCapacity, quantity)
            if clipCapacity > quantity:
                reloadShellCount = quantity
            if gunReloadType == ReloadEffectsType.DUALGUN_RELOAD:
                reloadEffect.start(timeLeft, ammoLowMask, directTrigger=reloadType == ReloadType.DUALGUN, gunIndex=gunIndex)
            elif gunReloadType in (ReloadEffectsType.DUALGUN_AUTORELOAD, ReloadEffectsType.DUALGUN_BARREL):
                reloadEffect.start(timeLeft, ammoLowMask, quantityInClip, reloadShellCount, currentShellCD, reloadFromStart, clipCapacity, reloadType, gunIndex)
            else:
                reloadEffect.start(timeLeft, ammoLowMask, quantityInClip, reloadShellCount, currentShellCD, reloadFromStart, clipCapacity)
        return

    @staticmethod
    def __getAmmoLowMask(gunReloadType, clipCapacity, shellsLeft):
        ammoLowMask = 0
        if clipCapacity > shellsLeft:
            ammoLowMask |= 1 << ReloadType.CLIP
        if gunReloadType in (ReloadEffectsType.DUALGUN_RELOAD, ReloadEffectsType.DUALGUN_AUTORELOAD,
         ReloadEffectsType.DUALGUN_BARREL):
            if shellsLeft == 1:
                ammoLowMask |= 1 << ReloadType.DUALGUN
        return ammoLowMask


@dependency.replace_none_kwargs(sessionProvider=IBattleSessionProvider)
def _needGunRammerEffect(sessionProvider=None):
    if sessionProvider is not None:
        return sessionProvider.shared.optionalDevices.soundManager.needGunRammerEffect()
    else:
        return


def _playGunRammerEffect():
    SoundGroups.g_instance.playSound2D(GUN_RAMMER_EFFECT_NAME)
    return


RELOAD_EFFECTS_DESCR_MAP = {(ReloadEffectsType.SIMPLE_RELOAD): _SimpleReloadDesc, 
   (ReloadEffectsType.BARREL_RELOAD): _BarrelReloadDesc, 
   (ReloadEffectsType.AUTO_RELOAD): _AutoReloadDesc, 
   (ReloadEffectsType.DUALGUN_RELOAD): _DualGunReloadDesc, 
   (ReloadEffectsType.AUTO_SHOOT_CHANGE_SHELL_RELOAD): _AutoShootChangeShellGunReloadDescr, 
   (ReloadEffectsType.AUTO_SHOOT_RELOAD): _AutoShootGunReloadDescr, 
   (ReloadEffectsType.DUALGUN_AUTORELOAD): _DualGunAutoReloadDesc, 
   (ReloadEffectsType.DUALGUN_BARREL): _DualGunBarrelReloadDesc}
