from gui.impl.gen.view_models.common.missions.bonuses.icon_bonus_model import IconBonusModel

class TankAcademyBonusModel(IconBonusModel):
    __slots__ = ()
    NAME_VEHICLE_REWARD = b'vehicle'
    NAME_TOKEN_VEHICLE_REWARD = b'tokenVehicle'

    def __init__(self, properties=12, commands=0):
        super(TankAcademyBonusModel, self).__init__(properties=properties, commands=commands)
        return

    def getIsEssential(self):
        return self._getBool(8)

    def setIsEssential(self, value):
        self._setBool(8, value)
        return

    def getTier(self):
        return self._getNumber(9)

    def setTier(self, value):
        self._setNumber(9, value)
        return

    def getIsPremium(self):
        return self._getBool(10)

    def setIsPremium(self, value):
        self._setBool(10, value)
        return

    def getType(self):
        return self._getString(11)

    def setType(self, value):
        self._setString(11, value)
        return

    def _initialize(self):
        super(TankAcademyBonusModel, self)._initialize()
        self._addBoolProperty(b'isEssential', False)
        self._addNumberProperty(b'tier', 0)
        self._addBoolProperty(b'isPremium', False)
        self._addStringProperty(b'type', b'')
        return
