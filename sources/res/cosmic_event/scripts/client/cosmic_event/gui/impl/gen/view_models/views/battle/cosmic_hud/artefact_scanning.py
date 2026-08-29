from frameworks.wulf import ViewModel

class ArtefactScanning(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(ArtefactScanning, self).__init__(properties=properties, commands=commands)
        return

    def getTimeLeft(self):
        return self._getNumber(0)

    def setTimeLeft(self, value):
        self._setNumber(0, value)
        return

    def getTotalTime(self):
        return self._getNumber(1)

    def setTotalTime(self, value):
        self._setNumber(1, value)
        return

    def getActivePlayers(self):
        return self._getNumber(2)

    def setActivePlayers(self, value):
        self._setNumber(2, value)
        return

    def _initialize(self):
        super(ArtefactScanning, self)._initialize()
        self._addNumberProperty(b'timeLeft', 0)
        self._addNumberProperty(b'totalTime', 0)
        self._addNumberProperty(b'activePlayers', 0)
        return
