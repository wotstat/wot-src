from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.views.battle.prebattle_highlights.prebattle_highlights_marker_model import PrebattleHighlightsMarkerModel
from gui.impl.gen.view_models.views.battle.prebattle_highlights.prebattle_highlights_player_stats_model import PrebattleHighlightsPlayerStatsModel

class PrebattleHighlightsViewModel(ViewModel):
    __slots__ = ()
    WINTER_MAP_TYPE = 0
    SUMMER_MAP_TYPE = 1
    DESERT_MAP_TYPE = 3
    PBH_INTRO = b'intro'
    PBH_STAGE = b'stage'
    PBH_OUTRO = b'outro'

    def __init__(self, properties=5, commands=0):
        super(PrebattleHighlightsViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getCurrentState(self):
        return self._getString(0)

    def setCurrentState(self, value):
        self._setString(0, value)
        return

    def getMapType(self):
        return self._getNumber(1)

    def setMapType(self, value):
        self._setNumber(1, value)
        return

    def getHistoricalCompliance(self):
        return self._getBool(2)

    def setHistoricalCompliance(self, value):
        self._setBool(2, value)
        return

    def getMarkers(self):
        return self._getArray(3)

    def setMarkers(self, value):
        self._setArray(3, value)
        return

    @staticmethod
    def getMarkersType():
        return PrebattleHighlightsMarkerModel

    def getPlayersStats(self):
        return self._getArray(4)

    def setPlayersStats(self, value):
        self._setArray(4, value)
        return

    @staticmethod
    def getPlayersStatsType():
        return PrebattleHighlightsPlayerStatsModel

    def _initialize(self):
        super(PrebattleHighlightsViewModel, self)._initialize()
        self._addStringProperty(b'currentState', b'intro')
        self._addNumberProperty(b'mapType', 0)
        self._addBoolProperty(b'historicalCompliance', False)
        self._addArrayProperty(b'markers', Array())
        self._addArrayProperty(b'playersStats', Array())
        return
