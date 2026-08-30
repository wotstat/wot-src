from frameworks.wulf import ViewModel

class WelcomeViewModel(ViewModel):
    __slots__ = (b'onClose',)

    def __init__(self, properties=0, commands=1):
        super(WelcomeViewModel, self).__init__(properties=properties, commands=commands)
        return

    def _initialize(self):
        super(WelcomeViewModel, self)._initialize()
        self.onClose = self._addCommand(b'onClose')
        return
