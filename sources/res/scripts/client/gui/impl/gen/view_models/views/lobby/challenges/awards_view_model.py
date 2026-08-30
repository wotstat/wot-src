from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.views.lobby.challenges.bonus_model import BonusModel

class AwardsViewModel(ViewModel):
    __slots__ = (b'onClose', b'onHangar', b'onChallenges')

    def __init__(self, properties=5, commands=3):
        super(AwardsViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getChallengeName(self):
        return self._getString(0)

    def setChallengeName(self, value):
        self._setString(0, value)
        return

    def getMainRewardType(self):
        return self._getString(1)

    def setMainRewardType(self, value):
        self._setString(1, value)
        return

    def getIsCompleted(self):
        return self._getBool(2)

    def setIsCompleted(self, value):
        self._setBool(2, value)
        return

    def getIsAvailable(self):
        return self._getBool(3)

    def setIsAvailable(self, value):
        self._setBool(3, value)
        return

    def getRewards(self):
        return self._getArray(4)

    def setRewards(self, value):
        self._setArray(4, value)
        return

    @staticmethod
    def getRewardsType():
        return BonusModel

    def _initialize(self):
        super(AwardsViewModel, self)._initialize()
        self._addStringProperty(b'challengeName', b'')
        self._addStringProperty(b'mainRewardType', b'')
        self._addBoolProperty(b'isCompleted', False)
        self._addBoolProperty(b'isAvailable', False)
        self._addArrayProperty(b'rewards', Array())
        self.onClose = self._addCommand(b'onClose')
        self.onHangar = self._addCommand(b'onHangar')
        self.onChallenges = self._addCommand(b'onChallenges')
        return
