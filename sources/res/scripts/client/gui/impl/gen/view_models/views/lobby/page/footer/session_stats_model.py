from frameworks.wulf import ViewModel

class SessionStatsModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(SessionStatsModel, self).__init__(properties=properties, commands=commands)
        return

    def getBattleCount(self):
        return self._getNumber(0)

    def setBattleCount(self, value):
        self._setNumber(0, value)
        return

    def getEnabled(self):
        return self._getBool(1)

    def setEnabled(self, value):
        self._setBool(1, value)
        return

    def getSessionStatsEnabled(self):
        return self._getBool(2)

    def setSessionStatsEnabled(self, value):
        self._setBool(2, value)
        return

    def getWinback(self):
        return self._getBool(3)

    def setWinback(self, value):
        self._setBool(3, value)
        return

    def _initialize(self):
        super(SessionStatsModel, self)._initialize()
        self._addNumberProperty(b'battleCount', 0)
        self._addBoolProperty(b'enabled', False)
        self._addBoolProperty(b'sessionStatsEnabled', False)
        self._addBoolProperty(b'winback', False)
        return
