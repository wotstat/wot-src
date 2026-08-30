from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.common.vehicle_info_model import VehicleInfoModel
from gui.impl.gen.view_models.views.lobby.vehicle_hub.views.sub_models.veh_skill_tree.alternate_configuration_dialog_loadout_model import AlternateConfigurationDialogLoadoutModel

class AlternateConfigurationDialogModel(ViewModel):
    __slots__ = (b'onClose', b'onAffirmate')

    def __init__(self, properties=3, commands=2):
        super(AlternateConfigurationDialogModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def vehicleInfo(self):
        return self._getViewModel(0)

    @staticmethod
    def getVehicleInfoType():
        return VehicleInfoModel

    def getLoadouts(self):
        return self._getArray(1)

    def setLoadouts(self, value):
        self._setArray(1, value)
        return

    @staticmethod
    def getLoadoutsType():
        return AlternateConfigurationDialogLoadoutModel

    def getNodeID(self):
        return self._getNumber(2)

    def setNodeID(self, value):
        self._setNumber(2, value)
        return

    def _initialize(self):
        super(AlternateConfigurationDialogModel, self)._initialize()
        self._addViewModelProperty(b'vehicleInfo', VehicleInfoModel())
        self._addArrayProperty(b'loadouts', Array())
        self._addNumberProperty(b'nodeID', 0)
        self.onClose = self._addCommand(b'onClose')
        self.onAffirmate = self._addCommand(b'onAffirmate')
        return
