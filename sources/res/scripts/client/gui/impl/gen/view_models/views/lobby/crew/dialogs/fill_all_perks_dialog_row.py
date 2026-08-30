from frameworks.wulf import Array, ViewModel

class FillAllPerksDialogRow(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(FillAllPerksDialogRow, self).__init__(properties=properties, commands=commands)
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
        super(FillAllPerksDialogRow, self)._initialize()
        self._addStringProperty(b'role', b'')
        self._addArrayProperty(b'skills', Array())
        return
