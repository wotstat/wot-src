from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.common.missions.bonuses.bonus_model import BonusModel
from gui.impl.gen.view_models.common.missions.bonuses.icon_bonus_model import IconBonusModel

class BirthdayRewardsViewModel(ViewModel):
    __slots__ = (b'onClose', b'goToContainers', b'goToGoldCarriage', b'goToTicketExchange')

    def __init__(self, properties=13, commands=4):
        super(BirthdayRewardsViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getBloggerName(self):
        return self._getString(0)

    def setBloggerName(self, value):
        self._setString(0, value)
        return

    def getPhraseID(self):
        return self._getNumber(1)

    def setPhraseID(self, value):
        self._setNumber(1, value)
        return

    def getStage(self):
        return self._getNumber(2)

    def setStage(self, value):
        self._setNumber(2, value)
        return

    def getIsRewardSeen(self):
        return self._getBool(3)

    def setIsRewardSeen(self, value):
        self._setBool(3, value)
        return

    def getIsFinalReward(self):
        return self._getBool(4)

    def setIsFinalReward(self, value):
        self._setBool(4, value)
        return

    def getIsAllChallengesComplete(self):
        return self._getBool(5)

    def setIsAllChallengesComplete(self, value):
        self._setBool(5, value)
        return

    def getIsNameLoading(self):
        return self._getBool(6)

    def setIsNameLoading(self, value):
        self._setBool(6, value)
        return

    def getIsOnlyBadge(self):
        return self._getBool(7)

    def setIsOnlyBadge(self, value):
        self._setBool(7, value)
        return

    def getReplyGiftsCount(self):
        return self._getNumber(8)

    def setReplyGiftsCount(self, value):
        self._setNumber(8, value)
        return

    def getIsGoldWagonEnabled(self):
        return self._getBool(9)

    def setIsGoldWagonEnabled(self, value):
        self._setBool(9, value)
        return

    def getIsTicketExchangeEnabled(self):
        return self._getBool(10)

    def setIsTicketExchangeEnabled(self, value):
        self._setBool(10, value)
        return

    def getMainRewards(self):
        return self._getArray(11)

    def setMainRewards(self, value):
        self._setArray(11, value)
        return

    @staticmethod
    def getMainRewardsType():
        return BonusModel

    def getRewards(self):
        return self._getArray(12)

    def setRewards(self, value):
        self._setArray(12, value)
        return

    @staticmethod
    def getRewardsType():
        return IconBonusModel

    def _initialize(self):
        super(BirthdayRewardsViewModel, self)._initialize()
        self._addStringProperty(b'bloggerName', b'')
        self._addNumberProperty(b'phraseID', 1)
        self._addNumberProperty(b'stage', 0)
        self._addBoolProperty(b'isRewardSeen', True)
        self._addBoolProperty(b'isFinalReward', False)
        self._addBoolProperty(b'isAllChallengesComplete', False)
        self._addBoolProperty(b'isNameLoading', False)
        self._addBoolProperty(b'isOnlyBadge', False)
        self._addNumberProperty(b'replyGiftsCount', 0)
        self._addBoolProperty(b'isGoldWagonEnabled', True)
        self._addBoolProperty(b'isTicketExchangeEnabled', True)
        self._addArrayProperty(b'mainRewards', Array())
        self._addArrayProperty(b'rewards', Array())
        self.onClose = self._addCommand(b'onClose')
        self.goToContainers = self._addCommand(b'goToContainers')
        self.goToGoldCarriage = self._addCommand(b'goToGoldCarriage')
        self.goToTicketExchange = self._addCommand(b'goToTicketExchange')
        return
