from gui.impl.gen import R
from frameworks.wulf import ViewModel

class MapsTrainingQueueModel(ViewModel):
    __slots__ = (b'onQuit', b'onMenu', b'onShowPrevTip', b'onShowNextTip', b'onMoveSpace')
    DELAY_DEFAULT = b''
    DELAY_NORMAL = b'normal'
    DELAY_LONG = b'long'

    def __init__(self, properties=4, commands=5):
        super(MapsTrainingQueueModel, self).__init__(properties=properties, commands=commands)
        return

    def getTime(self):
        return self._getString(0)

    def setTime(self, value):
        self._setString(0, value)
        return

    def getDescrTip(self):
        return self._getResource(1)

    def setDescrTip(self, value):
        self._setResource(1, value)
        return

    def getIsDelay(self):
        return self._getBool(2)

    def setIsDelay(self, value):
        self._setBool(2, value)
        return

    def getDelayStatus(self):
        return self._getString(3)

    def setDelayStatus(self, value):
        self._setString(3, value)
        return

    def _initialize(self):
        super(MapsTrainingQueueModel, self)._initialize()
        self._addStringProperty(b'time', b'')
        self._addResourceProperty(b'descrTip', R.invalid())
        self._addBoolProperty(b'isDelay', False)
        self._addStringProperty(b'delayStatus', b'')
        self.onQuit = self._addCommand(b'onQuit')
        self.onMenu = self._addCommand(b'onMenu')
        self.onShowPrevTip = self._addCommand(b'onShowPrevTip')
        self.onShowNextTip = self._addCommand(b'onShowNextTip')
        self.onMoveSpace = self._addCommand(b'onMoveSpace')
        return
