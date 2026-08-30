from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.common.missions.bonuses.bonus_model import BonusModel

class JmNodePopoverModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(JmNodePopoverModel, self).__init__(properties=properties, commands=commands)
        return

    def getRewards(self):
        return self._getArray(0)

    def setRewards(self, value):
        self._setArray(0, value)
        return

    @staticmethod
    def getRewardsType():
        return BonusModel

    def getCoinTokenPrice(self):
        return self._getNumber(1)

    def setCoinTokenPrice(self, value):
        self._setNumber(1, value)
        return

    def getUnlockTokenPrice(self):
        return self._getNumber(2)

    def setUnlockTokenPrice(self, value):
        self._setNumber(2, value)
        return

    def getUnlockTokenNodeId(self):
        return self._getString(3)

    def setUnlockTokenNodeId(self, value):
        self._setString(3, value)
        return

    def _initialize(self):
        super(JmNodePopoverModel, self)._initialize()
        self._addArrayProperty(b'rewards', Array())
        self._addNumberProperty(b'coinTokenPrice', 0)
        self._addNumberProperty(b'unlockTokenPrice', 0)
        self._addStringProperty(b'unlockTokenNodeId', b'')
        return
