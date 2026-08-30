from frameworks.wulf import ViewModel

class QualificationTooltipViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(QualificationTooltipViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getRoleName(self):
        return self._getString(0)

    def setRoleName(self, value):
        self._setString(0, value)
        return

    def getQualificationIndex(self):
        return self._getNumber(1)

    def setQualificationIndex(self, value):
        self._setNumber(1, value)
        return

    def getIsFemale(self):
        return self._getBool(2)

    def setIsFemale(self, value):
        self._setBool(2, value)
        return

    def getIsBonusQualification(self):
        return self._getBool(3)

    def setIsBonusQualification(self, value):
        self._setBool(3, value)
        return

    def _initialize(self):
        super(QualificationTooltipViewModel, self)._initialize()
        self._addStringProperty(b'roleName', b'')
        self._addNumberProperty(b'qualificationIndex', 0)
        self._addBoolProperty(b'isFemale', False)
        self._addBoolProperty(b'isBonusQualification', False)
        return
