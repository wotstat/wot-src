from frameworks.wulf import ViewModel

class RetrainRoleModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(RetrainRoleModel, self).__init__(properties=properties, commands=commands)
        return

    def getIconName(self):
        return self._getString(0)

    def setIconName(self, value):
        self._setString(0, value)
        return

    def getIsTaken(self):
        return self._getBool(1)

    def setIsTaken(self, value):
        self._setBool(1, value)
        return

    def getRolesCount(self):
        return self._getNumber(2)

    def setRolesCount(self, value):
        self._setNumber(2, value)
        return

    def _initialize(self):
        super(RetrainRoleModel, self)._initialize()
        self._addStringProperty(b'iconName', b'')
        self._addBoolProperty(b'isTaken', False)
        self._addNumberProperty(b'rolesCount', 0)
        return
