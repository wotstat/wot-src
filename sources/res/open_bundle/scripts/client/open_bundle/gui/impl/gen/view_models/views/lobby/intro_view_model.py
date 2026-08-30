from frameworks.wulf import ViewModel

class IntroViewModel(ViewModel):
    __slots__ = (b'onClose', b'onExternalLink')

    def __init__(self, properties=2, commands=2):
        super(IntroViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getBundleType(self):
        return self._getString(0)

    def setBundleType(self, value):
        self._setString(0, value)
        return

    def getTimeLeft(self):
        return self._getNumber(1)

    def setTimeLeft(self, value):
        self._setNumber(1, value)
        return

    def _initialize(self):
        super(IntroViewModel, self)._initialize()
        self._addStringProperty(b'bundleType', b'')
        self._addNumberProperty(b'timeLeft', 0)
        self.onClose = self._addCommand(b'onClose')
        self.onExternalLink = self._addCommand(b'onExternalLink')
        return
