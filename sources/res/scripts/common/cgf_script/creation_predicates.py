import BigWorld

def inBattleCreationPredicate(_=None):
    player = BigWorld.player()
    return hasattr(player, b'isOnArena')
