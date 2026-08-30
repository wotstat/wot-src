from enum import Enum
from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.views.lobby.personal_missions_30.style_bonus_model import StyleBonusModel

class RewardsType(Enum):
    MAIN = b'main'
    OPERATION = b'operation'
    CAMPAIGN = b'campaign'


class MainViewRewardModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(MainViewRewardModel, self).__init__(properties=properties, commands=commands)
        return

    def getItems(self):
        return self._getArray(0)

    def setItems(self, value):
        self._setArray(0, value)
        return

    @staticmethod
    def getItemsType():
        return StyleBonusModel

    def getRewardsType(self):
        return RewardsType(self._getString(1))

    def setRewardsType(self, value):
        self._setString(1, value.value)
        return

    def getCompletedTasks(self):
        return self._getNumber(2)

    def setCompletedTasks(self, value):
        self._setNumber(2, value)
        return

    def getTasksNumber(self):
        return self._getNumber(3)

    def setTasksNumber(self, value):
        self._setNumber(3, value)
        return

    def _initialize(self):
        super(MainViewRewardModel, self)._initialize()
        self._addArrayProperty(b'items', Array())
        self._addStringProperty(b'rewardsType')
        self._addNumberProperty(b'completedTasks', 0)
        self._addNumberProperty(b'tasksNumber', 0)
        return
