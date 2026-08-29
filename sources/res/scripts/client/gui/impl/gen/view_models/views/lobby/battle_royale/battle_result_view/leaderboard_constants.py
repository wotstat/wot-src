from frameworks.wulf import ViewModel

class LeaderboardConstants(ViewModel):
    __slots__ = ()
    ROW_TYPE_BR_PLAYER = b'rowBrPlayer'
    ROW_TYPE_BR_ENEMY = b'rowBrEnemy'

    def __init__(self, properties=0, commands=0):
        super(LeaderboardConstants, self).__init__(properties=properties, commands=commands)
        return

    def _initialize(self):
        super(LeaderboardConstants, self)._initialize()
        return
