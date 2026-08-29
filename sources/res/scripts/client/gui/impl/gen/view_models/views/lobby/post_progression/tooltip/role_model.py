from frameworks.wulf import ViewModel

class RoleModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(RoleModel, self).__init__(properties=properties, commands=commands)
        return

    def getRole(self):
        return self._getString(0)

    def setRole(self, value):
        self._setString(0, value)
        return

    def getId(self):
        return self._getNumber(1)

    def setId(self, value):
        self._setNumber(1, value)
        return

    def _initialize(self):
        super(RoleModel, self)._initialize()
        self._addStringProperty(b'role', b'')
        self._addNumberProperty(b'id', 0)
        return
