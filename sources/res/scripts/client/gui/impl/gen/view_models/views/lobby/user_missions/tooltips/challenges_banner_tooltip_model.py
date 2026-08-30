from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.common.missions.challenge_mission_model import ChallengeMissionModel

class ChallengesBannerTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=6, commands=0):
        super(ChallengesBannerTooltipModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def mission(self):
        return self._getViewModel(0)

    @staticmethod
    def getMissionType():
        return ChallengeMissionModel

    def getTime(self):
        return self._getNumber(1)

    def setTime(self, value):
        self._setNumber(1, value)
        return

    def getChallengeName(self):
        return self._getString(2)

    def setChallengeName(self, value):
        self._setString(2, value)
        return

    def getCompletedMissions(self):
        return self._getNumber(3)

    def setCompletedMissions(self, value):
        self._setNumber(3, value)
        return

    def getTotalMissions(self):
        return self._getNumber(4)

    def setTotalMissions(self, value):
        self._setNumber(4, value)
        return

    def getRemainingAttempts(self):
        return self._getNumber(5)

    def setRemainingAttempts(self, value):
        self._setNumber(5, value)
        return

    def _initialize(self):
        super(ChallengesBannerTooltipModel, self)._initialize()
        self._addViewModelProperty(b'mission', ChallengeMissionModel())
        self._addNumberProperty(b'time', 0)
        self._addStringProperty(b'challengeName', b'')
        self._addNumberProperty(b'completedMissions', 0)
        self._addNumberProperty(b'totalMissions', 0)
        self._addNumberProperty(b'remainingAttempts', 0)
        return
