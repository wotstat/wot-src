from comp7.gui.impl.gen.view_models.views.lobby.enums import Division, Rank, SeasonName
from frameworks.wulf import ViewModel
from comp7.gui.impl.gen.view_models.views.battle.comp7_vehicle_model import Comp7VehicleModel

class PlayerModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=17, commands=0):
        super(PlayerModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def vehicle(self):
        return self._getViewModel(0)

    @staticmethod
    def getVehicleType():
        return Comp7VehicleModel

    @property
    def vehicleToBan(self):
        return self._getViewModel(1)

    @staticmethod
    def getVehicleToBanType():
        return Comp7VehicleModel

    def getIsLoaded(self):
        return self._getBool(2)

    def setIsLoaded(self, value):
        self._setBool(2, value)
        return

    def getId(self):
        return self._getNumber(3)

    def setId(self, value):
        self._setNumber(3, value)
        return

    def getBadgeID(self):
        return self._getNumber(4)

    def setBadgeID(self, value):
        self._setNumber(4, value)
        return

    def getUserName(self):
        return self._getString(5)

    def setUserName(self, value):
        self._setString(5, value)
        return

    def getClanTag(self):
        return self._getString(6)

    def setClanTag(self, value):
        self._setString(6, value)
        return

    def getSuffixBadgeID(self):
        return self._getNumber(7)

    def setSuffixBadgeID(self, value):
        self._setNumber(7, value)
        return

    def getIsQualification(self):
        return self._getBool(8)

    def setIsQualification(self, value):
        self._setBool(8, value)
        return

    def getRank(self):
        return Rank(self._getNumber(9))

    def setRank(self, value):
        self._setNumber(9, value.value)
        return

    def getSeasonName(self):
        return SeasonName(self._getString(10))

    def setSeasonName(self, value):
        self._setString(10, value.value)
        return

    def getDivision(self):
        return Division(self._getNumber(11))

    def setDivision(self, value):
        self._setNumber(11, value.value)
        return

    def getSelectedVehicleToBan(self):
        return self._getBool(12)

    def setSelectedVehicleToBan(self, value):
        self._setBool(12, value)
        return

    def getConfirmedChoice(self):
        return self._getBool(13)

    def setConfirmedChoice(self, value):
        self._setBool(13, value)
        return

    def getIsVoiceActive(self):
        return self._getBool(14)

    def setIsVoiceActive(self, value):
        self._setBool(14, value)
        return

    def getIsChatEnabled(self):
        return self._getBool(15)

    def setIsChatEnabled(self, value):
        self._setBool(15, value)
        return

    def getIsVoiceEnabled(self):
        return self._getBool(16)

    def setIsVoiceEnabled(self, value):
        self._setBool(16, value)
        return

    def _initialize(self):
        super(PlayerModel, self)._initialize()
        self._addViewModelProperty(b'vehicle', Comp7VehicleModel())
        self._addViewModelProperty(b'vehicleToBan', Comp7VehicleModel())
        self._addBoolProperty(b'isLoaded', False)
        self._addNumberProperty(b'id', 0)
        self._addNumberProperty(b'badgeID', 0)
        self._addStringProperty(b'userName', b'')
        self._addStringProperty(b'clanTag', b'')
        self._addNumberProperty(b'suffixBadgeID', 0)
        self._addBoolProperty(b'isQualification', False)
        self._addNumberProperty(b'rank')
        self._addStringProperty(b'seasonName')
        self._addNumberProperty(b'division')
        self._addBoolProperty(b'selectedVehicleToBan', False)
        self._addBoolProperty(b'confirmedChoice', False)
        self._addBoolProperty(b'isVoiceActive', False)
        self._addBoolProperty(b'isChatEnabled', True)
        self._addBoolProperty(b'isVoiceEnabled', True)
        return
