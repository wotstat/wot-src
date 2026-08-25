from frameworks.wulf import ViewModel

class TeamStatsColumnTypes(ViewModel):
    __slots__ = ()
    SQUAD = b'squad'
    PLAYER = b'player'
    DAMAGE = b'damage'
    FRAG = b'frag'
    XP = b'xp'
    VEHICLE = b'tank'

    def __init__(self, properties=0, commands=0):
        super(TeamStatsColumnTypes, self).__init__(properties=properties, commands=commands)
        return

    def _initialize(self):
        super(TeamStatsColumnTypes, self)._initialize()
        return
