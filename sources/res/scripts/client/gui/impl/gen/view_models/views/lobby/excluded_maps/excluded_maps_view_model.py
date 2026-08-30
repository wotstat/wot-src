from enum import Enum
from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.views.lobby.account_dashboard.map_model import MapModel
from gui.impl.gen.view_models.views.lobby.excluded_maps.filter_model import FilterModel
from gui.impl.gen.view_models.views.lobby.excluded_maps.map_item_model import MapItemModel

class MapStateEnum(Enum):
    AVAILABLE = b'Available'
    EXCLUDEDINCOOLDOWN = b'ExcludedInCooldown'
    EXCLUDEDREPLACEABLE = b'ExcludedReplaceable'
    DISABLED = b'Disabled'


class FilterNameEnum(Enum):
    SUMMER = b'summer'
    WINTER = b'winter'
    DESERT = b'desert'


class ExcludedMapsViewModel(ViewModel):
    __slots__ = (b'onBackAction', b'onMapClick', b'onMapRemoveFromSlot', b'onFilterReset', b'onFilterClick')

    def __init__(self, properties=6, commands=5):
        super(ExcludedMapsViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getMapsSelected(self):
        return self._getNumber(0)

    def setMapsSelected(self, value):
        self._setNumber(0, value)
        return

    def getMapsTotal(self):
        return self._getNumber(1)

    def setMapsTotal(self, value):
        self._setNumber(1, value)
        return

    def getIsFilterApplied(self):
        return self._getBool(2)

    def setIsFilterApplied(self, value):
        self._setBool(2, value)
        return

    def getExcludedMaps(self):
        return self._getArray(3)

    def setExcludedMaps(self, value):
        self._setArray(3, value)
        return

    @staticmethod
    def getExcludedMapsType():
        return MapModel

    def getMapFilters(self):
        return self._getArray(4)

    def setMapFilters(self, value):
        self._setArray(4, value)
        return

    @staticmethod
    def getMapFiltersType():
        return FilterModel

    def getMaps(self):
        return self._getArray(5)

    def setMaps(self, value):
        self._setArray(5, value)
        return

    @staticmethod
    def getMapsType():
        return MapItemModel

    def _initialize(self):
        super(ExcludedMapsViewModel, self)._initialize()
        self._addNumberProperty(b'mapsSelected', 0)
        self._addNumberProperty(b'mapsTotal', 0)
        self._addBoolProperty(b'isFilterApplied', False)
        self._addArrayProperty(b'excludedMaps', Array())
        self._addArrayProperty(b'mapFilters', Array())
        self._addArrayProperty(b'maps', Array())
        self.onBackAction = self._addCommand(b'onBackAction')
        self.onMapClick = self._addCommand(b'onMapClick')
        self.onMapRemoveFromSlot = self._addCommand(b'onMapRemoveFromSlot')
        self.onFilterReset = self._addCommand(b'onFilterReset')
        self.onFilterClick = self._addCommand(b'onFilterClick')
        return
