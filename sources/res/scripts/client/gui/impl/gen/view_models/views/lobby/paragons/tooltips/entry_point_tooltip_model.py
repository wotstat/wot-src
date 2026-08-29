from enum import Enum
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.paragons.common.chapter_model import ChapterModel

class ProgressState(Enum):
    ACTIVE = b'active'
    NORESETTEDBRANCHES = b'noResettedBranches'
    NEEDVEHICLETORESET = b'needVehicleToReset'
    CHAPTERNOTCHOSEN = b'chapterNotChosen'
    ALLCHAPTERSCOMPLETED = b'allChaptersCompleted'
    PAUSED = b'paused'
    NOTAVAILABLE = b'notAvailable'


class EntryPointTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=7, commands=0):
        super(EntryPointTooltipModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def currentChapter(self):
        return self._getViewModel(0)

    @staticmethod
    def getCurrentChapterType():
        return ChapterModel

    def getIsFirstEntry(self):
        return self._getBool(1)

    def setIsFirstEntry(self, value):
        self._setBool(1, value)
        return

    def getPoints(self):
        return self._getNumber(2)

    def setPoints(self, value):
        self._setNumber(2, value)
        return

    def getTimeStamp(self):
        return self._getNumber(3)

    def setTimeStamp(self, value):
        self._setNumber(3, value)
        return

    def getVehicleToReset(self):
        return self._getNumber(4)

    def setVehicleToReset(self, value):
        self._setNumber(4, value)
        return

    def getVehicleCount(self):
        return self._getNumber(5)

    def setVehicleCount(self, value):
        self._setNumber(5, value)
        return

    def getProgressState(self):
        return ProgressState(self._getString(6))

    def setProgressState(self, value):
        self._setString(6, value.value)
        return

    def _initialize(self):
        super(EntryPointTooltipModel, self)._initialize()
        self._addViewModelProperty(b'currentChapter', ChapterModel())
        self._addBoolProperty(b'isFirstEntry', False)
        self._addNumberProperty(b'points', 0)
        self._addNumberProperty(b'timeStamp', 0)
        self._addNumberProperty(b'vehicleToReset', 0)
        self._addNumberProperty(b'vehicleCount', 0)
        self._addStringProperty(b'progressState', ProgressState.ACTIVE.value)
        return
