from frameworks.wulf import ViewModel

class PersonalMissionsIntroViewModel(ViewModel):
    __slots__ = (b'onClose', b'onContinue', b'onVideoOpen', b'onMoreInfo')

    def __init__(self, properties=0, commands=4):
        super(PersonalMissionsIntroViewModel, self).__init__(properties=properties, commands=commands)
        return

    def _initialize(self):
        super(PersonalMissionsIntroViewModel, self)._initialize()
        self.onClose = self._addCommand(b'onClose')
        self.onContinue = self._addCommand(b'onContinue')
        self.onVideoOpen = self._addCommand(b'onVideoOpen')
        self.onMoreInfo = self._addCommand(b'onMoreInfo')
        return
