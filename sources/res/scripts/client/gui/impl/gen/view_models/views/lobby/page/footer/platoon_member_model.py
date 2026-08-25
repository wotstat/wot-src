from frameworks.wulf import ViewModel

class PlatoonMemberModel(ViewModel):
    __slots__ = ()
    READY = b'ready'
    NOT_READY = b'notReady'
    IN_BATTLE = b'inBattle'
    SEARCHING = b'searching'
    EMPTY = b'empty'

    def __init__(self, properties=1, commands=0):
        super(PlatoonMemberModel, self).__init__(properties=properties, commands=commands)
        return

    def getState(self):
        return self._getString(0)

    def setState(self, value):
        self._setString(0, value)
        return

    def _initialize(self):
        super(PlatoonMemberModel, self)._initialize()
        self._addStringProperty(b'state', b'')
        return
