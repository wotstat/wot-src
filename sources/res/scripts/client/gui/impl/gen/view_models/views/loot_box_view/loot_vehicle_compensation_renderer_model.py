from gui.impl.gen.view_models.views.loot_box_view.loot_compensation_renderer_model import LootCompensationRendererModel

class LootVehicleCompensationRendererModel(LootCompensationRendererModel):
    __slots__ = ()

    def __init__(self, properties=30, commands=0):
        super(LootVehicleCompensationRendererModel, self).__init__(properties=properties, commands=commands)
        return

    def getVehicleName(self):
        return self._getString(26)

    def setVehicleName(self, value):
        self._setString(26, value)
        return

    def getVehicleType(self):
        return self._getString(27)

    def setVehicleType(self, value):
        self._setString(27, value)
        return

    def getVehicleLvl(self):
        return self._getString(28)

    def setVehicleLvl(self, value):
        self._setString(28, value)
        return

    def getIsElite(self):
        return self._getBool(29)

    def setIsElite(self, value):
        self._setBool(29, value)
        return

    def _initialize(self):
        super(LootVehicleCompensationRendererModel, self)._initialize()
        self._addStringProperty(b'vehicleName', b'')
        self._addStringProperty(b'vehicleType', b'')
        self._addStringProperty(b'vehicleLvl', b'')
        self._addBoolProperty(b'isElite', True)
        return
