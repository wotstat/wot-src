from frameworks.wulf import Array, ViewModel

class PetTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=5, commands=0):
        super(PetTooltipModel, self).__init__(properties=properties, commands=commands)
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

    def getPromotionBonuses(self):
        return self._getArray(4)

    def setPromotionBonuses(self, value):
        self._setArray(4, value)
        return

    @staticmethod
    def getPromotionBonusesType():
        return unicode

    def _initialize(self):
        super(PetTooltipModel, self)._initialize()
        self._addNumberProperty(b'petNameID', 0)
        self._addNumberProperty(b'petID', 0)
        self._addStringProperty(b'petType', b'')
        self._addStringProperty(b'breedName', b'')
        self._addArrayProperty(b'promotionBonuses', Array())
        return
