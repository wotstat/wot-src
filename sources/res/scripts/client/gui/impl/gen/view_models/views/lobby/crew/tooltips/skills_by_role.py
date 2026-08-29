from frameworks.wulf import Array
from frameworks.wulf import ViewModel

class SkillsByRole(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(SkillsByRole, self).__init__(properties=properties, commands=commands)
        return

    def getRole(self):
        return self._getString(0)

    def setRole(self, value):
        self._setString(0, value)
        return

    def getSkills(self):
        return self._getArray(1)

    def setSkills(self, value):
        self._setArray(1, value)
        return

    @staticmethod
    def getSkillsType():
        return unicode

    def _initialize(self):
        super(SkillsByRole, self)._initialize()
        self._addStringProperty(b'role', b'')
        self._addArrayProperty(b'skills', Array())
        return
