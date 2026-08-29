from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.crew.common.tankman_restore_info import TankmanRestoreInfo
from gui.impl.gen.view_models.views.lobby.crew.tooltips.tankman_tooltip_commander_feature import TankmanTooltipCommanderFeature
from gui.impl.gen.view_models.views.lobby.crew.tooltips.tankman_tooltip_vehicle_specialization import TankmanTooltipVehicleSpecialization

class TankmanTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=12, commands=0):
        super(TankmanTooltipModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def currentVehicle(self):
        return self._getViewModel(0)

    @staticmethod
    def getCurrentVehicleType():
        return TankmanTooltipVehicleSpecialization

    @property
    def nativeVehicle(self):
        return self._getViewModel(1)

    @staticmethod
    def getNativeVehicleType():
        return TankmanTooltipVehicleSpecialization

    @property
    def restoreInfo(self):
        return self._getViewModel(2)

    @staticmethod
    def getRestoreInfoType():
        return TankmanRestoreInfo

    def getRole(self):
        return self._getString(3)

    def setRole(self, value):
        self._setString(3, value)
        return

    def getRankIcon(self):
        return self._getString(4)

    def setRankIcon(self, value):
        self._setString(4, value)
        return

    def getFullName(self):
        return self._getString(5)

    def setFullName(self, value):
        self._setString(5, value)
        return

    def getRankUserName(self):
        return self._getString(6)

    def setRankUserName(self, value):
        self._setString(6, value)
        return

    def getIsFemale(self):
        return self._getBool(7)

    def setIsFemale(self, value):
        self._setBool(7, value)
        return

    def getIsDismissed(self):
        return self._getBool(8)

    def setIsDismissed(self, value):
        self._setBool(8, value)
        return

    def getHasFreeRestore(self):
        return self._getBool(9)

    def setHasFreeRestore(self, value):
        self._setBool(9, value)
        return

    def getSecondsLeftToRestore(self):
        return self._getNumber(10)

    def setSecondsLeftToRestore(self, value):
        self._setNumber(10, value)
        return

    def getCommanderFeatures(self):
        return self._getArray(11)

    def setCommanderFeatures(self, value):
        self._setArray(11, value)
        return

    @staticmethod
    def getCommanderFeaturesType():
        return TankmanTooltipCommanderFeature

    def _initialize(self):
        super(TankmanTooltipModel, self)._initialize()
        self._addViewModelProperty(b'currentVehicle', TankmanTooltipVehicleSpecialization())
        self._addViewModelProperty(b'nativeVehicle', TankmanTooltipVehicleSpecialization())
        self._addViewModelProperty(b'restoreInfo', TankmanRestoreInfo())
        self._addStringProperty(b'role', b'')
        self._addStringProperty(b'rankIcon', b'')
        self._addStringProperty(b'fullName', b'')
        self._addStringProperty(b'rankUserName', b'')
        self._addBoolProperty(b'isFemale', False)
        self._addBoolProperty(b'isDismissed', False)
        self._addBoolProperty(b'hasFreeRestore', False)
        self._addNumberProperty(b'secondsLeftToRestore', 0)
        self._addArrayProperty(b'commanderFeatures', Array())
        return
