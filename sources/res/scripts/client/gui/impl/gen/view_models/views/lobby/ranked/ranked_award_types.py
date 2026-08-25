from frameworks.wulf import ViewModel

class RankedAwardTypes(ViewModel):
    __slots__ = ()
    SMALL = b'small'
    MEDIUM = b'medium'
    BIG = b'big'
    LARGE = b'large'

    def __init__(self, properties=0, commands=0):
        super(RankedAwardTypes, self).__init__(properties=properties, commands=commands)
        return

    def _initialize(self):
        super(RankedAwardTypes, self)._initialize()
        return
