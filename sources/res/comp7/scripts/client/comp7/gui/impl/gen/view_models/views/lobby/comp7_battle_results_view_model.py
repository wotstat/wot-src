from enum import Enum
from frameworks.wulf import Array, Map, ViewModel
from comp7.gui.impl.gen.view_models.views.lobby.battle_results.comp7_bans_model import Comp7BansModel
from comp7.gui.impl.gen.view_models.views.lobby.battle_results.comp7_battle_info_model import Comp7BattleInfoModel
from comp7.gui.impl.gen.view_models.views.lobby.battle_results.comp7_team_stats_model import Comp7TeamStatsModel
from comp7.gui.impl.gen.view_models.views.lobby.progression_item_model import ProgressionItemModel
from comp7.gui.impl.gen.view_models.views.lobby.qualification_model import QualificationModel
from comp7.gui.impl.gen.view_models.views.lobby.schedule_info_model import ScheduleInfoModel
from gui.impl.gen.view_models.views.lobby.battle_results.additional_bonus_model import AdditionalBonusModel
from gui.impl.gen.view_models.views.lobby.battle_results.base_capture_info_model import BaseCaptureInfoModel
from gui.impl.gen.view_models.views.lobby.battle_results.detailed_personal_efficiency_model import DetailedPersonalEfficiencyModel
from gui.impl.gen.view_models.views.lobby.battle_results.financial_report_model import FinancialReportModel
from gui.impl.gen.view_models.views.lobby.battle_results.player_satisfaction_model import PlayerSatisfactionModel
from gui.impl.gen.view_models.views.lobby.battle_results.postbattle_achievement_model import PostbattleAchievementModel
from gui.impl.gen.view_models.views.lobby.common.router_model import RouterModel

class WarningType(Enum):
    NONE = b'none'
    LEAVE = b'leave'


class Comp7BattleResultsViewModel(ViewModel):
    __slots__ = (b'onClose', b'onOpenMissions')
    OVERVIEW = b'overview'
    TEAMS_STATISTICS = b'teamScore'
    PROGRESSION = b'missionProgress'
    FINANCIAL_REPORT = b'financialReport'

    def __init__(self, properties=21, commands=2):
        super(Comp7BattleResultsViewModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def scheduleInfo(self):
        return self._getViewModel(0)

    @staticmethod
    def getScheduleInfoType():
        return ScheduleInfoModel

    @property
    def qualificationModel(self):
        return self._getViewModel(1)

    @staticmethod
    def getQualificationModelType():
        return QualificationModel

    @property
    def bansModel(self):
        return self._getViewModel(2)

    @staticmethod
    def getBansModelType():
        return Comp7BansModel

    @property
    def battleInfo(self):
        return self._getViewModel(3)

    @staticmethod
    def getBattleInfoType():
        return Comp7BattleInfoModel

    @property
    def teamStats(self):
        return self._getViewModel(4)

    @staticmethod
    def getTeamStatsType():
        return Comp7TeamStatsModel

    @property
    def baseCaptureInfo(self):
        return self._getViewModel(5)

    @staticmethod
    def getBaseCaptureInfoType():
        return BaseCaptureInfoModel

    @property
    def financialReport(self):
        return self._getViewModel(6)

    @staticmethod
    def getFinancialReportType():
        return FinancialReportModel

    @property
    def additionalBonus(self):
        return self._getViewModel(7)

    @staticmethod
    def getAdditionalBonusType():
        return AdditionalBonusModel

    @property
    def playerSatisfaction(self):
        return self._getViewModel(8)

    @staticmethod
    def getPlayerSatisfactionType():
        return PlayerSatisfactionModel

    @property
    def router(self):
        return self._getViewModel(9)

    @staticmethod
    def getRouterType():
        return RouterModel

    def getUnRankedBattleTypes(self):
        return self._getArray(10)

    def setUnRankedBattleTypes(self, value):
        self._setArray(10, value)
        return

    @staticmethod
    def getUnRankedBattleTypesType():
        return int

    def getProgressionItems(self):
        return self._getArray(11)

    def setProgressionItems(self, value):
        self._setArray(11, value)
        return

    @staticmethod
    def getProgressionItemsType():
        return ProgressionItemModel

    def getCurrentItemIndex(self):
        return self._getNumber(12)

    def setCurrentItemIndex(self, value):
        self._setNumber(12, value)
        return

    def getPreviousScore(self):
        return self._getNumber(13)

    def setPreviousScore(self, value):
        self._setNumber(13, value)
        return

    def getCurrentScore(self):
        return self._getNumber(14)

    def setCurrentScore(self, value):
        self._setNumber(14, value)
        return

    def getRatingDelta(self):
        return self._getNumber(15)

    def setRatingDelta(self, value):
        self._setNumber(15, value)
        return

    def getWarningType(self):
        return WarningType(self._getString(16))

    def setWarningType(self, value):
        self._setString(16, value.value)
        return

    def getTopPercentage(self):
        return self._getNumber(17)

    def setTopPercentage(self, value):
        self._setNumber(17, value)
        return

    def getAchievements(self):
        return self._getArray(18)

    def setAchievements(self, value):
        self._setArray(18, value)
        return

    @staticmethod
    def getAchievementsType():
        return PostbattleAchievementModel

    def getDetailedPersonalEfficiency(self):
        return self._getArray(19)

    def setDetailedPersonalEfficiency(self, value):
        self._setArray(19, value)
        return

    @staticmethod
    def getDetailedPersonalEfficiencyType():
        return DetailedPersonalEfficiencyModel

    def getPathToPlugins(self):
        return self._getMap(20)

    def setPathToPlugins(self, value):
        self._setMap(20, value)
        return

    @staticmethod
    def getPathToPluginsType():
        return (int, unicode)

    def _initialize(self):
        super(Comp7BattleResultsViewModel, self)._initialize()
        self._addViewModelProperty(b'scheduleInfo', ScheduleInfoModel())
        self._addViewModelProperty(b'qualificationModel', QualificationModel())
        self._addViewModelProperty(b'bansModel', Comp7BansModel())
        self._addViewModelProperty(b'battleInfo', Comp7BattleInfoModel())
        self._addViewModelProperty(b'teamStats', Comp7TeamStatsModel())
        self._addViewModelProperty(b'baseCaptureInfo', BaseCaptureInfoModel())
        self._addViewModelProperty(b'financialReport', FinancialReportModel())
        self._addViewModelProperty(b'additionalBonus', AdditionalBonusModel())
        self._addViewModelProperty(b'playerSatisfaction', PlayerSatisfactionModel())
        self._addViewModelProperty(b'router', RouterModel())
        self._addArrayProperty(b'unRankedBattleTypes', Array())
        self._addArrayProperty(b'progressionItems', Array())
        self._addNumberProperty(b'currentItemIndex', 0)
        self._addNumberProperty(b'previousScore', 0)
        self._addNumberProperty(b'currentScore', 0)
        self._addNumberProperty(b'ratingDelta', 0)
        self._addStringProperty(b'warningType', WarningType.NONE.value)
        self._addNumberProperty(b'topPercentage', 0)
        self._addArrayProperty(b'achievements', Array())
        self._addArrayProperty(b'detailedPersonalEfficiency', Array())
        self._addMapProperty(b'pathToPlugins', Map(int, unicode))
        self.onClose = self._addCommand(b'onClose')
        self.onOpenMissions = self._addCommand(b'onOpenMissions')
        return
