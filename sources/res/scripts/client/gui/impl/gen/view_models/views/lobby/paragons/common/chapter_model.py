from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.paragons.common.chapter_status_model import ChapterStatusModel
from gui.impl.gen.view_models.views.lobby.paragons.common.level_model import LevelModel

class ChapterModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=10, commands=0):
        super(ChapterModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def chapterStatus(self):
        return self._getViewModel(0)

    @staticmethod
    def getChapterStatusType():
        return ChapterStatusModel

    def getId(self):
        return self._getNumber(1)

    def setId(self, value):
        self._setNumber(1, value)
        return

    def getName(self):
        return self._getString(2)

    def setName(self, value):
        self._setString(2, value)
        return

    def getIsCompleted(self):
        return self._getBool(3)

    def setIsCompleted(self, value):
        self._setBool(3, value)
        return

    def getChapterLevel(self):
        return self._getNumber(4)

    def setChapterLevel(self, value):
        self._setNumber(4, value)
        return

    def getPoints(self):
        return self._getNumber(5)

    def setPoints(self, value):
        self._setNumber(5, value)
        return

    def getIsAllRewardsClaimed(self):
        return self._getBool(6)

    def setIsAllRewardsClaimed(self, value):
        self._setBool(6, value)
        return

    def getFinalVehicleCDs(self):
        return self._getArray(7)

    def setFinalVehicleCDs(self, value):
        self._setArray(7, value)
        return

    @staticmethod
    def getFinalVehicleCDsType():
        return int

    def getLevels(self):
        return self._getArray(8)

    def setLevels(self, value):
        self._setArray(8, value)
        return

    @staticmethod
    def getLevelsType():
        return LevelModel

    def getTimeStamp(self):
        return self._getNumber(9)

    def setTimeStamp(self, value):
        self._setNumber(9, value)
        return

    def _initialize(self):
        super(ChapterModel, self)._initialize()
        self._addViewModelProperty(b'chapterStatus', ChapterStatusModel())
        self._addNumberProperty(b'id', 1)
        self._addStringProperty(b'name', b'')
        self._addBoolProperty(b'isCompleted', False)
        self._addNumberProperty(b'chapterLevel', 0)
        self._addNumberProperty(b'points', 0)
        self._addBoolProperty(b'isAllRewardsClaimed', False)
        self._addArrayProperty(b'finalVehicleCDs', Array())
        self._addArrayProperty(b'levels', Array())
        self._addNumberProperty(b'timeStamp', 0)
        return
