from frameworks.wulf import ViewModel

class LootboxEntryPoint(ViewModel):
    __slots__ = (b'onOpenStorage',)

    def __init__(self, properties=4, commands=1):
        super(LootboxEntryPoint, self).__init__(properties=properties, commands=commands)
        return

    def getBoxesCount(self):
        return self._getNumber(0)

    def setBoxesCount(self, value):
        self._setNumber(0, value)
        return

    def getHasNew(self):
        return self._getBool(1)

    def setHasNew(self, value):
        self._setBool(1, value)
        return

    def getIsLootBoxesEnabled(self):
        return self._getBool(2)

    def setIsLootBoxesEnabled(self, value):
        self._setBool(2, value)
        return

    def getHasInfinite(self):
        return self._getBool(3)

    def setHasInfinite(self, value):
        self._setBool(3, value)
        return

    def _initialize(self):
        super(LootboxEntryPoint, self)._initialize()
        self._addNumberProperty(b'boxesCount', 0)
        self._addBoolProperty(b'hasNew', False)
        self._addBoolProperty(b'isLootBoxesEnabled', True)
        self._addBoolProperty(b'hasInfinite', False)
        self.onOpenStorage = self._addCommand(b'onOpenStorage')
        return
