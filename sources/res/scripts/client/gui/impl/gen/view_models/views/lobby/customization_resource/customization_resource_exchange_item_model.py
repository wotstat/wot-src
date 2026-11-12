from frameworks.wulf import ViewModel

class CustomizationResourceExchangeItemModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=13, commands=0):
        super(CustomizationResourceExchangeItemModel, self).__init__(properties=properties, commands=commands)
        return

    def getIntCD(self):
        return self._getNumber(0)

    def setIntCD(self, value):
        self._setNumber(0, value)
        return

    def getVehicleCD(self):
        return self._getNumber(1)

    def setVehicleCD(self, value):
        self._setNumber(1, value)
        return

    def getName(self):
        return self._getString(2)

    def setName(self, value):
        self._setString(2, value)
        return

    def getIcon(self):
        return self._getString(3)

    def setIcon(self, value):
        self._setString(3, value)
        return

    def getVehicleName(self):
        return self._getString(4)

    def setVehicleName(self, value):
        self._setString(4, value)
        return

    def getTooltip(self):
        return self._getString(5)

    def setTooltip(self, value):
        self._setString(5, value)
        return

    def getInventoryCount(self):
        return self._getNumber(6)

    def setInventoryCount(self, value):
        self._setNumber(6, value)
        return

    def getInstalledCount(self):
        return self._getNumber(7)

    def setInstalledCount(self, value):
        self._setNumber(7, value)
        return

    def getAvailableCount(self):
        return self._getNumber(8)

    def setAvailableCount(self, value):
        self._setNumber(8, value)
        return

    def getSelectedCount(self):
        return self._getNumber(9)

    def setSelectedCount(self, value):
        self._setNumber(9, value)
        return

    def getIsWide(self):
        return self._getBool(10)

    def setIsWide(self, value):
        self._setBool(10, value)
        return

    def getExchangePrice(self):
        return self._getNumber(11)

    def setExchangePrice(self, value):
        self._setNumber(11, value)
        return

    def getIsFilled(self):
        return self._getBool(12)

    def setIsFilled(self, value):
        self._setBool(12, value)
        return

    def _initialize(self):
        super(CustomizationResourceExchangeItemModel, self)._initialize()
        self._addNumberProperty(b'intCD', 0)
        self._addNumberProperty(b'vehicleCD', 0)
        self._addStringProperty(b'name', b'')
        self._addStringProperty(b'icon', b'')
        self._addStringProperty(b'vehicleName', b'')
        self._addStringProperty(b'tooltip', b'')
        self._addNumberProperty(b'inventoryCount', 0)
        self._addNumberProperty(b'installedCount', 0)
        self._addNumberProperty(b'availableCount', 0)
        self._addNumberProperty(b'selectedCount', 0)
        self._addBoolProperty(b'isWide', False)
        self._addNumberProperty(b'exchangePrice', 0)
        self._addBoolProperty(b'isFilled', False)
        return
