from frameworks.wulf import ViewModel

class NewYearCollectionAdditional(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(NewYearCollectionAdditional, self).__init__(properties=properties, commands=commands)
        return

    def getCount(self):
        return self._getNumber(0)

    def setCount(self, value):
        self._setNumber(0, value)
        return

    def getName(self):
        return self._getString(1)

    def setName(self, value):
        self._setString(1, value)
        return

    def getItemType(self):
        return self._getString(2)

    def setItemType(self, value):
        self._setString(2, value)
        return

    def getTooltipId(self):
        return self._getNumber(3)

    def setTooltipId(self, value):
        self._setNumber(3, value)
        return

    def _initialize(self):
        super(NewYearCollectionAdditional, self)._initialize()
        self._addNumberProperty(b'count', 1)
        self._addStringProperty(b'name', b'')
        self._addStringProperty(b'itemType', b'')
        self._addNumberProperty(b'tooltipId', 0)
        return
