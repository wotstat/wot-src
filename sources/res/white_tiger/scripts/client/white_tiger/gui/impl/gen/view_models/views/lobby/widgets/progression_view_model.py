from frameworks.wulf import ViewModel

class ProgressionViewModel(ViewModel):
    __slots__ = (b'onClose', b'onAboutClicked', b'onTakeReward')

    def __init__(self, properties=0, commands=3):
        super(ProgressionViewModel, self).__init__(properties=properties, commands=commands)
        return

    def _initialize(self):
        super(ProgressionViewModel, self)._initialize()
        self.onClose = self._addCommand(b'onClose')
        self.onAboutClicked = self._addCommand(b'onAboutClicked')
        self.onTakeReward = self._addCommand(b'onTakeReward')
        return
