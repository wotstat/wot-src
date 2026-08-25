from enum import Enum
from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.common.vehicle_info_model import VehicleInfoModel

class ChapterStates(Enum):
    ACTIVE = b'active'
    PAUSED = b'paused'
    COMPLETED = b'completed'
    NOTSTARTED = b'notStarted'


class FinalRewardTypes(Enum):
    VEHICLE = b'vehicle'
    VEHICLESTYLE = b'vehicleStyle'
    STYLE = b'style'
    TANKMAN = b'tankman'
    POSTPROGRESSION = b'postProgression'


class ChapterModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=18, commands=0):
        super(ChapterModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def vehicleInfo(self):
        return self._getViewModel(0)

    @staticmethod
    def getVehicleInfoType():
        return VehicleInfoModel

    def getChapterID(self):
        return self._getNumber(1)

    def setChapterID(self, value):
        self._setNumber(1, value)
        return

    def getCurrentLevel(self):
        return self._getNumber(2)

    def setCurrentLevel(self, value):
        self._setNumber(2, value)
        return

    def getMaxLevel(self):
        return self._getNumber(3)

    def setMaxLevel(self, value):
        self._setNumber(3, value)
        return

    def getCyclesCompletedCount(self):
        return self._getNumber(4)

    def setCyclesCompletedCount(self, value):
        self._setNumber(4, value)
        return

    def getChapterState(self):
        return ChapterStates(self._getString(5))

    def setChapterState(self, value):
        self._setString(5, value.value)
        return

    def getIsVehicleInHangar(self):
        return self._getBool(6)

    def setIsVehicleInHangar(self, value):
        self._setBool(6, value)
        return

    def getIsBought(self):
        return self._getBool(7)

    def setIsBought(self, value):
        self._setBool(7, value)
        return

    def getLevelProgression(self):
        return self._getNumber(8)

    def setLevelProgression(self, value):
        self._setNumber(8, value)
        return

    def getIsExtra(self):
        return self._getBool(9)

    def setIsExtra(self, value):
        self._setBool(9, value)
        return

    def getIsPostProgression(self):
        return self._getBool(10)

    def setIsPostProgression(self, value):
        self._setBool(10, value)
        return

    def getTankmenScreenID(self):
        return self._getNumber(11)

    def setTankmenScreenID(self, value):
        self._setNumber(11, value)
        return

    def getFinalRewardType(self):
        return FinalRewardTypes(self._getString(12))

    def setFinalRewardType(self, value):
        self._setString(12, value.value)
        return

    def getStyleName(self):
        return self._getString(13)

    def setStyleName(self, value):
        self._setString(13, value)
        return

    def getTankmanNames(self):
        return self._getArray(14)

    def setTankmanNames(self, value):
        self._setArray(14, value)
        return

    @staticmethod
    def getTankmanNamesType():
        return unicode

    def getExpireTime(self):
        return self._getNumber(15)

    def setExpireTime(self, value):
        self._setNumber(15, value)
        return

    def getTimeLeft(self):
        return self._getNumber(16)

    def setTimeLeft(self, value):
        self._setNumber(16, value)
        return

    def getChapterRewardsCount(self):
        return self._getNumber(17)

    def setChapterRewardsCount(self, value):
        self._setNumber(17, value)
        return

    def _initialize(self):
        super(ChapterModel, self)._initialize()
        self._addViewModelProperty(b'vehicleInfo', VehicleInfoModel())
        self._addNumberProperty(b'chapterID', 0)
        self._addNumberProperty(b'currentLevel', 0)
        self._addNumberProperty(b'maxLevel', 0)
        self._addNumberProperty(b'cyclesCompletedCount', 0)
        self._addStringProperty(b'chapterState')
        self._addBoolProperty(b'isVehicleInHangar', False)
        self._addBoolProperty(b'isBought', False)
        self._addNumberProperty(b'levelProgression', 0)
        self._addBoolProperty(b'isExtra', False)
        self._addBoolProperty(b'isPostProgression', False)
        self._addNumberProperty(b'tankmenScreenID', 0)
        self._addStringProperty(b'finalRewardType')
        self._addStringProperty(b'styleName', b'')
        self._addArrayProperty(b'tankmanNames', Array())
        self._addNumberProperty(b'expireTime', 0)
        self._addNumberProperty(b'timeLeft', 0)
        self._addNumberProperty(b'chapterRewardsCount', 0)
        return
