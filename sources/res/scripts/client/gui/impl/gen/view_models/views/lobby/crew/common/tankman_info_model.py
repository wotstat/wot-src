from gui.impl.gen.view_models.views.lobby.common.vehicle_model import VehicleModel
from gui.impl.gen.view_models.views.lobby.crew.components.component_base_model import ComponentBaseModel

class TankmanInfoModel(ComponentBaseModel):
    __slots__ = (b'onPlayUniqueVoice', b'onChangeVehicle', b'onRetrain')

    def __init__(self, properties=17, commands=3):
        super(TankmanInfoModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def nativeVehicle(self):
        return self._getViewModel(1)

    @staticmethod
    def getNativeVehicleType():
        return VehicleModel

    @property
    def currentVehicle(self):
        return self._getViewModel(2)

    @staticmethod
    def getCurrentVehicleType():
        return VehicleModel

    def getInvId(self):
        return self._getNumber(3)

    def setInvId(self, value):
        self._setNumber(3, value)
        return

    def getIconName(self):
        return self._getString(4)

    def setIconName(self, value):
        self._setString(4, value)
        return

    def getFullName(self):
        return self._getString(5)

    def setFullName(self, value):
        self._setString(5, value)
        return

    def getDescription(self):
        return self._getString(6)

    def setDescription(self, value):
        self._setString(6, value)
        return

    def getRole(self):
        return self._getString(7)

    def setRole(self, value):
        self._setString(7, value)
        return

    def getSkillsEfficiency(self):
        return self._getReal(8)

    def setSkillsEfficiency(self, value):
        self._setReal(8, value)
        return

    def getIsInSkin(self):
        return self._getBool(9)

    def setIsInSkin(self, value):
        self._setBool(9, value)
        return

    def getIsFemale(self):
        return self._getBool(10)

    def setIsFemale(self, value):
        self._setBool(10, value)
        return

    def getIsCrewLocked(self):
        return self._getBool(11)

    def setIsCrewLocked(self, value):
        self._setBool(11, value)
        return

    def getIsPostProgressionAnimated(self):
        return self._getBool(12)

    def setIsPostProgressionAnimated(self, value):
        self._setBool(12, value)
        return

    def getHasPostProgression(self):
        return self._getBool(13)

    def setHasPostProgression(self, value):
        self._setBool(13, value)
        return

    def getHasUniqueSound(self):
        return self._getBool(14)

    def setHasUniqueSound(self, value):
        self._setBool(14, value)
        return

    def getHasRetrainDiscount(self):
        return self._getBool(15)

    def setHasRetrainDiscount(self, value):
        self._setBool(15, value)
        return

    def getIsWotPlusNativeVehicle(self):
        return self._getBool(16)

    def setIsWotPlusNativeVehicle(self, value):
        self._setBool(16, value)
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
        self._addRealProperty(b'skillsEfficiency', 0.0)
        self._addBoolProperty(b'isInSkin', False)
        self._addBoolProperty(b'isFemale', False)
        self._addBoolProperty(b'isCrewLocked', False)
        self._addBoolProperty(b'isPostProgressionAnimated', False)
        self._addBoolProperty(b'hasPostProgression', False)
        self._addBoolProperty(b'hasUniqueSound', False)
        self._addBoolProperty(b'hasRetrainDiscount', False)
        self._addBoolProperty(b'isWotPlusNativeVehicle', False)
        self.onPlayUniqueVoice = self._addCommand(b'onPlayUniqueVoice')
        self.onChangeVehicle = self._addCommand(b'onChangeVehicle')
        self.onRetrain = self._addCommand(b'onRetrain')
        return
