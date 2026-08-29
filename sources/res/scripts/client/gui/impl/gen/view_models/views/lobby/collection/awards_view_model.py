from enum import Enum
from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.collection.reward_model import RewardModel

class CollectionAwardState(Enum):
    COMPLETED = b'completed'
    ACTIVE = b'active'


class AwardsViewModel(ViewModel):
    __slots__ = (b'onOpenCollection', b'onCloseCollection')

    def __init__(self, properties=5, commands=2):
        super(AwardsViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getCollectionName(self):
        return self._getString(0)

    def setCollectionName(self, value):
        self._setString(0, value)
        return

    def getIsDisabled(self):
        return self._getBool(1)

    def setIsDisabled(self, value):
        self._setBool(1, value)
        return

    def getBackground(self):
        return self._getString(2)

    def setBackground(self, value):
        self._setString(2, value)
        return

    def getState(self):
        return CollectionAwardState(self._getString(3))

    def setState(self, value):
        self._setString(3, value.value)
        return

    def getRewards(self):
        return self._getArray(4)

    def setRewards(self, value):
        self._setArray(4, value)
        return

    @staticmethod
    def getRewardsType():
        return RewardModel

    def _initialize(self):
        super(AwardsViewModel, self)._initialize()
        self._addStringProperty(b'collectionName', b'')
        self._addBoolProperty(b'isDisabled', False)
        self._addStringProperty(b'background', b'')
        self._addStringProperty(b'state')
        self._addArrayProperty(b'rewards', Array())
        self.onOpenCollection = self._addCommand(b'onOpenCollection')
        self.onCloseCollection = self._addCommand(b'onCloseCollection')
        return
