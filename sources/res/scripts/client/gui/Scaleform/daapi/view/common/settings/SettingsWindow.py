import functools, BattleReplay, BigWorld, LGC, VOIP
from account_helpers import AccountSettings
from account_helpers.AccountSettings import COLOR_SETTINGS_TAB_IDX
from account_helpers.settings_core.ServerSettingsManager import SETTINGS_SECTIONS
from account_helpers.settings_core.settings_constants import SETTINGS_GROUP
from debug_utils import LOG_DEBUG, LOG_WARNING
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
from account_helpers.counter_settings import getNewSettings, invalidateSettings
from gui.Scaleform.framework.managers.loaders import SFViewLoadParams
from gui.Scaleform.locale.RES_ICONS import RES_ICONS
from gui.Scaleform.locale.SETTINGS import SETTINGS
from gui import DialogsInterface, g_guiResetters
from gui.shared import g_eventBus, events, EVENT_BUS_SCOPE
from gui.shared.utils import flashObject2Dict, decorators, graphics
from gui.Scaleform.daapi.view.meta.SettingsWindowMeta import SettingsWindowMeta
from gui.Scaleform.daapi.view.common.settings.SettingsParams import SettingsParams
from account_helpers.settings_core import settings_constants
from account_helpers.settings_core.options import APPLY_METHOD
from helpers import dependency
from messenger.m_constants import PROTO_TYPE
from messenger.proto import proto_getter
from gui.Scaleform.genConsts.SETTINGS_DIALOGS import SETTINGS_DIALOGS
from gui.shared.formatters import icons
from gui import makeHtmlString
from gui.impl import backport
from gui.impl.gen import R
from skeletons.account_helpers.settings_core import ISettingsCore
from skeletons.gui.game_control import IAnonymizerController, ILimitedUIController
from skeletons.gui.lobby_context import ILobbyContext
from uilogging.limited_ui.constants import LimitedUILogItem, LimitedUILogScreenParent
from uilogging.limited_ui.loggers import LimitedUILogger
_PAGES = (
 SETTINGS.GAMETITLE, SETTINGS.GRAFICTITLE, SETTINGS.SOUNDTITLE,
 SETTINGS.KEYBOARDTITLE, SETTINGS.CURSORTITLE, SETTINGS.MARKERTITLE,
 SETTINGS.FEEDBACK, SETTINGS.OTHERTITLE)
_PAGES_INDICES = dict((v, k) for k, v in enumerate(_PAGES))
_g_lastTabIdx = 0

def _getLastTabIndex():
    global _g_lastTabIdx
    return _g_lastTabIdx


def _setLastTabIndex(idx):
    global _g_lastTabIdx
    _g_lastTabIdx = idx
    return


def _delayCall(delay, function):
    if BattleReplay.g_replayCtrl.isPaused:
        function()
    else:
        BigWorld.callback(delay, function)
    return


class SettingsWindow(SettingsWindowMeta):
    anonymizerController = dependency.descriptor(IAnonymizerController)
    settingsCore = dependency.descriptor(ISettingsCore)
    lobbyContext = dependency.descriptor(ILobbyContext)
    limitedUIController = dependency.descriptor(ILimitedUIController)

    def __init__(self, ctx=None):
        super(SettingsWindow, self).__init__()
        self.__redefinedKeyModeEnabled = ctx.get(b'redefinedKeyMode', True)
        self.__isBattleSettings = ctx.get(b'isBattleSettings', False)
        if b'tabIndex' in ctx and ctx[b'tabIndex'] is not None:
            _setLastTabIndex(ctx[b'tabIndex'])
        self.params = SettingsParams()
        return

    @proto_getter(PROTO_TYPE.BW_CHAT2)
    def bwProto(self):
        return

    def __getSettingsParam(self):
        settings = {(SETTINGS_GROUP.GAME_SETTINGS): (self.params.getGameSettings()), 
           (SETTINGS_GROUP.GRAPHICS_SETTINGS): (self.params.getGraphicsSettings()), 
           (SETTINGS_GROUP.SOUND_SETTINGS): (self.params.getSoundSettings()), 
           (SETTINGS_GROUP.CONTROLS_SETTINGS): (self.params.getControlsSettings()), 
           (SETTINGS_GROUP.AIM_SETTINGS): (self.params.getAimSettings()), 
           (SETTINGS_GROUP.MARKERS_SETTINGS): (self.params.getMarkersSettings()), 
           (SETTINGS_GROUP.FEEDBACK_SETTINGS): (self.params.getFeedbackSettings())}
        return settings

    def __getSettings(self):
        settings = self.__getSettingsParam()
        return {key: {b'keys': (value.keys()), b'values': (value.values())} for key, value in settings.iteritems()}

    def __commitSettings(self, settings=None, restartApproved=False, isCloseWnd=False):
        if settings is None:
            settings = {}
        self.__apply(settings, restartApproved, isCloseWnd)
        return

    def __apply(self, settings, restartApproved=False, isCloseWnd=False):
        LOG_DEBUG(b'Settings window: apply settings', restartApproved, settings)
        self.settingsCore.isDeviseRecreated = False
        self.settingsCore.isChangesConfirmed = True
        isRestart = self.params.apply(settings, restartApproved)
        if settings_constants.GRAPHICS.INTERFACE_SCALE in settings:
            self.__updateInterfaceScale()
        isPresetApplied = self.__isGraphicsPresetApplied(settings)
        if self.settingsCore.isChangesConfirmed and isCloseWnd:
            self.onWindowClose()
        if isRestart:
            BigWorld.savePreferences()
            if restartApproved:
                _delayCall(0.3, self.__restartGame)
            elif self.settingsCore.isDeviseRecreated:
                self.onRecreateDevice()
                self.settingsCore.isDeviseRecreated = False
            else:
                _delayCall(0.0, functools.partial(BigWorld.changeVideoMode, -1, BigWorld.getWindowMode()))
        elif not isPresetApplied:
            DialogsInterface.showI18nInfoDialog(b'graphicsPresetNotInstalled', None)
        return

    def __restartGame(self):
        BigWorld.savePreferences()
        LGC.notifyRestart()
        BigWorld.worldDrawEnabled(False)
        BigWorld.restartGame()
        return

    def _populate(self):
        super(SettingsWindow, self)._populate()
        dataVO = [
         {b'label': (SETTINGS.FEEDBACK_TAB_DAMAGEINDICATOR), 
            b'linkage': (VIEW_ALIAS.FEEDBACK_DAMAGE_INDICATOR)},
         {b'label': (SETTINGS.FEEDBACK_TAB_SIXTHSENSE), 
            b'linkage': (VIEW_ALIAS.FEEDBACK_SIXTH_SENSE)},
         {b'label': (SETTINGS.FEEDBACK_TAB_EVENTSINFO), 
            b'linkage': (VIEW_ALIAS.FEEDBACK_BATTLE_EVENTS)},
         {b'label': (SETTINGS.FEEDBACK_TAB_DAMAGELOGPANEL), 
            b'linkage': (VIEW_ALIAS.FEEDBACK_DAMAGE_LOG)},
         {b'label': (SETTINGS.FEEDBACK_TAB_BATTLEBORDERMAP), 
            b'linkage': (VIEW_ALIAS.FEEDBACK_BATTLE_BORDER_MAP)},
         {b'label': (SETTINGS.FEEDBACK_TAB_QUESTSPROGRESS), 
            b'linkage': (VIEW_ALIAS.FEEDBACK_QUESTS_PROGRESS)}]
        self.as_setFeedbackDataProviderS(dataVO)
        if self.__redefinedKeyModeEnabled:
            BigWorld.setRedefineKeysMode(True)
        self.__currentSettings = self.params.getMonitorSettings()
        self._update()
        self.settingsCore.onSettingsChanged += self.__onSettingsChanged
        self.anonymizerController.onStateChanged += self.__refreshSettings
        g_guiResetters.add(self.onRecreateDevice)
        BigWorld.setAdapterOrdinalNotifyCallback(self.onRecreateDevice)
        return

    def _update(self):
        self.as_setDataS(self.__getSettings())
        newSettings = getNewSettings()
        if newSettings:
            self.as_setCountersDataS(newSettings)
        self.as_updateVideoSettingsS(self.params.getMonitorSettings())
        self.as_openTabS(_getLastTabIndex())
        self.__setColorGradingTechnique()
        self.__setLimitedUISettingVisibility()
        return

    def _dispose(self):
        if self.__redefinedKeyModeEnabled:
            BigWorld.setRedefineKeysMode(False)
        g_guiResetters.discard(self.onRecreateDevice)
        BigWorld.setAdapterOrdinalNotifyCallback(None)
        self.stopVoicesPreview()
        self.stopAltBulbPreview()
        self.stopArtyBulbPreview()
        self.anonymizerController.onStateChanged -= self.__refreshSettings
        self.settingsCore.onSettingsChanged -= self.__onSettingsChanged
        super(SettingsWindow, self)._dispose()
        return

    def onTabSelected(self, tabId):
        if tabId == SETTINGS.SOUNDTITLE:
            self.bwProto.voipController.invalidateInitialization()
        if tabId in _PAGES_INDICES:
            _setLastTabIndex(_PAGES_INDICES[tabId])
        else:
            LOG_WARNING(b"Unknown settings window's page id", tabId)
        return

    def onCounterTargetVisited(self, tabName, subTabName, controlsIDs):
        isSettingsChanged = invalidateSettings(tabName, subTabName, controlsIDs)
        if isSettingsChanged:
            newSettings = getNewSettings()
            self.as_setCountersDataS(newSettings)
        return

    def onSettingsChange(self, settingName, settingValue):
        settingValue = flashObject2Dict(settingValue)
        self.params.preview(settingName, settingValue)
        return

    def applySettings(self, settings, isCloseWnd):
        self._applySettings(flashObject2Dict(settings), isCloseWnd)
        return

    def _applySettings(self, settings, isCloseWnd):
        applyMethod = self.params.getApplyMethod(settings)

        def confirmHandler(isOk):
            if not self.isDisposed():
                self.as_ConfirmationOfApplicationS(isOk)
                if isOk:
                    self.__commitSettings(settings, isOk, isCloseWnd)
                else:
                    self.params.revert()
                if not isCloseWnd:
                    self._update()
            return

        if applyMethod == APPLY_METHOD.RESTART:
            DialogsInterface.showI18nConfirmDialog(b'graphicsPresetRestartConfirmation', confirmHandler)
        elif applyMethod == APPLY_METHOD.DELAYED:
            DialogsInterface.showI18nConfirmDialog(b'graphicsPresetDelayedConfirmation', confirmHandler)
        elif applyMethod == APPLY_METHOD.NEXT_BATTLE and self.__isBattleSettings:
            DialogsInterface.showI18nConfirmDialog(b'nextBattleOptionConfirmation', confirmHandler)
        else:
            confirmHandler(True)
        return

    def onWindowClose(self):
        self.params.revert()
        self.startVOIPTest(False)
        self.destroy()
        return

    def onRecreateDevice(self):
        actualSettings = self.params.getMonitorSettings()
        if self.__currentSettings and self.__currentSettings != actualSettings:
            curDrr = self.__currentSettings[settings_constants.GRAPHICS.DYNAMIC_RENDERER]
            actualDrr = actualSettings[settings_constants.GRAPHICS.DYNAMIC_RENDERER]
            self.__currentSettings = actualSettings
            result = self.__currentSettings.copy()
            if curDrr == actualDrr:
                result[settings_constants.GRAPHICS.DYNAMIC_RENDERER] = None
            self.as_updateVideoSettingsS(result)
        return

    def autodetectQuality(self):
        result = BigWorld.autoDetectGraphicsSettings()
        self.onRecreateDevice()
        return result

    def autodetectAcousticType(self):
        option = self.settingsCore.options.getSetting(settings_constants.SOUND.SOUND_SPEAKERS)
        return option.getSystemPreset()

    def canSelectAcousticType(self, index):
        index = int(index)
        option = self.settingsCore.options.getSetting(settings_constants.SOUND.SOUND_SPEAKERS)
        if not option.isPresetSupportedByIndex(index):

            def _apply(result):
                if not self.isDisposed():
                    LOG_DEBUG(b'Player result', result)
                    self.as_onSoundSpeakersPresetApplyS(result)
                return

            DialogsInterface.showI18nConfirmDialog(b'soundSpeakersPresetDoesNotMatch', callback=_apply)
            return False
        return True

    def startVOIPTest(self, isStart):
        LOG_DEBUG(b'Vivox test: %s' % str(isStart))
        rh = VOIP.getVOIPManager()
        if isStart:
            rh.enterTestChannel()
        else:
            rh.leaveTestChannel()
        return False

    @decorators.adisp_process(b'updateCaptureDevices')
    def updateCaptureDevices(self):
        yield self.bwProto.voipController.requestCaptureDevices()
        opt = self.settingsCore.options.getSetting(settings_constants.SOUND.CAPTURE_DEVICES)
        self.as_setCaptureDevicesS(opt.get(), opt.getOptions())
        return

    def altVoicesPreview(self):
        setting = self.settingsCore.options.getSetting(settings_constants.SOUND.ALT_VOICES)
        setting.playPreviewSound()
        return

    def altBulbPreview(self, sampleID):
        setting = self.settingsCore.options.getSetting(settings_constants.SOUND.DETECTION_ALERT_SOUND)
        setting.playPreviewSound(sampleID)
        return

    def artyBulbPreview(self, sampleID):
        setting = self.settingsCore.options.getSetting(settings_constants.SOUND.ARTY_SHOT_ALERT_SOUND)
        setting.playPreviewSound(sampleID)
        return

    def stopVoicesPreview(self):
        setting = self.settingsCore.options.getSetting(settings_constants.SOUND.ALT_VOICES)
        setting.clearPreviewSound()
        return

    def stopAltBulbPreview(self):
        setting = self.settingsCore.options.getSetting(settings_constants.SOUND.DETECTION_ALERT_SOUND)
        setting.clearPreviewSound()
        return

    def stopArtyBulbPreview(self):
        setting = self.settingsCore.options.getSetting(settings_constants.SOUND.ARTY_SHOT_ALERT_SOUND)
        setting.clearPreviewSound()
        return

    def isSoundModeValid(self):
        setting = self.settingsCore.options.getSetting(settings_constants.SOUND.ALT_VOICES)
        return setting.isSoundModeValid()

    def showWarningDialog(self, dialogID, settings, isCloseWnd):
        ctx = None
        applyMethod = functools.partial(self.applySettings, settings, False)
        if dialogID == SETTINGS_DIALOGS.MINIMAP_ALPHA_NOTIFICATION:
            ctx = {b'icon': (icons.alert()), b'alert': (makeHtmlString(b'html_templates:lobby/dialogs', b'minimapAlphaNotification', {b'message': (backport.text(R.strings.dialogs.minimapAlphaNotification.message.alert()))}))}
        elif dialogID == SETTINGS_DIALOGS.LIMITED_UI_OFF_NOTIFICATION:
            ctx = {b'icon': (icons.alert()), b'alert': (makeHtmlString(b'html_templates:lobby/dialogs', b'limitedUIOffNotification', {b'message': (backport.text(R.strings.dialogs.limitedUIOffNotification.message.alert()))}))}
            applyMethod = self.__applyLimitedUISetting

        def callback(isOk):
            if not self.isDisposed():
                if isOk:
                    applyMethod()
                self.as_confirmWarningDialogS(isOk, dialogID)
                if isCloseWnd and isOk:
                    self.onWindowClose()
            return

        DialogsInterface.showI18nConfirmDialog(dialogID, callback, ctx)
        return

    def openGammaWizard(self, x, y, size):
        g_eventBus.handleEvent(events.LoadViewEvent(SFViewLoadParams(VIEW_ALIAS.GAMMA_WIZARD), ctx={b'x': x, 
           b'y': y, 
           b'size': size}), EVENT_BUS_SCOPE.DEFAULT)
        return

    def openColorSettings(self):
        g_eventBus.handleEvent(events.LoadViewEvent(SFViewLoadParams(VIEW_ALIAS.COLOR_SETTING)), EVENT_BUS_SCOPE.DEFAULT)
        return

    def __updateInterfaceScale(self):
        self.as_updateVideoSettingsS(self.params.getMonitorSettings())
        return

    def __isGraphicsPresetApplied(self, settings):
        allsettings = BigWorld.getGraphicsPresetPropertyNames()
        isGraphicsQualitySettings = False
        for settingKey in settings.iterkeys():
            if settingKey in allsettings:
                isGraphicsQualitySettings = True
                break

        if isGraphicsQualitySettings:
            return self.as_isPresetAppliedS()
        return True

    def __onSettingsChanged(self, diff):
        if settings_constants.GRAPHICS.COLOR_GRADING_TECHNIQUE in diff:
            self.__setColorGradingTechnique(diff.get(settings_constants.GRAPHICS.COLOR_GRADING_TECHNIQUE, None))
        if any([section in diff for section in SETTINGS_SECTIONS.LIMITED_UI_GROUP]):
            self.__setLimitedUISettingVisibility()
        return

    def __refreshSettings(self, **_):
        self._update()
        return

    def __setColorGradingTechnique(self, value=None):
        colorSettingsSelectedTab = AccountSettings.getSettings(COLOR_SETTINGS_TAB_IDX)
        if colorSettingsSelectedTab is None or not graphics.isRendererPipelineDeferred():
            colorSettingsSelectedTab = 0
        label = SETTINGS.GRAPHICSSETTINGSOPTIONS_NONE
        image = RES_ICONS.MAPS_ICONS_SETTINGS_COLOR_GRADING_TECHNIQUE_NONE
        if colorSettingsSelectedTab == 2:
            label = SETTINGS.COLORSETTINGS_TAB_CUSTOMSETTINGS
            image = RES_ICONS.MAPS_ICONS_SETTINGS_COLOR_GRADING_TECHNIQUE_RANDOM
        elif colorSettingsSelectedTab == 1:
            setting = self.settingsCore.options.getSetting(settings_constants.GRAPHICS.COLOR_GRADING_TECHNIQUE)
            images = graphics.getGraphicSettingImages(settings_constants.GRAPHICS.COLOR_GRADING_TECHNIQUE)
            label = SETTINGS.GRAPHICSSETTINGSOPTIONS_NONE
            image = None
            filterIdx = setting.get() if value is None else value
            if setting is not None:
                for option in setting.getOptions():
                    currentIdx = option.get(b'data', 0)
                    if currentIdx == filterIdx:
                        label = option.get(b'label')
                        image = images.get(option.get(b'data', 0))
                        break

            if image is None:
                image = RES_ICONS.MAPS_ICONS_SETTINGS_COLOR_GRADING_TECHNIQUE_NONE
        self.as_setColorGradingTechniqueS(image, label)
        return

    def __setLimitedUISettingVisibility(self):
        self.as_showLimitedUISettingS(self.limitedUIController.isUserSettingsMayShow)
        return

    def __applyLimitedUISetting(self):
        self.limitedUIController.completeAllRules()
        LimitedUILogger().handleClickOnce(LimitedUILogItem.DISABLE_LIMITED_UI_BUTTON, LimitedUILogScreenParent.SETTINGS_WINDOW)
        return
