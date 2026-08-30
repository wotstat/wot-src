from frameworks.wulf import Array
from gui.impl.gen import R
from frameworks.wulf import ViewModel

class FullScreenDialogWindowModel(ViewModel):
    __slots__ = (b'onAcceptClicked', b'onCancelClicked', b'onExit')

    def __init__(self, properties=11, commands=3):
        super(FullScreenDialogWindowModel, self).__init__(properties=properties, commands=commands)
        return

    def getDialogType(self):
        return self._getString(0)

    def setDialogType(self, value):
        self._setString(0, value)
        return

    def getCredits(self):
        return self._getNumber(1)

    def setCredits(self, value):
        self._setNumber(1, value)
        return

    def getGolds(self):
        return self._getNumber(2)

    def setGolds(self, value):
        self._setNumber(2, value)
        return

    def getCrystals(self):
        return self._getNumber(3)

    def setCrystals(self, value):
        self._setNumber(3, value)
        return

    def getFreexp(self):
        return self._getNumber(4)

    def setFreexp(self, value):
        self._setNumber(4, value)
        return

    def getIsWalletAvailable(self):
        return self._getBool(5)

    def setIsWalletAvailable(self, value):
        self._setBool(5, value)
        return

    def getIsAcceptDisabled(self):
        return self._getBool(6)

    def setIsAcceptDisabled(self, value):
        self._setBool(6, value)
        return

    def getTitleBody(self):
        return self._getResource(7)

    def setTitleBody(self, value):
        self._setResource(7, value)
        return

    def getTitleArgs(self):
        return self._getArray(8)

    def setTitleArgs(self, value):
        self._setArray(8, value)
        return

    def getAcceptButtonText(self):
        return self._getResource(9)

    def setAcceptButtonText(self, value):
        self._setResource(9, value)
        return

    def getCancelButtonText(self):
        return self._getResource(10)

    def setCancelButtonText(self, value):
        self._setResource(10, value)
        return

    def _initialize(self):
        super(FullScreenDialogWindowModel, self)._initialize()
        self._addStringProperty(b'dialogType', b'simple')
        self._addNumberProperty(b'credits', 0)
        self._addNumberProperty(b'golds', 0)
        self._addNumberProperty(b'crystals', 0)
        self._addNumberProperty(b'freexp', 0)
        self._addBoolProperty(b'isWalletAvailable', True)
        self._addBoolProperty(b'isAcceptDisabled', False)
        self._addResourceProperty(b'titleBody', R.invalid())
        self._addArrayProperty(b'titleArgs', Array())
        self._addResourceProperty(b'acceptButtonText', R.invalid())
        self._addResourceProperty(b'cancelButtonText', R.invalid())
        self.onAcceptClicked = self._addCommand(b'onAcceptClicked')
        self.onCancelClicked = self._addCommand(b'onCancelClicked')
        self.onExit = self._addCommand(b'onExit')
        return
