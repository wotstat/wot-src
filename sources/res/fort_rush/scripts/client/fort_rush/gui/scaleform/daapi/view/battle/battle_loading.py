from __future__ import absolute_import
import random
from account_helpers.settings_core.options import BattleLoadingTipSetting
from gui.impl import backport
from gui.impl.gen import R
from gui.Scaleform.daapi.view.battle.shared.battle_loading import BattleLoading
_FORT_RUSH_TIP_ICONS = tuple(backport.image(R.images.fort_rush.gui.maps.icons.battle_loading.dyn((b'tip_{:02d}').format(index))()) for index in range(1, 4))
_FORT_RUSH_TIP_TEXT = (
 (
  R.strings.fort_rush.battleLoading.tips.tip01.title(), R.strings.fort_rush.battleLoading.tips.tip01.description()),
 (
  R.strings.fort_rush.battleLoading.tips.tip02.title(), R.strings.fort_rush.battleLoading.tips.tip02.description()),
 (
  R.strings.fort_rush.battleLoading.tips.tip03.title(), R.strings.fort_rush.battleLoading.tips.tip03.description()))

class FortRushBattleLoading(BattleLoading):

    def __init__(self):
        super(FortRushBattleLoading, self).__init__()
        self.__tipIndex = random.randrange(len(_FORT_RUSH_TIP_ICONS))
        self.__tipIcon = _FORT_RUSH_TIP_ICONS[self.__tipIndex]
        return

    def _setTipsInfo(self):
        super(FortRushBattleLoading, self)._setTipsInfo()
        titleRes, descriptionRes = _FORT_RUSH_TIP_TEXT[self.__tipIndex]
        self.as_setTipTitleS(self._formatTipTitle(backport.text(titleRes)))
        self.as_setTipS(self._formatTipBody(backport.text(descriptionRes)))
        return

    def _makeVisualTipVO(self, arenaDP, tip=None):
        vo = super(FortRushBattleLoading, self)._makeVisualTipVO(arenaDP, tip)
        settingID = BattleLoadingTipSetting.OPTIONS.VISUAL
        vo.update({b'settingID': settingID, 
           b'tipIcon': (self.__tipIcon), 
           b'showMinimap': False, 
           b'showTableBackground': False, 
           b'showTipsBackground': True})
        vo.update(self._getViewSettingByID(settingID))
        return vo
