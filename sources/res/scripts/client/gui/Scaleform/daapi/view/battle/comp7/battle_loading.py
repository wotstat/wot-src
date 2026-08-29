from gui.Scaleform.daapi.view.battle.shared.battle_loading import BattleLoading
from account_helpers.settings_core.options import BattleLoadingTipSetting

class Comp7BattleLoading(BattleLoading):

    def _getViewSettingByID(self, settingID):
        result = super(Comp7BattleLoading, self)._getViewSettingByID(settingID)
        result.update({b'leftTeamTitleLeft': (-483), 
           b'rightTeamTitleLeft': 275})
        return result

    def _makeVisualTipVO(self, arenaDP, tip=None):
        settingID = BattleLoadingTipSetting.OPTIONS.MINIMAP
        vo = {b'settingID': settingID, 
           b'tipIcon': None, 
           b'arenaTypeID': (self._arenaVisitor.type.getID()), 
           b'minimapTeam': (arenaDP.getNumberOfTeam()), 
           b'showMinimap': True, 
           b'showTipsBackground': True}
        vo.update(self._getViewSettingByID(settingID))
        return vo
