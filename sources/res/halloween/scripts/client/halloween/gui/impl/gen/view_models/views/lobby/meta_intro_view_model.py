from frameworks.wulf import ViewModel

class MetaIntroViewModel(ViewModel):
    __slots__ = (b'onClose',)

    def __init__(self, properties=2, commands=1):
        super(MetaIntroViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getLevel(self):
        return self._getNumber(0)

    def setLevel(self, value):
        self._setNumber(0, value)
        return

    def getName(self):
        return self._getString(1)

    def setName(self, value):
        self._setString(1, value)
        return

    def _initialize(self):
        super(MetaIntroViewModel, self)._initialize()
        self._addNumberProperty(b'level', 0)
        self._addStringProperty(b'name', b'')
        self.onClose = self._addCommand(b'onClose')
        return
