from frameworks.wulf import Array
from frameworks.wulf import ViewModel

class SelectedFiltersModel(ViewModel):
    __slots__ = (b'onFilterChanged', b'onFilterReset')

    def __init__(self, properties=4, commands=2):
        super(SelectedFiltersModel, self).__init__(properties=properties, commands=commands)
        return

    def getSelectedFilterCount(self):
        return self._getNumber(0)

    def setSelectedFilterCount(self, value):
        self._setNumber(0, value)
        return

    def getTotalFilterCount(self):
        return self._getNumber(1)

    def setTotalFilterCount(self, value):
        self._setNumber(1, value)
        return

    def getFilterIsEnabled(self):
        return self._getBool(2)

    def setFilterIsEnabled(self, value):
        self._setBool(2, value)
        return

    def getFilters(self):
        return self._getArray(3)

    def setFilters(self, value):
        self._setArray(3, value)
        return

    def _initialize(self):
        super(SelectedFiltersModel, self)._initialize()
        self._addNumberProperty(b'selectedFilterCount', 0)
        self._addNumberProperty(b'totalFilterCount', 0)
        self._addBoolProperty(b'filterIsEnabled', False)
        self._addArrayProperty(b'filters', Array())
        self.onFilterChanged = self._addCommand(b'onFilterChanged')
        self.onFilterReset = self._addCommand(b'onFilterReset')
        return
