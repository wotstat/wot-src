from enum import Enum
from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.personal_missions.pages.pm3_card_model import Pm3CardModel
from gui.impl.gen.view_models.views.lobby.personal_missions.pm3_quest_model import Pm3QuestModel

class QuestState(Enum):
    NAPREVIOUS = b'previous_progress'
    NAPREVIOUSALL = b'previous_progress_all'
    NATECH = b'no_tech'
    AVAILABLE = b'available'
    INPROGRESS = b'in_progress'
    INPROGRESSHONOR = b'in_progress_honor'
    PAUSE = b'pause'
    DONE = b'done'
    DONEBASIC = b'done_basic'
    DONEHONOR = b'done_honor'
    DONEPAUSE = b'done_pause'


class QuestLineType(Enum):
    HIT = b'hit'
    KILLS = b'kills'
    ASSIST = b'assist'
    BATTLE = b'battle'
    MASTER = b'master'


class Pm3QuestViewModel(ViewModel):
    __slots__ = (b'applyQuest', b'switchSelected', b'backToOperation', b'nextQuest', b'prevQuest', b'getSelectionBonus', b'updateRewards', b'resetQuest', b'pauseQuest')

    def __init__(self, properties=5, commands=9):
        super(Pm3QuestViewModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def questData(self):
        return self._getViewModel(0)

    @staticmethod
    def getQuestDataType():
        return Pm3QuestModel

    def getCardsList(self):
        return self._getArray(1)

    def setCardsList(self, value):
        self._setArray(1, value)
        return

    @staticmethod
    def getCardsListType():
        return Pm3CardModel

    def getTitleValue(self):
        return self._getString(2)

    def setTitleValue(self, value):
        self._setString(2, value)
        return

    def getType(self):
        return QuestLineType(self._getString(3))

    def setType(self, value):
        self._setString(3, value.value)
        return

    def getState(self):
        return QuestState(self._getString(4))

    def setState(self, value):
        self._setString(4, value.value)
        return

    def _initialize(self):
        super(Pm3QuestViewModel, self)._initialize()
        self._addViewModelProperty(b'questData', Pm3QuestModel())
        self._addArrayProperty(b'cardsList', Array())
        self._addStringProperty(b'titleValue', b'')
        self._addStringProperty(b'type')
        self._addStringProperty(b'state')
        self.applyQuest = self._addCommand(b'applyQuest')
        self.switchSelected = self._addCommand(b'switchSelected')
        self.backToOperation = self._addCommand(b'backToOperation')
        self.nextQuest = self._addCommand(b'nextQuest')
        self.prevQuest = self._addCommand(b'prevQuest')
        self.getSelectionBonus = self._addCommand(b'getSelectionBonus')
        self.updateRewards = self._addCommand(b'updateRewards')
        self.resetQuest = self._addCommand(b'resetQuest')
        self.pauseQuest = self._addCommand(b'pauseQuest')
        return
