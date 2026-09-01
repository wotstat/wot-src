from frameworks.wulf import ViewModel

class ShellModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(ShellModel, self).__init__(properties=properties, commands=commands)
        return

    def getIntCD(self):
        return self._getNumber(0)

    def setIntCD(self, value):
        self._setNumber(0, value)
        return

    def getItemType(self):
        return self._getString(1)

    def setItemType(self, value):
        self._setString(1, value)
        return

    def getIsPremium(self):
        return self._getBool(2)

    def setIsPremium(self, value):
        self._setBool(2, value)
        return

    def _initialize(self):
        super(ShellModel, self)._initialize()
        self._addNumberProperty(b'intCD', 0)
        self._addStringProperty(b'itemType', b'')
        self._addBoolProperty(b'isPremium', False)
        return
