from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.views.lobby.tank_setup.common.base_ammunition_slot import BaseAmmunitionSlot

class AmmunitionItemsSection(ViewModel):
    __slots__ = ()

    def __init__(self, properties=6, commands=0):
        super(AmmunitionItemsSection, self).__init__(properties=properties, commands=commands)
        return

    def getType(self):
        return self._getString(0)

    def setType(self, value):
        self._setString(0, value)
        return

    def getName(self):
        return self._getString(1)

    def setName(self, value):
        self._setString(1, value)
        return

    def getVehicle(self):
        return self._getString(2)

    def setVehicle(self, value):
        self._setString(2, value)
        return

    def getVehicleType(self):
        return self._getString(3)

    def setVehicleType(self, value):
        self._setString(3, value)
        return

    def getNewItemsCount(self):
        return self._getNumber(4)

    def setNewItemsCount(self, value):
        self._setNumber(4, value)
        return

    def getSlots(self):
        return self._getArray(5)

    def setSlots(self, value):
        self._setArray(5, value)
        return

    @staticmethod
    def getSlotsType():
        return BaseAmmunitionSlot

    def _initialize(self):
        super(AmmunitionItemsSection, self)._initialize()
        self._addStringProperty(b'type', b'')
        self._addStringProperty(b'name', b'')
        self._addStringProperty(b'vehicle', b'')
        self._addStringProperty(b'vehicleType', b'')
        self._addNumberProperty(b'newItemsCount', 0)
        self._addArrayProperty(b'slots', Array())
        return
