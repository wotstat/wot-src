from enum import Enum
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.missions.daily_quests_model import DailyQuestsModel
from gui.impl.gen.view_models.views.lobby.missions.epic_quest_model import EpicQuestModel
from gui.impl.gen.view_models.views.lobby.missions.premium_missions_model import PremiumMissionsModel

class DailyTypes(Enum):
    DEFAULT = b'default'


class OffersState(Enum):
    AVAILABLE = b'available'
    DISABLED = b'disabled'
    NO_OFFERS = b'no_offers'


class DailyQuestsViewModel(ViewModel):
    __slots__ = (b'onClose', b'onReroll', b'onTabClick', b'onInfoToggle', b'onBuyPremiumBtnClick', b'onVehiclePreviewClick', b'onStylePreviewClick', b'onRerollEnabled', b'onClaimRewards')

    def __init__(self, properties=12, commands=9):
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

    def getDailyType(self):
        return DailyTypes(self._getString(3))

    def setDailyType(self, value):
        self._setString(3, value.value)
        return

    def getGetRewardsTimeLeft(self):
        return self._getNumber(4)

    def setGetRewardsTimeLeft(self, value):
        self._setNumber(4, value)
        return

    def getOffersState(self):
        return OffersState(self._getString(5))

    def setOffersState(self, value):
        self._setString(5, value.value)
        return

    def getCurrentTabIdx(self):
        return self._getNumber(6)

    def setCurrentTabIdx(self, value):
        self._setNumber(6, value)
        return

    def getCountDown(self):
        return self._getNumber(7)

    def setCountDown(self, value):
        self._setNumber(7, value)
        return

    def getInfoVisible(self):
        return self._getBool(8)

    def setInfoVisible(self, value):
        self._setBool(8, value)
        return

    def getPremMissionsTabDiscovered(self):
        return self._getBool(9)

    def setPremMissionsTabDiscovered(self, value):
        self._setBool(9, value)
        return

    def getIsBattlePassActive(self):
        return self._getBool(10)

    def setIsBattlePassActive(self, value):
        self._setBool(10, value)
        return

    def getIsComp7Active(self):
        return self._getBool(11)

    def setIsComp7Active(self, value):
        self._setBool(11, value)
        return

    def _initialize(self):
        super(DailyQuestsViewModel, self)._initialize()
        self._addViewModelProperty(b'dailyQuests', DailyQuestsModel())
        self._addViewModelProperty(b'premiumMissions', PremiumMissionsModel())
        self._addViewModelProperty(b'epicQuest', EpicQuestModel())
        self._addStringProperty(b'dailyType')
        self._addNumberProperty(b'getRewardsTimeLeft', 0)
        self._addStringProperty(b'offersState')
        self._addNumberProperty(b'currentTabIdx', 0)
        self._addNumberProperty(b'countDown', 0)
        self._addBoolProperty(b'infoVisible', False)
        self._addBoolProperty(b'premMissionsTabDiscovered', False)
        self._addBoolProperty(b'isBattlePassActive', False)
        self._addBoolProperty(b'isComp7Active', False)
        self.onClose = self._addCommand(b'onClose')
        self.onReroll = self._addCommand(b'onReroll')
        self.onTabClick = self._addCommand(b'onTabClick')
        self.onInfoToggle = self._addCommand(b'onInfoToggle')
        self.onBuyPremiumBtnClick = self._addCommand(b'onBuyPremiumBtnClick')
        self.onVehiclePreviewClick = self._addCommand(b'onVehiclePreviewClick')
        self.onStylePreviewClick = self._addCommand(b'onStylePreviewClick')
        self.onRerollEnabled = self._addCommand(b'onRerollEnabled')
        self.onClaimRewards = self._addCommand(b'onClaimRewards')
        return
