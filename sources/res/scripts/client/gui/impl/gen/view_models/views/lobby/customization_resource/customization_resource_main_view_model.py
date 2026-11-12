from enum import IntEnum
from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.customization_resource.customization_resource_exchange_item_model import CustomizationResourceExchangeItemModel
from gui.impl.gen.view_models.views.lobby.customization_resource.customization_resource_exchange_tab_model import CustomizationResourceExchangeTabModel

class ExchangeCaptchaState(IntEnum):
    EMPTY = 0
    INVALID = 1
    VALID = 2


class CustomizationResourceMainViewModel(ViewModel):
    __slots__ = (b'onTabChange', b'onAdd', b'onReduce', b'onSelectAll', b'changeFilter', b'clearFilter', b'onExchange', b'onShowExchangeConfirmation', b'onCloseExchangeConfirmation', b'onCaptchaChange', b'onConfirmExchange', b'onShowInfo', b'onClose', b'onLoadCards')

    def __init__(self, properties=19, commands=14):
        super(CustomizationResourceMainViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getActiveTabId(self):
        return self._getNumber(0)

    def setActiveTabId(self, value):
        self._setNumber(0, value)
        return

    def getTabs(self):
        return self._getArray(1)

    def setTabs(self, value):
        self._setArray(1, value)
        return

    @staticmethod
    def getTabsType():
        return CustomizationResourceExchangeTabModel

    def getItems(self):
        return self._getArray(2)

    def setItems(self, value):
        self._setArray(2, value)
        return

    @staticmethod
    def getItemsType():
        return CustomizationResourceExchangeItemModel

    def getConfirmationTabs(self):
        return self._getArray(3)

    def setConfirmationTabs(self, value):
        self._setArray(3, value)
        return

    @staticmethod
    def getConfirmationTabsType():
        return CustomizationResourceExchangeTabModel

    def getLimit(self):
        return self._getNumber(4)

    def setLimit(self, value):
        self._setNumber(4, value)
        return

    def getCurrencyCode(self):
        return self._getString(5)

    def setCurrencyCode(self, value):
        self._setString(5, value)
        return

    def getCurrencyBalance(self):
        return self._getNumber(6)

    def setCurrencyBalance(self, value):
        self._setNumber(6, value)
        return

    def getSelectedCount(self):
        return self._getNumber(7)

    def setSelectedCount(self, value):
        self._setNumber(7, value)
        return

    def getIsAllSelected(self):
        return self._getBool(8)

    def setIsAllSelected(self, value):
        self._setBool(8, value)
        return

    def getIsLimitReached(self):
        return self._getBool(9)

    def setIsLimitReached(self, value):
        self._setBool(9, value)
        return

    def getNoAvailableItems(self):
        return self._getBool(10)

    def setNoAvailableItems(self, value):
        self._setBool(10, value)
        return

    def getIsAllItemsHiddenByFilter(self):
        return self._getBool(11)

    def setIsAllItemsHiddenByFilter(self, value):
        self._setBool(11, value)
        return

    def getIsExchangeConfirmationVisible(self):
        return self._getBool(12)

    def setIsExchangeConfirmationVisible(self, value):
        self._setBool(12, value)
        return

    def getExchangeItemsCount(self):
        return self._getNumber(13)

    def setExchangeItemsCount(self, value):
        self._setNumber(13, value)
        return

    def getExchangeReward(self):
        return self._getNumber(14)

    def setExchangeReward(self, value):
        self._setNumber(14, value)
        return

    def getCaptchaState(self):
        return ExchangeCaptchaState(self._getNumber(15))

    def setCaptchaState(self, value):
        self._setNumber(15, value.value)
        return

    def getAllItemsCounter(self):
        return self._getNumber(16)

    def setAllItemsCounter(self, value):
        self._setNumber(16, value)
        return

    def getFilteredItemsCounter(self):
        return self._getNumber(17)

    def setFilteredItemsCounter(self, value):
        self._setNumber(17, value)
        return

    def getIsFilteringActive(self):
        return self._getBool(18)

    def setIsFilteringActive(self, value):
        self._setBool(18, value)
        return

    def _initialize(self):
        super(CustomizationResourceMainViewModel, self)._initialize()
        self._addNumberProperty(b'activeTabId', -1)
        self._addArrayProperty(b'tabs', Array())
        self._addArrayProperty(b'items', Array())
        self._addArrayProperty(b'confirmationTabs', Array())
        self._addNumberProperty(b'limit', 0)
        self._addStringProperty(b'currencyCode', b'')
        self._addNumberProperty(b'currencyBalance', 0)
        self._addNumberProperty(b'selectedCount', 0)
        self._addBoolProperty(b'isAllSelected', False)
        self._addBoolProperty(b'isLimitReached', False)
        self._addBoolProperty(b'noAvailableItems', False)
        self._addBoolProperty(b'isAllItemsHiddenByFilter', False)
        self._addBoolProperty(b'isExchangeConfirmationVisible', False)
        self._addNumberProperty(b'exchangeItemsCount', 0)
        self._addNumberProperty(b'exchangeReward', 0)
        self._addNumberProperty(b'captchaState', ExchangeCaptchaState.EMPTY.value)
        self._addNumberProperty(b'allItemsCounter', 0)
        self._addNumberProperty(b'filteredItemsCounter', 0)
        self._addBoolProperty(b'isFilteringActive', False)
        self.onTabChange = self._addCommand(b'onTabChange')
        self.onAdd = self._addCommand(b'onAdd')
        self.onReduce = self._addCommand(b'onReduce')
        self.onSelectAll = self._addCommand(b'onSelectAll')
        self.changeFilter = self._addCommand(b'changeFilter')
        self.clearFilter = self._addCommand(b'clearFilter')
        self.onExchange = self._addCommand(b'onExchange')
        self.onShowExchangeConfirmation = self._addCommand(b'onShowExchangeConfirmation')
        self.onCloseExchangeConfirmation = self._addCommand(b'onCloseExchangeConfirmation')
        self.onCaptchaChange = self._addCommand(b'onCaptchaChange')
        self.onConfirmExchange = self._addCommand(b'onConfirmExchange')
        self.onShowInfo = self._addCommand(b'onShowInfo')
        self.onClose = self._addCommand(b'onClose')
        self.onLoadCards = self._addCommand(b'onLoadCards')
        return
