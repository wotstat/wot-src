from frameworks.wulf import ViewModel

class NyDecorationStateTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(NyDecorationStateTooltipModel, self).__init__(properties=properties, commands=commands)
        return

    def getAtmosphereBonus(self):
        return self._getNumber(0)

    def setAtmosphereBonus(self, value):
        self._setNumber(0, value)
        return

    def getDescription(self):
        return self._getString(1)

    def setDescription(self, value):
        self._setString(1, value)
        return

    def _initialize(self):
        super(NyDecorationStateTooltipModel, self)._initialize()
        self._addNumberProperty(b'atmosphereBonus', 0)
        self._addStringProperty(b'description', b'')
        return
