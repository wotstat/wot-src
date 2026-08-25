from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.common.price_item_model import PriceItemModel
from gui.impl.gen.view_models.common.price_model import PriceModel
from gui.impl.gen.view_models.views.lobby.tank_setup.sub_views.shell_specification_model import ShellSpecificationModel

class ShellModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=16, commands=0):
        super(ShellModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def totalPrice(self):
        return self._getViewModel(0)

    @staticmethod
    def getTotalPriceType():
        return PriceModel

    @property
    def price(self):
        return self._getViewModel(1)

    @staticmethod
    def getPriceType():
        return PriceModel

    @property
    def itemPrice(self):
        return self._getViewModel(2)

    @staticmethod
    def getItemPriceType():
        return PriceItemModel

    def getIntCD(self):
        return self._getNumber(3)

    def setIntCD(self, value):
        self._setNumber(3, value)
        return

    def getInDepotCount(self):
        return self._getNumber(4)

    def setInDepotCount(self, value):
        self._setNumber(4, value)
        return

    def getItemsCount(self):
        return self._getNumber(5)

    def setItemsCount(self, value):
        self._setNumber(5, value)
        return

    def getValue(self):
        return self._getNumber(6)

    def setValue(self, value):
        self._setNumber(6, value)
        return

    def getCount(self):
        return self._getNumber(7)

    def setCount(self, value):
        self._setNumber(7, value)
        return

    def getDelta(self):
        return self._getNumber(8)

    def setDelta(self, value):
        self._setNumber(8, value)
        return

    def getType(self):
        return self._getString(9)

    def setType(self, value):
        self._setString(9, value)
        return

    def getBuyCount(self):
        return self._getNumber(10)

    def setBuyCount(self, value):
        self._setNumber(10, value)
        return

    def getItemInstalledSetupIdx(self):
        return self._getNumber(11)

    def setItemInstalledSetupIdx(self, value):
        self._setNumber(11, value)
        return

    def getIsMounted(self):
        return self._getBool(12)

    def setIsMounted(self, value):
        self._setBool(12, value)
        return

    def getIsMountedMoreThanOne(self):
        return self._getBool(13)

    def setIsMountedMoreThanOne(self, value):
        self._setBool(13, value)
        return

    def getKind(self):
        return self._getString(14)

    def setKind(self, value):
        self._setString(14, value)
        return

    def getPropertiesList(self):
        return self._getArray(15)

    def setPropertiesList(self, value):
        self._setArray(15, value)
        return

    @staticmethod
    def getPropertiesListType():
        return ShellSpecificationModel

    def _initialize(self):
        super(ShellModel, self)._initialize()
        self._addViewModelProperty(b'totalPrice', PriceModel())
        self._addViewModelProperty(b'price', PriceModel())
        self._addViewModelProperty(b'itemPrice', PriceItemModel())
        self._addNumberProperty(b'intCD', 0)
        self._addNumberProperty(b'inDepotCount', 0)
        self._addNumberProperty(b'itemsCount', 0)
        self._addNumberProperty(b'value', 0)
        self._addNumberProperty(b'count', 0)
        self._addNumberProperty(b'delta', 0)
        self._addStringProperty(b'type', b'')
        self._addNumberProperty(b'buyCount', 0)
        self._addNumberProperty(b'itemInstalledSetupIdx', 0)
        self._addBoolProperty(b'isMounted', False)
        self._addBoolProperty(b'isMountedMoreThanOne', False)
        self._addStringProperty(b'kind', b'')
        self._addArrayProperty(b'propertiesList', Array())
        return
