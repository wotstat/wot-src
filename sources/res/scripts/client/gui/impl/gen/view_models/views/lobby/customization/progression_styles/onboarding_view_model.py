from frameworks.wulf import ViewModel

class OnboardingViewModel(ViewModel):
    __slots__ = (b'onClose', b'onGotoStyle')

    def __init__(self, properties=1, commands=2):
        super(OnboardingViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getIsFirstShow(self):
        return self._getBool(0)

    def setIsFirstShow(self, value):
        self._setBool(0, value)
        return

    def _initialize(self):
        super(OnboardingViewModel, self)._initialize()
        self._addBoolProperty(b'isFirstShow', False)
        self.onClose = self._addCommand(b'onClose')
        self.onGotoStyle = self._addCommand(b'onGotoStyle')
        return
