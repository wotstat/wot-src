from gui.impl.gen.view_models.views.lobby.common.vehicle_model import VehicleModel

class TankChangeVehicleModel(VehicleModel):
    __slots__ = ()

    def __init__(self, properties=13, commands=0):
        super(TankChangeVehicleModel, self).__init__(properties=properties, commands=commands)
        return

    def getIsInInventory(self):
        return self._getBool(9)

    def setIsInInventory(self, value):
        self._setBool(9, value)
        return

    def getIsElite(self):
        return self._getBool(10)

    def setIsElite(self, value):
        self._setBool(10, value)
        return

    def getIsSelected(self):
        return self._getBool(11)

    def setIsSelected(self, value):
        self._setBool(11, value)
        return

    def getIsTrainingAvailable(self):
        return self._getBool(12)

    def setIsTrainingAvailable(self, value):
        self._setBool(12, value)
        return

    def _initialize(self):
        super(TankChangeVehicleModel, self)._initialize()
        self._addBoolProperty(b'isInInventory', False)
        self._addBoolProperty(b'isElite', False)
        self._addBoolProperty(b'isSelected', False)
        self._addBoolProperty(b'isTrainingAvailable', False)
        return
