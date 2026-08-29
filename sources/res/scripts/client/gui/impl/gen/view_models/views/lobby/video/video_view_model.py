from gui.impl.gen import R
from frameworks.wulf import ViewModel

class VideoViewModel(ViewModel):
    __slots__ = (b'onCloseBtnClick', b'onVideoStarted', b'onVideoStopped', b'onLoadError')

    def __init__(self, properties=6, commands=4):
        super(VideoViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getVideoSource(self):
        return self._getResource(0)

    def setVideoSource(self, value):
        self._setResource(0, value)
        return

    def getSubtitleTrack(self):
        return self._getNumber(1)

    def setSubtitleTrack(self, value):
        self._setNumber(1, value)
        return

    def getIsWindowAccessible(self):
        return self._getBool(2)

    def setIsWindowAccessible(self, value):
        self._setBool(2, value)
        return

    def getIsUIVisible(self):
        return self._getBool(3)

    def setIsUIVisible(self, value):
        self._setBool(3, value)
        return

    def getIsVignetteVisible(self):
        return self._getBool(4)

    def setIsVignetteVisible(self, value):
        self._setBool(4, value)
        return

    def getIsAutoClose(self):
        return self._getBool(5)

    def setIsAutoClose(self, value):
        self._setBool(5, value)
        return

    def _initialize(self):
        super(VideoViewModel, self)._initialize()
        self._addResourceProperty(b'videoSource', R.invalid())
        self._addNumberProperty(b'subtitleTrack', 0)
        self._addBoolProperty(b'isWindowAccessible', True)
        self._addBoolProperty(b'isUIVisible', False)
        self._addBoolProperty(b'isVignetteVisible', True)
        self._addBoolProperty(b'isAutoClose', True)
        self.onCloseBtnClick = self._addCommand(b'onCloseBtnClick')
        self.onVideoStarted = self._addCommand(b'onVideoStarted')
        self.onVideoStopped = self._addCommand(b'onVideoStopped')
        self.onLoadError = self._addCommand(b'onLoadError')
        return
