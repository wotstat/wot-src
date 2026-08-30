from enum import Enum
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.common.vehicle_info_model import VehicleInfoModel

class ChapterStates(Enum):
    ACTIVE = b'active'
    PAUSED = b'paused'
    COMPLETED = b'completed'
    NOTSTARTED = b'notStarted'
    DISABLED = b'disabled'


class ChapterType(Enum):
    DEFAULT = b'default'
    MARATHON = b'marathon'
    RESOURCE = b'resource'


class ChapterModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=11, commands=0):
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

    def getStyleName(self):
        return self._getString(2)

    def setStyleName(self, value):
        self._setString(2, value)
        return

    def getTankman(self):
        return self._getString(3)

    def setTankman(self, value):
        self._setString(3, value)
        return

    def getCurrentLevel(self):
        return self._getNumber(4)

    def setCurrentLevel(self, value):
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

    def getFinalReward(self):
        return self._getString(9)

    def setFinalReward(self, value):
        self._setString(9, value)
        return

    def getChapterType(self):
        return ChapterType(self._getString(10))

    def setChapterType(self, value):
        self._setString(10, value.value)
        return

    def _initialize(self):
        super(ChapterModel, self)._initialize()
        self._addViewModelProperty(b'vehicleInfo', VehicleInfoModel())
        self._addNumberProperty(b'chapterID', 0)
        self._addStringProperty(b'styleName', b'')
        self._addStringProperty(b'tankman', b'')
        self._addNumberProperty(b'currentLevel', 0)
        self._addStringProperty(b'chapterState')
        self._addBoolProperty(b'isVehicleInHangar', False)
        self._addBoolProperty(b'isBought', False)
        self._addNumberProperty(b'levelProgression', 0)
        self._addStringProperty(b'finalReward', b'')
        self._addStringProperty(b'chapterType')
        return
