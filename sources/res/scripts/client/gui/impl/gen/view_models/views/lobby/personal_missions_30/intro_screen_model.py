from frameworks.wulf import ViewModel

class IntroScreenModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=1, commands=0):
        super(IntroScreenModel, self).__init__(properties=properties, commands=commands)
        return

    def getVideoPath(self):
        return self._getString(0)

    def setVideoPath(self, value):
        self._setString(0, value)
        return

    def _initialize(self):
        super(IntroScreenModel, self)._initialize()
        self._addStringProperty(b'videoPath', b'')
        return
