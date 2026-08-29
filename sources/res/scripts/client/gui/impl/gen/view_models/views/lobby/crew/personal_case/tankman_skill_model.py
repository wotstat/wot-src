from frameworks.wulf import ViewModel

class TankmanSkillModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=7, commands=0):
        super(TankmanSkillModel, self).__init__(properties=properties, commands=commands)
        return

    def getSkillId(self):
        return self._getString(0)

    def setSkillId(self, value):
        self._setString(0, value)
        return

    def getSkillUserName(self):
        return self._getString(1)

    def setSkillUserName(self, value):
        self._setString(1, value)
        return

    def getSkillIcon(self):
        return self._getString(2)

    def setSkillIcon(self, value):
        self._setString(2, value)
        return

    def getSkillProgress(self):
        return self._getNumber(3)

    def setSkillProgress(self, value):
        self._setNumber(3, value)
        return

    def getIsInProgress(self):
        return self._getBool(4)

    def setIsInProgress(self, value):
        self._setBool(4, value)
        return

    def getIsZero(self):
        return self._getBool(5)

    def setIsZero(self, value):
        self._setBool(5, value)
        return

    def getIsSingleHasLearnt(self):
        return self._getBool(6)

    def setIsSingleHasLearnt(self, value):
        self._setBool(6, value)
        return

    def _initialize(self):
        super(TankmanSkillModel, self)._initialize()
        self._addStringProperty(b'skillId', b'')
        self._addStringProperty(b'skillUserName', b'')
        self._addStringProperty(b'skillIcon', b'')
        self._addNumberProperty(b'skillProgress', 0)
        self._addBoolProperty(b'isInProgress', False)
        self._addBoolProperty(b'isZero', False)
        self._addBoolProperty(b'isSingleHasLearnt', False)
        return
