from frameworks.wulf import ViewModel

class CustomizationResourceVideoRewardViewModel(ViewModel):
    __slots__ = (b'onClose', b'onStarted')

    def __init__(self, properties=0, commands=2):
        super(CustomizationResourceVideoRewardViewModel, self).__init__(properties=properties, commands=commands)
        return

    def _initialize(self):
        super(CustomizationResourceVideoRewardViewModel, self)._initialize()
        self.onClose = self._addCommand(b'onClose')
        self.onStarted = self._addCommand(b'onStarted')
        return
