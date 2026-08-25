from frameworks.wulf import ViewModel

class VehiclesInventoryModel(ViewModel):
    __slots__ = (b'onSelect', b'onBuySlot', b'onGoBuyVehicle', b'onGoRecoverVehicle', b'onSelectTelecomRentalVehicle')
    NO_VEHICLE_ID = -1
    ENABLED = b'enabled'
    DISABLED = b'disabled'
    PAUSED = b'paused'
    READY_TO_SELECT = b'readyToSelect'
    PENDING = b'pending'

    def __init__(self, properties=11, commands=5):
        super(VehiclesInventoryModel, self).__init__(properties=properties, commands=commands)
        return

    def getCurrentVehicleIntCD(self):
        return self._getNumber(0)

    def setCurrentVehicleIntCD(self, value):
        self._setNumber(0, value)
        return

    def getCurrentVehicleInventoryId(self):
        return self._getNumber(1)

    def setCurrentVehicleInventoryId(self, value):
        self._setNumber(1, value)
        return

    def getFreeSlotsCount(self):
        return self._getNumber(2)

    def setFreeSlotsCount(self, value):
        self._setNumber(2, value)
        return

    def getRecoverableVehicleCount(self):
        return self._getNumber(3)

    def setRecoverableVehicleCount(self, value):
        self._setNumber(3, value)
        return

    def getSlotPrice(self):
        return self._getNumber(4)

    def setSlotPrice(self, value):
        self._setNumber(4, value)
        return

    def getDefaultSlotPrice(self):
        return self._getNumber(5)

    def setDefaultSlotPrice(self, value):
        self._setNumber(5, value)
        return

    def getBpEntityValid(self):
        return self._getBool(6)

    def setBpEntityValid(self, value):
        self._setBool(6, value)
        return

    def getBpStatus(self):
        return self._getString(7)

    def setBpStatus(self, value):
        self._setString(7, value)
        return

    def getSlotPriceCurrency(self):
        return self._getString(8)

    def setSlotPriceCurrency(self, value):
        self._setString(8, value)
        return

    def getHasDiscont(self):
        return self._getBool(9)

    def setHasDiscont(self, value):
        self._setBool(9, value)
        return

    def getTelecomRentStatus(self):
        return self._getString(10)

    def setTelecomRentStatus(self, value):
        self._setString(10, value)
        return

    def _initialize(self):
        super(VehiclesInventoryModel, self)._initialize()
        self._addNumberProperty(b'currentVehicleIntCD', -1)
        self._addNumberProperty(b'currentVehicleInventoryId', -1)
        self._addNumberProperty(b'freeSlotsCount', 0)
        self._addNumberProperty(b'recoverableVehicleCount', 0)
        self._addNumberProperty(b'slotPrice', 0)
        self._addNumberProperty(b'defaultSlotPrice', 0)
        self._addBoolProperty(b'bpEntityValid', False)
        self._addStringProperty(b'bpStatus', b'')
        self._addStringProperty(b'slotPriceCurrency', b'')
        self._addBoolProperty(b'hasDiscont', False)
        self._addStringProperty(b'telecomRentStatus', b'')
        self.onSelect = self._addCommand(b'onSelect')
        self.onBuySlot = self._addCommand(b'onBuySlot')
        self.onGoBuyVehicle = self._addCommand(b'onGoBuyVehicle')
        self.onGoRecoverVehicle = self._addCommand(b'onGoRecoverVehicle')
        self.onSelectTelecomRentalVehicle = self._addCommand(b'onSelectTelecomRentalVehicle')
        return
