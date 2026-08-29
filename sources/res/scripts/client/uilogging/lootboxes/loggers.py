import json, BigWorld
from account_helpers.AccountSettings import LOOT_BOXES_SHORT_STAT_STATE
from helpers import dependency
from gui_lootboxes.skeletons.statistic_lootbox_controller import IStatisticLootBoxController
from skeletons.gui.impl import IGuiLoader
from skeletons.gui.shared import IItemsCache
from wotdecorators import noexcept
from skeletons.gui.game_control import IGuiLootBoxesController
from uilogging.base.logger import FlowLogger, MetricsLogger
from uilogging.lootboxes.constants import Actions, BUY_BUTTONS_MAP, DEFAULT_TIME_LIMIT, FEATURE, Items, STATISTIC_BUTTONS_MAP, TABS_STATE_MAP, Views

class LootboxMetricsLogger(MetricsLogger):

    def __init__(self):
        super(LootboxMetricsLogger, self).__init__(FEATURE)
        return


class LootboxFlowLogger(FlowLogger):

    def __init__(self):
        super(LootboxFlowLogger, self).__init__(FEATURE)
        return


class LootboxStorageLogger(LootboxMetricsLogger):
    __gui = dependency.descriptor(IGuiLoader)
    __guiLootBoxesCtrl = dependency.descriptor(IGuiLootBoxesController)
    __guiLootBoxesStatisticCtrl = dependency.descriptor(IStatisticLootBoxController)
    __itemsCache = dependency.descriptor(IItemsCache)

    @noexcept
    def logAnimationSwitch(self, state):
        logInfo = {b'lootBoxCount': (self.__guiLootBoxesCtrl.getBoxesCount()), 
           b'quality': (BigWorld.currentGraphicPresetKey())}
        self.log(action=Actions.ANIMATION_SWITCH, item=Items.ANIMATION_SWITCH_BUTTON, itemState=str(state), info=json.dumps(logInfo))
        return

    @noexcept
    def logBuyBtnClick(self, lootBoxID, btnID):
        rotationsToGuaranteed = 0
        lootboxType = b''
        lootBoxCount = 0
        lootBox = self.__itemsCache.items.tokens.getLootBoxByID(int(lootBoxID))
        if lootBox:
            lootboxType = lootBox.getType()
            lootBoxID = lootBox.getID()
            lootBoxCount = lootBox.getInventoryCount()
            attemptsAfterGuaranteed = self.__itemsCache.items.tokens.getAttemptsAfterGuaranteedRewards(lootBox)
            guaranteed = lootBox.getGuaranteedFrequency()
            rotationsToGuaranteed = guaranteed - attemptsAfterGuaranteed if attemptsAfterGuaranteed <= guaranteed else guaranteed
        logInfo = {b'lootBox': lootboxType, 
           b'lootBoxID': (lootBoxID or 0), 
           b'lootBoxCount': lootBoxCount, 
           b'rotationsToGuaranteed': rotationsToGuaranteed, 
           b'silverCount': (self.__itemsCache.items.stats.money.credits), 
           b'goldCount': (self.__itemsCache.items.stats.money.gold)}
        self.log(action=Actions.CLICK, item=BUY_BUTTONS_MAP.get(btnID, BUY_BUTTONS_MAP[0]), info=json.dumps(logInfo))
        return

    @noexcept
    def logOpenProbabilityClick(self, lootBox):
        boxesHistory = self.__itemsCache.items.tokens.getCacheValue(b'lootBoxes', {}).get(b'history', {})
        logInfo = {b'lootBox': (lootBox.getType()), 
           b'lootBoxID': (lootBox.getID()), 
           b'been_opened': (lootBox.getHistoryName() in boxesHistory)}
        self.log(action=Actions.PROBABILITY_OPEN_CLICK, item=Items.PROBABILITY_BTN, info=json.dumps(logInfo))
        return

    def logStorageEscHotkey(self):
        self.log(action=Actions.STORAGE_ESC_HOTKEY, item=Items.CLOSE_ESC_HOTKEY, parentScreen=Views.STORAGE)
        return

    @noexcept
    def logStatisticsClick(self, lootBox, btnID=None, btn=None, hasPreviewItems=False):
        if lootBox is not None:
            lootboxType = lootBox.getType()
            lootBoxID = lootBox.getID()
            totalCollected = self.__guiLootBoxesStatisticCtrl.getLootBoxesVersionInfo(lootBox.getID())
        else:
            lootboxType = lootBoxID = b'all_boxes'
            totalCollected = self.__guiLootBoxesStatisticCtrl.getLootBoxesVersionInfo()
        lastTabsState = TABS_STATE_MAP[self.__guiLootBoxesCtrl.getSetting(LOOT_BOXES_SHORT_STAT_STATE)]
        logInfo = {b'lootBox': lootboxType, 
           b'lootBoxID': lootBoxID, 
           b'lootBoxCount': (lootBox.getInventoryCount() if lootBox else self.__guiLootBoxesCtrl.getBoxesCount()), 
           b'lootBoxTotalCollected': totalCollected, 
           b'lastTabsState': (lastTabsState.value)}
        item = btn if btn else self._getButtonByID(btnID)
        if item == Items.STATISTIC_FULL_STATS_BTN:
            logInfo[b'hasPreviewItems'] = hasPreviewItems
            logInfo[b'lootBoxTotalCollected'] = self.__guiLootBoxesStatisticCtrl.getLootBoxesVersionInfo()
        self.log(action=Actions.STATISTIC_OPEN_CLICK, item=item, info=json.dumps(logInfo))
        return

    def logFullStatisticClick(self, lootBox=None, hasPreviewItems=False):
        self.logStatisticsClick(lootBox, btn=Items.STATISTIC_FULL_STATS_BTN, hasPreviewItems=hasPreviewItems)
        return

    def logStatisticsEscHotkey(self, activeTab):
        self.log(action=Actions.STATISTIC_ESC_HOTKEY, item=Items.CLOSE_ESC_HOTKEY, parentScreen=Views.STATISTICS_SHORT_STATS, info=json.dumps({b'activeTab': (activeTab.value)}))
        return

    @staticmethod
    def _getButtonByID(btnID):
        if btnID is None:
            return Items.UNKNOWN_STATS_BTN
        else:
            return STATISTIC_BUTTONS_MAP.get(int(btnID), Items.UNKNOWN_STATS_BTN)


class LootboxProbabilityViewLogger(LootboxMetricsLogger):

    def startViewAction(self):
        self.startAction(Actions.PROBABILITY_VIEWED)
        return

    def stopViewAction(self, item=b''):
        if item == b'esc_button':
            item = Items.CLOSE_ESC_HOTKEY.value
        elif item == b'close_button':
            item = Items.CLOSE_CROSS_BTN.value
        self.stopAction(action=Actions.PROBABILITY_VIEWED, item=item, timeLimit=DEFAULT_TIME_LIMIT)
        return
