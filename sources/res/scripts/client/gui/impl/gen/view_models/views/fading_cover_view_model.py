from frameworks.wulf import ViewModel
from gui.impl.gen import R

class FadingCoverViewModel(ViewModel):
    __slots__ = (b'onFadingOutComplete', b'onFadingInComplete')

    def __init__(self, properties=4, commands=2):
        super(FadingCoverViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getBackground(self):
        return self._getResource(0)

    def setBackground(self, value):
        self._setResource(0, value)
        return

    def getIsVisible(self):
        return self._getBool(1)

    def setIsVisible(self, value):
        self._setBool(1, value)
        return

    def getFadeInDuration(self):
        return self._getReal(2)

    def setFadeInDuration(self, value):
        self._setReal(2, value)
        return

    def getFadeOutDuration(self):
        return self._getReal(3)

    def setFadeOutDuration(self, value):
        self._setReal(3, value)
        return

    def _initialize(self):
        super(FadingCoverViewModel, self)._initialize()
        self._addResourceProperty(b'background', R.invalid())
        self._addBoolProperty(b'isVisible', False)
        self._addRealProperty(b'fadeInDuration', 0.0)
        self._addRealProperty(b'fadeOutDuration', 0.0)
        self.onFadingOutComplete = self._addCommand(b'onFadingOutComplete')
        self.onFadingInComplete = self._addCommand(b'onFadingInComplete')
        return
