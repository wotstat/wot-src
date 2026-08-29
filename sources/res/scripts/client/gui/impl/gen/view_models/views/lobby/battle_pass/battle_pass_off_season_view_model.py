from frameworks.wulf import ViewModel

class BattlePassOffSeasonViewModel(ViewModel):
    __slots__ = ()
    LOSE_VOTE = b'loseVote'
    WIN_VOTE = b'winVote'
    NOT_VOTE = b'notVote'

    def __init__(self, properties=12, commands=0):
        super(BattlePassOffSeasonViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getLevel(self):
        return self._getNumber(0)

    def setLevel(self, value):
        self._setNumber(0, value)
        return

    def getHasBattlePass(self):
        return self._getBool(1)

    def setHasBattlePass(self, value):
        self._setBool(1, value)
        return

    def getIsPostProgression(self):
        return self._getBool(2)

    def setIsPostProgression(self, value):
        self._setBool(2, value)
        return

    def getIsPostProgressionCompleted(self):
        return self._getBool(3)

    def setIsPostProgressionCompleted(self, value):
        self._setBool(3, value)
        return

    def getIsEnabled(self):
        return self._getBool(4)

    def setIsEnabled(self, value):
        self._setBool(4, value)
        return

    def getLeftVehicle(self):
        return self._getString(5)

    def setLeftVehicle(self, value):
        self._setString(5, value)
        return

    def getLeftPoints(self):
        return self._getNumber(6)

    def setLeftPoints(self, value):
        self._setNumber(6, value)
        return

    def getRightVehicle(self):
        return self._getString(7)

    def setRightVehicle(self, value):
        self._setString(7, value)
        return

    def getRightPoints(self):
        return self._getNumber(8)

    def setRightPoints(self, value):
        self._setNumber(8, value)
        return

    def getSeasonName(self):
        return self._getString(9)

    def setSeasonName(self, value):
        self._setString(9, value)
        return

    def getIsFailedService(self):
        return self._getBool(10)

    def setIsFailedService(self, value):
        self._setBool(10, value)
        return

    def getVoteStatus(self):
        return self._getString(11)

    def setVoteStatus(self, value):
        self._setString(11, value)
        return

    def _initialize(self):
        super(BattlePassOffSeasonViewModel, self)._initialize()
        self._addNumberProperty(b'level', 1)
        self._addBoolProperty(b'hasBattlePass', False)
        self._addBoolProperty(b'isPostProgression', False)
        self._addBoolProperty(b'isPostProgressionCompleted', False)
        self._addBoolProperty(b'isEnabled', True)
        self._addStringProperty(b'leftVehicle', b'')
        self._addNumberProperty(b'leftPoints', 0)
        self._addStringProperty(b'rightVehicle', b'')
        self._addNumberProperty(b'rightPoints', 0)
        self._addStringProperty(b'seasonName', b'')
        self._addBoolProperty(b'isFailedService', False)
        self._addStringProperty(b'voteStatus', b'notVote')
        return
