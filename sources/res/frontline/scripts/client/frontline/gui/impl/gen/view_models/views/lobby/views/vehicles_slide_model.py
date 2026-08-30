from frameworks.wulf import ViewModel

class VehiclesSlideModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(VehiclesSlideModel, self).__init__(properties=properties, commands=commands)
        return

    def getFromLevel(self):
        return self._getNumber(0)

    def setFromLevel(self, value):
        self._setNumber(0, value)
        return

    def getToLevel(self):
        return self._getNumber(1)

    def setToLevel(self, value):
        self._setNumber(1, value)
        return

    def _initialize(self):
        super(VehiclesSlideModel, self)._initialize()
        self._addNumberProperty(b'fromLevel', 0)
        self._addNumberProperty(b'toLevel', 0)
        return
