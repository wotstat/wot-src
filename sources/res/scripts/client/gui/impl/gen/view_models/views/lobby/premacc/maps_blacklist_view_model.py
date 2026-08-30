from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.ui_kit.list_model import ListModel

class MapsBlacklistViewModel(ViewModel):
    __slots__ = (b'onBackAction', b'onCloseEvent', b'onMapAddToBlacklistEvent', b'onMapRemoveFromBlacklistEvent', b'onFilterReset', b'onInitialized', b'onFilterClick', b'onShopOpenWotPlus', b'onShopOpenPremium')

    def __init__(self, properties=7, commands=9):
        super(MapsBlacklistViewModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def disabledMaps(self):
        return self._getViewModel(0)

    @staticmethod
    def getDisabledMapsType():
        return ListModel

    @property
    def mapsFilters(self):
        return self._getViewModel(1)

    @staticmethod
    def getMapsFiltersType():
        return ListModel

    @property
    def maps(self):
        return self._getViewModel(2)

    @staticmethod
    def getMapsType():
        return ListModel

    def getCooldownTime(self):
        return self._getNumber(3)

    def setCooldownTime(self, value):
        self._setNumber(3, value)
        return

    def getMapsSelected(self):
        return self._getNumber(4)

    def setMapsSelected(self, value):
        self._setNumber(4, value)
        return

    def getMapsTotal(self):
        return self._getNumber(5)

    def setMapsTotal(self, value):
        self._setNumber(5, value)
        return

    def getIsFilterApplied(self):
        return self._getBool(6)

    def setIsFilterApplied(self, value):
        self._setBool(6, value)
        return

    def _initialize(self):
        super(MapsBlacklistViewModel, self)._initialize()
        self._addViewModelProperty(b'disabledMaps', ListModel())
        self._addViewModelProperty(b'mapsFilters', ListModel())
        self._addViewModelProperty(b'maps', ListModel())
        self._addNumberProperty(b'cooldownTime', 0)
        self._addNumberProperty(b'mapsSelected', 0)
        self._addNumberProperty(b'mapsTotal', 0)
        self._addBoolProperty(b'isFilterApplied', False)
        self.onBackAction = self._addCommand(b'onBackAction')
        self.onCloseEvent = self._addCommand(b'onCloseEvent')
        self.onMapAddToBlacklistEvent = self._addCommand(b'onMapAddToBlacklistEvent')
        self.onMapRemoveFromBlacklistEvent = self._addCommand(b'onMapRemoveFromBlacklistEvent')
        self.onFilterReset = self._addCommand(b'onFilterReset')
        self.onInitialized = self._addCommand(b'onInitialized')
        self.onFilterClick = self._addCommand(b'onFilterClick')
        self.onShopOpenWotPlus = self._addCommand(b'onShopOpenWotPlus')
        self.onShopOpenPremium = self._addCommand(b'onShopOpenPremium')
        return
