from enum import IntEnum
from comp7.gui.impl.gen.view_models.views.lobby.enums import StatisticsMode
from frameworks.wulf import Array
from comp7.gui.impl.gen.view_models.views.lobby.meta_view.pages.customization_tasks_model import CustomizationTasksModel
from comp7.gui.impl.gen.view_models.views.lobby.meta_view.pages.day_statistics_model import DayStatisticsModel
from comp7.gui.impl.gen.view_models.views.lobby.meta_view.pages.season_statistics_model import SeasonStatisticsModel
from comp7.gui.impl.gen.view_models.views.lobby.meta_view.pages.top_vehicle_statistics_model import TopVehicleStatisticsModel
from comp7.gui.impl.gen.view_models.views.lobby.meta_view.progression_base_model import ProgressionBaseModel
from comp7.gui.impl.gen.view_models.views.lobby.meta_view.progression_qualification_model import ProgressionQualificationModel
from comp7.gui.impl.gen.view_models.views.lobby.progression_item_model import ProgressionItemModel

class PageState(IntEnum):
    INITIAL = 0
    SUCCESS = 1
    ERROR = 2


class ProgressionModel(ProgressionBaseModel):
    __slots__ = (b'onSelectDay', b'onOpenCustomization', b'onCustomizationProgressShown', b'onOpenVehicleStats', b'onRefresh')
    DEFAULT_SELECTED_DAY = -1

    def __init__(self, properties=19, commands=5):
        super(ProgressionModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def qualificationModel(self):
        return self._getViewModel(2)

    @staticmethod
    def getQualificationModelType():
        return ProgressionQualificationModel

    @property
    def seasonStatisticsModel(self):
        return self._getViewModel(3)

    @staticmethod
    def getSeasonStatisticsModelType():
        return SeasonStatisticsModel

    def getCurrentScore(self):
        return self._getNumber(4)

    def setCurrentScore(self, value):
        self._setNumber(4, value)
        return

    def getLastBestUserPointsValue(self):
        return self._getNumber(5)

    def setLastBestUserPointsValue(self, value):
        self._setNumber(5, value)
        return

    def getIsLastBestUserPointsValueLoading(self):
        return self._getBool(6)

    def setIsLastBestUserPointsValueLoading(self, value):
        self._setBool(6, value)
        return

    def getLeaderboardUpdateTimestamp(self):
        return self._getNumber(7)

    def setLeaderboardUpdateTimestamp(self, value):
        self._setNumber(7, value)
        return

    def getRankInactivityCount(self):
        return self._getNumber(8)

    def setRankInactivityCount(self, value):
        self._setNumber(8, value)
        return

    def getItems(self):
        return self._getArray(9)

    def setItems(self, value):
        self._setArray(9, value)
        return

    @staticmethod
    def getItemsType():
        return ProgressionItemModel

    def getPageState(self):
        return PageState(self._getNumber(10))

    def setPageState(self, value):
        self._setNumber(10, value.value)
        return

    def getStatisticsMode(self):
        return StatisticsMode(self._getNumber(11))

    def setStatisticsMode(self, value):
        self._setNumber(11, value.value)
        return

    def getIsStatisticsLoading(self):
        return self._getBool(12)

    def setIsStatisticsLoading(self, value):
        self._setBool(12, value)
        return

    def getStatisticsUpdateTimestamp(self):
        return self._getNumber(13)

    def setStatisticsUpdateTimestamp(self, value):
        self._setNumber(13, value)
        return

    def getCurrentDayIndex(self):
        return self._getNumber(14)

    def setCurrentDayIndex(self, value):
        self._setNumber(14, value)
        return

    def getSelectedDayIndex(self):
        return self._getNumber(15)

    def setSelectedDayIndex(self, value):
        self._setNumber(15, value)
        return

    def getStatisticsByDay(self):
        return self._getArray(16)

    def setStatisticsByDay(self, value):
        self._setArray(16, value)
        return

    @staticmethod
    def getStatisticsByDayType():
        return DayStatisticsModel

    def getTopVehiclesStatistics(self):
        return self._getArray(17)

    def setTopVehiclesStatistics(self, value):
        self._setArray(17, value)
        return

    @staticmethod
    def getTopVehiclesStatisticsType():
        return TopVehicleStatisticsModel

    def getCustomizationTasks(self):
        return self._getArray(18)

    def setCustomizationTasks(self, value):
        self._setArray(18, value)
        return

    @staticmethod
    def getCustomizationTasksType():
        return CustomizationTasksModel

    def _initialize(self):
        super(ProgressionModel, self)._initialize()
        self._addViewModelProperty(b'qualificationModel', ProgressionQualificationModel())
        self._addViewModelProperty(b'seasonStatisticsModel', SeasonStatisticsModel())
        self._addNumberProperty(b'currentScore', 0)
        self._addNumberProperty(b'lastBestUserPointsValue', 0)
        self._addBoolProperty(b'isLastBestUserPointsValueLoading', False)
        self._addNumberProperty(b'leaderboardUpdateTimestamp', 0)
        self._addNumberProperty(b'rankInactivityCount', -1)
        self._addArrayProperty(b'items', Array())
        self._addNumberProperty(b'pageState')
        self._addNumberProperty(b'statisticsMode')
        self._addBoolProperty(b'isStatisticsLoading', False)
        self._addNumberProperty(b'statisticsUpdateTimestamp', 0)
        self._addNumberProperty(b'currentDayIndex', 0)
        self._addNumberProperty(b'selectedDayIndex', -1)
        self._addArrayProperty(b'statisticsByDay', Array())
        self._addArrayProperty(b'topVehiclesStatistics', Array())
        self._addArrayProperty(b'customizationTasks', Array())
        self.onSelectDay = self._addCommand(b'onSelectDay')
        self.onOpenCustomization = self._addCommand(b'onOpenCustomization')
        self.onCustomizationProgressShown = self._addCommand(b'onCustomizationProgressShown')
        self.onOpenVehicleStats = self._addCommand(b'onOpenVehicleStats')
        self.onRefresh = self._addCommand(b'onRefresh')
        return
