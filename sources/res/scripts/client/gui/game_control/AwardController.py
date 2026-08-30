import datetime, logging, types, typing, weakref
from abc import ABCMeta, abstractmethod
from copy import deepcopy
from functools import partial
from itertools import chain, ifilter
import ArenaType, BigWorld, gui.awards.event_dispatcher as award_events
from gui.impl.gen.view_models.views.lobby.personal_missions.personal_missions_rewards_view_model import CompletedQuestsType
from gui.impl.lobby import promo_code_reward_screen
from gui.impl.lobby.promo_code_reward_screen import REWARDS_SOURCE_INVOICE, REWARDS_SOURCE_BATTLE_RESULTS, REWARDS_SOURCE_TOKEN_QUESTS
from gui.shared.account_settings_helper import AccountSettingsHelper
import personal_missions, th_async
from PlayerEvents import g_playerEvents
from account_helpers.AccountSettings import AccountSettings, RANKED_CURRENT_AWARDS_BUBBLE_YEAR_REACHED, RANKED_YEAR_POSITION, SPEAKERS_DEVICE, PersonalMissions
from account_helpers.settings_core.settings_constants import SOUND
from adisp import adisp_process
from battle_pass_common import BattlePassRewardReason, get3DStyleProgressToken
from chat_shared import SYS_MESSAGE_TYPE
from collector_vehicle import CollectorVehicleConsts
from comp7_common import Comp7QuestType, COMP7_QUALIFICATION_QUEST_ID, COMP7_TOKEN_COUPON_REWARD_ID
from constants import DOSSIER_TYPE, EVENT_TYPE, INVOICE_ASSET, ARENA_BONUS_TYPE, SUBSCRIPTION_ENTITLEMENT
from dossiers2.custom.records import DB_ID_TO_RECORD
from dossiers2.ui.achievements import BADGES_BLOCK
from dossiers2.ui.layouts import PERSONAL_MISSIONS_GROUP
from gui import DialogsInterface, SystemMessages
from gui.DialogsInterface import showPunishmentDialog
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
from gui.Scaleform.framework.entities.View import ViewKey
from gui.Scaleform.framework.managers.loaders import SFViewLoadParams
from gui.Scaleform.framework.managers.view_lifecycle_watcher import IViewLifecycleHandler, ViewLifecycleWatcher
from gui.Scaleform.locale.MESSENGER import MESSENGER
from gui.Scaleform.locale.SYSTEM_MESSAGES import SYSTEM_MESSAGES
from gui.awards.event_dispatcher import showDynamicAward
from gui.battle_pass.battle_pass_constants import MIN_LEVEL
from gui.battle_pass.battle_pass_helpers import getStyleInfoForChapter
from gui.battle_pass.state_machine.state_machine_helpers import packStartEvent, packToken, defaultEventMethod, multipleBattlePassPurchasedEventMethod
from gui.customization.shared import checkIsFirstProgressionDecalOnVehicle
from gui.gold_fish import isGoldFishActionActive, isTimeToShowGoldFishPromo
from gui.impl.auxiliary.rewards_helper import getProgressiveRewardBonuses
from gui.impl.gen import R
from gui.impl.gen.view_models.views.loot_box_view.loot_congrats_types import LootCongratsTypes
from gui.impl.lobby.early_access.early_access_window_events import showEarlyAccessRewardsView
from gui.impl.lobby.awards.items_collection_provider import MultipleAwardRewardsMainPacker
from gui.impl.lobby.comp7.comp7_quest_helpers import isComp7VisibleQuest, getComp7QuestType, parseComp7RanksQuestID, parseComp7TokensQuestID
from gui.impl.lobby.mapbox.map_box_awards_view import MapBoxAwardsViewWindow
from gui.impl.lobby.personal_missions.personal_missions_window_events import showPersonalMissionsRewardsView
from gui.impl.lobby.personal_missions.personal_missions_window_events import showOperationAdditionRewardsView
from gui.impl.pub.notification_commands import WindowNotificationCommand
from gui.limited_ui.lui_rules_storage import LuiRules
from gui.prb_control.entities.listener import IGlobalListener
from gui.ranked_battles import ranked_helpers
from gui.ranked_battles.constants import YEAR_AWARD_SELECTABLE_OPT_DEVICE_PREFIX
from gui.server_events import awards, events_dispatcher as quests_events, recruit_helper
from gui.server_events.bonuses import getServiceBonuses, getMergedBonusesFromDicts
from gui.server_events.events_dispatcher import showCurrencyReserveAwardWindow, showLootboxesAward, showMissionsBattlePass, showSubscriptionAwardWindow
from gui.server_events.events_helpers import isACEmailConfirmationQuest, isDailyQuest
from gui.server_events.finders import CHAMPION_BADGES_BY_BRANCH, CHAMPION_BADGE_AT_OPERATION_ID, PM_FINAL_TOKEN_QUEST_IDS_BY_OPERATION_ID, getBranchByOperationId, BRANCH_TO_OPERATION_IDS
from gui.shared import EVENT_BUS_SCOPE, events, g_eventBus
from gui.shared import event_dispatcher
from gui.shared.event_dispatcher import showBadgeInvoiceAwardWindow, showBattlePassAwardsWindow, showBattlePassVehicleAwardWindow, showDedicationRewardWindow, showEliteWindow, showMultiAwardWindow, showProgressionRequiredStyleUnlockedWindow, showProgressiveItemsRewardWindow, showProgressiveRewardAwardWindow, showRankedSeasonCompleteView, showRankedSelectableReward, showRankedYearAwardWindow, showRankedYearLBAwardWindow, showResourceWellAwardWindow, showSeniorityRewardAwardWindow, showBlankGiftWindow, showCollectionAwardsWindow, showParagonsRewardsWindow, showDailyEpicQuestRewardWindow, showPromoCodeRewardScreen, showTelecomRewardsPage
from gui.impl.lobby.paragons.paragons_window_events import showVideoRewardView
from gui.shared.events import PersonalMissionsEvent
from gui.shared.gui_items.dossier.factories import getAchievementFactory
from gui.shared.money import ZERO_MONEY, Money, Currency
from gui.shared.system_factory import registerAwardControllerHandlers, collectAwardControllerHandlers
from gui.shared.utils import isPopupsWindowsOpenDisabled
from gui.shared.utils.requesters import REQ_CRITERIA
from gui.sounds.sound_constants import SPEAKERS_CONFIG
from gui.summer_sale.video_reward_handler import tryShowWithVideoReward
from helpers import dependency, i18n
from items import ITEM_TYPE_INDICES, vehicles as vehicles_core
from items.components.crew_books_constants import CREW_BOOK_DISPLAYED_AWARDS_COUNT
from messenger.m_constants import SCH_CLIENT_MSG_TYPE
from messenger.proto.events import g_messengerEvents
from nations import NAMES
from personal_missions_constants import PM3_PREFIX_NAME, PM3_FINAL_REWARD_VIEW_ID
from paragons_common import PARAGONS_SELECTED_REWARD_TOKEN_PREFIX, getAllParagonsEntitlements
from renewable_subscription_common.settings_constants import WotPlusState
from shared_utils import first, findFirst
from skeletons.account_helpers.settings_core import ISettingsCore
from skeletons.gui.app_loader import IAppLoader
from skeletons.gui.battle_matters import IBattleMattersController
from skeletons.gui.game_control import IAwardController, IBattlePassController, IBootcampController, ILimitedUIController, IMapboxController, IRankedBattlesController, ISeniorityAwardsController, ICollectionsSystemController, IWotPlusController, IEarlyAccessController, IComp7Controller, IPersonalMissionsController, IParagonsRewardsShopController, ISummerSaleController
from skeletons.gui.goodies import IGoodiesCache
from skeletons.gui.impl import IGuiLoader, INotificationWindowController
from skeletons.gui.platform.catalog_service_controller import IPurchaseCache
from skeletons.gui.server_events import IEventsCache
from skeletons.gui.shared import IItemsCache
from skeletons.gui.shared.utils import IHangarSpace
from skeletons.gui.sounds import ISoundsController
from skeletons.gui.system_messages import ISystemMessages
from personal_missions import PM_BRANCH
if typing.TYPE_CHECKING:
    from typing import Tuple, Union, Dict, Literal
    from messenger.proto.bw.wrappers import _ServiceChannelData
    from comp7_ranks_common import Comp7Division
    from gui.platform.catalog_service.controller import _PurchaseDescriptor
    from gui.server_events.event_items import TokenQuest, PersonalMission
_logger = logging.getLogger(__name__)

class QUEST_AWARD_POSTFIX(object):
    CREW_BOOKS = b'awardcrewbook'


_POPUP_RECORDS = b'popUpRecords'

class _NonOverlappingStarBehaviorDescr(object):
    __NON_OVERLAPPING_START_BEHAVIOR = ()

    @classmethod
    def hasAnyOverlap(cls):
        overlaps = list(AccountSettingsHelper.isWelcomeScreenShown(behavior) for behavior in cls.__NON_OVERLAPPING_START_BEHAVIOR)
        return any(not overlap for overlap in overlaps)

    def __set__(self, obj, value_):
        obj.wasBehaviorOnStart = value_
        return

    def __get__(self, obj, type=None):
        value = obj.wasBehaviorOnStart and self.hasAnyOverlap()
        obj.wasBehaviorOnStart = value
        return value


class _NonOverlappingViewsLifecycleHandler(IViewLifecycleHandler):
    __NON_OVERLAPPING_VIEWS = (
     VIEW_ALIAS.LOBBY_CUSTOMIZATION,)

    def __init__(self, postponeAwardsCallback, handlePostponedCallback):
        super(_NonOverlappingViewsLifecycleHandler, self).__init__([ViewKey(alias) for alias in self.__NON_OVERLAPPING_VIEWS])
        self.__openedViews = set()
        self.__postponeAwardsCallback = postponeAwardsCallback
        self.__handlePostponedCallback = handlePostponedCallback
        return

    def onViewCreated(self, view):
        self.__postponeAwardsCallback(True)
        self.__openedViews.add(view.key)
        return

    def onViewDestroyed(self, view):
        self.__openedViews.discard(view.key)
        if not self.__openedViews:
            self.__postponeAwardsCallback(False)
            self.__handlePostponedCallback()
        return


def _showDailyQuestEpicRewardScreen(quest, context):
    bonusesFromMissionAward = awards.EpicAward(quest, context, None).getAwards()
    if bonusesFromMissionAward:
        showProgressiveRewardAwardWindow(bonusesFromMissionAward, LootCongratsTypes.INIT_CONGRAT_TYPE_EPIC_REWARDS, 0)
    return


def _showACEmailConfirmedRewardScreen(quest, context):
    missionAwards = awards.MissionAward(quest, context, None).getAwards()
    if missionAwards:
        showProgressiveRewardAwardWindow(missionAwards, LootCongratsTypes.INIT_CONGRAT_TYPE_AC_EMAIL_CONFIRMATION, 0)
    else:
        _logger.warning(b'Empty mission [%s] awards.', quest.getID())
    return


def _getBlueprintActualBonus(data, quest):
    questData = data.get(b'detailedRewards', {}).get(quest.getID(), {})
    if b'blueprints' in questData:
        blueprintActualBonus = questData.get(b'blueprints', {})
        actualQuest = deepcopy(quest)
        actualQuest.getData()[b'bonus'].update({b'blueprints': blueprintActualBonus})
        return actualQuest
    return quest


class AwardController(IAwardController, IGlobalListener):
    appLoader = dependency.descriptor(IAppLoader)
    bootcampController = dependency.descriptor(IBootcampController)
    eventsCache = dependency.descriptor(IEventsCache)
    settingsCore = dependency.descriptor(ISettingsCore)
    hasBehaviorOnStart = _NonOverlappingStarBehaviorDescr()

    def __init__(self):
        super(AwardController, self).__init__()
        self.__handlers = []
        self.__delayedHandlers = []
        self.__isLobbyLoaded = False
        self.__postpone = False
        self.__viewLifecycleWatcher = ViewLifecycleWatcher()
        self.hasBehaviorOnStart = False
        return

    def init(self):
        handlers = collectAwardControllerHandlers()
        self.__handlers = [handler(self) for handler in handlers]
        for handler in self.__handlers:
            handler.init()

        return

    def fini(self):
        for handler in self.__handlers:
            handler.fini()

        return

    def postponeOrCall(self, handler, ctx):
        if self.canShow():
            handler(ctx)
        else:
            _logger.debug(b'Postponed award call: %s, %s', handler, ctx)
            self.__delayedHandlers.insert(0 if isinstance(handler, BattlePassRewardHandler) else len(self.__delayedHandlers), (handler, ctx))
        return

    def handlePostponed(self, *_):
        while self.canShow() and self.__delayedHandlers:
            handler, ctx = self.__delayedHandlers.pop()
            _logger.debug(b'Calling postponed award handler: %s, %s', handler, ctx)
            handler(ctx)

        return

    def canShow(self):
        if self.__postpone:
            return False
        else:
            if self.__isLobbyLoaded:
                if self.hasBehaviorOnStart:
                    return False
                popupsWindowsDisabled = isPopupsWindowsOpenDisabled() or self.bootcampController.isInBootcamp()
                prbDispatcher = self.prbDispatcher
                if prbDispatcher is None:
                    return not popupsWindowsDisabled
                return not popupsWindowsDisabled and not prbDispatcher.getFunctionalState().hasLockedState
            return self.__isLobbyLoaded

    def onAvatarBecomePlayer(self):
        self.__isLobbyLoaded = False
        if self.hasBehaviorOnStart:
            self.hasBehaviorOnStart = False
            self.settingsCore.onSettingsChanged -= self.onSettingsChanged
        for handler in self.__handlers:
            handler.onAvatarBecomePlayer()

        self.stopGlobalListening()
        return

    def onAccountBecomeNonPlayer(self):
        self.hasBehaviorOnStart = False
        return

    def onConnected(self):
        bootcamp = self.bootcampController
        self.hasBehaviorOnStart = not bootcamp.isInBootcamp() and not bootcamp.isInBootcampAccount()
        return

    def onDisconnected(self):
        self.__isLobbyLoaded = False
        self.stopGlobalListening()
        if self.hasBehaviorOnStart:
            self.hasBehaviorOnStart = False
            self.settingsCore.onSettingsChanged -= self.onSettingsChanged
        for handler in self.__handlers:
            handler.stop()

        self.__viewLifecycleWatcher.stop()
        return

    def onLobbyInited(self, *args):
        self.startGlobalListening()
        self.__isLobbyLoaded = True
        if self.hasBehaviorOnStart:
            self.settingsCore.onSettingsChanged += self.onSettingsChanged
        self.handlePostponed()
        for handler in self.__handlers:
            handler.start()

        app = self.appLoader.getApp()
        handler = _NonOverlappingViewsLifecycleHandler(postponeAwardsCallback=self.__postponeAwards, handlePostponedCallback=self.handlePostponed)
        self.__viewLifecycleWatcher.start(app.containerManager, [handler])
        return

    def addMonitoredDynamicViewKey(self, viewKey):
        self.__viewLifecycleWatcher.addMonitoredDynamicViewKey(viewKey)
        return

    def onPlayerStateChanged(self, entity, roster, accountInfo):
        self.handlePostponed()
        return

    def onUnitFlagsChanged(self, flags, timeLeft):
        self.handlePostponed()
        return

    def onDequeued(self, queueType, *args):
        self.handlePostponed()
        return

    def onSettingsChanged(self, diff):
        if not self.hasBehaviorOnStart:
            self.settingsCore.onSettingsChanged -= self.onSettingsChanged
            self.handlePostponed()
        return

    def __postponeAwards(self, value):
        self.__postpone = value
        return


class AwardHandler(object):
    __metaclass__ = ABCMeta
    itemsCache = dependency.descriptor(IItemsCache)

    def __init__(self, awardCtrl):
        self._awardCtrl = weakref.proxy(awardCtrl)
        return

    def init(self):
        return

    def fini(self):
        return

    def start(self):
        return

    def stop(self):
        return

    def handle(self, *args):
        if self._needToShowAward(args):
            self._awardCtrl.postponeOrCall(self._showAward, args)
        return

    def isShowCongrats(self, quest):
        if quest:
            return quest.getData().get(b'showCongrats', False)
        return False

    def onAvatarBecomePlayer(self):
        return

    @abstractmethod
    def _needToShowAward(self, ctx):
        return

    @abstractmethod
    def _showAward(self, ctx):
        return


class ServiceChannelHandler(AwardHandler):
    eventsCache = dependency.descriptor(IEventsCache)

    def __init__(self, channelType, awardCtrl):
        super(ServiceChannelHandler, self).__init__(awardCtrl)
        self.__type = channelType
        return

    def init(self):
        g_messengerEvents.serviceChannel.onChatMessageReceived += self.handle
        return

    def fini(self):
        g_messengerEvents.serviceChannel.onChatMessageReceived -= self.handle
        return

    def _needToShowAward(self, ctx):
        _, message = ctx
        return message is not None and message.type == self.__type and message.data is not None and message.data


class MultiTypeServiceChannelHandler(ServiceChannelHandler):

    def __init__(self, handledTypes, awardCtrl):
        super(MultiTypeServiceChannelHandler, self).__init__(None, awardCtrl)
        self.__types = handledTypes
        return

    def _needToShowAward(self, ctx):
        _, message = ctx
        return message is not None and message.type in self.__types and message.data is not None

    def _showAward(self, ctx):
        return


class EliteWindowHandler(AwardHandler):
    __gui = dependency.descriptor(IGuiLoader)

    def init(self):
        g_playerEvents.onVehicleBecomeElite += self.handle
        return

    def fini(self):
        g_playerEvents.onVehicleBecomeElite -= self.handle
        return

    def _needToShowAward(self, ctx):
        return self.__gui.windowsManager.getViewByLayoutID(R.views.lobby.blueprints.blueprint_screen.blueprint_screen.BlueprintScreen()) is None

    def _showAward(self, ctx):
        if BigWorld.checkUnattended():
            return
        vehTypeCompDescrs = ctx
        for vehTypeCompDescr in vehTypeCompDescrs:
            showEliteWindow(vehTypeCompDescr)

        return


class PunishWindowHandler(ServiceChannelHandler):
    EXCLUDED_ARENA_BONUS_TYPES = [
     ARENA_BONUS_TYPE.BATTLE_ROYALE_SOLO, ARENA_BONUS_TYPE.BATTLE_ROYALE_SQUAD]

    def __init__(self, awardCtrl):
        super(PunishWindowHandler, self).__init__(SYS_MESSAGE_TYPE.battleResults.index(), awardCtrl)
        return

    def _showAward(self, ctx):
        _, message = ctx
        arenaTypeID = message.data.get(b'arenaTypeID', 0)
        if arenaTypeID > 0 and arenaTypeID in ArenaType.g_cache:
            arenaType = ArenaType.g_cache[arenaTypeID]
        else:
            arenaType = None
        arenaCreateTime = message.data.get(b'arenaCreateTime', None)
        fairplayViolations = message.data.get(b'fairplayViolations', None)
        bonusType = message.data.get(b'bonusType')
        if arenaCreateTime and arenaType and bonusType not in self.EXCLUDED_ARENA_BONUS_TYPES and fairplayViolations is not None and fairplayViolations[:2] != (0, 0):
            banDuration = message.data[b'restriction'][1] if b'restriction' in message.data else None
            showPunishmentDialog(arenaType, arenaCreateTime, fairplayViolations, banDuration)
        return


class PersonalMissionBonusHandler(ServiceChannelHandler):

    def __init__(self, awardCtrl):
        super(PersonalMissionBonusHandler, self).__init__(SYS_MESSAGE_TYPE.pmQuestBonus.index(), awardCtrl)
        return

    def _showAward(self, ctx):
        _logger.debug(b'Show personal mission bonus award! %s', ctx)
        data = ctx[1].data
        achievements = []
        for recordIdx, value in data.get(_POPUP_RECORDS, []):
            factory = getAchievementFactory(DB_ID_TO_RECORD[recordIdx])
            if factory is not None:
                a = factory.create(value=int(value))
                if a is not None:
                    achievements.append(a)

        if achievements:
            quests_events.showAchievementsAward(achievements)
        return


class PersonalMissionWindowAfterBattleHandler(ServiceChannelHandler):

    def __init__(self, awardCtrl):
        super(PersonalMissionWindowAfterBattleHandler, self).__init__(SYS_MESSAGE_TYPE.battleResults.index(), awardCtrl)
        return

    def _showAward(self, ctx):
        achievements = []
        popUpRecords = ctx[1].data.get(_POPUP_RECORDS, [])
        for recordIdx, value in popUpRecords:
            recordName = DB_ID_TO_RECORD[recordIdx]
            if recordName in PERSONAL_MISSIONS_GROUP:
                factory = getAchievementFactory(recordName)
                if factory is not None:
                    a = factory.create(value=int(value))
                    if a is not None:
                        achievements.append(a)

        if achievements:
            quests_events.showAchievementsAward(achievements)
        return


class TokenQuestsWindowHandler(ServiceChannelHandler):
    seniorityAwardCtrl = dependency.descriptor(ISeniorityAwardsController)

    def __init__(self, awardCtrl):
        super(TokenQuestsWindowHandler, self).__init__(SYS_MESSAGE_TYPE.tokenQuests.index(), awardCtrl)
        return

    def _showAward(self, ctx):
        data = ctx[1].data
        completedQuests = {}
        allQuests = self.eventsCache.getAllQuests(includePersonalMissions=True)
        seniorityQuestPrefix = self.seniorityAwardCtrl.seniorityQuestPrefix
        for qID in data.get(b'completedQuestIDs', set()):
            if qID in allQuests:
                if self.isShowCongrats(allQuests[qID]):
                    vehiclesList = data.get(b'detailedRewards', {}).get(qID, {}).get(b'vehicles', [])
                    vehiclesDict = vehiclesList[0] if vehiclesList else {}
                    windowCtx = {b'eventsCache': (self.eventsCache), b'bonusVehicles': vehiclesDict}
                    currentQuest = allQuests[qID]
                    blueprintDict = data.get(b'detailedRewards', {}).get(qID, {}).get(b'blueprints', {})
                    currentQuest = _getBlueprintActualBonus(blueprintDict, currentQuest)
                    if not seniorityQuestPrefix or seniorityQuestPrefix not in qID:
                        completedQuests[qID] = (
                         currentQuest, windowCtx)

        for quest, context in completedQuests.itervalues():
            if isDailyQuest(str(quest.getID())):
                continue
            elif isACEmailConfirmationQuest(quest.getID()):
                _showACEmailConfirmedRewardScreen(quest, context)
            else:
                self._showWindow(quest, context)

        return

    @staticmethod
    def _showWindow(quest, context):
        quests_events.showMissionAward(quest, context)
        return


class SeniorityAwardsWindowHandler(ServiceChannelHandler):
    itemsCache = dependency.descriptor(IItemsCache)
    eventsCache = dependency.descriptor(IEventsCache)
    seniorityAwardCtrl = dependency.descriptor(ISeniorityAwardsController)

    def __init__(self, awardCtrl):
        super(SeniorityAwardsWindowHandler, self).__init__(SYS_MESSAGE_TYPE.tokenQuests.index(), awardCtrl)
        self.__completedQuests = None
        self.__mergedRewards = None
        self.__questsData = None
        self.__callback = None
        return

    def fini(self):
        self.__completedQuests = None
        self.eventsCache.onSyncCompleted -= self.__onEventCacheSyncCompleted
        self.seniorityAwardCtrl.onUpdated -= self.__onSAConfigReady
        super(SeniorityAwardsWindowHandler, self).fini()
        return

    def _needToShowAward(self, ctx):
        if ctx == (None,):
            return self.__update()
        else:
            _, message = ctx
            if not super(SeniorityAwardsWindowHandler, self)._needToShowAward(ctx):
                return False
            data = message.data
            seniorityQuestPrefix = self.seniorityAwardCtrl.seniorityQuestPrefix
            if not seniorityQuestPrefix:
                self.seniorityAwardCtrl.onUpdated += self.__onSAConfigReady
                return False
            completedQuests = tuple(qID for qID in data.get(b'completedQuestIDs', set()) if qID.startswith(seniorityQuestPrefix))
            if completedQuests:
                self.__completedQuests = completedQuests
                self.__questsData = data
                return self.__update()
            return False

    def _showAward(self, ctx=None):
        if self.__mergedRewards:
            self.seniorityAwardCtrl.markRewardReceived()
            showSeniorityRewardAwardWindow(self.__completedQuests, self.__mergedRewards)
            self.__mergedRewards = None
            self.__questsData = None
            self.__completedQuests = None
        return

    def __update(self):
        if self.__questsData:
            allQuests = self.eventsCache.getAllQuests()
            detailedRewards = self.__questsData.get(b'detailedRewards', {})
            rewards = list(detailedRewards.get(qID, {}) for qID in self.__completedQuests if self.isShowCongrats(allQuests.get(qID)))
            if rewards:
                self.__mergedRewards = getMergedBonusesFromDicts(rewards)
                return True
            self.eventsCache.onSyncCompleted += self.__onEventCacheSyncCompleted
        return False

    def __onSAConfigReady(self):
        self.seniorityAwardCtrl.onUpdated -= self.__onSAConfigReady
        if self.seniorityAwardCtrl.seniorityQuestPrefix:
            self.handle(None)
        return

    def __onEventCacheSyncCompleted(self, *_):
        self.eventsCache.onSyncCompleted -= self.__onEventCacheSyncCompleted
        allQuests = self.eventsCache.getAllQuests()
        if self.__completedQuests and all(qID in allQuests for qID in self.__completedQuests):
            self.handle(None)
        return


class LootBoxByInvoiceHandler(ServiceChannelHandler):
    itemsCache = dependency.descriptor(IItemsCache)
    appLoader = dependency.descriptor(IAppLoader)

    def __init__(self, awardCtrl):
        super(LootBoxByInvoiceHandler, self).__init__(SYS_MESSAGE_TYPE.invoiceReceived.index(), awardCtrl)
        return

    def _showAward(self, ctx):
        invoiceData = ctx[1].data
        lootBoxes = {}
        if invoiceData.get(b'assetType', None) == INVOICE_ASSET.DATA and b'data' in invoiceData and b'tokens' in invoiceData[b'data']:
            tokensDict = invoiceData[b'data'][b'tokens']
            boxes = self.itemsCache.items.tokens.getLootBoxes()
            for tokenName, tokenData in tokensDict.iteritems():
                count = tokenData.get(b'count', 0)
                if count > 0 and tokenName in boxes:
                    lootbox = boxes[tokenName]
                    lootboxType = lootbox.getType()
                    if lootboxType not in lootBoxes:
                        lootBoxes[lootboxType] = {b'count': count, b'userName': (lootbox.getUserName()), 
                           b'isFree': (lootbox.isFree())}
                    else:
                        lootBoxes[lootboxType][b'count'] += count

        if lootBoxes:
            self._showWindow(lootBoxes)
        return

    @classmethod
    def _showWindow(cls, lootBoxes):
        for lootBoxType, lootBoxInfo in lootBoxes.iteritems():
            lootboxesCount = lootBoxInfo.get(b'count', 0)
            app = cls.appLoader.getApp()
            view = app.containerManager.getViewByKey(ViewKey(VIEW_ALIAS.LOBBY_HANGAR))
            if view is not None:
                showLootboxesAward(lootboxId=lootBoxType, lootboxCount=lootboxesCount, isFree=lootBoxInfo[b'isFree'])

        return


class PiggyBankOpenHandler(ServiceChannelHandler):
    itemsCache = dependency.descriptor(IItemsCache)

    def __init__(self, awardCtrl):
        super(PiggyBankOpenHandler, self).__init__(SYS_MESSAGE_TYPE.piggyBankSmashed.index(), awardCtrl)
        return

    def _showAward(self, ctx):
        if ctx[1].data:
            data = ctx[1].data
            creditsEarned = data.get(b'credits', 0)
            goldEarned = data.get(b'gold', 0)
            if creditsEarned or goldEarned:
                showCurrencyReserveAwardWindow(creditsEarned, goldEarned)
        return


class RenewableSubscriptionHandler(ServiceChannelHandler):
    subscriptionCtrl = dependency.descriptor(IWotPlusController)

    def __init__(self, awardCtrl):
        super(RenewableSubscriptionHandler, self).__init__(SYS_MESSAGE_TYPE.wotPlusUnlocked.index(), awardCtrl)
        return

    def _showAward(self, ctx):
        self.__showArwardScren()
        return

    @adisp_process
    def __showArwardScren(self):
        yield self.subscriptionCtrl.synchronize()
        showSubscriptionAwardWindow()
        return


class MarkByInvoiceHandler(ServiceChannelHandler):

    def __init__(self, awardCtrl):
        super(MarkByInvoiceHandler, self).__init__(SYS_MESSAGE_TYPE.invoiceReceived.index(), awardCtrl)
        return

    def _showAward(self, ctx):
        invoiceData = ctx[1].data
        totalCount = 0
        if invoiceData.get(b'assetType') == INVOICE_ASSET.DATA:
            if b'data' in invoiceData:
                data = invoiceData[b'data']
                if b'tokens' in data:
                    tokensDict = data[b'tokens']
                    for tokenName, tokenData in tokensDict.iteritems():
                        if tokenName.startswith(b'img:'):
                            totalCount += tokenData.get(b'count', 0)

        if totalCount:
            self._showMessage(totalCount)
        return

    @staticmethod
    def _showMessage(tokenCount):
        SystemMessages.pushI18nMessage(SYSTEM_MESSAGES.TOKENS_NOTIFICATION_MARK_ACQUIRED, count=tokenCount, type=SystemMessages.SM_TYPE.tokenWithMarkAcquired)
        return


class MarkByQuestHandler(MultiTypeServiceChannelHandler):

    def __init__(self, awardCtrl):
        super(MarkByQuestHandler, self).__init__((
         SYS_MESSAGE_TYPE.battleResults.index(), SYS_MESSAGE_TYPE.tokenQuests.index()), awardCtrl)
        return

    def _showAward(self, ctx):
        _, message = ctx
        tokenCount = self.__extractCount(message)
        if tokenCount > 0:
            self.__showMessage(tokenCount)
        return

    def __showMessage(self, tokenCount):
        SystemMessages.pushI18nMessage(SYSTEM_MESSAGES.TOKENS_NOTIFICATION_MARK_ACQUIRED, count=tokenCount, type=SystemMessages.SM_TYPE.tokenWithMarkAcquired)
        return

    @staticmethod
    def __extractCount(message):
        totalCounts = 0
        tokensDict = message.data.get(b'tokens', {})
        for tokenName, tokenData in tokensDict.iteritems():
            if tokenName.startswith(b'img:'):
                totalCounts += tokenData.get(b'count', 0)

        return totalCounts


class RecertificationFormHandler(MultiTypeServiceChannelHandler):
    goodiesCache = dependency.descriptor(IGoodiesCache)
    itemsCache = dependency.descriptor(IItemsCache)
    QUEST_PREFIX = b'Crew22_'
    BATTLES_AMOUNT = 100

    @classmethod
    def checkBattlesCount(cls):
        return cls.itemsCache.items.getAccountDossier().getTotalStats().getBattlesCount() >= cls.BATTLES_AMOUNT

    def __init__(self, awardCtrl):
        super(RecertificationFormHandler, self).__init__((
         SYS_MESSAGE_TYPE.battleResults.index(), SYS_MESSAGE_TYPE.tokenQuests.index()), awardCtrl)
        self._handledQIDs = set()
        return

    def fini(self):
        self._handledQIDs = set()
        super(RecertificationFormHandler, self).fini()
        return

    def _needToShowAward(self, ctx):
        _, message = ctx
        res = super(RecertificationFormHandler, self)._needToShowAward(ctx)
        if res:
            completedQuestIDs = message.data.get(b'completedQuestIDs', set())
            completedQuestIDs.update(message.data.get(b'rewardsGottenQuestIDs', set()))
            res = res and b'goodies' in message.data
            qID = findFirst((lambda x: x.startswith(self.QUEST_PREFIX) and x not in self._handledQIDs), completedQuestIDs, None)
            res = res and qID is not None
            if res:
                self._handledQIDs.add(qID)
        return res

    def _showAward(self, ctx):
        _, message = ctx
        blanksInAccount = self.goodiesCache.getRecertificationForms(REQ_CRITERIA.RECERTIFICATION_FORM.IN_ACCOUNT | REQ_CRITERIA.RECERTIFICATION_FORM.IS_ENABLED)
        if self.checkBattlesCount():
            for itemID, data in message.data.get(b'goodies', {}).iteritems():
                if itemID in blanksInAccount:
                    showBlankGiftWindow(itemID, data[b'count'])
                    break
            else:
                _logger.warning(b'This code should not be reached')

        return


class CrewBooksQuestHandler(MultiTypeServiceChannelHandler):

    def __init__(self, awardCtrl):
        super(CrewBooksQuestHandler, self).__init__((
         SYS_MESSAGE_TYPE.battleResults.index(), SYS_MESSAGE_TYPE.tokenQuests.index()), awardCtrl)
        self._qId = None
        return

    def _needToShowAward(self, ctx):

        def isCrewBook(intCD):
            itemTypeID, _, _ = vehicles_core.parseIntCompactDescr(intCD)
            return itemTypeID == ITEM_TYPE_INDICES[b'crewBook']

        _, message = ctx
        res = super(CrewBooksQuestHandler, self)._needToShowAward(ctx)
        if res:
            questIDs = message.data.get(b'completedQuestIDs', set())
            res = res and b'items' in message.data
            res = res and any(isCrewBook(intCD) for intCD in message.data[b'items'].iterkeys())
            self._qId = next(ifilter((lambda x: x.endswith(QUEST_AWARD_POSTFIX.CREW_BOOKS)), questIDs), None)
            res = res and self._qId is not None
        return res

    def _showAward(self, ctx):
        _, message = ctx
        questData = message.data.get(b'detailedRewards', {}).get(self._qId, {})
        bonuses, _ = getProgressiveRewardBonuses(questData, maxAwardCount=CREW_BOOK_DISPLAYED_AWARDS_COUNT)
        if bonuses:
            showProgressiveRewardAwardWindow(bonuses, LootCongratsTypes.INIT_CONGRAT_TYPE_CREW_BOOKS, 0)
        else:
            _logger.error(b"Can't show empty or invalid reward!")
        return


class RecruitHandler(ServiceChannelHandler):

    def __init__(self, awardCtrl):
        super(RecruitHandler, self).__init__(SYS_MESSAGE_TYPE.tokenQuests.index(), awardCtrl)
        self.__questTypes = [
         SYS_MESSAGE_TYPE.battleResults.index(),
         SYS_MESSAGE_TYPE.tokenQuests.index(),
         SYS_MESSAGE_TYPE.invoiceReceived.index(),
         SYS_MESSAGE_TYPE.converter.index()]
        return

    def _needToShowAward(self, ctx):
        _, message = ctx
        return message is not None and message.type in self.__questTypes and message.data is not None

    def _showAward(self, ctx):
        messageData = ctx[1].data
        if b'data' in messageData:
            data = messageData[b'data']
        else:
            data = messageData
        tokensDict = data.get(b'tokens', {})
        for tokenName in tokensDict:
            recruitInfo = recruit_helper.getRecruitInfo(tokenName)
            if recruitInfo is not None:
                self._showWindow(recruitInfo.getEventName())
                return

        return

    @staticmethod
    def _showWindow(eventKey):
        event = i18n.makeString(eventKey)
        SystemMessages.pushMessage(i18n.makeString(MESSENGER.SERVICECHANNELMESSAGES_RECRUITGIFT_TEXT, event=event), SystemMessages.SM_TYPE.RecruitGift, messageData={b'header': (i18n.makeString(MESSENGER.SERVICECHANNELMESSAGES_RECRUITGIFT_HEADER))})
        return


class MotiveQuestsWindowHandler(ServiceChannelHandler):

    def __init__(self, awardCtrl):
        super(MotiveQuestsWindowHandler, self).__init__(SYS_MESSAGE_TYPE.battleResults.index(), awardCtrl)
        return

    def _showAward(self, ctx):
        data = ctx[1].data
        motiveQuests = self.eventsCache.getMotiveQuests()
        for qID in data.get(b'completedQuestIDs', set()):
            if qID in motiveQuests and self.isShowCongrats(motiveQuests[qID]):
                quests_events.showMotiveAward(motiveQuests[qID])

        return


class BattleQuestsAutoWindowHandler(MultiTypeServiceChannelHandler):
    _BRANCHES_SHOW_ORDER = {(personal_missions.PM_BRANCH.PERSONAL_MISSION_3): 1, 
       (personal_missions.PM_BRANCH.PERSONAL_MISSION_2): 2, 
       (personal_missions.PM_BRANCH.REGULAR): 3}

    def __init__(self, awardCtrl):
        super(BattleQuestsAutoWindowHandler, self).__init__((
         SYS_MESSAGE_TYPE.battleResults.index(), SYS_MESSAGE_TYPE.personalMissionRebalance.index()), awardCtrl)
        return

    def _showAward(self, ctx):
        _, message = ctx
        completedQuests = {}
        allQuests = self.eventsCache.getAllQuests(includePersonalMissions=True, filterFunc=self._isAppropriate)
        completedQuestUniqueIDs = message.data.get(b'completedQuestIDs', set())
        for uniqueQuestID in completedQuestUniqueIDs:
            questID, ctx = self._getContext(uniqueQuestID, completedQuests, completedQuestUniqueIDs)
            if questID in allQuests:
                quest = allQuests[questID]
                if self.isShowCongrats(quest):
                    vehiclesList = message.data.get(b'detailedRewards', {}).get(questID, {}).get(b'vehicles', [])
                    vehiclesDict = vehiclesList[0] if vehiclesList else {}
                    ctx.update({b'eventsCache': (self.eventsCache), b'bonusVehicles': vehiclesDict})
                    blueprintDict = message.data.get(b'detailedRewards', {}).get(questID, {}).get(b'blueprints', {})
                    quest = _getBlueprintActualBonus(blueprintDict, quest)
                    completedQuests[questID] = (quest, ctx)

        values = sorted(completedQuests.values(), key=self.__questShowOrderKey)
        for quest, context in values:
            if isDailyQuest(str(quest.getID())):
                continue
            else:
                self._showWindow(quest, context)

        return

    @staticmethod
    def _showWindow(quest, context):
        quests_events.showMissionAward(quest, context)
        return

    @staticmethod
    def _isAppropriate(quest):
        return quest.getType() in (EVENT_TYPE.BATTLE_QUEST, EVENT_TYPE.TOKEN_QUEST,
         EVENT_TYPE.PERSONAL_QUEST, EVENT_TYPE.RANKED_QUEST)

    @staticmethod
    def _getContext(uniqueQuestID, completedQuests, completedQuestUniqueIDs):
        return (
         uniqueQuestID, {})

    def __questShowOrderKey(self, completedQuest):
        quest, _ = completedQuest
        questId = quest.getID()
        missionsCache = personal_missions.g_cache
        if missionsCache.hasMission(questId):
            branchType = missionsCache.questByPMQuestID(questId).branch
            return self._BRANCHES_SHOW_ORDER.get(branchType, questId)
        return questId


class PersonalMissionAutoWindowHandler(BattleQuestsAutoWindowHandler):
    __pmController = dependency.descriptor(IPersonalMissionsController)

    def __init__(self, awardCtrl):
        super(PersonalMissionAutoWindowHandler, self).__init__(awardCtrl)
        self.__completedQuestsPm3 = list()
        self.__completedQuestsPm1_2 = list()
        self.__currentQuestData = None
        self.__openedRewardQuestsIds = set()
        self.__openedRewardOperationsIds = set()
        return

    def init(self):
        super(PersonalMissionAutoWindowHandler, self).init()
        g_eventBus.addListener(PersonalMissionsEvent.ON_AWARD_PM_SCREEN_CLOSE, self.__onRewardsPmViewClose, EVENT_BUS_SCOPE.LOBBY)
        return

    def fini(self):
        self.eventsCache.onProgressUpdated -= self.__onShowAwardSyncCompleted
        g_eventBus.removeListener(PersonalMissionsEvent.ON_AWARD_PM_SCREEN_CLOSE, self.__onRewardsPmViewClose, EVENT_BUS_SCOPE.LOBBY)
        super(PersonalMissionAutoWindowHandler, self).fini()
        return

    def _showWindow(self, quest, context):
        windowData = {b'quest': quest, b'context': context}
        if quest.getQuestBranch() == personal_missions.PM_BRANCH.PERSONAL_MISSION_3:
            self.__completedQuestsPm3.append(windowData)
        else:
            self.__completedQuestsPm1_2.append(windowData)
        self.__tryShowWindow()
        return

    @staticmethod
    def _isAppropriate(quest):
        return quest.getType() == EVENT_TYPE.PERSONAL_MISSION

    @staticmethod
    def _getContext(uniqueQuestID, completedQuests, completedQuestUniqueIDs):
        if personal_missions.g_cache.isPersonalMission(uniqueQuestID):
            pmQuestType = personal_missions.g_cache.questByUniqueQuestID(uniqueQuestID)
            if pmQuestType.id not in completedQuests:
                ctx = {b'isMainReward': (pmQuestType.mainQuestID in completedQuestUniqueIDs), b'isAddReward': (pmQuestType.addQuestID in completedQuestUniqueIDs), 
                   b'awardListReturned': (uniqueQuestID.endswith(b'_add_award_list'))}
                return (
                 pmQuestType.id, ctx)
            if uniqueQuestID.endswith(b'_add_award_list'):
                _, ctx = completedQuests[pmQuestType.id]
                ctx.update(awardListReturned=True)
        return (
         None, {})

    def __showPM3Awards(self, quest, ctx):
        questId = quest.getID()
        showPersonalMissionsRewardsView(questId, viewType=self.__getCompletedQuestsType(quest, ctx), addToQueue=True)
        self.__updateCompletedOperationId(questId)
        return

    def __tryShowWindow(self):
        localCopyCompletedQuestsPm3 = self.__completedQuestsPm3[:]
        for dataWindow in localCopyCompletedQuestsPm3:
            quest = dataWindow[b'quest']
            context = dataWindow[b'context']
            if not quest.isCompleted() or context.get(b'isAddReward') and not quest.isFullCompleted():
                self.__currentQuestData = dataWindow
                self.eventsCache.onProgressUpdated += self.__onShowAwardSyncCompleted
                return
            self.__completedQuestsPm3.remove(dataWindow)
            self.__openedRewardQuestsIds.add(dataWindow[b'quest'].getID())
            self.__showPM3Awards(dataWindow[b'quest'], dataWindow[b'context'])

        localCopyCompletedQuestsPm1_2 = self.__completedQuestsPm1_2[:]
        for dataWindow in localCopyCompletedQuestsPm1_2:
            self.__completedQuestsPm1_2.remove(dataWindow)
            self.__openedRewardQuestsIds.add(dataWindow[b'quest'].getID())
            quests_events.showPersonalMissionAward(dataWindow[b'quest'], dataWindow[b'context'])

        return

    def __updateCompletedOperationId(self, questId):
        pmCtrl = self.__pmController
        quest = pmCtrl.getQuest(questId)
        if quest is None or quest.getQuestBranchName() != PM3_PREFIX_NAME:
            return
        operationID = quest.getOperationID()
        operation = pmCtrl.getOperationById(operationID)
        if operation is None or not operation.isCompleted():
            return
        settings = AccountSettings.getPersonalMissions(PersonalMissions.OPERATIONS_VIDEO_REWARDS_STATUS)
        if settings.get(operationID, False) and operation.isFullCompleted():
            self.__openedRewardOperationsIds.add(operationID)
            showOperationAdditionRewardsView(operationID, addToQueue=True)
        if not settings.get(operationID, False):
            self.__openedRewardOperationsIds.add(operationID)
            pmCtrl.openVideoRewardAndUpdateAccSettings(operationID, settings)
        if all(pmCtrl.getOperationById(operationId).isFullCompleted() for operationId in BRANCH_TO_OPERATION_IDS[personal_missions.PM_BRANCH.PERSONAL_MISSION_3]):
            self.__openedRewardOperationsIds.add(PM3_FINAL_REWARD_VIEW_ID)
            pmCtrl.openVideoRewardAndUpdateAccSettings(PM3_FINAL_REWARD_VIEW_ID, settings)
        AccountSettings.setPersonalMissions(PersonalMissions.OPERATIONS_VIDEO_REWARDS_STATUS, settings)
        return

    def __onRewardsPmViewClose(self, event):
        self.__getCloseEvent(questId=event.ctx.get(b'questID'), operationId=event.ctx.get(b'operationID'))
        return

    def __getCloseEvent(self, questId=None, operationId=None):
        if not self.__openedRewardQuestsIds and not self.__openedRewardOperationsIds:
            return
        else:
            if questId is not None:
                self.__openedRewardQuestsIds.discard(questId)
            if operationId is not None:
                self.__openedRewardOperationsIds.discard(operationId)
            if not (self.__openedRewardQuestsIds or self.__openedRewardOperationsIds):
                g_eventBus.handleEvent(PersonalMissionsEvent(PersonalMissionsEvent.ON_ALL_REWARDS_PM3_VIEW_CLOSE, ctx={}), scope=EVENT_BUS_SCOPE.LOBBY)
            return

    @staticmethod
    def __getCompletedQuestsType(quest, context):
        if not quest.isFinal():
            return CompletedQuestsType.COMPLETE_BASIC
        if context.get(b'isMainReward'):
            if context.get(b'isAddReward'):
                return CompletedQuestsType.COMPLETE_WITH_HONOR
            return CompletedQuestsType.COMPLETE
        return CompletedQuestsType.COMPLETE_ADD

    def __onShowAwardSyncCompleted(self, *_):
        dataWindow = self.__currentQuestData
        if dataWindow is None:
            self.eventsCache.onProgressUpdated -= self.__onShowAwardSyncCompleted
            return
        else:
            quest = dataWindow[b'quest']
            if not quest.isCompleted() or dataWindow[b'context'].get(b'isAddReward') and not quest.isFullCompleted():
                return
            self.eventsCache.onProgressUpdated -= self.__onShowAwardSyncCompleted
            self.__completedQuestsPm3.remove(dataWindow)
            self.__openedRewardQuestsIds.add(dataWindow[b'quest'].getID())
            self.__showPM3Awards(dataWindow[b'quest'], dataWindow[b'context'])
            self.__currentQuestData = None
            self.__tryShowWindow()
            return


class PersonalMissionByAwardListHandler(PersonalMissionAutoWindowHandler):

    def _needToShowAward(self, ctx):
        _, msg = ctx
        if msg is not None and isinstance(msg.data, types.DictType):
            completedQuestUniqueIDs = msg.data.get(b'completedQuestIDs', set())
            for uniqueQuestID in completedQuestUniqueIDs:
                if personal_missions.g_cache.isPersonalMission(uniqueQuestID) and uniqueQuestID.endswith(b'_main_award_list'):
                    return True

        return False

    @staticmethod
    def _getContext(uniqueQuestID, completedQuests, completedQuestUniqueIDs):
        if personal_missions.g_cache.isPersonalMission(uniqueQuestID):
            pmQuestType = personal_missions.g_cache.questByUniqueQuestID(uniqueQuestID)
            if pmQuestType.id not in completedQuests:
                ctx = {b'isMainReward': True, b'isAddReward': False, 
                   b'isAwardListUsed': True}
                return (
                 pmQuestType.id, ctx)
        return (
         None, {})


class PersonalMissionOperationAwardHandler(BattleQuestsAutoWindowHandler):
    __CHAMPION_BADGES_IDS = CHAMPION_BADGES_BY_BRANCH.values()
    __systemMessages = dependency.descriptor(ISystemMessages)

    def __init__(self, awardCtrl):
        super(PersonalMissionOperationAwardHandler, self).__init__(awardCtrl)
        self.__postponedAwards = []
        self.__openedOperationsAwards = set()
        self.__delayedWindows = {}
        return

    def init(self):
        super(PersonalMissionOperationAwardHandler, self).init()
        g_eventBus.addListener(PersonalMissionsEvent.ON_AWARD_SCEEN_CLOSE, self.__onAwardScreenClose, EVENT_BUS_SCOPE.LOBBY)
        return

    def fini(self):
        super(PersonalMissionOperationAwardHandler, self).fini()
        g_eventBus.removeListener(PersonalMissionsEvent.ON_AWARD_SCEEN_CLOSE, self.__onAwardScreenClose, EVENT_BUS_SCOPE.LOBBY)
        self.__delayedWindows.clear()
        self.__postponedAwards = []
        self.__openedOperationsAwards.clear()
        return

    def _needToShowAward(self, ctx):
        _, msg = ctx
        if msg is not None and isinstance(msg.data, types.DictType):
            completedQuestUniqueIDs = msg.data.get(b'completedQuestIDs', set())
            for uniqueQuestID in completedQuestUniqueIDs:
                if personal_missions.g_cache.isPersonalMission(uniqueQuestID):
                    pmQuestType = personal_missions.g_cache.questByUniqueQuestID(uniqueQuestID)
                    if pmQuestType.isFinal:
                        self.__openedOperationsAwards.add((pmQuestType.id, pmQuestType.tileID))
                for operationID, prefix in self.__getFinalTokenQuestIdsByOperationId():
                    if uniqueQuestID == CHAMPION_BADGES_BY_BRANCH[PM_BRANCH.PERSONAL_MISSION_3]:
                        return False
                    if uniqueQuestID in self.__CHAMPION_BADGES_IDS:
                        return True
                    if uniqueQuestID.startswith(prefix):
                        if operationID in CHAMPION_BADGE_AT_OPERATION_ID:
                            pmCache = self.eventsCache.getPersonalMissions()
                            operation = pmCache.getAllOperations()[operationID]
                            operations = pmCache.getOperationsForBranch(operation.getBranch())
                            if all([op.isFullCompleted() for op in operations.itervalues()]):
                                self.__postponedAwards.append(uniqueQuestID)
                            else:
                                return True
                        else:
                            return True

        return False

    def _showAward(self, ctx):
        _, message = ctx
        completedQuestIDs = message.data.get(b'completedQuestIDs', set())
        allQuests = self.eventsCache.getHiddenQuests()
        self.__sendSystemNotification(message)
        for operationId, prefix in self.__getFinalTokenQuestIdsByOperationId():
            quests = []
            for uniqueQuestID in completedQuestIDs:
                if (uniqueQuestID.startswith(prefix) or self.__isChampionBadgeQuest(uniqueQuestID, operationId)) and uniqueQuestID in allQuests:
                    quests.append(uniqueQuestID)

            if quests:
                ctx = {b'operationID': operationId, b'branch': (getBranchByOperationId(operationId)), 
                   b'questIds': (quests + self.__postponedAwards)}
                self._showWindow(None, ctx)
                self.__postponedAwards = []

        return

    def _showWindow(self, quest, context):
        opId = context[b'operationID']
        operations = [data[1] for data in self.__openedOperationsAwards]
        if opId not in operations:
            quests_events.showPersonalMissionsOperationAwardsScreen(context)
        else:
            self.__delayedWindows[opId] = context
        return

    @staticmethod
    def __isChampionBadgeQuest(qID, operationID):
        if operationID not in CHAMPION_BADGE_AT_OPERATION_ID:
            return False
        return qID == CHAMPION_BADGE_AT_OPERATION_ID[operationID]

    def __onAwardScreenClose(self, event):
        opID = event.ctx[b'operationID']
        eventID = event.ctx[b'eventID']
        if (eventID, opID) in self.__openedOperationsAwards:
            self.__openedOperationsAwards.discard((eventID, opID))
        operations = [data[1] for data in self.__openedOperationsAwards]
        if opID not in operations and opID in self.__delayedWindows:
            quests_events.showPersonalMissionsOperationAwardsScreen(self.__delayedWindows.pop(opID))
        return

    def __sendSystemNotification(self, message):
        completedQuestIDs = message.data.get(b'completedQuestIDs', set())
        lastPM3Operation = BRANCH_TO_OPERATION_IDS[personal_missions.PM_BRANCH.PERSONAL_MISSION_3][-1]
        pm3ChampionTokenQuestID = CHAMPION_BADGE_AT_OPERATION_ID[lastPM3Operation]
        if pm3ChampionTokenQuestID in completedQuestIDs:
            self.__systemMessages.proto.serviceChannel.pushClientMessage(message, SCH_CLIENT_MSG_TYPE.PM3_CAMPAIGN_COMPLETED_PERFECT, auxData=pm3ChampionTokenQuestID)
        return

    def __getFinalTokenQuestIdsByOperationId(self):
        return sorted(PM_FINAL_TOKEN_QUEST_IDS_BY_OPERATION_ID.items(), key=(lambda v: self._BRANCHES_SHOW_ORDER.get(getBranchByOperationId(v[0]))))


class PersonalMissionOperationUnlockedHandler(BattleQuestsAutoWindowHandler):
    OPERATION_COMPLETION_IDS = {b'pt_final_s1_t1': 1, 
       b'pt_final_s1_t2': 2, 
       b'pt_final_s1_t3': 3, 
       b'pt_final_s1_t4': 4, 
       b'pt_final_s2_t5': 5, 
       b'pt_final_s2_t6': 6, 
       b'pt_final_s2_t7': 7, 
       b'pt_final_s3_t8': 8, 
       b'pt_final_s3_t9': 9, 
       b'pt_final_s3_t10': 10}

    def _needToShowAward(self, ctx):
        _, msg = ctx
        if msg is not None and isinstance(msg.data, types.DictType):
            completedQuestUniqueIDs = msg.data.get(b'completedQuestIDs', set())
            for uniqueQuestID in completedQuestUniqueIDs:
                if uniqueQuestID in self.OPERATION_COMPLETION_IDS:
                    return True

        return False

    def _showAward(self, ctx):
        _, message = ctx
        allQuests = self.eventsCache.getHiddenQuests()
        operations = self.eventsCache.getPersonalMissions().getAllOperations()
        context = {b'eventsCache': (self.eventsCache)}
        completedQuestUniqueIDs = message.data.get(b'completedQuestIDs', set())
        for uniqueQuestID in (qID for qID in completedQuestUniqueIDs if qID in allQuests):
            for oCompletionID, oID in self.OPERATION_COMPLETION_IDS.iteritems():
                if uniqueQuestID == oCompletionID:
                    quest = allQuests[uniqueQuestID]
                    operation = operations[oID]
                    nextOperationIDs = operation.getNextOperationIDs()
                    for nextOperationID in nextOperationIDs:
                        ctx = {b'nextOperationID': nextOperationID}
                        ctx.update(context)
                        self._showWindow(quest, ctx)

        return

    @staticmethod
    def _showWindow(quest, context):
        quests_events.showOperationUnlockedAward(quest, context)
        return


class GoldFishHandler(AwardHandler):

    def start(self):
        self.handle()
        return

    def _needToShowAward(self, ctx):
        return True

    def _showAward(self, ctx):
        if isGoldFishActionActive() and isTimeToShowGoldFishPromo():
            g_eventBus.handleEvent(events.LoadViewEvent(SFViewLoadParams(VIEW_ALIAS.GOLD_FISH_WINDOW)), scope=EVENT_BUS_SCOPE.LOBBY)
        return


class TelecomHandler(ServiceChannelHandler):

    def __init__(self, awardCtrl):
        super(TelecomHandler, self).__init__(SYS_MESSAGE_TYPE.telecomOrderCreated.index(), awardCtrl)
        return

    @staticmethod
    def __getVehileDesrs(data):
        return [vehicles_core.getVehicleType(v).compactDescr for v in data[b'data'].get(b'vehicles', {})]

    def _showAward(self, ctx):
        data = ctx[1].data
        vehicleDesrs = self.__getVehileDesrs(data)
        if vehicleDesrs:
            showTelecomRewardsPage()
        else:
            _logger.debug(b'There is no vehicle in the award. Telecom award window not needed!')
        return


class RankedQuestsHandler(ServiceChannelHandler):
    __rankedController = dependency.descriptor(IRankedBattlesController)

    def __init__(self, awardCtrl):
        super(RankedQuestsHandler, self).__init__(SYS_MESSAGE_TYPE.tokenQuests.index(), awardCtrl)
        return

    def _showAward(self, ctx):
        _, message = ctx
        data = message.data.copy()
        seasonQuestIDs = []
        finalRewardsQuestIDs = []
        finalLeaderQuestIDs = []
        for questID in (h for h in data.get(b'completedQuestIDs', set()) if ranked_helpers.isRankedQuestID(h)):
            if ranked_helpers.isSeasonTokenQuest(questID):
                seasonQuestIDs.append(questID)
            elif ranked_helpers.isFinalTokenQuest(questID):
                finalRewardsQuestIDs.append(questID)
            elif ranked_helpers.isLeaderTokenQuest(questID):
                finalLeaderQuestIDs.append(questID)

        if seasonQuestIDs:
            self.__processQuests(seasonQuestIDs, data, self.__showSeasonAward)
        if finalRewardsQuestIDs:
            self.__showFinalAward(finalRewardsQuestIDs, data)
        if finalLeaderQuestIDs:
            self.__processQuests(finalLeaderQuestIDs, data, self.__showFinalLeaderAward)
        return

    def __showSeasonAward(self, quest, data):
        seasonID, league, _ = ranked_helpers.getDataFromSeasonTokenQuestID(quest.getID())
        season = self.__rankedController.getSeason(seasonID)
        if season is not None:
            showRankedSeasonCompleteView({b'quest': quest, b'awards': data}, True)
        else:
            _logger.error(b'Try to show RankedBattlesSeasonCompleteView, but season is None. Params: %s %s', seasonID, league)
        return

    def __showFinalAward(self, questIDs, data):
        points = ranked_helpers.getDataFromFinalTokenQuestID(first(questIDs))
        awardType = self.__rankedController.getAwardTypeByPoints(points)
        if awardType is not None:
            if any(token.startswith(YEAR_AWARD_SELECTABLE_OPT_DEVICE_PREFIX) for token in data.get(b'tokens', {}).keys()):
                AccountSettings.setSettings(RANKED_CURRENT_AWARDS_BUBBLE_YEAR_REACHED, False)
                showRankedSelectableReward()
            else:
                showRankedYearAwardWindow(data, self.__rankedController.getYearRewardPoints(), True)
        return

    def __showFinalLeaderAward(self, _, data):
        yearPosition = AccountSettings.getSettings(RANKED_YEAR_POSITION)
        if yearPosition is not None and data:
            showRankedYearLBAwardWindow(yearPosition, data, True)
        return

    def __processQuests(self, questIDs, data, handler):
        questID = questIDs[0]
        quest = self.eventsCache.getHiddenQuests().get(questID)
        if quest:
            questData = data.get(b'detailedRewards', {}).get(questID, {})
            handler(quest, questData)
        if len(questIDs) > 1:
            _logger.error(b'There can not be 2 or more quests with the same meaning at the same time')
        return


class SoundDeviceHandler(AwardHandler):
    soundsCtrl = dependency.descriptor(ISoundsController)
    settingsCore = dependency.descriptor(ISettingsCore)

    def start(self):
        self.handle()
        return

    def _needToShowAward(self, ctx):
        deviceSetting = self.settingsCore.options.getSetting(SOUND.SOUND_DEVICE)
        isValid, currentDeviceID = deviceSetting.getSystemState()
        if isValid:
            return False
        lastDeviceID = AccountSettings.getFilter(SPEAKERS_DEVICE)
        if currentDeviceID == lastDeviceID:
            return False
        return True

    def _showAward(self, ctx):
        DialogsInterface.showI18nConfirmDialog(b'soundSpeakersPresetReset', callback=self.__callback)
        return

    def __callback(self, result):
        deviceSetting = self.settingsCore.options.getSetting(SOUND.SOUND_DEVICE)
        if result:
            deviceSetting.apply(deviceSetting.SYSTEMS.SPEAKERS)
            self.soundsCtrl.system.setUserSpeakersPresetID(SPEAKERS_CONFIG.AUTO_DETECTION)
        else:
            _, currentDeviceID = deviceSetting.getSystemState()
            AccountSettings.setFilter(SPEAKERS_DEVICE, currentDeviceID)
        return


class ProgressiveRewardHandler(ServiceChannelHandler):

    def __init__(self, awardCtrl):
        super(ProgressiveRewardHandler, self).__init__(SYS_MESSAGE_TYPE.progressiveReward.index(), awardCtrl)
        return

    def _showAward(self, ctx):
        _, message = ctx
        bonuses, specialRewardType = getProgressiveRewardBonuses(message.data[b'rewards'])
        if bonuses:
            showProgressiveRewardAwardWindow(bonuses, specialRewardType, message.data[b'level'])
        else:
            _logger.error(b"Can't show empty or invalid reward!")
        return


class ParagonsLevelRewardsReceivedHandler(ServiceChannelHandler):
    __selectableRewardsCtrl = dependency.descriptor(IParagonsRewardsShopController)

    def __init__(self, awardCtrl):
        super(ParagonsLevelRewardsReceivedHandler, self).__init__(SYS_MESSAGE_TYPE.paragonsLevelRewardsReceived.index(), awardCtrl)
        return

    def _showAward(self, ctx):
        _, message = ctx
        rewardInfo = message.data.get(b'levelRewardsInfo', None)
        chapterID = message.data.get(b'chapterID', 1)
        entitlements = {}
        for _, info in rewardInfo.iteritems():
            if info.get(b'entitlements'):
                for entitlement in getAllParagonsEntitlements():
                    count = info.get(b'entitlements').get(entitlement, {}).get(b'count', 0)
                    if count > 0:
                        entitlements.update({entitlement: (count + entitlements.get(entitlement, 0))})

        if chapterID > 0 and entitlements:
            self.__selectableRewardsCtrl.entitlements.update()
            self.__selectableRewardsCtrl.entitlements.storeGranted(entitlements)
        for chapterLevel, levelRewards in sorted(rewardInfo.items()):
            showParagonsRewardsWindow(levelRewards, chapterID, chapterLevel)

        return


class ParagonsSelectableRewardReceivedHandler(ServiceChannelHandler):
    __selectableRewardsCtrl = dependency.descriptor(IParagonsRewardsShopController)

    def __init__(self, awardCtrl):
        super(ParagonsSelectableRewardReceivedHandler, self).__init__(SYS_MESSAGE_TYPE.invoiceReceived.index(), awardCtrl)
        return

    def _showAward(self, ctx):
        _, message = ctx
        invoiceData = ctx[1].data
        if invoiceData.get(b'assetType') == INVOICE_ASSET.PURCHASE:
            invoiceData = message.data.get(b'data', {})
            tokensDict = invoiceData.get(b'tokens', {})
            if any(token.startswith(PARAGONS_SELECTED_REWARD_TOKEN_PREFIX) for token in tokensDict):
                self.__selectableRewardsCtrl.selectableRewardReceived(invoiceData)
                vehicle = first(invoiceData.get(b'vehicles', []))
                if vehicle is not None:
                    showVideoRewardView(first(vehicle.keys()), None, (lambda : showParagonsRewardsWindow(invoiceData, isVehicleSelected=True, addToQueue=False)))
                else:
                    showParagonsRewardsWindow(invoiceData, addToQueue=False)
        return


class ProgressiveItemsRewardHandler(ServiceChannelHandler):
    _gui = dependency.descriptor(IGuiLoader)
    _hangarSpace = dependency.descriptor(IHangarSpace)
    _itemsCache = dependency.descriptor(IItemsCache)
    __limitedUIController = dependency.descriptor(ILimitedUIController)

    def __init__(self, awardCtrl):
        super(ProgressiveItemsRewardHandler, self).__init__(SYS_MESSAGE_TYPE.customizationProgress.index(), awardCtrl)
        self.__message = None
        return

    def fini(self):
        self._hangarSpace.onSpaceCreate -= self.__show
        super(ProgressiveItemsRewardHandler, self).fini()
        return

    def _showAward(self, ctx):
        if BigWorld.checkUnattended():
            return
        _, self.__message = ctx
        if self._hangarSpace.spaceInited:
            self.__show()
        else:
            self._hangarSpace.onSpaceCreate += self.__show
        return

    def __show(self):
        self._hangarSpace.onSpaceCreate -= self.__show
        if not self.__limitedUIController.isRuleCompleted(LuiRules.PROGRESSIVE_ITEMS_REWARD):
            return
        for vehicleCD, items in self.__message.data.iteritems():
            newItemsCDs = items.keys()
            isFirst = checkIsFirstProgressionDecalOnVehicle(vehicleCD, newItemsCDs)
            for itemCD, level in items.iteritems():
                showProgressiveItemsRewardWindow(itemCD, vehicleCD, level, itemCD == newItemsCDs[-1] and not isFirst)

            if isFirst:
                showProgressionRequiredStyleUnlockedWindow(vehicleCD)

        return


class VehicleCollectorAchievementHandler(ServiceChannelHandler):
    _PATTERN = CollectorVehicleConsts.COLLECTOR_MEDAL_PREFIX

    def __init__(self, awardCtrl):
        super(VehicleCollectorAchievementHandler, self).__init__(SYS_MESSAGE_TYPE.achievementReceived.index(), awardCtrl)
        self.__nationAwards = []
        self.__isCollectionAssembled = False
        return

    def fini(self):
        self.__clear()
        super(VehicleCollectorAchievementHandler, self).fini()
        return

    def _needToShowAward(self, ctx):
        isNeedToShow = super(VehicleCollectorAchievementHandler, self)._needToShowAward(ctx)
        if isNeedToShow:
            self.__setAwards(ctx)
            return self.__isAwardsReceived()
        return False

    def __setAwards(self, ctx):
        _, message = ctx
        medals = message.data.get(_POPUP_RECORDS, {})
        if not medals:
            return
        for _, medalName in medals:
            if not medalName.startswith(self._PATTERN):
                continue
            if len(medalName) == len(self._PATTERN):
                self.__isCollectionAssembled = True
            else:
                nation = int(medalName[len(self._PATTERN):])
                if self.__isNationCorrect(nation):
                    self.__nationAwards.append(nation)

        return

    def __isAwardsReceived(self):
        return len(self.__nationAwards) > 0 or self.__isCollectionAssembled

    def _showAward(self, ctx):
        self.__showNationalCollectorAward()
        self.__showVehicleCollectorOfEverythingAward()
        self.__clear()
        return

    def __showNationalCollectorAward(self):
        if self.__nationAwards is None:
            return
        else:
            for nationID in self.__nationAwards:
                award_events.showVehicleCollectorAward(nationID)

            return

    def __showVehicleCollectorOfEverythingAward(self):
        if self.__isCollectionAssembled:
            award_events.showVehicleCollectorOfEverythingAward()
        return

    def __clear(self):
        self.__nationAwards = []
        self.__isCollectionAssembled = False
        return

    def __isNationCorrect(self, nationID):
        if nationID is None or nationID >= len(NAMES) or nationID < 0:
            _logger.error(b'Incorrect nationID=%s for the award window of the vehicle collector', nationID)
            return False
        else:
            return True


class BattlePassRewardHandler(ServiceChannelHandler):
    __battlePass = dependency.descriptor(IBattlePassController)
    __notificationMgr = dependency.descriptor(INotificationWindowController)

    def __init__(self, awardCtrl):
        super(BattlePassRewardHandler, self).__init__(SYS_MESSAGE_TYPE.battlePassReward.index(), awardCtrl)
        return

    def _showAward(self, ctx):
        _, message = ctx
        rewards = message.data.get(b'reward', {})
        data = message.data.get(b'ctx', {})
        packageRewards = message.data.get(b'packageReward')
        eventMethod = defaultEventMethod
        if b'reason' not in data:
            _logger.error(b'Invalid Battle Pass Reward data received! "reward" key missing!')
            return
        else:
            if data.get(b'reason') == BattlePassRewardReason.PURCHASE_BATTLE_PASS_MULTIPLE:
                if not rewards:
                    return
                eventMethod = multipleBattlePassPurchasedEventMethod
            for key in (b'newLevel', b'prevLevel', b'chapter'):
                if key not in data:
                    _logger.error(b'Invalid Battle Pass Reward data received! "%s" key missing!', key)
                    return

            packageRewards = packageRewards or {}
            event = packStartEvent(rewards, data, packageRewards, eventMethod, battlePass=self.__battlePass)
            if event is not None:
                self.__notificationMgr.append(event)
            return


class BattlePassStyleRecievedHandler(ServiceChannelHandler):
    __battlePassController = dependency.descriptor(IBattlePassController)
    __itemsCache = dependency.descriptor(IItemsCache)

    def __init__(self, awardCtrl):
        super(BattlePassStyleRecievedHandler, self).__init__(SYS_MESSAGE_TYPE.battlePassStyleRecieved.index(), awardCtrl)
        self.__chapter = None
        return

    def fini(self):
        self.__itemsCache.onSyncCompleted -= self.__showAward
        super(BattlePassStyleRecievedHandler, self).fini()
        return

    def _showAward(self, ctx):
        _, message = ctx
        self.__chapter = message.data.get(b'chapter', 0)
        _, level = getStyleInfoForChapter(self.__chapter)
        if level < 1:
            self.__itemsCache.onSyncCompleted += self.__showAward
        else:
            self.__showAward()
        return

    def __showAward(self, *_):
        self.__itemsCache.onSyncCompleted -= self.__showAward
        _, level = getStyleInfoForChapter(self.__chapter)
        if level > 1:
            return
        data = {b'chapter': (self.__chapter), b'reason': (BattlePassRewardReason.STYLE_UPGRADE)}
        styleToken = get3DStyleProgressToken(self.__battlePassController.getSeasonID(), self.__chapter, level)
        rewards = packToken(styleToken)
        showBattlePassAwardsWindow([rewards], data, useQueue=True)
        return


class BattlePassBuyEmptyHandler(ServiceChannelHandler):
    __battlePass = dependency.descriptor(IBattlePassController)

    def __init__(self, awardCtrl):
        super(BattlePassBuyEmptyHandler, self).__init__(SYS_MESSAGE_TYPE.battlePassBought.index(), awardCtrl)
        return

    def _needToShowAward(self, ctx):
        needToShow = super(BattlePassBuyEmptyHandler, self)._needToShowAward(ctx)
        if needToShow:
            _, message = ctx
            chapterID = message.data.get(b'chapter')
            if chapterID is None:
                return False
            if chapterID:
                minLevel, _ = self.__battlePass.getChapterLevelInterval(chapterID)
                chapterIDs = (chapterID,)
            else:
                minLevel = MIN_LEVEL
                chapterIDs = self.__battlePass.getChapterIDs()
            return all(self.__battlePass.getLevelInChapter(chapterID) < minLevel for chapterID in chapterIDs)
        else:
            return False

    def _showAward(self, ctx):
        _, message = ctx
        packageRewards = message.data.get(b'packageReward')
        chapterID = message.data.get(b'chapter')
        reason = message.data.get(b'reason')
        if chapterID is None:
            _logger.error(b'chapter can not be None!')
            return
        else:
            if reason is None:
                if chapterID:
                    reason = BattlePassRewardReason.PURCHASE_BATTLE_PASS
                else:
                    reason = BattlePassRewardReason.PURCHASE_BATTLE_PASS_MULTIPLE
            prevLevel, _ = self.__battlePass.getChapterLevelInterval(chapterID)
            callback = partial(self.__onAwardShown, chapterID)
            data = {b'prevLevel': prevLevel, b'chapter': chapterID, b'reason': reason, b'callback': callback}
            showBattlePassAwardsWindow([], data, useQueue=True, packageRewards=packageRewards)
            return

    def __onAwardShown(self, chapterID):
        if self.__battlePass.isDisabled() or chapterID is None:
            return
        if self.__battlePass.isResourceChapter(chapterID) and self.__battlePass.allRegularChaptersPurchased():
            return
        else:
            showMissionsBattlePass(R.views.lobby.battle_pass.BattlePassProgressionsView() if chapterID else None, chapterID)
            return


class BattlePassCapHandler(ServiceChannelHandler):
    __battlePassController = dependency.descriptor(IBattlePassController)

    def __init__(self, awardCtrl):
        super(BattlePassCapHandler, self).__init__(SYS_MESSAGE_TYPE.battlePassReachedCap.index(), awardCtrl)
        return

    def _showAward(self, ctx):
        _, message = ctx
        for key in (b'vehTypeCompDescr', b'vehiclePoints', b'bonusPoints'):
            if key not in message.data:
                _logger.error(b'Invalid Reached Cap data!')
                return

        showBattlePassVehicleAwardWindow(message.data)
        return


class Comp7CouponHandler(ServiceChannelHandler):

    def __init__(self, awardCtrl):
        super(Comp7CouponHandler, self).__init__(SYS_MESSAGE_TYPE.tokenQuests.index(), awardCtrl)
        self.__questTypes = [
         SYS_MESSAGE_TYPE.battleResults.index(),
         SYS_MESSAGE_TYPE.tokenQuests.index(),
         SYS_MESSAGE_TYPE.invoiceReceived.index()]
        return

    def _needToShowAward(self, ctx):
        _, message = ctx
        return message is not None and message.type in self.__questTypes and message.data is not None

    def _showAward(self, ctx):
        messageData = ctx[1].data
        if b'data' in messageData:
            data = messageData[b'data']
        else:
            data = messageData
        tokensDict = data.get(b'tokens', {})
        for tokenName, value in tokensDict.iteritems():
            if tokenName.startswith(COMP7_TOKEN_COUPON_REWARD_ID):
                self._showWindow(value.get(b'count', 1))
                return

        return

    @staticmethod
    def _showWindow(count):
        SystemMessages.pushMessage(b'', type=SystemMessages.SM_TYPE.Comp7CouponReceived, messageData={b'count': count})
        return


class DynamicBonusHandler(ServiceChannelHandler):
    AVAILABLE_TAGS = [
     b'wgcq.clan_reward',
     b'wgcq.player_reward']

    def __init__(self, awardCtrl):
        super(DynamicBonusHandler, self).__init__(SYS_MESSAGE_TYPE.invoiceReceived.index(), awardCtrl)
        return

    def _showAward(self, ctx):
        invoiceData = ctx[1].data
        if invoiceData.get(b'assetType') in (INVOICE_ASSET.DATA, INVOICE_ASSET.PURCHASE) and b'tags' in invoiceData:
            if b'data' not in invoiceData:
                _logger.error(b'Invalid Reached Cap data!')
            for tag in invoiceData[b'tags']:
                if tag in self.AVAILABLE_TAGS:
                    showDynamicAward(tag.replace(b'.', b'_'), invoiceData[b'data'])

        return


class DedicationReward(ServiceChannelHandler):
    itemsCache = dependency.descriptor(IItemsCache)
    _hangarSpace = dependency.descriptor(IHangarSpace)

    def __init__(self, awardCtrl):
        super(DedicationReward, self).__init__(SYS_MESSAGE_TYPE.dedicationReward.index(), awardCtrl)
        self.__pending = []
        self.__locked = False
        return

    def fini(self):
        self._hangarSpace.onSpaceCreate -= self.__onSpaceCreated
        super(DedicationReward, self).fini()
        return

    def _showAward(self, ctx):
        _, message = ctx
        rewards = message.data.get(b'rewards', {})
        data = message.data.get(b'ctx', {})
        self.__processOrHold(([rewards], data))
        return

    def __onSpaceCreated(self):
        self.__unlock()
        return

    def _showDedicationReward(self, rewards, data):
        showDedicationRewardWindow(rewards, data, closeCallback=self.__unlock)
        return

    def __processOrHold(self, args):
        if self.__locked or not self._hangarSpace.spaceInited:
            self._hangarSpace.onSpaceCreate += self.__onSpaceCreated
            self.__pending.append(args)
        else:
            self.__locked = True
            self._showDedicationReward(*args)
        return

    def __unlock(self):
        self.__locked = False
        if self.__pending:
            self.__processOrHold(self.__pending.pop(0))
        return


class BadgesInvoiceHandler(ServiceChannelHandler):

    def __init__(self, awardCtrl):
        super(BadgesInvoiceHandler, self).__init__(channelType=SYS_MESSAGE_TYPE.invoiceReceived.index(), awardCtrl=awardCtrl)
        return

    def _showAward(self, ctx):
        _, message = ctx
        invoiceData = message.data.get(b'data', {})
        changes = invoiceData.get(b'dossier', {}).get(DOSSIER_TYPE.ACCOUNT, {})
        it = changes.iteritems() if isinstance(changes, dict) else changes
        for (blockName, recordName), paramsDict in it:
            if blockName == BADGES_BLOCK:
                if paramsDict[b'value'] > 0:
                    badgeId = int(recordName)
                    badge = self.itemsCache.items.getBadgeByID(badgeId)
                    if badge is None:
                        _logger.error(b'Unknown Badge. id=%s', badgeId)
                    elif badge.showCongratsView:
                        self._showWindow(badge)

        return

    @staticmethod
    def _showWindow(badge):
        showBadgeInvoiceAwardWindow(badge)
        return


class MapboxProgressionRewardHandler(AwardHandler):
    __notificationMgr = dependency.descriptor(INotificationWindowController)
    __eventsCache = dependency.descriptor(IEventsCache)
    __mapboxCtrl = dependency.descriptor(IMapboxController)

    def init(self):
        g_messengerEvents.serviceChannel.onClientMessageReceived += self.handle
        return

    def fini(self):
        g_messengerEvents.serviceChannel.onClientMessageReceived -= self.handle
        return

    def _needToShowAward(self, args):
        _, __, settings = args
        return settings.messageSubtype == SCH_CLIENT_MSG_TYPE.MAPBOX_PROGRESSION_REWARD

    @th_async.th_async
    def _showAward(self, ctx):
        _, message, __ = ctx
        bonuses = chain.from_iterable([getServiceBonuses(name, value) for name, value in message[b'savedData'].get(b'rewards', {}).iteritems()])
        window = MapBoxAwardsViewWindow(message[b'savedData'][b'battles'], bonuses)
        self.__notificationMgr.append(WindowNotificationCommand(window))
        self.__eventsCache.onEventsVisited()
        yield th_async.th_await(self.__mapboxCtrl.forceUpdateProgressData())
        return


class PurchaseHandler(ServiceChannelHandler):
    __purchaseCache = dependency.descriptor(IPurchaseCache)

    def __init__(self, awardCtrl):
        super(PurchaseHandler, self).__init__(SYS_MESSAGE_TYPE.invoiceReceived.index(), awardCtrl)
        return

    def _showAward(self, ctx):
        _, message = ctx
        invoiceData = message.data
        if invoiceData.get(b'assetType', 0) == INVOICE_ASSET.PURCHASE:
            if self.__purchaseCache.canBeRequestedFromProduct(invoiceData):
                if b'data' not in invoiceData:
                    _logger.error(b'Invalid purchase invoice data!')
                    return
                self.__tryToShowAwards(invoiceData)
            else:
                _logger.debug(b'Data can not be requested from the product! Award window will not be shown!')
        return

    @adisp_process
    def __tryToShowAwards(self, invoiceData):
        yield lambda callback: callback(True)
        metaData = invoiceData.get(b'meta', {})
        if metaData.get(b'type') == b'normal':
            productCode = self.__purchaseCache.getProductCode(metaData)
            if productCode:
                pD = yield self.__purchaseCache.requestPurchaseByID(productCode)
                if pD.getDisplayWays().showAwardScreen:
                    rewards, tTips = yield MultipleAwardRewardsMainPacker().getWholeBonusesData(invoiceData, productCode)
                    if rewards:
                        showMultiAwardWindow(rewards, tTips, productCode)
                    else:
                        _logger.info(b'Reward list is empty, multiple awards window will not be shown for purchase %s', productCode)
            else:
                _logger.debug(b'Product code is empty! Awards Window will not be shown!')
        return


class BattleMattersQuestsHandler(MultiTypeServiceChannelHandler):
    __battleMattersCtrl = dependency.descriptor(IBattleMattersController)
    __systemMessages = dependency.descriptor(ISystemMessages)

    def __init__(self, awardCtrl):
        super(BattleMattersQuestsHandler, self).__init__((
         SYS_MESSAGE_TYPE.hangarQuests.index(),
         SYS_MESSAGE_TYPE.tokenQuests.index(),
         SYS_MESSAGE_TYPE.battleResults.index(),
         SYS_MESSAGE_TYPE.versusAIBattleResults.index()), awardCtrl)
        return

    def _showAward(self, ctx, clientCtx=None):
        _, message = ctx
        if message.type in (SYS_MESSAGE_TYPE.battleResults.index(), SYS_MESSAGE_TYPE.versusAIBattleResults.index()):
            self.__systemMessages.proto.serviceChannel.pushClientMessage(message, SCH_CLIENT_MSG_TYPE.BATTLE_MATTERS_BATTLE_AWARD)
        self.__battleMattersCtrl.showAwardView(message.data)
        return

    def _needToShowAward(self, ctx):
        _, message = ctx
        if not super(BattleMattersQuestsHandler, self)._needToShowAward(ctx):
            return False
        data = message.data
        return [qID for qID in data.get(b'completedQuestIDs', set()) if self.__battleMattersCtrl.isBattleMattersQuestID(qID)]


class ResourceWellRewardHandler(ServiceChannelHandler):

    def __init__(self, awardCtrl):
        super(ResourceWellRewardHandler, self).__init__(SYS_MESSAGE_TYPE.resourceWellReward.index(), awardCtrl)
        return

    def _showAward(self, ctx):
        _, message = ctx
        showResourceWellAwardWindow(serialNumber=message.data.get(b'serialNumber', b''))
        return


class Comp7RewardHandler(MultiTypeServiceChannelHandler):
    __comp7Ctrl = dependency.descriptor(IComp7Controller)

    def __init__(self, awardCtrl):
        super(Comp7RewardHandler, self).__init__((
         SYS_MESSAGE_TYPE.battleResults.index(), SYS_MESSAGE_TYPE.tokenQuests.index()), awardCtrl)
        self.__completedQuestIDs = set()
        return

    def fini(self):
        self.__completedQuestIDs.clear()
        self.eventsCache.onSyncCompleted -= self.__showAward
        super(Comp7RewardHandler, self).fini()
        return

    def _showAward(self, ctx):
        _, message = ctx
        data = message.data
        bonusType = data.get(b'bonusType', 0)
        if bonusType == ARENA_BONUS_TYPE.COMP7:
            self.__comp7Ctrl.onComp7BattleFinished()
        self.__completedQuestIDs.update(qID for qID in data.get(b'completedQuestIDs', set()) if isComp7VisibleQuest(qID))
        if not self.__completedQuestIDs:
            return
        if self.eventsCache.waitForSync:
            self.eventsCache.onSyncCompleted += self.__onEventCacheSyncCompleted
        else:
            self.__showAward()
        return

    def __showAward(self):
        ranksQuests, tokensQuests, periodicQuests, isQualification = self.__getComp7CompletedQuests()
        self.__completedQuestIDs.clear()
        if isQualification:
            event_dispatcher.showComp7QualificationRewardsScreen(quests=ranksQuests)
        else:
            for quest in ranksQuests:
                event_dispatcher.showComp7RanksRewardsScreen(quest=quest, periodicQuests=periodicQuests)

        for quest in tokensQuests:
            event_dispatcher.showComp7TokensRewardsScreen(quest=quest)

        return

    def __getComp7CompletedQuests(self):
        ranksQuests = []
        tokensQuests = []
        periodicQuests = []
        isQualification = False
        if not self.__completedQuestIDs:
            return (ranksQuests, tokensQuests, periodicQuests)
        else:
            allQuests = self.eventsCache.getAllQuests((lambda q: isComp7VisibleQuest(q.getID())))
            for qID in self.__completedQuestIDs:
                quest = allQuests.get(qID)
                if quest is None:
                    _logger.error(b'Missing Comp7 Quest qID=%s', qID)
                    continue
                qType = getComp7QuestType(qID)
                if qType == Comp7QuestType.RANKS:
                    ranksQuests.append(quest)
                elif qType == Comp7QuestType.TOKENS:
                    tokensQuests.append(quest)
                periodicQuest = self.__getPeriodicQuest(qID, allQuests)
                if periodicQuest:
                    periodicQuests.append(periodicQuest)
                if qID == COMP7_QUALIFICATION_QUEST_ID:
                    isQualification = True

            ranksQuests.sort(key=self.__getRanksQuestSortKey, reverse=True)
            tokensQuests.sort(key=self.__getTokensQuestSortKey)
            return (
             ranksQuests, tokensQuests, periodicQuests, isQualification)

    def __onEventCacheSyncCompleted(self, *_):
        self.eventsCache.onSyncCompleted -= self.__onEventCacheSyncCompleted
        self.__showAward()
        return

    @staticmethod
    def __getPeriodicQuest(questID, allQuests):
        periodicID = questID.replace(Comp7QuestType.RANKS.value, Comp7QuestType.PERIODIC.value)
        qType = getComp7QuestType(periodicID)
        if qType == Comp7QuestType.PERIODIC:
            return allQuests.get(periodicID)
        else:
            return

    @staticmethod
    def __getRanksQuestSortKey(quest):
        division = parseComp7RanksQuestID(quest.getID())
        return (
         division.rank, division.index)

    @staticmethod
    def __getTokensQuestSortKey(quest):
        return parseComp7TokensQuestID(quest.getID())


class CollectionsRewardHandler(ServiceChannelHandler):
    __collections = dependency.descriptor(ICollectionsSystemController)

    def __init__(self, awardCtrl):
        super(CollectionsRewardHandler, self).__init__(SYS_MESSAGE_TYPE.collectionsReward.index(), awardCtrl)
        return

    def _needToShowAward(self, ctx):
        if not super(CollectionsRewardHandler, self)._needToShowAward(ctx):
            return False
        _, message = ctx
        data = message.data
        isFinal = data[b'requiredCount'] == self.__collections.getMaxProgressItemCount(data[b'collectionId'])
        return isFinal

    def _showAward(self, ctx):
        _, message = ctx
        data = message.data
        showCollectionAwardsWindow(data[b'collectionId'], [data[b'reward']], isFinal=True)
        return


class PremiumSubsEntitlementReceivedHandler(MultiTypeServiceChannelHandler):
    _SUBSCRIPTION_TRIAL_TOKEN = b'premium_subs_trial_day'
    __premiumSubsCtrl = dependency.descriptor(IWotPlusController)
    __systemMessages = dependency.descriptor(ISystemMessages)

    def __init__(self, awardCtrl):
        super(PremiumSubsEntitlementReceivedHandler, self).__init__((
         SYS_MESSAGE_TYPE.invoiceReceived.index(),), awardCtrl)
        return

    def _needToShowAward(self, ctx):
        if not super(PremiumSubsEntitlementReceivedHandler, self)._needToShowAward(ctx):
            return False
        _, message = ctx
        days = self.__getEntitlementsDaysReceived(message)
        if days and self.__premiumSubsCtrl.isWotPlusEnabled():
            return True
        return

    def _showAward(self, ctx):
        _, message = ctx
        self.__sentReceivedMsg(self.__getEntitlementsDaysReceived(message), message)
        return

    def __getEntitlementsDaysReceived(self, message):
        days = 0
        data = message.data
        dataEx = data.get(b'data', {}) if message.type == SYS_MESSAGE_TYPE.invoiceReceived.index() else data
        premiumSubsData = dataEx.get(b'entitlements', {}).get(SUBSCRIPTION_ENTITLEMENT, {})
        premiumSubsTrialTokenData = first((v for k, v in dataEx.get(b'tokens', {}).iteritems() if self._SUBSCRIPTION_TRIAL_TOKEN in k), {})
        if premiumSubsData:
            days = datetime.timedelta(seconds=premiumSubsData.get(b'count', 0)).days
        elif premiumSubsTrialTokenData:
            days = premiumSubsTrialTokenData.get(b'count', 0)
        return days

    @adisp_process
    def __sentReceivedMsg(self, days, message):
        if days and self.__premiumSubsCtrl.isWotPlusEnabled():
            if self.__premiumSubsCtrl.getState() == WotPlusState.INACTIVE:
                yield self.__premiumSubsCtrl.synchronize()
            savedData = message.data.setdefault(b'savedData', {})
            savedData[b'premium_subs_days'] = days
            self.__systemMessages.proto.serviceChannel.pushClientMessage(message, SCH_CLIENT_MSG_TYPE.PREMIUM_SUBS_RECEIVED_FROM_INVOICE)
        return


class EarlyAccessQuestHandler(ServiceChannelHandler):
    __earlyAccessController = dependency.descriptor(IEarlyAccessController)

    def __init__(self, awardCtrl):
        super(EarlyAccessQuestHandler, self).__init__(SYS_MESSAGE_TYPE.battleResults.index(), awardCtrl)
        self.__mergedBonuses = {}
        return

    def _showAward(self, ctx):
        showEarlyAccessRewardsView(self.__mergedBonuses)
        return

    def _needToShowAward(self, ctx):
        if not super(EarlyAccessQuestHandler, self)._needToShowAward(ctx):
            return False
        _, message = ctx
        return bool(self.__checkEarlyAccessQuests(message.data))

    def __checkEarlyAccessQuests(self, data):
        completedQuestIDs = data.get(b'completedQuestIDs', ())
        rewards = []
        for qID in completedQuestIDs:
            if self.__earlyAccessController.isPostProgressionQuest(qID):
                rewards.append(data.get(b'detailedRewards', {}).get(qID, {}))

        self.__mergedBonuses = getMergedBonusesFromDicts(rewards)
        return bool(self.__mergedBonuses)


class DailyEpicQuestsHandler(ServiceChannelHandler):
    _EPIC_QUEST = b'QUEST_EPIC_REWARD'

    def __init__(self, awardCtrl):
        super(DailyEpicQuestsHandler, self).__init__(SYS_MESSAGE_TYPE.battleResults.index(), awardCtrl)
        self._qId = None
        return

    def _showAward(self, ctx):
        _, message = ctx
        rewards = message.data.get(b'detailedRewards', {}).get(self._qId, {})
        bonuses = getMergedBonusesFromDicts([rewards])
        if bonuses:
            showDailyEpicQuestRewardWindow(bonuses)
        else:
            _logger.error(b"Can't show empty or invalid reward!")
        return

    def _needToShowAward(self, ctx):
        if not super(DailyEpicQuestsHandler, self)._needToShowAward(ctx):
            return False
        _, message = ctx
        questIDs = message.data.get(b'completedQuestIDs', set())
        self._qId = findFirst((lambda x: self._EPIC_QUEST in x), questIDs, self._qId)
        return bool(self._qId)


class PromoCodeInvoiceHandler(MultiTypeServiceChannelHandler):

    def __init__(self, awardCtrl):
        super(PromoCodeInvoiceHandler, self).__init__((
         SYS_MESSAGE_TYPE.invoiceReceived.index(),
         SYS_MESSAGE_TYPE.tokenQuests.index(),
         SYS_MESSAGE_TYPE.battleResults.index()), awardCtrl)
        return

    def _needToShowAward(self, ctx):
        _, message = ctx
        if not super(PromoCodeInvoiceHandler, self)._needToShowAward(ctx):
            return False
        if not promo_code_reward_screen.isPromoCodeRewardScreenEnabled():
            return False
        data = message.data
        if message.type == SYS_MESSAGE_TYPE.invoiceReceived.index():
            for token in data[b'data'].get(b'tokens', {}):
                if promo_code_reward_screen.isPromoCodeToken(token):
                    return True

            return False
        if message.type in (SYS_MESSAGE_TYPE.battleResults.index(), SYS_MESSAGE_TYPE.tokenQuests.index()):
            for _, rewards in data.get(b'detailedRewards', {}).iteritems():
                for token in rewards.get(b'tokens', {}):
                    if promo_code_reward_screen.isPromoCodeToken(token):
                        return True

        return False

    def _showAward(self, ctx):
        _, message = ctx
        data = message.data
        rewards = {}
        if message.type == SYS_MESSAGE_TYPE.invoiceReceived.index():
            for token in data[b'data'].get(b'tokens', {}):
                if promo_code_reward_screen.isPromoCodeToken(token):
                    rewards[token] = (
                     data[b'data'], REWARDS_SOURCE_INVOICE)

        if message.type in (SYS_MESSAGE_TYPE.battleResults.index(), SYS_MESSAGE_TYPE.tokenQuests.index()):
            for _, rwrds in data.get(b'detailedRewards', {}).iteritems():
                for token in rwrds.get(b'tokens', {}):
                    if promo_code_reward_screen.isPromoCodeToken(token):
                        rewardsSource = REWARDS_SOURCE_BATTLE_RESULTS if message.type else REWARDS_SOURCE_TOKEN_QUESTS
                        rewards[token] = (rwrds, rewardsSource)
                        break

        for token, reward in rewards.iteritems():
            showPromoCodeRewardScreen(token, [reward[0]], reward[1])

        return


class SummerSaleRewardReceivedHandler(MultiTypeServiceChannelHandler):
    __summerSale = dependency.descriptor(ISummerSaleController)

    def __init__(self, awardCtrl):
        super(SummerSaleRewardReceivedHandler, self).__init__((
         SYS_MESSAGE_TYPE.invoiceReceived.index(),
         SYS_MESSAGE_TYPE.immediatelyOpenBoxReward.index()), awardCtrl)
        return

    def _needToShowAward(self, ctx):
        _, message = ctx
        if not super(SummerSaleRewardReceivedHandler, self)._needToShowAward(ctx):
            return False
        if message.type == SYS_MESSAGE_TYPE.invoiceReceived.index() and self.__summerSale.getProductTag() in message.data.get(b'tags', []):
            return True
        if message.type == SYS_MESSAGE_TYPE.immediatelyOpenBoxReward.index():
            return any(self.itemsCache.items.tokens.getLootBoxByID(lootBoxID).getType() == self.__summerSale.getSummerSaleSetType() for lootBoxID in message.data.iterkeys())
        return False

    def _showAward(self, ctx):
        _, message = ctx
        data = message.data
        rewards = {}
        if message.type == SYS_MESSAGE_TYPE.invoiceReceived.index():
            rewards = data.get(b'data', {})
        if message.type == SYS_MESSAGE_TYPE.immediatelyOpenBoxReward.index():
            if data:
                box = first(data.values())
                rewards = box.get(b'rewards', {})
        self.preformatCompensationValue(rewards)
        self.preformatStyle(rewards)
        tryShowWithVideoReward(rewards)
        return

    @classmethod
    def preformatCompensationValue(cls, rewards):
        vehiclesList = rewards.get(b'vehicles', [])
        compValue = cls.__getCompensationVehicleValue(vehiclesList)
        for currency in Currency.ALL:
            if compValue.get(currency, 0) > 0:
                currencyValue = rewards.pop(currency, 0)
                if currency is not None:
                    newCurrencyValue = currencyValue - compValue.get(currency, 0)
                    if newCurrencyValue:
                        rewards[currency] = max(newCurrencyValue, 0)

        return

    @classmethod
    def preformatStyle(cls, rewards):
        customizations = rewards.get(b'customizations', [])
        if customizations:
            rewards[b'customizations'] = [cData for cData in customizations if not cData.get(b'boundToCurrentVehicle', False)]
            if not rewards[b'customizations']:
                rewards.pop(b'customizations')
        return

    @classmethod
    def __getCompensationVehicleValue(cls, vehiclesList):
        comp = ZERO_MONEY
        for vehiclesDict in vehiclesList:
            for _, vehicleData in vehiclesDict.iteritems():
                if b'rentCompensation' in vehicleData:
                    comp += Money.makeFromMoneyTuple(vehicleData[b'rentCompensation'])
                if b'customCompensation' in vehicleData:
                    comp += Money.makeFromMoneyTuple(vehicleData[b'customCompensation'])

        return comp


registerAwardControllerHandlers((
 BattleQuestsAutoWindowHandler,
 PunishWindowHandler,
 TokenQuestsWindowHandler,
 MotiveQuestsWindowHandler,
 PersonalMissionBonusHandler,
 PersonalMissionWindowAfterBattleHandler,
 PersonalMissionAutoWindowHandler,
 PersonalMissionByAwardListHandler,
 PersonalMissionOperationAwardHandler,
 PersonalMissionOperationUnlockedHandler,
 GoldFishHandler,
 TelecomHandler,
 MarkByInvoiceHandler,
 MarkByQuestHandler,
 CrewBooksQuestHandler,
 RecertificationFormHandler,
 RecruitHandler,
 SoundDeviceHandler,
 EliteWindowHandler,
 LootBoxByInvoiceHandler,
 ProgressiveRewardHandler,
 ParagonsLevelRewardsReceivedHandler,
 ParagonsSelectableRewardReceivedHandler,
 PiggyBankOpenHandler,
 SeniorityAwardsWindowHandler,
 RankedQuestsHandler,
 BattlePassRewardHandler,
 BattlePassStyleRecievedHandler,
 BattlePassBuyEmptyHandler,
 BattlePassCapHandler,
 VehicleCollectorAchievementHandler,
 DynamicBonusHandler,
 ProgressiveItemsRewardHandler,
 DedicationReward,
 BadgesInvoiceHandler,
 MapboxProgressionRewardHandler,
 PurchaseHandler,
 RenewableSubscriptionHandler,
 BattleMattersQuestsHandler,
 ResourceWellRewardHandler,
 Comp7RewardHandler,
 CollectionsRewardHandler,
 PremiumSubsEntitlementReceivedHandler,
 Comp7CouponHandler,
 EarlyAccessQuestHandler,
 DailyEpicQuestsHandler,
 PromoCodeInvoiceHandler,
 SummerSaleRewardReceivedHandler))
