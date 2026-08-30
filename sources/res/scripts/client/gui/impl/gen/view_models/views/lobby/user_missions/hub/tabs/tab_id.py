from frameworks.wulf import ViewModel

class TabId(ViewModel):
    __slots__ = ()
    BASIC = b'basic'
    COMMON = b'common'
    CHALLENGES = b'challenges'

    def __init__(self, properties=0, commands=0):
        super(TabId, self).__init__(properties=properties, commands=commands)
        return

    def _initialize(self):
        super(TabId, self)._initialize()
        return
