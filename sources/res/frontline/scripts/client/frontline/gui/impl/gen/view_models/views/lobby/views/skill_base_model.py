from frameworks.wulf import ViewModel

class SkillBaseModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(SkillBaseModel, self).__init__(properties=properties, commands=commands)
        return

    def getId(self):
        return self._getNumber(0)

    def setId(self, value):
        self._setNumber(0, value)
        return

    def getIcon(self):
        return self._getString(1)

    def setIcon(self, value):
        self._setString(1, value)
        return

    def getName(self):
        return self._getString(2)

    def setName(self, value):
        self._setString(2, value)
        return

    def _initialize(self):
        super(SkillBaseModel, self)._initialize()
        self._addNumberProperty(b'id', 0)
        self._addStringProperty(b'icon', b'')
        self._addStringProperty(b'name', b'')
        return
