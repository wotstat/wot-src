from frameworks.wulf import ViewModel

class FunBattleType(ViewModel):
    __slots__ = ()
    STANDARD = b'standard'
    RACE = b'race'

    def __init__(self, properties=0, commands=0):
        super(FunBattleType, self).__init__(properties=properties, commands=commands)
        return

    def _initialize(self):
        super(FunBattleType, self)._initialize()
        return
