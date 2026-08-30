from enum import IntEnum
from frameworks.wulf import ViewModel
from gui.impl.wrappers.user_list_model import UserListModel
from gui.impl.gen.view_models.views.lobby.ranked.division_model import DivisionModel
from gui.impl.gen.view_models.views.lobby.ranked.ranked_statistics_model import RankedStatisticsModel

class States(IntEnum):
    PROGRESSION = 0
    FINAL = 1


class RankedProgressionViewModel(ViewModel):
    __slots__ = (b'onClose', b'onAbout', b'onSelectDivision', b'onOpenFinalState', b'onSelectReward')

    def __init__(self, properties=14, commands=5):
        super(RankedProgressionViewModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def divisions(self):
        return self._getViewModel(0)

    @staticmethod
    def getDivisionsType():
        return DivisionModel

    @property
    def statistics(self):
        return self._getViewModel(1)

    @staticmethod
    def getStatisticsType():
        return RankedStatisticsModel

    def getStartTimestamp(self):
        return self._getNumber(2)

    def setStartTimestamp(self, value):
        self._setNumber(2, value)
        return

    def getEndTimestamp(self):
        return self._getNumber(3)

    def setEndTimestamp(self, value):
        self._setNumber(3, value)
        return

    def getServerTimestamp(self):
        return self._getNumber(4)

    def setServerTimestamp(self, value):
        self._setNumber(4, value)
        return

    def getCurrentDivisionID(self):
        return self._getNumber(5)

    def setCurrentDivisionID(self, value):
        self._setNumber(5, value)
        return

    def getCurrentRank(self):
        return self._getNumber(6)

    def setCurrentRank(self, value):
        self._setNumber(6, value)
        return

    def getCurrentStep(self):
        return self._getNumber(7)

    def setCurrentStep(self, value):
        self._setNumber(7, value)
        return

    def getMaxRank(self):
        return self._getNumber(8)

    def setMaxRank(self, value):
        self._setNumber(8, value)
        return

    def getSelectedDivision(self):
        return self._getNumber(9)

    def setSelectedDivision(self, value):
        self._setNumber(9, value)
        return

    def getSelectedState(self):
        return States(self._getNumber(10))

    def setSelectedState(self, value):
        self._setNumber(10, value.value)
        return

    def getIsFinalStateAvailable(self):
        return self._getBool(11)

    def setIsFinalStateAvailable(self, value):
        self._setBool(11, value)
        return

    def getBonusBattles(self):
        return self._getNumber(12)

    def setBonusBattles(self, value):
        self._setNumber(12, value)
        return

    def getHasRewardToSelect(self):
        return self._getBool(13)

    def setHasRewardToSelect(self, value):
        self._setBool(13, value)
        return

    def _initialize(self):
        super(RankedProgressionViewModel, self)._initialize()
        self._addViewModelProperty(b'divisions', UserListModel())
        self._addViewModelProperty(b'statistics', RankedStatisticsModel())
        self._addNumberProperty(b'startTimestamp', 0)
        self._addNumberProperty(b'endTimestamp', 0)
        self._addNumberProperty(b'serverTimestamp', 0)
        self._addNumberProperty(b'currentDivisionID', 0)
        self._addNumberProperty(b'currentRank', 0)
        self._addNumberProperty(b'currentStep', 0)
        self._addNumberProperty(b'maxRank', 0)
        self._addNumberProperty(b'selectedDivision', 0)
        self._addNumberProperty(b'selectedState')
        self._addBoolProperty(b'isFinalStateAvailable', True)
        self._addNumberProperty(b'bonusBattles', 0)
        self._addBoolProperty(b'hasRewardToSelect', False)
        self.onClose = self._addCommand(b'onClose')
        self.onAbout = self._addCommand(b'onAbout')
        self.onSelectDivision = self._addCommand(b'onSelectDivision')
        self.onOpenFinalState = self._addCommand(b'onOpenFinalState')
        self.onSelectReward = self._addCommand(b'onSelectReward')
        return
