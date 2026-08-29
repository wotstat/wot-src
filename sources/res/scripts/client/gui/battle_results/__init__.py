from gui.battle_results.service import BattleResultsService
from gui.battle_results.context import RequestResultsContext
from gui.battle_results.context import RequestEmblemContext
from gui.battle_results.settings import EMBLEM_TYPE
from skeletons.gui.battle_results import IBattleResultsService
__all__ = (b'getBattleResultsServiceConfig', b'RequestResultsContext', b'RequestEmblemContext', b'EMBLEM_TYPE')

def getBattleResultsServiceConfig(manager):
    instance = BattleResultsService()
    instance.init()
    manager.addInstance(IBattleResultsService, instance, finalizer=b'fini')
    return
