from frameworks.wulf import ViewModel

class RewardViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=6, commands=0):
        super(RewardViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getId(self):
        return self._getString(0)

    def setId(self, value):
        self._setString(0, value)
        return

    def getIcon(self):
        return self._getString(1)

    def setIcon(self, value):
        self._setString(1, value)
        return

    def getName(self):
        return self._getString(2)

    def setName(self, value):
        self._setString(2, value)
        return

    def getCountInStock(self):
        return self._getNumber(3)

    def setCountInStock(self, value):
        self._setNumber(3, value)
        return

    def getMaxCount(self):
        return self._getNumber(4)

    def setMaxCount(self, value):
        self._setNumber(4, value)
        return

    def getTooltipId(self):
        return self._getString(5)

    def setTooltipId(self, value):
        self._setString(5, value)
        return

    def _initialize(self):
        super(RewardViewModel, self)._initialize()
        self._addStringProperty(b'id', b'')
        self._addStringProperty(b'icon', b'')
        self._addStringProperty(b'name', b'')
        self._addNumberProperty(b'countInStock', 0)
        self._addNumberProperty(b'maxCount', 0)
        self._addStringProperty(b'tooltipId', b'')
        return
