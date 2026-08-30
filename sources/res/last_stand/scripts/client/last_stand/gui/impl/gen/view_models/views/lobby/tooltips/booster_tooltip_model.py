from frameworks.wulf import ViewModel

class BoosterTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(BoosterTooltipModel, self).__init__(properties=properties, commands=commands)
        return

    def getBooster(self):
        return self._getString(0)

    def setBooster(self, value):
        self._setString(0, value)
        return

    def getBody(self):
        return self._getString(1)

    def setBody(self, value):
        self._setString(1, value)
        return

    def getActivated(self):
        return self._getBool(2)

    def setActivated(self, value):
        self._setBool(2, value)
        return

    def _initialize(self):
        super(BoosterTooltipModel, self)._initialize()
        self._addStringProperty(b'booster', b'')
        self._addStringProperty(b'body', b'')
        self._addBoolProperty(b'activated', False)
        return
