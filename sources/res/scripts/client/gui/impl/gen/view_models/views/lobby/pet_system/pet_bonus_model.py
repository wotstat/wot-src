from frameworks.wulf import ViewModel

class PetBonusModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(PetBonusModel, self).__init__(properties=properties, commands=commands)
        return

    def getId(self):
        return self._getNumber(0)

    def setId(self, value):
        self._setNumber(0, value)
        return

    def getName(self):
        return self._getString(1)

    def setName(self, value):
        self._setString(1, value)
        return

    def getValue(self):
        return self._getString(2)

    def setValue(self, value):
        self._setString(2, value)
        return

    def _initialize(self):
        super(PetBonusModel, self)._initialize()
        self._addNumberProperty(b'id', 0)
        self._addStringProperty(b'name', b'')
        self._addStringProperty(b'value', b'')
        return
