from gui.impl.gen.view_models.common.missions.bonuses.icon_bonus_model import IconBonusModel

class JmBonusModel(IconBonusModel):
    __slots__ = ()

    def __init__(self, properties=14, commands=0):
        super(JmBonusModel, self).__init__(properties=properties, commands=commands)
        return

    def getIsElite(self):
        return self._getBool(9)

    def setIsElite(self, value):
        self._setBool(9, value)
        return

    def getVehicleShortName(self):
        return self._getString(10)

    def setVehicleShortName(self, value):
        self._setString(10, value)
        return

    def getVehicleLvl(self):
        return self._getNumber(11)

    def setVehicleLvl(self, value):
        self._setNumber(11, value)
        return

    def getVehicleType(self):
        return self._getString(12)

    def setVehicleType(self, value):
        self._setString(12, value)
        return

    def getIsPremium(self):
        return self._getBool(13)

    def setIsPremium(self, value):
        self._setBool(13, value)
        return

    def _initialize(self):
        super(JmBonusModel, self)._initialize()
        self._addBoolProperty(b'isElite', True)
        self._addStringProperty(b'vehicleShortName', b'')
        self._addNumberProperty(b'vehicleLvl', 0)
        self._addStringProperty(b'vehicleType', b'')
        self._addBoolProperty(b'isPremium', False)
        return
