from gui.impl.gen import R
from frameworks.wulf import ViewModel

class VideoViewModel(ViewModel):
    __slots__ = (b'onClose',)

    def __init__(self, properties=6, commands=1):
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

    def getCanEscape(self):
        return self._getBool(4)

    def setCanEscape(self, value):
        self._setBool(4, value)
        return

    def getIsNewYear(self):
        return self._getBool(5)

    def setIsNewYear(self, value):
        self._setBool(5, value)
        return

    def _initialize(self):
        super(VideoViewModel, self)._initialize()
        self._addBoolProperty(b'isControlsVisible', True)
        self._addBoolProperty(b'isSubtitlesVisible', True)
        self._addResourceProperty(b'videoPath', R.invalid())
        self._addRealProperty(b'initialAudioVolume', 0.5)
        self._addBoolProperty(b'canEscape', True)
        self._addBoolProperty(b'isNewYear', False)
        self.onClose = self._addCommand(b'onClose')
        return
