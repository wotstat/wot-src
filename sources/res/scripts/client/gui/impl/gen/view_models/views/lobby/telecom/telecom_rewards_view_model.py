from frameworks.wulf import ViewModel

class TelecomRewardsViewModel(ViewModel):
    __slots__ = (b'onClose',)

    def __init__(self, properties=0, commands=1):
        super(TelecomRewardsViewModel, self).__init__(properties=properties, commands=commands)
        return

    def _initialize(self):
        super(TelecomRewardsViewModel, self)._initialize()
        self.onClose = self._addCommand(b'onClose')
        return
