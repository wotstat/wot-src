from frameworks.wulf import ViewModel

class AssemblingVideoViewModel(ViewModel):
    __slots__ = (b'startAssembling',)

    def __init__(self, properties=2, commands=1):
        super(AssemblingVideoViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getOperationID(self):
        return self._getNumber(0)

    def setOperationID(self, value):
        self._setNumber(0, value)
        return

    def getStageNumber(self):
        return self._getNumber(1)

    def setStageNumber(self, value):
        self._setNumber(1, value)
        return

    def _initialize(self):
        super(AssemblingVideoViewModel, self)._initialize()
        self._addNumberProperty(b'operationID', 0)
        self._addNumberProperty(b'stageNumber', 0)
        self.startAssembling = self._addCommand(b'startAssembling')
        return
