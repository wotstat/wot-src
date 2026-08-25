__all__ = (b'getGameplayConfig',)

def getGameplayConfig(manager):
    from gameplay.delegator import GameplayLogic
    from gameplay.machine import create
    from skeletons.gameplay import IGameplayLogic
    manager.addInstance(IGameplayLogic, GameplayLogic(create()), finalizer=b'stop')
    return
