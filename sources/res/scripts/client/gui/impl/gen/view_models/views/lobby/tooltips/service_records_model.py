from frameworks.wulf import ViewModel

class ServiceRecordsModel(ViewModel):
    __slots__ = ()
    IRON = b'iron'
    BRONZE = b'bronze'
    SILVER = b'silver'
    GOLD = b'gold'
    ENAMEL = b'enamel'
    MAXIMUM = b'prestige'
    UNDEFINED = b'undefined'

    def __init__(self, properties=10, commands=0):
        super(ServiceRecordsModel, self).__init__(properties=properties, commands=commands)
        return

    def getPrestigeLevel(self):
        return self._getNumber(0)

    def setPrestigeLevel(self, value):
        self._setNumber(0, value)
        return

    def getPrestigeGrade(self):
        return self._getNumber(1)

    def setPrestigeGrade(self, value):
        self._setNumber(1, value)
        return

    def getPrestigeType(self):
        return self._getString(2)

    def setPrestigeType(self, value):
        self._setString(2, value)
        return

    def getPrestigeXp(self):
        return self._getNumber(3)

    def setPrestigeXp(self, value):
        self._setNumber(3, value)
        return

    def getPrestigeXpNextLevel(self):
        return self._getNumber(4)

    def setPrestigeXpNextLevel(self, value):
        self._setNumber(4, value)
        return

    def getMarksOnGun(self):
        return self._getNumber(5)

    def setMarksOnGun(self, value):
        self._setNumber(5, value)
        return

    def getMarksOnGunPercentage(self):
        return self._getString(6)

    def setMarksOnGunPercentage(self, value):
        self._setString(6, value)
        return

    def getMarksOfMastery(self):
        return self._getNumber(7)

    def setMarksOfMastery(self, value):
        self._setNumber(7, value)
        return

    def getWinsCount(self):
        return self._getNumber(8)

    def setWinsCount(self, value):
        self._setNumber(8, value)
        return

    def getBattlesCount(self):
        return self._getNumber(9)

    def setBattlesCount(self, value):
        self._setNumber(9, value)
        return

    def _initialize(self):
        super(ServiceRecordsModel, self)._initialize()
        self._addNumberProperty(b'prestigeLevel', -1)
        self._addNumberProperty(b'prestigeGrade', -1)
        self._addStringProperty(b'prestigeType', b'')
        self._addNumberProperty(b'prestigeXp', 0)
        self._addNumberProperty(b'prestigeXpNextLevel', 0)
        self._addNumberProperty(b'marksOnGun', -1)
        self._addStringProperty(b'marksOnGunPercentage', b'')
        self._addNumberProperty(b'marksOfMastery', 0)
        self._addNumberProperty(b'winsCount', 0)
        self._addNumberProperty(b'battlesCount', 0)
        return
