from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.views.lobby.loadout.crew.bonus_skills_model import BonusSkillsModel
from gui.impl.gen.view_models.views.lobby.loadout.crew.native_vehicle import NativeVehicle
from gui.impl.gen.view_models.views.lobby.loadout.crew.perk_model import PerkModel
from gui.impl.gen.view_models.views.lobby.loadout.crew.vehicle_bonus import VehicleBonus
from gui.impl.gen.view_models.views.lobby.loadout.crew.vehicle_bonus_detail_model import VehicleBonusDetailModel

class TankmanModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=23, commands=0):
        super(TankmanModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def vehicleBonus(self):
        return self._getViewModel(0)

    @staticmethod
    def getVehicleBonusType():
        return VehicleBonus

    @property
    def nativeVehicle(self):
        return self._getViewModel(1)

    @staticmethod
    def getNativeVehicleType():
        return NativeVehicle

    def getId(self):
        return self._getNumber(2)

    def setId(self, value):
        self._setNumber(2, value)
        return

    def getLevel(self):
        return self._getNumber(3)

    def setLevel(self, value):
        self._setNumber(3, value)
        return

    def getMaxLevelAchieved(self):
        return self._getBool(4)

    def setMaxLevelAchieved(self, value):
        self._setBool(4, value)
        return

    def getCrewSkinId(self):
        return self._getString(5)

    def setCrewSkinId(self, value):
        self._setString(5, value)
        return

    def getCustomizedSkin(self):
        return self._getBool(6)

    def setCustomizedSkin(self, value):
        self._setBool(6, value)
        return

    def getNewPerksCount(self):
        return self._getNumber(7)

    def setNewPerksCount(self, value):
        self._setNumber(7, value)
        return

    def getNewBonusPerksCount(self):
        return self._getNumber(8)

    def setNewBonusPerksCount(self, value):
        self._setNumber(8, value)
        return

    def getTrainingProgress(self):
        return self._getNumber(9)

    def setTrainingProgress(self, value):
        self._setNumber(9, value)
        return

    def getQuickTraining(self):
        return self._getBool(10)

    def setQuickTraining(self, value):
        self._setBool(10, value)
        return

    def getPerks(self):
        return self._getArray(11)

    def setPerks(self, value):
        self._setArray(11, value)
        return

    @staticmethod
    def getPerksType():
        return PerkModel

    def getBonusSkills(self):
        return self._getArray(12)

    def setBonusSkills(self, value):
        self._setArray(12, value)
        return

    @staticmethod
    def getBonusSkillsType():
        return BonusSkillsModel

    def getVehicleBonusDetails(self):
        return self._getArray(13)

    def setVehicleBonusDetails(self, value):
        self._setArray(13, value)
        return

    @staticmethod
    def getVehicleBonusDetailsType():
        return VehicleBonusDetailModel

    def getRole(self):
        return self._getString(14)

    def setRole(self, value):
        self._setString(14, value)
        return

    def getIsInNativeTank(self):
        return self._getBool(15)

    def setIsInNativeTank(self, value):
        self._setBool(15, value)
        return

    def getNation(self):
        return self._getString(16)

    def setNation(self, value):
        self._setString(16, value)
        return

    def getFullName(self):
        return self._getString(17)

    def setFullName(self, value):
        self._setString(17, value)
        return

    def getSkillsEfficiency(self):
        return self._getReal(18)

    def setSkillsEfficiency(self, value):
        self._setReal(18, value)
        return

    def getSkillsEfficiencyXP(self):
        return self._getNumber(19)

    def setSkillsEfficiencyXP(self, value):
        self._setNumber(19, value)
        return

    def getCurrentVehicleSkillsEfficiency(self):
        return self._getReal(20)

    def setCurrentVehicleSkillsEfficiency(self, value):
        self._setReal(20, value)
        return

    def getTankmanSuitable(self):
        return self._getBool(21)

    def setTankmanSuitable(self, value):
        self._setBool(21, value)
        return

    def getLockedByVehicle(self):
        return self._getBool(22)

    def setLockedByVehicle(self, value):
        self._setBool(22, value)
        return

    def _initialize(self):
        super(TankmanModel, self)._initialize()
        self._addViewModelProperty(b'vehicleBonus', VehicleBonus())
        self._addViewModelProperty(b'nativeVehicle', NativeVehicle())
        self._addNumberProperty(b'id', 0)
        self._addNumberProperty(b'level', 0)
        self._addBoolProperty(b'maxLevelAchieved', False)
        self._addStringProperty(b'crewSkinId', b'')
        self._addBoolProperty(b'customizedSkin', False)
        self._addNumberProperty(b'newPerksCount', 0)
        self._addNumberProperty(b'newBonusPerksCount', 0)
        self._addNumberProperty(b'trainingProgress', -1)
        self._addBoolProperty(b'quickTraining', False)
        self._addArrayProperty(b'perks', Array())
        self._addArrayProperty(b'bonusSkills', Array())
        self._addArrayProperty(b'vehicleBonusDetails', Array())
        self._addStringProperty(b'role', b'')
        self._addBoolProperty(b'isInNativeTank', False)
        self._addStringProperty(b'nation', b'')
        self._addStringProperty(b'fullName', b'')
        self._addRealProperty(b'skillsEfficiency', 0.0)
        self._addNumberProperty(b'skillsEfficiencyXP', 0)
        self._addRealProperty(b'currentVehicleSkillsEfficiency', 0.0)
        self._addBoolProperty(b'tankmanSuitable', True)
        self._addBoolProperty(b'lockedByVehicle', False)
        return
