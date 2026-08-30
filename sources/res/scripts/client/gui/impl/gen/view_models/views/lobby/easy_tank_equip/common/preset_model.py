from enum import Enum
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.common.price_model import PriceModel

class PresetDisableReason(Enum):
    NONE = b'none'
    DEMOUNT_NOT_POSSIBLE = b'demountNotPossible'
    NOT_ENOUGH_BUNKS = b'notEnoughBunks'


class PresetModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=5, commands=0):
        super(PresetModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def price(self):
        return self._getViewModel(0)

    @staticmethod
    def getPriceType():
        return PriceModel

    def getInstalled(self):
        return self._getBool(1)

    def setInstalled(self, value):
        self._setBool(1, value)
        return

    def getDisableReason(self):
        return PresetDisableReason(self._getString(2))

    def setDisableReason(self, value):
        self._setString(2, value.value)
        return

    def getStoredItemsCount(self):
        return self._getNumber(3)

    def setStoredItemsCount(self, value):
        self._setNumber(3, value)
        return

    def getInstalledItemsCount(self):
        return self._getNumber(4)

    def setInstalledItemsCount(self, value):
        self._setNumber(4, value)
        return

    def _initialize(self):
        super(PresetModel, self)._initialize()
        self._addViewModelProperty(b'price', PriceModel())
        self._addBoolProperty(b'installed', False)
        self._addStringProperty(b'disableReason')
        self._addNumberProperty(b'storedItemsCount', 0)
        self._addNumberProperty(b'installedItemsCount', 0)
        return
