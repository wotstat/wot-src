from enum import Enum
from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.personal_missions.pm3_quest_model import Pm3QuestModel
from gui.impl.gen.view_models.views.lobby.personal_missions.pm3_reward_item_model import Pm3RewardItemModel

class CompletedQuestsType(Enum):
    COMPLETE = b'complete'
    COMPLETE_WITH_HONOR = b'completeWithHonor'
    COMPLETE_ADD = b'completeAdd'
    COMPLETE_BASIC = b'completeBasic'


class LineType(Enum):
    HIT = b'hit'
    KILLS = b'kills'
    ASSIST = b'assist'
    BATTLE = b'battle'
    MASTER = b'master'


class PersonalMissionsRewardsViewModel(ViewModel):
    __slots__ = (b'onApply', b'onClose', b'onOpenQuest', b'onChooseReward')

    def __init__(self, properties=15, commands=4):
        super(PersonalMissionsRewardsViewModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def questModel(self):
        return self._getViewModel(0)

    @staticmethod
    def getQuestModelType():
        return Pm3QuestModel

    def getType(self):
        return LineType(self._getString(1))

    def setType(self, value):
        self._setString(1, value.value)
        return

    def getIsOperationAddRewards(self):
        return self._getBool(2)

    def setIsOperationAddRewards(self, value):
        self._setBool(2, value)
        return

    def getIsSelectedRewards(self):
        return self._getBool(3)

    def setIsSelectedRewards(self, value):
        self._setBool(3, value)
        return

    def getQuestID(self):
        return self._getNumber(4)

    def setQuestID(self, value):
        self._setNumber(4, value)
        return

    def getNextQuestID(self):
        return self._getNumber(5)

    def setNextQuestID(self, value):
        self._setNumber(5, value)
        return

    def getValue(self):
        return self._getNumber(6)

    def setValue(self, value):
        self._setNumber(6, value)
        return

    def getMaxValue(self):
        return self._getNumber(7)

    def setMaxValue(self, value):
        self._setNumber(7, value)
        return

    def getDelta(self):
        return self._getNumber(8)

    def setDelta(self, value):
        self._setNumber(8, value)
        return

    def getIsFullChainComplete(self):
        return self._getBool(9)

    def setIsFullChainComplete(self, value):
        self._setBool(9, value)
        return

    def getOperationName(self):
        return self._getString(10)

    def setOperationName(self, value):
        self._setString(10, value)
        return

    def getCurrentTaskName(self):
        return self._getString(11)

    def setCurrentTaskName(self, value):
        self._setString(11, value)
        return

    def getNextTaskName(self):
        return self._getString(12)

    def setNextTaskName(self, value):
        self._setString(12, value)
        return

    def getQuestTypeComplete(self):
        return CompletedQuestsType(self._getString(13))

    def setQuestTypeComplete(self, value):
        self._setString(13, value.value)
        return

    def getRewards(self):
        return self._getArray(14)

    def setRewards(self, value):
        self._setArray(14, value)
        return

    @staticmethod
    def getRewardsType():
        return Pm3RewardItemModel

    def _initialize(self):
        super(PersonalMissionsRewardsViewModel, self)._initialize()
        self._addViewModelProperty(b'questModel', Pm3QuestModel())
        self._addStringProperty(b'type')
        self._addBoolProperty(b'isOperationAddRewards', False)
        self._addBoolProperty(b'isSelectedRewards', False)
        self._addNumberProperty(b'questID', 0)
        self._addNumberProperty(b'nextQuestID', 0)
        self._addNumberProperty(b'value', 0)
        self._addNumberProperty(b'maxValue', 0)
        self._addNumberProperty(b'delta', 0)
        self._addBoolProperty(b'isFullChainComplete', False)
        self._addStringProperty(b'operationName', b'')
        self._addStringProperty(b'currentTaskName', b'')
        self._addStringProperty(b'nextTaskName', b'')
        self._addStringProperty(b'questTypeComplete')
        self._addArrayProperty(b'rewards', Array())
        self.onApply = self._addCommand(b'onApply')
        self.onClose = self._addCommand(b'onClose')
        self.onOpenQuest = self._addCommand(b'onOpenQuest')
        self.onChooseReward = self._addCommand(b'onChooseReward')
        return
