from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.promo_code_reward_screen.reward_bonus_model import RewardBonusModel

class PromoCodeRewardScreenViewModel(ViewModel):
    __slots__ = (b'onClose', b'navigateToQuests')
    QUEST_REWARDS_NAME = b'questRewards'
    ARG_REWARD_INDEX = b'tooltipId'
    MAX_REWARDS = 10
    MAX_MAIN_REWARDS = 3

    def __init__(self, properties=10, commands=2):
        super(PromoCodeRewardScreenViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getDescription(self):
        return self._getString(0)

    def setDescription(self, value):
        self._setString(0, value)
        return

    def getTitle(self):
        return self._getString(1)

    def setTitle(self, value):
        self._setString(1, value)
        return

    def getSubtitle(self):
        return self._getString(2)

    def setSubtitle(self, value):
        self._setString(2, value)
        return

    def getQuestsDescription(self):
        return self._getString(3)

    def setQuestsDescription(self, value):
        self._setString(3, value)
        return

    def getBackgroundImage(self):
        return self._getString(4)

    def setBackgroundImage(self, value):
        self._setString(4, value)
        return

    def getMainRewards(self):
        return self._getArray(5)

    def setMainRewards(self, value):
        self._setArray(5, value)
        return

    @staticmethod
    def getMainRewardsType():
        return RewardBonusModel

    def getRewards(self):
        return self._getArray(6)

    def setRewards(self, value):
        self._setArray(6, value)
        return

    @staticmethod
    def getRewardsType():
        return RewardBonusModel

    def getQuestRewards(self):
        return self._getArray(7)

    def setQuestRewards(self, value):
        self._setArray(7, value)
        return

    @staticmethod
    def getQuestRewardsType():
        return RewardBonusModel

    def getHasQuests(self):
        return self._getBool(8)

    def setHasQuests(self, value):
        self._setBool(8, value)
        return

    def getShowToTasksButton(self):
        return self._getBool(9)

    def setShowToTasksButton(self, value):
        self._setBool(9, value)
        return

    def _initialize(self):
        super(PromoCodeRewardScreenViewModel, self)._initialize()
        self._addStringProperty(b'description', b'')
        self._addStringProperty(b'title', b'')
        self._addStringProperty(b'subtitle', b'')
        self._addStringProperty(b'questsDescription', b'')
        self._addStringProperty(b'backgroundImage', b'')
        self._addArrayProperty(b'mainRewards', Array())
        self._addArrayProperty(b'rewards', Array())
        self._addArrayProperty(b'questRewards', Array())
        self._addBoolProperty(b'hasQuests', False)
        self._addBoolProperty(b'showToTasksButton', False)
        self.onClose = self._addCommand(b'onClose')
        self.navigateToQuests = self._addCommand(b'navigateToQuests')
        return
