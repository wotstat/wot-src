from enum import Enum
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.paragons.common.chapter_model import ChapterModel

class ProgressState(Enum):
    ACTIVE = b'active'
    CHAPTERNOTCHOSEN = b'chapterNotChosen'
    NOTAVAILABLE = b'notAvailable'
    ALLCHAPTERSCOMPLETED = b'allChaptersCompleted'
    PAUSED = b'paused'


class ParagonsEntryPointViewModel(ViewModel):
    __slots__ = (b'onEntryPointClick',)

    def __init__(self, properties=5, commands=1):
        super(ParagonsEntryPointViewModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def currentChapter(self):
        return self._getViewModel(0)

    @staticmethod
    def getCurrentChapterType():
        return ChapterModel

    def getIsAnySelectableReward(self):
        return self._getBool(1)

    def setIsAnySelectableReward(self, value):
        self._setBool(1, value)
        return

    def getIsAnySelectableRewardInInventory(self):
        return self._getBool(2)

    def setIsAnySelectableRewardInInventory(self, value):
        self._setBool(2, value)
        return

    def getProgressState(self):
        return ProgressState(self._getString(3))

    def setProgressState(self, value):
        self._setString(3, value.value)
        return

    def getFreePoints(self):
        return self._getNumber(4)

    def setFreePoints(self, value):
        self._setNumber(4, value)
        return

    def _initialize(self):
        super(ParagonsEntryPointViewModel, self)._initialize()
        self._addViewModelProperty(b'currentChapter', ChapterModel())
        self._addBoolProperty(b'isAnySelectableReward', False)
        self._addBoolProperty(b'isAnySelectableRewardInInventory', False)
        self._addStringProperty(b'progressState', ProgressState.ACTIVE.value)
        self._addNumberProperty(b'freePoints', 0)
        self.onEntryPointClick = self._addCommand(b'onEntryPointClick')
        return
