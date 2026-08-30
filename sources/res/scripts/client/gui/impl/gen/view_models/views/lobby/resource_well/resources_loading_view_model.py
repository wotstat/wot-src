from enum import Enum
from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.resource_well.resources_tab_model import ResourcesTabModel
from gui.impl.gen.view_models.views.lobby.resource_well.vehicle_counter_model import VehicleCounterModel

class ProgressionState(Enum):
    ACTIVE = b'active'
    NOPROGRESS = b'noProgress'
    NOVEHICLES = b'noVehicles'
    BEFOREEVENT = b'beforeEvent'


class ResourcesLoadingViewModel(ViewModel):
    __slots__ = (b'showHangar', b'loadResources')

    def __init__(self, properties=5, commands=2):
        super(ResourcesLoadingViewModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def vehicleCounter(self):
        return self._getViewModel(0)

    @staticmethod
    def getVehicleCounterType():
        return VehicleCounterModel

    def getProgressionState(self):
        return ProgressionState(self._getString(1))

    def setProgressionState(self, value):
        self._setString(1, value.value)
        return

    def getProgression(self):
        return self._getNumber(2)

    def setProgression(self, value):
        self._setNumber(2, value)
        return

    def getResourcesTabs(self):
        return self._getArray(3)

    def setResourcesTabs(self, value):
        self._setArray(3, value)
        return

    @staticmethod
    def getResourcesTabsType():
        return ResourcesTabModel

    def getIsLoadingError(self):
        return self._getBool(4)

    def setIsLoadingError(self, value):
        self._setBool(4, value)
        return

    def _initialize(self):
        super(ResourcesLoadingViewModel, self)._initialize()
        self._addViewModelProperty(b'vehicleCounter', VehicleCounterModel())
        self._addStringProperty(b'progressionState')
        self._addNumberProperty(b'progression', 0)
        self._addArrayProperty(b'resourcesTabs', Array())
        self._addBoolProperty(b'isLoadingError', False)
        self.showHangar = self._addCommand(b'showHangar')
        self.loadResources = self._addCommand(b'loadResources')
        return
