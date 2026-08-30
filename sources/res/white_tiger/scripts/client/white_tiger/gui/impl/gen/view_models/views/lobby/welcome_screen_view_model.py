from frameworks.wulf import ViewModel

class WelcomeScreenViewModel(ViewModel):
    __slots__ = (b'onVideoPlay', b'onClose', b'onViewLoaded')

    def __init__(self, properties=0, commands=3):
        super(WelcomeScreenViewModel, self).__init__(properties=properties, commands=commands)
        return

    def _initialize(self):
        super(WelcomeScreenViewModel, self)._initialize()
        self.onVideoPlay = self._addCommand(b'onVideoPlay')
        self.onClose = self._addCommand(b'onClose')
        self.onViewLoaded = self._addCommand(b'onViewLoaded')
        return
