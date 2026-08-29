from frameworks.wulf import ViewModel

class VideoViewSubsPhraseModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(VideoViewSubsPhraseModel, self).__init__(properties=properties, commands=commands)
        return

    def getStartTime(self):
        return self._getReal(0)

    def setStartTime(self, value):
        self._setReal(0, value)
        return

    def getEndTime(self):
        return self._getReal(1)

    def setEndTime(self, value):
        self._setReal(1, value)
        return

    def getText(self):
        return self._getString(2)

    def setText(self, value):
        self._setString(2, value)
        return

    def _initialize(self):
        super(VideoViewSubsPhraseModel, self)._initialize()
        self._addRealProperty(b'startTime', 0.0)
        self._addRealProperty(b'endTime', 0.0)
        self._addStringProperty(b'text', b'')
        return
