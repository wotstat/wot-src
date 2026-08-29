from collections import namedtuple
BattlePlayerData = namedtuple(b'_BattlePlayerData', (b'name', b'clanAbbrev', b'spaID', b'arenaUniqueID'))

class ArenaData(object):
    __slots__ = (b'arenaUniqueID', b'isLost', b'players')

    def __init__(self, arenaUniqueID, isLost, players):
        self.arenaUniqueID = arenaUniqueID
        self.isLost = isLost
        self.players = players
        return

    def __repr__(self):
        return (b'{}({},{},{})').format(self.__class__.__name__, self.arenaUniqueID, self.isLost, self.players)
