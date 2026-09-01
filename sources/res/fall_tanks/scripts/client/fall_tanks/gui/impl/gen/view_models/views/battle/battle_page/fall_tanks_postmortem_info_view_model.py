from frameworks.wulf import ViewModel

class FallTanksPostmortemInfoViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=1, commands=0):
        super(FallTanksPostmortemInfoViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getIsFinished(self):
        return self._getBool(0)

    def setIsFinished(self, value):
        self._setBool(0, value)
        return

    def _initialize(self):
        super(FallTanksPostmortemInfoViewModel, self)._initialize()
        self._addBoolProperty(b'isFinished', False)
        return
