from frameworks.wulf import ViewModel

class ExcludedMapsTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(ExcludedMapsTooltipModel, self).__init__(properties=properties, commands=commands)
        return

    def getMapCount(self):
        return self._getNumber(0)

    def setMapCount(self, value):
        self._setNumber(0, value)
        return

    def getMaxCooldownTimeStr(self):
        return self._getString(1)

    def setMaxCooldownTimeStr(self, value):
        self._setString(1, value)
        return

    def _initialize(self):
        super(ExcludedMapsTooltipModel, self)._initialize()
        self._addNumberProperty(b'mapCount', 0)
        self._addStringProperty(b'maxCooldownTimeStr', b'')
        return
