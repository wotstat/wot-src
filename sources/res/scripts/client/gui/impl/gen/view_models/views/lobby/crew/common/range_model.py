from frameworks.wulf import ViewModel

class RangeModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(RangeModel, self).__init__(properties=properties, commands=commands)
        return

    def getFrom(self):
        return self._getNumber(0)

    def setFrom(self, value):
        self._setNumber(0, value)
        return

    def getTo(self):
        return self._getNumber(1)

    def setTo(self, value):
        self._setNumber(1, value)
        return

    def _initialize(self):
        super(RangeModel, self)._initialize()
        self._addNumberProperty(b'from', 0)
        self._addNumberProperty(b'to', 0)
        return
