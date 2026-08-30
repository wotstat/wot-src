from gui.impl.gen.view_models.common.missions.challenge_mission_model import ChallengeMissionModel

class ChallengeQuestProgressModel(ChallengeMissionModel):
    __slots__ = ()

    def __init__(self, properties=18, commands=0):
        super(ChallengeQuestProgressModel, self).__init__(properties=properties, commands=commands)
        return

    def getId(self):
        return self._getString(12)

    def setId(self, value):
        self._setString(12, value)
        return

    def getChallengeName(self):
        return self._getString(13)

    def setChallengeName(self, value):
        self._setString(13, value)
        return

    def getNavigationEnabled(self):
        return self._getBool(14)

    def setNavigationEnabled(self, value):
        self._setBool(14, value)
        return

    def getIsCompleted(self):
        return self._getBool(15)

    def setIsCompleted(self, value):
        self._setBool(15, value)
        return

    def getCurrentProgress(self):
        return self._getNumber(16)

    def setCurrentProgress(self, value):
        self._setNumber(16, value)
        return

    def getTotalProgress(self):
        return self._getNumber(17)

    def setTotalProgress(self, value):
        self._setNumber(17, value)
        return

    def _initialize(self):
        super(ChallengeQuestProgressModel, self)._initialize()
        self._addStringProperty(b'id', b'')
        self._addStringProperty(b'challengeName', b'')
        self._addBoolProperty(b'navigationEnabled', False)
        self._addBoolProperty(b'isCompleted', False)
        self._addNumberProperty(b'currentProgress', 0)
        self._addNumberProperty(b'totalProgress', 0)
        return
