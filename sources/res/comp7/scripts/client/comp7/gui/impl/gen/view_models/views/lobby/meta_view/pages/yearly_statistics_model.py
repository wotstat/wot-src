from frameworks.wulf import Array, ViewModel
from comp7.gui.impl.gen.view_models.views.lobby.meta_view.pages.yearly_statistics_season_model import YearlyStatisticsSeasonModel

class YearlyStatisticsModel(ViewModel):
    __slots__ = (b'onGoToSeasonStatistics',)

    def __init__(self, properties=1, commands=1):
        super(YearlyStatisticsModel, self).__init__(properties=properties, commands=commands)
        return

    def getSeasonCards(self):
        return self._getArray(0)

    def setSeasonCards(self, value):
        self._setArray(0, value)
        return

    @staticmethod
    def getSeasonCardsType():
        return YearlyStatisticsSeasonModel

    def _initialize(self):
        super(YearlyStatisticsModel, self)._initialize()
        self._addArrayProperty(b'seasonCards', Array())
        self.onGoToSeasonStatistics = self._addCommand(b'onGoToSeasonStatistics')
        return
