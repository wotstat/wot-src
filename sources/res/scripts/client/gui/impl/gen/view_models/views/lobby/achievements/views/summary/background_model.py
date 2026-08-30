from frameworks.wulf import ViewModel

class BackgroundModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(BackgroundModel, self).__init__(properties=properties, commands=commands)
        return

    def getId(self):
        return self._getNumber(0)

    def setId(self, value):
        self._setNumber(0, value)
        return

    def getImage(self):
        return self._getString(1)

    def setImage(self, value):
        self._setString(1, value)
        return

    def getLabel(self):
        return self._getString(2)

    def setLabel(self, value):
        self._setString(2, value)
        return

    def _initialize(self):
        super(BackgroundModel, self)._initialize()
        self._addNumberProperty(b'id', 0)
        self._addStringProperty(b'image', b'')
        self._addStringProperty(b'label', b'')
        return
