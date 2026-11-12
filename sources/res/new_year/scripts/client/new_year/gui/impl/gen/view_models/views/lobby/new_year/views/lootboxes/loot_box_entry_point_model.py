from frameworks.wulf import ViewModel

class LootBoxEntryPointModel(ViewModel):
    __slots__ = (b'onLootBoxEntryPointClick',)

    def __init__(self, properties=3, commands=1):
        super(LootBoxEntryPointModel, self).__init__(properties=properties, commands=commands)
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

    def _initialize(self):
        super(LootBoxEntryPointModel, self)._initialize()
        self._addNumberProperty(b'boxesCount', 0)
        self._addBoolProperty(b'hasNew', False)
        self._addBoolProperty(b'isLootBoxesEnabled', True)
        self.onLootBoxEntryPointClick = self._addCommand(b'onLootBoxEntryPointClick')
        return
