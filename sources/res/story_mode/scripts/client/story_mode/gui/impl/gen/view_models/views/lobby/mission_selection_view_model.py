from frameworks.wulf import Array
from frameworks.wulf import ViewModel

class MissionSelectionViewModel(ViewModel):
    __slots__ = (b'onQuit', b'onMissionSelect', b'onLoaded')

    def __init__(self, properties=3, commands=3):
        super(MissionSelectionViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getMissionId(self):
        return self._getNumber(0)

    def setMissionId(self, value):
        self._setNumber(0, value)
        return

    def getIsTaskCompleted(self):
        return self._getBool(1)

    def setIsTaskCompleted(self, value):
        self._setBool(1, value)
        return

    def getMissions(self):
        return self._getArray(2)

    def setMissions(self, value):
        self._setArray(2, value)
        return

    @staticmethod
    def getMissionsType():
        return bool

    def _initialize(self):
        super(MissionSelectionViewModel, self)._initialize()
        self._addNumberProperty(b'missionId', 0)
        self._addBoolProperty(b'isTaskCompleted', False)
        self._addArrayProperty(b'missions', Array())
        self.onQuit = self._addCommand(b'onQuit')
        self.onMissionSelect = self._addCommand(b'onMissionSelect')
        self.onLoaded = self._addCommand(b'onLoaded')
        return
