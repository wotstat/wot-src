from frameworks.wulf import ViewModel

class NyLeaderboardInfoViewModel(ViewModel):
    __slots__ = (b'onClose',)

    def __init__(self, properties=0, commands=1):
        super(NyLeaderboardInfoViewModel, self).__init__(properties=properties, commands=commands)
        return

    def _initialize(self):
        super(NyLeaderboardInfoViewModel, self)._initialize()
        self.onClose = self._addCommand(b'onClose')
        return
