from frameworks.wulf import Array, ViewModel

class CrewMemberModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(CrewMemberModel, self).__init__(properties=properties, commands=commands)
        return

    def getRole(self):
        return self._getString(0)

    def setRole(self, value):
        self._setString(0, value)
        return

    def getAdditionalRoles(self):
        return self._getArray(1)

    def setAdditionalRoles(self, value):
        self._setArray(1, value)
        return

    @staticmethod
    def getAdditionalRolesType():
        return unicode

    def _initialize(self):
        super(CrewMemberModel, self)._initialize()
        self._addStringProperty(b'role', b'')
        self._addArrayProperty(b'additionalRoles', Array())
        return
