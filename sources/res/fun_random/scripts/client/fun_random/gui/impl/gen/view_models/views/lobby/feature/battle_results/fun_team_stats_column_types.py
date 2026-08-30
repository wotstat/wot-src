from frameworks.wulf import ViewModel

class FunTeamStatsColumnTypes(ViewModel):
    __slots__ = ()
    FINISH_TIME = b'finishTime'
    FINISH_POSITION = b'finishPosition'
    CHECKPOINTS = b'checkpoints'

    def __init__(self, properties=0, commands=0):
        super(FunTeamStatsColumnTypes, self).__init__(properties=properties, commands=commands)
        return

    def _initialize(self):
        super(FunTeamStatsColumnTypes, self)._initialize()
        return
