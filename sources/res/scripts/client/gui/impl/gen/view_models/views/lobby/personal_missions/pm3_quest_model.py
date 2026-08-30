from enum import Enum
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.personal_missions.pm3_quest_part_model import Pm3QuestPartModel

class ResetButtonState(Enum):
    ENABLED = b'enabled'
    DISABLED = b'disabled'
    INVISIBLE = b'invisible'


class Pm3QuestModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=9, commands=0):
        super(Pm3QuestModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def mainQuests(self):
        return self._getViewModel(0)

    @staticmethod
    def getMainQuestsType():
        return Pm3QuestPartModel

    @property
    def addQuests(self):
        return self._getViewModel(1)

    @staticmethod
    def getAddQuestsType():
        return Pm3QuestPartModel

    def getId(self):
        return self._getNumber(2)

    def setId(self, value):
        self._setNumber(2, value)
        return

    def getName(self):
        return self._getString(3)

    def setName(self, value):
        self._setString(3, value)
        return

    def getIsFinal(self):
        return self._getBool(4)

    def setIsFinal(self, value):
        self._setBool(4, value)
        return

    def getQuestLevelFrom(self):
        return self._getString(5)

    def setQuestLevelFrom(self, value):
        self._setString(5, value)
        return

    def getQuestLevelTo(self):
        return self._getString(6)

    def setQuestLevelTo(self, value):
        self._setString(6, value)
        return

    def getIsPauseButtonEnabled(self):
        return self._getBool(7)

    def setIsPauseButtonEnabled(self, value):
        self._setBool(7, value)
        return

    def getResetButtonStatus(self):
        return ResetButtonState(self._getString(8))

    def setResetButtonStatus(self, value):
        self._setString(8, value.value)
        return

    def _initialize(self):
        super(Pm3QuestModel, self)._initialize()
        self._addViewModelProperty(b'mainQuests', Pm3QuestPartModel())
        self._addViewModelProperty(b'addQuests', Pm3QuestPartModel())
        self._addNumberProperty(b'id', 0)
        self._addStringProperty(b'name', b'')
        self._addBoolProperty(b'isFinal', False)
        self._addStringProperty(b'questLevelFrom', b'')
        self._addStringProperty(b'questLevelTo', b'')
        self._addBoolProperty(b'isPauseButtonEnabled', False)
        self._addStringProperty(b'resetButtonStatus')
        return
