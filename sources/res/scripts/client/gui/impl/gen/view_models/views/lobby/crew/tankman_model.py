from enum import Enum
from frameworks.wulf import ViewModel
from gui.impl.gen import R
from gui.impl.gen.view_models.common.vehicle_info_model import VehicleInfoModel
from gui.impl.gen.view_models.views.lobby.crew.common.crew_skill_list_model import CrewSkillListModel

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

    @property
    def skills(self):
        return self._getViewModel(2)

    @staticmethod
    def getSkillsType():
        return CrewSkillListModel

    def getTankmanID(self):
        return self._getNumber(3)

    def setTankmanID(self, value):
        self._setNumber(3, value)
        return

    def getRecruitID(self):
        return self._getString(4)

    def setRecruitID(self, value):
        self._setString(4, value)
        return

    def getIconName(self):
        return self._getString(5)

    def setIconName(self, value):
        self._setString(5, value)
        return

    def getNation(self):
        return self._getString(6)

    def setNation(self, value):
        self._setString(6, value)
        return

    def getRole(self):
        return TankmanRole(self._getString(7))

    def setRole(self, value):
        self._setString(7, value.value)
        return

    def getTankmanKind(self):
        return TankmanKind(self._getString(8))

    def setTankmanKind(self, value):
        self._setString(8, value.value)
        return

    def getCardState(self):
        return TankmanCardState(self._getString(9))

    def setCardState(self, value):
        self._setString(9, value.value)
        return

    def getLocation(self):
        return TankmanLocation(self._getString(10))

    def setLocation(self, value):
        self._setString(10, value.value)
        return

    def getFullUserName(self):
        return self._getString(11)

    def setFullUserName(self, value):
        self._setString(11, value)
        return

    def getHasRolePenalty(self):
        return self._getBool(12)

    def setHasRolePenalty(self, value):
        self._setBool(12, value)
        return

    def getIsInSkin(self):
        return self._getBool(13)

    def setIsInSkin(self, value):
        self._setBool(13, value)
        return

    def getLastSkillLevel(self):
        return self._getNumber(14)

    def setLastSkillLevel(self, value):
        self._setNumber(14, value)
        return

    def getRecruitGlowImage(self):
        return self._getResource(15)

    def setRecruitGlowImage(self, value):
        self._setResource(15, value)
        return

    def getIsMainActionDisabled(self):
        return self._getBool(16)

    def setIsMainActionDisabled(self, value):
        self._setBool(16, value)
        return

    def getTimeToDismiss(self):
        return self._getNumber(17)

    def setTimeToDismiss(self, value):
        self._setNumber(17, value)
        return

    def getHasVoiceover(self):
        return self._getBool(18)

    def setHasVoiceover(self, value):
        self._setBool(18, value)
        return

    def getHasPostProgression(self):
        return self._getBool(19)

    def setHasPostProgression(self, value):
        self._setBool(19, value)
        return

    def getDisableIcon(self):
        return self._getResource(20)

    def setDisableIcon(self, value):
        self._setResource(20, value)
        return

    def getDisableReason(self):
        return self._getResource(21)

    def setDisableReason(self, value):
        self._setResource(21, value)
        return

    def getIsNew(self):
        return self._getBool(22)

    def setIsNew(self, value):
        self._setBool(22, value)
        return

    def _initialize(self):
        super(TankmanModel, self)._initialize()
        self._addViewModelProperty(b'vehicleInfo', VehicleInfoModel())
        self._addViewModelProperty(b'tankmanVehicleInfo', VehicleInfoModel())
        self._addViewModelProperty(b'skills', CrewSkillListModel())
        self._addNumberProperty(b'tankmanID', 0)
        self._addStringProperty(b'recruitID', b'')
        self._addStringProperty(b'iconName', b'')
        self._addStringProperty(b'nation', b'')
        self._addStringProperty(b'role', TankmanRole.ANY.value)
        self._addStringProperty(b'tankmanKind')
        self._addStringProperty(b'cardState', TankmanCardState.DEFAULT.value)
        self._addStringProperty(b'location', TankmanLocation.INBARRACKS.value)
        self._addStringProperty(b'fullUserName', b'')
        self._addBoolProperty(b'hasRolePenalty', False)
        self._addBoolProperty(b'isInSkin', False)
        self._addNumberProperty(b'lastSkillLevel', 0)
        self._addResourceProperty(b'recruitGlowImage', R.invalid())
        self._addBoolProperty(b'isMainActionDisabled', False)
        self._addNumberProperty(b'timeToDismiss', 0)
        self._addBoolProperty(b'hasVoiceover', False)
        self._addBoolProperty(b'hasPostProgression', False)
        self._addResourceProperty(b'disableIcon', R.invalid())
        self._addResourceProperty(b'disableReason', R.invalid())
        self._addBoolProperty(b'isNew', False)
        return
