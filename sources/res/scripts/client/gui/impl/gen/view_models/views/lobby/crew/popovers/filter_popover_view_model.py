from enum import Enum
from frameworks.wulf import Array
from gui.impl.gen import R
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.crew.common.filter_toggle_group_model import FilterToggleGroupModel
from gui.impl.gen.view_models.views.lobby.crew.popovers.filter_popover_vehicle_model import FilterPopoverVehicleModel

class VehicleSortColumn(Enum):
    NAME = b'name'
    TIER = b'tier'
    TYPE = b'type'


class FilterPopoverViewModel(ViewModel):
    __slots__ = (b'onUpdateFilter', b'onSelectVehicle', b'onResetFilter', b'onSortVehiclesByColumn')

    def __init__(self, properties=7, commands=4):
        super(FilterPopoverViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getTitle(self):
        return self._getResource(0)

    def setTitle(self, value):
        self._setResource(0, value)
        return

    def getFilterGroups(self):
        return self._getArray(1)

    def setFilterGroups(self, value):
        self._setArray(1, value)
        return

    @staticmethod
    def getFilterGroupsType():
        return FilterToggleGroupModel

    def getVehicles(self):
        return self._getArray(2)

    def setVehicles(self, value):
        self._setArray(2, value)
        return

    @staticmethod
    def getVehiclesType():
        return FilterPopoverVehicleModel

    def getVehicleSortColumn(self):
        return VehicleSortColumn(self._getString(3))

    def setVehicleSortColumn(self, value):
        self._setString(3, value.value)
        return

    def getIsVehicleSortAscending(self):
        return self._getBool(4)

    def setIsVehicleSortAscending(self, value):
        self._setBool(4, value)
        return

    def getHasVehicleFilter(self):
        return self._getBool(5)

    def setHasVehicleFilter(self, value):
        self._setBool(5, value)
        return

    def getCanResetFilter(self):
        return self._getBool(6)

    def setCanResetFilter(self, value):
        self._setBool(6, value)
        return

    def _initialize(self):
        super(FilterPopoverViewModel, self)._initialize()
        self._addResourceProperty(b'title', R.invalid())
        self._addArrayProperty(b'filterGroups', Array())
        self._addArrayProperty(b'vehicles', Array())
        self._addStringProperty(b'vehicleSortColumn')
        self._addBoolProperty(b'isVehicleSortAscending', True)
        self._addBoolProperty(b'hasVehicleFilter', False)
        self._addBoolProperty(b'canResetFilter', False)
        self.onUpdateFilter = self._addCommand(b'onUpdateFilter')
        self.onSelectVehicle = self._addCommand(b'onSelectVehicle')
        self.onResetFilter = self._addCommand(b'onResetFilter')
        self.onSortVehiclesByColumn = self._addCommand(b'onSortVehiclesByColumn')
        return
