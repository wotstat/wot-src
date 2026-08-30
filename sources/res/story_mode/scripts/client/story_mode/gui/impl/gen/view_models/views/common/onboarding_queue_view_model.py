from frameworks.wulf import ViewModel

class OnboardingQueueViewModel(ViewModel):
    __slots__ = (b'onQuit', b'onLoaded')

    def __init__(self, properties=1, commands=2):
        super(OnboardingQueueViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getIsVisibleButton(self):
        return self._getBool(0)

    def setIsVisibleButton(self, value):
        self._setBool(0, value)
        return

    def _initialize(self):
        super(OnboardingQueueViewModel, self)._initialize()
        self._addBoolProperty(b'isVisibleButton', False)
        self.onQuit = self._addCommand(b'onQuit')
        self.onLoaded = self._addCommand(b'onLoaded')
        return
