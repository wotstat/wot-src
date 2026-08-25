import typing
from soft_exception import SoftException
from gui.battle_results.pbs_helpers.common import pushNoBattleResultsDataMessage
from gui.battle_results.stats_ctrl import IBattleResultStatsCtrl, BattleResults
from gui.shared.event_dispatcher import showFrontlinePostBattleResultsWindow
if typing.TYPE_CHECKING:
    from gui.battle_results.reusable import _ReusableInfo

class FrontlineBattleResultStatsCtrl(IBattleResultStatsCtrl):

    def __init__(self, _):
        self._battleResults = None
        return

    @property
    def ctrlImplType(self):
        return self.CTRL_IMPL_TYPE_GAMEFACE

    def clear(self):
        self._battleResults = None
        return

    def getVO(self):
        raise SoftException(b'Unsupported method')
        return

    def setResults(self, results, reusable):
        self._battleResults = BattleResults(results, reusable)
        return

    def getResults(self):
        return self._battleResults

    def onResultsPosted(self, arenaUniqueID):
        if self._battleResults:
            showFrontlinePostBattleResultsWindow(arenaUniqueID)
            return
        pushNoBattleResultsDataMessage()
        return

    @staticmethod
    def onShowResults(arenaUniqueID):
        return
