from frameworks.wulf import ViewModel

class UiLoggerModel(ViewModel):
    __slots__ = (b'log',)

    def __init__(self, properties=0, commands=1):
        super(UiLoggerModel, self).__init__(properties=properties, commands=commands)
        return

    def _initialize(self):
        super(UiLoggerModel, self)._initialize()
        self.log = self._addCommand(b'log')
        return
