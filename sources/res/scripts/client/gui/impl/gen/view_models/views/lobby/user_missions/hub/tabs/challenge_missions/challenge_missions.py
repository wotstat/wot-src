from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.views.lobby.user_missions.hub.tabs.challenge_missions.challenges_pack import ChallengesPack

class ChallengeMissions(ViewModel):
    __slots__ = (b'onSelectChallenge', b'openPreview', b'onAction')
    ACTION_ACTIVATE = b'activate'
    ACTION_RESTART = b'restart'
    ACTION_SURRENDER = b'surrender'

    def __init__(self, properties=6, commands=3):
        super(ChallengeMissions, self).__init__(properties=properties, commands=commands)
        return

    def getEnabled(self):
        return self._getBool(0)

    def setEnabled(self, value):
        self._setBool(0, value)
        return

    def getActiveChallengeID(self):
        return self._getNumber(1)

    def setActiveChallengeID(self, value):
        self._setNumber(1, value)
        return

    def getIsSuitableVehicles(self):
        return self._getBool(2)

    def setIsSuitableVehicles(self, value):
        self._setBool(2, value)
        return

    def getSelectedChallengeID(self):
        return self._getNumber(3)

    def setSelectedChallengeID(self, value):
        self._setNumber(3, value)
        return

    def getSelectedChallengeExpireTime(self):
        return self._getNumber(4)

    def setSelectedChallengeExpireTime(self, value):
        self._setNumber(4, value)
        return

    def getChallengesPacks(self):
        return self._getArray(5)

    def setChallengesPacks(self, value):
        self._setArray(5, value)
        return

    @staticmethod
    def getChallengesPacksType():
        return ChallengesPack

    def _initialize(self):
        super(ChallengeMissions, self)._initialize()
        self._addBoolProperty(b'enabled', False)
        self._addNumberProperty(b'activeChallengeID', 0)
        self._addBoolProperty(b'isSuitableVehicles', False)
        self._addNumberProperty(b'selectedChallengeID', 0)
        self._addNumberProperty(b'selectedChallengeExpireTime', 0)
        self._addArrayProperty(b'challengesPacks', Array())
        self.onSelectChallenge = self._addCommand(b'onSelectChallenge')
        self.openPreview = self._addCommand(b'openPreview')
        self.onAction = self._addCommand(b'onAction')
        return
