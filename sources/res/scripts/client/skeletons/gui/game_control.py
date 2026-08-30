from __future__ import absolute_import
import typing
from constants import ARENA_BONUS_TYPE
if typing.TYPE_CHECKING:
    from typing import Any, Callable, Dict, Iterable, Iterator, List, Optional, Set, Tuple, Union, Sequence, Generator
    from collections_common import Collection, CollectionItem
    from comp7.helpers.comp7_server_settings import Comp7RewardsConfig, Comp7Config
    from comp7.gui.game_control.comp7_controller import _LeaderboardDataProvider, _ProgressionDataProvider
    from disjoint_set import DisjointSet
    from Event import Event
    from gui.collection.resources.cdn.cache import CollectionsCdnCacheMgr
    from fun_random.gui.feature.configs.modes.mode import FunModeCompositeConfigurationModel
    from fun_random.gui.feature.models.common import FunSubModesStatus
    from fun_random.gui.feature.models.notifications import FunNotification
    from fun_random.gui.feature.models.progressions import FunProgression
    from fun_random.gui.feature.sub_modes.base_sub_mode import IFunSubMode
    from fun_random.helpers.server_settings import FunRandomConfig, FunMetaProgressionConfig
    from fun_random.gui.shared.events import FunEventScope, FunEventType
    from fun_random.gui.feature.sub_systems.fun_performance_analyzers import PerformanceGroup
    from gui.Scaleform.daapi.view.lobby.hangar.Hangar import Hangar
    from gui.battle_control.controllers.w2gt.w2gt_data_mgr import W2gtProgress
    from gui.battle_pass.state_machine.delegator import BattlePassRewardLogic
    from gui.game_control.epic_meta_game_ctrl import EpicMetaGameSkill
    from gui.game_control.mapbox_controller import ProgressionData
    from gui.game_control.trade_in import TradeInDiscounts
    from gui.game_control.live_ops_web_events_controller import EventState
    from gui.game_control.w2gt_controller import _W2gtResponseData
    from gui.gift_system.hubs.base.hub_core import IGiftEventHub
    from gui.hangar_presets.obsolete.hangar_gui_config import HangarGuiPreset
    from gui.hangar_presets.obsolete.hangar_presets_getters import IPresetsGetter
    from gui.hangar_presets.providers.base_dynamic_gui_provider import IHangarDynamicGuiProvider
    from gui.impl.lobby.winback.winback_helpers import WinbackQuestTypes
    from enumerations import EnumItem
    from gui.mapbox.mapbox_survey_manager import MapboxSurveyManager
    from gui.periodic_battles.models import AlertData, PeriodInfo, PrimeTime
    from gui.prb_control.items import ValidationResult
    from gui.ranked_battles.constants import YearAwardsNames
    from gui.ranked_battles.ranked_helpers.sound_manager import RankedSoundManager
    from gui.ranked_battles.ranked_helpers.stats_composer import RankedBattlesStatsComposer
    from gui.ranked_battles.ranked_helpers.web_season_provider import RankedWebSeasonProvider, WebSeasonInfo
    from gui.ranked_battles.ranked_models import BattleRankInfo, Division, PostBattleRankInfo, Rank
    from gui.server_events.bonuses import BattlePassSelectTokensBonus, BattlePassStyleProgressTokenBonus, SimpleBonus, TokensBonus
    from gui.server_events.event_items import RankedQuest
    from gui.shared.event_bus import SharedEvent
    from gui.shared.gui_items import Tankman, Vehicle, ItemsCollection
    from gui.shared.gui_items.artefacts import OptionalDevice
    from gui.shared.gui_items.badge import Badge
    from gui.shared.gui_items.fitting_item import RentalInfoProvider
    from gui.shared.gui_items.gui_item_economics import ItemPrice
    from gui.shared.gui_items.loot_box import LootBox
    from gui.shared.gui_items.tankman_skill import TankmanSkill
    from gui.shared.money import Money, CURRENCY_TYPE
    from gui.shared.utils.requesters.EpicMetaGameRequester import EpicMetaGameRequester
    from helpers.server_settings import BattleRoyaleConfig, EpicGameConfig, GiftSystemConfig, RankedBattlesConfig, VehiclePostProgressionConfig, _MapboxConfig, WinbackConfig, LiveOpsWebEventsConfig, EasyTankEquipConfig, SeniorityAwardsConfig, _W2GTConfig
    from items.vehicles import VehicleType
    from season_common import GameSeason
    from items.artefacts import Equipment
    from skeletons.gui.battle_session import IClientArenaVisitor
    from renewable_subscription_common.settings_constants import WotPlusState, WotPlusTier
    from gui.entitlements.entitlement_model import AgateEntitlement
    from gui.server_events.event_items import Quest
    from advanced_achievements_client.items import _BaseGuiAchievement
    from exchange.personal_discounts_constants import ExchangeDiscountInfo, ExchangeRate
    from renewable_subscription_common.optional_devices_usage_config import VehicleLoadout
    from gui.game_control.wotlda.loadout_model import BaseOptDeviceLoadoutModel
    from gui.shared.view_helpers.blur_manager import ImmediateSceneBlurConfig, SceneBlurConfig, UILayerBlurConfig
    from gui.game_control.vehicle_playlists_controller import VehiclePlaylist
    from helpers.ingame_tournament_helper import IngameTournamentState, IngameTournamentType
    from helpers.server_settings import _IngameTournamentShowmatchConfig
    from gui.game_control.ingame_tournament_controller import _IngameTournamentData
    from renewable_subscription_common.settings_helpers import SubscriptionSettingsStorage
    from gui.impl.gen.view_models.views.lobby.page.header.wot_plus_subscription_model import WotPlusPeriodicityEnum
    from gui.game_control.wot_plus.service_record_customization.service_record_customization import ServiceRecordAssetManager
    BattlePassBonusOpts = Optional[TokensBonus, BattlePassSelectTokensBonus]

class IGameController(object):

    def init(self):
        return

    def fini(self):
        return

    def onConnected(self):
        return

    def onDisconnected(self):
        return

    def onAvatarBecomePlayer(self):
        return

    def onAccountBecomePlayer(self):
        return

    def onAccountBecomeNonPlayer(self):
        return

    def onServerReplayEntering(self):
        return

    def onServerReplayExiting(self):
        return

    def onLobbyInited(self, event):
        return

    def onLobbyStarted(self, ctx):
        return


class IGameWindowController(IGameController):

    def hideWindow(self):
        return

    def showWindow(self, url=None, invokedFrom=None):
        return

    def getUrl(self, callback=lambda *args: None):
        raise NotImplementedError
        return

    def _getUrl(self):
        raise NotImplementedError
        return


class ISeasonProvider(object):

    def isAvailable(self):
        raise NotImplementedError
        return

    def isBattlesPossible(self):
        raise NotImplementedError
        return

    def isInPrimeTime(self):
        raise NotImplementedError
        return

    def isFrozen(self):
        raise NotImplementedError
        return

    def isNotSet(self, now=None, peripheryID=None):
        raise NotImplementedError
        return

    def isWithinSeasonTime(self, seasonID):
        raise NotImplementedError
        return

    def hasAnySeason(self):
        raise NotImplementedError
        return

    def hasAvailablePrimeTimeServers(self, now=None):
        raise NotImplementedError
        return

    def hasConfiguredPrimeTimeServers(self, now=None):
        raise NotImplementedError
        return

    def hasPrimeTimesLeftForCurrentCycle(self):
        raise NotImplementedError
        return

    def hasPrimeTimesPassedForCurrentCycle(self):
        raise NotImplementedError
        return

    def getClosestStateChangeTime(self, now=None):
        raise NotImplementedError
        return

    def getCurrentCycleID(self):
        raise NotImplementedError
        return

    def getCurrentCycleInfo(self):
        raise NotImplementedError
        return

    def getCurrentSeason(self, now=None):
        raise NotImplementedError
        return

    def getCurrentOrNextActiveCycleNumber(self, season):
        raise NotImplementedError
        return

    def getEventEndTimestamp(self):
        raise NotImplementedError
        return

    def getModeSettings(self):
        raise NotImplementedError
        return

    def getNextSeason(self, now=None):
        raise NotImplementedError
        return

    def getPeriodInfo(self, now=None, peripheryID=None):
        raise NotImplementedError
        return

    def getPrimeTimes(self):
        raise NotImplementedError
        return

    def getPrimeTimesForDay(self, selectedTime, groupIdentical=False):
        raise NotImplementedError
        return

    def getPrimeTimeStatus(self, now=None, peripheryID=None):
        raise NotImplementedError
        return

    def getPreviousSeason(self, now=None):
        raise NotImplementedError
        return

    def getSeason(self, seasonID):
        raise NotImplementedError
        return

    def getSeasonsPassed(self, now=None):
        raise NotImplementedError
        return

    def getAllSeasons(self):
        raise NotImplementedError
        return

    def getTimer(self, now=None, peripheryID=None):
        raise NotImplementedError
        return

    def getLeftTimeToPrimeTimesEnd(self, now=None):
        raise NotImplementedError
        return

    def getQuestsTimerLeft(self):
        raise NotImplementedError
        return


class IGameStateTracker(IGameController):

    def onAccountShowGUI(self, ctx):
        raise NotImplementedError
        return

    def addController(self, controller):
        raise NotImplementedError
        return

    def removeController(self, controller):
        raise NotImplementedError
        return


class IReloginController(IGameController):

    @property
    def isActive(self):
        return NotImplementedError

    def doRelogin(self, peripheryID, onStoppedHandler=None, extraChainSteps=None):
        raise NotImplementedError
        return


class IAOGASController(IGameController):
    onNotifyAccount = None


class IGameSessionController(IGameController):
    onClientNotify = None
    onTimeTillBan = None
    onNewDayNotify = None
    onPremiumNotify = None
    onPremiumTypeChanged = None
    onParentControlNotify = None
    onNotifyTimeTillKick = None

    def isSessionStartedThisDay(self):
        raise NotImplementedError
        return

    def getDailyPlayTimeLeft(self):
        raise NotImplementedError
        return

    def getWeeklyPlayTimeLeft(self):
        raise NotImplementedError
        return

    @property
    def isParentControlEnabled(self):
        raise NotImplementedError
        return

    @property
    def isParentControlActive(self):
        raise NotImplementedError
        return

    @property
    def sessionStartedAt(self):
        raise NotImplementedError
        return

    @property
    def sessionDuration(self):
        raise NotImplementedError
        return

    @property
    def lastBanMsg(self):
        raise NotImplementedError
        return

    @property
    def battlesCount(self):
        raise NotImplementedError
        return

    @property
    def isAdult(self):
        raise NotImplementedError
        return

    @property
    def isPlayTimeBlock(self):
        raise NotImplementedError
        return

    @property
    def isPrivateMessagesForbidden(self):
        raise NotImplementedError
        return

    @property
    def isNonFriendPrivateMessagesForbidden(self):
        raise NotImplementedError
        return

    @property
    def privateMessagesRestrictionReason(self):
        raise NotImplementedError
        return

    def incBattlesCounter(self):
        raise NotImplementedError
        return

    def getCurfewBlockTime(self):
        raise NotImplementedError
        return

    def getParentControlNotificationMeta(self):
        raise NotImplementedError
        return

    def getKickAtTime(self):
        raise NotImplementedError
        return


class IRentalsController(IGameController):
    onRentChangeNotify = None

    def getRentPackagesInfo(self, rentPrices, currentRentInfo):
        raise NotImplementedError
        return

    def filterRentPackages(self, rentPrices):
        raise NotImplementedError
        return

    def getRentPriceOfPackage(self, vehicle, rentType, packageID, package):
        raise NotImplementedError
        return


class ISeasonsController(IGameController):
    onSeasonChangeNotify = None

    def hasAnySeason(self, seasonType):
        raise NotImplementedError
        return

    def getCurrentSeason(self, seasonType):
        raise NotImplementedError
        return

    def getCurrentCycleID(self, seasonType):
        raise NotImplementedError
        return

    def getSeason(self, seasonType, seasonID):
        raise NotImplementedError
        return

    def isSeasonActive(self, seasonID, seasonType):
        raise NotImplementedError
        return

    def isWithinSeasonTime(self, seasonID, seasonType):
        raise NotImplementedError
        return

    def isSeasonCycleActive(self, cycleID, seasonType):
        raise NotImplementedError
        return


class IRestoreController(IGameController):
    onRestoreChangeNotify = None
    onTankmenBufferUpdated = None

    def getMaxTankmenBufferLength(self):
        raise NotImplementedError
        return

    def getDismissedTankmen(self):
        raise NotImplementedError
        return

    def getTankmenBeingDeleted(self, newTankmenCount=1):
        raise NotImplementedError
        return

    def getTankmenDeletedBySelling(self, *vehicles):
        raise NotImplementedError
        return


class IIGRController(IGameController):
    onIgrTypeChanged = None

    def getXPFactor(self):
        raise NotImplementedError
        return

    def getRoomType(self):
        raise NotImplementedError
        return


class IWalletController(IGameController):
    onWalletStatusChanged = None

    @property
    def status(self):
        raise NotImplementedError
        return

    @property
    def componentsStatuses(self):
        raise NotImplementedError
        return

    @property
    def dynamicComponentsStatuses(self):
        raise NotImplementedError
        return

    @property
    def isSyncing(self):
        raise NotImplementedError
        return

    @property
    def isNotAvailable(self):
        raise NotImplementedError
        return

    @property
    def isAvailable(self):
        raise NotImplementedError
        return

    @property
    def useGold(self):
        raise NotImplementedError
        return

    @property
    def useFreeXP(self):
        raise NotImplementedError
        return


class INotifyController(IGameController):
    pass


class IExternalLinksController(IGameController):

    def open(self, url):
        raise NotImplementedError
        return

    def getURL(self, name, params, callback):
        raise NotImplementedError
        return

    def externalAllowed(self, url):
        raise NotImplementedError
        return


class IInternalLinksController(IGameController):

    def getURL(self, name, callback):
        raise NotImplementedError
        return


class ISoundEventChecker(IGameController):

    def lockPlayingSounds(self):
        raise NotImplementedError
        return

    def unlockPlayingSounds(self, restore=True):
        raise NotImplementedError
        return


class IHeroTankController(IGameController):
    onUpdated = None
    onInteractive = None

    def getRandomTankCD(self):
        raise NotImplementedError
        return

    def setInteractive(self, interactive):
        raise NotImplementedError
        return

    def getCurrentTankCD(self):
        raise NotImplementedError
        return

    def getCurrentTankStyleId(self):
        raise NotImplementedError
        return

    def getCurrentTankCrew(self):
        raise NotImplementedError
        return

    def getCurrentRelatedURL(self):
        raise NotImplementedError
        return

    def getCurrentVehicleName(self):
        raise NotImplementedError
        return

    def getCurrentFromBoxes(self):
        raise NotImplementedError
        return

    def getCurrentShopUrl(self):
        raise NotImplementedError
        return

    def setDebugTankCD(self, debugTankCD):
        raise NotImplementedError
        return

    def isEnabled(self):
        raise NotImplementedError
        return

    def setEnabled(self, isEnabled):
        raise NotImplementedError
        return


class IPlatoonController(IGameController):
    onFilterUpdate = None
    onMembersUpdate = None
    onPlatoonTankUpdated = None
    onPlatoonTankVisualizationChanged = None
    onChannelControllerChanged = None
    onAvailableTiersForSearchChanged = None
    onAutoSearchCooldownChanged = None
    onPlatoonTankRemove = None

    def buildExtendedSquadInfoVo(self):
        raise NotImplementedError
        return

    def getUserSearchFlags(self):
        raise NotImplementedError
        return

    def getCurrentSearchFlags(self):
        raise NotImplementedError
        return

    def saveUserSearchFlags(self, value):
        raise NotImplementedError
        return

    def resetUnitTierFilter(self):
        raise NotImplementedError
        return

    def evaluateVisibility(self, toggleUI=False):
        raise NotImplementedError
        return

    def createPlatoon(self, startAutoSearchOnUnitJoin=False):
        raise NotImplementedError
        return

    def leavePlatoon(self, isExit=True, ignoreConfirmation=False, parent=None):
        raise NotImplementedError
        return

    def isPlayerRoleAutoSearch(self):
        raise NotImplementedError
        return

    def isAnyPlatoonUIShown(self):
        raise NotImplementedError
        return

    def isInSearch(self):
        raise NotImplementedError
        return

    def isInQueue(self):
        raise NotImplementedError
        return

    def isInPlatoon(self):
        raise NotImplementedError
        return

    def isSearchingForPlayersEnabled(self):
        raise NotImplementedError
        return

    def isTankLevelPreferenceEnabled(self):
        raise NotImplementedError
        return

    def getAllowedTankLevels(self, prebattleType):
        raise NotImplementedError
        return

    def isVOIPEnabled(self):
        raise NotImplementedError
        return

    def isInCoolDown(self, requestType):
        raise NotImplementedError
        return

    def canStartSearch(self):
        raise NotImplementedError
        return

    def getPrbEntity(self):
        raise NotImplementedError
        return

    def getQueueType(self):
        raise NotImplementedError
        return

    def destroyUI(self, hideOnly=False):
        raise NotImplementedError
        return

    def getExpandedSearchFlags(self):
        raise NotImplementedError
        return

    def setPlatoonPopoverPosition(self, xPopoverOffset):
        raise NotImplementedError
        return

    def togglePlayerReadyAction(self, skipAmmocheck=False, callback=None):
        raise NotImplementedError
        return

    def getChannelController(self):
        raise NotImplementedError
        return

    def requestPlayerQueueInfo(self):
        raise NotImplementedError
        return

    def canSelectSquadSize(self):
        raise NotImplementedError
        return

    def hasSelectorPopover(self):
        raise NotImplementedError
        return

    def hasSearchSupport(self):
        raise NotImplementedError
        return

    def hasWelcomeWindow(self):
        raise NotImplementedError
        return

    def getPlatoonSlotsData(self):
        raise NotImplementedError
        return

    def hasFreeSlot(self):
        raise NotImplementedError
        return

    def getMaxSlotCount(self):
        raise NotImplementedError
        return

    def getPlayerInfo(self):
        raise NotImplementedError
        return

    def cancelSearch(self):
        raise NotImplementedError
        return

    def startSearch(self):
        raise NotImplementedError
        return

    def registerPlatoonTank(self, platoonTank):
        raise NotImplementedError
        return

    def getPermissions(self):
        raise NotImplementedError
        return

    def getPrbEntityType(self):
        raise NotImplementedError
        return

    def isUnitWithPremium(self):
        raise NotImplementedError
        return

    def getFunctionalState(self):
        raise NotImplementedError
        return

    def hasVehiclesForSearch(self, tierLevel=None):
        raise NotImplementedError
        return

    def getSquadManStates(self, player, role):
        raise NotImplementedError
        return

    def orderSlotsBasedOnDisplaySlotsIndices(self, slots):
        raise NotImplementedError
        return

    def processPlatoonActions(self, mapID, entity, currentVehicle, callback):
        raise NotImplementedError
        return

    def getPopoverParams(self):
        raise NotImplementedError
        return

    def setPopoverParams(self, params):
        raise NotImplementedError
        return


class IServerStatsController(IGameController):
    onStatsReceived = None

    def getFormattedStats(self):
        raise NotImplementedError
        return

    def getStats(self):
        raise NotImplementedError
        return


class IBrowserController(IGameController):
    onBrowserDeleted = None
    onBrowserAdded = None

    def addFilterHandler(self, handler):
        raise NotImplementedError
        return

    def removeFilterHandler(self, handler):
        raise NotImplementedError
        return

    def load(self, url=None, title=None, showActionBtn=True, showWaiting=True, browserID=None, isAsync=False, browserSize=None, isDefault=True, callback=None, showCloseBtn=False, useBrowserWindow=True, isModal=False, showCreateWaiting=False, handlers=None, showBrowserCallback=None, isSolidBorder=False):
        raise NotImplementedError
        return

    def getAllBrowsers(self):
        raise NotImplementedError
        return

    def getBrowser(self, browserID):
        raise NotImplementedError
        return

    def delBrowser(self, browserID):
        raise NotImplementedError
        return


class IPromoController(IGameController):
    onNewTeaserReceived = None
    onPromoCountChanged = None
    onTeaserShown = None
    onTeaserClosed = None

    @property
    def isPromoOpen(self):
        raise NotImplementedError
        return

    def isActive(self):
        raise NotImplementedError
        return

    def getPromoCount(self):
        raise NotImplementedError
        return

    def showPromo(self, url, closeCallback=None, source=None):
        raise NotImplementedError
        return

    def setNewTeaserData(self, teaserData):
        raise NotImplementedError
        return

    def showFieldPost(self):
        raise NotImplementedError
        return

    def showLastTeaserPromo(self):
        raise NotImplementedError
        return

    def setUnreadPromoCount(self, count):
        raise NotImplementedError
        return

    def isTeaserOpen(self):
        raise NotImplementedError
        return

    def getUrlWithAuthParams(self, url):
        raise NotImplementedError
        return

    def subscribePresenter(self, presentCb):
        raise NotImplementedError
        return

    def unsubscribePresenter(self, presentCb):
        raise NotImplementedError
        return


class IEventsNotificationsController(IGameController):
    onEventNotificationsChanged = None

    def getEventsNotifications(self, filterFunc=None):
        raise NotImplementedError
        return


class IAnonymizerController(IGameController):
    onStateChanged = None

    @property
    def isInBattle(self):
        raise NotImplementedError
        return

    @property
    def isEnabled(self):
        raise NotImplementedError
        return

    @property
    def isRestricted(self):
        raise NotImplementedError
        return

    @property
    def isAnonymized(self):
        raise NotImplementedError
        return

    def setAnonymized(self, value):
        raise NotImplementedError
        return


class IAwardController(IGameController):
    pass


class IBoostersController(IGameController):
    onPersonalReserveTick = None
    onBoostersDataUpdate = None
    onClanReserveTick = None
    onGameModeStatusChange = None

    def isGameModeSupported(self, category):
        raise NotImplementedError
        return

    def selectRandomBattle(self):
        raise NotImplementedError
        return

    def shouldShowOnBoardingCardHint(self, boosterID):
        raise NotImplementedError
        return

    def setCardHintSeenFor(self, boosterID):
        raise NotImplementedError
        return

    def getExpirableBoosters(self):
        raise NotImplementedError
        return


class IScreenCastController(IGameController):
    pass


class IClanLockController(IGameController):
    onClanLockUpdate = None


class IVehicleComparisonBasket(IGameController):
    onChange = None
    onParametersChange = None
    onSwitchChange = None
    onNationChange = None

    def applyNewParameters(self, index, vehicle, crewLvl, crewSkills, selectedShellIndex=0):
        raise NotImplementedError
        return

    def addVehicle(self, vehicleCompactDesr, initParameters=None):
        raise NotImplementedError
        return

    def addVehicles(self, vehCDs):
        raise NotImplementedError
        return

    def removeVehicleByIdx(self, index):
        raise NotImplementedError
        return

    def removeAllVehicles(self):
        raise NotImplementedError
        return

    @property
    def maxVehiclesToCompare(self):
        raise NotImplementedError
        return

    def isFull(self):
        raise NotImplementedError
        return

    def isReadyToAdd(self, vehicle):
        raise NotImplementedError
        return

    @property
    def isLocked(self):
        raise NotImplementedError
        return

    def isAvailable(self):
        raise NotImplementedError
        return

    def isEnabled(self):
        raise NotImplementedError
        return

    def cloneVehicle(self, index):
        raise NotImplementedError
        return

    def getVehiclesCDs(self):
        raise NotImplementedError
        return

    def getVehiclesCount(self):
        raise NotImplementedError
        return

    def getVehicleAt(self, index):
        raise NotImplementedError
        return

    def getVehiclesPropertiesIter(self, getter):
        raise NotImplementedError
        return

    def writeCache(self):
        raise NotImplementedError
        return

    def revertVehicleByIdx(self, index):
        raise NotImplementedError
        return


class IChinaController(IGameController):

    def showBrowser(self):
        raise NotImplementedError
        return


class ITradeInController(IGameController):

    def getAllPossibleVehiclesToSell(self):
        raise NotImplementedError
        return

    def getAllPossibleVehiclesToBuy(self):
        raise NotImplementedError
        return

    def getPossibleVehiclesToBuy(self):
        raise NotImplementedError
        return

    def selectVehicleToBuy(self, vehCD):
        raise NotImplementedError
        return

    def getSelectedVehicleToBuy(self):
        raise NotImplementedError
        return

    def selectVehicleToSell(self, vehCD):
        raise NotImplementedError
        return

    def getSelectedVehicleToSell(self):
        raise NotImplementedError
        return

    def isEnabled(self):
        raise NotImplementedError
        return

    def hasAvailableOffer(self):
        raise NotImplementedError
        return

    def getExpirationTime(self):
        raise NotImplementedError
        return

    def getVehiclesToSell(self, respectSelectedVehicleToBuy):
        raise NotImplementedError
        return

    def getVehiclesToBuy(self, respectSelectedVehicleToSell):
        raise NotImplementedError
        return

    def getConfig(self):
        raise NotImplementedError
        return

    def getTradeInDiscounts(self, vehicle):
        raise NotImplementedError
        return

    def validatePossibleVehicleToBuy(self, vehicle):
        raise NotImplementedError
        return

    def getTradeInPrice(self, vehicle):
        raise NotImplementedError
        return

    def addTradeInPriceIfNeeded(self, vehicle, money):
        raise NotImplementedError
        return


class IQuestsController(IGameController):

    def getInventoryVehicles(self):
        raise NotImplementedError
        return

    def isNewbiePlayer(self):
        raise NotImplementedError
        return

    def getQuestForVehicle(self, vehicle):
        raise NotImplementedError
        return

    def getAllAvailableQuests(self):
        raise NotImplementedError
        return

    def isAnyQuestAvailable(self):
        raise NotImplementedError
        return

    def getFirstAvailableQuest(self):
        raise NotImplementedError
        return

    def getQuestGroups(self):
        raise NotImplementedError
        return

    def getCurrentModeQuestsForVehicle(self, vehicle, notCompleted=False):
        raise NotImplementedError
        return


class IRankedBattlesController(IGameController, ISeasonProvider):
    onEntitlementEvent = None
    onGameModeStatusTick = None
    onGameModeStatusUpdated = None
    onKillWebOverlays = None
    onUpdated = None
    onYearPointsChanges = None
    onSelectableRewardsChanged = None

    def isAccountMastered(self):
        raise NotImplementedError
        return

    def isEnabled(self):
        raise NotImplementedError
        return

    def isRankedPrbActive(self):
        raise NotImplementedError
        return

    def isRankedShopEnabled(self):
        raise NotImplementedError
        return

    def isSeasonRewarding(self):
        raise NotImplementedError
        return

    def isSuitableVehicle(self, vehicle):
        raise NotImplementedError
        return

    def isUnset(self):
        raise NotImplementedError
        return

    def isYearGap(self):
        raise NotImplementedError
        return

    def isYearLBEnabled(self):
        raise NotImplementedError
        return

    def isYearRewardEnabled(self):
        raise NotImplementedError
        return

    def hasSpecialSeason(self):
        raise NotImplementedError
        return

    def hasPrimeTimesTotalLeft(self):
        raise NotImplementedError
        return

    def hasPrimeTimesNextDayLeft(self):
        raise NotImplementedError
        return

    def hasSuitableVehicles(self):
        raise NotImplementedError
        return

    def suitableVehicleIsAvailable(self):
        raise NotImplementedError
        return

    def vehicleIsAvailableForBuy(self):
        raise NotImplementedError
        return

    def vehicleIsAvailableForRestore(self):
        raise NotImplementedError
        return

    def hasVehicleRankedBonus(self, compactDescr):
        raise NotImplementedError
        return

    def getAlertBlock(self):
        raise NotImplementedError
        return

    def getAwardTypeByPoints(self, points):
        return

    def getBonusBattlesMultiplier(self):
        raise NotImplementedError
        return

    def getClientRank(self):
        raise NotImplementedError
        return

    def getClientMaxRank(self):
        raise NotImplementedError
        return

    def getClientShields(self):
        raise NotImplementedError
        return

    def getClientSeasonInfo(self):
        raise NotImplementedError
        return

    def getClientSeasonInfoUpdateTime(self):
        raise NotImplementedError
        return

    def getClientEfficiency(self):
        raise NotImplementedError
        return

    def getClientEfficiencyDiff(self):
        raise NotImplementedError
        return

    def getClientBonusBattlesCount(self):
        raise NotImplementedError
        return

    def getCompensation(self, points):
        return

    def getCurrentDivision(self):
        raise NotImplementedError
        return

    def getCurrentPointToCrystalRate(self):
        return

    def getCurrentRank(self):
        raise NotImplementedError
        return

    def getDailyBattleQuests(self):
        raise NotImplementedError
        return

    def getDivision(self, rankID):
        raise NotImplementedError
        return

    def getDivisions(self):
        raise NotImplementedError
        return

    def getEntitlementEvents(self):
        raise NotImplementedError
        return

    def getExpectedSeasons(self):
        raise NotImplementedError
        return

    def getWebSeasonProvider(self):
        raise NotImplementedError
        return

    def getLeagueRewards(self, bonusName=None):
        raise NotImplementedError
        return

    def getMaxPossibleRank(self):
        raise NotImplementedError
        return

    def getMaxRank(self):
        raise NotImplementedError
        return

    def getRank(self, rankID):
        raise NotImplementedError
        return

    def getRankChangeStatus(self, changeInfo):
        raise NotImplementedError
        return

    def getRankDisplayInfoForBattle(self, rankID):
        raise NotImplementedError
        return

    def getRankedWelcomeCallback(self):
        raise NotImplementedError
        return

    def getQuestsForRank(self, rankID):
        raise NotImplementedError
        return

    def setRankedWelcomeCallback(self, value):
        raise NotImplementedError
        return

    def getRanksChain(self, leftRequiredBorder, rightRequiredBorder):
        raise NotImplementedError
        return

    def getRanksChainExt(self, currentProgress, lastProgress, maxProgress, shields, lastShields, isBonusBattle):
        raise NotImplementedError
        return

    def getRanksChanges(self, isLoser=False):
        return

    def getRanksTops(self, isLoser=False, stepDiff=None):
        return

    def getSoundManager(self):
        raise NotImplementedError
        return

    def getStatsComposer(self):
        raise NotImplementedError
        return

    def getSuitableVehicleLevels(self):
        raise NotImplementedError
        return

    def getTotalQualificationBattles(self):
        raise NotImplementedError
        return

    def getYearAwardsPointsMap(self):
        raise NotImplementedError
        return

    def getYearLBSize(self):
        raise NotImplementedError
        return

    def getYearLBState(self):
        raise NotImplementedError
        return

    def getYearRewards(self, points):
        raise NotImplementedError
        return

    def getCompletedYearQuest(self):
        raise NotImplementedError
        return

    def getYearRewardPoints(self):
        raise NotImplementedError
        return

    def getWebOpenPageCtx(self):
        raise NotImplementedError
        return

    def getQualificationQuests(self, quests=None):
        raise NotImplementedError
        return

    def awardWindowShouldBeShown(self, rankChangeInfo):
        raise NotImplementedError
        return

    def clearRankedWelcomeCallback(self):
        raise NotImplementedError
        return

    def clearWebOpenPageCtx(self):
        raise NotImplementedError
        return

    def runQuests(self, quests):
        raise NotImplementedError
        return

    def showRankedAwardWindow(self, rankedInfo, questsProgress):
        raise NotImplementedError
        return

    def showRankedBattlePage(self, ctx):
        raise NotImplementedError
        return

    def updateClientValues(self):
        raise NotImplementedError
        return

    def doActionOnEntryPointClick(self):
        raise NotImplementedError
        return

    def getYearRewardCount(self):
        raise NotImplementedError
        return


class IMarathonEventsController(IGameController):
    onFlagUpdateNotify = None
    onMarathonDataChanged = None
    onVehicleReceived = None

    def addMarathon(self, data):
        raise NotImplementedError
        return

    def delMarathon(self, prefix):
        raise NotImplementedError
        return

    def getMarathon(self, prefix):
        raise NotImplementedError
        return

    def getMarathons(self):
        raise NotImplementedError
        return

    def getPrimaryMarathon(self):
        raise NotImplementedError
        return

    def getFirstEnabledMarathon(self):
        raise NotImplementedError
        return

    def getPrefix(self, eventID):
        raise NotImplementedError
        return

    def getVisibleInPostBattleQuests(self):
        raise NotImplementedError
        return

    def getQuestsData(self, prefix=None, postfix=None):
        raise NotImplementedError
        return

    def getTokensData(self, prefix=None, postfix=None):
        raise NotImplementedError
        return

    def isAnyActive(self):
        raise NotImplementedError
        return

    def doesShowAnyMissionsTab(self):
        raise NotImplementedError
        return


class IEpicBattleMetaGameController(IGameController, ISeasonProvider):
    onUpdated = None
    onPrimeTimeStatusUpdated = None
    onEventEnded = None
    onGameModeStatusTick = None
    onBattleAbilitiesUpdated = None
    TOKEN_QUEST_ID = b''
    DAILY_QUEST_ID = b''
    FINAL_BADGE_QUEST_ID = b''

    def isEnabled(self):
        raise NotImplementedError
        return

    @property
    def enableWelcomeScreen(self):
        raise NotImplementedError
        return

    def isEpicPrbActive(self):
        raise NotImplementedError
        return

    def isCurrentCycleActive(self):
        raise NotImplementedError
        return

    def getLevelsToUpgradeAllReserves(self):
        raise NotImplementedError
        return

    def isBattlePassDataEnabled(self):
        raise NotImplementedError
        return

    def getTooltipData(self, tooltip):
        raise NotImplementedError
        return

    def isUnlockVehiclesInBattleEnabled(self):
        raise NotImplementedError
        return

    def isDailyQuestsUnlocked(self):
        raise NotImplementedError
        return

    def isDailyQuestsRefreshAvailable(self):
        raise NotImplementedError
        return

    def isMaxLevel(self):
        raise NotImplementedError
        return

    def getAlertBlock(self):
        raise NotImplementedError
        return

    def getDailyBattleQuests(self):
        raise NotImplementedError
        return

    def getPerformanceGroup(self):
        raise NotImplementedError
        return

    def getMaxPlayerLevel(self):
        raise NotImplementedError
        return

    def getCurrentLevel(self):
        raise NotImplementedError
        return

    def getCurrentProgress(self):
        raise NotImplementedError
        return

    def getStageLimit(self):
        raise NotImplementedError
        return

    def getNextLevelXP(self):
        raise NotImplementedError
        return

    def getAbilityPointsForLevel(self):
        raise NotImplementedError
        return

    def getValidVehicleLevels(self):
        raise NotImplementedError
        return

    def getUnlockableInBattleVehLevels(self):
        raise NotImplementedError
        return

    def getSuitableForQueueVehicleLevels(self):
        raise NotImplementedError
        return

    def getPointsProgressForLevel(self, level):
        raise NotImplementedError
        return

    def getPointsForLevel(self, level):
        raise NotImplementedError
        return

    def getLevelProgress(self):
        raise NotImplementedError
        return

    def getLevelForPoints(self, points):
        raise NotImplementedError
        return

    def getEpicSkills(self):
        raise NotImplementedError
        return

    def getAllSkillsInformation(self):
        raise NotImplementedError
        return

    def getGroupedSkills(self):
        raise NotImplementedError
        return

    def getPlayerLevelInfo(self):
        raise NotImplementedError
        return

    def getSkillLevelRanks(self):
        raise NotImplementedError
        return

    def getPlayerRanksInfo(self):
        raise NotImplementedError
        return

    def getPlayerRanksWithBonusInfo(self):
        raise NotImplementedError
        return

    def isRandomReservesModeEnabled(self):
        raise NotImplementedError
        return

    def getRandomReservesBonusProbability(self):
        raise NotImplementedError
        return

    def getSeasonData(self):
        raise NotImplementedError
        return

    def getCurrentSeasonID(self):
        raise NotImplementedError
        return

    def getSkillPoints(self):
        raise NotImplementedError
        return

    def getSkillLevels(self):
        raise NotImplementedError
        return

    def getSelectedSkills(self, vehicleCD):
        raise NotImplementedError
        return

    def increaseSkillLevel(self, skillID, callback=None):
        raise NotImplementedError
        return

    def changeEquippedSkills(self, skillIDArray, vehicleCD, callback=None, classVehs=False):
        raise NotImplementedError
        return

    def getAllUnlockedSkillInfoBySkillId(self):
        raise NotImplementedError
        return

    def getUnlockedAbilityIds(self):
        raise NotImplementedError
        return

    def getNumAbilitySlots(self, vehicleType):
        raise NotImplementedError
        return

    def getAbilitySlotsOrder(self, vehicleType):
        raise NotImplementedError
        return

    def getAbilitySlotsUnlockOrder(self, vehicleType):
        raise NotImplementedError
        return

    def getAllLevelRewards(self):
        raise NotImplementedError
        return

    def getLevelRewards(self, level):
        raise NotImplementedError
        return

    def getMergedLevelRewards(self):
        raise NotImplementedError
        return

    def isNeedToTakeReward(self):
        raise NotImplementedError
        return

    def getNotChosenRewardTokens(self):
        raise NotImplementedError
        return

    def getNotChosenRewardCount(self):
        raise NotImplementedError
        return

    def getReserveData(self, reserve):
        raise NotImplementedError
        return

    def isReserveStack(self, reserve):
        raise NotImplementedError
        return

    def getReserveCategory(self, reserve):
        raise NotImplementedError
        return

    def getReserveTechName(self, reserve):
        raise NotImplementedError
        return

    def setBattleTypeAsKnown(self):
        raise NotImplementedError
        return

    def selectEpicBattle(self):
        raise NotImplementedError
        return

    def showProgressionDuringSomeStates(self, showDefaultTab=False):
        raise NotImplementedError
        return

    def hasAnyOfferGiftToken(self):
        raise NotImplementedError
        return

    def replaceOfferByReward(self, bonuses):
        raise NotImplementedError
        return

    def replaceOfferByGift(self, bonuses):
        raise NotImplementedError
        return

    def getCurrentCycleInfo(self):
        raise NotImplementedError
        return

    def getCycleInfo(self, cycleID=None):
        raise NotImplementedError
        return

    def getCycleOrdinalNumber(self, cycleID):
        raise NotImplementedError
        return

    def getSeasonTimeRange(self):
        raise NotImplementedError
        return

    def getActiveSeason(self):
        raise NotImplementedError
        return

    def hasSuitableVehicles(self, additionalCriteria=None):
        raise NotImplementedError
        return

    def isCurVehicleSuitable(self, additionalCriteria=None):
        raise NotImplementedError
        return

    def getBaseEpicCriteria(self):
        raise NotImplementedError
        return

    def hasVehiclesToRent(self):
        raise NotImplementedError
        return

    def getStoredEpicDiscount(self):
        raise NotImplementedError
        return

    def getStats(self):
        raise NotImplementedError
        return

    def storeCycle(self):
        raise NotImplementedError
        return


class IBattleRoyaleController(IGameController, ISeasonProvider):
    onUpdated = None
    onBalanceUpdated = None
    onPrimeTimeStatusUpdated = None
    onWidgetUpdate = None
    onSubModeUpdated = None
    onStatusTick = None
    onTournamentBannerStateChanged = None
    onEntryPointUpdated = None
    TOKEN_QUEST_ID = b''

    def isEnabled(self):
        raise NotImplementedError
        return

    def isStPatrick(self):
        raise NotImplementedError
        return

    def getVehicleShells(self, vehicleName):
        raise NotImplementedError
        return

    def getPerformanceGroup(self):
        raise NotImplementedError
        return

    def getEndTime(self):
        raise NotImplementedError
        return

    def getStartTime(self):
        raise NotImplementedError
        return

    def getTimeLeftTillCycleEnd(self):
        raise NotImplementedError
        return

    def fightClick(self):
        raise NotImplementedError
        return

    def isActive(self):
        raise NotImplementedError
        return

    def isBattleRoyaleMode(self):
        raise NotImplementedError
        return

    def isBattlePassAvailable(self, bonusType):
        raise NotImplementedError
        return

    def isInBattleRoyaleSquad(self):
        raise NotImplementedError
        return

    def isInRandomSquadSubMode(self):
        raise NotImplementedError
        return

    def selectRoyaleBattle(self):
        raise NotImplementedError
        return

    def getCurrentSubModeID(self):
        raise NotImplementedError
        return

    def setCurrentSubModeID(self, subModeID, updateNeeded=True):
        raise NotImplementedError
        return

    def selectSubModeBattle(self, selectedSubModeID, **kwargs):
        raise NotImplementedError
        return

    def isGeneralHangarEntryPoint(self):
        raise NotImplementedError
        return

    def setDefaultHangarEntryPoint(self):
        raise NotImplementedError
        return

    def selectRandomBattle(self):
        raise NotImplementedError
        return

    def getVehicleEquipment(self, vehicleName):
        raise NotImplementedError
        return

    def getStats(self):
        raise NotImplementedError
        return

    def getBRCoinBalance(self):
        raise NotImplementedError
        return

    def getSTPCoinBalance(self):
        raise NotImplementedError
        return

    @staticmethod
    def getBrCommanderSkills():
        raise NotImplementedError
        return

    @staticmethod
    def showIntroWindow(ctx=None, parent=None, guiLoader=None):
        raise NotImplementedError
        return

    def getQuests(self):
        raise NotImplementedError
        return

    def isDailyQuestsRefreshAvailable(self):
        raise NotImplementedError
        return

    def showIntroVideo(self, alias, force=False):
        raise NotImplementedError
        return

    def getProgressionPointsTableData(self):
        raise NotImplementedError
        return

    def openInfoPageWindow(self, isModeSelector=False):
        raise NotImplementedError
        return

    def getTournamentBannerData(self):
        raise NotImplementedError
        return

    @property
    def isTournamentBannerEnabled(self):
        raise NotImplementedError
        return

    def getModeState(self):
        raise NotImplementedError
        return

    def hasDailyBonus(self, vehicle):
        raise NotImplementedError
        return

    def getStpCoinsPerPlace(self, place):
        raise NotImplementedError
        return


class IBattleRoyaleTournamentController(IGameController):
    onUpdatedParticipants = None
    onSelectBattleRoyaleTournament = None

    def isAvailable(self):
        raise NotImplementedError
        return

    def getSelectedToken(self):
        raise NotImplementedError
        return

    def getTokens(self):
        raise NotImplementedError
        return

    def updateParticipants(self, participants):
        raise NotImplementedError
        return

    def getParticipants(self):
        raise NotImplementedError
        return

    def selectBattleRoyaleTournament(self, token):
        raise NotImplementedError
        return

    def join(self, tokenStr):
        raise NotImplementedError
        return

    def leave(self):
        raise NotImplementedError
        return

    def ready(self, vehicleID):
        raise NotImplementedError
        return

    def notReady(self):
        raise NotImplementedError
        return

    def leaveCurrentAndJoinToAnotherTournament(self, tournamentID):
        raise NotImplementedError
        return

    def leaveBattleRoyaleTournament(self, isChangingToBattleRoyaleHangar=False):
        raise NotImplementedError
        return

    def isSelected(self):
        raise NotImplementedError
        return

    def resetReady(self):
        raise NotImplementedError
        return


class IManualController(IGameController):

    def isActivated(self):
        raise NotImplementedError
        return

    def clear(self):
        raise NotImplementedError
        return

    def getNewContentCount(self):
        raise NotImplementedError
        return

    def pageFilter(self, pageType):
        raise NotImplementedError
        return

    def show(self, lessonID=None):
        raise NotImplementedError
        return

    def getView(self):
        raise NotImplementedError
        return


class ICraftmachineController(IGameController):

    def getModuleName(self):
        raise NotImplementedError
        return


class IReferralProgramController(IGameController):
    onReferralStateChanged = None
    onReferralProgramUpdated = None

    @property
    def isEnabled(self):
        raise NotImplementedError
        return

    @property
    def isNewReferralSeason(self):
        raise NotImplementedError
        return

    def isFirstIndication(self):
        raise NotImplementedError
        return

    def getBubbleCount(self):
        raise NotImplementedError
        return

    def updateBubble(self):
        raise NotImplementedError
        return

    def setReferralHardDisabled(self, isDisabled):
        raise NotImplementedError
        return


class IClanNotificationController(IGameController):

    def getCounters(self, aliases=None):
        raise NotImplementedError
        return

    def setCounters(self, alias, count, isIncrement=False):
        raise NotImplementedError
        return

    def resetCounters(self):
        raise NotImplementedError
        return


class IFestivityController(IGameController):
    onStateChanged = None
    serverSettings = None

    def isEnabled(self):
        raise NotImplementedError
        return


class IBadgesController(IGameController):
    onUpdated = None

    def select(self, badges):
        raise NotImplementedError
        return

    def getPrefix(self):
        raise NotImplementedError
        return

    def getSuffix(self):
        raise NotImplementedError
        return


class ISpecialSoundCtrl(IGameController):

    @property
    def arenaMusicSetup(self):
        raise NotImplementedError
        return

    @property
    def specialVoice(self):
        raise NotImplementedError
        return

    def setPlayerVehicle(self, vehiclePublicInfo, isPlayerVehicle):
        raise NotImplementedError
        return

    def getVoiceoverByTankmanTagOrVehicle(self, tag):
        raise NotImplementedError
        return

    def getVoiceoverSpecialModesByTag(self, tag):
        raise NotImplementedError
        return

    def checkTagForSpecialVoice(self, tag):
        raise NotImplementedError
        return


class IBattlePassController(IGameController):
    onPointsUpdated = None
    onVehiclesPointsUpdated = None
    onLevelUp = None
    onBattlePassIsBought = None
    onSelectTokenUpdated = None
    onSeasonStateChanged = None
    onBattlePassSettingsChange = None
    onFinalRewardStateChange = None
    onRewardSelectChange = None
    onOffersUpdated = None
    onChapterChanged = None
    onExtraChapterExpired = None
    onEntitlementCacheUpdated = None

    def isEnabled(self):
        raise NotImplementedError
        return

    def isActive(self):
        raise NotImplementedError
        return

    def isVisible(self):
        raise NotImplementedError
        return

    def isDisabled(self):
        raise NotImplementedError
        return

    def isPaused(self):
        raise NotImplementedError
        return

    def isSeasonStarted(self):
        raise NotImplementedError
        return

    def isSeasonFinished(self):
        raise NotImplementedError
        return

    def isValidBattleType(self, prbEntity):
        raise NotImplementedError
        return

    def isCompleted(self):
        raise NotImplementedError
        return

    def getLevelByPoints(self, chapterID, points):
        raise NotImplementedError
        return

    def getProgressionByPoints(self, chapterID, points, level):
        raise NotImplementedError
        return

    def getMaxLevelInChapter(self, chapterId):
        raise NotImplementedError
        return

    def hasExtra(self):
        raise NotImplementedError
        return

    def getExtraChapterIDs(self):
        raise NotImplementedError
        return

    def isRegularProgressionCompleted(self):
        raise NotImplementedError
        return

    def isPostProgressionActive(self):
        raise NotImplementedError
        return

    def getRewardTypes(self, chapterID):
        raise NotImplementedError
        return

    def getFreeFinalRewardTypes(self, chapterID):
        raise NotImplementedError
        return

    def getPaidFinalRewardTypes(self, chapterID):
        raise NotImplementedError
        return

    def isChapterExists(self, chapterID):
        raise NotImplementedError
        return

    def getChapterIDs(self):
        raise NotImplementedError
        return

    def getMainChapterIDs(self):
        raise NotImplementedError
        return

    def getRegularChapterIDs(self):
        raise NotImplementedError
        return

    def isExtraChapter(self, chapterID):
        raise NotImplementedError
        return

    def isHoliday(self):
        raise NotImplementedError
        return

    def isAllMainChaptersBought(self):
        raise NotImplementedError
        return

    def getHolidayChapterID(self):
        raise NotImplementedError
        return

    def getBattlePassCost(self, chapterID):
        raise NotImplementedError
        return

    def getChapterExpiration(self, chapterID):
        raise NotImplementedError
        return

    def getChapterRemainingTime(self, chapterID):
        raise NotImplementedError
        return

    def getLevelInChapter(self, chapterID):
        raise NotImplementedError
        return

    def getCurrentChapterID(self):
        raise NotImplementedError
        return

    def getPostProgressionChapterID(self):
        raise NotImplementedError
        return

    def hasActiveChapter(self):
        raise NotImplementedError
        return

    def activateChapter(self, chapterID, seasonID=None):
        raise NotImplementedError
        return

    def getCurrentLevel(self):
        raise NotImplementedError
        return

    def getCurrentLevelWithPostProgress(self):
        raise NotImplementedError
        return

    def getState(self):
        raise NotImplementedError
        return

    def isBought(self, chapterID, seasonID=None):
        raise NotImplementedError
        return

    def isOfferEnabled(self):
        raise NotImplementedError
        return

    def isGameModeEnabled(self, arenaBonusType):
        raise NotImplementedError
        return

    def getVisibleGameModes(self):
        raise NotImplementedError
        return

    def getSupportedArenaBonusTypes(self):
        raise NotImplementedError
        return

    def getLevelPoints(self, chapterID, level):
        raise NotImplementedError
        return

    def getFullChapterPoints(self, chapterID):
        raise NotImplementedError
        return

    def isRareLevel(self, chapterID, level):
        raise NotImplementedError
        return

    def isFinalLevel(self, chapterID, level):
        raise NotImplementedError
        return

    def getChapterStarterPack(self, chapterID):
        raise NotImplementedError
        return

    def getSingleAward(self, chapterId, level, awardType=b'free', needSort=True):
        raise NotImplementedError
        return

    def getAwardsInterval(self, chapterId, fromLevel, toLevel, awardType=b'free'):
        raise NotImplementedError
        return

    def replaceOfferByReward(self, bonuses):
        raise NotImplementedError
        return

    def getPackedAwardsInterval(self, chapterId, fromLevel, toLevel, awardType=b'free'):
        raise NotImplementedError
        return

    def isNeedToTakeReward(self, chapterId, awardType, level):
        raise NotImplementedError
        return

    def isChooseRewardEnabled(self, awardType, chapterId, level):
        raise NotImplementedError
        return

    def canChooseAnyReward(self):
        raise NotImplementedError
        return

    def getLevelsConfig(self, chapterID):
        raise NotImplementedError
        return

    def getChapterConfig(self):
        raise NotImplementedError
        return

    def getChapterLevelInterval(self, chapterID):
        raise NotImplementedError
        return

    def getChapterState(self, chapterID):
        raise NotImplementedError
        return

    def isChapterActive(self, chapterID):
        raise NotImplementedError
        return

    def isChapterCompleted(self, chapterID):
        raise NotImplementedError
        return

    def getChapterIndex(self, chapterID):
        raise NotImplementedError
        return

    def getTankmenScreens(self):
        raise NotImplementedError
        return

    def getTankmenEntitlements(self):
        raise NotImplementedError
        return

    def tankmenCacheUpdate(self, isWaiting=False):
        raise NotImplementedError
        return

    def getRewardLogic(self):
        raise NotImplementedError
        return

    def getPointsInChapter(self, chapterID):
        raise NotImplementedError
        return

    def getLevelProgression(self, chapterID):
        raise NotImplementedError
        return

    def getCompletedCyclesCount(self, chapterID):
        raise NotImplementedError
        return

    def getPerBattlePoints(self, gameMode=ARENA_BONUS_TYPE.REGULAR, vehCompDesc=None):
        raise NotImplementedError
        return

    def getPerBattleRoyalePoints(self, gameMode=ARENA_BONUS_TYPE.BATTLE_ROYALE_SOLO, vehCompDesc=None, needPlacesWithoutPoints=False):
        raise NotImplementedError
        return

    def isSpecialVehicle(self, intCD):
        raise NotImplementedError
        return

    def getSpecialVehicles(self, gameMode=ARENA_BONUS_TYPE.REGULAR):
        raise NotImplementedError
        return

    def getPointsDiffForVehicle(self, intCD, gameMode=ARENA_BONUS_TYPE.REGULAR):
        raise NotImplementedError
        return

    def getVehicleProgression(self, intCD):
        raise NotImplementedError
        return

    def getSpecialVehicleCapBonus(self):
        raise NotImplementedError
        return

    def getVehicleCapBonus(self, intCD):
        raise NotImplementedError
        return

    def getSeasonTimeLeft(self):
        raise NotImplementedError
        return

    def getFinalOfferTimeLeft(self):
        raise NotImplementedError
        return

    def getSeasonStartTime(self):
        raise NotImplementedError
        return

    def getSeasonFinishTime(self):
        raise NotImplementedError
        return

    def hasMaxPointsOnVehicle(self, intCD):
        raise NotImplementedError
        return

    def isProgressionOnVehiclePossible(self, intCD):
        raise NotImplementedError
        return

    def getSeasonID(self):
        raise NotImplementedError
        return

    def getSeasonNum(self):
        raise NotImplementedError
        return

    def getCurrentCollectionId(self):
        raise NotImplementedError
        return

    def getFinalOfferTime(self):
        raise NotImplementedError
        return

    def getStylesConfig(self):
        raise NotImplementedError
        return

    def getNotChosenRewardCount(self):
        raise NotImplementedError
        return

    def getNotChosenRewardsIter(self):
        raise NotImplementedError
        return

    def getFreePoints(self):
        raise NotImplementedError
        return

    def takeRewardForLevel(self, chapterID, level):
        raise NotImplementedError
        return

    def takeAllRewards(self):
        raise NotImplementedError
        return

    def hasAnyOfferGiftToken(self):
        raise NotImplementedError
        return

    def getChapterStyleProgress(self, chapter):
        raise NotImplementedError
        return

    def isVoicedTankman(self, tankmanGroupName):
        raise NotImplementedError
        return

    def getSpecialTankmen(self):
        raise NotImplementedError
        return

    def getTankmenScreenID(self, chapterID):
        raise NotImplementedError
        return

    def getChapterToTankmenScreen(self):
        raise NotImplementedError
        return


class IHangarLoadingController(IGameController):
    onHangarLoadedAfterLogin = None

    def isHangarLoadedAfterLogin(self):
        raise NotImplementedError
        return


class IReactiveCommunicationService(IGameController):
    onChannelMessage = None
    onChannelClosed = None
    onSubscriptionClosed = None

    @property
    def isChannelSubscriptionAvailable(self):
        raise NotImplementedError
        return

    def subscribeToChannel(self, subscription):
        raise NotImplementedError
        return

    def unsubscribeFromChannel(self, subscription):
        raise NotImplementedError
        return

    def getLastMessageFromChannel(self, subscription):
        raise NotImplementedError
        return

    def getChannelHistory(self, name):
        raise NotImplementedError
        return

    def getChannelStatus(self, name):
        raise NotImplementedError
        return


class IRTSBattlesController(IGameController):

    def isVisible(self):
        raise NotImplementedError
        return


class IBlueprintsConvertSaleController(IGameController):
    pass


class IMapboxController(IGameController, ISeasonProvider):
    onPrimeTimeStatusUpdated = None
    onMapboxSurveyShown = None
    onMapboxSurveyCompleted = None

    @property
    def surveyManager(self):
        raise NotImplementedError
        return

    def addProgressionListener(self, listener):
        raise NotImplementedError
        return

    def removeProgressionListener(self, listener):
        raise NotImplementedError
        return

    def isEnabled(self):
        raise NotImplementedError
        return

    def isActive(self):
        raise NotImplementedError
        return

    def isMapboxMode(self):
        raise NotImplementedError
        return

    def isMapboxPrbActive(self):
        raise NotImplementedError
        return

    def isMapVisited(self, mapName):
        raise NotImplementedError
        return

    def addVisitedMap(self, mapName):
        raise NotImplementedError
        return

    def forceUpdateProgressData(self):
        raise NotImplementedError
        return

    def getAlertBlock(self):
        raise NotImplementedError
        return

    def getModeSettings(self):
        raise NotImplementedError
        return

    def getProgressionData(self):
        raise NotImplementedError
        return

    def getProgressionRestartTime(self):
        raise NotImplementedError
        return

    def getPrevBattlesPlayed(self):
        raise NotImplementedError
        return

    def getUnseenItemsCount(self):
        raise NotImplementedError
        return

    def handleSurveyCompleted(self, surveyData):
        raise NotImplementedError
        return

    def selectMapboxBattle(self):
        raise NotImplementedError
        return

    def setPrevBattlesPlayed(self, numBattles):
        raise NotImplementedError
        return

    def showMapboxInfoPage(self):
        raise NotImplementedError
        return

    def showSurvey(self, mapName):
        raise NotImplementedError
        return


class IOverlayController(IGameController):
    onStateChanged = None

    @property
    def isActive(self):
        raise NotImplementedError
        return

    def setOverlayState(self, state):
        raise NotImplementedError
        return

    def waitShow(self):
        raise NotImplementedError
        return


class ISteamCompletionController(IGameController):

    @property
    def isSteamAccount(self):
        raise NotImplementedError
        return

    @property
    def isLockNotificationManagerNeeded(self):
        raise NotImplementedError
        return

    @property
    def isAddEmailOverlayShown(self):
        raise NotImplementedError
        return

    @property
    def isConfirmEmailOverlayAllowed(self):
        raise NotImplementedError
        return

    def setAddEmailOverlayShown(self):
        raise NotImplementedError
        return

    def setConfirmEmailOverlayAllowed(self, isAllowed):
        raise NotImplementedError
        return


class IDemoAccCompletionController(IGameController):

    @property
    def isDemoAccount(self):
        raise NotImplementedError
        return

    @property
    def isDemoAccountOnce(self):
        raise NotImplementedError
        return

    @property
    def isInDemoAccRegistration(self):
        raise NotImplementedError
        return

    @isInDemoAccRegistration.setter
    def isInDemoAccRegistration(self, value):
        raise NotImplementedError
        return


class IMapsTrainingController(IGameController):
    onUpdated = None

    @property
    def isMapsTrainingEnabled(self):
        raise NotImplementedError
        return

    @property
    def isMapsTrainingPrbActive(self):
        raise NotImplementedError
        return

    @property
    def preferences(self):
        raise NotImplementedError
        return

    def showMapsTrainingQueue(self):
        raise NotImplementedError
        return

    def selectMapsTrainingMode(self):
        raise NotImplementedError
        return

    def selectRandomMode(self):
        raise NotImplementedError
        return

    def getSelectedMap(self):
        raise NotImplementedError
        return

    def setSelectedMap(self, mapName):
        raise NotImplementedError
        return

    def getSelectedVehicle(self):
        raise NotImplementedError
        return

    def updateSelectedVehicle(self):
        raise NotImplementedError
        return

    def setSelectedVehicle(self, vehicleName):
        raise NotImplementedError
        return

    def getSelectedTeam(self):
        raise NotImplementedError
        return

    def setSelectedTeam(self, team):
        raise NotImplementedError
        return

    def isValid(self):
        raise NotImplementedError
        return

    def reset(self):
        raise NotImplementedError
        return

    def requestInitialDataFromServer(self, callback):
        raise NotImplementedError
        return

    def getConfig(self):
        raise NotImplementedError
        return

    def onEnter(self):
        raise NotImplementedError
        return

    def onExit(self):
        raise NotImplementedError
        return

    def getPageCtx(self):
        raise NotImplementedError
        return

    def setExitSoundState(self):
        raise NotImplementedError
        return


class IVehiclePostProgressionController(IGameController):

    def isDisabledFor(self, vehicle, settings=None, skipRentalIsOver=False):
        raise NotImplementedError
        return

    def isEnabled(self):
        raise NotImplementedError
        return

    def isExistsFor(self, vehType, settings=None):
        raise NotImplementedError
        return

    def isSwitchSetupFeatureEnabled(self):
        raise NotImplementedError
        return

    def getSettings(self):
        raise NotImplementedError
        return

    def getInvalidProgressions(self, diff, existingIDs):
        raise NotImplementedError
        return

    def processVehExtData(self, vehType, extData):
        raise NotImplementedError
        return


class IWotPlusController(IGameController):
    onDataChanged = None
    onAttendanceUpdated = None
    onPendingRentChanged = None
    onEnabledStatusChanged = None
    onProBoostCooldownIsFinished = None

    def processSwitchNotifications(self):
        raise NotImplementedError
        return

    def selectIdleCrewXPVehicle(self, vehicleInvID, successCallback=None, errorCallback=None):
        raise NotImplementedError
        return

    def activateProBoostOnVehicle(self, vehicleInvID, successCallback=None, errorCallback=None):
        raise NotImplementedError
        return

    def hasSubscription(self):
        raise NotImplementedError
        return

    def getTier(self):
        raise NotImplementedError
        return

    def getBillingPeriod(self):
        raise NotImplementedError
        return

    def getProBoostedVehicleInvID(self):
        raise NotImplementedError
        return

    def getProBoostActivationTime(self):
        raise NotImplementedError
        return

    def isFreeToDemount(self, device):
        raise NotImplementedError
        return

    def getState(self):
        raise NotImplementedError
        return

    def hasSteamSubscription(self):
        raise NotImplementedError
        return

    def getExpiryTime(self):
        raise NotImplementedError
        return

    def getStartTime(self):
        raise NotImplementedError
        return

    def getGoldReserve(self):
        raise NotImplementedError
        return

    def hasVehicleCrewIdleXP(self, vehicleInvID):
        raise NotImplementedError
        return

    def getVehicleIDWithIdleXP(self):
        raise NotImplementedError
        return

    def getExclusiveVehicles(self):
        raise NotImplementedError
        return

    def toggleWotPlusDev(self):
        raise NotImplementedError
        return

    def activateWotPlusDev(self, expirySecondsInFuture):
        raise NotImplementedError
        return

    def simulateNewGameDay(self):
        raise NotImplementedError
        return

    def simulateWGMoneyBalanceUpdate(self):
        raise NotImplementedError
        return

    def setReservesDev(self, creditsVal, goldVal):
        raise NotImplementedError
        return

    def smashPiggyBankDev(self):
        raise NotImplementedError
        return

    def isWotPlusVisible(self):
        raise NotImplementedError
        return

    def onDailyAttendanceUpdate(self):
        raise NotImplementedError
        return

    def isDailyAttendanceQuest(self, questID):
        raise NotImplementedError
        return

    def getFormattedDailyAttendanceBonuses(self, bonuses):
        raise NotImplementedError
        return

    def getNextBillingTime(self):
        raise NotImplementedError
        return

    def hasOptDeviceAssistLoadout(self, vehicle):
        raise NotImplementedError
        return

    def getOptDeviceAssistPresets(self, vehicle):
        raise NotImplementedError
        return

    def getMostPopularOptDevicesLoadout(self, vehicle):
        raise NotImplementedError
        return

    def isCrewAssistEnabled(self):
        raise NotImplementedError
        return

    def hasCrewAssistOrderSets(self, vehIntCD, tankmanRole):
        raise NotImplementedError
        return

    def getCrewAssistOrderSets(self, vehIntCD, tankmanRole):
        raise NotImplementedError
        return

    def validateCrewAssistOrderSets(self, orderSets):
        raise NotImplementedError
        return

    def getSettingsStorage(self):
        raise NotImplementedError
        return

    def getServiceRecordBackgroundID(self):
        raise NotImplementedError
        return

    def getServiceRecordRibbonID(self):
        raise NotImplementedError
        return

    def canBeProBoosted(self, vehicleCD):
        raise NotImplementedError
        return

    def getSRCAssetManager(self):
        raise NotImplementedError
        return


class IEntitlementsConsumer(object):

    @property
    def isConsumesEntitlements(self):
        raise NotImplementedError
        return


class IEntitlementsController(IGameController):
    onCacheUpdated = None

    def updateCache(self, codes):
        raise NotImplementedError
        return

    def forceUpdateCache(self, codes):
        raise NotImplementedError
        return

    def getBalanceEntitlementFromCache(self, code):
        raise NotImplementedError
        return

    def isCacheInited(self):
        raise NotImplementedError
        return

    def getConsumedEntitlementFromCache(self, code):
        raise NotImplementedError
        return

    def getGrantedEntitlementFromCache(self, code):
        raise NotImplementedError
        return

    def isCodesWasFailedInLastRequest(self, codes):
        raise NotImplementedError
        return


class ILootBoxSystemController(IGameController):
    onBoxesAvailabilityChanged = None
    onStatusChanged = None
    onBoxesCountChanged = None
    onBoxesUpdated = None
    onBoxesInfoUpdated = None
    onBoxesConfigUpdated = None

    @property
    def eventNames(self):
        raise NotImplementedError
        return

    @property
    def mainEntryPoint(self):
        raise NotImplementedError
        return

    def isAvailable(self, eventName):
        raise NotImplementedError
        return

    def isActive(self, eventName):
        raise NotImplementedError
        return

    def isEnabled(self, eventName):
        raise NotImplementedError
        return

    def getActiveEvents(self):
        raise NotImplementedError
        return

    def getBoxesPriority(self, eventName):
        raise NotImplementedError
        return

    @property
    def isLootBoxesAvailable(self):
        raise NotImplementedError
        return

    def useStats(self, eventName):
        raise NotImplementedError
        return

    def getStatistics(self, eventName, boxID=None):
        raise NotImplementedError
        return

    def resetStatistics(self, boxIDs):
        raise NotImplementedError
        return

    def getSetting(self, eventName, setting):
        raise NotImplementedError
        return

    def setSetting(self, eventName, setting, value):
        raise NotImplementedError
        return

    def getActiveTime(self, eventName):
        raise NotImplementedError
        return

    def getBoxesCountToGuaranteed(self, category):
        raise NotImplementedError
        return

    def getBoxesCount(self, eventName, category=None):
        raise NotImplementedError
        return

    def getBoxesIDs(self, boxType):
        raise NotImplementedError
        return

    def getActiveBoxes(self, eventName, criteria=None):
        raise NotImplementedError
        return

    def getBoxes(self, eventName, criteria=None):
        raise NotImplementedError
        return

    def getBoxInfo(self, boxID):
        raise NotImplementedError
        return

    def getBoxInfoByCategory(self, boxCategory):
        raise NotImplementedError
        return

    def getBoxesInfo(self):
        raise NotImplementedError
        return

    def getBox(self, eventName, category):
        raise NotImplementedError
        return

    def isEnoughMoneyForReroll(self, box):
        raise NotImplementedError
        return

    def getPendingRerollRewards(self, eventName, category):
        raise NotImplementedError
        return


class ITelecomRentalsNotificationController(IGameController):

    def processSwitchNotifications(self):
        raise NotImplementedError
        return


class IEventBattlesController(IGameController, ISeasonProvider):
    onPrimeTimeStatusUpdated = None

    def isEnabled(self):
        raise NotImplementedError
        return

    def isAvailable(self):
        raise NotImplementedError
        return

    def isFrozen(self):
        raise NotImplementedError
        return

    def getConfig(self):
        raise NotImplementedError
        return


class IGiftSystemController(IGameController):
    onEventHubsCreated = None
    onEventHubsDestroyed = None

    def getEventHub(self, eventID):
        raise NotImplementedError
        return

    def getSettings(self):
        raise NotImplementedError
        return

    def requestWebState(self, eventID):
        raise NotImplementedError
        return


class ISeniorityAwardsController(IGameController):
    onUpdated = None
    onVehicleSelectionChanged = None
    onQuestsReceived = None

    @property
    def config(self):
        raise NotImplementedError
        return

    @property
    def isEnabled(self):
        raise NotImplementedError
        return

    @property
    def isActive(self):
        raise NotImplementedError
        return

    @property
    def isAvailable(self):
        raise NotImplementedError
        return

    @property
    def timeLeft(self):
        raise NotImplementedError
        return

    @property
    def endTime(self):
        raise NotImplementedError
        return

    @property
    def clockOnNotification(self):
        raise NotImplementedError
        return

    @property
    def isRewardReceived(self):
        raise NotImplementedError
        return

    @property
    def seniorityQuestPrefix(self):
        raise NotImplementedError
        return

    @property
    def claimVehicleRewardTokenPattern(self):
        raise NotImplementedError
        return

    @property
    def vehicleSelectionQuestPattern(self):
        raise NotImplementedError
        return

    @property
    def vehicleSelectionQuestPrefix(self):
        raise NotImplementedError
        return

    @property
    def vehicleSelectionToken(self):
        raise NotImplementedError
        return

    @property
    def categories(self):
        raise NotImplementedError
        return

    @property
    def maxCategory(self):
        raise NotImplementedError
        return

    @property
    def isEligibleToReward(self):
        raise NotImplementedError
        return

    @property
    def showRewardNotification(self):
        raise NotImplementedError
        return

    @property
    def showRewardHangarNotification(self):
        raise NotImplementedError
        return

    @property
    def isNeedToShowRewardNotification(self):
        raise NotImplementedError
        return

    @property
    def isNeedToShowNotificationBullet(self):
        raise NotImplementedError
        return

    @property
    def isVehicleSelectionAvailable(self):
        raise NotImplementedError
        return

    @property
    def yearsInGame(self):
        raise NotImplementedError
        return

    @property
    def yearTier(self):
        raise NotImplementedError
        return

    @property
    def pendingReminderTimestamp(self):
        raise NotImplementedError
        return

    @property
    def rewardCategory(self):
        raise NotImplementedError
        return

    @property
    def testGroup(self):
        raise NotImplementedError
        return

    @property
    def completedSeniorityAwardsQuests(self):
        raise NotImplementedError
        return

    @property
    def getVehiclesForSelectionCount(self):
        raise NotImplementedError
        return

    def isVehicleSelectionQuestCompleted(self, vehicleRewardId):
        raise NotImplementedError
        return

    def getVehicleSelectionRewards(self):
        raise NotImplementedError
        return

    def getAvailableVehicleSelectionRewards(self):
        raise NotImplementedError
        return

    def getVehicleSelectionQuestReward(self, vehicleRewardId):
        raise NotImplementedError
        return

    def claimReward(self):
        raise NotImplementedError
        return

    def markRewardReceived(self):
        raise NotImplementedError
        return

    def getSACoin(self):
        raise NotImplementedError
        return

    @staticmethod
    def getSeniorityLevel(completedQuests, regexp):
        raise NotImplementedError
        return


class IFunRandomController(IGameController):

    class IFunSubSystem(object):

        def fini(self):
            return

        def clear(self):
            return

    class IFunHiddenVehicles(IFunSubSystem):

        def startVehiclesListening(self):
            raise NotImplementedError
            return

        def stopVehiclesListening(self):
            raise NotImplementedError
            return

        def updateCurrentVehicle(self, desiredSubMode):
            raise NotImplementedError
            return

    class IFunNotifications(IFunSubSystem):

        def isNotificationsAllowed(self):
            raise NotImplementedError
            return

        def isNotificationsEnabled(self):
            raise NotImplementedError
            return

        def addToQueue(self, notification):
            raise NotImplementedError
            return

        def markSeenAsFrozen(self, subModesIDs):
            raise NotImplementedError
            return

        def pushNotification(self, notification):
            raise NotImplementedError
            return

        def startNotificationPushing(self):
            raise NotImplementedError
            return

        def stopNotificationPushing(self):
            raise NotImplementedError
            return

        def updateSettings(self, settings):
            raise NotImplementedError
            return

    class IFunProgressions(IFunSubSystem):

        def isProgressionExecutor(self, questID):
            raise NotImplementedError
            return

        def getActiveProgression(self):
            raise NotImplementedError
            return

        def getProgressionTimer(self):
            raise NotImplementedError
            return

        def getSettings(self):
            raise NotImplementedError
            return

        def startProgressListening(self):
            raise NotImplementedError
            return

        def stopProgressListening(self):
            raise NotImplementedError
            return

        def updateSettings(self, progressionSettings):
            raise NotImplementedError
            return

    class IFunSubscription(IFunSubSystem):

        def resume(self):
            raise NotImplementedError
            return

        def suspend(self):
            raise NotImplementedError
            return

        def addListener(self, eventType, handler, scope=None):
            raise NotImplementedError
            return

        def removeListener(self, eventType, handler, scope=None):
            raise NotImplementedError
            return

        def handleEvent(self, event, scope=None):
            raise NotImplementedError
            return

        def startCoreNotifications(self):
            raise NotImplementedError
            return

    class IFunSubModesHolder(IFunSubSystem):

        def getBattleSubMode(self, arenaVisitor=None):
            raise NotImplementedError
            return

        def getBattleSubModeID(self, arenaVisitor=None):
            raise NotImplementedError
            return

        def getDesiredSubMode(self):
            raise NotImplementedError
            return

        def getDesiredSubModeID(self):
            raise NotImplementedError
            return

        def getSubMode(self, subModeID):
            raise NotImplementedError
            return

        def getSubModes(self, subModesIDs=None, isOrdered=False):
            raise NotImplementedError
            return

        def getSubModesIDs(self):
            raise NotImplementedError
            return

        def setDesiredSubModeID(self, subModeID, trustedSource=False):
            raise NotImplementedError
            return

        def startNotification(self):
            raise NotImplementedError
            return

        def stopNotification(self):
            raise NotImplementedError
            return

        def updateSettings(self, prevSettings, newSettings):
            raise NotImplementedError
            return

    class IFunSubModesInfo(IFunSubSystem):

        def isAvailable(self):
            raise NotImplementedError
            return

        def isEntryPointAvailable(self):
            raise NotImplementedError
            return

        def getEventEndDate(self, now=None, subModesIDs=None):
            raise NotImplementedError
            return

        def getLeftTimeToPrimeTimesEnd(self, now=None, subModes=None):
            raise NotImplementedError
            return

        def getPrimeTimesForDay(self, selectedTime, groupIdentical=False):
            raise NotImplementedError
            return

        def getSubModesStatus(self, subModesIDs=None):
            raise NotImplementedError
            return

        def getPerformanceAlertGroup(self, subModesIDs=None):
            raise NotImplementedError
            return

    @property
    def hiddenVehicles(self):
        raise NotImplementedError
        return

    @property
    def notifications(self):
        raise NotImplementedError
        return

    @property
    def progressions(self):
        raise NotImplementedError
        return

    @property
    def subModesHolder(self):
        raise NotImplementedError
        return

    @property
    def subModesInfo(self):
        raise NotImplementedError
        return

    @property
    def subscription(self):
        raise NotImplementedError
        return

    def isEnabled(self):
        raise NotImplementedError
        return

    def isFunRandomPrbActive(self):
        raise NotImplementedError
        return

    def isOnlyFunRandomVehicle(self, vehicle):
        raise NotImplementedError
        return

    def getConfigurationModel(self):
        raise NotImplementedError
        return

    def getSettings(self):
        raise NotImplementedError
        return

    def setDesiredSubModeID(self, subModeID, trustedSource=False):
        raise NotImplementedError
        return

    def selectFunRandomBattle(self, desiredSubModeID, callback=None):
        raise NotImplementedError
        return


class IComp7Controller(IGameController, ISeasonProvider):
    onStatusUpdated = None
    onStatusTick = None
    onRankUpdated = None
    onModeConfigChanged = None
    onComp7RanksConfigChanged = None
    onBanUpdated = None
    onOfflineStatusUpdated = None
    onQualificationBattlesUpdated = None
    onQualificationStateUpdated = None
    onSeasonPointsUpdated = None
    onComp7RewardsConfigChanged = None
    onNewMaxRank = None
    onEntitlementsUpdated = None
    onEntitlementsUpdateFailed = None

    @property
    def rating(self):
        raise NotImplementedError
        return

    @property
    def isElite(self):
        raise NotImplementedError
        return

    @property
    def isBanned(self):
        raise NotImplementedError
        return

    @property
    def banDuration(self):
        raise NotImplementedError
        return

    @property
    def isOffline(self):
        raise NotImplementedError
        return

    @property
    def leaderboard(self):
        raise NotImplementedError
        return

    @property
    def progression(self):
        raise NotImplementedError
        return

    @property
    def activityPoints(self):
        raise NotImplementedError
        return

    @property
    def battleModifiers(self):
        raise NotImplementedError
        return

    @property
    def subModes(self):
        raise NotImplementedError
        return

    @property
    def qualificationBattlesNumber(self):
        raise NotImplementedError
        return

    @property
    def qualificationBattlesStatuses(self):
        raise NotImplementedError
        return

    @property
    def qualificationState(self):
        raise NotImplementedError
        return

    @property
    def remainingOfferTokensNotifications(self):
        raise NotImplementedError
        return

    @property
    def bans(self):
        raise NotImplementedError
        return

    @property
    def vehicleCopiesInfo(self):
        raise NotImplementedError
        return

    def getRanksConfig(self):
        raise NotImplementedError
        return

    def isEnabled(self):
        raise NotImplementedError
        return

    def isAvailable(self):
        raise NotImplementedError
        return

    def isFrozen(self):
        raise NotImplementedError
        return

    def isTrainingEnabled(self):
        raise NotImplementedError
        return

    def isVehicleBanEnabled(self):
        raise NotImplementedError
        return

    def isSuperSquadEnabled(self):
        raise NotImplementedError
        return

    def hasActiveSeason(self, includePreannounced=False):
        raise NotImplementedError
        return

    def getActualSeasonNumber(self, includePreannounced=False):
        raise NotImplementedError
        return

    def getCurrentSeason(self, now=None, includePreannounced=False):
        raise NotImplementedError
        return

    def isQualificationActive(self):
        raise NotImplementedError
        return

    def isQualificationResultsProcessing(self):
        raise NotImplementedError
        return

    def isQualificationCalculationRating(self):
        raise NotImplementedError
        return

    def isQualificationSquadAllowed(self):
        raise NotImplementedError
        return

    def preannounceSeasonId(self):
        raise NotImplementedError
        return

    def isInPreannounceState(self):
        raise NotImplementedError
        return

    def getPreannouncedSeason(self):
        raise NotImplementedError
        return

    def getRoleEquipmentKey(self, vehType):
        raise NotImplementedError
        return

    def getRoleEquipment(self, roleName):
        raise NotImplementedError
        return

    def getEquipmentStartLevel(self, roleName):
        raise NotImplementedError
        return

    def getRoleEquipmentOverrides(self, roleName):
        raise NotImplementedError
        return

    def getPoiEquipmentOverrides(self, poiName):
        raise NotImplementedError
        return

    def getViewData(self, viewAlias):
        raise NotImplementedError
        return

    def isSuitableVehicle(self, vehicle):
        raise NotImplementedError
        return

    def hasSuitableVehicles(self):
        raise NotImplementedError
        return

    def hasEnoughReadyToFightVehicles(self):
        raise NotImplementedError
        return

    def vehicleIsAvailableForBuy(self):
        raise NotImplementedError
        return

    def vehicleIsAvailableForRestore(self):
        raise NotImplementedError
        return

    def hasPlayableVehicle(self):
        raise NotImplementedError
        return

    def isModePrbActive(self):
        raise NotImplementedError
        return

    def isBattleModifiersAvailable(self):
        raise NotImplementedError
        return

    def getPlatoonRankRestriction(self, squadSize=None):
        raise NotImplementedError
        return

    def getPlatoonMaxRankRestriction(self):
        raise NotImplementedError
        return

    def getStatsSeasonsKeys(self):
        raise NotImplementedError
        return

    def getReceivedSeasonPoints(self):
        raise NotImplementedError
        return

    def getMaxAvailableSeasonPoints(self):
        raise NotImplementedError
        return

    def getYearlyRewards(self):
        raise NotImplementedError
        return

    def isQualificationPassedInSeason(self, seasonNumber):
        raise NotImplementedError
        return

    def getRatingForSeason(self, seasonNumber):
        raise NotImplementedError
        return

    def getMaxRankNumberForSeason(self, seasonNumber=None):
        raise NotImplementedError
        return

    def isEliteForSeason(self, seasonNumber=None):
        raise NotImplementedError
        return

    def updateEntitlementsCache(self, force=False, retryTimes=None):
        raise NotImplementedError
        return

    def tryToShowSeasonStatistics(self):
        raise NotImplementedError
        return


class IComp7LightController(IGameController, ISeasonProvider):
    onStatusUpdated = None
    onStatusTick = None
    onModeConfigChanged = None

    @property
    def isBanned(self):
        raise NotImplementedError
        return

    @property
    def isOffline(self):
        raise NotImplementedError
        return

    @property
    def battleModifiers(self):
        raise NotImplementedError
        return

    def isEnabled(self):
        raise NotImplementedError
        return

    def isFrozen(self):
        raise NotImplementedError
        return

    def isAvailable(self):
        raise NotImplementedError
        return

    def isSuitableVehicle(self, vehicle):
        raise NotImplementedError
        return

    def hasSuitableVehicles(self):
        raise NotImplementedError
        return

    def isModePrbActive(self):
        raise NotImplementedError
        return

    def isProgressionActive(self):
        raise NotImplementedError
        return

    def vehicleIsAvailableForBuy(self):
        raise NotImplementedError
        return

    def vehicleIsAvailableForRestore(self):
        raise NotImplementedError
        return

    def getPreannouncedSeason(self):
        raise NotImplementedError
        return

    def getRoleEquipmentKey(self, vehType):
        raise NotImplementedError
        return

    def getRoleEquipment(self, roleName):
        raise NotImplementedError
        return

    def getEquipmentStartLevel(self, roleName):
        raise NotImplementedError
        return

    def getRoleEquipmentOverrides(self, roleName):
        raise NotImplementedError
        return

    def getPoiEquipmentOverrides(self, poiName):
        raise NotImplementedError
        return

    def getCurrentSeason(self, now=None, includePreannounced=False):
        raise NotImplementedError
        return

    def isBattleModifiersAvailable(self):
        raise NotImplementedError
        return


class IHangarSpaceSwitchController(IGameController):
    onCheckSceneChange = None
    onSpaceUpdated = None

    def hangarSpaceUpdate(self, sceneName):
        raise NotImplementedError
        return

    def lockHangarOverride(self, sceneName):
        raise NotImplementedError
        return


class ICollectionsSystemController(IGameController):
    onServerSettingsChanged = None
    onBalanceUpdated = None
    onAvailabilityChanged = None

    @property
    def cache(self):
        raise NotImplementedError
        return

    def isEnabled(self):
        raise NotImplementedError
        return

    def getCollections(self, reverseSort=False):
        raise NotImplementedError
        return

    def getCollection(self, collectionId):
        raise NotImplementedError
        return

    def getCollectionByName(self, collectionName):
        raise NotImplementedError
        return

    def isRelatedEventActive(self, collectionId):
        raise NotImplementedError
        return

    def getLinkedCollections(self, collectionId):
        raise NotImplementedError
        return

    def getCollectionIDs(self):
        raise NotImplementedError
        return

    def getCollectionItem(self, collectionId, itemId):
        raise NotImplementedError
        return

    def getNewLinkedCollectionsItemCount(self, collectionId):
        raise NotImplementedError
        return

    def getNewCollectionItemCount(self, collectionId):
        raise NotImplementedError
        return

    def getReceivedItemCount(self, collectionId):
        raise NotImplementedError
        return

    def isCollectionCompleted(self, collectionId):
        raise NotImplementedError
        return

    def getMaxItemCount(self, collectionId):
        raise NotImplementedError
        return

    def getMaxProgressItemCount(self, collectionId):
        raise NotImplementedError
        return

    def getReceivedProgressItemCount(self, collectionId):
        raise NotImplementedError
        return

    def isRewardReceived(self, collectionId, requiredCount):
        raise NotImplementedError
        return

    def isItemReceived(self, collectionId, itemId):
        raise NotImplementedError
        return


class IWinbackController(IGameController):
    onConfigUpdated = None
    onStateUpdated = None

    @property
    def winbackConfig(self):
        raise NotImplementedError
        return

    @property
    def winbackQuests(self):
        raise NotImplementedError
        return

    @property
    def winbackPromoURL(self):
        raise NotImplementedError
        return

    def isEnabled(self):
        raise NotImplementedError
        return

    def isModeAvailable(self):
        raise NotImplementedError
        return

    def isProgressionAvailable(self):
        raise NotImplementedError
        return

    def isWinbackQuest(self, quest):
        raise NotImplementedError
        return

    def parseOfferToken(self, token):
        raise NotImplementedError
        return

    def getQuestIdx(self, quest):
        raise NotImplementedError
        return

    def getQuestType(self, questID):
        raise NotImplementedError
        return

    def isFinished(self):
        raise NotImplementedError
        return

    def isWinbackOfferToken(self, offerToken):
        raise NotImplementedError
        return

    def hasWinbackOfferToken(self):
        raise NotImplementedError
        return

    def getWinbackBattlesCountLeft(self):
        raise NotImplementedError
        return

    def isPromoEnabled(self):
        raise NotImplementedError
        return


class IAchievements20EarningController(IGameController):

    def pause(self):
        raise NotImplementedError
        return

    def resume(self):
        raise NotImplementedError
        return


class IAchievements20Controller(IGameController):
    onUpdate = None
    onRankIncrease = None
    onRankDecrease = None

    def showNewSummaryEnabled(self):
        raise NotImplementedError
        return

    def showRatingUpgrade(self):
        raise NotImplementedError
        return

    def showRatingChanged(self):
        raise NotImplementedError
        return

    def showRankedComplete(self):
        raise NotImplementedError
        return

    def showEditAvailable(self):
        raise NotImplementedError
        return

    def onSummaryPageVisited(self):
        raise NotImplementedError
        return

    def getAchievementsTabCounter(self):
        raise NotImplementedError
        return

    def getPrevAchievementsList(self):
        raise NotImplementedError
        return

    def setPrevAchievementsList(self, value):
        raise NotImplementedError
        return

    def getInitialBattleCount(self):
        raise NotImplementedError
        return

    def setInitialBattleCount(self, value):
        raise NotImplementedError
        return

    def getWtrPrevPointsNotification(self):
        raise NotImplementedError
        return

    def setMaxWtrPoints(self, points):
        raise NotImplementedError
        return

    def getMaxWtrPoints(self):
        raise NotImplementedError
        return

    def setWtrPrevPointsNotification(self, points):
        raise NotImplementedError
        return

    def getWtrPrevPoints(self):
        raise NotImplementedError
        return

    def setWtrPrevPoints(self, points):
        raise NotImplementedError
        return

    def getWtrPrevRank(self):
        raise NotImplementedError
        return

    def setWtrPrevRank(self, rank):
        raise NotImplementedError
        return

    def getWtrPrevSubRank(self):
        raise NotImplementedError
        return

    def setWtrPrevSubRank(self, subRank):
        raise NotImplementedError
        return

    def getFirstEntryStatus(self):
        raise NotImplementedError
        return

    def setFirstEntryStatus(self, value):
        raise NotImplementedError
        return

    def getRatingCalculatedStatus(self):
        raise NotImplementedError
        return

    def setRatingCalculatedStatus(self, value):
        raise NotImplementedError
        return

    def getMedalAddedStatus(self):
        raise NotImplementedError
        return

    def setMedalAddedStatus(self, value):
        raise NotImplementedError
        return

    def getAchievementEditingEnabledStatus(self):
        raise NotImplementedError
        return

    def setAchievementEditingEnabledStatus(self, value):
        raise NotImplementedError
        return

    def getRatingChangedStatus(self):
        raise NotImplementedError
        return

    def setRatingChangedStatus(self, value):
        raise NotImplementedError
        return

    def getMedalCountInfo(self):
        raise NotImplementedError
        return

    def setMedalCountInfo(self, value):
        raise NotImplementedError
        return


class ILimitedUIController(IGameController):
    onStateChanged = None
    onConfigChanged = None
    onVersionUpdated = None

    @property
    def isEnabled(self):
        raise NotImplementedError
        return

    @property
    def isInited(self):
        raise NotImplementedError
        return

    @property
    def configVersion(self):
        raise NotImplementedError
        return

    @property
    def version(self):
        raise NotImplementedError
        return

    @property
    def isUserSettingsMayShow(self):
        raise NotImplementedError
        return

    def isRuleCompleted(self, ruleID):
        raise NotImplementedError
        return

    def completeRule(self, ruleID):
        raise NotImplementedError
        return

    def completeAllRules(self):
        raise NotImplementedError
        return

    def completeAllRulesByTypes(self, ruleTypes):
        raise NotImplementedError
        return

    def startObserve(self, ruleID, handler):
        raise NotImplementedError
        return

    def startObserves(self, ruleIDs, handler):
        raise NotImplementedError
        return

    def stopObserve(self, ruleID, handler):
        raise NotImplementedError
        return

    def stopObserves(self, ruleIDs, handler):
        raise NotImplementedError
        return


class IHangarGuiController(IGameController):

    class IHangarGuiSubSystem(object):

        def init(self):
            return

        def fini(self):
            return

    class IHangarGuiProvidersHolder(IHangarGuiSubSystem):

        def getBonusGuiProvider(self, bonusType):
            raise NotImplementedError
            return

        def getCurrentGuiProvider(self, defaultQueueType):
            raise NotImplementedError
            return

    class IHangarGuiDynamicEconomics(IHangarGuiSubSystem):

        def checkBonusCaps(self, bonusType, bonusCaps):
            raise NotImplementedError
            return

        def checkCurrentBonusCaps(self, bonusCaps, default=False):
            raise NotImplementedError
            return

        def checkCrystalRewards(self, bonusType):
            raise NotImplementedError
            return

        def checkCurrentCrystalRewards(self, default=False):
            raise NotImplementedError
            return

    class IHangarGuiScaleformController(IHangarGuiSubSystem):

        @property
        def currentPresetGetter(self):
            raise NotImplementedError
            return

        def isComponentAvailable(self, componentType):
            raise NotImplementedError
            return

        def getCurrentPreset(self):
            raise NotImplementedError
            return

        def holdHangar(self, hangar):
            raise NotImplementedError
            return

        def releaseHangar(self):
            raise NotImplementedError
            return

        def updateChangeableComponents(self, isVisible, forced=False):
            raise NotImplementedError
            return

        def updateComponentsVisibility(self, preset=None):
            raise NotImplementedError
            return

    @property
    def currentGuiProvider(self):
        raise NotImplementedError
        return

    @property
    def dynamicEconomics(self):
        raise NotImplementedError
        return

    @property
    def sfController(self):
        raise NotImplementedError
        return


class IGraphicsOptimizationController(IGameController):
    onUiVisibilityToggled = None
    onSettingsChanged = None

    def getConfig(self):
        raise NotImplementedError
        return

    def updateConfig(self, config):
        raise NotImplementedError
        return

    def registerOptimizationArea(self, x, y, width, height):
        raise NotImplementedError
        return

    def unregisterOptimizationArea(self, optimizationId):
        raise NotImplementedError
        return

    def updateOptimizationArea(self, optimizationId, x, y, width, height):
        raise NotImplementedError
        return

    def switchOptimizationEnabled(self, value):
        raise NotImplementedError
        return

    def getEnable(self):
        raise NotImplementedError
        return

    def isOptimizationEnabled(self, alias):
        raise NotImplementedError
        return

    def isOptimizationAvailable(self, alias):
        raise NotImplementedError
        return


class ILiveOpsWebEventsController(IGameController):
    onSettingsChanged = None
    onEventStateChanged = None

    @property
    def eventConfig(self):
        raise NotImplementedError
        return

    @property
    def eventUniqueName(self):
        raise NotImplementedError
        return

    def isEnabled(self):
        raise NotImplementedError
        return

    @property
    def eventUrl(self):
        raise NotImplementedError
        return

    @property
    def preEventStart(self):
        raise NotImplementedError
        return

    @property
    def eventStart(self):
        raise NotImplementedError
        return

    @property
    def postEventEnd(self):
        raise NotImplementedError
        return

    @property
    def eventEnd(self):
        raise NotImplementedError
        return

    @property
    def eventState(self):
        raise NotImplementedError
        return

    @property
    def previousEventState(self):
        raise NotImplementedError
        return

    @property
    def isEntryPointSmall(self):
        raise NotImplementedError
        return

    @property
    def isHighQualityPreset(self):
        raise NotImplementedError
        return

    def canShowHangarEntryPoint(self):
        raise NotImplementedError
        return

    def canShowEventsTab(self):
        raise NotImplementedError
        return

    def getEventTabVisited(self):
        raise NotImplementedError
        return

    def markEventTabVisited(self):
        raise NotImplementedError
        return

    def getIsFirstEventEntry(self):
        raise NotImplementedError
        return

    def markEventEntered(self):
        raise NotImplementedError
        return


class IAchievementsController(IGameController):
    onUpdate = None
    onNewAchievementsEarned = None
    onUnseenAchievementsUpdate = None

    def getCurrentScore(self, userId=None):
        raise NotImplementedError
        return

    def getTotalScore(self):
        raise NotImplementedError
        return

    def getProgress(self, userId=None):
        raise NotImplementedError
        return

    def getTrophiesAchievementsScore(self, userId=None):
        raise NotImplementedError
        return

    def getTrophiesAchievements(self, userId=None):
        raise NotImplementedError
        return

    def getTotalAchievementsCount(self, userId=None):
        raise NotImplementedError
        return

    def getAchievementByID(self, achievementID, achievementCategory):
        raise NotImplementedError
        return

    def getPrevAchievementsScore(self):
        raise NotImplementedError
        return

    def setPrevAchievementsScore(self, value):
        raise NotImplementedError
        return

    def getPrevPlayerCollectionProgress(self):
        raise NotImplementedError
        return

    def setPrevPlayerCollectionProgress(self, value):
        raise NotImplementedError
        return

    def getPrevTrophy(self):
        raise NotImplementedError
        return

    def setPrevTrophy(self, value):
        raise NotImplementedError
        return

    def getUnseenAdvancedAchievementsCount(self, achievementCategory, achievementID, userId=None):
        raise NotImplementedError
        return

    def seeUnseenAdvancedAchievement(self, achievementCategory, achievementID):
        raise NotImplementedError
        return

    def seeUnseenTrophiesAdvancedAchievement(self, achievementCategory, achievementID):
        raise NotImplementedError
        return

    def getTotalUnseenAdvancedAchievementsCount(self):
        raise NotImplementedError
        return

    def initUnseenAdvancedAchievements(self, achievementsData):
        raise NotImplementedError
        return

    def getUnseenTrophiesAdvancedAchievementsCount(self, userId=None):
        raise NotImplementedError
        return

    def getUnseenAdvancedAchievements(self, achievementCategory):
        raise NotImplementedError
        return

    def getSeenTrophiesAdvancedAchievements(self, achievementCategory):
        raise NotImplementedError
        return

    def getPrevCategoryData(self):
        raise NotImplementedError
        return

    def setPrevCategoryData(self, value):
        raise NotImplementedError
        return

    def getMainAdvancedAchievementsPageVisited(self):
        raise NotImplementedError
        return

    def setMainAdvancedAchievementsPageVisited(self, value):
        raise NotImplementedError
        return

    def getShowHint(self):
        raise NotImplementedError
        return

    def setShowHint(self, value):
        raise NotImplementedError
        return


class IExchangeRateWithDiscountsOperations(object):

    def calculateExchange(self, goldAmount):
        raise NotImplementedError
        return

    def calculateGoldToExchange(self, resourceAmount):
        raise NotImplementedError
        return

    def calculateResourceToExchange(self, resourceAmount):
        raise NotImplementedError
        return


class IExchangeRate(object):
    onUpdated = None

    @property
    def getExchangeRateName(self):
        raise NotImplementedError
        return

    @property
    def defaultRate(self):
        raise NotImplementedError
        return

    @property
    def unlimitedDiscountInfo(self):
        raise NotImplementedError
        return

    @property
    def allPersonalLimitedDiscounts(self):
        raise NotImplementedError
        return


class IExchangeRateWithDiscounts(IExchangeRate, IExchangeRateWithDiscountsOperations):

    def init(self):
        raise NotImplementedError
        return

    def fini(self):
        raise NotImplementedError
        return

    @property
    def unlimitedRateAfterMainDiscount(self):
        raise NotImplementedError
        return

    @property
    def unlimitedDiscountRate(self):
        raise NotImplementedError
        return

    @property
    def bestPersonalDiscount(self):
        raise NotImplementedError
        return

    @property
    def commonServerDiscountRate(self):
        raise NotImplementedError
        return

    @property
    def discountRate(self):
        raise NotImplementedError
        return

    @property
    def discountInfo(self):
        raise NotImplementedError
        return

    @property
    def exchangeDiscountPercent(self):
        raise NotImplementedError
        return

    def isDiscountAvailable(self):
        raise NotImplementedError
        return


class IExchangeRatesWithDiscountsProvider(IGameController):

    def get(self, rateType):
        raise NotImplementedError
        return

    @property
    def goldToCredits(self):
        raise NotImplementedError
        return

    @property
    def freeXpTranslation(self):
        raise NotImplementedError
        return

    def exchange(self, currency, toCurrency, amount):
        raise NotImplementedError
        return


class IFadingController(IGameController):

    def show(self, layerID):
        raise NotImplementedError
        return

    def hide(self, layerID):
        raise NotImplementedError
        return


class IEasyTankEquipController(IGameController):
    onUpdated = None

    @property
    def config(self):
        raise NotImplementedError
        return

    def getLoadoutByVehicleID(self, vehicleID):
        raise NotImplementedError
        return


class ILoadoutController(IGameController):
    onInteractorUpdated = None
    onSlotSelected = None
    onUpdateFromItem = None
    onResetItem = None
    onSpecializationSelect = None

    @property
    def interactor(self):
        raise NotImplementedError
        return

    def setInteractor(self, interactor):
        raise NotImplementedError
        return

    def clearInteractor(self):
        raise NotImplementedError
        return


class ICommendationsController(IGameController):
    onSettingsChanged = None

    @property
    def isCommendationsEnabled(self):
        raise NotImplementedError
        return

    @property
    def isLiveTagsEnabled(self):
        raise NotImplementedError
        return


class IOitAvailabilityController(IGameController):

    def isOitEnabledForPreset(self, qualityLevel):
        raise NotImplementedError
        return


class IVehiclePlaylistsController(IGameController):
    onEnabledStatusChanged = None
    onModifiedPlaylistDiscarded = None
    onDirtyClean = None
    onPlaylistSaved = None

    @property
    def isEnabled(self):
        raise NotImplementedError
        return

    def updateModifiedPlaylist(self, plStrID, playlistData):
        raise NotImplementedError
        return

    def setInitialModifiedPlaylist(self, plStrID, playlistData):
        raise NotImplementedError
        return

    def discardModifiedPlaylist(self):
        raise NotImplementedError
        return

    def generateId(self):
        raise NotImplementedError
        return

    def clearModifiedPlaylist(self):
        raise NotImplementedError
        return

    def saveModifiedPlaylist(self):
        raise NotImplementedError
        return

    def setModifiedPlaylistChanged(self, isChanged):
        raise NotImplementedError
        return

    @property
    def isModifiedPlaylistChanged(self):
        raise NotImplementedError
        return

    def createPlaylist(self, plStrID, playlistData):
        raise NotImplementedError
        return

    def deletePlaylist(self, plStrID):
        raise NotImplementedError
        return

    def getPlaylistDataByID(self, plStrID):
        raise NotImplementedError
        return

    def getSelectedID(self):
        raise NotImplementedError
        return

    def setSelectedID(self, val):
        raise NotImplementedError
        return

    def iterPlaylists(self):
        raise NotImplementedError
        return

    def initPlayLists(self):
        raise NotImplementedError
        return

    def simplePlayListParser(self, pStrData):
        raise NotImplementedError
        return


class IBlurController(IGameController):

    def createBlur(self, config):
        raise NotImplementedError
        return

    def getSettingsByAlias(self, alias):
        raise NotImplementedError
        return


class IBlurEffect(object):

    def fini(self):
        return

    def enable(self):
        raise NotImplementedError
        return

    def disable(self):
        raise NotImplementedError
        return

    @property
    def config(self):
        raise NotImplementedError
        return

    def updateConfig(self, config):
        raise NotImplementedError
        return


class ICrewController(IGameController):
    onJunkStatusChanged = None

    def setWidgetData(self, viewKey):
        raise NotImplementedError
        return

    def getWidgetData(self):
        raise NotImplementedError
        return


class IIngameTournamentController(IGameController):
    onTournamentEntryPointUpdated = None
    onTournamentWGCGDataUpdated = None

    def isTournamentAvailable(self, tournamentType):
        raise NotImplementedError
        return

    def getTournamentState(self, tournamentType):
        raise NotImplementedError
        return

    def getCurrentShowmatch(self, tournamentType):
        raise NotImplementedError
        return

    def getNextShowmatch(self, tournamentType):
        raise NotImplementedError
        return

    def getTournamentShowmatchPeriod(self, tournamentType):
        raise NotImplementedError
        return

    def getIsIntroSeen(self, tournamentType):
        raise NotImplementedError
        return

    def setIsIntroSeen(self, tournamentType):
        raise NotImplementedError
        return

    def requestTournamentWGCGData(self):
        raise NotImplementedError
        return

    def openShop(self, tournamentType):
        raise NotImplementedError
        return

    def getTokenStoreOpeningTime(self, tournamentType):
        raise NotImplementedError
        return

    def getOfferGiftsToken(self, tournamentType):
        raise NotImplementedError
        return

    def openOfferGifts(self, tournamentType, overrideOnBackCallback):
        raise NotImplementedError
        return


class IW2GTGameController(IGameController):

    @property
    def isEnabled(self):
        raise NotImplementedError
        return

    @property
    def isEnabledByServer(self):
        raise NotImplementedError
        return

    @property
    def w2gtConfig(self):
        raise NotImplementedError
        return

    def getTips(self, geometryName, gameplayID, vehRole, vehLevel, team):
        raise NotImplementedError
        return

    def saveProgress(self, arenaUniqueID, playerID, progress):
        raise NotImplementedError
        return

    def getProgress(self, arenaUniqueID, playerID):
        raise NotImplementedError
        return


class IRestBonusController(IGameController):
    onUpdated = None

    @property
    def dailyXPFactor(self):
        raise NotImplementedError
        return

    @property
    def restBonusQuests(self):
        raise NotImplementedError
        return

    def isRestBonusQuestID(self, quest):
        raise NotImplementedError
        return

    def getXpFactor(self, vehicle):
        raise NotImplementedError
        return

    def getActualXPFactor(self, vehicle):
        raise NotImplementedError
        return

    def getRestBonusExpiryTime(self):
        raise NotImplementedError
        return

    def getDailyResetTime(self):
        raise NotImplementedError
        return

    def hasActiveBattleQuest(self, vehicle):
        raise NotImplementedError
        return
