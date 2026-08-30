from enum import Enum, IntEnum
from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.common.missions.bonuses.bonus_model import BonusModel
from gui.impl.gen.view_models.common.user_name_model import UserNameModel
from white_tiger.gui.impl.gen.view_models.views.lobby.feature.battle_results.simplified_quests_view_model import SimplifiedQuestsViewModel
from white_tiger.gui.impl.gen.view_models.views.lobby.feature.battle_results.white_tiger_battle_info_model import WhiteTigerBattleInfoModel
from white_tiger.gui.impl.gen.view_models.views.lobby.feature.battle_results.white_tiger_progress_model import WhiteTigerProgressModel
from white_tiger.gui.impl.gen.view_models.views.lobby.feature.battle_results.white_tiger_team_stats_model import WhiteTigerTeamStatsModel
from gui.impl.gen.view_models.views.lobby.battle_results.personal_efficiency_model import PersonalEfficiencyModel
from gui.impl.gen.view_models.views.lobby.battle_results.premium_plus_model import PremiumPlusModel
from gui.impl.gen.view_models.views.lobby.battle_results.user_status_model import UserStatusModel

class Tab(IntEnum):
    PERSONAL = 1
    TEAMSTATS = 2


class TankTypeEnum(Enum):
    HUNTER = b'wt_hunter'
    BOSS = b'wt_boss'
    SPECIALBOSS = b'wt_special_boss'


class WhiteTigerResultsViewModel(ViewModel):
    __slots__ = (b'onClose', b'onTabChanged')

    def __init__(self, properties=11, commands=2):
        super(WhiteTigerResultsViewModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def userNames(self):
        return self._getViewModel(0)

    @staticmethod
    def getUserNamesType():
        return UserNameModel

    @property
    def userStatus(self):
        return self._getViewModel(1)

    @staticmethod
    def getUserStatusType():
        return UserStatusModel

    @property
    def battleInfo(self):
        return self._getViewModel(2)

    @staticmethod
    def getBattleInfoType():
        return WhiteTigerBattleInfoModel

    @property
    def premiumPlus(self):
        return self._getViewModel(3)

    @staticmethod
    def getPremiumPlusType():
        return PremiumPlusModel

    @property
    def teamStats(self):
        return self._getViewModel(4)

    @staticmethod
    def getTeamStatsType():
        return WhiteTigerTeamStatsModel

    @property
    def progress(self):
        return self._getViewModel(5)

    @staticmethod
    def getProgressType():
        return WhiteTigerProgressModel

    def getEfficiency(self):
        return self._getArray(6)

    def setEfficiency(self, value):
        self._setArray(6, value)
        return

    @staticmethod
    def getEfficiencyType():
        return PersonalEfficiencyModel

    def getRewards(self):
        return self._getArray(7)

    def setRewards(self, value):
        self._setArray(7, value)
        return

    @staticmethod
    def getRewardsType():
        return BonusModel

    def getHarrierQuests(self):
        return self._getArray(8)

    def setHarrierQuests(self, value):
        self._setArray(8, value)
        return

    @staticmethod
    def getHarrierQuestsType():
        return SimplifiedQuestsViewModel

    def getEngineerQuests(self):
        return self._getArray(9)

    def setEngineerQuests(self, value):
        self._setArray(9, value)
        return

    @staticmethod
    def getEngineerQuestsType():
        return SimplifiedQuestsViewModel

    def getTankType(self):
        return TankTypeEnum(self._getString(10))

    def setTankType(self, value):
        self._setString(10, value.value)
        return

    def _initialize(self):
        super(WhiteTigerResultsViewModel, self)._initialize()
        self._addViewModelProperty(b'userNames', UserNameModel())
        self._addViewModelProperty(b'userStatus', UserStatusModel())
        self._addViewModelProperty(b'battleInfo', WhiteTigerBattleInfoModel())
        self._addViewModelProperty(b'premiumPlus', PremiumPlusModel())
        self._addViewModelProperty(b'teamStats', WhiteTigerTeamStatsModel())
        self._addViewModelProperty(b'progress', WhiteTigerProgressModel())
        self._addArrayProperty(b'efficiency', Array())
        self._addArrayProperty(b'rewards', Array())
        self._addArrayProperty(b'harrierQuests', Array())
        self._addArrayProperty(b'engineerQuests', Array())
        self._addStringProperty(b'tankType')
        self.onClose = self._addCommand(b'onClose')
        self.onTabChanged = self._addCommand(b'onTabChanged')
        return
