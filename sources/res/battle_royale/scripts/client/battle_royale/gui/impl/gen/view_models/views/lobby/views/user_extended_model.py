from battle_royale.gui.impl.gen.view_models.views.lobby.views.user_model import UserModel

class UserExtendedModel(UserModel):
    __slots__ = ()

    def __init__(self, properties=5, commands=0):
        super(UserExtendedModel, self).__init__(properties=properties, commands=commands)
        return

    def getVehicleType(self):
        return self._getString(3)

    def setVehicleType(self, value):
        self._setString(3, value)
        return

    def getVehicleName(self):
        return self._getString(4)

    def setVehicleName(self, value):
        self._setString(4, value)
        return

    def _initialize(self):
        super(UserExtendedModel, self)._initialize()
        self._addStringProperty(b'vehicleType', b'')
        self._addStringProperty(b'vehicleName', b'')
        return
