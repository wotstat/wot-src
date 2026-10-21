from portal.gui.battle_results import templates
from portal.gui.shared import event_dispatcher
from gui.battle_results.composer import IStatsComposer
from gui.battle_results.templates.regular import REGULAR_COMMON_STATS_BLOCK
from gui.battle_results.components import base

class PortalBattleStatsComposer(IStatsComposer):

    def __init__(self, _):
        super(PortalBattleStatsComposer, self).__init__()
        self._block = templates.PORTAL_TOTAL_RESULTS_BLOCK.clone()
        return

    def clear(self):
        self._block.clear()
        return

    def setResults(self, results, reusable):
        self._block.addNextComponent(base.DirectStatsItem(b'results', results))
        self._block.addNextComponent(base.DirectStatsItem(b'reusable', reusable))
        self._block.addNextComponent(REGULAR_COMMON_STATS_BLOCK.clone())
        self._block.addNextComponent(templates.PERSONAL_STATS_BLOCK.clone())
        self._block.addNextComponent(templates.TEAM_STATS_BLOCK.clone())
        self._block.setRecord(results, reusable)
        return

    def getVO(self):
        return self._block.getVO()

    def popAnimation(self):
        return

    @staticmethod
    def onShowResults(arenaUniqueID):
        return

    @staticmethod
    def onResultsPosted(arenaUniqueID):
        import BigWorld
        if PortalBattleStatsComposer.__canNavigate():
            event_dispatcher.showPortalBattleResultView(arenaUniqueID)
        else:
            BigWorld.callback(0.0, PortalBattleStatsComposer.__showErrorMessage)
        return

    @staticmethod
    def __canNavigate():
        from gui.prb_control.dispatcher import g_prbLoader
        prbDispatcher = g_prbLoader.getDispatcher()
        if prbDispatcher is not None and prbDispatcher.getFunctionalState().isNavigationDisabled():
            return False
        else:
            return True

    @staticmethod
    def __showErrorMessage():
        from gui import SystemMessages
        SystemMessages.pushI18nMessage(b'#system_messages:queue/isInQueue', type=SystemMessages.SM_TYPE.Error, priority=b'high')
        return
