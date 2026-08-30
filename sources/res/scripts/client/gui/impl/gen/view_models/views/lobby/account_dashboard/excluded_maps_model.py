from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.views.lobby.account_dashboard.map_model import MapModel

class ExcludedMapsModel(ViewModel):
    __slots__ = (b'onClick',)

    def __init__(self, properties=2, commands=1):
        super(ExcludedMapsModel, self).__init__(properties=properties, commands=commands)
        return

    def getIsEnabled(self):
        return self._getBool(0)

    def setIsEnabled(self, value):
        self._setBool(0, value)
        return

    def getExcludedMaps(self):
        return self._getArray(1)

    def setExcludedMaps(self, value):
        self._setArray(1, value)
        return

    @staticmethod
    def getExcludedMapsType():
        return MapModel

    def _initialize(self):
        super(ExcludedMapsModel, self)._initialize()
        self._addBoolProperty(b'isEnabled', True)
        self._addArrayProperty(b'excludedMaps', Array())
        self.onClick = self._addCommand(b'onClick')
        return
