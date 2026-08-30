from frameworks.wulf import ViewModel

class StatsBaseItem(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(StatsBaseItem, self).__init__(properties=properties, commands=commands)
        return

    def getId(self):
        return self._getString(0)

    def setId(self, value):
        self._setString(0, value)
        return

    def getBlockIdx(self):
        return self._getNumber(1)

    def setBlockIdx(self, value):
        self._setNumber(1, value)
        return

    def getItemType(self):
        return self._getString(2)

    def setItemType(self, value):
        self._setString(2, value)
        return

    def getHasTooltip(self):
        return self._getBool(3)

    def setHasTooltip(self, value):
        self._setBool(3, value)
        return

    def _initialize(self):
        super(StatsBaseItem, self)._initialize()
        self._addStringProperty(b'id', b'')
        self._addNumberProperty(b'blockIdx', 0)
        self._addStringProperty(b'itemType', b'')
        self._addBoolProperty(b'hasTooltip', False)
        return
