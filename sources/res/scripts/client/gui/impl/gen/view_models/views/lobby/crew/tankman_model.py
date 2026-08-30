from enum import Enum
from frameworks.wulf import Array
from gui.impl.gen import R
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.common.vehicle_info_model import VehicleInfoModel
from gui.impl.gen.view_models.views.lobby.crew.common.crew_widget_tankman_skill_model import CrewWidgetTankmanSkillModel

class TankmanRole(Enum):
    ANY = b'any'
    COMMANDER = b'commander'
    RADIOMAN = b'radioman'
    DRIVER = b'driver'
    GUNNER = b'gunner'
    LOADER = b'loader'


class TankmanLocation(Enum):
    INBARRACKS = b'in_barracks'
    INTANK = b'in_tank'
    DISMISSED = b'dismissed'


class TankmanKind(Enum):
    TANKMAN = b'tankman'
    RECRUIT = b'recruit'
    DISMISSED = b'dismissed'
    UNIQUE = b'unique'


class TankmanCardState(Enum):
    DEFAULT = b'default'
    SELECTED = b'selected'
    DISABLED = b'disabled'


class TankmanInfo(Enum):
    ISLOCKCREW = b'isLockCrew'
    TANKMANHASROLE = b'tankmanHasRole'


class TankmanModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=23, commands=0):
        super(TankmanModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def vehicleInfo(self):
        return self._getViewModel(0)

    @staticmethod
    def getVehicleInfoType():
        return VehicleInfoModel

    @property
    def tankmanVehicleInfo(self):
        return self._getViewModel(1)

    @staticmethod
    def getTankmanVehicleInfoType():
        return VehicleInfoModel

    def getTankmanID(self):
        return self._getNumber(2)

    def setTankmanID(self, value):
        self._setNumber(2, value)
        return

    def getRecruitID(self):
        return self._getString(3)

    def setRecruitID(self, value):
        self._setString(3, value)
        return

    def getIconName(self):
        return self._getString(4)

    def setIconName(self, value):
        self._setString(4, value)
        return

    def getNation(self):
        return self._getString(5)

    def setNation(self, value):
        self._setString(5, value)
        return

    def getRole(self):
        return TankmanRole(self._getString(6))

    def setRole(self, value):
        self._setString(6, value.value)
        return

    def getTankmanKind(self):
        return TankmanKind(self._getString(7))

    def setTankmanKind(self, value):
        self._setString(7, value.value)
        return

    def getCardState(self):
        return TankmanCardState(self._getString(8))

    def setCardState(self, value):
        self._setString(8, value.value)
        return

    def getLocation(self):
        return TankmanLocation(self._getString(9))

    def setLocation(self, value):
        self._setString(9, value.value)
        return

    def getFullUserName(self):
        return self._getString(10)

    def setFullUserName(self, value):
        self._setString(10, value)
        return

    def getSpecializationLevel(self):
        return self._getNumber(11)

    def setSpecializationLevel(self, value):
        self._setNumber(11, value)
        return

    def getHasRolePenalty(self):
        return self._getBool(12)

    def setHasRolePenalty(self, value):
        self._setBool(12, value)
        return

    def getHasSpecializationLevelPenalty(self):
        return self._getBool(13)

    def setHasSpecializationLevelPenalty(self, value):
        self._setBool(13, value)
        return

    def getIsInSkin(self):
        return self._getBool(14)

    def setIsInSkin(self, value):
        self._setBool(14, value)
        return

    def getSkills(self):
        return self._getArray(15)

    def setSkills(self, value):
        self._setArray(15, value)
        return

    @staticmethod
    def getSkillsType():
        return CrewWidgetTankmanSkillModel

    def getLastSkillLevel(self):
        return self._getNumber(16)

    def setLastSkillLevel(self, value):
        self._setNumber(16, value)
        return

    def getRecruitGlowImage(self):
        return self._getResource(17)

    def setRecruitGlowImage(self, value):
        self._setResource(17, value)
        return

    def getIsMainActionDisabled(self):
        return self._getBool(18)

    def setIsMainActionDisabled(self, value):
        self._setBool(18, value)
        return

    def getTimeToDismiss(self):
        return self._getNumber(19)

    def setTimeToDismiss(self, value):
        self._setNumber(19, value)
        return

    def getHasVoiceover(self):
        return self._getBool(20)

    def setHasVoiceover(self, value):
        self._setBool(20, value)
        return

    def getDisableIcon(self):
        return self._getResource(21)

    def setDisableIcon(self, value):
        self._setResource(21, value)
        return

    def getDisableReason(self):
        return self._getResource(22)

    def setDisableReason(self, value):
        self._setResource(22, value)
        return

    def _initialize(self):
        super(TankmanModel, self)._initialize()
        self._addViewModelProperty(b'vehicleInfo', VehicleInfoModel())
        self._addViewModelProperty(b'tankmanVehicleInfo', VehicleInfoModel())
        self._addNumberProperty(b'tankmanID', 0)
        self._addStringProperty(b'recruitID', b'')
        self._addStringProperty(b'iconName', b'')
        self._addStringProperty(b'nation', b'')
        self._addStringProperty(b'role', TankmanRole.ANY.value)
        self._addStringProperty(b'tankmanKind')
        self._addStringProperty(b'cardState')
        self._addStringProperty(b'location', TankmanLocation.INBARRACKS.value)
        self._addStringProperty(b'fullUserName', b'')
        self._addNumberProperty(b'specializationLevel', 0)
        self._addBoolProperty(b'hasRolePenalty', False)
        self._addBoolProperty(b'hasSpecializationLevelPenalty', False)
        self._addBoolProperty(b'isInSkin', False)
        self._addArrayProperty(b'skills', Array())
        self._addNumberProperty(b'lastSkillLevel', 0)
        self._addResourceProperty(b'recruitGlowImage', R.invalid())
        self._addBoolProperty(b'isMainActionDisabled', False)
        self._addNumberProperty(b'timeToDismiss', 0)
        self._addBoolProperty(b'hasVoiceover', False)
        self._addResourceProperty(b'disableIcon', R.invalid())
        self._addResourceProperty(b'disableReason', R.invalid())
        return
