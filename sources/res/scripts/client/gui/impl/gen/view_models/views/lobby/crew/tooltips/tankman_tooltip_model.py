from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.common.vehicle_info_model import VehicleInfoModel
from gui.impl.gen.view_models.views.lobby.crew.common.tankman_restore_info import TankmanRestoreInfo
from gui.impl.gen.view_models.views.lobby.crew.tooltips.tankman_tooltip_modifier_model import TankmanTooltipModifierModel

class TankmanTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=18, commands=0):
        super(TankmanTooltipModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def currentVehicle(self):
        return self._getViewModel(0)

    @staticmethod
    def getCurrentVehicleType():
        return VehicleInfoModel

    @property
    def nativeVehicle(self):
        return self._getViewModel(1)

    @staticmethod
    def getNativeVehicleType():
        return VehicleInfoModel

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
        return TankmanTooltipModifierModel

    def getPerks(self):
        return self._getArray(12)

    def setPerks(self, value):
        self._setArray(12, value)
        return

    @staticmethod
    def getPerksType():
        return TankmanTooltipModifierModel

    def getConsumables(self):
        return self._getArray(13)

    def setConsumables(self, value):
        self._setArray(13, value)
        return

    @staticmethod
    def getConsumablesType():
        return TankmanTooltipModifierModel

    def getFinalEfficiencyValue(self):
        return self._getReal(14)

    def setFinalEfficiencyValue(self, value):
        self._setReal(14, value)
        return

    def getIsInfoAdvanced(self):
        return self._getBool(15)

    def setIsInfoAdvanced(self, value):
        self._setBool(15, value)
        return

    def getVoiceoverReason(self):
        return self._getString(16)

    def setVoiceoverReason(self, value):
        self._setString(16, value)
        return

    def getSkillsEfficiency(self):
        return self._getReal(17)

    def setSkillsEfficiency(self, value):
        self._setReal(17, value)
        return

    def _initialize(self):
        super(TankmanTooltipModel, self)._initialize()
        self._addViewModelProperty(b'currentVehicle', VehicleInfoModel())
        self._addViewModelProperty(b'nativeVehicle', VehicleInfoModel())
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
        self._addArrayProperty(b'perks', Array())
        self._addArrayProperty(b'consumables', Array())
        self._addRealProperty(b'finalEfficiencyValue', 0.0)
        self._addBoolProperty(b'isInfoAdvanced', False)
        self._addStringProperty(b'voiceoverReason', b'')
        self._addRealProperty(b'skillsEfficiency', 0.0)
        return
