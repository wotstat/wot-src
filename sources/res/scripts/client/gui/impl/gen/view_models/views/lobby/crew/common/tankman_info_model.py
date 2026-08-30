from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.common.vehicle_model import VehicleModel

class TankmanInfoModel(ViewModel):
    __slots__ = (b'onPlayUniqueVoice', b'onChangeVehicle', b'onRetrain', b'onEditProfileClick')

    def __init__(self, properties=15, commands=4):
        super(TankmanInfoModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def nativeVehicle(self):
        return self._getViewModel(0)

    @staticmethod
    def getNativeVehicleType():
        return VehicleModel

    @property
    def currentVehicle(self):
        return self._getViewModel(1)

    @staticmethod
    def getCurrentVehicleType():
        return VehicleModel

    def getInvId(self):
        return self._getNumber(2)

    def setInvId(self, value):
        self._setNumber(2, value)
        return

    def getIconName(self):
        return self._getString(3)

    def setIconName(self, value):
        self._setString(3, value)
        return

    def getFullName(self):
        return self._getString(4)

    def setFullName(self, value):
        self._setString(4, value)
        return

    def getDescription(self):
        return self._getString(5)

    def setDescription(self, value):
        self._setString(5, value)
        return

    def getRole(self):
        return self._getString(6)

    def setRole(self, value):
        self._setString(6, value)
        return

    def getRealRoleLevel(self):
        return self._getNumber(7)

    def setRealRoleLevel(self, value):
        self._setNumber(7, value)
        return

    def getNativeTankRealRoleLevel(self):
        return self._getNumber(8)

    def setNativeTankRealRoleLevel(self, value):
        self._setNumber(8, value)
        return

    def getRoleLevel(self):
        return self._getNumber(9)

    def setRoleLevel(self, value):
        self._setNumber(9, value)
        return

    def getHasRetrainDiscount(self):
        return self._getBool(10)

    def setHasRetrainDiscount(self, value):
        self._setBool(10, value)
        return

    def getIsInSkin(self):
        return self._getBool(11)

    def setIsInSkin(self, value):
        self._setBool(11, value)
        return

    def getIsFemale(self):
        return self._getBool(12)

    def setIsFemale(self, value):
        self._setBool(12, value)
        return

    def getIsCrewLocked(self):
        return self._getBool(13)

    def setIsCrewLocked(self, value):
        self._setBool(13, value)
        return

    def getHasUniqueSound(self):
        return self._getBool(14)

    def setHasUniqueSound(self, value):
        self._setBool(14, value)
        return

    def _initialize(self):
        super(TankmanInfoModel, self)._initialize()
        self._addViewModelProperty(b'nativeVehicle', VehicleModel())
        self._addViewModelProperty(b'currentVehicle', VehicleModel())
        self._addNumberProperty(b'invId', 0)
        self._addStringProperty(b'iconName', b'')
        self._addStringProperty(b'fullName', b'')
        self._addStringProperty(b'description', b'')
        self._addStringProperty(b'role', b'')
        self._addNumberProperty(b'realRoleLevel', 0)
        self._addNumberProperty(b'nativeTankRealRoleLevel', 0)
        self._addNumberProperty(b'roleLevel', 0)
        self._addBoolProperty(b'hasRetrainDiscount', False)
        self._addBoolProperty(b'isInSkin', False)
        self._addBoolProperty(b'isFemale', False)
        self._addBoolProperty(b'isCrewLocked', False)
        self._addBoolProperty(b'hasUniqueSound', False)
        self.onPlayUniqueVoice = self._addCommand(b'onPlayUniqueVoice')
        self.onChangeVehicle = self._addCommand(b'onChangeVehicle')
        self.onRetrain = self._addCommand(b'onRetrain')
        self.onEditProfileClick = self._addCommand(b'onEditProfileClick')
        return
