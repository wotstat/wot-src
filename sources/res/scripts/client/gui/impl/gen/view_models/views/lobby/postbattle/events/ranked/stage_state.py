from frameworks.wulf import ViewModel

class StageState(ViewModel):
    __slots__ = ()
    STAGES_BONUS = b'stage4_bonus'
    STAGES = b'stage2_green'
    STAGE_BONUS = b'stage2_bonus'
    STAGE = b'stage_green'
    STAGE_LOST = b'stage_red'
    STAGE_IDLE = b'stage_grey'

    def __init__(self, properties=0, commands=0):
        super(StageState, self).__init__(properties=properties, commands=commands)
        return

    def _initialize(self):
        super(StageState, self)._initialize()
        return
