from frameworks.wulf import Array
from gui.impl.gen import R
from gui.impl.gen.view_models.common.vehicle_info_model import VehicleInfoModel
from gui.impl.gen.view_models.views.lobby.crew.common.base_crew_view_model import BaseCrewViewModel
from gui.impl.gen.view_models.views.lobby.crew.tankman_container_tab_model import TankmanContainerTabModel

class TankmanContainerViewModel(BaseCrewViewModel):
    __slots__ = (b'onTabChange',)

    def __init__(self, properties=8, commands=5):
        super(TankmanContainerViewModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def vehicleInfo(self):
        return self._getViewModel(2)

    @staticmethod
    def getVehicleInfoType():
        return VehicleInfoModel

    def getCurrentTabId(self):
        return self._getNumber(3)

    def setCurrentTabId(self, value):
        self._setNumber(3, value)
        return

    def getBackground(self):
        return self._getString(4)

    def setBackground(self, value):
        self._setString(4, value)
        return

    def getTabs(self):
        return self._getArray(5)

    def setTabs(self, value):
        self._setArray(5, value)
        return

    @staticmethod
    def getTabsType():
        return TankmanContainerTabModel

    def getNation(self):
        return self._getString(6)

    def setNation(self, value):
        self._setString(6, value)
        return

    def getBackButtonLabel(self):
        return self._getResource(7)

    def setBackButtonLabel(self, value):
        self._setResource(7, value)
        return

    def _initialize(self):
        super(TankmanContainerViewModel, self)._initialize()
        self._addViewModelProperty(b'vehicleInfo', VehicleInfoModel())
        self._addNumberProperty(b'currentTabId', 0)
        self._addStringProperty(b'background', b'')
        self._addArrayProperty(b'tabs', Array())
        self._addStringProperty(b'nation', b'')
        self._addResourceProperty(b'backButtonLabel', R.invalid())
        self.onTabChange = self._addCommand(b'onTabChange')
        return
