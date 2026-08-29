from frameworks.wulf import ViewModel

class CongratulationsWindowViewModel(ViewModel):
    __slots__ = (b'onClose', b'onLoaded')

    def __init__(self, properties=2, commands=2):
        super(CongratulationsWindowViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getIsCloseVisible(self):
        return self._getBool(0)

    def setIsCloseVisible(self, value):
        self._setBool(0, value)
        return

    def getIsOnboarding(self):
        return self._getBool(1)

    def setIsOnboarding(self, value):
        self._setBool(1, value)
        return

    def _initialize(self):
        super(CongratulationsWindowViewModel, self)._initialize()
        self._addBoolProperty(b'isCloseVisible', False)
        self._addBoolProperty(b'isOnboarding', False)
        self.onClose = self._addCommand(b'onClose')
        self.onLoaded = self._addCommand(b'onLoaded')
        return
