from enum import Enum
from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.common.missions.bonuses.item_bonus_model import ItemBonusModel

class State(Enum):
    DONE = b'done'
    INPROGRESS = b'inProgress'
    UNAVAILABLE = b'unavailable'


class QuestViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=11, commands=0):
        super(QuestViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getNumber(self):
        return self._getNumber(0)

    def setNumber(self, value):
        self._setNumber(0, value)
        return

    def getTitle(self):
        return self._getString(1)

    def setTitle(self, value):
        self._setString(1, value)
        return

    def getDescription(self):
        return self._getString(2)

    def setDescription(self, value):
        self._setString(2, value)
        return

    def getCondition(self):
        return self._getString(3)

    def setCondition(self, value):
        self._setString(3, value)
        return

    def getHasAnimation(self):
        return self._getBool(4)

    def setHasAnimation(self, value):
        self._setBool(4, value)
        return

    def getHasManualPage(self):
        return self._getBool(5)

    def setHasManualPage(self, value):
        self._setBool(5, value)
        return

    def getState(self):
        return State(self._getString(6))

    def setState(self, value):
        self._setString(6, value.value)
        return

    def getRewards(self):
        return self._getArray(7)

    def setRewards(self, value):
        self._setArray(7, value)
        return

    @staticmethod
    def getRewardsType():
        return ItemBonusModel

    def getCurrentProgress(self):
        return self._getNumber(8)

    def setCurrentProgress(self, value):
        self._setNumber(8, value)
        return

    def getLastSeenProgress(self):
        return self._getNumber(9)

    def setLastSeenProgress(self, value):
        self._setNumber(9, value)
        return

    def getMaxProgress(self):
        return self._getNumber(10)

    def setMaxProgress(self, value):
        self._setNumber(10, value)
        return

    def _initialize(self):
        super(QuestViewModel, self)._initialize()
        self._addNumberProperty(b'number', 0)
        self._addStringProperty(b'title', b'')
        self._addStringProperty(b'description', b'')
        self._addStringProperty(b'condition', b'')
        self._addBoolProperty(b'hasAnimation', False)
        self._addBoolProperty(b'hasManualPage', False)
        self._addStringProperty(b'state')
        self._addArrayProperty(b'rewards', Array())
        self._addNumberProperty(b'currentProgress', -1)
        self._addNumberProperty(b'lastSeenProgress', 0)
        self._addNumberProperty(b'maxProgress', -1)
        return
