from frameworks.wulf import Array, ViewModel
from comp7_light.gui.impl.gen.view_models.views.lobby.season_model import SeasonModel

class EntryPointTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(EntryPointTooltipModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def season(self):
        return self._getViewModel(0)

    @staticmethod
    def getSeasonType():
        return SeasonModel

    def getTimeLeftUntilPrimeTime(self):
        return self._getNumber(1)

    def setTimeLeftUntilPrimeTime(self, value):
        self._setNumber(1, value)
        return

    def getVehicleLevels(self):
        return self._getArray(2)

    def setVehicleLevels(self, value):
        self._setArray(2, value)
        return

    @staticmethod
    def getVehicleLevelsType():
        return int

    def _initialize(self):
        super(EntryPointTooltipModel, self)._initialize()
        self._addViewModelProperty(b'season', SeasonModel())
        self._addNumberProperty(b'timeLeftUntilPrimeTime', 0)
        self._addArrayProperty(b'vehicleLevels', Array())
        return
