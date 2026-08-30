from gui.impl.gen import R
from frameworks.wulf import ViewModel

class ImageSubstitutionViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=6, commands=0):
        super(ImageSubstitutionViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getPath(self):
        return self._getResource(0)

    def setPath(self, value):
        self._setResource(0, value)
        return

    def getPlaceholder(self):
        return self._getString(1)

    def setPlaceholder(self, value):
        self._setString(1, value)
        return

    def getMarginTop(self):
        return self._getNumber(2)

    def setMarginTop(self, value):
        self._setNumber(2, value)
        return

    def getMarginRight(self):
        return self._getNumber(3)

    def setMarginRight(self, value):
        self._setNumber(3, value)
        return

    def getMarginBottom(self):
        return self._getNumber(4)

    def setMarginBottom(self, value):
        self._setNumber(4, value)
        return

    def getMarginLeft(self):
        return self._getNumber(5)

    def setMarginLeft(self, value):
        self._setNumber(5, value)
        return

    def _initialize(self):
        super(ImageSubstitutionViewModel, self)._initialize()
        self._addResourceProperty(b'path', R.invalid())
        self._addStringProperty(b'placeholder', b'')
        self._addNumberProperty(b'marginTop', 0)
        self._addNumberProperty(b'marginRight', 0)
        self._addNumberProperty(b'marginBottom', 0)
        self._addNumberProperty(b'marginLeft', 0)
        return
