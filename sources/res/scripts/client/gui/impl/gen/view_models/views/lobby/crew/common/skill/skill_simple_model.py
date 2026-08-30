from frameworks.wulf import ViewModel

class SkillSimpleModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(SkillSimpleModel, self).__init__(properties=properties, commands=commands)
        return

    def getName(self):
        return self._getString(0)

    def setName(self, value):
        self._setString(0, value)
        return

    def getIconName(self):
        return self._getString(1)

    def setIconName(self, value):
        self._setString(1, value)
        return

    def getRoleName(self):
        return self._getString(2)

    def setRoleName(self, value):
        self._setString(2, value)
        return

    def getLevel(self):
        return self._getReal(3)

    def setLevel(self, value):
        self._setReal(3, value)
        return

    def _initialize(self):
        super(SkillSimpleModel, self)._initialize()
        self._addStringProperty(b'name', b'')
        self._addStringProperty(b'iconName', b'')
        self._addStringProperty(b'roleName', b'')
        self._addRealProperty(b'level', 0.0)
        return
