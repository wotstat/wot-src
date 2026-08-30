from frameworks.wulf import ViewModel

class FunRandomLoadoutConstants(ViewModel):
    __slots__ = ()
    FUN_RANDOM_CUSTOM_SHELLS = b'funRandomCustomShells'
    FUN_RANDOM_CUSTOM_ABILITIES = b'funRandomCustomAbilities'
    BATTLE_ABILITIES_GROUP = 3

    def __init__(self, properties=0, commands=0):
        super(FunRandomLoadoutConstants, self).__init__(properties=properties, commands=commands)
        return

    def _initialize(self):
        super(FunRandomLoadoutConstants, self)._initialize()
        return
