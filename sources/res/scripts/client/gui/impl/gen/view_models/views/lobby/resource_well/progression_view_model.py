from enum import Enum
from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.resource_well.reward_model import RewardModel

class ProgressionState(Enum):
    ACTIVE = b'active'
    FORBIDDEN = b'forbidden'
    NOPROGRESS = b'noProgress'
    NOVEHICLES = b'noVehicles'
    BEFOREEVENT = b'beforeEvent'


class ProgressionViewModel(ViewModel):
    __slots__ = (b'onPreview', b'onAboutClick', b'onResourcesContribute', b'onResourcesReturn', b'onHangarShow', b'onViewLoaded', b'onClose')

    def __init__(self, properties=12, commands=7):
        super(ProgressionViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getStartDate(self):
        return self._getNumber(0)

    def setStartDate(self, value):
        self._setNumber(0, value)
        return

    def getEndDate(self):
        return self._getNumber(1)

    def setEndDate(self, value):
        self._setNumber(1, value)
        return

    def getTimeLeft(self):
        return self._getNumber(2)

    def setTimeLeft(self, value):
        self._setNumber(2, value)
        return

    def getBeforeEventTimeLeft(self):
        return self._getNumber(3)

    def setBeforeEventTimeLeft(self, value):
        self._setNumber(3, value)
        return

    def getServerTimestamp(self):
        return self._getNumber(4)

    def setServerTimestamp(self, value):
        self._setNumber(4, value)
        return

    def getIsEventEndingSoon(self):
        return self._getBool(5)

    def setIsEventEndingSoon(self, value):
        self._setBool(5, value)
        return

    def getTopRewardPlayersCount(self):
        return self._getNumber(6)

    def setTopRewardPlayersCount(self, value):
        self._setNumber(6, value)
        return

    def getRegularRewardVehiclesCount(self):
        return self._getNumber(7)

    def setRegularRewardVehiclesCount(self, value):
        self._setNumber(7, value)
        return

    def getRewards(self):
        return self._getArray(8)

    def setRewards(self, value):
        self._setArray(8, value)
        return

    @staticmethod
    def getRewardsType():
        return RewardModel

    def getProgressionState(self):
        return ProgressionState(self._getString(9))

    def setProgressionState(self, value):
        self._setString(9, value.value)
        return

    def getProgression(self):
        return self._getNumber(10)

    def setProgression(self, value):
        self._setNumber(10, value)
        return

    def getVehicleName(self):
        return self._getString(11)

    def setVehicleName(self, value):
        self._setString(11, value)
        return

    def _initialize(self):
        super(ProgressionViewModel, self)._initialize()
        self._addNumberProperty(b'startDate', 0)
        self._addNumberProperty(b'endDate', 0)
        self._addNumberProperty(b'timeLeft', 0)
        self._addNumberProperty(b'beforeEventTimeLeft', 0)
        self._addNumberProperty(b'serverTimestamp', 0)
        self._addBoolProperty(b'isEventEndingSoon', False)
        self._addNumberProperty(b'topRewardPlayersCount', 0)
        self._addNumberProperty(b'regularRewardVehiclesCount', 0)
        self._addArrayProperty(b'rewards', Array())
        self._addStringProperty(b'progressionState')
        self._addNumberProperty(b'progression', 0)
        self._addStringProperty(b'vehicleName', b'')
        self.onPreview = self._addCommand(b'onPreview')
        self.onAboutClick = self._addCommand(b'onAboutClick')
        self.onResourcesContribute = self._addCommand(b'onResourcesContribute')
        self.onResourcesReturn = self._addCommand(b'onResourcesReturn')
        self.onHangarShow = self._addCommand(b'onHangarShow')
        self.onViewLoaded = self._addCommand(b'onViewLoaded')
        self.onClose = self._addCommand(b'onClose')
        return
