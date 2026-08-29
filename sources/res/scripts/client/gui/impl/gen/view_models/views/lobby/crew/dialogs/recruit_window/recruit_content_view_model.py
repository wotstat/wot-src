from enum import Enum
from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.crew.dialogs.recruit_window.drop_down_item_view_model import DropDownItemViewModel
from gui.impl.gen.view_models.views.lobby.crew.dialogs.recruit_window.vehicle_item_view_model import VehicleItemViewModel

class DropDownState(Enum):
    NORMAL = b'normal'
    DISABLED = b'disabled'
    LOCKED = b'locked'


class RecruitContentViewModel(ViewModel):
    __slots__ = (b'onNationChange', b'onVehTypeChange', b'onVehicleChange', b'onSpecializationChange')

    def __init__(self, properties=12, commands=4):
        super(RecruitContentViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getNationState(self):
        return DropDownState(self._getString(0))

    def setNationState(self, value):
        self._setString(0, value.value)
        return

    def getVehTypeState(self):
        return DropDownState(self._getString(1))

    def setVehTypeState(self, value):
        self._setString(1, value.value)
        return

    def getVehicleState(self):
        return DropDownState(self._getString(2))

    def setVehicleState(self, value):
        self._setString(2, value.value)
        return

    def getSpecializationState(self):
        return DropDownState(self._getString(3))

    def setSpecializationState(self, value):
        self._setString(3, value.value)
        return

    def getSelectedNation(self):
        return self._getString(4)

    def setSelectedNation(self, value):
        self._setString(4, value)
        return

    def getNations(self):
        return self._getArray(5)

    def setNations(self, value):
        self._setArray(5, value)
        return

    @staticmethod
    def getNationsType():
        return DropDownItemViewModel

    def getSelectedVehType(self):
        return self._getString(6)

    def setSelectedVehType(self, value):
        self._setString(6, value)
        return

    def getVehTypes(self):
        return self._getArray(7)

    def setVehTypes(self, value):
        self._setArray(7, value)
        return

    @staticmethod
    def getVehTypesType():
        return DropDownItemViewModel

    def getSelectedVehicle(self):
        return self._getString(8)

    def setSelectedVehicle(self, value):
        self._setString(8, value)
        return

    def getVehicles(self):
        return self._getArray(9)

    def setVehicles(self, value):
        self._setArray(9, value)
        return

    @staticmethod
    def getVehiclesType():
        return VehicleItemViewModel

    def getSelectedSpecialization(self):
        return self._getString(10)

    def setSelectedSpecialization(self, value):
        self._setString(10, value)
        return

    def getSpecializations(self):
        return self._getArray(11)

    def setSpecializations(self, value):
        self._setArray(11, value)
        return

    @staticmethod
    def getSpecializationsType():
        return DropDownItemViewModel

    def _initialize(self):
        super(RecruitContentViewModel, self)._initialize()
        self._addStringProperty(b'nationState')
        self._addStringProperty(b'vehTypeState')
        self._addStringProperty(b'vehicleState')
        self._addStringProperty(b'specializationState')
        self._addStringProperty(b'selectedNation', b'-1')
        self._addArrayProperty(b'nations', Array())
        self._addStringProperty(b'selectedVehType', b'-1')
        self._addArrayProperty(b'vehTypes', Array())
        self._addStringProperty(b'selectedVehicle', b'-1')
        self._addArrayProperty(b'vehicles', Array())
        self._addStringProperty(b'selectedSpecialization', b'-1')
        self._addArrayProperty(b'specializations', Array())
        self.onNationChange = self._addCommand(b'onNationChange')
        self.onVehTypeChange = self._addCommand(b'onVehTypeChange')
        self.onVehicleChange = self._addCommand(b'onVehicleChange')
        self.onSpecializationChange = self._addCommand(b'onSpecializationChange')
        return
