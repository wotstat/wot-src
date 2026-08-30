from frameworks.wulf import ViewModel

class AlertMessageModel(ViewModel):
    __slots__ = (b'onClick',)

    def __init__(self, properties=2, commands=1):
        super(AlertMessageModel, self).__init__(properties=properties, commands=commands)
        return

    def getMessage(self):
        return self._getString(0)

    def setMessage(self, value):
        self._setString(0, value)
        return

    def getButtonLabel(self):
        return self._getString(1)

    def setButtonLabel(self, value):
        self._setString(1, value)
        return

    def _initialize(self):
        super(AlertMessageModel, self)._initialize()
        self._addStringProperty(b'message', b'')
        self._addStringProperty(b'buttonLabel', b'')
        self.onClick = self._addCommand(b'onClick')
        return
