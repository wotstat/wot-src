from enum import Enum
from frameworks.wulf import Array, ViewModel

class RoleSection(Enum):
    LIGHTTANK = b'light_tank'
    MEDIUMTANK = b'medium_tank'
    HEAVYTANK = b'heavy_tank'
    ATSPG = b'at_spg'


class FilterSection(Enum):
    NATIONS = b'nations'
    VEHICLETYPES = b'vehicle_types'
    LEVELS = b'levels'
    SPECIALS = b'specials'
    TEXTSEARCH = b'text_search'
    ROLES = b'roles'
    BATTLEPASS = b'battle_pass'


class VehicleFilterModel(ViewModel):
    __slots__ = (b'onSaveFilter', b'onCarouselTypeChange', b'onResetFilter')

    def __init__(self, properties=4, commands=3):
        super(VehicleFilterModel, self).__init__(properties=properties, commands=commands)
        return

    def getFilters(self):
        return self._getString(0)

    def setFilters(self, value):
        self._setString(0, value)
        return

    def getDefaultFilters(self):
        return self._getString(1)

    def setDefaultFilters(self, value):
        self._setString(1, value)
        return

    def getNationsOrder(self):
        return self._getArray(2)

    def setNationsOrder(self, value):
        self._setArray(2, value)
        return

    @staticmethod
    def getNationsOrderType():
        return unicode

    def getCarouselRowCount(self):
        return self._getNumber(3)

    def setCarouselRowCount(self, value):
        self._setNumber(3, value)
        return

    def _initialize(self):
        super(VehicleFilterModel, self)._initialize()
        self._addStringProperty(b'filters', b'')
        self._addStringProperty(b'defaultFilters', b'{}')
        self._addArrayProperty(b'nationsOrder', Array())
        self._addNumberProperty(b'carouselRowCount', 0)
        self.onSaveFilter = self._addCommand(b'onSaveFilter')
        self.onCarouselTypeChange = self._addCommand(b'onCarouselTypeChange')
        self.onResetFilter = self._addCommand(b'onResetFilter')
        return
