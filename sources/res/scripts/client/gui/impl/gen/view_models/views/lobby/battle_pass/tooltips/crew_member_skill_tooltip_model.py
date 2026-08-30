from frameworks.wulf import ViewModel

class CrewMemberSkillTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(CrewMemberSkillTooltipModel, self).__init__(properties=properties, commands=commands)
        return

    def getName(self):
        return self._getString(0)

    def setName(self, value):
        self._setString(0, value)
        return

    def getIsZero(self):
        return self._getBool(1)

    def setIsZero(self, value):
        self._setBool(1, value)
        return

    def getHasZeroPerk(self):
        return self._getBool(2)

    def setHasZeroPerk(self, value):
        self._setBool(2, value)
        return

    def _initialize(self):
        super(CrewMemberSkillTooltipModel, self)._initialize()
        self._addStringProperty(b'name', b'')
        self._addBoolProperty(b'isZero', False)
        self._addBoolProperty(b'hasZeroPerk', False)
        return
