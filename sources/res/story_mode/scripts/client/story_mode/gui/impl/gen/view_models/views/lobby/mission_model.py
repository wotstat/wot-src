from enum import Enum
from frameworks.wulf import ViewModel

class MissionsDifficulty(Enum):
    UNDEFINED = b''
    NORMAL = b'normal'
    HARD = b'hard'
    VERY_HARD = b'very_hard'


class MissionModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=5, commands=0):
        super(MissionModel, self).__init__(properties=properties, commands=commands)
        return

    def getMissionId(self):
        return self._getNumber(0)

    def setMissionId(self, value):
        self._setNumber(0, value)
        return

    def getDisplayName(self):
        return self._getString(1)

    def setDisplayName(self, value):
        self._setString(1, value)
        return

    def getIsCompleted(self):
        return self._getBool(2)

    def setIsCompleted(self, value):
        self._setBool(2, value)
        return

    def getLocked(self):
        return self._getBool(3)

    def setLocked(self, value):
        self._setBool(3, value)
        return

    def getDifficulty(self):
        return MissionsDifficulty(self._getString(4))

    def setDifficulty(self, value):
        self._setString(4, value.value)
        return

    def _initialize(self):
        super(MissionModel, self)._initialize()
        self._addNumberProperty(b'missionId', 0)
        self._addStringProperty(b'displayName', b'')
        self._addBoolProperty(b'isCompleted', False)
        self._addBoolProperty(b'locked', False)
        self._addStringProperty(b'difficulty')
        return
