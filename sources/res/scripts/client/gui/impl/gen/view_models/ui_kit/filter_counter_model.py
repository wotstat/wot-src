from frameworks.wulf import ViewModel

class FilterCounterModel(ViewModel):
    __slots__ = (b'onResetBtnClick',)

    def __init__(self, properties=3, commands=1):
        super(FilterCounterModel, self).__init__(properties=properties, commands=commands)
        return

    def getCurrentCount(self):
        return self._getNumber(0)

    def setCurrentCount(self, value):
        self._setNumber(0, value)
        return

    def getTotalCount(self):
        return self._getNumber(1)

    def setTotalCount(self, value):
        self._setNumber(1, value)
        return

    def getIsFilterApplied(self):
        return self._getBool(2)

    def setIsFilterApplied(self, value):
        self._setBool(2, value)
        return

    def _initialize(self):
        super(FilterCounterModel, self)._initialize()
        self._addNumberProperty(b'currentCount', 0)
        self._addNumberProperty(b'totalCount', 0)
        self._addBoolProperty(b'isFilterApplied', False)
        self.onResetBtnClick = self._addCommand(b'onResetBtnClick')
        return
