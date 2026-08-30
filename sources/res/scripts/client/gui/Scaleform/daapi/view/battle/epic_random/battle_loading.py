from __future__ import absolute_import
from gui.Scaleform.daapi.view.battle.shared.battle_loading import BattleLoading, BattleLoadingTipSetting

class EpicRandomBattleLoading(BattleLoading):

    def _getViewSettingByID(self, settingID):
        result = {}
        if settingID == BattleLoadingTipSetting.OPTIONS.TEXT:
            result.update({b'leftTeamTitleLeft': (-418), 
               b'rightTeamTitleLeft': 200, 
               b'tipTitleTop': 536, 
               b'tipBodyTop': 562, 
               b'showTableBackground': True, 
               b'showTipsBackground': False})
        else:
            result.update({b'leftTeamTitleLeft': (-468), 
               b'rightTeamTitleLeft': 255, 
               b'tipTitleTop': 366, 
               b'tipBodyTop': 397, 
               b'showTableBackground': False, 
               b'showTipsBackground': True})
        return result
