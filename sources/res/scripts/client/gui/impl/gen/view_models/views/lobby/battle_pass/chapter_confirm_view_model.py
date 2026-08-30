from frameworks.wulf import ViewModel

class ChapterConfirmViewModel(ViewModel):
    __slots__ = (b'onAccept', b'onCancel')

    def __init__(self, properties=3, commands=2):
        super(ChapterConfirmViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getPrevChapter(self):
        return self._getNumber(0)

    def setPrevChapter(self, value):
        self._setNumber(0, value)
        return

    def getNextChapter(self):
        return self._getNumber(1)

    def setNextChapter(self, value):
        self._setNumber(1, value)
        return

    def getIsSwitchFromPostProgressionToExtraChapter(self):
        return self._getBool(2)

    def setIsSwitchFromPostProgressionToExtraChapter(self, value):
        self._setBool(2, value)
        return

    def _initialize(self):
        super(ChapterConfirmViewModel, self)._initialize()
        self._addNumberProperty(b'prevChapter', 0)
        self._addNumberProperty(b'nextChapter', 0)
        self._addBoolProperty(b'isSwitchFromPostProgressionToExtraChapter', False)
        self.onAccept = self._addCommand(b'onAccept')
        self.onCancel = self._addCommand(b'onCancel')
        return
