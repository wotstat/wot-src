from frameworks.wulf import ViewModel

class FullStatsViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(FullStatsViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getMissionTitle(self):
        return self._getString(0)

    def setMissionTitle(self, value):
        self._setString(0, value)
        return

    def getMissionTask(self):
        return self._getString(1)

    def setMissionTask(self, value):
        self._setString(1, value)
        return

    def getDifficultyLevel(self):
        return self._getNumber(2)

    def setDifficultyLevel(self, value):
        self._setNumber(2, value)
        return

    def _initialize(self):
        super(FullStatsViewModel, self)._initialize()
        self._addStringProperty(b'missionTitle', b'')
        self._addStringProperty(b'missionTask', b'')
        self._addNumberProperty(b'difficultyLevel', 0)
        return
