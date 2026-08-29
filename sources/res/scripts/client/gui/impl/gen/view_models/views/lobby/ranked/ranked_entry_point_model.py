from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.ranked.ranked_season_model import RankedSeasonModel

class RankedEntryPointModel(ViewModel):
    __slots__ = (b'onClick',)
    STATE_RANKED_DISABLED = 0
    STATE_BEFORE_SEASON = 1
    STATE_ACTIVE_SEASON = 2
    STATE_WAIT_NEXT_SEASON_DATE = 3
    STATE_WAIT_NEXT_SEASON_WITHOUT_DATE = 4
    STATE_FROZEN = 5
    STATE_PROGRESSION_COMPLETE = 6
    STATE_IN_FINAL_DIVISION = 7
    STATE_ALMOST_NEXT_DIVISION = 8
    STATE_NEXT_DIVISION_FAR_AWAY = 9

    def __init__(self, properties=3, commands=1):
        super(RankedEntryPointModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def currentSeason(self):
        return self._getViewModel(0)

    @staticmethod
    def getCurrentSeasonType():
        return RankedSeasonModel

    @property
    def nextSeason(self):
        return self._getViewModel(1)

    @staticmethod
    def getNextSeasonType():
        return RankedSeasonModel

    def getState(self):
        return self._getNumber(2)

    def setState(self, value):
        self._setNumber(2, value)
        return

    def _initialize(self):
        super(RankedEntryPointModel, self)._initialize()
        self._addViewModelProperty(b'currentSeason', RankedSeasonModel())
        self._addViewModelProperty(b'nextSeason', RankedSeasonModel())
        self._addNumberProperty(b'state', 0)
        self.onClick = self._addCommand(b'onClick')
        return
