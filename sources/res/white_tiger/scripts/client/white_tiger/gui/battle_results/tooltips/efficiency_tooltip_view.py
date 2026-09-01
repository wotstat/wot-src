from __future__ import absolute_import
from frameworks.wulf import ViewSettings
from gui.battle_results.presenters.wrappers import hasPresenter
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.battle_results.tooltips.efficiency_tooltip_model import EfficiencyTooltipModel
from gui.impl.pub import ViewImpl
from white_tiger.gui.shared.tooltips import TooltipType

class WTBattleResultsStatsTooltipView(ViewImpl):

    def __init__(self, arenaUniqueID, paramType):
        settings = ViewSettings(layoutID=R.views.lobby.tooltips.BattleResultsStatsTooltipView(), model=EfficiencyTooltipModel())
        super(WTBattleResultsStatsTooltipView, self).__init__(settings)
        self.__efficiencyParam = paramType
        self.__arenaUniqueID = arenaUniqueID
        return

    @property
    def arenaUniqueID(self):
        return self.__arenaUniqueID

    def _onLoading(self, *args, **kwargs):
        super(WTBattleResultsStatsTooltipView, self)._onLoading(*args, **kwargs)
        self.__packContent()
        return

    @hasPresenter()
    def __packContent(self, presenter=None):
        with self.getViewModel().transaction() as model:
            presenter.packTooltips(TooltipType.WHITE_TIGER_EFFICIENCY_PARAMETER, model, ctx={b'paramType': (self.__efficiencyParam), 
               b'isZeroValuesVisible': False, 
               b'isAdditionalValuesVisible': True})
        return
