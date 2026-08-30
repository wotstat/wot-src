import logging, typing, copy
from collections import namedtuple
import AccountCommands, BigWorld
from account_helpers.settings_core.ServerSettingsManager import SETTINGS_SECTIONS
from account_helpers.settings_core.settings_constants import WTLootBoxesViewedKeys
from adisp import adisp_process
from debug_utils import LOG_CODEPOINT_WARNING
from gui import SystemMessages
from gui.Scaleform.Waiting import Waiting
from gui.impl import backport
from gui.impl.gen import R
from gui.shared.formatters import formatPrice
from gui.shared.gui_items.processors import makeI18nError
from messenger.formatters import TimeFormatter
from optional_bonuses import BONUS_MERGERS
from white_tiger.gui.impl.lobby.wt_event_constants import getBonusGroup, WhiteTigerLootBoxes, ReRollButton
from helpers import dependency, time_utils
import Event
from gui.shared.money import Money
from gui.ClientUpdateManager import g_clientUpdateManager
from gui.battle_pass.battle_pass_award import BattlePassAwardsManager
from gui.shared.gui_items.processors.loot_boxes import LootBoxOpenProcessor, Processor, _DEFAULT_ERROR_KEY
from gui.shared.utils.requesters.tokens_requester import TOTAL_KEY
from white_tiger.gui.shared.event_dispatcher import showEventPortalAwardsWindow, showAwardWindow
from gui.server_events.bonuses import splitBonuses, getMergedBonusesFromDicts, VehiclesBonus
from white_tiger.gui.impl.lobby.packers.wt_event_bonuses_packers import LootBoxAwardsManager
from white_tiger.gui.impl.lobby.packers.wt_event_simple_bonus_packers import getWtSplitBonusFunction, getWtBonusGroup
from helpers import server_settings
from skeletons.account_helpers.settings_core import ISettingsCore
from skeletons.gui.shared import IItemsCache
from skeletons.gui.game_control import ILootBoxesController, IWhiteTigerController
from skeletons.gui.lobby_context import ILobbyContext
from shared_utils import findFirst
from soft_exception import SoftException
from white_tiger.messenger.formatters.service_channel import WTEventLootBoxMessageFormatter, WTEventLootBoxRerollRewardsMessageFormatter
from gui.wt_event.wt_event_helpers import getReceivedVehiclesData
from white_tiger_common.wt_constants import WT_MIN_COUNT_TO_ROLL, WT_MAX_COUNT_TO_ROLL
from white_tiger.gui.wt_event_helpers import extendBonusesByLootboxCustomSettings
if typing.TYPE_CHECKING:
    from AccountWhiteTigerComponent import AccountWhiteTigerComponent
_logger = logging.getLogger(__name__)
_TankLimits = namedtuple(b'_TankLimits', (b'guaranteedAttempts', b'leftAttempts', b'isIgnored'))
_GroupBonuses = namedtuple(b'_GroupBonuses', (b'probability', b'bonuses'))

def _processCustomizationBonus(intCD, bonus):
    for item in bonus.getCustomizations():
        itemCD = bonus.getC11nItem(item).intCD
        if itemCD == intCD:
            return True

    return False


def _processTmanTokenBonus(token, bonus):
    return token in bonus.getValue()


def _getBonusProcessor(bonus):
    bonusName = bonus.getName()
    if bonusName == b'customizations':
        return _processCustomizationBonus
    else:
        if bonusName == b'tmanToken':
            return _processTmanTokenBonus
        return


def _pushLootBoxOpenedSystemMessage(awards):
    fmt = WTEventLootBoxMessageFormatter.formatLootBoxRewards(awards)
    if fmt is not None:
        SystemMessages.pushMessage(fmt, SystemMessages.SM_TYPE.WTLootBoxRewards)
    return


def _pushLootBoxOpenedRerollRewardsSystemMessage(awards):
    fmt = WTEventLootBoxRerollRewardsMessageFormatter.formatLootBoxRewards(awards)
    if fmt is not None:
        SystemMessages.pushMessage(fmt, SystemMessages.SM_TYPE.WTLootBoxRerollRewards)
    return


def _pushTankPortalOpenedSystemMessage(ctx):
    fmt = WTEventLootBoxMessageFormatter.formatTankPortalRewards(ctx)
    if fmt is not None:
        SystemMessages.pushMessage(fmt, SystemMessages.SM_TYPE.WTLootBoxRewards)
    return


class _WtLootBoxOpenProcessor(LootBoxOpenProcessor):

    def _successHandler(self, code, ctx=None):
        bonus = ctx.get(b'bonus', [])
        _pushLootBoxOpenedSystemMessage(getMergedBonusesFromDicts(bonus))
        if ctx.get(b'extraRewards'):
            _pushLootBoxOpenedRerollRewardsSystemMessage(ctx.get(b'extraRewards'))
        return super(_WtLootBoxOpenProcessor, self)._successHandler(code, ctx)


class _WtLootBoxClaimProcessor(Processor):

    def __init__(self, boxID):
        super(_WtLootBoxClaimProcessor, self).__init__()
        self.__boxID = boxID
        return

    def _successHandler(self, code, ctx=None):
        bonus = ctx.get(b'bonus')
        extra = ctx.get(b'extra')
        _pushLootBoxOpenedSystemMessage(bonus)
        if extra:
            _pushLootBoxOpenedRerollRewardsSystemMessage(extra)
        return super(_WtLootBoxClaimProcessor, self)._successHandler(code, ctx)

    def _request(self, callback):
        _logger.debug(b'Make server request to claim loot box by boxOpenID: %r', self.__boxID)
        wtComponent = BigWorld.player().AccountWhiteTigerComponent
        wtComponent.claimLootBox(self.__boxID, (lambda code, errStr, ext: self._response(code, callback, ctx=ext, errStr=errStr)))
        return


class _WtLootBoxReRollHistoryProcessor(Processor):

    def __init__(self, boxID):
        super(_WtLootBoxReRollHistoryProcessor, self).__init__()
        self.__boxID = boxID
        return

    def _errorHandler(self, code, errStr=b'', ctx=None):
        return makeI18nError((b'/').join((_DEFAULT_ERROR_KEY, errStr)), _DEFAULT_ERROR_KEY)

    def _request(self, callback):
        _logger.debug(b'Make server request to re-roll history')
        wtComponent = BigWorld.player().AccountWhiteTigerComponent
        wtComponent.getLootBoxPendingBoxes(self.__boxID, (lambda code, errStr, ext: self._response(code, callback, ctx=ext, errStr=errStr)))
        return


class _WTLootBoxRerollProcessor(Processor):

    def __init__(self, boxID, reRollPrice):
        super(_WTLootBoxRerollProcessor, self).__init__()
        self.__boxID = boxID
        self.__reRollPrice = reRollPrice
        return

    def _errorHandler(self, code, errStr=b'', ctx=None):
        return makeI18nError((b'/').join((_DEFAULT_ERROR_KEY, errStr)), _DEFAULT_ERROR_KEY)

    def _request(self, callback):
        _logger.debug(b'Make server request to re-roll lootboxes : %r', self.__boxID)
        wtComponent = BigWorld.player().AccountWhiteTigerComponent
        wtComponent.reRollLootBox(self.__boxID, (lambda code, errStr, ext: self._response(code, callback, ctx=ext, errStr=errStr)))
        return

    def _successHandler(self, code, ctx=None):
        if not ctx:
            ctx = {}
        if ctx.get(b'extraRewards'):
            _pushLootBoxOpenedRerollRewardsSystemMessage(ctx.get(b'extraRewards'))
        msgText = backport.text(R.strings.white_tiger.notifications.lootBoxReRollPrice(), at=TimeFormatter.getLongDatetimeFormat(time_utils.getServerRegionalTime()), price=formatPrice(self.__reRollPrice, useStyle=True))
        SystemMessages.pushMessage(text=msgText, type=SystemMessages.SM_TYPE.FinancialTransactionWithGold)
        return super(_WTLootBoxRerollProcessor, self)._successHandler(code, ctx)


class _WTLootBoxRollProcessor(Processor):

    def __init__(self, lootBoxItem, boxType, boxCount, lootBoxesController):
        super(_WTLootBoxRollProcessor, self).__init__()
        self.__lootBoxesController = lootBoxesController
        self.__boxType = boxType
        self.__lootBox = lootBoxItem
        self.__lootBoxCount = boxCount
        return

    def _errorHandler(self, code, errStr=b'', ctx=None):
        return makeI18nError((b'/').join((_DEFAULT_ERROR_KEY, errStr)), _DEFAULT_ERROR_KEY)

    def _request(self, callback):
        _logger.debug(b'Make server request to re-roll loot box by id: %r', self.__lootBox)
        wtComponent = BigWorld.player().AccountWhiteTigerComponent
        wtComponent.rollLootBox(self.__lootBox.getID(), self.__lootBoxCount, (lambda code, errStr, ext: self._response(code, callback, ctx=ext, errStr=errStr)))
        return

    def _successHandler(self, code, ctx=None):
        if not ctx:
            ctx = {}
        rewards = _preprocessAwards([ctx.get(b'bonus', {})], self.__lootBox)
        isAutoClaimed = self.__lootBoxesController.isStopTokenAmongRewardList(rewards, self.__boxType)
        if isAutoClaimed:
            _pushLootBoxOpenedSystemMessage(ctx[b'bonus'])
        if ctx.get(b'extraRewards'):
            _pushLootBoxOpenedRerollRewardsSystemMessage(ctx.get(b'extraRewards'))
        return super(_WTLootBoxRollProcessor, self)._successHandler(code, ctx)


def getMergedBoxesRewards(boxes):

    def mergeReward(storage, rewardToMerge):
        for key, value in rewardToMerge.iteritems():
            if key in BONUS_MERGERS:
                BONUS_MERGERS[key](storage, key, value, False, 1, None)
            else:
                LOG_CODEPOINT_WARNING()

        storage = [{key: value} for key, value in storage.items()]
        return

    rewards = {}
    for _, boxRewards in boxes.iteritems():
        mergeReward(rewards, copy.deepcopy(boxRewards.get(b'bonus', {})))

    return rewards


class LootBoxesController(ILootBoxesController):
    __gameCtrl = dependency.descriptor(IWhiteTigerController)
    __lobbyContext = dependency.descriptor(ILobbyContext)
    __itemsCache = dependency.descriptor(IItemsCache)
    __settingsCore = dependency.descriptor(ISettingsCore)

    def __init__(self):
        super(LootBoxesController, self).__init__()
        self.__eventManager = Event.EventManager()
        self.onUpdated = Event.Event(self.__eventManager)
        self.onUpdatedConfig = Event.Event(self.__eventManager)
        self.__lootBoxesConfig = {}
        self.__hunterLastViewedCount = 0
        self.__bossLastViewedCount = 0
        self.__isEngineerReroll = False
        self.__mainPrizeVehicles = []
        self.__vehiclesWithCustomData = {}
        self.__isBoxEnabled = False
        return

    def fini(self):
        self.__clear()
        self.__eventManager.clear()
        self.__eventManager = None
        self.__isBoxEnabled = False
        super(LootBoxesController, self).fini()
        return

    def getModeSettings(self):
        return self.__gameCtrl.getModeSettings()

    def onLobbyInited(self, event):
        self.__addListeners()
        self.__packLootBoxes()
        return

    def onAvatarBecomePlayer(self):
        self.__clear()
        return

    def onDisconnected(self):
        self.__clear()
        return

    def onAccountBecomeNonPlayer(self):
        self.__hunterLastViewedCount = 0
        self.__bossLastViewedCount = 0
        return

    def getLootBoxesRewards(self, lootBoxType):
        return self.__lootBoxesConfig.get(lootBoxType, {})

    def getVehiclesWithCustomData(self, lootBoxType):
        return self.__vehiclesWithCustomData.get(lootBoxType, {})

    def getLastViewedCount(self):
        if self.__settingsCore.isReady:
            self.__hunterLastViewedCount = self.__settingsCore.serverSettings.getSectionSettings(SETTINGS_SECTIONS.LOOT_BOX_VIEWED, WTLootBoxesViewedKeys.HUNTER_LAST_VIEWED, 0)
            self.__bossLastViewedCount = self.__settingsCore.serverSettings.getSectionSettings(SETTINGS_SECTIONS.LOOT_BOX_VIEWED, WTLootBoxesViewedKeys.BOSS_LAST_VIEWED, 0)
            hunterCount = self.getLootBoxesCountByType(WhiteTigerLootBoxes.WT_HUNTER)
            bossCount = self.getLootBoxesCountByType(WhiteTigerLootBoxes.WT_BOSS, excludePending=True)
            if self.__hunterLastViewedCount > hunterCount:
                self.__hunterLastViewedCount = hunterCount
                self.__saveHunterLastViewedCount()
            if self.__bossLastViewedCount > bossCount:
                self.__bossLastViewedCount = bossCount
                self.__saveBossLastViewedCount()
        return (
         self.__hunterLastViewedCount, self.__bossLastViewedCount)

    def updateLastViewedCount(self):
        self.__hunterLastViewedCount = self.getLootBoxesCountByType(WhiteTigerLootBoxes.WT_HUNTER)
        self.__bossLastViewedCount = self.getLootBoxesCountByType(WhiteTigerLootBoxes.WT_BOSS, excludePending=True)
        self.__saveHunterLastViewedCount()
        self.__saveBossLastViewedCount()
        return

    def getLootBoxesByType(self, lootBoxType=None):
        if lootBoxType is None:
            lootBoxTypes = (
             WhiteTigerLootBoxes.WT_HUNTER, WhiteTigerLootBoxes.WT_BOSS, WhiteTigerLootBoxes.WT_TANK)
        else:
            lootBoxTypes = (
             lootBoxType,)
        return [lootBox for lootBox in self.__itemsCache.items.tokens.getLootBoxes().itervalues() if lootBox.getType() in lootBoxTypes]

    def getTankLootBoxesCount(self, excludePending):
        return self.getLootBoxesCountByType(WhiteTigerLootBoxes.WT_BOSS, excludePending)

    def getLootBoxesCountByType(self, lootBoxType, excludePending=False):
        if lootBoxType == WhiteTigerLootBoxes.WT_TANK:
            return self.getTankLootBoxesCount(excludePending)
        itemsByType = self.__itemsCache.items.tokens.getLootBoxesCountByType()
        lootBoxes = itemsByType.get(lootBoxType, {})
        resultCount = lootBoxes.get(TOTAL_KEY, 0)
        if excludePending:
            return max(0, resultCount - self.getPendingBoxesCount(lootBoxType))
        return resultCount

    def getLootBoxesCountByTypeForUI(self, lootBoxType, openedBoxes=1):
        count = self.getLootBoxesCountByType(lootBoxType)
        boxRemains = count - openedBoxes if count > openedBoxes else 0
        return boxRemains

    def getLootBoxByTypeInInventory(self, lootBoxType):
        return findFirst((lambda box: box.getType() == lootBoxType), self.getLootBoxesByType(lootBoxType))

    def hasAccountEnoughReRollAttempts(self, boxType):
        count = self.getReRollAttemptsCount(boxType)
        _logger.debug(b'Current %s re-roll attempts: %d, ', boxType, count)
        return count + 1 >= self.getReRollMaximumAttempts(boxType)

    def isEngineerReroll(self):
        return self.__isEngineerReroll

    def hasAccountEnoughMoneyForReRoll(self, boxType):
        reRollPrice = self.__getCurrentReRollPrice(boxType)
        priceType = self.getReRollPriceType(boxType)
        money = self.__itemsCache.items.stats.money
        if not money.isDefined() or not priceType or not reRollPrice.isDefined():
            _logger.error(b'Invalid money %s, priceType %s / %s reRollPrice', repr(money), priceType, repr(reRollPrice))
            return
        shortageTotal = money.getShortage(reRollPrice)
        shortageOfSelectedCurrency = shortageTotal.get(priceType)
        return not shortageOfSelectedCurrency

    def __getSpecificLootBoxConfig(self, boxType):
        config = self.__getLootBoxConfig()
        result = [dictItems for dictItems in config.values() if dictItems[b'type'] == boxType]
        if result:
            return result[0]
        return {}

    def __getCurrentReRollPrice(self, boxType):
        specificLootBoxConfig = self.__getSpecificLootBoxConfig(boxType)
        allPrices = specificLootBoxConfig.get(b'reRoll').get(b'prices')
        priceType = specificLootBoxConfig.get(b'reRoll').get(b'priceType')
        boxTypeAccountCount = self.getReRollAttemptsCount(boxType)
        if boxTypeAccountCount > len(allPrices):
            _logger.error(b'Asked for more Re-Rolls than allowed')
            return None
        else:
            if boxTypeAccountCount == len(allPrices):
                return None
            currentPrice = allPrices[boxTypeAccountCount]
            return Money(**{priceType: currentPrice})

    def getLootBoxLimitsInfo(self, lootBoxType):
        guaranteedAttempts = 0
        leftAttempts = 0
        isIgnored = False
        lootBox = self.getLootBoxByTypeInInventory(lootBoxType)
        if lootBox:
            lootBoxConfig = self.__getSpecificLootBoxConfig(lootBoxType)
            guaranteedAttempts = lootBox.getGuaranteedFrequency()
            limitID = lootBox.getGuaranteedFrequencyName()
            ignoredLimit = lootBoxConfig.get(b'reRoll', {}).get(b'ignoreLimits', {}).get(limitID, {})
            for tokenName, count in ignoredLimit.iteritems():
                if self.__itemsCache.items.tokens.getTokenCount(tokenName) >= count:
                    isIgnored = True

            attempts = self.__itemsCache.items.tokens.getAttemptsAfterGuaranteedRewards(lootBox)
            leftAttempts = max(guaranteedAttempts - attempts, 1)
        return _TankLimits(guaranteedAttempts=guaranteedAttempts, leftAttempts=leftAttempts, isIgnored=isIgnored)

    def getCollectionType(self, itemID):
        return

    def isCollectionElement(self, itemID, collection):
        for bonus in collection:
            processor = _getBonusProcessor(bonus)
            if processor is None:
                continue
            if processor(itemID, bonus):
                return True

        return False

    @adisp_process
    def onPortalOpened(self, boxType, parentWindow, boxCount=1, callbackFailure=None):
        lootBox = self.getLootBoxByTypeInInventory(boxType)
        boxID = lootBox.getID()
        result = yield _WtLootBoxReRollHistoryProcessor(boxID).request()
        if result is None or not result.success:
            _logger.error(b'LootBox result is None or returned Failure')
            if callbackFailure:
                callbackFailure()
            return
        if result.success and result.auxData == {}:
            _logger.debug(b'We do not have unopened lootBoxes, requesting for a new LootBox rewards')
            if boxType != WhiteTigerLootBoxes.WT_TANK:
                if boxCount > WT_MAX_COUNT_TO_ROLL or boxCount < WT_MIN_COUNT_TO_ROLL:
                    _logger.error(b'Wrong box count to roll. %r', boxCount)
                    return
                self.requestLootBoxRoll(boxType, boxCount, parentWindow, callbackFailure=callbackFailure)
            else:
                self.openTankLootBox(parentWindow)
            return
        bonus = result.auxData.get(b'bonus', {})
        boxCount = result.auxData.get(b'boxCount', boxCount)
        if not bonus:
            _logger.error(b'LootBox is opened, but no rewards has been received.')
            return
        else:
            rewards = _preprocessAwards([bonus], lootBox)
            if rewards:
                _logger.debug(b'We have unopened lootBoxes, display them')
                showEventPortalAwardsWindow(boxType, rewards, boxCount)
            else:
                _logger.error(b'It has been a problem with opening a latest unopened reward')
            return

    def openTankLootBox(self, parentWindow=None):

        def onTankLootBoxOpened(requestId, resultId, errorStr, ext):
            isSuccess = resultId == AccountCommands.RES_SUCCESS
            mainPrizeBoughtToken = self.__gameCtrl.getConfig().mainPrizeBoughtToken
            isTankBought = self.__itemsCache.items.tokens.getTokenCount(mainPrizeBoughtToken) > 0
            if isSuccess and isTankBought:
                vehCD = self.__mainPrizeVehicles[0]
                vehBonus = VehiclesBonus(b'vehicles', {vehCD: {}})
                showAwardWindow(WhiteTigerLootBoxes.WT_TANK, [vehBonus], parent=parentWindow)
                ext.update({b'vehicles': [{vehCD: {}}]})
                _pushTankPortalOpenedSystemMessage(ext)
            else:
                Waiting.hide(b'updating')
            return

        BigWorld.player().AccountWhiteTigerComponent.openTankLootBox(callback=onTankLootBoxOpened)
        return

    @adisp_process
    def requestLootBoxRoll(self, boxType, boxCount, parentWindow=None, callback=None, reRollButtonUsed=None, callbackFailure=None):
        boxItem = self.getLootBoxByTypeInInventory(boxType)
        if boxItem is None:
            _logger.error(b'Invalid lootBox item')
            return
        else:
            boxID = boxItem.getID()
            result = None
            if reRollButtonUsed:
                if reRollButtonUsed == ReRollButton.CLAIM_AND_RELAUNCH:
                    result = yield _WtLootBoxClaimProcessor(boxID).request()
                    if result is None:
                        raise SoftException(b'LootBoxOpenProcessor request return unknown result')
                    if result.success:
                        result = yield _WTLootBoxRollProcessor(boxItem, boxType, boxCount, self).request()
                elif reRollButtonUsed == ReRollButton.REROLL:
                    result = yield _WTLootBoxRerollProcessor(boxID, self.getReRollPrice(boxType) * boxCount).request()
            else:
                result = yield _WTLootBoxRollProcessor(boxItem, boxType, boxCount, self).request()
            self.__isEngineerReroll = reRollButtonUsed and reRollButtonUsed == ReRollButton.REROLL
            if result is None or not result.success:
                if callbackFailure:
                    callbackFailure()
                return
            if result.success:
                bonus = result.auxData.get(b'bonus', {})
                if not bonus:
                    _logger.error(b'LootBoxes opened, but no rewards received.')
                    return
                rewards = _preprocessAwards([bonus], boxItem)
                showAwardWindow(boxItem.getType(), rewards, boxCount=boxCount, parent=parentWindow, callback=callback)
            return

    @adisp_process
    def claimReRolledReward(self, boxType, count=1, parentWindow=None, callbackUpdate=None, callbackFailure=None):
        currentCount = self.getLootBoxesCountByType(boxType)
        if currentCount == 0:
            _logger.error(b'Invalid lootBox count')
            return
        else:
            boxItem = self.getLootBoxByTypeInInventory(boxType)
            if boxItem is None:
                _logger.error(b'Invalid lootBox item')
                return
            boxID = boxItem.getID()
            result = yield _WtLootBoxClaimProcessor(boxID).request()
            if result is None:
                raise SoftException(b'LootBoxOpenProcessor request return unknown result')
            if result.success:
                bonus = result.auxData.get(b'bonus', {})
                if not bonus:
                    _logger.error(b'LootBoxes opened, but no rewards received.')
                    return
                rewards = _preprocessAwards([bonus], boxItem)
                openedBoxes = count
                receivedVehicles = getReceivedVehiclesData(rewards, boxType)
                if openedBoxes == 1 and receivedVehicles:
                    showAwardWindow(boxType, rewards, boxCount=count, parent=parentWindow)
                if callbackUpdate is not None:
                    callbackUpdate()
            else:
                SystemMessages.pushMessage(text=result.userMsg, type=result.sysMsgType)
                if callbackFailure:
                    callbackFailure()
            return

    def hasPendingBoxes(self, boxType):
        lootBox = self.getLootBoxByTypeInInventory(boxType)
        boxID = lootBox.getID()
        pendingBoxes = BigWorld.player().whiteTiger.getPendingBoxesByBoxID(boxID)
        return len(pendingBoxes) > 0

    def getPendingBoxesCount(self, boxType):
        lootBox = self.getLootBoxByTypeInInventory(boxType)
        boxID = lootBox.getID()
        pendingBoxes = BigWorld.player().whiteTiger.getPendingBoxesByBoxID(boxID)
        return pendingBoxes.get(b'count', 0)

    def getReRollAttemptsCount(self, boxType):
        lootBox = self.getLootBoxByTypeInInventory(boxType)
        boxID = lootBox.getID()
        reRollCount = BigWorld.player().whiteTiger.getReRollCountByBoxID(boxID)
        return reRollCount

    def getReRollAttemptsLeft(self, boxType):
        boxTypeAttemptsCount = self.getReRollAttemptsCount(boxType)
        return self.getReRollMaximumAttempts(boxType) - boxTypeAttemptsCount

    def getReRollPrice(self, boxType):
        return self.__getCurrentReRollPrice(boxType)

    def getReRollMaximumAttempts(self, boxType):
        specificLootBoxConfig = self.__getSpecificLootBoxConfig(boxType)
        return specificLootBoxConfig.get(b'reRoll').get(b'maxAttempts')

    def getReRollPriceType(self, boxType):
        specificLootBoxConfig = self.__getSpecificLootBoxConfig(boxType)
        return specificLootBoxConfig.get(b'reRoll').get(b'priceType')

    def isStopTokenAmongRewardList(self, rewardsList, boxType):
        return self.__isStopTokenAmongRewards(rewardsList, boxType)

    def rewardsHaveCompensationBonus(self, rewards):
        for reward in rewards:
            if reward.getName() == b'vehicles' and self.__getCompensationBonusPrice(reward) != []:
                return True

        return False

    def getMainPrizeVehicles(self):
        return self.__mainPrizeVehicles

    def getExtraRewards(self, boxType, count=None):
        lootBoxConfig = self.__getSpecificLootBoxConfig(boxType)
        count = count if count is not None else self.getReRollAttemptsCount(boxType)
        return lootBoxConfig.get(b'reRoll', {}).get(b'extras', {}).get(count, None)

    def __getCompensationBonusPrice(self, reward):
        compensationList = reward.getCompensation()
        if any(number > 0 for number in compensationList):
            return compensationList
        return []

    def __addListeners(self):
        self.__lobbyContext.getServerSettings().onServerSettingsChange += self.__onServerSettingChanged
        g_clientUpdateManager.addCallbacks({b'tokens': (self.__onTokensUpdate)})
        return

    def __removeListeners(self):
        self.__lobbyContext.getServerSettings().onServerSettingsChange -= self.__onServerSettingChanged
        g_clientUpdateManager.removeObjectCallbacks(self)
        return

    def isEnabled(self):
        if not self.__lobbyContext.getServerSettings().isLootBoxesEnabled():
            return False
        return self.__isBoxEnabled

    def __clear(self):
        if self.__lootBoxesConfig:
            self.__lootBoxesConfig.clear()
        self.__hunterLastViewedCount = 0
        self.__bossLastViewedCount = 0
        self.__mainPrizeVehicles = []
        self.__removeListeners()
        self.__isBoxEnabled = False
        return

    @server_settings.serverSettingsChangeListener(b'lootBoxes_config')
    def __onServerSettingChanged(self, _):
        self.__lootBoxesConfig.clear()
        self.__mainPrizeVehicles = []
        self.__packLootBoxes()
        self.onUpdatedConfig()
        isHunterEnabled = self.__getSpecificLootBoxConfig(WhiteTigerLootBoxes.WT_HUNTER).get(b'enabled', False)
        isBossEnabled = self.__getSpecificLootBoxConfig(WhiteTigerLootBoxes.WT_BOSS).get(b'enabled', False)
        isTankEnabled = self.__getSpecificLootBoxConfig(WhiteTigerLootBoxes.WT_TANK).get(b'enabled', False)
        self.__isBoxEnabled = all((isHunterEnabled, isBossEnabled, isTankEnabled))
        return

    def __onTokensUpdate(self, diff):
        hunterCount = self.getLootBoxesCountByType(WhiteTigerLootBoxes.WT_HUNTER)
        bossCount = self.getLootBoxesCountByType(WhiteTigerLootBoxes.WT_BOSS)
        if self.__hunterLastViewedCount is None or hunterCount < self.__hunterLastViewedCount:
            self.__hunterLastViewedCount = hunterCount
        if self.__bossLastViewedCount is None or bossCount < self.__bossLastViewedCount:
            self.__bossLastViewedCount = bossCount
        self.onUpdated()
        return

    def __getLootBoxConfig(self):
        return self.__lobbyContext.getServerSettings().getLootBoxConfig()

    def __packLootBoxes(self):
        config = self.__getLootBoxConfig()
        self.__isBoxEnabled = False
        if not config:
            return
        else:
            for box in config.itervalues():
                boxType = box.get(b'type')
                if not self.__isWtBox(boxType) or boxType in self.__lootBoxesConfig:
                    continue
                bonuses = box.get(b'bonus', {})
                box = self.__itemsCache.items.tokens.getLootBoxByType(boxType)
                customBonusItems = box.getCustomBonusData()
                customData = customBonusItems.get(b'vehicles', {})
                self.__vehiclesWithCustomData[boxType] = sorted(customData.items(), key=(lambda x: x[1][b'priority']))
                if bonuses is not None:
                    self.__lootBoxesConfig[boxType] = _convertToBonuses(bonuses)
                    if self.__isMainPrizeWtBox(boxType):
                        bonuses = self.__lootBoxesConfig[boxType][b'guaranteed_items'].bonuses
                        for bonus in bonuses:
                            if bonus.getName() == b'vehicles':
                                for vehicle, _ in bonus.getVehicles():
                                    self.__mainPrizeVehicles.append(vehicle.intCD)

            isHunterEnabled = self.__getSpecificLootBoxConfig(WhiteTigerLootBoxes.WT_HUNTER).get(b'enabled', False)
            isBossEnabled = self.__getSpecificLootBoxConfig(WhiteTigerLootBoxes.WT_BOSS).get(b'enabled', False)
            isTankEnabled = self.__getSpecificLootBoxConfig(WhiteTigerLootBoxes.WT_TANK).get(b'enabled', False)
            self.__isBoxEnabled = all((isHunterEnabled, isBossEnabled, isTankEnabled))
            if not self.__lootBoxesConfig:
                _logger.error(b'[LootBox] Could not fetch lootBox bonus data for some reason')
            return

    def __saveHunterLastViewedCount(self):
        if self.__settingsCore.isReady:
            self.__settingsCore.serverSettings.setSectionSettings(SETTINGS_SECTIONS.LOOT_BOX_VIEWED, {(WTLootBoxesViewedKeys.HUNTER_LAST_VIEWED): (self.__hunterLastViewedCount)})
        return

    def __saveBossLastViewedCount(self):
        if self.__settingsCore.isReady:
            self.__settingsCore.serverSettings.setSectionSettings(SETTINGS_SECTIONS.LOOT_BOX_VIEWED, {(WTLootBoxesViewedKeys.BOSS_LAST_VIEWED): (self.__bossLastViewedCount)})
        return

    def __getStopToken(self, boxType):
        boosLootBoxConfig = self.__getSpecificLootBoxConfig(boxType)
        stopTokenValue = boosLootBoxConfig.get(b'reRoll').get(b'stopToken', None)
        return stopTokenValue

    def __isStopTokenAmongRewards(self, rewardsList, boxType):
        stopToken = self.__getStopToken(boxType)
        if stopToken is None:
            return False
        else:
            for reward in rewardsList:
                bonus = reward.getValue()
                if isinstance(bonus, dict) and stopToken in bonus:
                    return bonus[stopToken].get(b'count') > 0

            return False

    def __isWtBox(self, boxType):
        return boxType in (WhiteTigerLootBoxes.WT_HUNTER, WhiteTigerLootBoxes.WT_BOSS, WhiteTigerLootBoxes.WT_TANK)

    def __isMainPrizeWtBox(self, boxType):
        return boxType == WhiteTigerLootBoxes.WT_TANK


def _convertToBonuses(rewards):
    boxBonuses = BattlePassAwardsManager.composeBonuses([rewards])
    group = {b'byProbabilities': []}
    for boxBonus in boxBonuses:
        oldBonusGroup, probability, bonuses = _convertBonusGroup([boxBonus])
        prob = 0
        if isinstance(probability, list):
            prob = probability[0] * 100
        elif isinstance(probability, float):
            prob = probability * 100
        bonusGroup = getBonusGroup(bonuses)
        if bonusGroup is None:
            bonusGroup = oldBonusGroup
        if bonuses:
            groupBonuses = group.get(bonusGroup, _GroupBonuses(probability, []))
            groupBonuses.bonuses.extend(bonuses)
            group[bonusGroup] = groupBonuses
            group[b'byProbabilities'].append((prob, bonuses))

    return group


def _convertBonusGroup(bonuses):
    probability = None
    hasNewBonuses = True
    while hasNewBonuses:
        hasNewBonuses = False
        flatBonuses = []
        for bonus in bonuses:
            if bonus.getName() == b'groups':
                flatBonuses.extend(LootBoxAwardsManager.composeBonuses(bonus.getValue()))
                hasNewBonuses = True
            elif bonus.getName() in (b'oneof', b'allof'):
                bonusProbability, clearBonuses = bonus.getOptionalBonusesWithProbability()
                if not probability and bonusProbability:
                    probability = bonusProbability[0]
                flatBonuses.extend(clearBonuses)
                hasNewBonuses = True
            else:
                flatBonuses.append(bonus)

        bonuses = flatBonuses

    bonusGroup = getWtBonusGroup(bonuses)
    return (bonusGroup, probability, splitBonuses(bonuses, splitFunc=getWtSplitBonusFunction))


def _preprocessAwards(awards, lootBox):
    awards = [_preprocessBonusGroup(group) for group in awards] if len(awards) > 1 else _preprocessBonusGroup(awards)
    customBonusData = lootBox.getCustomBonusData()
    extendedRewards = extendBonusesByLootboxCustomSettings(awards, customBonusData)
    return sorted(extendedRewards, key=(lambda x: x.wtExtendData[b'weight']), reverse=True)


def _preprocessBonusGroup(awards):
    bonusList = [
     isinstance(awards, list) or awards] if 1 else awards
    bonuses = LootBoxAwardsManager.composeBonuses(bonusList)
    return LootBoxAwardsManager.processCompensation(bonuses)
