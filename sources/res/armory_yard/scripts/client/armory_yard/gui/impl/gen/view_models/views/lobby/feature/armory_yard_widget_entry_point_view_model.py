from enum import Enum
from frameworks.wulf import ViewModel

class State(Enum):
    BEFOREPROGRESSION = b'beforeProgression'
    ACTIVE = b'active'
    PURCHASESTAGE = b'purchaseStage'
    COMPLETED = b'completed'
    DISABLED = b'disabled'


class ArmoryYardWidgetEntryPointViewModel(ViewModel):
    __slots__ = (b'onAction',)

    def __init__(self, properties=7, commands=1):
        super(ArmoryYardWidgetEntryPointViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getState(self):
        return State(self._getString(0))

    def setState(self, value):
        self._setString(0, value.value)
        return

    def getStartTime(self):
        return self._getNumber(1)

    def setStartTime(self, value):
        self._setNumber(1, value)
        return

    def getEndTime(self):
        return self._getNumber(2)

    def setEndTime(self, value):
        self._setNumber(2, value)
        return

    def getCurrentTime(self):
        return self._getNumber(3)

    def setCurrentTime(self, value):
        self._setNumber(3, value)
        return

    def getIsRewardAvailable(self):
        return self._getBool(4)

    def setIsRewardAvailable(self, value):
        self._setBool(4, value)
        return

    def getIsLowPreset(self):
        return self._getBool(5)

    def setIsLowPreset(self, value):
        self._setBool(5, value)
        return

    def getIsQuestRerollState(self):
        return self._getBool(6)

    def setIsQuestRerollState(self, value):
        self._setBool(6, value)
        return

    def _initialize(self):
        super(ArmoryYardWidgetEntryPointViewModel, self)._initialize()
        self._addStringProperty(b'state')
        self._addNumberProperty(b'startTime', 0)
        self._addNumberProperty(b'endTime', 0)
        self._addNumberProperty(b'currentTime', 0)
        self._addBoolProperty(b'isRewardAvailable', False)
        self._addBoolProperty(b'isLowPreset', False)
        self._addBoolProperty(b'isQuestRerollState', False)
        self.onAction = self._addCommand(b'onAction')
        return
