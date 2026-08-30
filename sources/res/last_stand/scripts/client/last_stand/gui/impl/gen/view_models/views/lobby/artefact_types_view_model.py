from frameworks.wulf import ViewModel

class ArtefactTypesViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(ArtefactTypesViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getId(self):
        return self._getString(0)

    def setId(self, value):
        self._setString(0, value)
        return

    def getIndex(self):
        return self._getNumber(1)

    def setIndex(self, value):
        self._setNumber(1, value)
        return

    def getTypes(self):
        return self._getString(2)

    def setTypes(self, value):
        self._setString(2, value)
        return

    def _initialize(self):
        super(ArtefactTypesViewModel, self)._initialize()
        self._addStringProperty(b'id', b'')
        self._addNumberProperty(b'index', 0)
        self._addStringProperty(b'types', b'')
        return
