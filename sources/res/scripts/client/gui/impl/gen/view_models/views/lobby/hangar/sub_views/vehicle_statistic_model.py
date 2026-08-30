from frameworks.wulf import Array, ViewModel

class VehicleStatisticModel(ViewModel):
    __slots__ = ()
    IRON = b'iron'
    BRONZE = b'bronze'
    SILVER = b'silver'
    GOLD = b'gold'
    ENAMEL = b'enamel'
    MAXIMUM = b'prestige'
    UNDEFINED = b'undefined'

    def __init__(self, properties=22, commands=0):
        super(VehicleStatisticModel, self).__init__(properties=properties, commands=commands)
        return

    def getId(self):
        return self._getString(0)

    def setId(self, value):
        self._setString(0, value)
        return

    def getIntCD(self):
        return self._getNumber(1)

    def setIntCD(self, value):
        self._setNumber(1, value)
        return

    def getInventoryId(self):
        return self._getNumber(2)

    def setInventoryId(self, value):
        self._setNumber(2, value)
        return

    def getXp(self):
        return self._getNumber(3)

    def setXp(self, value):
        self._setNumber(3, value)
        return

    def getStatus(self):
        return self._getString(4)

    def setStatus(self, value):
        self._setString(4, value)
        return

    def getStateLevel(self):
        return self._getString(5)

    def setStateLevel(self, value):
        self._setString(5, value)
        return

    def getElite(self):
        return self._getBool(6)

    def setElite(self, value):
        self._setBool(6, value)
        return

    def getBonusMultiplier(self):
        return self._getNumber(7)

    def setBonusMultiplier(self, value):
        self._setNumber(7, value)
        return

    def getMastery(self):
        return self._getNumber(8)

    def setMastery(self, value):
        self._setNumber(8, value)
        return

    def getBattlesCount(self):
        return self._getNumber(9)

    def setBattlesCount(self, value):
        self._setNumber(9, value)
        return

    def getWinsCount(self):
        return self._getNumber(10)

    def setWinsCount(self, value):
        self._setNumber(10, value)
        return

    def getTooltipID(self):
        return self._getNumber(11)

    def setTooltipID(self, value):
        self._setNumber(11, value)
        return

    def getPrestigeLevel(self):
        return self._getNumber(12)

    def setPrestigeLevel(self, value):
        self._setNumber(12, value)
        return

    def getPrestigeGrade(self):
        return self._getNumber(13)

    def setPrestigeGrade(self, value):
        self._setNumber(13, value)
        return

    def getPrestigeType(self):
        return self._getString(14)

    def setPrestigeType(self, value):
        self._setString(14, value)
        return

    def getFromWotPlus(self):
        return self._getBool(15)

    def setFromWotPlus(self, value):
        self._setBool(15, value)
        return

    def getProBoostActive(self):
        return self._getBool(16)

    def setProBoostActive(self, value):
        self._setBool(16, value)
        return

    def getBpSpecial(self):
        return self._getBool(17)

    def setBpSpecial(self, value):
        self._setBool(17, value)
        return

    def getMaxBpScore(self):
        return self._getNumber(18)

    def setMaxBpScore(self, value):
        self._setNumber(18, value)
        return

    def getBpProgress(self):
        return self._getNumber(19)

    def setBpProgress(self, value):
        self._setNumber(19, value)
        return

    def getNumberOfCrystalEarned(self):
        return self._getArray(20)

    def setNumberOfCrystalEarned(self, value):
        self._setArray(20, value)
        return

    @staticmethod
    def getNumberOfCrystalEarnedType():
        return int

    def getOwn3DStyle(self):
        return self._getBool(21)

    def setOwn3DStyle(self, value):
        self._setBool(21, value)
        return

    def _initialize(self):
        super(VehicleStatisticModel, self)._initialize()
        self._addStringProperty(b'id', b'')
        self._addNumberProperty(b'intCD', 0)
        self._addNumberProperty(b'inventoryId', 0)
        self._addNumberProperty(b'xp', 0)
        self._addStringProperty(b'status', b'none')
        self._addStringProperty(b'stateLevel', b'')
        self._addBoolProperty(b'elite', False)
        self._addNumberProperty(b'bonusMultiplier', -1)
        self._addNumberProperty(b'mastery', 0)
        self._addNumberProperty(b'battlesCount', 0)
        self._addNumberProperty(b'winsCount', 0)
        self._addNumberProperty(b'tooltipID', -1)
        self._addNumberProperty(b'prestigeLevel', -1)
        self._addNumberProperty(b'prestigeGrade', -1)
        self._addStringProperty(b'prestigeType', b'')
        self._addBoolProperty(b'fromWotPlus', False)
        self._addBoolProperty(b'proBoostActive', False)
        self._addBoolProperty(b'bpSpecial', False)
        self._addNumberProperty(b'maxBpScore', -1)
        self._addNumberProperty(b'bpProgress', -1)
        self._addArrayProperty(b'numberOfCrystalEarned', Array())
        self._addBoolProperty(b'own3DStyle', False)
        return
