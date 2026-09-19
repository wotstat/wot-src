from frameworks.wulf import ViewModel

class ShopStylePanelModel(ViewModel):
    __slots__ = (b'onClick',)

    def __init__(self, properties=3, commands=1):
        super(ShopStylePanelModel, self).__init__(properties=properties, commands=commands)
        return

    def getName(self):
        return self._getString(0)

    def setName(self, value):
        self._setString(0, value)
        return

    def getTimer(self):
        return self._getNumber(1)

    def setTimer(self, value):
        self._setNumber(1, value)
        return

    def getIsOwned(self):
        return self._getBool(2)

    def setIsOwned(self, value):
        self._setBool(2, value)
        return

    def _initialize(self):
        super(ShopStylePanelModel, self)._initialize()
        self._addStringProperty(b'name', b'')
        self._addNumberProperty(b'timer', 0)
        self._addBoolProperty(b'isOwned', False)
        self.onClick = self._addCommand(b'onClick')
        return
