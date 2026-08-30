from frameworks.wulf import ViewModel

class PetCardModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=6, commands=0):
        super(PetCardModel, self).__init__(properties=properties, commands=commands)
        return

    def getPetID(self):
        return self._getNumber(0)

    def setPetID(self, value):
        self._setNumber(0, value)
        return

    def getPetNameID(self):
        return self._getNumber(1)

    def setPetNameID(self, value):
        self._setNumber(1, value)
        return

    def getBonusName(self):
        return self._getString(2)

    def setBonusName(self, value):
        self._setString(2, value)
        return

    def getBonusValue(self):
        return self._getNumber(3)

    def setBonusValue(self, value):
        self._setNumber(3, value)
        return

    def getIsMaxSynergyLevel(self):
        return self._getBool(4)

    def setIsMaxSynergyLevel(self, value):
        self._setBool(4, value)
        return

    def getIsNew(self):
        return self._getBool(5)

    def setIsNew(self, value):
        self._setBool(5, value)
        return

    def _initialize(self):
        super(PetCardModel, self)._initialize()
        self._addNumberProperty(b'petID', 0)
        self._addNumberProperty(b'petNameID', 0)
        self._addStringProperty(b'bonusName', b'')
        self._addNumberProperty(b'bonusValue', 0)
        self._addBoolProperty(b'isMaxSynergyLevel', False)
        self._addBoolProperty(b'isNew', False)
        return
