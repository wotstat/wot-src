from enum import IntEnum
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.paragons.all_chapters.allChapters_view_model import AllChaptersViewModel
from gui.impl.gen.view_models.views.lobby.paragons.all_rewards.allrewards_view_model import AllrewardsViewModel
from gui.impl.gen.view_models.views.lobby.paragons.progression.progression_view_model import ProgressionViewModel

class TabId(IntEnum):
    PROGRESS = 0
    CHAPTERS = 2
    ABOUT = 3


class NavigationViewModel(ViewModel):
    __slots__ = (b'onTabChange', b'onBack', b'onBackToSeasons', b'onClose', b'onToChaptersView', b'onSelectChapter', b'onToChapterRewards', b'onSeasonActivate')

    def __init__(self, properties=12, commands=8):
        super(NavigationViewModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def progression(self):
        return self._getViewModel(0)

    @staticmethod
    def getProgressionType():
        return ProgressionViewModel

    @property
    def allRewards(self):
        return self._getViewModel(1)

    @staticmethod
    def getAllRewardsType():
        return AllrewardsViewModel

    @property
    def allChapters(self):
        return self._getViewModel(2)

    @staticmethod
    def getAllChaptersType():
        return AllChaptersViewModel

    def getHasNewProgress(self):
        return self._getBool(3)

    def setHasNewProgress(self, value):
        self._setBool(3, value)
        return

    def getHasNewRewards(self):
        return self._getBool(4)

    def setHasNewRewards(self, value):
        self._setBool(4, value)
        return

    def getHasNewChapters(self):
        return self._getBool(5)

    def setHasNewChapters(self, value):
        self._setBool(5, value)
        return

    def getWasChapterSelected(self):
        return self._getBool(6)

    def setWasChapterSelected(self, value):
        self._setBool(6, value)
        return

    def getCurrentTabId(self):
        return TabId(self._getNumber(7))

    def setCurrentTabId(self, value):
        self._setNumber(7, value.value)
        return

    def getParagonPoints(self):
        return self._getNumber(8)

    def setParagonPoints(self, value):
        self._setNumber(8, value)
        return

    def getNecessaryVehicleCount(self):
        return self._getNumber(9)

    def setNecessaryVehicleCount(self, value):
        self._setNumber(9, value)
        return

    def getVehicleCount(self):
        return self._getNumber(10)

    def setVehicleCount(self, value):
        self._setNumber(10, value)
        return

    def getPreviewSeasonId(self):
        return self._getNumber(11)

    def setPreviewSeasonId(self, value):
        self._setNumber(11, value)
        return

    def _initialize(self):
        super(NavigationViewModel, self)._initialize()
        self._addViewModelProperty(b'progression', ProgressionViewModel())
        self._addViewModelProperty(b'allRewards', AllrewardsViewModel())
        self._addViewModelProperty(b'allChapters', AllChaptersViewModel())
        self._addBoolProperty(b'hasNewProgress', False)
        self._addBoolProperty(b'hasNewRewards', False)
        self._addBoolProperty(b'hasNewChapters', False)
        self._addBoolProperty(b'wasChapterSelected', False)
        self._addNumberProperty(b'currentTabId')
        self._addNumberProperty(b'paragonPoints', 0)
        self._addNumberProperty(b'necessaryVehicleCount', 0)
        self._addNumberProperty(b'vehicleCount', 0)
        self._addNumberProperty(b'previewSeasonId', 0)
        self.onTabChange = self._addCommand(b'onTabChange')
        self.onBack = self._addCommand(b'onBack')
        self.onBackToSeasons = self._addCommand(b'onBackToSeasons')
        self.onClose = self._addCommand(b'onClose')
        self.onToChaptersView = self._addCommand(b'onToChaptersView')
        self.onSelectChapter = self._addCommand(b'onSelectChapter')
        self.onToChapterRewards = self._addCommand(b'onToChapterRewards')
        self.onSeasonActivate = self._addCommand(b'onSeasonActivate')
        return
