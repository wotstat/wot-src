from __future__ import absolute_import
import typing
from frameworks.wulf.view.submodel_presenter import SubModelPresenter
from helpers import dependency
from skeletons.gui.battle_session import IBattleSessionProvider
from gui.impl.gen.view_models.views.battle.prebattle_highlights.prebattle_highlights_player_stats_model import PrebattleHighlightsPlayerStatsModel
from gui.impl.gen.view_models.views.battle.prebattle_highlights.stats_parameter_model import StatsParameterModel
if typing.TYPE_CHECKING:
    from frameworks.wulf import Array
_STATS_PARAMS_TO_MODEL_MAP = {b'pbhDynVeh.battlesCount': (StatsParameterModel.CURRENT_TANK_SESSION_BATTLES_COUNT), 
   b'pbhDynVeh.maxFrags': (StatsParameterModel.CURRENT_TANK_SESSION_MAX_FRAGS), 
   b'pbhDynVeh.maxDamageBlockedByArmor': (StatsParameterModel.CURRENT_TANK_SESSION_MAX_DAMAGE_BLOCKED_BY_ARMOR), 
   b'pbhDynVeh.maxDamageDealt': (StatsParameterModel.CURRENT_TANK_SESSION_MAX_DAMAGE_DEALT), 
   b'pbhDynVeh.maxAssisted': (StatsParameterModel.CURRENT_TANK_SESSION_MAX_ASSISTED), 
   b'pbhDynVeh.maxSpotted': (StatsParameterModel.CURRENT_TANK_SESSION_MAX_SPOTTED), 
   b'pbhDynVeh.survivedCount': (StatsParameterModel.CURRENT_TANK_SESSION_MAX_SURVIVED), 
   b'pbhDynVeh.winsCount': (StatsParameterModel.CURRENT_TANK_SESSION_WIN_STREAK), 
   b'pbhDynAcc.battlesCount': (StatsParameterModel.ACCOUNT_SESSION_BATTLES_COUNT), 
   b'pbhDynAcc.totalTanksUsed': (StatsParameterModel.ACCOUNT_SESSION_TOTAL_TANKS_USED), 
   b'pbhDynAcc.totalFrags': (StatsParameterModel.ACCOUNT_SESSION_TOTAL_FRAGS), 
   b'pbhDynAcc.totalWins': (StatsParameterModel.ACCOUNT_SESSION_TOTAL_WINS), 
   b'pbhDynAcc.totalDamageBlockedByArmor': (StatsParameterModel.ACCOUNT_SESSION_TOTAL_DAMAGE_BLOCKED_BY_ARMOR), 
   b'pbhDynAcc.totalDamageDealt': (StatsParameterModel.ACCOUNT_SESSION_TOTAL_DAMAGE_DEALT), 
   b'pbhDynAcc.totalAssisted': (StatsParameterModel.ACCOUNT_SESSION_TOTAL_ASSISTED), 
   b'pbhDynAcc.totalSpotted': (StatsParameterModel.ACCOUNT_SESSION_TOTAL_SPOTTED), 
   b'pbhDynAcc.winStreak': (StatsParameterModel.ACCOUNT_SESSION_WIN_STREAK), 
   b'veh.battlesCount': (StatsParameterModel.CURRENT_TANK_BATTLES_COUNT), 
   b'veh.frags': (StatsParameterModel.CURRENT_TANK_FRAGS), 
   b'veh.spotted': (StatsParameterModel.CURRENT_TANK_SPOTTED), 
   b'veh.damageDealt': (StatsParameterModel.CURRENT_TANK_DAMAGE_DEALT), 
   b'veh.damageBlockedByArmor': (StatsParameterModel.CURRENT_TANK_DAMAGE_BLOCKED_BY_ARMOR), 
   b'veh.assisted': (StatsParameterModel.CURRENT_TANK_ASSISTED), 
   b'veh.wins': (StatsParameterModel.CURRENT_TANK_WINS), 
   b'acc.totalDamageDealt': (StatsParameterModel.ACCOUNT_TOTAL_DAMAGE_DEALT), 
   b'acc.totalWins': (StatsParameterModel.ACCOUNT_TOTAL_WINS), 
   b'acc.totalSpotted': (StatsParameterModel.ACCOUNT_TOTAL_SPOTTED), 
   b'acc.battlesCount': (StatsParameterModel.ACCOUNT_BATTLES_COUNT), 
   b'fun.accAge': (StatsParameterModel.ACCOUNT_FUN_AGE), 
   b'fun.treesDestroyed': (StatsParameterModel.ACCOUNT_FUN_TREES_DESTROYED), 
   b'fun.totalMileage': (StatsParameterModel.ACCOUNT_TOTAL_MILEAGE)}

def getStatsParametersToModelMap():
    return _STATS_PARAMS_TO_MODEL_MAP


class StatisticsSubPresenter(SubModelPresenter):
    __sessionProvider = dependency.descriptor(IBattleSessionProvider)

    def packModel(self):
        playersStats = self.__sessionProvider.dynamic.prebattleHighlightsController.winnersStats
        if not playersStats:
            return
        else:
            playersStatsModel = self.getViewModel()
            playersStatsModel.clear()
            for playerInfo in playersStats:
                vehId = playerInfo.get(b'id')
                playerStats = playerInfo.get(b'stats')
                if vehId is None or playerStats is None:
                    return
                playerStatsModel = PrebattleHighlightsPlayerStatsModel()
                playerStatsModel.setVehId(vehId)
                statsParamsModel = playerStatsModel.getStatsParams()
                statsParamsModel.clear()
                for paramName, paramValue in playerStats.items():
                    paramModel = StatsParameterModel()
                    paramsMap = getStatsParametersToModelMap()
                    paramModel.setParameter(paramsMap.get(paramName, b''))
                    paramModel.setValue(paramValue if paramValue is not None else 0)
                    statsParamsModel.addViewModel(paramModel)

                playersStatsModel.addViewModel(playerStatsModel)

            playersStatsModel.invalidate()
            return
