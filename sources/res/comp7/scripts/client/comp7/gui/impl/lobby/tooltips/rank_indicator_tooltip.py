from comp7.gui.impl.gen.view_models.views.lobby.tooltips.rank_indicator_tooltip_model import RankIndicatorTooltipModel
from frameworks.wulf import ViewSettings
from gui.impl.gen import R
from gui.impl.pub import ViewImpl

class RankIndicatorTooltip(ViewImpl):
    __slots__ = (b'__params',)

    def __init__(self, layoutID=R.views.comp7.mono.lobby.tooltips.rank_indicator_tooltip(), params=None):
        settings = ViewSettings(layoutID)
        settings.model = RankIndicatorTooltipModel()
        super(RankIndicatorTooltip, self).__init__(settings)
        self.__params = params
        return

    @property
    def viewModel(self):
        return super(RankIndicatorTooltip, self).getViewModel()

    def _onLoading(self):
        super(RankIndicatorTooltip, self)._onLoading()
        with self.viewModel.transaction() as vm:
            vm.setStatisticsMode(self.__params[b'statisticsMode'])
            vm.setRank(self.__params[b'rank'])
            vm.setSeasonName(self.__params[b'seasonName'])
            vm.setMaxAchievedRatingPoints(self.__params[b'maxAchievedRatingPoints'])
            division = self.__params[b'division']
            ratingPoints = self.__params[b'ratingPoints']
            diff = self.__params[b'diff']
            dayOfMaxRatingIndex = self.__params[b'dayOfMaxRatingIndex']
            if division:
                vm.setDivision(division)
            if ratingPoints:
                vm.setRatingPoints(ratingPoints)
            if diff:
                vm.setDiff(diff)
            if dayOfMaxRatingIndex:
                vm.setDayOfMaxRatingIndex(dayOfMaxRatingIndex)
        return
