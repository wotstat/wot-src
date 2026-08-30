from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.views.lobby.collection.reward_model import RewardModel

class AwardsViewModel(ViewModel):
    __slots__ = (b'onOpenCollection',)

    def __init__(self, properties=4, commands=1):
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

    def getRewards(self):
        return self._getArray(3)

    def setRewards(self, value):
        self._setArray(3, value)
        return

    @staticmethod
    def getRewardsType():
        return RewardModel

    def _initialize(self):
        super(AwardsViewModel, self)._initialize()
        self._addStringProperty(b'collectionName', b'')
        self._addBoolProperty(b'isDisabled', False)
        self._addStringProperty(b'background', b'')
        self._addArrayProperty(b'rewards', Array())
        self.onOpenCollection = self._addCommand(b'onOpenCollection')
        return
