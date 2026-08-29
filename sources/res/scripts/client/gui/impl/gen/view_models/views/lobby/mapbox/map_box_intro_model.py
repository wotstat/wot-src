from frameworks.wulf import ViewModel

class MapBoxIntroModel(ViewModel):
    __slots__ = (b'onClose',)

    def __init__(self, properties=2, commands=1):
        super(MapBoxIntroModel, self).__init__(properties=properties, commands=commands)
        return

    def getDate(self):
        return self._getNumber(0)

    def setDate(self, value):
        self._setNumber(0, value)
        return

    def getIsActive(self):
        return self._getBool(1)

    def setIsActive(self, value):
        self._setBool(1, value)
        return

    def _initialize(self):
        super(MapBoxIntroModel, self)._initialize()
        self._addNumberProperty(b'date', 0)
        self._addBoolProperty(b'isActive', False)
        self.onClose = self._addCommand(b'onClose')
        return
