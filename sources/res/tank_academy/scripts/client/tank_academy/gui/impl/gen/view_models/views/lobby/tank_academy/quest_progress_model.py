from frameworks.wulf import ViewModel

class QuestProgressModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(QuestProgressModel, self).__init__(properties=properties, commands=commands)
        return

    def getCountCompleted(self):
        return self._getNumber(0)

    def setCountCompleted(self, value):
        self._setNumber(0, value)
        return

    def getLastSeenProgress(self):
        return self._getNumber(1)

    def setLastSeenProgress(self, value):
        self._setNumber(1, value)
        return

    def getTotalQuests(self):
        return self._getNumber(2)

    def setTotalQuests(self, value):
        self._setNumber(2, value)
        return

    def _initialize(self):
        super(QuestProgressModel, self)._initialize()
        self._addNumberProperty(b'countCompleted', 0)
        self._addNumberProperty(b'lastSeenProgress', 0)
        self._addNumberProperty(b'totalQuests', 0)
        return
