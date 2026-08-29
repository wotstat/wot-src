from enum import Enum
from gui.impl.gen import R
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.crew.common.filter_toggle_group_model import FilterToggleGroupModel
from gui.impl.gen.view_models.views.lobby.crew.common.range_model import RangeModel

class FilterPanelType(Enum):
    DEFAULT = b'default'
    BARRACKS = b'barracks'
    MEMBERCHANGE = b'memberChange'
    TANKCHANGE = b'tankChange'
    PERSONALDATA = b'personalData'


class FilterPanelWidgetModel(ViewModel):
    __slots__ = (b'onSearch', b'onUpdateFilter', b'onResetFilter', b'onSelectedModeChange', b'onCancelSelection', b'onDismissOrRestore')

    def __init__(self, properties=19, commands=6):
        super(FilterPanelWidgetModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def amountInfo(self):
        return self._getViewModel(0)

    @staticmethod
    def getAmountInfoType():
        return RangeModel

    @property
    def filter(self):
        return self._getViewModel(1)

    @staticmethod
    def getFilterType():
        return FilterToggleGroupModel

    def getIsSearchEnabled(self):
        return self._getBool(2)

    def setIsSearchEnabled(self, value):
        self._setBool(2, value)
        return

    def getTitle(self):
        return self._getResource(3)

    def setTitle(self, value):
        self._setResource(3, value)
        return

    def getPopoverTooltipHeader(self):
        return self._getResource(4)

    def setPopoverTooltipHeader(self, value):
        self._setResource(4, value)
        return

    def getPopoverTooltipBody(self):
        return self._getResource(5)

    def setPopoverTooltipBody(self, value):
        self._setResource(5, value)
        return

    def getSearchString(self):
        return self._getString(6)

    def setSearchString(self, value):
        self._setString(6, value)
        return

    def getSearchPlaceholder(self):
        return self._getResource(7)

    def setSearchPlaceholder(self, value):
        self._setResource(7, value)
        return

    def getSearchTooltipHeader(self):
        return self._getResource(8)

    def setSearchTooltipHeader(self, value):
        self._setResource(8, value)
        return

    def getSearchTooltipBody(self):
        return self._getString(9)

    def setSearchTooltipBody(self, value):
        self._setString(9, value)
        return

    def getIsPopoverEnabled(self):
        return self._getBool(10)

    def setIsPopoverEnabled(self, value):
        self._setBool(10, value)
        return

    def getIsPopoverHighlighted(self):
        return self._getBool(11)

    def setIsPopoverHighlighted(self, value):
        self._setBool(11, value)
        return

    def getHasDiscountAlert(self):
        return self._getBool(12)

    def setHasDiscountAlert(self, value):
        self._setBool(12, value)
        return

    def getHasAppliedFilters(self):
        return self._getBool(13)

    def setHasAppliedFilters(self, value):
        self._setBool(13, value)
        return

    def getPanelType(self):
        return FilterPanelType(self._getString(14))

    def setPanelType(self, value):
        self._setString(14, value.value)
        return

    def getIsSelectedMode(self):
        return self._getBool(15)

    def setIsSelectedMode(self, value):
        self._setBool(15, value)
        return

    def getIsSelectButtonVisible(self):
        return self._getBool(16)

    def setIsSelectButtonVisible(self, value):
        self._setBool(16, value)
        return

    def getIsSelectButtonActive(self):
        return self._getBool(17)

    def setIsSelectButtonActive(self, value):
        self._setBool(17, value)
        return

    def getIsSelectedLimitReached(self):
        return self._getBool(18)

    def setIsSelectedLimitReached(self, value):
        self._setBool(18, value)
        return

    def _initialize(self):
        super(FilterPanelWidgetModel, self)._initialize()
        self._addViewModelProperty(b'amountInfo', RangeModel())
        self._addViewModelProperty(b'filter', FilterToggleGroupModel())
        self._addBoolProperty(b'isSearchEnabled', False)
        self._addResourceProperty(b'title', R.invalid())
        self._addResourceProperty(b'popoverTooltipHeader', R.invalid())
        self._addResourceProperty(b'popoverTooltipBody', R.invalid())
        self._addStringProperty(b'searchString', b'')
        self._addResourceProperty(b'searchPlaceholder', R.invalid())
        self._addResourceProperty(b'searchTooltipHeader', R.invalid())
        self._addStringProperty(b'searchTooltipBody', b'')
        self._addBoolProperty(b'isPopoverEnabled', True)
        self._addBoolProperty(b'isPopoverHighlighted', False)
        self._addBoolProperty(b'hasDiscountAlert', False)
        self._addBoolProperty(b'hasAppliedFilters', False)
        self._addStringProperty(b'panelType')
        self._addBoolProperty(b'isSelectedMode', False)
        self._addBoolProperty(b'isSelectButtonVisible', True)
        self._addBoolProperty(b'isSelectButtonActive', False)
        self._addBoolProperty(b'isSelectedLimitReached', False)
        self.onSearch = self._addCommand(b'onSearch')
        self.onUpdateFilter = self._addCommand(b'onUpdateFilter')
        self.onResetFilter = self._addCommand(b'onResetFilter')
        self.onSelectedModeChange = self._addCommand(b'onSelectedModeChange')
        self.onCancelSelection = self._addCommand(b'onCancelSelection')
        self.onDismissOrRestore = self._addCommand(b'onDismissOrRestore')
        return
