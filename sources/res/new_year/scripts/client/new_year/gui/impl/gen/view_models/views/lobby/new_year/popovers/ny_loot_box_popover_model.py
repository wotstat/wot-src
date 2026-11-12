from frameworks.wulf import ViewModel

class NyLootBoxPopoverModel(ViewModel):
    __slots__ = (b'onEventBtnClick', b'onBuyBtnClick')

    def __init__(self, properties=1, commands=2):
        super(NyLootBoxPopoverModel, self).__init__(properties=properties, commands=commands)
        return

    def getIsBuyAvailable(self):
        return self._getBool(0)

    def setIsBuyAvailable(self, value):
        self._setBool(0, value)
        return

    def _initialize(self):
        super(NyLootBoxPopoverModel, self)._initialize()
        self._addBoolProperty(b'isBuyAvailable', True)
        self.onEventBtnClick = self._addCommand(b'onEventBtnClick')
        self.onBuyBtnClick = self._addCommand(b'onBuyBtnClick')
        return
