from frameworks.wulf import ViewModel

class EpilogueWindowViewModel(ViewModel):
    __slots__ = (b'onClose', b'onLoaded')

    def __init__(self, properties=0, commands=2):
        super(EpilogueWindowViewModel, self).__init__(properties=properties, commands=commands)
        return

    def _initialize(self):
        super(EpilogueWindowViewModel, self)._initialize()
        self.onClose = self._addCommand(b'onClose')
        self.onLoaded = self._addCommand(b'onLoaded')
        return
