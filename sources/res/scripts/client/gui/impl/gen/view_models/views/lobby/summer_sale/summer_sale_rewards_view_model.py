from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.common.missions.bonuses.bonus_model import BonusModel

class SummerSaleRewardsViewModel(ViewModel):
    __slots__ = (b'onClose', b'onShowVehicleInHangar')

    def __init__(self, properties=2, commands=2):
        super(SummerSaleRewardsViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getMainRewards(self):
        return self._getArray(0)

    def setMainRewards(self, value):
        self._setArray(0, value)
        return

    @staticmethod
    def getMainRewardsType():
        return BonusModel

    def getRewards(self):
        return self._getArray(1)

    def setRewards(self, value):
        self._setArray(1, value)
        return

    @staticmethod
    def getRewardsType():
        return BonusModel

    def _initialize(self):
        super(SummerSaleRewardsViewModel, self)._initialize()
        self._addArrayProperty(b'mainRewards', Array())
        self._addArrayProperty(b'rewards', Array())
        self.onClose = self._addCommand(b'onClose')
        self.onShowVehicleInHangar = self._addCommand(b'onShowVehicleInHangar')
        return
