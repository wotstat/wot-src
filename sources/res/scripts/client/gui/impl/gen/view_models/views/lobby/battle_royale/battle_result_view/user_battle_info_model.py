from gui.impl.gen.view_models.common.user_name_model import UserNameModel

class UserBattleInfoModel(UserNameModel):
    __slots__ = ()

    def __init__(self, properties=15, commands=0):
        super(UserBattleInfoModel, self).__init__(properties=properties, commands=commands)
        return

    def getVehicleName(self):
        return self._getString(10)

    def setVehicleName(self, value):
        self._setString(10, value)
        return

    def getVehicleType(self):
        return self._getString(11)

    def setVehicleType(self, value):
        self._setString(11, value)
        return

    def getVehicleLevel(self):
        return self._getNumber(12)

    def setVehicleLevel(self, value):
        self._setNumber(12, value)
        return

    def getDamage(self):
        return self._getNumber(13)

    def setDamage(self, value):
        self._setNumber(13, value)
        return

    def getKills(self):
        return self._getNumber(14)

    def setKills(self, value):
        self._setNumber(14, value)
        return

    def _initialize(self):
        super(UserBattleInfoModel, self)._initialize()
        self._addStringProperty(b'vehicleName', b'')
        self._addStringProperty(b'vehicleType', b'')
        self._addNumberProperty(b'vehicleLevel', 1)
        self._addNumberProperty(b'damage', 0)
        self._addNumberProperty(b'kills', 0)
        return
