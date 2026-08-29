from frameworks.wulf import ViewModel

class StyleVideoViewModel(ViewModel):
    __slots__ = (b'onClose', b'onError')

    def __init__(self, properties=3, commands=2):
        super(StyleVideoViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getChapter(self):
        return self._getNumber(0)

    def setChapter(self, value):
        self._setNumber(0, value)
        return

    def getLevel(self):
        return self._getNumber(1)

    def setLevel(self, value):
        self._setNumber(1, value)
        return

    def getIsWindowAccessible(self):
        return self._getBool(2)

    def setIsWindowAccessible(self, value):
        self._setBool(2, value)
        return

    def _initialize(self):
        super(StyleVideoViewModel, self)._initialize()
        self._addNumberProperty(b'chapter', 0)
        self._addNumberProperty(b'level', 0)
        self._addBoolProperty(b'isWindowAccessible', True)
        self.onClose = self._addCommand(b'onClose')
        self.onError = self._addCommand(b'onError')
        return
