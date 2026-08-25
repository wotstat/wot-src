from frameworks.wulf import ViewModel

class RewardPathViewModel(ViewModel):
    __slots__ = (b'onClick',)

    def __init__(self, properties=5, commands=1):
        super(RewardPathViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getCurrentProgress(self):
        return self._getNumber(0)

    def setCurrentProgress(self, value):
        self._setNumber(0, value)
        return

    def getIsCompleted(self):
        return self._getBool(1)

    def setIsCompleted(self, value):
        self._setBool(1, value)
        return

    def getDataCollected(self):
        return self._getNumber(2)

    def setDataCollected(self, value):
        self._setNumber(2, value)
        return

    def getDataAmount(self):
        return self._getNumber(3)

    def setDataAmount(self, value):
        self._setNumber(3, value)
        return

    def getTimeLeft(self):
        return self._getNumber(4)

    def setTimeLeft(self, value):
        self._setNumber(4, value)
        return

    def _initialize(self):
        super(RewardPathViewModel, self)._initialize()
        self._addNumberProperty(b'currentProgress', 0)
        self._addBoolProperty(b'isCompleted', False)
        self._addNumberProperty(b'dataCollected', 0)
        self._addNumberProperty(b'dataAmount', 0)
        self._addNumberProperty(b'timeLeft', 0)
        self.onClick = self._addCommand(b'onClick')
        return
