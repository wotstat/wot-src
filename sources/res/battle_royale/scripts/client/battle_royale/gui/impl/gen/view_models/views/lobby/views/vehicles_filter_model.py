from frameworks.wulf import Array, ViewModel

class VehiclesFilterModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(VehiclesFilterModel, self).__init__(properties=properties, commands=commands)
        return

    def getCarouselRowCount(self):
        return self._getNumber(0)

    def setCarouselRowCount(self, value):
        self._setNumber(0, value)
        return

    def getNationsOrder(self):
        return self._getArray(1)

    def setNationsOrder(self, value):
        self._setArray(1, value)
        return

    @staticmethod
    def getNationsOrderType():
        return unicode

    def _initialize(self):
        super(VehiclesFilterModel, self)._initialize()
        self._addNumberProperty(b'carouselRowCount', -1)
        self._addArrayProperty(b'nationsOrder', Array())
        return
