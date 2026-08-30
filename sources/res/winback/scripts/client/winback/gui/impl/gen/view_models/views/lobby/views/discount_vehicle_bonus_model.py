from winback.gui.impl.gen.view_models.views.lobby.views.vehicle_bonus_model import VehicleBonusModel

class DiscountVehicleBonusModel(VehicleBonusModel):
    __slots__ = ()

    def __init__(self, properties=22, commands=0):
        super(DiscountVehicleBonusModel, self).__init__(properties=properties, commands=commands)
        return

    def getOldPrice(self):
        return self._getNumber(17)

    def setOldPrice(self, value):
        self._setNumber(17, value)
        return

    def getNewPrice(self):
        return self._getNumber(18)

    def setNewPrice(self, value):
        self._setNumber(18, value)
        return

    def getOldExp(self):
        return self._getNumber(19)

    def setOldExp(self, value):
        self._setNumber(19, value)
        return

    def getNewExp(self):
        return self._getNumber(20)

    def setNewExp(self, value):
        self._setNumber(20, value)
        return

    def getIsSelected(self):
        return self._getBool(21)

    def setIsSelected(self, value):
        self._setBool(21, value)
        return

    def _initialize(self):
        super(DiscountVehicleBonusModel, self)._initialize()
        self._addNumberProperty(b'oldPrice', 0)
        self._addNumberProperty(b'newPrice', 0)
        self._addNumberProperty(b'oldExp', 0)
        self._addNumberProperty(b'newExp', 0)
        self._addBoolProperty(b'isSelected', False)
        return
