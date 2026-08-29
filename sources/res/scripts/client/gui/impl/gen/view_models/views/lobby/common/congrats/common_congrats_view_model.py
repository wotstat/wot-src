from gui.impl.gen import R
from frameworks.wulf import ViewModel

class CommonCongratsViewModel(ViewModel):
    __slots__ = (b'onCloseClick', b'onConfirmClick', b'onBackClick')

    def __init__(self, properties=8, commands=3):
        super(CommonCongratsViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getBackground(self):
        return self._getResource(0)

    def setBackground(self, value):
        self._setResource(0, value)
        return

    def getTitle(self):
        return self._getResource(1)

    def setTitle(self, value):
        self._setResource(1, value)
        return

    def getDescription(self):
        return self._getString(2)

    def setDescription(self, value):
        self._setString(2, value)
        return

    def getImage(self):
        return self._getString(3)

    def setImage(self, value):
        self._setString(3, value)
        return

    def getImageAlt(self):
        return self._getString(4)

    def setImageAlt(self, value):
        self._setString(4, value)
        return

    def getConfirmLbl(self):
        return self._getResource(5)

    def setConfirmLbl(self, value):
        self._setResource(5, value)
        return

    def getBackLbl(self):
        return self._getResource(6)

    def setBackLbl(self, value):
        self._setResource(6, value)
        return

    def getNeedReset(self):
        return self._getBool(7)

    def setNeedReset(self, value):
        self._setBool(7, value)
        return

    def _initialize(self):
        super(CommonCongratsViewModel, self)._initialize()
        self._addResourceProperty(b'background', R.invalid())
        self._addResourceProperty(b'title', R.invalid())
        self._addStringProperty(b'description', b'')
        self._addStringProperty(b'image', b'')
        self._addStringProperty(b'imageAlt', b'')
        self._addResourceProperty(b'confirmLbl', R.invalid())
        self._addResourceProperty(b'backLbl', R.invalid())
        self._addBoolProperty(b'needReset', False)
        self.onCloseClick = self._addCommand(b'onCloseClick')
        self.onConfirmClick = self._addCommand(b'onConfirmClick')
        self.onBackClick = self._addCommand(b'onBackClick')
        return
