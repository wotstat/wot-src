from enum import Enum
from frameworks.wulf import Array, ViewModel
from comp7.gui.impl.gen.view_models.views.lobby.weekly_quest_model import WeeklyQuestModel

class State(Enum):
    HIDE = b'hide'
    ACTIVE = b'active'
    WAITING = b'waiting'
    REWARD = b'reward'


class WeeklyQuestsWidgetModel(ViewModel):
    __slots__ = (b'onGoToWeeklyQuests', b'onMissionClick', b'onMarkAsViewed', b'onGoToRewardsSelection', b'onPollServerTime')

    def __init__(self, properties=6, commands=5):
        super(WeeklyQuestsWidgetModel, self).__init__(properties=properties, commands=commands)
        return

    def getQuests(self):
        return self._getArray(0)

    def setQuests(self, value):
        self._setArray(0, value)
        return

    @staticmethod
    def getQuestsType():
        return WeeklyQuestModel

    def getState(self):
        return State(self._getString(1))

    def setState(self, value):
        self._setString(1, value.value)
        return

    def getQuestsCompleted(self):
        return self._getNumber(2)

    def setQuestsCompleted(self, value):
        self._setNumber(2, value)
        return

    def getTotalQuestsCount(self):
        return self._getNumber(3)

    def setTotalQuestsCount(self, value):
        self._setNumber(3, value)
        return

    def getLeftToNewQuestsTimestamp(self):
        return self._getNumber(4)

    def setLeftToNewQuestsTimestamp(self, value):
        self._setNumber(4, value)
        return

    def getServerTimestamp(self):
        return self._getNumber(5)

    def setServerTimestamp(self, value):
        self._setNumber(5, value)
        return

    def _initialize(self):
        super(WeeklyQuestsWidgetModel, self)._initialize()
        self._addArrayProperty(b'quests', Array())
        self._addStringProperty(b'state')
        self._addNumberProperty(b'questsCompleted', 0)
        self._addNumberProperty(b'totalQuestsCount', 0)
        self._addNumberProperty(b'leftToNewQuestsTimestamp', 0)
        self._addNumberProperty(b'serverTimestamp', 0)
        self.onGoToWeeklyQuests = self._addCommand(b'onGoToWeeklyQuests')
        self.onMissionClick = self._addCommand(b'onMissionClick')
        self.onMarkAsViewed = self._addCommand(b'onMarkAsViewed')
        self.onGoToRewardsSelection = self._addCommand(b'onGoToRewardsSelection')
        self.onPollServerTime = self._addCommand(b'onPollServerTime')
        return
