from regular import RegularAchievement
from mixins import HasVehiclesList, Deprecated

class HistoricalAchievement(Deprecated, HasVehiclesList, RegularAchievement):
    _LIST_NAME = b'vehiclesTakePart'

    def _getVehiclesDescrsList(self):
        return []
