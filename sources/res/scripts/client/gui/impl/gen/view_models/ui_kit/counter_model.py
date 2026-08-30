from frameworks.wulf import ViewModel

class CounterModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=1, commands=0):
        super(CounterModel, self).__init__(properties=properties, commands=commands)
        return

    def getValue(self):
        return self._getNumber(0)

    def setValue(self, value):
        self._setNumber(0, value)
        return

    def _initialize(self):
        super(CounterModel, self)._initialize()
        self._addNumberProperty(b'value', -1)
        return
