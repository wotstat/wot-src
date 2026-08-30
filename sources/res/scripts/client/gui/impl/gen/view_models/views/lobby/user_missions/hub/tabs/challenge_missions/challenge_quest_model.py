from enum import Enum
from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.common.missions.challenge_mission_model import ChallengeMissionModel

class ChallengeState(Enum):
    INACTIVE = b'inactive'
    ACTIVE = b'active'
    FAILED = b'failed'
    COMPLETED = b'completed'


class ChallengeQuestModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=19, commands=0):
        super(ChallengeQuestModel, self).__init__(properties=properties, commands=commands)
        return

    def getChallengeID(self):
        return self._getNumber(0)

    def setChallengeID(self, value):
        self._setNumber(0, value)
        return

    def getState(self):
        return ChallengeState(self._getString(1))

    def setState(self, value):
        self._setString(1, value.value)
        return

    def getType(self):
        return self._getString(2)

    def setType(self, value):
        self._setString(2, value)
        return

    def getPriority(self):
        return self._getNumber(3)

    def setPriority(self, value):
        self._setNumber(3, value)
        return

    def getExpireTime(self):
        return self._getNumber(4)

    def setExpireTime(self, value):
        self._setNumber(4, value)
        return

    def getAttempts(self):
        return self._getNumber(5)

    def setAttempts(self, value):
        self._setNumber(5, value)
        return

    def getRemainingAttempts(self):
        return self._getNumber(6)

    def setRemainingAttempts(self, value):
        self._setNumber(6, value)
        return

    def getCompletedMissions(self):
        return self._getNumber(7)

    def setCompletedMissions(self, value):
        self._setNumber(7, value)
        return

    def getTotalMissions(self):
        return self._getNumber(8)

    def setTotalMissions(self, value):
        self._setNumber(8, value)
        return

    def getChallengeName(self):
        return self._getString(9)

    def setChallengeName(self, value):
        self._setString(9, value)
        return

    def getIsNew(self):
        return self._getBool(10)

    def setIsNew(self, value):
        self._setBool(10, value)
        return

    def getRemainingFreeRestarts(self):
        return self._getNumber(11)

    def setRemainingFreeRestarts(self, value):
        self._setNumber(11, value)
        return

    def getRestartCost(self):
        return self._getNumber(12)

    def setRestartCost(self, value):
        self._setNumber(12, value)
        return

    def getCurrencyType(self):
        return self._getString(13)

    def setCurrencyType(self, value):
        self._setString(13, value)
        return

    def getIsEnoughMoney(self):
        return self._getBool(14)

    def setIsEnoughMoney(self, value):
        self._setBool(14, value)
        return

    def getMissions(self):
        return self._getArray(15)

    def setMissions(self, value):
        self._setArray(15, value)
        return

    @staticmethod
    def getMissionsType():
        return ChallengeMissionModel

    def getMainRewardType(self):
        return self._getString(16)

    def setMainRewardType(self, value):
        self._setString(16, value)
        return

    def getCompletions(self):
        return self._getNumber(17)

    def setCompletions(self, value):
        self._setNumber(17, value)
        return

    def getAllowedCompletions(self):
        return self._getNumber(18)

    def setAllowedCompletions(self, value):
        self._setNumber(18, value)
        return

    def _initialize(self):
        super(ChallengeQuestModel, self)._initialize()
        self._addNumberProperty(b'challengeID', 0)
        self._addStringProperty(b'state')
        self._addStringProperty(b'type', b'')
        self._addNumberProperty(b'priority', 0)
        self._addNumberProperty(b'expireTime', 0)
        self._addNumberProperty(b'attempts', 0)
        self._addNumberProperty(b'remainingAttempts', 0)
        self._addNumberProperty(b'completedMissions', 0)
        self._addNumberProperty(b'totalMissions', 0)
        self._addStringProperty(b'challengeName', b'')
        self._addBoolProperty(b'isNew', False)
        self._addNumberProperty(b'remainingFreeRestarts', 0)
        self._addNumberProperty(b'restartCost', 0)
        self._addStringProperty(b'currencyType', b'')
        self._addBoolProperty(b'isEnoughMoney', False)
        self._addArrayProperty(b'missions', Array())
        self._addStringProperty(b'mainRewardType', b'')
        self._addNumberProperty(b'completions', 0)
        self._addNumberProperty(b'allowedCompletions', 0)
        return
