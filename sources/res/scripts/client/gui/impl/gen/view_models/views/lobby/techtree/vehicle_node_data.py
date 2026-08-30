from gui.impl.gen.view_models.common.price_model import PriceModel
from gui.impl.gen.view_models.common.vehicle_info_model import VehicleInfoModel
from gui.impl.gen.view_models.views.lobby.techtree.item_unlock import ItemUnlock

class VehicleNodeData(VehicleInfoModel):
    __slots__ = ()

    def __init__(self, properties=14, commands=0):
        super(VehicleNodeData, self).__init__(properties=properties, commands=commands)
        return

    @property
    def price(self):
        return self._getViewModel(10)

    @staticmethod
    def getPriceType():
        return PriceModel

    @property
    def unlock(self):
        return self._getViewModel(11)

    @staticmethod
    def getUnlockType():
        return ItemUnlock

    def getNodeId(self):
        return self._getNumber(12)

    def setNodeId(self, value):
        self._setNumber(12, value)
        return

    def getCanAddToCompare(self):
        return self._getBool(13)

    def setCanAddToCompare(self, value):
        self._setBool(13, value)
        return

    def _initialize(self):
        super(VehicleNodeData, self)._initialize()
        self._addViewModelProperty(b'price', PriceModel())
        self._addViewModelProperty(b'unlock', ItemUnlock())
        self._addNumberProperty(b'nodeId', 0)
        self._addBoolProperty(b'canAddToCompare', False)
        return
