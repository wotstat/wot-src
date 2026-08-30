from frameworks.wulf import Array
from gui.impl.gen import R
from frameworks.wulf import ViewModel

class SimpleDialogWindowModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=5, commands=0):
        super(SimpleDialogWindowModel, self).__init__(properties=properties, commands=commands)
        return

    def getMessage(self):
        return self._getResource(0)

    def setMessage(self, value):
        self._setResource(0, value)
        return

    def getFormattedMessage(self):
        return self._getString(1)

    def setFormattedMessage(self, value):
        self._setString(1, value)
        return

    def getMessageArgs(self):
        return self._getArray(2)

    def setMessageArgs(self, value):
        self._setArray(2, value)
        return

    def getMessageFmtArgs(self):
        return self._getArray(3)

    def setMessageFmtArgs(self, value):
        self._setArray(3, value)
        return

    def getIsMessageFmtArgsNamed(self):
        return self._getBool(4)

    def setIsMessageFmtArgsNamed(self, value):
        self._setBool(4, value)
        return

    def _initialize(self):
        super(SimpleDialogWindowModel, self)._initialize()
        self._addResourceProperty(b'message', R.invalid())
        self._addStringProperty(b'formattedMessage', b'')
        self._addArrayProperty(b'messageArgs', Array())
        self._addArrayProperty(b'messageFmtArgs', Array())
        self._addBoolProperty(b'isMessageFmtArgsNamed', True)
        return
