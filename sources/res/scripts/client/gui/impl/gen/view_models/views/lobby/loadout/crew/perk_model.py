from frameworks.wulf import ViewModel

class PerkModel(ViewModel):
    __slots__ = ()
    NEW_STATE = b'new'
    FREE_STATE = b'free'
    LEARNING_STATE = b'learning'
    LEARNED_STATE = b'learned'
    IRRELEVANT_STATE = b'irrelevant'

    def __init__(self, properties=2, commands=0):
        super(PerkModel, self).__init__(properties=properties, commands=commands)
        return

    def getName(self):
        return self._getString(0)

    def setName(self, value):
        self._setString(0, value)
        return

    def getState(self):
        return self._getString(1)

    def setState(self, value):
        self._setString(1, value)
        return

    def _initialize(self):
        super(PerkModel, self)._initialize()
        self._addStringProperty(b'name', b'')
        self._addStringProperty(b'state', b'')
        return
