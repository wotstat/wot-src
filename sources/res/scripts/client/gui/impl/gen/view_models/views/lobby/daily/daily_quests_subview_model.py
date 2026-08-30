from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.daily.daily_quests_mark_seen_model import DailyQuestsMarkSeenModel
from gui.impl.gen.view_models.views.lobby.daily.daily_quests_premium_model import DailyQuestsPremiumModel
from gui.impl.gen.view_models.views.lobby.daily.daily_quests_regular_model import DailyQuestsRegularModel
from gui.impl.gen.view_models.views.lobby.daily.epic_quest_model import EpicQuestModel

class DailyQuestsSubviewModel(ViewModel):
    __slots__ = (b'onClose', b'onReroll', b'onInfoToggle', b'onBuyPremiumBtnClick', b'onRerollEnabled')

    def __init__(self, properties=8, commands=5):
        super(DailyQuestsSubviewModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def regular(self):
        return self._getViewModel(0)

    @staticmethod
    def getRegularType():
        return DailyQuestsRegularModel

    @property
    def premium(self):
        return self._getViewModel(1)

    @staticmethod
    def getPremiumType():
        return DailyQuestsPremiumModel

    @property
    def epic(self):
        return self._getViewModel(2)

    @staticmethod
    def getEpicType():
        return EpicQuestModel

    @property
    def unseenQuests(self):
        return self._getViewModel(3)

    @staticmethod
    def getUnseenQuestsType():
        return DailyQuestsMarkSeenModel

    def getCurrentTabIdx(self):
        return self._getNumber(4)

    def setCurrentTabIdx(self, value):
        self._setNumber(4, value)
        return

    def getInfoVisible(self):
        return self._getBool(5)

    def setInfoVisible(self, value):
        self._setBool(5, value)
        return

    def getIsBattlePassActive(self):
        return self._getBool(6)

    def setIsBattlePassActive(self, value):
        self._setBool(6, value)
        return

    def getIsComp7Active(self):
        return self._getBool(7)

    def setIsComp7Active(self, value):
        self._setBool(7, value)
        return

    def _initialize(self):
        super(DailyQuestsSubviewModel, self)._initialize()
        self._addViewModelProperty(b'regular', DailyQuestsRegularModel())
        self._addViewModelProperty(b'premium', DailyQuestsPremiumModel())
        self._addViewModelProperty(b'epic', EpicQuestModel())
        self._addViewModelProperty(b'unseenQuests', DailyQuestsMarkSeenModel())
        self._addNumberProperty(b'currentTabIdx', 0)
        self._addBoolProperty(b'infoVisible', False)
        self._addBoolProperty(b'isBattlePassActive', False)
        self._addBoolProperty(b'isComp7Active', False)
        self.onClose = self._addCommand(b'onClose')
        self.onReroll = self._addCommand(b'onReroll')
        self.onInfoToggle = self._addCommand(b'onInfoToggle')
        self.onBuyPremiumBtnClick = self._addCommand(b'onBuyPremiumBtnClick')
        self.onRerollEnabled = self._addCommand(b'onRerollEnabled')
        return
