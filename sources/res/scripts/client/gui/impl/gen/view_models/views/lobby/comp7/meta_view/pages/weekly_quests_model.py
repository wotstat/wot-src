from enum import Enum
from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.comp7.meta_view.pages.progress_points_model import ProgressPointsModel
from gui.impl.gen.view_models.views.lobby.comp7.meta_view.pages.quest_card_model import QuestCardModel

class SeasonState(Enum):
    NOTSTARTED = b'notStarted'
    ACTIVE = b'active'
    LASTWEEK = b'lastWeek'
    FINISHED = b'finished'


class WeeklyQuestsModel(ViewModel):
    __slots__ = (b'onAnimationStart', b'onAnimationEnd')

    def __init__(self, properties=6, commands=2):
        super(WeeklyQuestsModel, self).__init__(properties=properties, commands=commands)
        return

    def getSeasonState(self):
        return SeasonState(self._getString(0))

    def setSeasonState(self, value):
        self._setString(0, value.value)
        return

    def getResetTimeLeft(self):
        return self._getNumber(1)

    def setResetTimeLeft(self, value):
        self._setNumber(1, value)
        return

    def getQuestCards(self):
        return self._getArray(2)

    def setQuestCards(self, value):
        self._setArray(2, value)
        return

    @staticmethod
    def getQuestCardsType():
        return QuestCardModel

    def getCurrentTokenValue(self):
        return self._getNumber(3)

    def setCurrentTokenValue(self, value):
        self._setNumber(3, value)
        return

    def getPreviousTokenValue(self):
        return self._getNumber(4)

    def setPreviousTokenValue(self, value):
        self._setNumber(4, value)
        return

    def getProgressPoints(self):
        return self._getArray(5)

    def setProgressPoints(self, value):
        self._setArray(5, value)
        return

    @staticmethod
    def getProgressPointsType():
        return ProgressPointsModel

    def _initialize(self):
        super(WeeklyQuestsModel, self)._initialize()
        self._addStringProperty(b'seasonState')
        self._addNumberProperty(b'resetTimeLeft', 0)
        self._addArrayProperty(b'questCards', Array())
        self._addNumberProperty(b'currentTokenValue', 0)
        self._addNumberProperty(b'previousTokenValue', 0)
        self._addArrayProperty(b'progressPoints', Array())
        self.onAnimationStart = self._addCommand(b'onAnimationStart')
        self.onAnimationEnd = self._addCommand(b'onAnimationEnd')
        return
