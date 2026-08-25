from frameworks.wulf import ViewModel

class MapsBlacklistMapFilterModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(MapsBlacklistMapFilterModel, self).__init__(properties=properties, commands=commands)
        return

    def getFilterName(self):
        return self._getString(0)

    def setFilterName(self, value):
        self._setString(0, value)
        return

    def getFilterID(self):
        return self._getNumber(1)

    def setFilterID(self, value):
        self._setNumber(1, value)
        return

    def getSelected(self):
        return self._getBool(2)

    def setSelected(self, value):
        self._setBool(2, value)
        return

    def _initialize(self):
        super(MapsBlacklistMapFilterModel, self)._initialize()
        self._addStringProperty(b'filterName', b'')
        self._addNumberProperty(b'filterID', -1)
        self._addBoolProperty(b'selected', False)
        return
