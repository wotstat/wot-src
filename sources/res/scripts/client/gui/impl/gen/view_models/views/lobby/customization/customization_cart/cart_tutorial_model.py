from frameworks.wulf import ViewModel

class CartTutorialModel(ViewModel):
    __slots__ = (b'onTutorialClose',)

    def __init__(self, properties=1, commands=1):
        super(CartTutorialModel, self).__init__(properties=properties, commands=commands)
        return

    def getShowProlongHint(self):
        return self._getBool(0)

    def setShowProlongHint(self, value):
        self._setBool(0, value)
        return

    def _initialize(self):
        super(CartTutorialModel, self)._initialize()
        self._addBoolProperty(b'showProlongHint', False)
        self.onTutorialClose = self._addCommand(b'onTutorialClose')
        return
