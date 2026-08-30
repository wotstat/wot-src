from frameworks.wulf import ViewModel

class FilterModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(FilterModel, self).__init__(properties=properties, commands=commands)
        return

    def getFilterName(self):
        return self._getString(0)

    def setFilterName(self, value):
        self._setString(0, value)
        return

    def getFilterId(self):
        return self._getNumber(1)

    def setFilterId(self, value):
        self._setNumber(1, value)
        return

    def getIsActive(self):
        return self._getBool(2)

    def setIsActive(self, value):
        self._setBool(2, value)
        return

    def _initialize(self):
        super(FilterModel, self)._initialize()
        self._addStringProperty(b'filterName', b'')
        self._addNumberProperty(b'filterId', -1)
        self._addBoolProperty(b'isActive', False)
        return
