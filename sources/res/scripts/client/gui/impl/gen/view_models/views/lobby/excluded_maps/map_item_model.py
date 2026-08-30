from frameworks.wulf import ViewModel

class MapItemModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(MapItemModel, self).__init__(properties=properties, commands=commands)
        return

    def getState(self):
        return self._getString(0)

    def setState(self, value):
        self._setString(0, value)
        return

    def getMapId(self):
        return self._getString(1)

    def setMapId(self, value):
        self._setString(1, value)
        return

    def getCooldownEndTime(self):
        return self._getNumber(2)

    def setCooldownEndTime(self, value):
        self._setNumber(2, value)
        return

    def _initialize(self):
        super(MapItemModel, self)._initialize()
        self._addStringProperty(b'state', b'')
        self._addStringProperty(b'mapId', b'')
        self._addNumberProperty(b'cooldownEndTime', 0)
        return
