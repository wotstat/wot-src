from gui.impl.gen.view_models.common.missions.bonuses.bonus_model import BonusModel

class DiscountBonusModel(BonusModel):
    __slots__ = ()
    NEW_YEAR_DISCOUNT_APPLY_POPOVER_ID = b'NYSelectVehicleForDiscountPopover'

    def __init__(self, properties=11, commands=0):
        super(DiscountBonusModel, self).__init__(properties=properties, commands=commands)
        return

    def getLevel(self):
        return self._getNumber(7)

    def setLevel(self, value):
        self._setNumber(7, value)
        return

    def getDiscount(self):
        return self._getNumber(8)

    def setDiscount(self, value):
        self._setNumber(8, value)
        return

    def getSelectedVehicle(self):
        return self._getString(9)

    def setSelectedVehicle(self, value):
        self._setString(9, value)
        return

    def getVariadicID(self):
        return self._getString(10)

    def setVariadicID(self, value):
        self._setString(10, value)
        return

    def _initialize(self):
        super(DiscountBonusModel, self)._initialize()
        self._addNumberProperty(b'level', 0)
        self._addNumberProperty(b'discount', 0)
        self._addStringProperty(b'selectedVehicle', b'')
        self._addStringProperty(b'variadicID', b'')
        return
