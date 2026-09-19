from frameworks.wulf import ViewModel

class CurrentEnemyModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(CurrentEnemyModel, self).__init__(properties=properties, commands=commands)
        return

    def getName(self):
        return self._getString(0)

    def setName(self, value):
        self._setString(0, value)
        return

    def getRole(self):
        return self._getString(1)

    def setRole(self, value):
        self._setString(1, value)
        return

    def getIsAvailable(self):
        return self._getBool(2)

    def setIsAvailable(self, value):
        self._setBool(2, value)
        return

    def _initialize(self):
        super(CurrentEnemyModel, self)._initialize()
        self._addStringProperty(b'name', b'')
        self._addStringProperty(b'role', b'')
        self._addBoolProperty(b'isAvailable', False)
        return
