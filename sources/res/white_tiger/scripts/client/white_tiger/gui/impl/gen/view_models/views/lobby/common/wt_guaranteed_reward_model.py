from frameworks.wulf import ViewModel

class WtGuaranteedRewardModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(WtGuaranteedRewardModel, self).__init__(properties=properties, commands=commands)
        return

    def getAttemptsCount(self):
        return self._getNumber(0)

    def setAttemptsCount(self, value):
        self._setNumber(0, value)
        return

    def getLeftAttemptsCount(self):
        return self._getNumber(1)

    def setLeftAttemptsCount(self, value):
        self._setNumber(1, value)
        return

    def getGuaranteedTankAttemptCount(self):
        return self._getNumber(2)

    def setGuaranteedTankAttemptCount(self, value):
        self._setNumber(2, value)
        return

    def getIsIgnored(self):
        return self._getBool(3)

    def setIsIgnored(self, value):
        self._setBool(3, value)
        return

    def _initialize(self):
        super(WtGuaranteedRewardModel, self)._initialize()
        self._addNumberProperty(b'attemptsCount', 0)
        self._addNumberProperty(b'leftAttemptsCount', 0)
        self._addNumberProperty(b'guaranteedTankAttemptCount', 0)
        self._addBoolProperty(b'isIgnored', False)
        return
