from gui.impl.gen.view_models.views.lobby.common.vehicle_model import VehicleModel

class PrebattleVehicleModel(VehicleModel):
    __slots__ = ()

    def __init__(self, properties=12, commands=0):
        super(PrebattleVehicleModel, self).__init__(properties=properties, commands=commands)
        return

    def getIsFavorite(self):
        return self._getBool(9)

    def setIsFavorite(self, value):
        self._setBool(9, value)
        return

    def getIsSelected(self):
        return self._getBool(10)

    def setIsSelected(self, value):
        self._setBool(10, value)
        return

    def getIsVisible(self):
        return self._getBool(11)

    def setIsVisible(self, value):
        self._setBool(11, value)
        return

    def _initialize(self):
        super(PrebattleVehicleModel, self)._initialize()
        self._addBoolProperty(b'isFavorite', False)
        self._addBoolProperty(b'isSelected', False)
        self._addBoolProperty(b'isVisible', True)
        return
