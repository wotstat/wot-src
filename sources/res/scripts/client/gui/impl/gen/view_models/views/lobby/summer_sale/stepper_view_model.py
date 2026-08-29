from frameworks.wulf import ViewModel

class StepperViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(StepperViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getMinimum(self):
        return self._getNumber(0)

    def setMinimum(self, value):
        self._setNumber(0, value)
        return

    def getMaximum(self):
        return self._getNumber(1)

    def setMaximum(self, value):
        self._setNumber(1, value)
        return

    def getStepSize(self):
        return self._getNumber(2)

    def setStepSize(self, value):
        self._setNumber(2, value)
        return

    def getValue(self):
        return self._getNumber(3)

    def setValue(self, value):
        self._setNumber(3, value)
        return

    def _initialize(self):
        super(StepperViewModel, self)._initialize()
        self._addNumberProperty(b'minimum', 1)
        self._addNumberProperty(b'maximum', 1)
        self._addNumberProperty(b'stepSize', 1)
        self._addNumberProperty(b'value', 1)
        return
