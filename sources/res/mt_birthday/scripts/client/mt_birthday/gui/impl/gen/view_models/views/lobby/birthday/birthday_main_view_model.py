from enum import IntEnum
from frameworks.wulf import ViewModel
from mt_birthday.gui.impl.gen.view_models.views.lobby.birthday.lootbox_entry_point import LootboxEntryPoint

class TabId(IntEnum):
    MAIL = 0
    QUESTS = 1
    REWARDS = 2
    GOLD_WAGON = 3
    TICKET_EXCHANGE = 4
    ABOUT = 5


class BirthdayMainViewModel(ViewModel):
    __slots__ = (b'onTabChange', b'onClose', b'onOpenGoldenCarriage', b'onTipsCompleted')

    def __init__(self, properties=9, commands=4):
        super(BirthdayMainViewModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def lootboxEntryPoint(self):
        return self._getViewModel(0)

    @staticmethod
    def getLootboxEntryPointType():
        return LootboxEntryPoint

    def getIsTipEnabled(self):
        return self._getBool(1)

    def setIsTipEnabled(self, value):
        self._setBool(1, value)
        return

    def getIsGeneralTipEnabled(self):
        return self._getBool(2)

    def setIsGeneralTipEnabled(self, value):
        self._setBool(2, value)
        return

    def getHasNewRewards(self):
        return self._getBool(3)

    def setHasNewRewards(self, value):
        self._setBool(3, value)
        return

    def getCurrentTabId(self):
        return self._getNumber(4)

    def setCurrentTabId(self, value):
        self._setNumber(4, value)
        return

    def getIsIntroSeen(self):
        return self._getBool(5)

    def setIsIntroSeen(self, value):
        self._setBool(5, value)
        return

    def getHasGoldenTickets(self):
        return self._getBool(6)

    def setHasGoldenTickets(self, value):
        self._setBool(6, value)
        return

    def getIsEnabledGoldWagonEntry(self):
        return self._getBool(7)

    def setIsEnabledGoldWagonEntry(self, value):
        self._setBool(7, value)
        return

    def getIsEnabledTicketExchangeEntry(self):
        return self._getBool(8)

    def setIsEnabledTicketExchangeEntry(self, value):
        self._setBool(8, value)
        return

    def _initialize(self):
        super(BirthdayMainViewModel, self)._initialize()
        self._addViewModelProperty(b'lootboxEntryPoint', LootboxEntryPoint())
        self._addBoolProperty(b'isTipEnabled', False)
        self._addBoolProperty(b'isGeneralTipEnabled', False)
        self._addBoolProperty(b'hasNewRewards', False)
        self._addNumberProperty(b'currentTabId', 0)
        self._addBoolProperty(b'isIntroSeen', True)
        self._addBoolProperty(b'hasGoldenTickets', False)
        self._addBoolProperty(b'isEnabledGoldWagonEntry', False)
        self._addBoolProperty(b'isEnabledTicketExchangeEntry', False)
        self.onTabChange = self._addCommand(b'onTabChange')
        self.onClose = self._addCommand(b'onClose')
        self.onOpenGoldenCarriage = self._addCommand(b'onOpenGoldenCarriage')
        self.onTipsCompleted = self._addCommand(b'onTipsCompleted')
        return
