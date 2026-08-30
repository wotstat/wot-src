from frameworks.wulf import ViewModel

class WotPlusIntroViewModel(ViewModel):
    __slots__ = (b'onClose', b'onAffirmative', b'onInfo')

    def __init__(self, properties=0, commands=3):
        super(WotPlusIntroViewModel, self).__init__(properties=properties, commands=commands)
        return

    def _initialize(self):
        super(WotPlusIntroViewModel, self)._initialize()
        self.onClose = self._addCommand(b'onClose')
        self.onAffirmative = self._addCommand(b'onAffirmative')
        self.onInfo = self._addCommand(b'onInfo')
        return
