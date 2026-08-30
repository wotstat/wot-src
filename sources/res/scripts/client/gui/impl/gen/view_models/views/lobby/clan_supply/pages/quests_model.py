from enum import IntEnum
from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.common.missions.bonuses.icon_bonus_model import IconBonusModel
from gui.impl.gen.view_models.views.lobby.clan_supply.pages.quest_model import QuestModel

class ScreenStatus(IntEnum):
    PENDING = 0
    ERROR = 1
    PLAYER_NOT_IN_CLAN = 2
    REWARD_AVAILABLE = 3
    PREVIOUS_REWARDS = 4
    IN_PROGRESS = 5


class QuestsModel(ViewModel):
    __slots__ = (b'onClaimReward', b'onGoToClans', b'onRefresh')

    def __init__(self, properties=6, commands=3):
        super(QuestsModel, self).__init__(properties=properties, commands=commands)
        return

    def getStatus(self):
        return ScreenStatus(self._getNumber(0))

    def setStatus(self, value):
        self._setNumber(0, value.value)
        return

    def getCycleDuration(self):
        return self._getNumber(1)

    def setCycleDuration(self, value):
        self._setNumber(1, value)
        return

    def getUpdateTime(self):
        return self._getNumber(2)

    def setUpdateTime(self, value):
        self._setNumber(2, value)
        return

    def getIsRewardsLoading(self):
        return self._getBool(3)

    def setIsRewardsLoading(self, value):
        self._setBool(3, value)
        return

    def getQuests(self):
        return self._getArray(4)

    def setQuests(self, value):
        self._setArray(4, value)
        return

    @staticmethod
    def getQuestsType():
        return QuestModel

    def getPreviousRewards(self):
        return self._getArray(5)

    def setPreviousRewards(self, value):
        self._setArray(5, value)
        return

    @staticmethod
    def getPreviousRewardsType():
        return IconBonusModel

    def _initialize(self):
        super(QuestsModel, self)._initialize()
        self._addNumberProperty(b'status')
        self._addNumberProperty(b'cycleDuration', 0)
        self._addNumberProperty(b'updateTime', 0)
        self._addBoolProperty(b'isRewardsLoading', False)
        self._addArrayProperty(b'quests', Array())
        self._addArrayProperty(b'previousRewards', Array())
        self.onClaimReward = self._addCommand(b'onClaimReward')
        self.onGoToClans = self._addCommand(b'onGoToClans')
        self.onRefresh = self._addCommand(b'onRefresh')
        return
