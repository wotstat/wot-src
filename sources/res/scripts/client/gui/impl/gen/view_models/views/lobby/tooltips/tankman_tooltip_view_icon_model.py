from frameworks.wulf import ViewModel

class TankmanTooltipViewIconModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=1, commands=0):
        super(TankmanTooltipViewIconModel, self).__init__(properties=properties, commands=commands)
        return

    def getIcon(self):
        return self._getString(0)

    def setIcon(self, value):
        self._setString(0, value)
        return

    def _initialize(self):
        super(TankmanTooltipViewIconModel, self)._initialize()
        self._addStringProperty(b'icon', b'')
        return
