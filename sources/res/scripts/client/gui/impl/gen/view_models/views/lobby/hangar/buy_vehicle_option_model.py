from enum import Enum
from frameworks.wulf import ViewModel
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.hangar.buy_vehicle_price_model import BuyVehiclePriceModel
from gui.impl.gen.view_models.views.lobby.hangar.buy_vehicle_simple_tooltip_model import BuyVehicleSimpleTooltipModel

class OptionState(Enum):
    DEFAULT = b'default'
    WARNING = b'warning'
    SELECTED = b'selected'
    DISABLED = b'disabled'


class BuyVehicleOptionModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=7, commands=0):
        super(BuyVehicleOptionModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def price(self):
        return self._getViewModel(0)

    @staticmethod
    def getPriceType():
        return BuyVehiclePriceModel

    @property
    def tooltip(self):
        return self._getViewModel(1)

    @staticmethod
    def getTooltipType():
        return BuyVehicleSimpleTooltipModel

    def getName(self):
        return self._getString(2)

    def setName(self, value):
        self._setString(2, value)
        return

    def getOptionState(self):
        return OptionState(self._getString(3))

    def setOptionState(self, value):
        self._setString(3, value.value)
        return

    def getIcon(self):
        return self._getResource(4)

    def setIcon(self, value):
        self._setResource(4, value)
        return

    def getTitle(self):
        return self._getString(5)

    def setTitle(self, value):
        self._setString(5, value)
        return

    def getIsPriceVisible(self):
        return self._getBool(6)

    def setIsPriceVisible(self, value):
        self._setBool(6, value)
        return

    def _initialize(self):
        super(BuyVehicleOptionModel, self)._initialize()
        self._addViewModelProperty(b'price', BuyVehiclePriceModel())
        self._addViewModelProperty(b'tooltip', BuyVehicleSimpleTooltipModel())
        self._addStringProperty(b'name', b'')
        self._addStringProperty(b'optionState')
        self._addResourceProperty(b'icon', R.invalid())
        self._addStringProperty(b'title', b'')
        self._addBoolProperty(b'isPriceVisible', False)
        return
