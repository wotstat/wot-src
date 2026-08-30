from gui.Scaleform.daapi.view.battle.shared.battle_loading import BattleLoading, BattleLoadingTipSetting

class RankedBattleLoading(BattleLoading):

    def _getViewSettingByID(self, settingID):
        result = {}
        if settingID != BattleLoadingTipSetting.OPTIONS.TEXT:
            result.update({b'leftTeamTitleLeft': (-475), 
               b'rightTeamTitleLeft': 270, 
               b'tipTitleTop': 356, 
               b'tipBodyTop': 387, 
               b'showTableBackground': False, 
               b'showTipsBackground': True})
        else:
            result = super(RankedBattleLoading, self)._getViewSettingByID(settingID)
        return result
