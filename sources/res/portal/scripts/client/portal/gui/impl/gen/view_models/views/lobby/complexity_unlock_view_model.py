from frameworks.wulf import ViewModel

class ComplexityUnlockViewModel(ViewModel):
    __slots__ = (b'onApprove',)

    def __init__(self, properties=1, commands=1):
        super(ComplexityUnlockViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getComplexity(self):
        return self._getNumber(0)

    def setComplexity(self, value):
        self._setNumber(0, value)
        return

    def _initialize(self):
        super(ComplexityUnlockViewModel, self)._initialize()
        self._addNumberProperty(b'complexity', 0)
        self.onApprove = self._addCommand(b'onApprove')
        return
