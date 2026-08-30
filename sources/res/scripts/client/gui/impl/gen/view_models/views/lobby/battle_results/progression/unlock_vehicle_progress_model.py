from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.common.price_item_model import PriceItemModel

class UnlockVehicleProgressModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=8, commands=0):
        super(UnlockVehicleProgressModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def price(self):
        return self._getViewModel(0)

    @staticmethod
    def getPriceType():
        return PriceItemModel

    def getVehicleId(self):
        return self._getNumber(1)

    def setVehicleId(self, value):
        self._setNumber(1, value)
        return

    def getUserName(self):
        return self._getString(2)

    def setUserName(self, value):
        self._setString(2, value)
        return

    def getVehicleIcon(self):
        return self._getString(3)

    def setVehicleIcon(self, value):
        self._setString(3, value)
        return

    def getVehicleType(self):
        return self._getString(4)

    def setVehicleType(self, value):
        self._setString(4, value)
        return

    def getNationName(self):
        return self._getString(5)

    def setNationName(self, value):
        self._setString(5, value)
        return

    def getLevel(self):
        return self._getNumber(6)

    def setLevel(self, value):
        self._setNumber(6, value)
        return

    def getAvgBattlesTillUnlock(self):
        return self._getNumber(7)

    def setAvgBattlesTillUnlock(self, value):
        self._setNumber(7, value)
        return

    def _initialize(self):
        super(UnlockVehicleProgressModel, self)._initialize()
        self._addViewModelProperty(b'price', PriceItemModel())
        self._addNumberProperty(b'vehicleId', 0)
        self._addStringProperty(b'userName', b'')
        self._addStringProperty(b'vehicleIcon', b'')
        self._addStringProperty(b'vehicleType', b'')
        self._addStringProperty(b'nationName', b'')
        self._addNumberProperty(b'level', 0)
        self._addNumberProperty(b'avgBattlesTillUnlock', 0)
        return
