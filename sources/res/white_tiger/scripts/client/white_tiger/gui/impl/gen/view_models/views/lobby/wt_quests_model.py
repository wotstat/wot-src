from enum import Enum
from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from white_tiger.gui.impl.gen.view_models.views.lobby.wt_quest_model import WtQuestModel

class QuestsTabType(Enum):
    ENGINEER = b'ENGINEER'
    HARRIER = b'HARRIER'


class WtQuestsModel(ViewModel):
    __slots__ = (b'onSelectedTab',)

    def __init__(self, properties=6, commands=1):
        super(WtQuestsModel, self).__init__(properties=properties, commands=commands)
        return

    def getActiveTab(self):
        return QuestsTabType(self._getString(0))

    def setActiveTab(self, value):
        self._setString(0, value.value)
        return

    def getHarrierQuests(self):
        return self._getArray(1)

    def setHarrierQuests(self, value):
        self._setArray(1, value)
        return

    @staticmethod
    def getHarrierQuestsType():
        return WtQuestModel

    def getHarrierQuestsVisited(self):
        return self._getArray(2)

    def setHarrierQuestsVisited(self, value):
        self._setArray(2, value)
        return

    def getEngineerQuests(self):
        return self._getArray(3)

    def setEngineerQuests(self, value):
        self._setArray(3, value)
        return

    @staticmethod
    def getEngineerQuestsType():
        return WtQuestModel

    def getEngineerQuestsVisited(self):
        return self._getArray(4)

    def setEngineerQuestsVisited(self, value):
        self._setArray(4, value)
        return

    def getUpdateCountdown(self):
        return self._getNumber(5)

    def setUpdateCountdown(self, value):
        self._setNumber(5, value)
        return

    def _initialize(self):
        super(WtQuestsModel, self)._initialize()
        self._addStringProperty(b'activeTab')
        self._addArrayProperty(b'harrierQuests', Array())
        self._addArrayProperty(b'harrierQuestsVisited', Array())
        self._addArrayProperty(b'engineerQuests', Array())
        self._addArrayProperty(b'engineerQuestsVisited', Array())
        self._addNumberProperty(b'updateCountdown', -1)
        self.onSelectedTab = self._addCommand(b'onSelectedTab')
        return
