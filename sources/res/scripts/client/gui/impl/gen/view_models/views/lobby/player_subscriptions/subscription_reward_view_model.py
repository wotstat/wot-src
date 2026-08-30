from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.common.missions.bonuses.bonus_model import BonusModel
from gui.impl.gen.view_models.views.lobby.player_subscriptions.main_reward_model import MainRewardModel

class SubscriptionRewardViewModel(ViewModel):
    __slots__ = (b'onCloseButtonClick', b'onChooseButtonClick')

    def __init__(self, properties=5, commands=2):
        super(SubscriptionRewardViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getSubscriptionTitle(self):
        return self._getString(0)

    def setSubscriptionTitle(self, value):
        self._setString(0, value)
        return

    def getDescText(self):
        return self._getString(1)

    def setDescText(self, value):
        self._setString(1, value)
        return

    def getMainRewards(self):
        return self._getArray(2)

    def setMainRewards(self, value):
        self._setArray(2, value)
        return

    @staticmethod
    def getMainRewardsType():
        return MainRewardModel

    def getHasSelectiveRewards(self):
        return self._getBool(3)

    def setHasSelectiveRewards(self, value):
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
        super(SubscriptionRewardViewModel, self)._initialize()
        self._addStringProperty(b'subscriptionTitle', b'')
        self._addStringProperty(b'descText', b'')
        self._addArrayProperty(b'mainRewards', Array())
        self._addBoolProperty(b'hasSelectiveRewards', True)
        self._addArrayProperty(b'rewards', Array())
        self.onCloseButtonClick = self._addCommand(b'onCloseButtonClick')
        self.onChooseButtonClick = self._addCommand(b'onChooseButtonClick')
        return
