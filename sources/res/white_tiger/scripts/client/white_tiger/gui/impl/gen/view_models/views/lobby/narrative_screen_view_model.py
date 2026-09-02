from frameworks.wulf import ViewModel

class NarrativeScreenViewModel(ViewModel):
    __slots__ = (b'onClose', b'onVoiceoverToggle')

    def __init__(self, properties=1, commands=2):
        super(NarrativeScreenViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getIsVoiceoverActive(self):
        return self._getBool(0)

    def setIsVoiceoverActive(self, value):
        self._setBool(0, value)
        return

    def _initialize(self):
        super(NarrativeScreenViewModel, self)._initialize()
        self._addBoolProperty(b'isVoiceoverActive', False)
        self.onClose = self._addCommand(b'onClose')
        self.onVoiceoverToggle = self._addCommand(b'onVoiceoverToggle')
        return
