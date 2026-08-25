from frameworks.wulf import ViewModel

class TitleModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=5, commands=0):
        super(TitleModel, self).__init__(properties=properties, commands=commands)
        return

    def getTitle(self):
        return self._getString(0)

    def setTitle(self, value):
        self._setString(0, value)
        return

    def getSkillName(self):
        return self._getString(1)

    def setSkillName(self, value):
        self._setString(1, value)
        return

    def getRoleName(self):
        return self._getString(2)

    def setRoleName(self, value):
        self._setString(2, value)
        return

    def getSkillCustomName(self):
        return self._getString(3)

    def setSkillCustomName(self, value):
        self._setString(3, value)
        return

    def getIconName(self):
        return self._getString(4)

    def setIconName(self, value):
        self._setString(4, value)
        return

    def _initialize(self):
        super(TitleModel, self)._initialize()
        self._addStringProperty(b'title', b'')
        self._addStringProperty(b'skillName', b'')
        self._addStringProperty(b'roleName', b'')
        self._addStringProperty(b'skillCustomName', b'')
        self._addStringProperty(b'iconName', b'')
        return
