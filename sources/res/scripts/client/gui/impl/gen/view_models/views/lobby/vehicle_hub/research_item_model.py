from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.common.vehicle_mechanic_model import VehicleMechanicModel

class ResearchItemModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=24, commands=0):
        super(ResearchItemModel, self).__init__(properties=properties, commands=commands)
        return

    def getId(self):
        return self._getNumber(0)

    def setId(self, value):
        self._setNumber(0, value)
        return

    def getImage(self):
        return self._getString(1)

    def setImage(self, value):
        self._setString(1, value)
        return

    def getUserName(self):
        return self._getString(2)

    def setUserName(self, value):
        self._setString(2, value)
        return

    def getState(self):
        return self._getNumber(3)

    def setState(self, value):
        self._setNumber(3, value)
        return

    def getRenderer(self):
        return self._getString(4)

    def setRenderer(self, value):
        self._setString(4, value)
        return

    def getIsInstalled(self):
        return self._getBool(5)

    def setIsInstalled(self, value):
        self._setBool(5, value)
        return

    def getIsDisabled(self):
        return self._getBool(6)

    def setIsDisabled(self, value):
        self._setBool(6, value)
        return

    def getLevel(self):
        return self._getNumber(7)

    def setLevel(self, value):
        self._setNumber(7, value)
        return

    def getRequiredXp(self):
        return self._getNumber(8)

    def setRequiredXp(self, value):
        self._setNumber(8, value)
        return

    def getIsDiscountedXp(self):
        return self._getBool(9)

    def setIsDiscountedXp(self, value):
        self._setBool(9, value)
        return

    def getEarnedXp(self):
        return self._getNumber(10)

    def setEarnedXp(self, value):
        self._setNumber(10, value)
        return

    def getPriceAmount(self):
        return self._getNumber(11)

    def setPriceAmount(self, value):
        self._setNumber(11, value)
        return

    def getPriceCurrency(self):
        return self._getString(12)

    def setPriceCurrency(self, value):
        self._setString(12, value)
        return

    def getIsDiscountedPrice(self):
        return self._getBool(13)

    def setIsDiscountedPrice(self, value):
        self._setBool(13, value)
        return

    def getPrimaryClass(self):
        return self._getString(14)

    def setPrimaryClass(self, value):
        self._setString(14, value)
        return

    def getIsResearched(self):
        return self._getBool(15)

    def setIsResearched(self, value):
        self._setBool(15, value)
        return

    def getHasEnoughCurrency(self):
        return self._getBool(16)

    def setHasEnoughCurrency(self, value):
        self._setBool(16, value)
        return

    def getHasEnoughXP(self):
        return self._getBool(17)

    def setHasEnoughXP(self, value):
        self._setBool(17, value)
        return

    def getIsElite(self):
        return self._getBool(18)

    def setIsElite(self, value):
        self._setBool(18, value)
        return

    def getAutoUnlocked(self):
        return self._getBool(19)

    def setAutoUnlocked(self, value):
        self._setBool(19, value)
        return

    def getIsInInventory(self):
        return self._getBool(20)

    def setIsInInventory(self, value):
        self._setBool(20, value)
        return

    def getUrgentIds(self):
        return self._getArray(21)

    def setUrgentIds(self, value):
        self._setArray(21, value)
        return

    @staticmethod
    def getUrgentIdsType():
        return int

    def getPath(self):
        return self._getArray(22)

    def setPath(self, value):
        self._setArray(22, value)
        return

    @staticmethod
    def getPathType():
        return int

    def getMechanics(self):
        return self._getArray(23)

    def setMechanics(self, value):
        self._setArray(23, value)
        return

    @staticmethod
    def getMechanicsType():
        return VehicleMechanicModel

    def _initialize(self):
        super(ResearchItemModel, self)._initialize()
        self._addNumberProperty(b'id', 0)
        self._addStringProperty(b'image', b'')
        self._addStringProperty(b'userName', b'')
        self._addNumberProperty(b'state', 0)
        self._addStringProperty(b'renderer', b'')
        self._addBoolProperty(b'isInstalled', False)
        self._addBoolProperty(b'isDisabled', False)
        self._addNumberProperty(b'level', 1)
        self._addNumberProperty(b'requiredXp', 0)
        self._addBoolProperty(b'isDiscountedXp', False)
        self._addNumberProperty(b'earnedXp', 0)
        self._addNumberProperty(b'priceAmount', 0)
        self._addStringProperty(b'priceCurrency', b'')
        self._addBoolProperty(b'isDiscountedPrice', False)
        self._addStringProperty(b'primaryClass', b'')
        self._addBoolProperty(b'isResearched', False)
        self._addBoolProperty(b'hasEnoughCurrency', False)
        self._addBoolProperty(b'hasEnoughXP', False)
        self._addBoolProperty(b'isElite', False)
        self._addBoolProperty(b'autoUnlocked', False)
        self._addBoolProperty(b'isInInventory', False)
        self._addArrayProperty(b'urgentIds', Array())
        self._addArrayProperty(b'path', Array())
        self._addArrayProperty(b'mechanics', Array())
        return
