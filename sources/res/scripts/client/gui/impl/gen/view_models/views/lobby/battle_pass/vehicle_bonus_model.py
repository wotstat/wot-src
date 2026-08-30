from gui.impl.gen.view_models.views.lobby.battle_pass.reward_item_model import RewardItemModel

class VehicleBonusModel(RewardItemModel):
    __slots__ = ()

    def __init__(self, properties=19, commands=0):
        super(VehicleBonusModel, self).__init__(properties=properties, commands=commands)
        return

    def getIsElite(self):
        return self._getBool(15)

    def setIsElite(self, value):
        self._setBool(15, value)
        return

    def getVehicleName(self):
        return self._getString(16)

    def setVehicleName(self, value):
        self._setString(16, value)
        return

    def getVehicleType(self):
        return self._getString(17)

    def setVehicleType(self, value):
        self._setString(17, value)
        return

    def getVehicleLvl(self):
        return self._getNumber(18)

    def setVehicleLvl(self, value):
        self._setNumber(18, value)
        return

    def _initialize(self):
        super(VehicleBonusModel, self)._initialize()
        self._addBoolProperty(b'isElite', True)
        self._addStringProperty(b'vehicleName', b'')
        self._addStringProperty(b'vehicleType', b'')
        self._addNumberProperty(b'vehicleLvl', 0)
        return
