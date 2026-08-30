from frameworks.wulf import ViewModel

class BuyChapterModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(BuyChapterModel, self).__init__(properties=properties, commands=commands)
        return

    def getChapterID(self):
        return self._getNumber(0)

    def setChapterID(self, value):
        self._setNumber(0, value)
        return

    def getHasStarterPack(self):
        return self._getBool(1)

    def setHasStarterPack(self, value):
        self._setBool(1, value)
        return

    def getIsExtra(self):
        return self._getBool(2)

    def setIsExtra(self, value):
        self._setBool(2, value)
        return

    def _initialize(self):
        super(BuyChapterModel, self)._initialize()
        self._addNumberProperty(b'chapterID', 0)
        self._addBoolProperty(b'hasStarterPack', False)
        self._addBoolProperty(b'isExtra', False)
        return
