from gui.impl.gen.view_models.views.dialogs.dialog_template_view_model import DialogTemplateViewModel
from gui.impl.gen.view_models.views.lobby.common.vehicle_model import VehicleModel

class RoleChangeDialogModel(DialogTemplateViewModel):
    __slots__ = ()

    def __init__(self, properties=15, commands=2):
        super(RoleChangeDialogModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def currentVehicle(self):
        return self._getViewModel(6)

    @staticmethod
    def getCurrentVehicleType():
        return VehicleModel

    @property
    def newVehicle(self):
        return self._getViewModel(7)

    @staticmethod
    def getNewVehicleType():
        return VehicleModel

    @property
    def currentSpecializationVehicle(self):
        return self._getViewModel(8)

    @staticmethod
    def getCurrentSpecializationVehicleType():
        return VehicleModel

    def getIconName(self):
        return self._getString(9)

    def setIconName(self, value):
        self._setString(9, value)
        return

    def getCurrentRole(self):
        return self._getString(10)

    def setCurrentRole(self, value):
        self._setString(10, value)
        return

    def getNewRole(self):
        return self._getString(11)

    def setNewRole(self, value):
        self._setString(11, value)
        return

    def getIsSkin(self):
        return self._getBool(12)

    def setIsSkin(self, value):
        self._setBool(12, value)
        return

    def getIsTankChange(self):
        return self._getBool(13)

    def setIsTankChange(self, value):
        self._setBool(13, value)
        return

    def getIsSpecializationChange(self):
        return self._getBool(14)

    def setIsSpecializationChange(self, value):
        self._setBool(14, value)
        return

    def _initialize(self):
        super(RoleChangeDialogModel, self)._initialize()
        self._addViewModelProperty(b'currentVehicle', VehicleModel())
        self._addViewModelProperty(b'newVehicle', VehicleModel())
        self._addViewModelProperty(b'currentSpecializationVehicle', VehicleModel())
        self._addStringProperty(b'iconName', b'')
        self._addStringProperty(b'currentRole', b'')
        self._addStringProperty(b'newRole', b'')
        self._addBoolProperty(b'isSkin', False)
        self._addBoolProperty(b'isTankChange', False)
        self._addBoolProperty(b'isSpecializationChange', False)
        return
