from frameworks.wulf import Array
from frameworks.wulf import ViewModel

class WtRunPortalModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(WtRunPortalModel, self).__init__(properties=properties, commands=commands)
        return

    def getAttemptPrice(self):
        return self._getNumber(0)

    def setAttemptPrice(self, value):
        self._setNumber(0, value)
        return

    def getOpenLootBoxesCount(self):
        return self._getArray(1)

    def setOpenLootBoxesCount(self, value):
        self._setArray(1, value)
        return

    @staticmethod
    def getOpenLootBoxesCountType():
        return int

    def getLootBoxesCount(self):
        return self._getNumber(2)

    def setLootBoxesCount(self, value):
        self._setNumber(2, value)
        return

    def _initialize(self):
        super(WtRunPortalModel, self)._initialize()
        self._addNumberProperty(b'attemptPrice', 0)
        self._addArrayProperty(b'openLootBoxesCount', Array())
        self._addNumberProperty(b'lootBoxesCount', 0)
        return
