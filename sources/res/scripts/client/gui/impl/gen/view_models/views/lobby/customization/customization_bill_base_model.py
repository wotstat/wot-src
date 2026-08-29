from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.common.price_model import PriceModel

class CustomizationBillBaseModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=10, commands=0):
        super(CustomizationBillBaseModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def buyPrice(self):
        return self._getViewModel(0)

    @staticmethod
    def getBuyPriceType():
        return PriceModel

    def getBuyButtonEnabled(self):
        return self._getBool(1)

    def setBuyButtonEnabled(self, value):
        self._setBool(1, value)
        return

    def getIsVehicleCustomized(self):
        return self._getBool(2)

    def setIsVehicleCustomized(self, value):
        self._setBool(2, value)
        return

    def getIsApplyButton(self):
        return self._getBool(3)

    def setIsApplyButton(self, value):
        self._setBool(3, value)
        return

    def getIsGoldPrice(self):
        return self._getBool(4)

    def setIsGoldPrice(self, value):
        self._setBool(4, value)
        return

    def getIsEnoughMoney(self):
        return self._getBool(5)

    def setIsEnoughMoney(self, value):
        self._setBool(5, value)
        return

    def getIsRentable(self):
        return self._getBool(6)

    def setIsRentable(self, value):
        self._setBool(6, value)
        return

    def getRentCount(self):
        return self._getNumber(7)

    def setRentCount(self, value):
        self._setNumber(7, value)
        return

    def getInStorageCount(self):
        return self._getNumber(8)

    def setInStorageCount(self, value):
        self._setNumber(8, value)
        return

    def getLockedCount(self):
        return self._getNumber(9)

    def setLockedCount(self, value):
        self._setNumber(9, value)
        return

    def _initialize(self):
        super(CustomizationBillBaseModel, self)._initialize()
        self._addViewModelProperty(b'buyPrice', PriceModel())
        self._addBoolProperty(b'buyButtonEnabled', False)
        self._addBoolProperty(b'isVehicleCustomized', False)
        self._addBoolProperty(b'isApplyButton', False)
        self._addBoolProperty(b'isGoldPrice', False)
        self._addBoolProperty(b'isEnoughMoney', False)
        self._addBoolProperty(b'isRentable', False)
        self._addNumberProperty(b'rentCount', 0)
        self._addNumberProperty(b'inStorageCount', 0)
        self._addNumberProperty(b'lockedCount', 0)
        return
