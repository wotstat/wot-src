from gui.battle_control.battle_session import BattleSessionProvider
from gui.battle_control.controllers import BattleSessionSetup
from skeletons.gui.battle_session import IBattleSessionProvider
__all__ = (b'BattleSessionSetup', b'getBattleSessionConfig')

def getBattleSessionConfig(manager):
    manager.addInstance(IBattleSessionProvider, BattleSessionProvider(), finalizer=b'stop')
    return
