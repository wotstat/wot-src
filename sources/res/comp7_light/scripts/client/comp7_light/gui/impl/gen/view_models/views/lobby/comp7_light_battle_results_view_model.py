from enum import Enum
from frameworks.wulf import Array, Map, ViewModel
from comp7_light.gui.impl.gen.view_models.views.lobby.battle_results.comp7_light_battle_info_model import Comp7LightBattleInfoModel
from comp7_light.gui.impl.gen.view_models.views.lobby.battle_results.comp7_light_team_stats_model import Comp7LightTeamStatsModel
from comp7_light.gui.impl.gen.view_models.views.lobby.schedule_info_model import ScheduleInfoModel
from gui.impl.gen.view_models.views.lobby.battle_results.additional_bonus_model import AdditionalBonusModel
from gui.impl.gen.view_models.views.lobby.battle_results.base_capture_info_model import BaseCaptureInfoModel
from gui.impl.gen.view_models.views.lobby.battle_results.detailed_personal_efficiency_model import DetailedPersonalEfficiencyModel
from gui.impl.gen.view_models.views.lobby.battle_results.financial_report_model import FinancialReportModel
from gui.impl.gen.view_models.views.lobby.battle_results.postbattle_achievement_model import PostbattleAchievementModel
from gui.impl.gen.view_models.views.lobby.common.router_model import RouterModel

class WarningType(Enum):
    NONE = b'none'
    LEAVE = b'leave'


class Comp7LightBattleResultsViewModel(ViewModel):
    __slots__ = (b'onClose', b'onOpenMissions')
    OVERVIEW = b'overview'
    TEAMS_STATISTICS = b'teamScore'
    PROGRESSION = b'missionProgress'
    FINANCIAL_REPORT = b'financialReport'

    def __init__(self, properties=11, commands=2):
        super(Comp7LightBattleResultsViewModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def scheduleInfo(self):
        return self._getViewModel(0)

    @staticmethod
    def getScheduleInfoType():
        return ScheduleInfoModel

    @property
    def battleInfo(self):
        return self._getViewModel(1)

    @staticmethod
    def getBattleInfoType():
        return Comp7LightBattleInfoModel

    @property
    def teamStats(self):
        return self._getViewModel(2)

    @staticmethod
    def getTeamStatsType():
        return Comp7LightTeamStatsModel

    @property
    def baseCaptureInfo(self):
        return self._getViewModel(3)

    @staticmethod
    def getBaseCaptureInfoType():
        return BaseCaptureInfoModel

    @property
    def financialReport(self):
        return self._getViewModel(4)

    @staticmethod
    def getFinancialReportType():
        return FinancialReportModel

    @property
    def additionalBonus(self):
        return self._getViewModel(5)

    @staticmethod
    def getAdditionalBonusType():
        return AdditionalBonusModel

    @property
    def router(self):
        return self._getViewModel(6)

    @staticmethod
    def getRouterType():
        return RouterModel

    def getWarningType(self):
        return WarningType(self._getString(7))

    def setWarningType(self, value):
        self._setString(7, value.value)
        return

    def getAchievements(self):
        return self._getArray(8)

    def setAchievements(self, value):
        self._setArray(8, value)
        return

    @staticmethod
    def getAchievementsType():
        return PostbattleAchievementModel

    def getDetailedPersonalEfficiency(self):
        return self._getArray(9)

    def setDetailedPersonalEfficiency(self, value):
        self._setArray(9, value)
        return

    @staticmethod
    def getDetailedPersonalEfficiencyType():
        return DetailedPersonalEfficiencyModel

    def getPathToPlugins(self):
        return self._getMap(10)

    def setPathToPlugins(self, value):
        self._setMap(10, value)
        return

    @staticmethod
    def getPathToPluginsType():
        return (int, unicode)

    def _initialize(self):
        super(Comp7LightBattleResultsViewModel, self)._initialize()
        self._addViewModelProperty(b'scheduleInfo', ScheduleInfoModel())
        self._addViewModelProperty(b'battleInfo', Comp7LightBattleInfoModel())
        self._addViewModelProperty(b'teamStats', Comp7LightTeamStatsModel())
        self._addViewModelProperty(b'baseCaptureInfo', BaseCaptureInfoModel())
        self._addViewModelProperty(b'financialReport', FinancialReportModel())
        self._addViewModelProperty(b'additionalBonus', AdditionalBonusModel())
        self._addViewModelProperty(b'router', RouterModel())
        self._addStringProperty(b'warningType', WarningType.NONE.value)
        self._addArrayProperty(b'achievements', Array())
        self._addArrayProperty(b'detailedPersonalEfficiency', Array())
        self._addMapProperty(b'pathToPlugins', Map(int, unicode))
        self.onClose = self._addCommand(b'onClose')
        self.onOpenMissions = self._addCommand(b'onOpenMissions')
        return
