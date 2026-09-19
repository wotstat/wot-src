from frameworks.wulf import Array, ViewModel

class AbilityTooltipViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=10, commands=0):
        super(AbilityTooltipViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getAbilityName(self):
        return self._getString(0)

    def setAbilityName(self, value):
        self._setString(0, value)
        return

    def getIcon(self):
        return self._getString(1)

    def setIcon(self, value):
        self._setString(1, value)
        return

    def getCooldown(self):
        return self._getNumber(2)

    def setCooldown(self, value):
        self._setNumber(2, value)
        return

    def getMiriumCost(self):
        return self._getNumber(3)

    def setMiriumCost(self, value):
        self._setNumber(3, value)
        return

    def getAbilityPrice(self):
        return self._getNumber(4)

    def setAbilityPrice(self, value):
        self._setNumber(4, value)
        return

    def getCurrencyType(self):
        return self._getString(5)

    def setCurrencyType(self, value):
        self._setString(5, value)
        return

    def getRequiredMore(self):
        return self._getNumber(6)

    def setRequiredMore(self, value):
        self._setNumber(6, value)
        return

    def getInDepot(self):
        return self._getNumber(7)

    def setInDepot(self, value):
        self._setNumber(7, value)
        return

    def getInVehiclesList(self):
        return self._getArray(8)

    def setInVehiclesList(self, value):
        self._setArray(8, value)
        return

    @staticmethod
    def getInVehiclesListType():
        return unicode

    def getShowPriceBlock(self):
        return self._getBool(9)

    def setShowPriceBlock(self, value):
        self._setBool(9, value)
        return

    def _initialize(self):
        super(AbilityTooltipViewModel, self)._initialize()
        self._addStringProperty(b'abilityName', b'')
        self._addStringProperty(b'icon', b'')
        self._addNumberProperty(b'cooldown', 0)
        self._addNumberProperty(b'miriumCost', 0)
        self._addNumberProperty(b'abilityPrice', 0)
        self._addStringProperty(b'currencyType', b'')
        self._addNumberProperty(b'requiredMore', 0)
        self._addNumberProperty(b'inDepot', 0)
        self._addArrayProperty(b'inVehiclesList', Array())
        self._addBoolProperty(b'showPriceBlock', True)
        return
