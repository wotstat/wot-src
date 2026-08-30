from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from tank_academy.gui.impl.gen.view_models.views.lobby.tank_academy.popovers.filter_control_view_model import FilterControlViewModel
from tank_academy.gui.impl.gen.view_models.views.lobby.tank_academy.tank_academy_vehicle_model import TankAcademyVehicleModel
from tank_academy.gui.impl.gen.view_models.views.lobby.tank_academy.tank_academy_vehicles_selection_tabs_model import TankAcademyVehiclesSelectionTabsModel

class TankAcademyVehiclesSelectionViewModel(ViewModel):
    __slots__ = (b'onGoBack', b'onShowVehicle', b'onCompareVehicle', b'onResetFilter', b'onSelectTab')
    ARG_VEHICLE_ID = b'vehCD'
    ARG_TAB_LEVEL = b'level'
    ARG_TAB_IS_PREMIUM = b'isPremium'

    def __init__(self, properties=6, commands=5):
        super(TankAcademyVehiclesSelectionViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getEndDate(self):
        return self._getNumber(0)

    def setEndDate(self, value):
        self._setNumber(0, value)
        return

    def getTotalVehiclesCount(self):
        return self._getNumber(1)

    def setTotalVehiclesCount(self, value):
        self._setNumber(1, value)
        return

    def getVehicles(self):
        return self._getArray(2)

    def setVehicles(self, value):
        self._setArray(2, value)
        return

    @staticmethod
    def getVehiclesType():
        return TankAcademyVehicleModel

    def getTabs(self):
        return self._getArray(3)

    def setTabs(self, value):
        self._setArray(3, value)
        return

    @staticmethod
    def getTabsType():
        return TankAcademyVehiclesSelectionTabsModel

    def getTypes(self):
        return self._getArray(4)

    def setTypes(self, value):
        self._setArray(4, value)
        return

    @staticmethod
    def getTypesType():
        return FilterControlViewModel

    def getNations(self):
        return self._getArray(5)

    def setNations(self, value):
        self._setArray(5, value)
        return

    @staticmethod
    def getNationsType():
        return FilterControlViewModel

    def _initialize(self):
        super(TankAcademyVehiclesSelectionViewModel, self)._initialize()
        self._addNumberProperty(b'endDate', 0)
        self._addNumberProperty(b'totalVehiclesCount', 0)
        self._addArrayProperty(b'vehicles', Array())
        self._addArrayProperty(b'tabs', Array())
        self._addArrayProperty(b'types', Array())
        self._addArrayProperty(b'nations', Array())
        self.onGoBack = self._addCommand(b'onGoBack')
        self.onShowVehicle = self._addCommand(b'onShowVehicle')
        self.onCompareVehicle = self._addCommand(b'onCompareVehicle')
        self.onResetFilter = self._addCommand(b'onResetFilter')
        self.onSelectTab = self._addCommand(b'onSelectTab')
        return
