from frameworks.wulf import ViewModel

class LeaderboardConstants(ViewModel):
    __slots__ = ()
    LIST_TYPE_BR_SOLO = b'listBrSolo'
    LIST_TYPE_BR_PLATOON = b'listBrPlatoon'
    ROW_TYPE_BR_PLAYER = b'rowBrPlayer'
    ROW_TYPE_BR_PLATOON = b'rowBrPlatoon'
    ROW_TYPE_BR_ENEMY = b'rowBrEnemy'

    def __init__(self, properties=0, commands=0):
        super(LeaderboardConstants, self).__init__(properties=properties, commands=commands)
        return

    def _initialize(self):
        super(LeaderboardConstants, self)._initialize()
        return
