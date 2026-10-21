from gui.impl.gen.view_models.common.missions.bonuses.bonus_model import BonusModel

class SessionProgressRewardBonusModel(BonusModel):
    __slots__ = ()

    def __init__(self, properties=12, commands=0):
        super(SessionProgressRewardBonusModel, self).__init__(properties=properties, commands=commands)
        return

    def getVehicleName(self):
        return self._getString(7)

    def setVehicleName(self, value):
        self._setString(7, value)
        return

    def getVehicleType(self):
        return self._getString(8)

    def setVehicleType(self, value):
        self._setString(8, value)
        return

    def getVehicleLevel(self):
        return self._getNumber(9)

    def setVehicleLevel(self, value):
        self._setNumber(9, value)
        return

    def getIsElite(self):
        return self._getBool(10)

    def setIsElite(self, value):
        self._setBool(10, value)
        return

    def getCompensatedBonus(self):
        return self._getString(11)

    def setCompensatedBonus(self, value):
        self._setString(11, value)
        return

    def _initialize(self):
        super(SessionProgressRewardBonusModel, self)._initialize()
        self._addStringProperty(b'vehicleName', b'')
        self._addStringProperty(b'vehicleType', b'')
        self._addNumberProperty(b'vehicleLevel', 0)
        self._addBoolProperty(b'isElite', False)
        self._addStringProperty(b'compensatedBonus', b'')
        return
