import functools, weakref, BigWorld, BattleReplay
from AvatarInputHandler.cameras import FovExtended
from adisp import adisp_async
from debug_utils import LOG_DEBUG, LOG_ERROR
from gui import DialogsInterface
from gui.Scaleform.daapi.view.dialogs import TimerConfirmDialogMeta
from gui.shared.utils.monitor_settings import g_monitorSettings
from messenger import g_settings as messenger_settings

class ISettingsStorage(object):

    def __init__(self, manager, core):
        self._manager = weakref.proxy(manager)
        self._core = weakref.proxy(core)
        self._settings = {}
        return

    def store(self, setting):
        settingOption = setting[b'option']
        settingValue = setting[b'value']
        self._settings[settingOption] = settingValue
        return

    def extract(self, settingOption, default=None):
        return self._settings.get(settingOption, default)

    def apply(self, restartApproved):
        return (
         None, (lambda : None))

    def clear(self):
        self._settings.clear()
        return


class ServerSettingsStorage(ISettingsStorage):

    def __init__(self, manager, core, section):
        super(ServerSettingsStorage, self).__init__(manager, core)
        self._section = section
        return

    def apply(self, restartApproved):
        if self._settings and not BattleReplay.isPlaying():
            self._manager.setSectionSettings(self._section, self._settings)
        return super(ServerSettingsStorage, self).apply(restartApproved)

    def extract(self, settingOption, default=None):
        if not BattleReplay.isPlaying():
            default = self._manager.getSectionSettings(self._section, settingOption, default)
        return super(ServerSettingsStorage, self).extract(settingOption, default)


class VideoSettingsStorage(ISettingsStorage):

    @property
    def windowMode(self):
        return self._settings.get(b'windowMode', g_monitorSettings.windowMode)

    @windowMode.setter
    def windowMode(self, value):
        self.store({b'option': b'windowMode', b'value': value})
        return

    @property
    def resolution(self):
        resolution = (None, None)
        current = g_monitorSettings.currentVideoMode
        if current is not None:
            resolution = (
             current.width, current.height)
        return self._settings.get(b'resolution', resolution)

    @resolution.setter
    def resolution(self, value):
        self.store({b'option': b'resolution', b'value': value})
        return

    @property
    def refreshRate(self):
        refreshRate = None
        current = g_monitorSettings.currentVideoMode
        if current is not None:
            refreshRate = current.refreshRate
        return self._settings.get(b'refreshRate', refreshRate)

    @refreshRate.setter
    def refreshRate(self, value):
        self.store({b'option': b'refreshRate', b'value': value})
        return

    @property
    def videoMode(self):
        return self.videoModeForAdapterOutputIndex(g_monitorSettings.activeMonitor)

    def videoModeForAdapterOutputIndex(self, adapterOutputIndex):
        width, height = self.resolution
        refreshRate = self.refreshRate
        adapterOutputExclusiveFullscreenModes = g_monitorSettings.videoModesForAdapterOutputIndex(adapterOutputIndex)
        for mode in adapterOutputExclusiveFullscreenModes:
            if mode.width == width and mode.height == height and mode.refreshRate == refreshRate:
                return mode

        if adapterOutputIndex == g_monitorSettings.activeMonitor:
            LOG_ERROR(b'Unable to find appropriate display mode for the target monitor, falling back to the current mode.')
            return g_monitorSettings.currentVideoMode
        LOG_ERROR(b'Unable to find appropriate display mode for the target monitor, falling back to the first supported mode.')
        return adapterOutputExclusiveFullscreenModes[0]

    @property
    def windowSize(self):
        size = (None, None)
        current = g_monitorSettings.currentWindowSize
        if current is not None:
            size = (
             current.width, current.height)
        return self._settings.get(b'windowSize', size)

    @windowSize.setter
    def windowSize(self, value):
        self.store({b'option': b'windowSize', b'value': value})
        return

    @property
    def borderlessSize(self):
        size = (None, None)
        current = g_monitorSettings.currentBorderlessSize
        if current is not None:
            size = (
             current.width, current.height)
        return self._settings.get(b'borderlessSize', size)

    @borderlessSize.setter
    def borderlessSize(self, value):
        self.store({b'option': b'borderlessSize', b'value': value})
        return

    @property
    def monitor(self):
        return self._settings.get(b'monitor', g_monitorSettings.activeMonitor)

    @monitor.setter
    def monitor(self, value):
        self.store({b'option': b'monitor', b'value': value})
        return

    def apply(self, restartApproved):
        if self._settings:
            LOG_DEBUG(b'Applying video settings: ', self._settings)
            cWindowSize = g_monitorSettings.currentWindowSize
            windowSizeWidth, windowSizeHeight = self.windowSize
            cBorderlessSize = g_monitorSettings.currentBorderlessSize
            borderlessSizeWidth, borderlessSizeHeight = self.borderlessSize
            cWindowMode = g_monitorSettings.windowMode
            windowMode = self.windowMode
            cMonitor = g_monitorSettings.activeMonitor
            monitor = self.monitor
            exclusiveFullscreenMonitorIndex = g_monitorSettings.noRestartExclusiveFullscreenMonitorIndex
            restartNeeded = windowMode == BigWorld.WindowModeExclusiveFullscreen and monitor != exclusiveFullscreenMonitorIndex
            cVideoMode = g_monitorSettings.currentVideoMode
            cAspectRatio = float(cVideoMode.width) / cVideoMode.height
            videoMode = self.videoModeForAdapterOutputIndex(monitor)
            aspectRatio = float(videoMode.width) / videoMode.height
            windowSizeChanged = cWindowSize is not None and windowSizeWidth is not None and windowSizeHeight is not None and (windowSizeWidth != cWindowSize.width or windowSizeHeight != cWindowSize.height)
            borderlessSizeChanged = cBorderlessSize is not None and borderlessSizeWidth is not None and borderlessSizeHeight is not None and (borderlessSizeWidth != cBorderlessSize.width or borderlessSizeHeight != cBorderlessSize.height)
            monitorChanged = monitor != cMonitor
            videModeChanged = cVideoMode is not None and videoMode is not None and videoMode.index != cVideoMode.index
            windowModeChanged = windowMode != cWindowMode
            deviseRecreated = False
            if monitorChanged:
                g_monitorSettings.changeMonitor(monitor)
                deviseRecreated = windowMode == BigWorld.WindowModeExclusiveFullscreen or cWindowMode == BigWorld.WindowModeExclusiveFullscreen
            if restartNeeded:
                deviseRecreated = False
                LOG_DEBUG(b"VideoSettingsStorage apply is expecting a restart so it didn't invoke changeVideoMode.")
            elif windowSizeChanged and windowMode == BigWorld.WindowModeWindowed:
                deviseRecreated = True
                g_monitorSettings.changeWindowSize(windowSizeWidth, windowSizeHeight)
            elif borderlessSizeChanged and windowMode == BigWorld.WindowModeBorderless:
                deviseRecreated = True
                g_monitorSettings.changeBorderlessSize(borderlessSizeWidth, borderlessSizeHeight)
            elif (not monitorChanged or restartApproved) and (videModeChanged or windowModeChanged):
                deviseRecreated = True
                BigWorld.changeVideoMode(videoMode.index, int(windowMode))
            BigWorld.changeFullScreenAspectRatio(aspectRatio)
            self.clear()
            self._core.isDeviseRecreated = deviseRecreated
            if deviseRecreated:

                def wrapper(monitorChanged, windowSizeChanged, borderlessSizeChanged, cMonitor, cWindowSize, cVideoMode, cWindowMode, cAspectRatio):

                    def revert():
                        if monitorChanged:
                            g_monitorSettings.changeMonitor(cMonitor)
                        if borderlessSizeChanged and cWindowMode == BigWorld.WindowModeBorderless:
                            g_monitorSettings.changeBorderlessSize(cBorderlessSize.width, cBorderlessSize.height)
                        elif windowSizeChanged and cWindowMode == BigWorld.WindowModeWindowed:
                            g_monitorSettings.changeWindowSize(cWindowSize.width, cWindowSize.height)
                        elif not monitorChanged and (videModeChanged or windowModeChanged):
                            BigWorld.changeVideoMode(cVideoMode.index, cWindowMode)
                        BigWorld.changeFullScreenAspectRatio(cAspectRatio)
                        return

                    return revert

                @adisp_async
                def confirmator(callback=None):
                    BigWorld.callback(0.0, (lambda : DialogsInterface.showI18nConfirmDialog(b'graphicsChangeConfirmation', callback, meta=TimerConfirmDialogMeta(b'graphicsChangeConfirmation', timer=15))))
                    return

                return (
                 confirmator,
                 wrapper(monitorChanged, windowSizeChanged, borderlessSizeChanged, cMonitor, cWindowSize, cVideoMode, cWindowMode, cAspectRatio))
        return super(VideoSettingsStorage, self).apply(restartApproved)


class MessengerSettingsStorage(object):

    def __init__(self, proxy=None):
        self._proxy = weakref.proxy(proxy)
        self._settings = {}
        return

    def store(self, setting):
        settingOption = setting[b'option']
        settingValue = setting[b'value']
        self._settings[settingOption] = settingValue
        self._proxy.store(setting)
        return

    def extract(self, settingOption, default=None):
        return self._proxy.extract(settingOption, default)

    def apply(self, restartApproved):
        messenger_settings.saveUserPreferences(self._settings)
        return (
         None, (lambda : None))

    def clear(self):
        self._settings.clear()
        return


class AimSettingsStorage(ISettingsStorage):

    def apply(self, restartApproved):
        if self._settings and not BattleReplay.isPlaying():
            self._manager.setAimSettings(self._settings)
        return super(AimSettingsStorage, self).apply(restartApproved)

    def extract(self, settingOption, key=None, default=None):
        if not BattleReplay.isPlaying():
            default = self._manager.getAimSetting(settingOption, key, default)
        return self._settings.get(settingOption, {}).get(key, default)


class MarkersSettingsStorage(ISettingsStorage):

    def apply(self, restartApproved):
        if self._settings and not BattleReplay.isPlaying():
            self._manager.setMarkersSettings(self._settings)
        return super(MarkersSettingsStorage, self).apply(restartApproved)

    def extract(self, settingOption, key=None, default=None):
        if not BattleReplay.isPlaying():
            default = self._manager.getMarkersSetting(settingOption, key, default)
        return self._settings.get(settingOption, {}).get(key, default)


class FOVSettingsStorage(ISettingsStorage):

    def __init__(self, manager=None, core=None):
        super(FOVSettingsStorage, self).__init__(manager, core)
        self.__dynamicFOVEnabled = None
        self.__FOV = None
        return

    def proxyDynamicFOVEnabled(self, option):
        self.__dynamicFOVEnabled = weakref.proxy(option)
        return

    @property
    def dynamicFOVEnabled(self):
        value = self.__dynamicFOVEnabled.get() if self.__dynamicFOVEnabled is not None else None
        return self._settings.get(b'dynamicFOVEnabled', value)

    @dynamicFOVEnabled.setter
    def dynamicFOVEnabled(self, value):
        self.store({b'option': b'dynamicFOVEnabled', b'value': value})
        return

    def proxyFOV(self, option):
        self.__FOV = weakref.proxy(option)
        return

    @property
    def FOV(self):
        value = self.__FOV.get() if self.__dynamicFOVEnabled is not None else None
        return self._settings.get(b'FOV', value)

    @FOV.setter
    def FOV(self, value):
        self.store({b'option': b'FOV', b'value': value})
        return

    def apply(self, restartApproved, forceApply=False):
        if self._settings or forceApply:
            staticFOV, dynamicFOVLow, dynamicFOVTop = self.FOV
            dynamicFOVEnabled = self.dynamicFOVEnabled

            def setFov(value, multiplier, dynamicFOVEnabled):
                if not dynamicFOVEnabled:
                    FovExtended.instance().resetFov()
                FovExtended.instance().horizontalFov = value
                return

            if dynamicFOVEnabled:
                multiplier = float(dynamicFOVLow) / dynamicFOVTop
                horizontalFov = dynamicFOVTop
            else:
                multiplier = 1.0
                horizontalFov = staticFOV
            BigWorld.callback(0.0, functools.partial(setFov, horizontalFov, multiplier, dynamicFOVEnabled))
        return super(FOVSettingsStorage, self).apply(restartApproved)
