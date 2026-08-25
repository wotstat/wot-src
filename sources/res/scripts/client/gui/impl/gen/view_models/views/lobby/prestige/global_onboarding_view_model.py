from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.views.lobby.prestige.prestige_vehicle_model import PrestigeVehicleModel

class GlobalOnboardingViewModel(ViewModel):
    __slots__ = (b'onClose', b'onGoToVehicleStatistic')

    def __init__(self, properties=2, commands=2):
        super(GlobalOnboardingViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getEliteVehicleAmount(self):
        return self._getNumber(0)

    def setEliteVehicleAmount(self, value):
        self._setNumber(0, value)
        return

    def getVehicles(self):
        return self._getArray(1)

    def setVehicles(self, value):
        self._setArray(1, value)
        return

    @staticmethod
    def getVehiclesType():
        return PrestigeVehicleModel

    def _initialize(self):
        super(GlobalOnboardingViewModel, self)._initialize()
        self._addNumberProperty(b'eliteVehicleAmount', 0)
        self._addArrayProperty(b'vehicles', Array())
        self.onClose = self._addCommand(b'onClose')
        self.onGoToVehicleStatistic = self._addCommand(b'onGoToVehicleStatistic')
        return
