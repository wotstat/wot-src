from enum import Enum
from frameworks.wulf import Array, ViewModel
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.crew.common.filter_toggle_button_model import FilterToggleButtonModel

class ToggleGroupType(Enum):
    DEFAULT = b'default'
    NATION = b'nation'
    LOCATION = b'location'
    TANKMANROLE = b'tankmanRole'
    TANKMANKIND = b'tankmanKind'
    VEHICLEGRADE = b'vehicleGrade'
    VEHICLETIER = b'vehicleTier'
    VEHICLETYPE = b'vehicleType'
    PERSONALDATATYPE = b'personalDataType'
    VEHICLECD = b'vehicle'


class FilterToggleGroupModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=5, commands=0):
        super(FilterToggleGroupModel, self).__init__(properties=properties, commands=commands)
        return

    def getLabel(self):
        return self._getResource(0)

    def setLabel(self, value):
        self._setResource(0, value)
        return

    def getId(self):
        return self._getString(1)

    def setId(self, value):
        self._setString(1, value)
        return

    def getType(self):
        return ToggleGroupType(self._getString(2))

    def setType(self, value):
        self._setString(2, value.value)
        return

    def getHasDiscount(self):
        return self._getBool(3)

    def setHasDiscount(self, value):
        self._setBool(3, value)
        return

    def getFilters(self):
        return self._getArray(4)

    def setFilters(self, value):
        self._setArray(4, value)
        return

    @staticmethod
    def getFiltersType():
        return FilterToggleButtonModel

    def _initialize(self):
        super(FilterToggleGroupModel, self)._initialize()
        self._addResourceProperty(b'label', R.invalid())
        self._addStringProperty(b'id', b'')
        self._addStringProperty(b'type')
        self._addBoolProperty(b'hasDiscount', False)
        self._addArrayProperty(b'filters', Array())
        return
