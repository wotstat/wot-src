from frameworks.wulf import Array, ViewModel
from halloween.gui.impl.gen.view_models.views.common.bonus_item_view_model import BonusItemViewModel
from halloween.gui.impl.gen.view_models.views.lobby.vehicle_title_view_model import VehicleTitleViewModel

class KingRewardCongratsViewModel(ViewModel):
    __slots__ = (b'onClose', b'onToGarageClick', b'onToOutroClick')

    def __init__(self, properties=2, commands=3):
        super(KingRewardCongratsViewModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def mainGiftVehicle(self):
        return self._getViewModel(0)

    @staticmethod
    def getMainGiftVehicleType():
        return VehicleTitleViewModel

    def getRewards(self):
        return self._getArray(1)

    def setRewards(self, value):
        self._setArray(1, value)
        return

    @staticmethod
    def getRewardsType():
        return BonusItemViewModel

    def _initialize(self):
        super(KingRewardCongratsViewModel, self)._initialize()
        self._addViewModelProperty(b'mainGiftVehicle', VehicleTitleViewModel())
        self._addArrayProperty(b'rewards', Array())
        self.onClose = self._addCommand(b'onClose')
        self.onToGarageClick = self._addCommand(b'onToGarageClick')
        self.onToOutroClick = self._addCommand(b'onToOutroClick')
        return
