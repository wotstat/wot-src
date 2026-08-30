from frameworks.wulf import ViewModel

class DtComponent(ViewModel):
    __slots__ = ()

    def __init__(self, properties=14, commands=0):
        super(DtComponent, self).__init__(properties=properties, commands=commands)
        return

    def getId(self):
        return self._getNumber(0)

    def setId(self, value):
        self._setNumber(0, value)
        return

    def getType(self):
        return self._getString(1)

    def setType(self, value):
        self._setString(1, value)
        return

    def getIsLocked(self):
        return self._getBool(2)

    def setIsLocked(self, value):
        self._setBool(2, value)
        return

    def getPurpose(self):
        return self._getString(3)

    def setPurpose(self, value):
        self._setString(3, value)
        return

    def getCurrentGradeValue(self):
        return self._getReal(4)

    def setCurrentGradeValue(self, value):
        self._setReal(4, value)
        return

    def getNextGradeValue(self):
        return self._getReal(5)

    def setNextGradeValue(self, value):
        self._setReal(5, value)
        return

    def getCurrentGrade(self):
        return self._getNumber(6)

    def setCurrentGrade(self, value):
        self._setNumber(6, value)
        return

    def getCurrentProgress(self):
        return self._getReal(7)

    def setCurrentProgress(self, value):
        self._setReal(7, value)
        return

    def getProgressNumberType(self):
        return self._getString(8)

    def setProgressNumberType(self, value):
        self._setString(8, value)
        return

    def getIsNew(self):
        return self._getBool(9)

    def setIsNew(self, value):
        self._setBool(9, value)
        return

    def getDisplayableProgress(self):
        return self._getString(10)

    def setDisplayableProgress(self, value):
        self._setString(10, value)
        return

    def getIsDeprecated(self):
        return self._getBool(11)

    def setIsDeprecated(self, value):
        self._setBool(11, value)
        return

    def getIsExternalUnlockOnly(self):
        return self._getBool(12)

    def setIsExternalUnlockOnly(self, value):
        self._setBool(12, value)
        return

    def getIsDemoted(self):
        return self._getBool(13)

    def setIsDemoted(self, value):
        self._setBool(13, value)
        return

    def _initialize(self):
        super(DtComponent, self)._initialize()
        self._addNumberProperty(b'id', 0)
        self._addStringProperty(b'type', b'')
        self._addBoolProperty(b'isLocked', False)
        self._addStringProperty(b'purpose', b'')
        self._addRealProperty(b'currentGradeValue', 0.0)
        self._addRealProperty(b'nextGradeValue', 0.0)
        self._addNumberProperty(b'currentGrade', 0)
        self._addRealProperty(b'currentProgress', 0.0)
        self._addStringProperty(b'progressNumberType', b'')
        self._addBoolProperty(b'isNew', False)
        self._addStringProperty(b'displayableProgress', b'')
        self._addBoolProperty(b'isDeprecated', False)
        self._addBoolProperty(b'isExternalUnlockOnly', False)
        self._addBoolProperty(b'isDemoted', False)
        return
