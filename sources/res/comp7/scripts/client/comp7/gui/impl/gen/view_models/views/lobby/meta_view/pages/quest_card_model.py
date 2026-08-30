from enum import Enum
from frameworks.wulf import Array, ViewModel
from comp7.gui.impl.gen.view_models.views.lobby.comp7_bonus_model import Comp7BonusModel

class CardState(Enum):
    LOCKED_BY_NO_X_VEHICLES = b'lockedByNoXVehicles'
    LOCKED_BY_INACTIVE_SEASON = b'lockedByInactiveSeason'
    LOCKED_BY_PREVIOUS_QUEST = b'lockedByPreviousQuest'
    ACTIVE = b'active'
    COMPLETED = b'completed'


class QuestCardModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=6, commands=0):
        super(QuestCardModel, self).__init__(properties=properties, commands=commands)
        return

    def getState(self):
        return CardState(self._getString(0))

    def setState(self, value):
        self._setString(0, value.value)
        return

    def getCurrentProgress(self):
        return self._getNumber(1)

    def setCurrentProgress(self, value):
        self._setNumber(1, value)
        return

    def getTotalProgress(self):
        return self._getNumber(2)

    def setTotalProgress(self, value):
        self._setNumber(2, value)
        return

    def getDescription(self):
        return self._getString(3)

    def setDescription(self, value):
        self._setString(3, value)
        return

    def getIconKey(self):
        return self._getString(4)

    def setIconKey(self, value):
        self._setString(4, value)
        return

    def getRewards(self):
        return self._getArray(5)

    def setRewards(self, value):
        self._setArray(5, value)
        return

    @staticmethod
    def getRewardsType():
        return Comp7BonusModel

    def _initialize(self):
        super(QuestCardModel, self)._initialize()
        self._addStringProperty(b'state')
        self._addNumberProperty(b'currentProgress', 0)
        self._addNumberProperty(b'totalProgress', 0)
        self._addStringProperty(b'description', b'')
        self._addStringProperty(b'iconKey', b'')
        self._addArrayProperty(b'rewards', Array())
        return
