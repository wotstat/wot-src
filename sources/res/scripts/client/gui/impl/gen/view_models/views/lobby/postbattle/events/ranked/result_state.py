from frameworks.wulf import ViewModel

class ResultState(ViewModel):
    __slots__ = ()
    STAGE = b'stage'
    RANK = b'rank'
    RANK_LOST = b'rank_lost'
    DIVISION = b'division'
    LEAGUE = b'league'

    def __init__(self, properties=0, commands=0):
        super(ResultState, self).__init__(properties=properties, commands=commands)
        return

    def _initialize(self):
        super(ResultState, self)._initialize()
        return
