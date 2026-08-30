from frameworks.wulf import ViewModel

class BundleCardModel(ViewModel):
    __slots__ = (b'onClick',)

    def __init__(self, properties=2, commands=1):
        super(BundleCardModel, self).__init__(properties=properties, commands=commands)
        return

    def getId(self):
        return self._getString(0)

    def setId(self, value):
        self._setString(0, value)
        return

    def getDescriptionKey(self):
        return self._getString(1)

    def setDescriptionKey(self, value):
        self._setString(1, value)
        return

    def _initialize(self):
        super(BundleCardModel, self)._initialize()
        self._addStringProperty(b'id', b'')
        self._addStringProperty(b'descriptionKey', b'')
        self.onClick = self._addCommand(b'onClick')
        return
