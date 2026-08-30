from enum import Enum
from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.views.lobby.user_missions.widget.bonus_model import BonusModel

class State(Enum):
    ACTIVE = b'active'
    WAITING = b'waiting'
    REWARD = b'reward'


class WeeklyQuestWidgetTooltipModel(ViewModel):
    __slots__ = ()
    QUESTS_PER_WEEK = 5

    def __init__(self, properties=7, commands=0):
        super(WeeklyQuestWidgetTooltipModel, self).__init__(properties=properties, commands=commands)
        return

    def getState(self):
        return State(self._getString(0))

    def setState(self, value):
        self._setString(0, value.value)
        return

    def getDescription(self):
        return self._getString(1)

    def setDescription(self, value):
        self._setString(1, value)
        return

    def getBonuses(self):
        return self._getArray(2)

    def setBonuses(self, value):
        self._setArray(2, value)
        return

    @staticmethod
    def getBonusesType():
        return BonusModel

    def getQuestsPassed(self):
        return self._getNumber(3)

    def setQuestsPassed(self, value):
        self._setNumber(3, value)
        return

    def getTotalQuests(self):
        return self._getNumber(4)

    def setTotalQuests(self, value):
        self._setNumber(4, value)
        return

    def getQuestNumbersToRewards(self):
        return self._getArray(5)

    def setQuestNumbersToRewards(self, value):
        self._setArray(5, value)
        return

    @staticmethod
    def getQuestNumbersToRewardsType():
        return int

    def getTimeToNewQuests(self):
        return self._getNumber(6)

    def setTimeToNewQuests(self, value):
        self._setNumber(6, value)
        return

    def _initialize(self):
        super(WeeklyQuestWidgetTooltipModel, self)._initialize()
        self._addStringProperty(b'state')
        self._addStringProperty(b'description', b'')
        self._addArrayProperty(b'bonuses', Array())
        self._addNumberProperty(b'questsPassed', 0)
        self._addNumberProperty(b'totalQuests', 0)
        self._addArrayProperty(b'questNumbersToRewards', Array())
        self._addNumberProperty(b'timeToNewQuests', 0)
        return
