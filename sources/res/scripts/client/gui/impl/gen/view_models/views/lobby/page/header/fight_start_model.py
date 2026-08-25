from frameworks.wulf import ViewModel

class FightStartModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=1, commands=0):
        super(FightStartModel, self).__init__(properties=properties, commands=commands)
        return

    def getTooltip(self):
        return self._getString(0)

    def setTooltip(self, value):
        self._setString(0, value)
        return

    def _initialize(self):
        super(FightStartModel, self)._initialize()
        self._addStringProperty(b'tooltip', b'')
        return
