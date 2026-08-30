from frameworks.wulf import ViewModel

class TextWithWarningViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(TextWithWarningViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getMainText(self):
        return self._getString(0)

    def setMainText(self, value):
        self._setString(0, value)
        return

    def getWarningText(self):
        return self._getString(1)

    def setWarningText(self, value):
        self._setString(1, value)
        return

    def _initialize(self):
        super(TextWithWarningViewModel, self)._initialize()
        self._addStringProperty(b'mainText', b'')
        self._addStringProperty(b'warningText', b'')
        return
