from gui.impl.gen.view_models.views.loot_box_compensation_tooltip_model import LootBoxCompensationTooltipModel

class LootBoxVehicleCompensationTooltipModel(LootBoxCompensationTooltipModel):
    __slots__ = ()

    def __init__(self, properties=11, commands=0):
        super(LootBoxVehicleCompensationTooltipModel, self).__init__(properties=properties, commands=commands)
        return

    def getIsElite(self):
        return self._getBool(7)

    def setIsElite(self, value):
        self._setBool(7, value)
        return

    def getVehicleName(self):
        return self._getString(8)

    def setVehicleName(self, value):
        self._setString(8, value)
        return

    def getVehicleType(self):
        return self._getString(9)

    def setVehicleType(self, value):
        self._setString(9, value)
        return

    def getVehicleLvl(self):
        return self._getString(10)

    def setVehicleLvl(self, value):
        self._setString(10, value)
        return

    def _initialize(self):
        super(LootBoxVehicleCompensationTooltipModel, self)._initialize()
        self._addBoolProperty(b'isElite', True)
        self._addStringProperty(b'vehicleName', b'')
        self._addStringProperty(b'vehicleType', b'')
        self._addStringProperty(b'vehicleLvl', b'')
        return
