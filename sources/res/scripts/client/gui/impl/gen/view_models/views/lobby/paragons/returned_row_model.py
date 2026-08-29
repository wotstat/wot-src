from frameworks.wulf import ViewModel

class ReturnedRowModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=5, commands=0):
        super(ReturnedRowModel, self).__init__(properties=properties, commands=commands)
        return

    def getName(self):
        return self._getString(0)

    def setName(self, value):
        self._setString(0, value)
        return

    def getCount(self):
        return self._getNumber(1)

    def setCount(self, value):
        self._setNumber(1, value)
        return

    def getIcon(self):
        return self._getString(2)

    def setIcon(self, value):
        self._setString(2, value)
        return

    def getOverlayIcon(self):
        return self._getString(3)

    def setOverlayIcon(self, value):
        self._setString(3, value)
        return

    def getIntCD(self):
        return self._getNumber(4)

    def setIntCD(self, value):
        self._setNumber(4, value)
        return

    def _initialize(self):
        super(ReturnedRowModel, self)._initialize()
        self._addStringProperty(b'name', b'')
        self._addNumberProperty(b'count', 0)
        self._addStringProperty(b'icon', b'')
        self._addStringProperty(b'overlayIcon', b'')
        self._addNumberProperty(b'intCD', 0)
        return
