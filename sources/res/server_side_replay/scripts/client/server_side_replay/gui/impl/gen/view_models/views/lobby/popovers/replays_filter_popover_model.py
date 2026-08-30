from enum import Enum, IntEnum
from frameworks.wulf import Array, ViewModel
from server_side_replay.gui.impl.gen.view_models.views.lobby.filter_toggle_group_model import FilterToggleGroupModel
from server_side_replay.gui.impl.gen.view_models.views.lobby.popovers.filter_popover_vehicle_model import FilterPopoverVehicleModel

class VehicleSortColumn(Enum):
    NAME = b'name'
    TIER = b'tier'
    TYPE = b'type'


class Checkboxes(IntEnum):
    PRIMETIME = 0


class ReplaysFilterPopoverModel(ViewModel):
    __slots__ = (b'onCheckboxSelect', b'onLastDaysOptionSelect', b'onUpdateFilter', b'onSelectVehicle', b'onResetFilter', b'onApplyFilter', b'onSortVehiclesByColumn')

    def __init__(self, properties=8, commands=7):
        super(ReplaysFilterPopoverModel, self).__init__(properties=properties, commands=commands)
        return

    def getFilterGroups(self):
        return self._getArray(0)

    def setFilterGroups(self, value):
        self._setArray(0, value)
        return

    @staticmethod
    def getFilterGroupsType():
        return FilterToggleGroupModel

    def getVehicles(self):
        return self._getArray(1)

    def setVehicles(self, value):
        self._setArray(1, value)
        return

    @staticmethod
    def getVehiclesType():
        return FilterPopoverVehicleModel

    def getVehicleSortColumn(self):
        return VehicleSortColumn(self._getString(2))

    def setVehicleSortColumn(self, value):
        self._setString(2, value.value)
        return

    def getIsVehicleSortAscending(self):
        return self._getBool(3)

    def setIsVehicleSortAscending(self, value):
        self._setBool(3, value)
        return

    def getCanResetFilter(self):
        return self._getBool(4)

    def setCanResetFilter(self, value):
        self._setBool(4, value)
        return

    def getCanApplyFilter(self):
        return self._getBool(5)

    def setCanApplyFilter(self, value):
        self._setBool(5, value)
        return

    def getIsPrimeTime(self):
        return self._getBool(6)

    def setIsPrimeTime(self, value):
        self._setBool(6, value)
        return

    def getSelectedLastDays(self):
        return self._getNumber(7)

    def setSelectedLastDays(self, value):
        self._setNumber(7, value)
        return

    def _initialize(self):
        super(ReplaysFilterPopoverModel, self)._initialize()
        self._addArrayProperty(b'filterGroups', Array())
        self._addArrayProperty(b'vehicles', Array())
        self._addStringProperty(b'vehicleSortColumn')
        self._addBoolProperty(b'isVehicleSortAscending', True)
        self._addBoolProperty(b'canResetFilter', False)
        self._addBoolProperty(b'canApplyFilter', True)
        self._addBoolProperty(b'isPrimeTime', False)
        self._addNumberProperty(b'selectedLastDays', 14)
        self.onCheckboxSelect = self._addCommand(b'onCheckboxSelect')
        self.onLastDaysOptionSelect = self._addCommand(b'onLastDaysOptionSelect')
        self.onUpdateFilter = self._addCommand(b'onUpdateFilter')
        self.onSelectVehicle = self._addCommand(b'onSelectVehicle')
        self.onResetFilter = self._addCommand(b'onResetFilter')
        self.onApplyFilter = self._addCommand(b'onApplyFilter')
        self.onSortVehiclesByColumn = self._addCommand(b'onSortVehiclesByColumn')
        return
