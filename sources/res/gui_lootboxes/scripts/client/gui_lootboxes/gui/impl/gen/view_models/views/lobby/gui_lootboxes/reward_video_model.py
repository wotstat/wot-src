from gui.impl.gen import R
from frameworks.wulf import ViewModel

class RewardVideoModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(RewardVideoModel, self).__init__(properties=properties, commands=commands)
        return

    def getVideoResName(self):
        return self._getResource(0)

    def setVideoResName(self, value):
        self._setResource(0, value)
        return

    def getDuration(self):
        return self._getNumber(1)

    def setDuration(self, value):
        self._setNumber(1, value)
        return

    def getShowFooterTiming(self):
        return self._getNumber(2)

    def setShowFooterTiming(self, value):
        self._setNumber(2, value)
        return

    def _initialize(self):
        super(RewardVideoModel, self)._initialize()
        self._addResourceProperty(b'videoResName', R.invalid())
        self._addNumberProperty(b'duration', 0)
        self._addNumberProperty(b'showFooterTiming', 0)
        return
