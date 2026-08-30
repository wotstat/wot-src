from frameworks.wulf import Array, ViewModel

class SeniorityAwardsTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(SeniorityAwardsTooltipModel, self).__init__(properties=properties, commands=commands)
        return

    def getCategory(self):
        return self._getString(0)

    def setCategory(self, value):
        self._setString(0, value)
        return

    def getMaxCategory(self):
        return self._getString(1)

    def setMaxCategory(self, value):
        self._setString(1, value)
        return

    def getYears(self):
        return self._getNumber(2)

    def setYears(self, value):
        self._setNumber(2, value)
        return

    def getCategories(self):
        return self._getArray(3)

    def setCategories(self, value):
        self._setArray(3, value)
        return

    @staticmethod
    def getCategoriesType():
        return unicode

    def _initialize(self):
        super(SeniorityAwardsTooltipModel, self)._initialize()
        self._addStringProperty(b'category', b'')
        self._addStringProperty(b'maxCategory', b'')
        self._addNumberProperty(b'years', 0)
        self._addArrayProperty(b'categories', Array())
        return
