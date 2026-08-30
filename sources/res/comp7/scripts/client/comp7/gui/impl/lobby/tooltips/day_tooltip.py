from comp7.gui.impl.gen.view_models.views.lobby.tooltips.day_tooltip_model import DayTooltipModel
from frameworks.wulf import ViewSettings
from gui.impl.gen import R
from gui.impl.pub import ViewImpl

class DayTooltip(ViewImpl):
    __slots__ = (b'__params',)

    def __init__(self, layoutID=R.views.comp7.mono.lobby.tooltips.day_tooltip(), params=None):
        settings = ViewSettings(layoutID)
        settings.model = DayTooltipModel()
        super(DayTooltip, self).__init__(settings)
        self.__params = params
        return

    @property
    def viewModel(self):
        return super(DayTooltip, self).getViewModel()

    def _onLoading(self):
        super(DayTooltip, self)._onLoading()
        with self.viewModel.transaction() as vm:
            vm.setIndex(self.__params[b'index'])
            vm.setIsQualification(self.__params[b'isQualification'])
            vm.setSeasonName(self.__params[b'seasonName'])
            vm.setDiff(self.__params[b'diff'])
            vm.setHasBattles(self.__params[b'hasBattles'])
            vm.setRatingPoints(self.__params[b'ratingPoints'])
            vm.setRankInactivityPenalty(self.__params[b'rankInactivityPenalty'])
            vm.setCurrentDayIndex(self.__params[b'currentDayIndex'])
            rank = self.__params[b'rank']
            if rank:
                vm.setRank(rank)
            division = self.__params[b'division']
            if division:
                vm.setDivision(division)
        return
