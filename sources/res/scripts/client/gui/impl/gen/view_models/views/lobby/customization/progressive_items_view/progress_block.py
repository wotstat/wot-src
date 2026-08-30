from frameworks.wulf import ViewModel

class ProgressBlock(ViewModel):
    __slots__ = ()
    PB_EMPTY = b'empty'
    PB_DISCRETE = b'discrete'
    PB_PLAIN = b'plain'

    def __init__(self, properties=5, commands=0):
        super(ProgressBlock, self).__init__(properties=properties, commands=commands)
        return

    def getProgressBarType(self):
        return self._getString(0)

    def setProgressBarType(self, value):
        self._setString(0, value)
        return

    def getHideProgressBarAndString(self):
        return self._getBool(1)

    def setHideProgressBarAndString(self, value):
        self._setBool(1, value)
        return

    def getUnlockCondition(self):
        return self._getString(2)

    def setUnlockCondition(self, value):
        self._setString(2, value)
        return

    def getProgressionVal(self):
        return self._getNumber(3)

    def setProgressionVal(self, value):
        self._setNumber(3, value)
        return

    def getMaxProgressionVal(self):
        return self._getNumber(4)

    def setMaxProgressionVal(self, value):
        self._setNumber(4, value)
        return

    def _initialize(self):
        super(ProgressBlock, self)._initialize()
        self._addStringProperty(b'progressBarType', b'PB_EMPTY')
        self._addBoolProperty(b'hideProgressBarAndString', False)
        self._addStringProperty(b'unlockCondition', b'')
        self._addNumberProperty(b'progressionVal', 0)
        self._addNumberProperty(b'maxProgressionVal', 0)
        return
