from frameworks.wulf import ViewModel

class DirectiveConversionDirectiveModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(DirectiveConversionDirectiveModel, self).__init__(properties=properties, commands=commands)
        return

    def getIcon(self):
        return self._getString(0)

    def setIcon(self, value):
        self._setString(0, value)
        return

    def getUserName(self):
        return self._getString(1)

    def setUserName(self, value):
        self._setString(1, value)
        return

    def _initialize(self):
        super(DirectiveConversionDirectiveModel, self)._initialize()
        self._addStringProperty(b'icon', b'')
        self._addStringProperty(b'userName', b'')
        return
