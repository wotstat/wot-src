from gui.impl.gen.view_models.views.loot_box_view.loot_compensation_renderer_model import LootCompensationRendererModel

class LootVehicleCompensationRendererModel(LootCompensationRendererModel):
    __slots__ = ()

    def __init__(self, properties=29, commands=0):
        super(LootVehicleCompensationRendererModel, self).__init__(properties=properties, commands=commands)
        return

    def getVehicleName(self):
        return self._getString(25)

    def setVehicleName(self, value):
        self._setString(25, value)
        return

    def getVehicleType(self):
        return self._getString(26)

    def setVehicleType(self, value):
        self._setString(26, value)
        return

    def getVehicleLvl(self):
        return self._getString(27)

    def setVehicleLvl(self, value):
        self._setString(27, value)
        return

    def getIsElite(self):
        return self._getBool(28)

    def setIsElite(self, value):
        self._setBool(28, value)
        return

    def _initialize(self):
        super(LootVehicleCompensationRendererModel, self)._initialize()
        self._addStringProperty(b'vehicleName', b'')
        self._addStringProperty(b'vehicleType', b'')
        self._addStringProperty(b'vehicleLvl', b'')
        self._addBoolProperty(b'isElite', True)
        return
