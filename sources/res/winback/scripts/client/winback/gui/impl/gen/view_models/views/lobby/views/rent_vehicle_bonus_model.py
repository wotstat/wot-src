from enum import Enum
from winback.gui.impl.gen.view_models.views.lobby.views.vehicle_bonus_model import VehicleBonusModel

class RentType(Enum):
    TIME = b'time'
    WINS = b'wins'
    BATTLES = b'battles'


class RentVehicleBonusModel(VehicleBonusModel):
    __slots__ = ()

    def __init__(self, properties=19, commands=0):
        super(RentVehicleBonusModel, self).__init__(properties=properties, commands=commands)
        return

    def getRentType(self):
        return RentType(self._getString(17))

    def setRentType(self, value):
        self._setString(17, value.value)
        return

    def getRentDuration(self):
        return self._getNumber(18)

    def setRentDuration(self, value):
        self._setNumber(18, value)
        return

    def _initialize(self):
        super(RentVehicleBonusModel, self)._initialize()
        self._addStringProperty(b'rentType')
        self._addNumberProperty(b'rentDuration', 0)
        return
