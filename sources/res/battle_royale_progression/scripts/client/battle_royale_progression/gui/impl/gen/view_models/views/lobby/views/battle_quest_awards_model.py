from enum import Enum
from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.battle_pass.reward_item_model import RewardItemModel

class BattleStatus(Enum):
    INPROGRESS = b'inProgress'
    COMPLETED = b'completed'


class BattleQuestAwardsModel(ViewModel):
    __slots__ = (b'onApprove', b'onClose')

    def __init__(self, properties=3, commands=2):
        super(BattleQuestAwardsModel, self).__init__(properties=properties, commands=commands)
        return

    def getBattleStatus(self):
        return BattleStatus(self._getString(0))

    def setBattleStatus(self, value):
        self._setString(0, value.value)
        return

    def getLevel(self):
        return self._getNumber(1)

    def setLevel(self, value):
        self._setNumber(1, value)
        return

    def getRewards(self):
        return self._getArray(2)

    def setRewards(self, value):
        self._setArray(2, value)
        return

    @staticmethod
    def getRewardsType():
        return RewardItemModel

    def _initialize(self):
        super(BattleQuestAwardsModel, self)._initialize()
        self._addStringProperty(b'battleStatus')
        self._addNumberProperty(b'level', 0)
        self._addArrayProperty(b'rewards', Array())
        self.onApprove = self._addCommand(b'onApprove')
        self.onClose = self._addCommand(b'onClose')
        return
