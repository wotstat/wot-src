from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.views.lobby.battle_pass.chapter_model import ChapterModel

class ChapterChoiceViewModel(ViewModel):
    __slots__ = (b'onPreviewClick', b'onChapterSelect', b'onAboutClick', b'onPointsInfoClick', b'onBuyClick', b'onViewLoaded', b'onClose', b'onShowPostProgression', b'showTankmen')

    def __init__(self, properties=5, commands=9):
        super(ChapterChoiceViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getChapters(self):
        return self._getArray(0)

    def setChapters(self, value):
        self._setArray(0, value)
        return

    @staticmethod
    def getChaptersType():
        return ChapterModel

    def getSelectedChapter(self):
        return self._getNumber(1)

    def setSelectedChapter(self, value):
        self._setNumber(1, value)
        return

    def getFreePoints(self):
        return self._getNumber(2)

    def setFreePoints(self, value):
        self._setNumber(2, value)
        return

    def getSeasonNum(self):
        return self._getNumber(3)

    def setSeasonNum(self, value):
        self._setNumber(3, value)
        return

    def getIsPostProgressionUnlocked(self):
        return self._getBool(4)

    def setIsPostProgressionUnlocked(self, value):
        self._setBool(4, value)
        return

    def _initialize(self):
        super(ChapterChoiceViewModel, self)._initialize()
        self._addArrayProperty(b'chapters', Array())
        self._addNumberProperty(b'selectedChapter', 0)
        self._addNumberProperty(b'freePoints', 0)
        self._addNumberProperty(b'seasonNum', 0)
        self._addBoolProperty(b'isPostProgressionUnlocked', False)
        self.onPreviewClick = self._addCommand(b'onPreviewClick')
        self.onChapterSelect = self._addCommand(b'onChapterSelect')
        self.onAboutClick = self._addCommand(b'onAboutClick')
        self.onPointsInfoClick = self._addCommand(b'onPointsInfoClick')
        self.onBuyClick = self._addCommand(b'onBuyClick')
        self.onViewLoaded = self._addCommand(b'onViewLoaded')
        self.onClose = self._addCommand(b'onClose')
        self.onShowPostProgression = self._addCommand(b'onShowPostProgression')
        self.showTankmen = self._addCommand(b'showTankmen')
        return
