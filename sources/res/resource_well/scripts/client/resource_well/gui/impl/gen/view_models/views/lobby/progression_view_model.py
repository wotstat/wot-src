from enum import Enum
from resource_well.gui.impl.gen.view_models.views.lobby.enums import EventMode
from frameworks.wulf import Array, ViewModel
from resource_well.gui.impl.gen.view_models.views.lobby.reward_model import RewardModel

class ProgressionState(Enum):
    ACTIVE = b'active'
    FORBIDDEN = b'forbidden'
    NOPROGRESS = b'noProgress'
    NOVEHICLES = b'noVehicles'


class ProgressionViewModel(ViewModel):
    __slots__ = (b'onPreview', b'onAboutClick', b'onResourcesContribute', b'onResourcesReturn', b'onHangarShow', b'onClose', b'onRewardSelected')

    def __init__(self, properties=9, commands=7):
        super(ProgressionViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getEndDate(self):
        return self._getNumber(0)

    def setEndDate(self, value):
        self._setNumber(0, value)
        return

    def getTimeLeft(self):
        return self._getNumber(1)

    def setTimeLeft(self, value):
        self._setNumber(1, value)
        return

    def getIsEventEndingSoon(self):
        return self._getBool(2)

    def setIsEventEndingSoon(self, value):
        self._setBool(2, value)
        return

    def getRewards(self):
        return self._getArray(3)

    def setRewards(self, value):
        self._setArray(3, value)
        return

    @staticmethod
    def getRewardsType():
        return RewardModel

    def getProgressionState(self):
        return ProgressionState(self._getString(4))

    def setProgressionState(self, value):
        self._setString(4, value.value)
        return

    def getEventMode(self):
        return EventMode(self._getString(5))

    def setEventMode(self, value):
        self._setString(5, value.value)
        return

    def getCurrentRewardId(self):
        return self._getString(6)

    def setCurrentRewardId(self, value):
        self._setString(6, value)
        return

    def getProgression(self):
        return self._getNumber(7)

    def setProgression(self, value):
        self._setNumber(7, value)
        return

    def getShowBlur(self):
        return self._getBool(8)

    def setShowBlur(self, value):
        self._setBool(8, value)
        return

    def _initialize(self):
        super(ProgressionViewModel, self)._initialize()
        self._addNumberProperty(b'endDate', 0)
        self._addNumberProperty(b'timeLeft', 0)
        self._addBoolProperty(b'isEventEndingSoon', False)
        self._addArrayProperty(b'rewards', Array())
        self._addStringProperty(b'progressionState')
        self._addStringProperty(b'eventMode')
        self._addStringProperty(b'currentRewardId', b'')
        self._addNumberProperty(b'progression', 0)
        self._addBoolProperty(b'showBlur', False)
        self.onPreview = self._addCommand(b'onPreview')
        self.onAboutClick = self._addCommand(b'onAboutClick')
        self.onResourcesContribute = self._addCommand(b'onResourcesContribute')
        self.onResourcesReturn = self._addCommand(b'onResourcesReturn')
        self.onHangarShow = self._addCommand(b'onHangarShow')
        self.onClose = self._addCommand(b'onClose')
        self.onRewardSelected = self._addCommand(b'onRewardSelected')
        return
