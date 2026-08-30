from frameworks.wulf import ViewModel

class BattleInfoModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=7, commands=0):
        super(BattleInfoModel, self).__init__(properties=properties, commands=commands)
        return

    def getArenaName(self):
        return self._getString(0)

    def setArenaName(self, value):
        self._setString(0, value)
        return

    def getScenario(self):
        return self._getString(1)

    def setScenario(self, value):
        self._setString(1, value)
        return

    def getBattleStartTime(self):
        return self._getNumber(2)

    def setBattleStartTime(self, value):
        self._setNumber(2, value)
        return

    def getBattleDuration(self):
        return self._getNumber(3)

    def setBattleDuration(self, value):
        self._setNumber(3, value)
        return

    def getWinStatus(self):
        return self._getString(4)

    def setWinStatus(self, value):
        self._setString(4, value)
        return

    def getFinishReason(self):
        return self._getString(5)

    def setFinishReason(self, value):
        self._setString(5, value)
        return

    def getFinishReasonClarification(self):
        return self._getString(6)

    def setFinishReasonClarification(self, value):
        self._setString(6, value)
        return

    def _initialize(self):
        super(BattleInfoModel, self)._initialize()
        self._addStringProperty(b'arenaName', b'')
        self._addStringProperty(b'scenario', b'')
        self._addNumberProperty(b'battleStartTime', 0)
        self._addNumberProperty(b'battleDuration', 0)
        self._addStringProperty(b'winStatus', b'')
        self._addStringProperty(b'finishReason', b'')
        self._addStringProperty(b'finishReasonClarification', b'')
        return
