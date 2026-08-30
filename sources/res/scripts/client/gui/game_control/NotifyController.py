from __future__ import absolute_import
import base64
from collections import namedtuple
from future.moves import pickle
import BigWorld, Settings
from adisp import adisp_async, adisp_process
from debug_utils import LOG_DEBUG, LOG_ERROR
from frameworks.wulf import WindowLayer
from gui.Scaleform.framework.managers.containers import POP_UP_CRITERIA
from gui.app_loader import decorators as ap_decorators
from gui.shared import event_dispatcher
from gui.shared import events, g_eventBus, EVENT_BUS_SCOPE
from gui.shared.utils import graphics
from helpers import dependency
from skeletons.account_helpers.settings_core import ISettingsCore
from skeletons.gui.battle_session import IBattleSessionProvider
from skeletons.gui.game_control import INotifyController
from gui.impl import backport
from gui.impl.gen import R
from gui import makeHtmlString
_Settings = namedtuple(b'_Settings', [
 b'presetChangingVersion',
 b'lastBattleAvgFps'])

class NotifyController(INotifyController):
    LOW_FPS_VALUE = 20
    CURRENT_LOW_FPS_WARNING_VERSION = 1
    MIN_BATTLE_LENGHT = 180
    sessionProvider = dependency.descriptor(IBattleSessionProvider)
    settingsCore = dependency.descriptor(ISettingsCore)

    def __init__(self):
        super(NotifyController, self).__init__()
        self.__graphicsResetShown = False
        self.__settings = _Settings(0, None)
        return

    @ap_decorators.sf_lobby
    def app(self):
        return

    def init(self):
        self.__readSettings()
        self._startUIListening()
        self._startPlayingTimeListening()
        return

    def fini(self):
        self._stopUIListening()
        self._stopPlayingTimeListening()
        self.__writeSettings()
        super(NotifyController, self).fini()
        return

    def updateBattleFpsInfo(self, avgBattleFps, battlePlayingTime):
        LOG_DEBUG(b'Updating battle fps info', avgBattleFps, battlePlayingTime)
        if battlePlayingTime >= self.MIN_BATTLE_LENGHT:
            self.__settings = self.__settings._replace(lastBattleAvgFps=avgBattleFps)
        return

    def _startUIListening(self):
        g_eventBus.addListener(events.FightButtonEvent.FIGHT_BUTTON_UPDATE, self.__handleUiUpdated, scope=EVENT_BUS_SCOPE.LOBBY)
        return

    def _startPlayingTimeListening(self):
        g_eventBus.addListener(events.GameEvent.PLAYING_TIME_ON_ARENA, self.__handlePlayingTimeOnArena, scope=EVENT_BUS_SCOPE.BATTLE)
        return

    def _stopUIListening(self):
        g_eventBus.removeListener(events.FightButtonEvent.FIGHT_BUTTON_UPDATE, self.__handleUiUpdated, scope=EVENT_BUS_SCOPE.LOBBY)
        return

    def _stopPlayingTimeListening(self):
        g_eventBus.removeListener(events.GameEvent.PLAYING_TIME_ON_ARENA, self.__handlePlayingTimeOnArena, scope=EVENT_BUS_SCOPE.BATTLE)
        return

    @adisp_process
    def __handleUiUpdated(self, _):
        self._stopUIListening()
        yield lambda callback: callback(True)
        if self.sessionProvider.getCtx().wasInBattle:
            return
        graphicsStatus = graphics.getStatus()
        if not self.__graphicsResetShown and graphicsStatus.isReset():
            isOk = yield self.__showI18nDialog(b'resetGraphics', ctx={b'alert': (self.__wrapHtmlMessage(backport.text(R.strings.dialogs.graphics.message.alert())))})
            self.__graphicsResetShown = True
            if isOk:
                event_dispatcher.showSettingsWindow(redefinedKeyMode=False, tabIndex=event_dispatcher.SettingsTabIndex.GRAPHICS)
        elif graphicsStatus.isShowWarning():
            event_dispatcher.showSettingsWindow(redefinedKeyMode=False, tabIndex=event_dispatcher.SettingsTabIndex.GRAPHICS)
            isOk = yield self.__showI18nDialog(b'changeGraphics', ctx={b'alert': (self.__wrapHtmlMessage(backport.text(R.strings.dialogs.graphics.message.alert())))})
            if isOk:
                self.__updatePresetSetting()
        elif self.__isNeedToShowPresetChangingDialog():
            event_dispatcher.showSettingsWindow(redefinedKeyMode=False, tabIndex=event_dispatcher.SettingsTabIndex.GRAPHICS)
            isOk = yield self.__showI18nDialog(b'lowFpsWarning')
            if isOk:
                BigWorld.callback(0.001, self.__downgradePresetIndex)
            else:
                self.__updateLowFpsDialogVersion()
        graphicsStatus.markProcessed()
        self.__clearCurrentFpsInfo()
        return

    def __handlePlayingTimeOnArena(self, event):
        ctx = event.ctx
        if b'time' in ctx:
            playingTime = ctx[b'time']
        else:
            LOG_ERROR(b'Playing time is not found', event.ctx)
            return
        avgBattleFps = BigWorld.getBattleFPS()[2]
        LOG_DEBUG(b'Updating battle fps info', avgBattleFps, playingTime)
        if playingTime >= self.MIN_BATTLE_LENGHT:
            self.__settings = self.__settings._replace(lastBattleAvgFps=avgBattleFps)
        return

    @adisp_async
    def __showI18nDialog(self, key, callback, ctx=None):
        from gui import DialogsInterface
        return DialogsInterface.showI18nConfirmDialog(key, callback, ctx)

    def __getSettingsWindow(self):
        from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
        windowContainer = self.app.containerManager.getContainer(WindowLayer.TOP_WINDOW)
        return windowContainer.getView(criteria={(POP_UP_CRITERIA.VIEW_ALIAS): (VIEW_ALIAS.SETTINGS_WINDOW)})

    def __closeSettingsWindow(self):
        window = self.__getSettingsWindow()
        if window is not None:
            window.onWindowClose()
        return

    def __updatePresetSetting(self, presetIdx=None):
        window = self.__getSettingsWindow()
        if window is not None:
            if presetIdx is None:
                presetIdx = window.autodetectQuality()
            window.as_setGraphicsPresetS(presetIdx)
        return

    @classmethod
    def __getGraphicsPresetSetting(cls):
        from account_helpers.settings_core.settings_constants import GRAPHICS
        return cls.settingsCore.options.getSetting(GRAPHICS.PRESETS)

    def __downgradePresetIndex(self):
        presetSetting = self.__getGraphicsPresetSetting()
        nextPresetToApply = presetSetting.get() + 1
        if nextPresetToApply < len(graphics.getGraphicsPresetsIndices()):
            self.__updatePresetSetting(nextPresetToApply)
            window = self.__getSettingsWindow()
            if window is not None:
                for opt in presetSetting.getOptions():
                    if opt[b'index'] == nextPresetToApply:
                        return window._applySettings(opt[b'settings'], True)

        return

    def __isNeedToShowPresetChangingDialog(self):
        avgFps = self.__settings.lastBattleAvgFps
        isCustomPreset = BigWorld.isCustomGraphicPreset()
        canToDowngradePreset = BigWorld.canToDowngradePreset()
        return avgFps and avgFps <= self.LOW_FPS_VALUE and not isCustomPreset and canToDowngradePreset and self.__settings.presetChangingVersion < self.CURRENT_LOW_FPS_WARNING_VERSION

    def __clearCurrentFpsInfo(self):
        self.__settings = self.__settings._replace(lastBattleAvgFps=None)
        self.__writeSettings()
        return

    def __updateLowFpsDialogVersion(self):
        self.__settings = self.__settings._replace(presetChangingVersion=self.CURRENT_LOW_FPS_WARNING_VERSION)
        self.__writeSettings()
        return

    def __readSettings(self):
        try:
            userPrefs = Settings.g_instance.userPrefs
            if userPrefs.has_key(Settings.KEY_GUI_NOTIFY_INFO):
                self.__settings = self.__settings._replace(**pickle.loads(base64.b64decode(userPrefs.readString(Settings.KEY_GUI_NOTIFY_INFO))))
        except Exception as msg:
            LOG_DEBUG(b'There is error while reading gui notifying settings', msg)

        return

    def __writeSettings(self):
        Settings.g_instance.userPrefs.write(Settings.KEY_GUI_NOTIFY_INFO, base64.b64encode(pickle.dumps(self.__settings._asdict())))
        return

    @classmethod
    def __wrapHtmlMessage(cls, message):
        return makeHtmlString(b'html_templates:lobby/dialogs', b'graphicsAlert', {b'message': message})
