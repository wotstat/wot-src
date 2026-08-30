from frameworks.wulf import ViewModel

class PetStorageTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=9, commands=0):
        super(PetStorageTooltipModel, self).__init__(properties=properties, commands=commands)
        return

    def getPetNameID(self):
        return self._getNumber(0)

    def setPetNameID(self, value):
        self._setNumber(0, value)
        return

    def getPetID(self):
        return self._getNumber(1)

    def setPetID(self, value):
        self._setNumber(1, value)
        return

    def getPetType(self):
        return self._getString(2)

    def setPetType(self, value):
        self._setString(2, value)
        return

    def getBreedName(self):
        return self._getString(3)

    def setBreedName(self, value):
        self._setString(3, value)
        return

    def getBonusName(self):
        return self._getString(4)

    def setBonusName(self, value):
        self._setString(4, value)
        return

    def getBonusValue(self):
        return self._getNumber(5)

    def setBonusValue(self, value):
        self._setNumber(5, value)
        return

    def getTotalBattleCount(self):
        return self._getNumber(6)

    def setTotalBattleCount(self, value):
        self._setNumber(6, value)
        return

    def getCurrentBattleCount(self):
        return self._getNumber(7)

    def setCurrentBattleCount(self, value):
        self._setNumber(7, value)
        return

    def getIsUnsuitableMode(self):
        return self._getBool(8)

    def setIsUnsuitableMode(self, value):
        self._setBool(8, value)
        return

    def _initialize(self):
        super(PetStorageTooltipModel, self)._initialize()
        self._addNumberProperty(b'petNameID', 0)
        self._addNumberProperty(b'petID', 0)
        self._addStringProperty(b'petType', b'')
        self._addStringProperty(b'breedName', b'')
        self._addStringProperty(b'bonusName', b'')
        self._addNumberProperty(b'bonusValue', 0)
        self._addNumberProperty(b'totalBattleCount', 0)
        self._addNumberProperty(b'currentBattleCount', 0)
        self._addBoolProperty(b'isUnsuitableMode', False)
        return
