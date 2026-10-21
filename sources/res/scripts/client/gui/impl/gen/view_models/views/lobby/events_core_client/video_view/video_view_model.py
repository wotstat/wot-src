from gui.impl.gen import R
from frameworks.wulf import ViewModel

class VideoViewModel(ViewModel):
    __slots__ = (b'onClose',)

    def __init__(self, properties=11, commands=1):
        super(VideoViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getIsControlsVisible(self):
        return self._getBool(0)

    def setIsControlsVisible(self, value):
        self._setBool(0, value)
        return

    def getIsSubtitlesVisible(self):
        return self._getBool(1)

    def setIsSubtitlesVisible(self, value):
        self._setBool(1, value)
        return

    def getVideoPath(self):
        return self._getResource(2)

    def setVideoPath(self, value):
        self._setResource(2, value)
        return

    def getInitialAudioVolume(self):
        return self._getReal(3)

    def setInitialAudioVolume(self, value):
        self._setReal(3, value)
        return

    def getPauseOnMinimize(self):
        return self._getBool(4)

    def setPauseOnMinimize(self, value):
        self._setBool(4, value)
        return

    def getIsCloseButtonVisible(self):
        return self._getBool(5)

    def setIsCloseButtonVisible(self, value):
        self._setBool(5, value)
        return

    def getStartFadeIn(self):
        return self._getReal(6)

    def setStartFadeIn(self, value):
        self._setReal(6, value)
        return

    def getStartFadeOut(self):
        return self._getReal(7)

    def setStartFadeOut(self, value):
        self._setReal(7, value)
        return

    def getEndFadeIn(self):
        return self._getReal(8)

    def setEndFadeIn(self, value):
        self._setReal(8, value)
        return

    def getEndFadeOut(self):
        return self._getReal(9)

    def setEndFadeOut(self, value):
        self._setReal(9, value)
        return

    def getIsClosing(self):
        return self._getBool(10)

    def setIsClosing(self, value):
        self._setBool(10, value)
        return

    def _initialize(self):
        super(VideoViewModel, self)._initialize()
        self._addBoolProperty(b'isControlsVisible', True)
        self._addBoolProperty(b'isSubtitlesVisible', True)
        self._addResourceProperty(b'videoPath', R.invalid())
        self._addRealProperty(b'initialAudioVolume', 0.5)
        self._addBoolProperty(b'pauseOnMinimize', True)
        self._addBoolProperty(b'isCloseButtonVisible', True)
        self._addRealProperty(b'startFadeIn', 0.0)
        self._addRealProperty(b'startFadeOut', 0.0)
        self._addRealProperty(b'endFadeIn', 0.0)
        self._addRealProperty(b'endFadeOut', 0.0)
        self._addBoolProperty(b'isClosing', False)
        self.onClose = self._addCommand(b'onClose')
        return
