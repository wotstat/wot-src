from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.views.lobby.tank_setup.common.sub_filter_model import SubFilterModel

class FiltersModel(ViewModel):
    __slots__ = (b'onFilterChanged', b'onFilterReset')

    def __init__(self, properties=4, commands=2):
        super(FiltersModel, self).__init__(properties=properties, commands=commands)
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

    def getIsEnabled(self):
        return self._getBool(2)

    def setIsEnabled(self, value):
        self._setBool(2, value)
        return

    def getFilters(self):
        return self._getArray(3)

    def setFilters(self, value):
        self._setArray(3, value)
        return

    @staticmethod
    def getFiltersType():
        return SubFilterModel

    def _initialize(self):
        super(FiltersModel, self)._initialize()
        self._addNumberProperty(b'selectedFilterCount', 0)
        self._addNumberProperty(b'totalFilterCount', 0)
        self._addBoolProperty(b'isEnabled', False)
        self._addArrayProperty(b'filters', Array())
        self.onFilterChanged = self._addCommand(b'onFilterChanged')
        self.onFilterReset = self._addCommand(b'onFilterReset')
        return
