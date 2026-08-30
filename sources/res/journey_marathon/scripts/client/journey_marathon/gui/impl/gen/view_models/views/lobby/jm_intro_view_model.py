from frameworks.wulf import ViewModel

class JmIntroViewModel(ViewModel):
    __slots__ = (b'onClose',)

    def __init__(self, properties=0, commands=1):
        super(JmIntroViewModel, self).__init__(properties=properties, commands=commands)
        return

    def _initialize(self):
        super(JmIntroViewModel, self)._initialize()
        self.onClose = self._addCommand(b'onClose')
        return
