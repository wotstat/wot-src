from __future__ import absolute_import
from future.utils import viewitems
from past.utils import old_div
import BigWorld
from debug_utils import LOG_DEBUG
import GUI
from account_helpers.AccountSettings import AccountSettings, COLOR_SETTINGS_TAB_IDX, APPLIED_COLOR_SETTINGS
from account_helpers.settings_core import settings_constants
from account_helpers.settings_core.settings_constants import GRAPHICS, COLOR_GRADING_TECHNIQUE_DEFAULT
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
from gui.Scaleform.daapi.view.common.settings.mixins import LayerVisibilityMixin
from gui.Scaleform.daapi.view.meta.ColorSettingsViewMeta import ColorSettingsViewMeta
from gui.Scaleform.genConsts.COLOR_SETTINGS import COLOR_SETTINGS
from gui.Scaleform.locale.RES_ICONS import RES_ICONS
from gui.Scaleform.locale.SETTINGS import SETTINGS
from gui.shared import EVENT_BUS_SCOPE, events
from gui.shared.events import GameEvent
from gui.shared.formatters import text_styles
from gui.shared.utils import flashObject2Dict, graphics
from gui.hangar_cameras.hangar_camera_common import CameraRelatedEvents
from gui.shared.view_helpers.blur_manager import CachedBlur
from helpers import dependency, i18n
from skeletons.account_helpers.settings_core import ISettingsCore

class TABS(object):
    DEFAULT = 0
    FILTERS = 1
    CUSTOM = 2


class ColorSettingsView(LayerVisibilityMixin, ColorSettingsViewMeta):
    settingsCore = dependency.descriptor(ISettingsCore)

    def __init__(self, ctx=None):
        super(ColorSettingsView, self).__init__(ColorSettingsView)
        self.fireEvent(GameEvent(GameEvent.HIDE_EXTERNAL_COMPONENTS), scope=EVENT_BUS_SCOPE.GLOBAL)
        self.__selectedTabIdx = AccountSettings.getSettings(COLOR_SETTINGS_TAB_IDX)
        self.__componentWidth = 0
        self.__isColorPreviewFilterActive = False
        self.__initSettings = self.__getSettings()
        self.__tabsPreviewSettings = self.__getLastAppliedTabsSettings()
        self.__wasGraphicsOptimizationEnabled = False
        if self.__selectedTabIdx == TABS.CUSTOM:
            self.__showColorPreviewFilter()
        self.__blur = None
        return

    def setViewWidth(self, value):
        self.__componentWidth = value
        if self.__isColorPreviewFilterActive:
            self.__showColorPreviewFilter()
        return

    def moveSpace(self, dx, dy, dz):
        self.fireEvent(CameraRelatedEvents(CameraRelatedEvents.LOBBY_VIEW_MOUSE_MOVE, ctx={b'dx': dx, b'dy': dy, b'dz': dz}))
        self.fireEvent(events.LobbySimpleEvent(events.LobbySimpleEvent.NOTIFY_SPACE_MOVED, ctx={b'dx': dx, b'dy': dy, b'dz': dz}))
        return

    def onSettingsChange(self, settingName, settingValue):
        settingValue = flashObject2Dict(settingValue)
        LOG_DEBUG(b'onSettingsChange', settingName, settingValue)
        self.settingsCore.previewSetting(settingName, settingValue)
        self.__tabsPreviewSettings[self.__selectedTabIdx][settingName] = settingValue
        return

    def onApply(self, diff):
        diff = flashObject2Dict(diff)
        AccountSettings.setSettings(COLOR_SETTINGS_TAB_IDX, self.__selectedTabIdx)
        if self.__selectedTabIdx == TABS.CUSTOM:
            if self.__hasChangesInSettings(settings_constants.GRAPHICS.getCustomColorSettings(), diff):
                diff.update({(settings_constants.GRAPHICS.COLOR_GRADING_TECHNIQUE): COLOR_GRADING_TECHNIQUE_DEFAULT})
            diff[COLOR_SETTINGS.COLOR_GRADING_TECHNIQUE] = 0
            diff[COLOR_SETTINGS.COLOR_FILTER_INTENSITY] = 25
        self.settingsCore.applySettings(diff)
        lastAppliedSettings = AccountSettings.getSettings(APPLIED_COLOR_SETTINGS)
        lastAppliedSettings[self.__selectedTabIdx] = diff
        AccountSettings.setSettings(APPLIED_COLOR_SETTINGS, lastAppliedSettings)
        BigWorld.commitPendingGraphicsSettings()
        self.destroy()
        return

    def onTabSelected(self, selectedTab):
        savedTab = AccountSettings.getSettings(COLOR_SETTINGS_TAB_IDX)
        if savedTab == self.__selectedTabIdx and self.__selectedTabIdx == TABS.FILTERS and selectedTab == TABS.CUSTOM:
            prevSettings = self.__getLastAppliedTabsSettings()[TABS.FILTERS]
            self.__selectedTabIdx = selectedTab
            settings = self.__getCurrentTabSettings()
            prevFilter = prevSettings[settings_constants.GRAPHICS.COLOR_GRADING_TECHNIQUE]
            settings[settings_constants.GRAPHICS.COLOR_GRADING_TECHNIQUE] = prevFilter
            settings[COLOR_SETTINGS.COLOR_FILTER_INTENSITY] = prevSettings[COLOR_SETTINGS.COLOR_FILTER_INTENSITY]
        else:
            self.__selectedTabIdx = selectedTab
            settings = self.__getCurrentTabSettings()
        self.__previewSettings(settings)
        self.as_updateDataS(self.__selectedTabIdx, settings)
        if self.__selectedTabIdx == TABS.CUSTOM:
            self.__showColorPreviewFilter()
        else:
            self.__hideColorPreviewFilter()
        return

    def onReset(self):
        settings = self.__getCurrentTabSettings()
        for settingName in settings_constants.GRAPHICS.getCustomColorSettings():
            setting = self.settingsCore.options.getSetting(settingName)
            defaultValue = setting.getDefaultValue()
            self.settingsCore.previewSetting(settingName, defaultValue)
            self.__tabsPreviewSettings[self.__selectedTabIdx][settingName] = defaultValue
            settings[settingName] = defaultValue

        self.as_updateDataS(self.__selectedTabIdx, settings)
        return

    def onClose(self):
        self.settingsCore.options.revert(settings_constants.GRAPHICS.getColorSettings())
        self.destroy()
        return

    def _populate(self):
        super(ColorSettingsView, self)._populate()
        if self.app is not None:
            self._savedBackgroundAlpha = self.app.getBackgroundAlpha()
            self.app.setBackgroundAlpha(0)
            self.addListener(GameEvent.ON_BACKGROUND_ALPHA_CHANGE, self.__onExternalBackgroundAlphaChange, EVENT_BUS_SCOPE.GLOBAL)
            self.__wasGraphicsOptimizationEnabled = self.app.graphicsOptimizationManager.getEnable()
            self.app.graphicsOptimizationManager.switchOptimizationEnabled(False)
        self.as_initDataS({b'header': (text_styles.superPromoTitle(SETTINGS.COLORSETTINGS_VIEW_HEADER)), 
           b'typesHeader': (text_styles.highTitle(SETTINGS.COLORSETTINGS_VIEW_SUBTITLE)), 
           b'typesDesc': (text_styles.main(SETTINGS.COLORSETTINGS_VIEW_DESCRIPTION)), 
           b'applyLabel': (i18n.makeString(SETTINGS.APPLY_BUTTON)), 
           b'cancelLabel': (i18n.makeString(SETTINGS.CANCEL_BUTTON)), 
           b'settingsTypes': (self.__getTypes()), 
           b'closeLabel': (i18n.makeString(SETTINGS.COLORSETTINGS_VIEW_CLOSEBTN)), 
           b'beforeStr': (text_styles.promoSubTitle(SETTINGS.COLORSETTINGS_VIEW_BEFORE)), 
           b'afterStr': (text_styles.promoSubTitle(SETTINGS.COLORSETTINGS_VIEW_AFTER)), 
           b'filtersHeader': (text_styles.highTitle(SETTINGS.COLORSETTINGS_TAB_FILTERS)), 
           b'filterPowerLabel': (i18n.makeString(SETTINGS.COLORSETTINGS_TAB_FILTERS_INTENSITY)), 
           b'filtersTypes': (self.__getFiltersTypes()), 
           b'manualHeader': (text_styles.highTitle(SETTINGS.COLORSETTINGS_TAB_CUSTOMSETTINGS)), 
           b'brightnessLabel': (i18n.makeString(SETTINGS.COLORSETTINGS_TAB_CUSTOMSETTINGS_BRIGHTNESS)), 
           b'contrastLabel': (i18n.makeString(SETTINGS.COLORSETTINGS_TAB_CUSTOMSETTINGS_CONTRAST)), 
           b'saturationLabel': (i18n.makeString(SETTINGS.COLORSETTINGS_TAB_CUSTOMSETTINGS_SATURATION)), 
           b'resetLabel': (i18n.makeString(SETTINGS.COLORSETTINGS_VIEW_RESETBTN))})
        self.as_updateDataS(self.__selectedTabIdx, self.__initSettings)
        self.__blur = CachedBlur(enabled=False)
        return

    def _dispose(self):
        self.__hideColorPreviewFilter()
        self.settingsCore.clearStorages()
        self.removeListener(GameEvent.ON_BACKGROUND_ALPHA_CHANGE, self.__onExternalBackgroundAlphaChange, EVENT_BUS_SCOPE.GLOBAL)
        if self.app is not None:
            self.app.setBackgroundAlpha(self._savedBackgroundAlpha)
            if hasattr(self.app, b'leaveGuiControlMode'):
                self.app.leaveGuiControlMode(VIEW_ALIAS.COLOR_SETTING)
            self.app.graphicsOptimizationManager.switchOptimizationEnabled(self.__wasGraphicsOptimizationEnabled)
        self.fireEvent(GameEvent(GameEvent.SHOW_EXTERNAL_COMPONENTS), scope=EVENT_BUS_SCOPE.GLOBAL)
        if self.__initSettings is not None:
            self.__initSettings.clear()
            self.__initSettings = None
        if self.__blur is not None:
            self.__blur.fini()
        super(ColorSettingsView, self)._dispose()
        return

    def __getLastAppliedTabsSettings(self):
        lastAppliedSettings = AccountSettings.getSettings(APPLIED_COLOR_SETTINGS)
        filterTabsKeys = (GRAPHICS.COLOR_GRADING_TECHNIQUE, GRAPHICS.COLOR_FILTER_INTENSITY)
        return {(TABS.DEFAULT): {}, (TABS.FILTERS): (self.__getTabSettings(lastAppliedSettings, TABS.FILTERS, filterTabsKeys)), 
           (TABS.CUSTOM): (self.__getTabSettings(lastAppliedSettings, TABS.CUSTOM, GRAPHICS.getCustomColorSettings()))}

    def __getTabSettings(self, lastAppliedSettings, tabIdx, settingKeys):
        tabSettings = lastAppliedSettings.get(tabIdx, {})
        settings = {}
        for key in settingKeys:
            settings[key] = tabSettings.get(key, self.__initSettings[key])

        return settings

    def __getTypes(self):
        return [
         {b'id': (TABS.DEFAULT), 
            b'label': (text_styles.highlightText(SETTINGS.COLORSETTINGS_TAB_DEFAULT)), 
            b'icon': (RES_ICONS.MAPS_ICONS_SETTINGS_COLORSETTINGS_DEFAULT)},
         {b'id': (TABS.FILTERS), 
            b'label': (text_styles.highlightText(SETTINGS.COLORSETTINGS_TAB_FILTERS)), 
            b'icon': (RES_ICONS.MAPS_ICONS_SETTINGS_COLORSETTINGS_FILTERS)},
         {b'id': (TABS.CUSTOM), 
            b'label': (text_styles.highlightText(SETTINGS.COLORSETTINGS_TAB_CUSTOMSETTINGS)), 
            b'icon': (RES_ICONS.MAPS_ICONS_SETTINGS_COLORSETTINGS_MANUAL)}]

    def __getFiltersTypes(self):
        result = []
        setting = self.settingsCore.options.getSetting(GRAPHICS.COLOR_GRADING_TECHNIQUE)
        images = graphics.getGraphicSettingColorSettingsFiletersImages()
        if setting is not None:
            for option in setting.getOptions():
                result.append({b'id': (option.get(b'data', COLOR_GRADING_TECHNIQUE_DEFAULT)), 
                   b'label': (text_styles.stats(option.get(b'label'))), 
                   b'icon': (images.get(option.get(b'data', COLOR_GRADING_TECHNIQUE_DEFAULT)))})

            result = sorted(result, key=(lambda k: k[b'id']))
        return result

    def __getSettings(self):
        settings = {}
        for setting in settings_constants.GRAPHICS.getColorSettings():
            settings[setting] = self.settingsCore.getSetting(setting)

        return settings

    def __showColorPreviewFilter(self):
        width, _ = GUI.screenResolution()[:2]
        witdthPrc = old_div(self.__componentWidth, width)
        delimiterPrc = witdthPrc + old_div(1 - witdthPrc, 2)
        BigWorld.setColorBCSSetup(1, delimiterPrc)
        self.__isColorPreviewFilterActive = True
        return

    def __hideColorPreviewFilter(self):
        BigWorld.setColorBCSSetup(0, 0)
        self.__isColorPreviewFilterActive = False
        return

    def __hasChangesInSettings(self, settingsNames, diff):
        for name in settingsNames:
            if self.__initSettings[name] != diff[name]:
                return True

        return False

    def __getCurrentTabSettings(self):
        settings = {}
        for settingName in settings_constants.GRAPHICS.getColorSettings():
            setting = self.settingsCore.options.getSetting(settingName)
            if settingName != settings_constants.GRAPHICS.COLOR_GRADING_TECHNIQUE:
                defaultValue = setting.getDefaultValue()
            else:
                defaultValue = COLOR_GRADING_TECHNIQUE_DEFAULT
            settings[settingName] = defaultValue

        settings.update(self.__tabsPreviewSettings[self.__selectedTabIdx])
        return settings

    def __previewSettings(self, settings):
        for settingName, value in viewitems(settings):
            self.settingsCore.applySetting(settingName, value)

        return

    def __onExternalBackgroundAlphaChange(self, event):
        self._savedBackgroundAlpha = event.ctx[b'alpha']
        self.app.setBackgroundAlpha(0, notSilentChange=False)
        return
