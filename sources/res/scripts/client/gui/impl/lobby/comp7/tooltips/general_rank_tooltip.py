from frameworks.wulf import ViewSettings
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.comp7.tooltips.general_rank_tooltip_model import GeneralRankTooltipModel
from gui.impl.pub import ViewImpl

class GeneralRankTooltip(ViewImpl):
    __slots__ = (b'__params',)

    def __init__(self, layoutID=R.views.lobby.comp7.tooltips.GeneralRankTooltip(), params=None):
        settings = ViewSettings(layoutID)
        settings.model = GeneralRankTooltipModel()
        super(GeneralRankTooltip, self).__init__(settings)
        self.__params = params
        return

    @property
    def viewModel(self):
        return super(GeneralRankTooltip, self).getViewModel()

    def _onLoading(self):
        super(GeneralRankTooltip, self)._onLoading()
        with self.viewModel.transaction() as vm:
            vm.setRank(self.__params[b'rank'])
            vm.setDivisions(self.__params[b'divisions'])
            vm.setFrom(self.__params[b'from'])
            vm.setTo(self.__params[b'to'])
        return
