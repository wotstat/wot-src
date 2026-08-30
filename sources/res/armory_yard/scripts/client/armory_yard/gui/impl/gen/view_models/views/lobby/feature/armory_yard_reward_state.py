from frameworks.wulf import ViewModel

class ArmoryYardRewardState(ViewModel):
    __slots__ = ()
    STAGE = b'stage'
    STYLE = b'style'
    SHOP = b'shop'

    def __init__(self, properties=0, commands=0):
        super(ArmoryYardRewardState, self).__init__(properties=properties, commands=commands)
        return

    def _initialize(self):
        super(ArmoryYardRewardState, self)._initialize()
        return
