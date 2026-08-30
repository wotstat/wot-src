from frameworks.wulf import ViewModel

class MenuItemModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(MenuItemModel, self).__init__(properties=properties, commands=commands)
        return

    def getTabName(self):
        return self._getString(0)

    def setTabName(self, value):
        self._setString(0, value)
        return

    def getCounter(self):
        return self._getNumber(1)

    def setCounter(self, value):
        self._setNumber(1, value)
        return

    def _initialize(self):
        super(MenuItemModel, self)._initialize()
        self._addStringProperty(b'tabName', b'')
        self._addNumberProperty(b'counter', 0)
        return
