from gui.impl.gen.view_models.views.lobby.common.vehicle_model import VehicleModel

class TankChangeVehicleModel(VehicleModel):
    __slots__ = ()

    def __init__(self, properties=15, commands=0):
        super(TankChangeVehicleModel, self).__init__(properties=properties, commands=commands)
        return

    def getIsInInventory(self):
        return self._getBool(10)

    def setIsInInventory(self, value):
        self._setBool(10, value)
        return

    def getIsElite(self):
        return self._getBool(11)

    def setIsElite(self, value):
        self._setBool(11, value)
        return

    def getIsSelected(self):
        return self._getBool(12)

    def setIsSelected(self, value):
        self._setBool(12, value)
        return

    def getIsTrainingAvailable(self):
        return self._getBool(13)

    def setIsTrainingAvailable(self, value):
        self._setBool(13, value)
        return

    def getIsWotPlusVehicle(self):
        return self._getBool(14)

    def setIsWotPlusVehicle(self, value):
        self._setBool(14, value)
        return

    def _initialize(self):
        super(TankChangeVehicleModel, self)._initialize()
        self._addBoolProperty(b'isInInventory', False)
        self._addBoolProperty(b'isElite', False)
        self._addBoolProperty(b'isSelected', False)
        self._addBoolProperty(b'isTrainingAvailable', False)
        self._addBoolProperty(b'isWotPlusVehicle', False)
        return
