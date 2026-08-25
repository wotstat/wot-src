from frameworks.wulf import ViewModel

class SelectableViewModel(ViewModel):
    __slots__ = (b'onMoveSpace', b'onOverScene')

    def __init__(self, properties=0, commands=2):
        super(SelectableViewModel, self).__init__(properties=properties, commands=commands)
        return

    def _initialize(self):
        super(SelectableViewModel, self)._initialize()
        self.onMoveSpace = self._addCommand(b'onMoveSpace')
        self.onOverScene = self._addCommand(b'onOverScene')
        return
