from frameworks.wulf import ViewModel

class FullscreenVideoViewModel(ViewModel):
    __slots__ = (b'onClose',)

    def __init__(self, properties=3, commands=1):
        super(FullscreenVideoViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getVideoName(self):
        return self._getString(0)

    def setVideoName(self, value):
        self._setString(0, value)
        return

    def getAudioName(self):
        return self._getString(1)

    def setAudioName(self, value):
        self._setString(1, value)
        return

    def getIsWindowAccessible(self):
        return self._getBool(2)

    def setIsWindowAccessible(self, value):
        self._setBool(2, value)
        return

    def _initialize(self):
        super(FullscreenVideoViewModel, self)._initialize()
        self._addStringProperty(b'videoName', b'')
        self._addStringProperty(b'audioName', b'')
        self._addBoolProperty(b'isWindowAccessible', False)
        self.onClose = self._addCommand(b'onClose')
        return
