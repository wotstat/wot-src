from __future__ import absolute_import
from account_helpers.settings_core import settings_constants
from halloween.gui.halloween_gui_constants import BATTLE_CTRL_ID
from halloween.gui.scaleform.daapi.view.meta.HWBossIndicatorProgressMeta import HWBossIndicatorProgressMeta
from helpers import dependency
from skeletons.account_helpers.settings_core import ISettingsCore
from skeletons.gui.battle_session import IBattleSessionProvider

class HWBossIndicator(HWBossIndicatorProgressMeta):
    guiSessionProvider = dependency.descriptor(IBattleSessionProvider)
    settingsCore = dependency.descriptor(ISettingsCore)

    def _populate(self):
        super(HWBossIndicator, self)._populate()
        hwBattleGuiCtrl = self.guiSessionProvider.dynamic.getControllerByID(BATTLE_CTRL_ID.HW_BATTLE_GUI_CTRL)
        if hwBattleGuiCtrl:
            hwBattleGuiCtrl.onVehicleDetectorChangeDistance += self.__handleChangeDistance
        self.settingsCore.onSettingsChanged += self.__onSettingsChange
        self.as_setValueS(0)
        self.as_setIndicatorEnabledS(True)
        self.__updateAlpha()
        return

    def _dispose(self):
        hwBattleGuiCtrl = self.guiSessionProvider.dynamic.getControllerByID(BATTLE_CTRL_ID.HW_BATTLE_GUI_CTRL)
        if hwBattleGuiCtrl:
            hwBattleGuiCtrl.onVehicleDetectorChangeDistance -= self.__handleChangeDistance
        self.settingsCore.onSettingsChanged -= self.__onSettingsChange
        super(HWBossIndicator, self)._dispose()
        return

    def __handleChangeDistance(self, ctx):
        self.as_setValueS(ctx.get(b'indicator', 0))
        return

    def __onSettingsChange(self, diff):
        if settings_constants.GAME.MINIMAP_ALPHA in diff or settings_constants.GAME.MINIMAP_ALPHA_ENABLED in diff:
            self.__updateAlpha()
        return

    def __updateAlpha(self):
        value = 0.0
        if self.settingsCore.getSetting(settings_constants.GAME.MINIMAP_ALPHA_ENABLED):
            value = int(self.settingsCore.getSetting(settings_constants.GAME.MINIMAP_ALPHA))
        self.as_setAlphaS(1 - value / 100.0)
        return
