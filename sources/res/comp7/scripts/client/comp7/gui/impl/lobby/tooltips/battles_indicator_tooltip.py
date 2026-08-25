from comp7.gui.impl.gen.view_models.views.lobby.tooltips.battles_indicator_tooltip_model import BattlesIndicatorTooltipModel
from frameworks.wulf import ViewSettings
from gui.impl.gen import R
from gui.impl.pub import ViewImpl

class BattlesIndicatorTooltip(ViewImpl):
    __slots__ = (b'__params',)

    def __init__(self, layoutID=R.views.comp7.mono.lobby.tooltips.battles_indicator_tooltip(), params=None):
        settings = ViewSettings(layoutID)
        settings.model = BattlesIndicatorTooltipModel()
        super(BattlesIndicatorTooltip, self).__init__(settings)
        self.__params = params
        return

    @property
    def viewModel(self):
        return super(BattlesIndicatorTooltip, self).getViewModel()

    def _onLoading(self):
        super(BattlesIndicatorTooltip, self)._onLoading()
        with self.viewModel.transaction() as vm:
            vm.setStatisticsMode(self.__params[b'statisticsMode'])
            vm.setSoloBattlesCount(self.__params[b'soloBattlesCount'])
            vm.setSuperPlatoonBattlesCount(self.__params[b'superPlatoonBattlesCount'])
        return
