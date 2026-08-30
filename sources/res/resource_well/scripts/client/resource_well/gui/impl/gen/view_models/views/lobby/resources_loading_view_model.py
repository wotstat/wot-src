from enum import Enum
from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.common.vehicle_info_model import VehicleInfoModel
from resource_well.gui.impl.gen.view_models.views.lobby.resources_tab_model import ResourcesTabModel
from resource_well.gui.impl.gen.view_models.views.lobby.vehicle_counter_model import VehicleCounterModel

class ProgressionState(Enum):
    ACTIVE = b'active'
    NOPROGRESS = b'noProgress'
    NOVEHICLES = b'noVehicles'


class ResourcesLoadingViewModel(ViewModel):
    __slots__ = (b'showHangar', b'close', b'loadResources')

    def __init__(self, properties=7, commands=3):
        super(ResourcesLoadingViewModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def vehicleCounter(self):
        return self._getViewModel(0)

    @staticmethod
    def getVehicleCounterType():
        return VehicleCounterModel

    @property
    def vehicleInfo(self):
        return self._getViewModel(1)

    @staticmethod
    def getVehicleInfoType():
        return VehicleInfoModel

    def getProgressionState(self):
        return ProgressionState(self._getString(2))

    def setProgressionState(self, value):
        self._setString(2, value.value)
        return

    def getProgression(self):
        return self._getNumber(3)

    def setProgression(self, value):
        self._setNumber(3, value)
        return

    def getResourcesTabs(self):
        return self._getArray(4)

    def setResourcesTabs(self, value):
        self._setArray(4, value)
        return

    @staticmethod
    def getResourcesTabsType():
        return ResourcesTabModel

    def getIsLoadingError(self):
        return self._getBool(5)

    def setIsLoadingError(self, value):
        self._setBool(5, value)
        return

    def getShowBlur(self):
        return self._getBool(6)

    def setShowBlur(self, value):
        self._setBool(6, value)
        return

    def _initialize(self):
        super(ResourcesLoadingViewModel, self)._initialize()
        self._addViewModelProperty(b'vehicleCounter', VehicleCounterModel())
        self._addViewModelProperty(b'vehicleInfo', VehicleInfoModel())
        self._addStringProperty(b'progressionState')
        self._addNumberProperty(b'progression', 0)
        self._addArrayProperty(b'resourcesTabs', Array())
        self._addBoolProperty(b'isLoadingError', False)
        self._addBoolProperty(b'showBlur', False)
        self.showHangar = self._addCommand(b'showHangar')
        self.close = self._addCommand(b'close')
        self.loadResources = self._addCommand(b'loadResources')
        return
