from frameworks.wulf import ViewModel

class FortRushProgressionCompleteViewModel(ViewModel):
    __slots__ = (b'onClose', b'onSoundPlay')

    def __init__(self, properties=0, commands=2):
        super(FortRushProgressionCompleteViewModel, self).__init__(properties=properties, commands=commands)
        return

    def _initialize(self):
        super(FortRushProgressionCompleteViewModel, self)._initialize()
        self.onClose = self._addCommand(b'onClose')
        self.onSoundPlay = self._addCommand(b'onSoundPlay')
        return
