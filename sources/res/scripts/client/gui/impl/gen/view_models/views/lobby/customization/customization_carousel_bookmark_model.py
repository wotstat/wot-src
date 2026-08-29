from frameworks.wulf import ViewModel

class CustomizationCarouselBookmarkModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(CustomizationCarouselBookmarkModel, self).__init__(properties=properties, commands=commands)
        return

    def getBookmarkIndex(self):
        return self._getNumber(0)

    def setBookmarkIndex(self, value):
        self._setNumber(0, value)
        return

    def getBookmarkName(self):
        return self._getString(1)

    def setBookmarkName(self, value):
        self._setString(1, value)
        return

    def getIsProgressive(self):
        return self._getBool(2)

    def setIsProgressive(self, value):
        self._setBool(2, value)
        return

    def _initialize(self):
        super(CustomizationCarouselBookmarkModel, self)._initialize()
        self._addNumberProperty(b'bookmarkIndex', 0)
        self._addStringProperty(b'bookmarkName', b'')
        self._addBoolProperty(b'isProgressive', False)
        return
