from enum import IntEnum
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.comp7.meta_view.pages.leaderboard_model import LeaderboardModel
from gui.impl.gen.view_models.views.lobby.comp7.meta_view.pages.progression_model import ProgressionModel
from gui.impl.gen.view_models.views.lobby.comp7.meta_view.pages.rank_rewards_model import RankRewardsModel
from gui.impl.gen.view_models.views.lobby.comp7.meta_view.pages.weekly_quests_model import WeeklyQuestsModel
from gui.impl.gen.view_models.views.lobby.comp7.meta_view.pages.yearly_statistics_model import YearlyStatisticsModel
from gui.impl.gen.view_models.views.lobby.comp7.meta_view.sidebar_model import SidebarModel
from gui.impl.gen.view_models.views.lobby.comp7.schedule_info_model import ScheduleInfoModel

class MetaRootViews(IntEnum):
    PROGRESSION = 0
    RANKREWARDS = 1
    WEEKLYQUESTS = 2
    LEADERBOARD = 3


class RootViewModel(ViewModel):
    __slots__ = (b'onClose', b'onInfoPageOpen')

    def __init__(self, properties=8, commands=2):
        super(RootViewModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def sidebar(self):
        return self._getViewModel(0)

    @staticmethod
    def getSidebarType():
        return SidebarModel

    @property
    def scheduleInfo(self):
        return self._getViewModel(1)

    @staticmethod
    def getScheduleInfoType():
        return ScheduleInfoModel

    @property
    def progressionModel(self):
        return self._getViewModel(2)

    @staticmethod
    def getProgressionModelType():
        return ProgressionModel

    @property
    def rankRewardsModel(self):
        return self._getViewModel(3)

    @staticmethod
    def getRankRewardsModelType():
        return RankRewardsModel

    @property
    def weeklyQuestsModel(self):
        return self._getViewModel(4)

    @staticmethod
    def getWeeklyQuestsModelType():
        return WeeklyQuestsModel

    @property
    def leaderboardModel(self):
        return self._getViewModel(5)

    @staticmethod
    def getLeaderboardModelType():
        return LeaderboardModel

    @property
    def yearlyStatisticsModel(self):
        return self._getViewModel(6)

    @staticmethod
    def getYearlyStatisticsModelType():
        return YearlyStatisticsModel

    def getPageViewId(self):
        return MetaRootViews(self._getNumber(7))

    def setPageViewId(self, value):
        self._setNumber(7, value.value)
        return

    def _initialize(self):
        super(RootViewModel, self)._initialize()
        self._addViewModelProperty(b'sidebar', SidebarModel())
        self._addViewModelProperty(b'scheduleInfo', ScheduleInfoModel())
        self._addViewModelProperty(b'progressionModel', ProgressionModel())
        self._addViewModelProperty(b'rankRewardsModel', RankRewardsModel())
        self._addViewModelProperty(b'weeklyQuestsModel', WeeklyQuestsModel())
        self._addViewModelProperty(b'leaderboardModel', LeaderboardModel())
        self._addViewModelProperty(b'yearlyStatisticsModel', YearlyStatisticsModel())
        self._addNumberProperty(b'pageViewId')
        self.onClose = self._addCommand(b'onClose')
        self.onInfoPageOpen = self._addCommand(b'onInfoPageOpen')
        return
