from frameworks.wulf import ViewModel

class PostProgressionTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(PostProgressionTooltipModel, self).__init__(properties=properties, commands=commands)
        return

    def getBookXp(self):
        return self._getNumber(0)

    def setBookXp(self, value):
        self._setNumber(0, value)
        return

    def getProgressCurrent(self):
        return self._getNumber(1)

    def setProgressCurrent(self, value):
        self._setNumber(1, value)
        return

    def getProgressMax(self):
        return self._getNumber(2)

    def setProgressMax(self, value):
        self._setNumber(2, value)
        return

    def getHasWarning(self):
        return self._getBool(3)

    def setHasWarning(self, value):
        self._setBool(3, value)
        return

    def _initialize(self):
        super(PostProgressionTooltipModel, self)._initialize()
        self._addNumberProperty(b'bookXp', 0)
        self._addNumberProperty(b'progressCurrent', 0)
        self._addNumberProperty(b'progressMax', 0)
        self._addBoolProperty(b'hasWarning', False)
        return
