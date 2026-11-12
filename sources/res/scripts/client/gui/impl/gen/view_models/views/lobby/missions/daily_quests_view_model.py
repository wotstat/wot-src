from enum import Enum
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.missions.daily_quests_model import DailyQuestsModel
from gui.impl.gen.view_models.views.lobby.missions.epic_quest_model import EpicQuestModel
from gui.impl.gen.view_models.views.lobby.missions.lootboxes_intro_model import LootboxesIntroModel
from gui.impl.gen.view_models.views.lobby.missions.premium_missions_model import PremiumMissionsModel

class DailyTypes(Enum):
    DEFAULT = b'default'


class OffersState(Enum):
    AVAILABLE = b'available'
    DISABLED = b'disabled'
    NO_OFFERS = b'no_offers'


class DailyQuestsViewModel(ViewModel):
    __slots__ = (b'onClose', b'onReroll', b'onTabClick', b'onInfoToggle', b'onBuyPremiumBtnClick', b'onVehiclePreviewClick', b'onStylePreviewClick', b'onRerollEnabled', b'onClaimRewards', b'onLootboxesIntroClosed')

    def __init__(self, properties=16, commands=10):
        super(DailyQuestsViewModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def dailyQuests(self):
        return self._getViewModel(0)

    @staticmethod
    def getDailyQuestsType():
        return DailyQuestsModel

    @property
    def premiumMissions(self):
        return self._getViewModel(1)

    @staticmethod
    def getPremiumMissionsType():
        return PremiumMissionsModel

    @property
    def epicQuest(self):
        return self._getViewModel(2)

    @staticmethod
    def getEpicQuestType():
        return EpicQuestModel

    @property
    def lootboxesIntro(self):
        return self._getViewModel(3)

    @staticmethod
    def getLootboxesIntroType():
        return LootboxesIntroModel

    def getDailyType(self):
        return DailyTypes(self._getString(4))

    def setDailyType(self, value):
        self._setString(4, value.value)
        return

    def getGetRewardsTimeLeft(self):
        return self._getNumber(5)

    def setGetRewardsTimeLeft(self, value):
        self._setNumber(5, value)
        return

    def getOffersState(self):
        return OffersState(self._getString(6))

    def setOffersState(self, value):
        self._setString(6, value.value)
        return

    def getCurrentTabIdx(self):
        return self._getNumber(7)

    def setCurrentTabIdx(self, value):
        self._setNumber(7, value)
        return

    def getCountDown(self):
        return self._getNumber(8)

    def setCountDown(self, value):
        self._setNumber(8, value)
        return

    def getInfoVisible(self):
        return self._getBool(9)

    def setInfoVisible(self, value):
        self._setBool(9, value)
        return

    def getIsLootboxesIntroVisible(self):
        return self._getBool(10)

    def setIsLootboxesIntroVisible(self, value):
        self._setBool(10, value)
        return

    def getPremMissionsTabDiscovered(self):
        return self._getBool(11)

    def setPremMissionsTabDiscovered(self, value):
        self._setBool(11, value)
        return

    def getIsBattlePassActive(self):
        return self._getBool(12)

    def setIsBattlePassActive(self, value):
        self._setBool(12, value)
        return

    def getIsComp7Active(self):
        return self._getBool(13)

    def setIsComp7Active(self, value):
        self._setBool(13, value)
        return

    def getIsGiftSystemDisabled(self):
        return self._getBool(14)

    def setIsGiftSystemDisabled(self, value):
        self._setBool(14, value)
        return

    def getIsNewYearAvailable(self):
        return self._getBool(15)

    def setIsNewYearAvailable(self, value):
        self._setBool(15, value)
        return

    def _initialize(self):
        super(DailyQuestsViewModel, self)._initialize()
        self._addViewModelProperty(b'dailyQuests', DailyQuestsModel())
        self._addViewModelProperty(b'premiumMissions', PremiumMissionsModel())
        self._addViewModelProperty(b'epicQuest', EpicQuestModel())
        self._addViewModelProperty(b'lootboxesIntro', LootboxesIntroModel())
        self._addStringProperty(b'dailyType')
        self._addNumberProperty(b'getRewardsTimeLeft', 0)
        self._addStringProperty(b'offersState')
        self._addNumberProperty(b'currentTabIdx', 0)
        self._addNumberProperty(b'countDown', 0)
        self._addBoolProperty(b'infoVisible', False)
        self._addBoolProperty(b'isLootboxesIntroVisible', False)
        self._addBoolProperty(b'premMissionsTabDiscovered', False)
        self._addBoolProperty(b'isBattlePassActive', False)
        self._addBoolProperty(b'isComp7Active', False)
        self._addBoolProperty(b'isGiftSystemDisabled', False)
        self._addBoolProperty(b'isNewYearAvailable', False)
        self.onClose = self._addCommand(b'onClose')
        self.onReroll = self._addCommand(b'onReroll')
        self.onTabClick = self._addCommand(b'onTabClick')
        self.onInfoToggle = self._addCommand(b'onInfoToggle')
        self.onBuyPremiumBtnClick = self._addCommand(b'onBuyPremiumBtnClick')
        self.onVehiclePreviewClick = self._addCommand(b'onVehiclePreviewClick')
        self.onStylePreviewClick = self._addCommand(b'onStylePreviewClick')
        self.onRerollEnabled = self._addCommand(b'onRerollEnabled')
        self.onClaimRewards = self._addCommand(b'onClaimRewards')
        self.onLootboxesIntroClosed = self._addCommand(b'onLootboxesIntroClosed')
        return
