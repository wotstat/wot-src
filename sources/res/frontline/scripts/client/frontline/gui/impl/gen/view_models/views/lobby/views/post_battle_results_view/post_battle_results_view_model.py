from frameworks.wulf import Array, ViewModel
from frontline.gui.impl.gen.view_models.views.lobby.views.post_battle_results_view.achievement_model import AchievementModel
from frontline.gui.impl.gen.view_models.views.lobby.views.post_battle_results_view.battle_financial_report_model import BattleFinancialReportModel
from frontline.gui.impl.gen.view_models.views.lobby.views.post_battle_results_view.battle_info_model import BattleInfoModel
from frontline.gui.impl.gen.view_models.views.lobby.views.post_battle_results_view.battle_team_stats_model import BattleTeamStatsModel
from gui.impl.gen.view_models.views.lobby.battle_results.detailed_personal_efficiency_model import DetailedPersonalEfficiencyModel
from gui.impl.gen.view_models.views.lobby.common.router_model import RouterModel

class PostBattleResultsViewModel(ViewModel):
    __slots__ = (b'onClose',)

    def __init__(self, properties=6, commands=1):
        super(PostBattleResultsViewModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def battleInfo(self):
        return self._getViewModel(0)

    @staticmethod
    def getBattleInfoType():
        return BattleInfoModel

    @property
    def teamStats(self):
        return self._getViewModel(1)

    @staticmethod
    def getTeamStatsType():
        return BattleTeamStatsModel

    @property
    def financialReport(self):
        return self._getViewModel(2)

    @staticmethod
    def getFinancialReportType():
        return BattleFinancialReportModel

    @property
    def router(self):
        return self._getViewModel(3)

    @staticmethod
    def getRouterType():
        return RouterModel

    def getAchievements(self):
        return self._getArray(4)

    def setAchievements(self, value):
        self._setArray(4, value)
        return

    @staticmethod
    def getAchievementsType():
        return AchievementModel

    def getDetailedPersonalEfficiency(self):
        return self._getArray(5)

    def setDetailedPersonalEfficiency(self, value):
        self._setArray(5, value)
        return

    @staticmethod
    def getDetailedPersonalEfficiencyType():
        return DetailedPersonalEfficiencyModel

    def _initialize(self):
        super(PostBattleResultsViewModel, self)._initialize()
        self._addViewModelProperty(b'battleInfo', BattleInfoModel())
        self._addViewModelProperty(b'teamStats', BattleTeamStatsModel())
        self._addViewModelProperty(b'financialReport', BattleFinancialReportModel())
        self._addViewModelProperty(b'router', RouterModel())
        self._addArrayProperty(b'achievements', Array())
        self._addArrayProperty(b'detailedPersonalEfficiency', Array())
        self.onClose = self._addCommand(b'onClose')
        return
