from frameworks.wulf import ViewModel

class NewYearCollectionStyleTab(ViewModel):
    __slots__ = ()

    def __init__(self, properties=5, commands=0):
        super(NewYearCollectionStyleTab, self).__init__(properties=properties, commands=commands)
        return

    def getName(self):
        return self._getString(0)

    def setName(self, value):
        self._setString(0, value)
        return

    def getYear(self):
        return self._getString(1)

    def setYear(self, value):
        self._setString(1, value)
        return

    def getCount(self):
        return self._getNumber(2)

    def setCount(self, value):
        self._setNumber(2, value)
        return

    def getTotal(self):
        return self._getNumber(3)

    def setTotal(self, value):
        self._setNumber(3, value)
        return

    def getIsSelected(self):
        return self._getBool(4)

    def setIsSelected(self, value):
        self._setBool(4, value)
        return

    def _initialize(self):
        super(NewYearCollectionStyleTab, self)._initialize()
        self._addStringProperty(b'name', b'NewYear')
        self._addStringProperty(b'year', b'ny21')
        self._addNumberProperty(b'count', 0)
        self._addNumberProperty(b'total', 0)
        self._addBoolProperty(b'isSelected', False)
        return
