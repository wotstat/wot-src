import typing
from constants import ARENA_BONUS_TYPE
from enum import Enum
if typing.TYPE_CHECKING:
    from typing import Any, Callable, Dict, Generator, Iterable, Iterator, List, Optional, Sequence, Set, Tuple, Union
    from armory_yard.gui.game_control.armory_yard_controller import _ServerSettings
    from battle_pass_common import FinalReward
    from collections_common import Collection, CollectionItem
    from Event import Event
    from gui.collection.resources.cdn.cache import CollectionsCdnCacheMgr
    from fun_random.gui.feature.models.common import FunSubModesStatus
    from fun_random.gui.feature.models.notifications import FunNotification
    from fun_random.gui.feature.models.progressions import FunProgression
    from fun_random.gui.feature.sub_modes.base_sub_mode import IFunSubMode
    from fun_random.helpers.server_settings import FunRandomConfig, FunMetaProgressionConfig
    from fun_random.gui.shared.events import FunEventScope, FunEventType
    from gui.Scaleform.daapi.view.lobby.comp7.shared import Comp7AlertData
    from gui.Scaleform.daapi.view.lobby.hangar.Hangar import Hangar
    from gui.battle_pass.state_machine.delegator import BattlePassRewardLogic
    from gui.comp7.entitlements_cache import EntitlementsCache
    from gui.game_control.comp7_controller import _LeaderboardDataProvider
    from gui.game_control.epic_meta_game_ctrl import EpicMetaGameSkill
    from gui.game_control.mapbox_controller import ProgressionData
    from gui.game_control.trade_in import TradeInDiscounts
    from gui.game_control.early_access_controller import _EarlyAccessSystemMessagesController
    from gui.gift_system.hubs.base.hub_core import IGiftEventHub
    from gui.hangar_presets.hangar_gui_config import HangarGuiPreset
    from gui.limited_ui.lui_rules_storage import LuiRules
    from gui.limited_ui.lui_representations_storage import LimitedUIConditionRepresentation
    from gui.mapbox.mapbox_survey_manager import MapboxSurveyManager
    from gui.periodic_battles.models import AlertData, PeriodInfo, PrimeTime
    from gui.prb_control.items import ValidationResult
    from gui.ranked_battles.constants import YearAwardsNames
    from gui.ranked_battles.ranked_helpers.sound_manager import RankedSoundManager
    from gui.ranked_battles.ranked_helpers.stats_composer import RankedBattlesStatsComposer
    from gui.ranked_battles.ranked_helpers.web_season_provider import RankedWebSeasonProvider, WebSeasonInfo
    from gui.ranked_battles.ranked_models import BattleRankInfo, Division, PostBattleRankInfo, Rank
    from gui.server_events.bonuses import BattlePassSelectTokensBonus, BattlePassStyleProgressTokenBonus, SimpleBonus, TokensBonus, WoTPlusBonus, SelectableBonus, DossierBonus
    from gui.server_events.event_items import RankedQuest, Quest, PMOperation, PersonalMission, ITankAcademyQuest, ITankAcademyGroup
    from gui.shared.event_bus import SharedEvent
    from gui.shared.gui_items import Tankman, Vehicle, ItemsCollection
    from gui.shared.gui_items.artefacts import OptionalDevice
    from gui.shared.gui_items.customization.c11n_items import Customization
    from gui.shared.gui_items.fitting_item import RentalInfoProvider
    from gui.shared.gui_items.gui_item_economics import ItemPrice
    from gui.shared.gui_items.loot_box import LootBox, LootBoxKey
    from gui.shared.gui_items.Tankman import TankmanSkill
    from gui.shared.money import Currency, DynamicMoney, Money, CURRENCY_TYPE
    from gui.shared.utils.requesters.EpicMetaGameRequester import EpicMetaGameRequester
    from helpers.server_settings import BattleRoyaleConfig, EpicGameConfig, GiftSystemConfig, RankedBattlesConfig, VehiclePostProgressionConfig, _MapboxConfig, Comp7Config, WinbackConfig, EarlyAccessConfig, ModeSelectorConfig, ParagonsConfig
    from items.vehicles import VehicleType
    from season_common import GameSeason, GameSeasonCycle
    from items.artefacts import Equipment
    from skeletons.gui.battle_session import IClientArenaVisitor
    from renewable_subscription_common.settings_constants import WotPlusState
    from gui.entitlements.entitlement_model import AgateEntitlement
    from gui.server_events.event_items import Quest
    from gui.Scaleform.framework.entities.View import ViewKeyDynamic
    from account_helpers.paragons import Paragons
    from gui.game_control.paragons_controller import _ParagonsBranchesController
    from account_helpers import AccountSettings
    from gui.game_control.summer_sale_controller import ProductsStates
    from gui.Scaleform.daapi.view.lobby.hangar.entry_points.gf_header_widget import GFWidgetAliases
    BattlePassBonusOpts = Optional[TokensBonus, BattlePassSelectTokensBonus]
    BonusOpts = Optional[TokensBonus, SelectableBonus]

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
    onUpdated = None

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

    def getSeasonPassed(self, now=None):
        raise NotImplementedError
        return

    def getTimer(self, now=None, peripheryID=None):
        raise NotImplementedError
        return

    def getLeftTimeToPrimeTimesEnd(self, now=None):
        raise NotImplementedError
        return

    def getAnyPrimeStatusServerID(self, states, now=None):
        raise NotImplementedError
        return


class IGameStateTracker(IGameController):

    def onAccountShowGUI(self, ctx):
        raise NotImplementedError
        return

    def addController(self, controller):
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


class IEpicModeController(IGameController):
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
    onHidden = None

    def hasAdventHero(self):
        raise NotImplementedError
        return

    def isAdventHero(self):
        raise NotImplementedError
        return

    def getRandomTankCD(self):
        raise NotImplementedError
        return

    def setInteractive(self, interactive):
        raise NotImplementedError
        return

    def setHidden(self, isHidden):
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

    def getCurrentShopUrl(self):
        raise NotImplementedError
        return


class IPlatoonController(IGameController):
    onFilterUpdate = None
    onMembersUpdate = None
    onPlatoonTankUpdated = None
    onPlatoonTankVisualizationChanged = None
    onPlatoonTankVisualizationBlocked = None
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

    def evaluateVisibility(self, xPopoverOffset=0, toggleUI=False):
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

    def togglePlayerReadyAction(self, callback):
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

    def orderSlotsBasedOnDisplaySlotsIndices(self, slots):
        raise NotImplementedError
        return

    def processPlatoonActions(self, mapID, entity, currentVehicle, callback):
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

    def showPromo(self, url, handlers=None, source=None):
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

    def addMonitoredDynamicViewKey(self, viewKey):
        raise NotImplementedError
        return


class IBoostersController(IGameController):
    onBoosterChangeNotify = None
    onReserveTimerTick = None
    onGameModeStatusChange = None

    def isGameModeSupported(self, category):
        raise NotImplementedError
        return

    def selectRandomBattle(self):
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

    def addVehicle(self, vehicleCompactDesr, initParameters=None, settings=None):
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

    def getTradeInDiscounts(self, item):
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
    onRankedPrbClosing = None

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

    def isLeagueRewardEnabled(self):
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

    def getRankSquadRestriction(self):
        raise NotImplementedError
        return

    def getDivisionSquadRestriction(self):
        raise NotImplementedError
        return

    def getStepsList(self):
        raise NotImplementedError
        return

    def getStepsToEarnRank(self, rankID):
        raise NotImplementedError
        return

    def getCanTakeReward(self, rankID):
        raise NotImplementedError
        return

    def isUnburnableRank(self, rankID):
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

    def showRankedAwardWindow(self, rankInfo, questsProgress):
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

    def takeRewardForRank(self, rank):
        raise NotImplementedError
        return

    def hasAnyRewardToTake(self):
        raise NotImplementedError
        return

    def replaceOfferByReward(self, bonuses):
        raise NotImplementedError
        return

    def isLocked(self):
        raise NotImplementedError
        return


class IBootcampController(IGameController):

    @property
    def replayCtrl(self):
        raise NotImplementedError
        return

    @property
    def nationData(self):
        raise NotImplementedError
        return

    @property
    def nation(self):
        raise NotImplementedError
        return

    @property
    def version(self):
        raise NotImplementedError
        return

    def getBootcampOutfit(self, vehDescr):
        raise NotImplementedError
        return

    def isInBootcamp(self):
        raise NotImplementedError
        return

    def startBootcamp(self, inBattle):
        raise NotImplementedError
        return

    def stopBootcamp(self, inBattle):
        raise NotImplementedError
        return

    def getContext(self):
        raise NotImplementedError
        return

    def hasFinishedBootcampBefore(self):
        raise NotImplementedError
        return

    def runCount(self):
        raise NotImplementedError
        return

    def isReferralEnabled(self):
        raise NotImplementedError
        return

    def needAwarding(self):
        raise NotImplementedError
        return

    def setAutomaticStart(self, enable):
        raise NotImplementedError
        return

    def isInBootcampAccount(self):
        raise NotImplementedError
        return

    def showActionWaitWindow(self):
        raise NotImplementedError
        return

    def hideActionWaitWindow(self):
        raise NotImplementedError
        return

    def getLessonNum(self):
        raise NotImplementedError
        return

    def getAwardVehicles(self):
        raise NotImplementedError
        return

    def isEnableCriticalDamageIcon(self):
        raise NotImplementedError
        return

    def getCheckpoint(self):
        raise NotImplementedError
        return

    def saveCheckpoint(self, checkpoint):
        raise NotImplementedError
        return

    def changeNation(self, nationIndex):
        raise NotImplementedError
        return

    def getDisabledSettings(self):
        raise NotImplementedError
        return

    def showFinalVideo(self, callback):
        raise NotImplementedError
        return

    def finishBootcamp(self):
        raise NotImplementedError
        return

    def runBootcamp(self):
        raise NotImplementedError
        return

    def canRun(self):
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
    TOKEN_QUEST_ID = b''
    DAILY_QUEST_ID = b''
    FINAL_BADGE_QUEST_ID = b''

    def isEnabled(self):
        raise NotImplementedError
        return

    def isEpicPrbActive(self):
        raise NotImplementedError
        return

    def isCurrentCycleActive(self):
        raise NotImplementedError
        return

    def getLevelsToUPGAllReserves(self):
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

    def getPerformanceGroup(self):
        raise NotImplementedError
        return

    def getMaxPlayerLevel(self):
        raise NotImplementedError
        return

    def getStageLimit(self):
        raise NotImplementedError
        return

    def getAbilityPointsForLevel(self):
        raise NotImplementedError
        return

    def getValidVehicleLevels(self):
        raise NotImplementedError
        return

    def getForbiddenVehicles(self):
        raise NotImplementedError
        return

    def getUnlockableInBattleVehLevels(self):
        raise NotImplementedError
        return

    def getUnlockableInBattleVehLevelStr(self):
        raise NotImplementedError
        return

    def getSuitableForQueueVehicleLevels(self):
        raise NotImplementedError
        return

    def getSuitableForQueueVehicleLevelStr(self):
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

    def getAllSkillsInformation(self):
        raise NotImplementedError
        return

    def getOrderedSkillTree(self):
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

    def getDestructiblesArmor(self):
        raise NotImplementedError
        return

    def isNeedToTakeReward(self):
        raise NotImplementedError
        return

    def getNotChosenRewardCount(self):
        raise NotImplementedError
        return

    def showProgressionDuringSomeStates(self, showDefaultTab=False):
        raise NotImplementedError
        return

    def selectEpicBattle(self):
        raise NotImplementedError
        return

    def hasAnyOfferGiftToken(self):
        raise NotImplementedError
        return

    def replaceOfferByReward(self, bonuses):
        raise NotImplementedError
        return

    def getSectorsProgression(self):
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

    def hasSuitableVehicles(self):
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

    def showWelcomeScreenIfNeed(self):
        raise NotImplementedError
        return

    def storeCycle(self):
        raise NotImplementedError
        return

    def getSupplyParams(self):
        raise NotImplementedError
        return


class IBattleRoyaleController(IGameController, ISeasonProvider):
    onUpdated = None
    onPrimeTimeStatusUpdated = None
    onWidgetUpdate = None
    TOKEN_QUEST_ID = b''

    def isEnabled(self):
        raise NotImplementedError
        return

    def isShowTimeLeft(self):
        raise NotImplementedError
        return

    def getDefaultAmmoCount(self, itemKey, intCD=None, vehicleName=None):
        raise NotImplementedError
        return

    def getPerformanceGroup(self):
        raise NotImplementedError
        return

    def getEndTime(self):
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

    def selectRoyaleBattle(self):
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

    def wasInLobby(self):
        raise NotImplementedError
        return

    def getBrVehicleEquipmentIds(self, vehicleName):
        raise NotImplementedError
        return

    def getStats(self):
        raise NotImplementedError
        return

    @staticmethod
    def getBrCommanderSkills():
        raise NotImplementedError
        return

    def openURL(self, url=None):
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

    def getIntroVideoURL(self):
        raise NotImplementedError
        return

    def getProgressionPointsTableData(self):
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

    def leaveCurrentAndJoinToAnotherTournament(self, newTournamentID):
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


class IBattleRoyaleRentVehiclesController(IGameController):
    onBalanceUpdated = None
    onPriceInfoUpdated = None
    onRentInfoUpdated = None
    onUpdated = None

    def getRentState(self, intCD=None):
        raise NotImplementedError
        return

    def isRentable(self, intCD=None):
        raise NotImplementedError
        return

    def getTestDrivePrice(self, intCD=None):
        raise NotImplementedError
        return

    def getRentPrice(self, intCD=None):
        raise NotImplementedError
        return

    def getRentDaysLeft(self, intCD=None):
        raise NotImplementedError
        return

    def getRentTimeLeft(self, intCD=None):
        raise NotImplementedError
        return

    def getFormatedRentTimeLeft(self, intCD=None, isRoundUp=True):
        raise NotImplementedError
        return

    def getPendingRentDays(self, intCD=None):
        raise NotImplementedError
        return

    def getNextTestDriveDaysTotal(self, intCD=None):
        raise NotImplementedError
        return

    def getNextRentDaysTotal(self, intCD=None):
        raise NotImplementedError
        return

    def isInTestDriveRent(self, intCD=None):
        raise NotImplementedError
        return

    def isEnoughMoneyToPurchase(self, intCD=None, state=None):
        raise NotImplementedError
        return

    def purchaseRent(self, intCD=None):
        raise NotImplementedError
        return

    def getBRCoinBalance(self, default=None):
        raise NotImplementedError
        return

    def watchRentVehicles(self, callback, vehIntCDs=None):
        raise NotImplementedError
        return

    def unwatchRentVehicles(self, callback, runWatch=True):
        raise NotImplementedError
        return

    def setRentUpdateCurrentVehicleCallback(self, callback):
        raise NotImplementedError
        return

    def clearRentUpdateCurrentVehicleCallback(self, callback):
        raise NotImplementedError
        return


class IBRProgressionOnTokensController(IGameController):
    progressionToken = b''
    PROGRESSION_COMPLETE_TOKEN = b''
    onProgressPointsUpdated = None
    onSettingsChanged = None

    def init(self):
        raise NotImplementedError
        return

    def fini(self):
        raise NotImplementedError
        return

    def setSettings(self, settings):
        raise NotImplementedError
        return

    def saveCurPoints(self):
        raise NotImplementedError
        return

    def getPrevPoints(self):
        raise NotImplementedError
        return

    def getCurPoints(self):
        raise NotImplementedError
        return

    def getCurrentStageData(self):
        raise NotImplementedError
        return

    def getProgressionLevelsData(self):
        raise NotImplementedError
        return

    def getProgessionPointsData(self):
        raise NotImplementedError
        return

    def getProgressionData(self):
        raise NotImplementedError
        return

    @property
    def isEnabled(self):
        raise NotImplementedError
        return

    @property
    def isFinished(self):
        raise NotImplementedError
        return


class IManualController(IGameController):

    def isActivated(self):
        raise NotImplementedError
        return

    def clear(self):
        raise NotImplementedError
        return

    def getBootcampRunCount(self):
        raise NotImplementedError
        return

    def runBootcamp(self):
        raise NotImplementedError
        return

    def getNewContentCount(self):
        raise NotImplementedError
        return

    def pageFilter(self, pageType):
        raise NotImplementedError
        return

    def show(self, lessonID=None, backCallback=None):
        raise NotImplementedError
        return

    def getView(self):
        raise NotImplementedError
        return


class ICraftmachineController(IGameController):

    def getModuleName(self):
        raise NotImplementedError
        return


class ICalendarController(IGameController):

    def updateHeroAdventActionInfo(self):
        raise NotImplementedError
        return

    def getHeroAdventActionInfo(self):
        raise NotImplementedError
        return

    def showWindow(self, url=None, invokedFrom=None):
        raise NotImplementedError
        return

    def hideWindow(self):
        raise NotImplementedError
        return


class IReferralProgramController(IGameController):
    onReferralProgramEnabled = None
    onReferralProgramDisabled = None
    onReferralProgramUpdated = None
    onPointsChanged = None

    def isFirstIndication(self):
        raise NotImplementedError
        return

    def getBubbleCount(self):
        raise NotImplementedError
        return

    def updateBubble(self):
        raise NotImplementedError
        return

    def isScoresLimitReached(self):
        raise NotImplementedError
        return

    def isShouldIndicate(self):
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

    def isEnabled(self):
        raise NotImplementedError
        return

    def getHangarQuestsFlagData(self):
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


class IBattlePassController(IGameController):
    onPointsUpdated = None
    onNonChapterPointsUpdated = None
    onLevelUp = None
    onBattlePassIsBought = None
    onSelectTokenUpdated = None
    onSeasonStateChanged = None
    onBattlePassSettingsChange = None
    onFinalRewardStateChange = None
    onRewardSelectChange = None
    onOffersUpdated = None
    onChapterChanged = None
    onMarathonChapterExpired = None

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

    def isResourceCompleted(self):
        raise NotImplementedError
        return

    def isMarathonCompleted(self):
        raise NotImplementedError
        return

    def isResourceChaptersCompleted(self):
        raise NotImplementedError
        return

    def isResourceChaptersBought(self):
        raise NotImplementedError
        return

    def isMarathonChaptersCompleted(self):
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

    def getLevelsToTriggerHint(self):
        raise NotImplementedError
        return

    def hasMarathon(self):
        raise NotImplementedError
        return

    def hasResource(self):
        raise NotImplementedError
        return

    def isValidChapterID(self, chapterID):
        raise NotImplementedError
        return

    def isSingleChapter(self):
        raise NotImplementedError
        return

    def getChapterType(self, chapterID):
        raise NotImplementedError
        return

    def getAvailableChapterTypes(self):
        raise NotImplementedError
        return

    def getRegularChapterIds(self):
        raise NotImplementedError
        return

    def getMarathonChapterID(self):
        raise NotImplementedError
        return

    def getMarathonChapterIDs(self):
        raise NotImplementedError
        return

    def getResourceChapterID(self):
        raise NotImplementedError
        return

    def getResourceChapterIDs(self):
        raise NotImplementedError
        return

    def getRewardType(self, chapterID):
        raise NotImplementedError
        return

    def isChapterExists(self, chapterID):
        raise NotImplementedError
        return

    def getChapterIDs(self):
        raise NotImplementedError
        return

    def isMainChaptersCompleted(self):
        raise NotImplementedError
        return

    def setTriggerHint(self, globalFlag, value):
        raise NotImplementedError
        return

    def getPotentialChaptersLevels(self):
        raise NotImplementedError
        return

    def isShowHint(self):
        raise NotImplementedError
        return

    def isShowWidgetHint(self):
        raise NotImplementedError
        return

    def isMarathonChapter(self, chapterID):
        raise NotImplementedError
        return

    def allRegularChaptersPurchased(self):
        raise NotImplementedError
        return

    def isResourceChapter(self, chapterID):
        raise NotImplementedError
        return

    def isResourceChapterAvailable(self):
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

    def hasActiveChapter(self):
        raise NotImplementedError
        return

    def activateChapter(self, chapterID, parent, seasonID=None):
        raise NotImplementedError
        return

    def getCurrentLevel(self):
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

    def isNeedToTakeReward(self, awardType, chapterId, level):
        raise NotImplementedError
        return

    def isChooseRewardEnabled(self, awardType, chapterId, level):
        raise NotImplementedError
        return

    def canChooseAnyReward(self):
        raise NotImplementedError
        return

    def getLevelsConfig(self, chapterId):
        raise NotImplementedError
        return

    def getChapterConfig(self):
        raise NotImplementedError
        return

    def getChapterLevelInterval(self, chapter):
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

    def getRewardLogic(self):
        raise NotImplementedError
        return

    def getPointsInChapter(self, chapterID):
        raise NotImplementedError
        return

    def getLevelProgression(self, chapterID):
        raise NotImplementedError
        return

    def getPerBattlePoints(self, gameMode=ARENA_BONUS_TYPE.REGULAR, vehCompDesc=None):
        raise NotImplementedError
        return

    def getWinLosePointsList(self, gameMode=ARENA_BONUS_TYPE.EPIC_BATTLE):
        raise NotImplementedError
        return

    def getPerBattleRoyalePoints(self, gameMode=ARENA_BONUS_TYPE.BATTLE_ROYALE_SOLO, vehCompDesc=None):
        raise NotImplementedError
        return

    def isSpecialVehicle(self, intCD):
        raise NotImplementedError
        return

    def getSpecialVehicles(self):
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

    def isShopOfferActive(self):
        raise NotImplementedError
        return

    def getShopOfferFinishTimeLeft(self):
        raise NotImplementedError
        return

    def getSeasonsHistory(self):
        raise NotImplementedError
        return

    def getStylesConfig(self):
        raise NotImplementedError
        return

    def getVehicleCDRewardForChapter(self, chapterID):
        raise NotImplementedError
        return

    def getNotChosenRewardCount(self):
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

    def getTimeToLimitReset(self):
        raise NotImplementedError
        return

    def getQuestTokensInChapter(self):
        raise NotImplementedError
        return


class IHangarLoadingController(IGameController):
    onHangarLoadedAfterLogin = None


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

    def selectMapboxBattle(self):
        raise NotImplementedError
        return

    def getProgressionData(self):
        raise NotImplementedError
        return

    def getProgressionRestartTime(self):
        raise NotImplementedError
        return

    def selectCrewbookNation(self, itemID):
        raise NotImplementedError
        return

    def handleSurveyCompleted(self, surveyData):
        raise NotImplementedError
        return

    def getUnseenItemsCount(self):
        raise NotImplementedError
        return

    def showSurvey(self, mapName):
        raise NotImplementedError
        return

    def addVisitedMap(self, mapName):
        raise NotImplementedError
        return

    def storeReward(self, numBattles, rewardIdx, rewardIconName):
        raise NotImplementedError
        return

    def getStoredReward(self, numBattles, rewardIdx):
        raise NotImplementedError
        return

    def setPrevBattlesPlayed(self, numBattles):
        raise NotImplementedError
        return

    def getPrevBattlesPlayed(self):
        raise NotImplementedError
        return

    def isMapVisited(self, mapName):
        raise NotImplementedError
        return

    def forceUpdateProgressData(self):
        raise NotImplementedError
        return

    def getModeSettings(self):
        raise NotImplementedError
        return


class IOverlayController(IGameController):

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

    def runDemoAccRegistration(self):
        raise NotImplementedError
        return

    def updateOverlayState(self, waitingID=None, onComplete=None):
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

    def showMapsTrainingPage(self, ctx=None):
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

    def processVehExtData(self, vehCD, extData):
        raise NotImplementedError
        return


class IWotPlusController(IGameController):
    onDataChanged = None
    onAttendanceUpdated = None
    onStateUpdate = None
    onPendingRentChanged = None

    def processSwitchNotifications(self):
        raise NotImplementedError
        return

    def selectIdleCrewXPVehicle(self, vehicleInvID, successCallback=None, errorCallback=None):
        raise NotImplementedError
        return

    def isEnabled(self):
        raise NotImplementedError
        return

    def isFreeToDemount(self, device):
        raise NotImplementedError
        return

    def getState(self):
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

    def getActiveExclusiveVehicle(self):
        raise NotImplementedError
        return

    def getActiveExclusiveVehicleName(self):
        raise NotImplementedError
        return

    def getEnabledBonuses(self):
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

    def setReservesDev(self, creditsVal, goldVal):
        raise NotImplementedError
        return

    def smashPiggyBankDev(self):
        raise NotImplementedError
        return

    def isWotPlusEnabled(self):
        raise NotImplementedError
        return

    def onDailyAttendanceUpdate(self):
        raise NotImplementedError
        return

    def resolveState(self):
        raise NotImplementedError
        return

    def synchronize(self):
        raise NotImplementedError
        return

    def isDailyAttendanceQuest(self, questID):
        raise NotImplementedError
        return

    def getFormattedDailyAttendanceBonuses(self, bonuses):
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


class IGuiLootBoxesController(IGameController, IEntitlementsConsumer):
    onStatusChange = None
    onAvailabilityChange = None
    onBoxesCountChange = None
    onKeysUpdate = None
    onBoxesHistoryUpdate = None
    onBoxInfoUpdated = None
    onStorageVisited = None
    onOpenLootboxesComplete = None

    @property
    def isConsumesEntitlements(self):
        raise NotImplementedError
        return

    def getSetting(self, setting):
        raise NotImplementedError
        return

    def setSetting(self, setting, value):
        raise NotImplementedError
        return

    def isEnabled(self):
        raise NotImplementedError
        return

    def isLootBoxesAvailable(self):
        raise NotImplementedError
        return

    def isBuyAvailable(self):
        raise NotImplementedError
        return

    def isFirstStorageEnter(self):
        raise NotImplementedError
        return

    def setStorageVisited(self):
        raise NotImplementedError
        return

    def getDayLimit(self):
        raise NotImplementedError
        return

    def openShop(self, lootboxID=None):
        raise NotImplementedError
        return

    def getStoreInfo(self, category):
        raise NotImplementedError
        return

    def getBoxesIDs(self, category):
        raise NotImplementedError
        return

    def getBoxesCount(self):
        raise NotImplementedError
        return

    def getBoxKeysCount(self):
        raise NotImplementedError
        return

    def getKeyByID(self, keyID):
        raise NotImplementedError
        return

    def getKeyByTokenID(self, tokenID):
        raise NotImplementedError
        return

    def getBonusesOrder(self, category=None):
        raise NotImplementedError
        return

    def getHangarOptimizer(self):
        raise NotImplementedError
        return

    def addShopWindowHandler(self, keyHandler, handler):
        raise NotImplementedError
        return

    def hasLootboxKey(self):
        raise NotImplementedError
        return

    def hasInfiniteLootboxes(self):
        raise NotImplementedError
        return

    def getGuiLootBoxes(self):
        raise NotImplementedError
        return

    def getGuiLootBoxByTokenID(self, tokenID):
        raise NotImplementedError
        return


class IGuiLootBoxesIntroController(IGameController):

    def tryShowIntro(self):
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


class IShopSalesEventController(IGameController):
    onSettingsChanged = None
    onPhaseChanged = None

    @property
    def isEnabled(self):
        raise NotImplementedError
        return

    @property
    def currentEventPhase(self):
        raise NotImplementedError
        return

    @property
    def currentEventPhaseTimeRange(self):
        raise NotImplementedError
        return

    @property
    def activePhaseStartTime(self):
        raise NotImplementedError
        return

    @property
    def activePhaseFinishTime(self):
        raise NotImplementedError
        return

    @property
    def eventFinishTime(self):
        raise NotImplementedError
        return

    @property
    def url(self):
        raise NotImplementedError
        return

    def getEventPhase(self, timestamp):
        raise NotImplementedError
        return

    def getEventPhaseTimeRange(self, state):
        raise NotImplementedError
        return

    def openMainView(self, url=None, origin=None):
        raise NotImplementedError
        return


class ISeniorityAwardsController(IGameController):
    onUpdated = None

    @property
    def isEnabled(self):
        raise NotImplementedError
        return

    @property
    def timeLeft(self):
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
    def isNeedToShowRewardNotification(self):
        raise NotImplementedError
        return

    @property
    def pendingReminderTimestamp(self):
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


class IResourceWellController(IGameController):
    onEventUpdated = None
    onSettingsChanged = None
    onNumberRequesterUpdated = None
    onEventStateChanged = None

    def isEnabled(self):
        raise NotImplementedError
        return

    def isActive(self):
        raise NotImplementedError
        return

    def isStarted(self):
        raise NotImplementedError
        return

    def isFinished(self):
        raise NotImplementedError
        return

    def isPaused(self):
        raise NotImplementedError
        return

    def isNotStarted(self):
        raise NotImplementedError
        return

    def getSeason(self):
        raise NotImplementedError
        return

    def getRewardLimit(self, isTop):
        raise NotImplementedError
        return

    def getFinishTime(self):
        raise NotImplementedError
        return

    def getStartTime(self):
        raise NotImplementedError
        return

    def getCurrentPoints(self):
        raise NotImplementedError
        return

    def getMaxPoints(self):
        raise NotImplementedError
        return

    def getRewardVehicle(self):
        raise NotImplementedError
        return

    def getRewardStyleID(self):
        raise NotImplementedError
        return

    def getRewardSequence(self, isTop):
        raise NotImplementedError
        return

    def getRewardLeftCount(self, isTop):
        raise NotImplementedError
        return

    def isRewardEnabled(self, isTop):
        raise NotImplementedError
        return

    def isRewardCountAvailable(self, isTop=True):
        raise NotImplementedError
        return

    def getReminderTime(self):
        raise NotImplementedError
        return

    def isCompleted(self):
        raise NotImplementedError
        return

    def getResources(self):
        raise NotImplementedError
        return

    def getRewards(self):
        raise NotImplementedError
        return

    def getRewardID(self, isTop):
        raise NotImplementedError
        return

    def startNumberRequesters(self):
        raise NotImplementedError
        return

    def stopNumberRequesters(self):
        raise NotImplementedError
        return


class ICollectiveGoalEntryPointController(IGameController):
    onSettingsChanged = None
    onEventUpdated = None
    onDataUpdated = None

    def isEnabled(self):
        raise NotImplementedError
        return

    def isCompleted(self):
        raise NotImplementedError
        return

    def isStarted(self):
        raise NotImplementedError
        return

    def isFinished(self):
        raise NotImplementedError
        return

    def isForbidden(self):
        raise NotImplementedError
        return

    def getEventStartTime(self):
        raise NotImplementedError
        return

    def getActivePhaseStartTime(self):
        raise NotImplementedError
        return

    def getActivePhaseFinishTime(self):
        raise NotImplementedError
        return

    def getEventFinishTime(self):
        raise NotImplementedError
        return

    def getCurrentPoints(self):
        raise NotImplementedError
        return

    def getStagePoints(self):
        raise NotImplementedError
        return

    def getDiscounts(self):
        raise NotImplementedError
        return

    def getCurrentDiscount(self):
        raise NotImplementedError
        return

    def getMarathonPrefix(self):
        raise NotImplementedError
        return

    def getMarathonName(self):
        raise NotImplementedError
        return

    def getGoalType(self):
        raise NotImplementedError
        return

    def getGoalDescription(self):
        raise NotImplementedError
        return

    def getRulesCaption(self):
        raise NotImplementedError
        return


class ICollectiveGoalMarathonsController(IGameController):
    onMarathonUpdated = None

    def getEventName(self):
        raise NotImplementedError
        return


class IUniversalFlagEntryPointController(IGameController):

    class VisibilityState(str, Enum):
        HIDDEN = b'hidden'
        SHOWN = b'shown'
        MAINTANANCE = b'maintenance'

    class TimerIconType(str, Enum):
        FLAG = b'flag'
        CLOCK = b'clock'
        NONE = b'none'

    class FlagBackground(object):
        __slots__ = (b'active', b'activeHover', b'disabled', b'disabledHover')

        def __init__(self):
            self.active = b''
            self.activeHover = b''
            self.disabled = b''
            self.disabledHover = b''
            return

    onDataUpdated = None

    @property
    def visibilityState(self):
        raise NotImplementedError
        return

    @property
    def timerTime(self):
        raise NotImplementedError
        return

    @property
    def timerIconType(self):
        raise NotImplementedError
        return

    @property
    def timerText(self):
        raise NotImplementedError
        return

    def openEvent(self):
        raise NotImplementedError
        return

    @property
    def eventCaption(self):
        raise NotImplementedError
        return

    @property
    def eventDescription(self):
        raise NotImplementedError
        return

    @property
    def flagBackground(self):
        raise NotImplementedError
        return

    @property
    def tooltipBackground(self):
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

        def addListener(self, eventType, handler, scope=None):
            raise NotImplementedError
            return

        def removeListener(self, eventType, handler, scope=None):
            raise NotImplementedError
            return

        def handleEvent(self, event, scope=None):
            raise NotImplementedError
            return

        def addSubModesWatcher(self, method, desiredOnly=False, withTicks=False):
            raise NotImplementedError
            return

        def removeSubModesWatcher(self, method, desiredOnly=False, withTicks=False):
            raise NotImplementedError
            return

        def resume(self):
            raise NotImplementedError
            return

        def suspend(self):
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

        def getLeftTimeToPrimeTimesEnd(self, now=None, subModes=None):
            raise NotImplementedError
            return

        def getPrimeTimesForDay(self, selectedTime, groupIdentical=False):
            raise NotImplementedError
            return

        def getSubModesStatus(self, subModesIDs=None):
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

    def getAssetsPointer(self):
        raise NotImplementedError
        return

    def getLocalsResRoot(self):
        raise NotImplementedError
        return

    def getIconsResRoot(self):
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

    def getCurrentFunType(self):
        raise NotImplementedError
        return

    def isArcade(self):
        raise NotImplementedError
        return

    def isFieldTrials(self):
        raise NotImplementedError
        return

    def isLocked(self):
        raise NotImplementedError
        return


class IBattleModifiersController(IGameController):

    class ModifiersDomains(object):
        STRONGHOLD = b'battleSeasonModifiers'
        GLOBAL_MAP = b'battleSeasonModifiersGM'
        COMP7 = b'comp7'
        STRONGHOLD_DOMAINS = (
         STRONGHOLD, GLOBAL_MAP)

    @property
    def battleModifiers(self):
        raise NotImplementedError
        return

    def getBattleModifiersObject(self):
        raise NotImplementedError
        return

    def isBattleModifiersAvailable(self):
        raise NotImplementedError
        return

    def modifiersInStrongholdBrowser(self):
        raise NotImplementedError
        return

    @property
    def tooltipConstant(self):
        raise NotImplementedError
        return

    def getBattleModifiersQueues(self):
        raise NotImplementedError
        return

    def getCurrentDomain(self):
        raise NotImplementedError
        return


class IComp7Controller(IGameController, ISeasonProvider):
    onStatusUpdated = None
    onStatusTick = None
    onRankUpdated = None
    onComp7ConfigChanged = None
    onComp7RanksConfigChanged = None
    onBanUpdated = None
    onOfflineStatusUpdated = None
    onQualificationBattlesUpdated = None
    onQualificationStateUpdated = None
    onSeasonPointsUpdated = None
    onComp7RewardsConfigChanged = None
    onComp7BattleFinished = None
    onComp7SkillsConfigChanged = None
    onLeaderboardDataRequested = None
    onLeaderboardDataProvided = None

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
    def activityPoints(self):
        raise NotImplementedError
        return

    @property
    def battleModifiers(self):
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
    def entitlementsCache(self):
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

    def getVehicleSkillEquipment(self, vehicle):
        raise NotImplementedError
        return

    def getVehicleEquipments(self, vehicle):
        raise NotImplementedError
        return

    def getRoleEquipment(self, roleName):
        raise NotImplementedError
        return

    def getEquipmentStartLevel(self, roleName):
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

    def vehicleIsAvailableForBuy(self):
        raise NotImplementedError
        return

    def vehicleIsAvailableForRestore(self):
        raise NotImplementedError
        return

    def hasPlayableVehicle(self):
        raise NotImplementedError
        return

    def isComp7PrbActive(self):
        raise NotImplementedError
        return

    def getAlertBlock(self):
        raise NotImplementedError
        return

    def getPlatoonRatingRestriction(self):
        raise NotImplementedError
        return

    def getStatsSeasonsKeys(self):
        raise NotImplementedError
        return

    def getReceivedSeasonPoints(self):
        raise NotImplementedError
        return

    def getYearlyRewards(self):
        raise NotImplementedError
        return

    def isYearlyRewardReceived(self):
        raise NotImplementedError
        return

    def isLocked(self):
        raise NotImplementedError
        return

    def getEliteDivisionIdx(self):
        raise NotImplementedError
        return


class IArmoryYardController(IGameController):
    onUpdated = None
    onProgressUpdated = None
    onStatusChange = None
    onQuestsUpdated = None
    onCheckNotify = None
    onAnnouncement = None
    onPayed = None
    onPayedError = None
    onBundleOutTime = None
    onServerSwitchChange = None
    onStyleQuestEnds = None
    onCollectReward = None
    cameraManager = None
    isVehiclePreview = None
    bundlesProducts = None
    onTabIdChanged = None
    onCollectFinalReward = None
    onBundlesDisabled = None
    onAYCoinsUpdate = None

    @property
    def isArmoryVisiting(self):
        raise NotImplementedError
        return

    @property
    def serverSettings(self):
        raise NotImplementedError
        return

    @property
    def isFinalQuestCompleted(self):
        raise NotImplementedError
        return

    @property
    def isPaused(self):
        raise NotImplementedError
        return

    @property
    def isPostProgressionState(self):
        raise NotImplementedError
        return

    @property
    def currentSeason(self):
        raise NotImplementedError
        return

    @property
    def currentSeasonID(self):
        raise NotImplementedError
        return

    @property
    def maxNumberOfSteps(self):
        raise NotImplementedError
        return

    @property
    def startStepOfPostProgression(self):
        raise NotImplementedError
        return

    def getCollectableRewards(self):
        raise NotImplementedError
        return

    def isChapterFinished(self, cycle):
        raise NotImplementedError
        return

    def receivedTokensInChapter(self, cycleID):
        raise NotImplementedError
        return

    def iterCycleProgressionQuests(self, cycleID):
        raise NotImplementedError
        return

    def getTokensInfo(self):
        raise NotImplementedError
        return

    def isAllTokensReceived(self):
        raise NotImplementedError
        return

    def getSeasonInterval(self):
        raise NotImplementedError
        return

    def getProgressionTimes(self):
        raise NotImplementedError
        return

    def getPurchaseStageTimes(self):
        raise NotImplementedError
        return

    def totalTokensInChapter(self, cycleID):
        raise NotImplementedError
        return

    def iterProgressionQuests(self):
        raise NotImplementedError
        return

    def getProgressionTokenCount(self):
        raise NotImplementedError
        return

    def getProgressionLevel(self):
        raise NotImplementedError
        return

    def getCurrentProgress(self):
        raise NotImplementedError
        return

    def getStepsRewards(self):
        raise NotImplementedError
        return

    def getFinalRewardVehicle(self):
        raise NotImplementedError
        return

    def getFinalProgressionRewardStyle(self):
        raise NotImplementedError
        return

    def getCurrencyTokenCost(self, currency):
        raise NotImplementedError
        return

    def isActive(self):
        raise NotImplementedError
        return

    def goToArmoryYard(self, tabId, ctx=None):
        raise NotImplementedError
        return

    def goToArmoryYardQuests(self):
        raise NotImplementedError
        return

    def hasCurrentRewards(self):
        raise NotImplementedError
        return

    def isProgressionQuest(self, questID):
        raise NotImplementedError
        return

    def isEnabled(self):
        raise NotImplementedError
        return

    def isClaimedProgressionReward(self):
        raise NotImplementedError
        return

    def isClaimedPostProgressionReward(self):
        raise NotImplementedError
        return

    def isQuestActive(self):
        raise NotImplementedError
        return

    def isSceneLoaded(self):
        raise NotImplementedError
        return

    def isPurchaseStageActive(self):
        raise NotImplementedError
        return

    def getAvailableQuestsCount(self):
        raise NotImplementedError
        return

    def getNextCycle(self, currentTime=None):
        raise NotImplementedError
        return

    def getState(self):
        raise NotImplementedError
        return

    def update(self):
        raise NotImplementedError
        return

    def isInAnnouncement(self):
        raise NotImplementedError
        return

    def onLoadingHangar(self):
        raise NotImplementedError
        return

    def unloadScene(self, isReload=True):
        raise NotImplementedError
        return

    def isCompleted(self):
        raise NotImplementedError
        return

    def isStarterPackAvailable(self):
        raise NotImplementedError
        return

    def getStarterPackSettings(self):
        raise NotImplementedError
        return

    def refreshBundle(self):
        raise NotImplementedError
        return

    def checkAnnouncement(self):
        raise NotImplementedError
        return

    def bundleTokensLeft(self):
        raise NotImplementedError
        return

    def isPurchaseStageEnabled(self):
        raise NotImplementedError
        return

    def getTokenCurrencies(self):
        raise NotImplementedError
        return

    def subtrahendStageToken(self):
        raise NotImplementedError
        return

    def getHangarFlagData(self):
        raise NotImplementedError
        return

    def getFinalRewardStep(self):
        raise NotImplementedError
        return

    def getFinalPostProgressionRewardStep(self):
        raise NotImplementedError
        return

    def updateVisibilityHangarHeaderMenu(self, isVisible=False):
        raise NotImplementedError
        return

    def totalTokensInPostProgressionChapter(self):
        raise NotImplementedError
        return

    def receivedTokensInPostProgressionChapter(self):
        raise NotImplementedError
        return

    def iterCyclePostProgressionQuests(self):
        raise NotImplementedError
        return

    def getTokensInfoMainProgression(self):
        raise NotImplementedError
        return

    def showVehiclePreview(self, isAnimationActive=False, disableAnimation=None, backCallback=None):
        raise NotImplementedError
        return

    def showStylePreview(self, isAnimationActive=False, disableAnimation=None, backLabel=None, backCallback=None):
        raise NotImplementedError
        return

    def showShopStylePreview(self, styleID=None, backCallback=None):
        raise NotImplementedError
        return


class IArmoryYardShopController(IGameController):
    onProductsUpdate = None
    onAYCoinsUpdate = None
    onSettingsUpdate = None
    onPurchaseComplete = None
    onPurchaseError = None

    @property
    def isEnabled(self):
        raise NotImplementedError
        return

    @property
    def ayCoins(self):
        raise NotImplementedError
        return

    @property
    def conversionPrices(self):
        raise NotImplementedError
        return

    @property
    def products(self):
        raise NotImplementedError
        return

    @property
    def isProgressionCompleted(self):
        raise NotImplementedError
        return

    def isBundle(self, productId):
        raise NotImplementedError
        return


class IHangarSpaceSwitchController(IGameController):
    onCheckSceneChange = None
    onSpaceUpdated = None

    def hangarSpaceUpdate(self, sceneName):
        raise NotImplementedError
        return

    def getSpacePath(self, spaceName):
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
    onTokensUpdated = None

    @property
    def winbackConfig(self):
        raise NotImplementedError
        return

    @property
    def activeProgressionConfig(self):
        raise NotImplementedError
        return

    @property
    def winbackProgression(self):
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

    @property
    def winbackInfoPageURL(self):
        raise NotImplementedError
        return

    @property
    def progressionName(self):
        raise NotImplementedError
        return

    def isEnabled(self):
        raise NotImplementedError
        return

    def isWidgetEnabled(self):
        raise NotImplementedError
        return

    def isProgressionEnabled(self):
        raise NotImplementedError
        return

    def isVersusAIPrbActive(self):
        raise NotImplementedError
        return

    def isWinbackQuest(self, quest):
        raise NotImplementedError
        return

    def isFinished(self):
        raise NotImplementedError
        return

    def isWinbackOfferToken(self, offerToken):
        raise NotImplementedError
        return

    def hasWinbackOfferGiftToken(self):
        raise NotImplementedError
        return

    def winbackOfferGiftTokenCount(self):
        raise NotImplementedError
        return

    def isPromoEnabled(self):
        raise NotImplementedError
        return

    def versusAIModeShouldBeDefault(self):
        raise NotImplementedError
        return

    def getHeaderFlagState(self):
        raise NotImplementedError
        return


class IDailyQuestIntroPresenter(IGameController):
    pass


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
    def version(self):
        raise NotImplementedError
        return

    @property
    def isOnlyUISpamOff(self):
        raise NotImplementedError
        return

    @property
    def isUserSettingsMayShow(self):
        raise NotImplementedError
        return

    @property
    def isFullCompleted(self):
        raise NotImplementedError
        return

    def getRuleConditionRepresentation(self, ruleID):
        raise NotImplementedError
        return

    def isRuleCompleted(self, ruleID):
        raise NotImplementedError
        return

    def isRuleCompletedByPrebattleType(self, prbType):
        raise NotImplementedError
        return

    def completeRule(self, ruleID):
        raise NotImplementedError
        return

    def completeAllRules(self):
        raise NotImplementedError
        return

    def startObserve(self, ruleID, handler):
        raise NotImplementedError
        return

    def stopObserve(self, ruleID, handler):
        raise NotImplementedError
        return

    def sendPlatoonLockedMessage(self, prbType, name):
        raise NotImplementedError
        return


class IHangarGuiController(IGameController):

    def isComponentAvailable(self, componentType):
        raise NotImplementedError
        return

    def getCurrentPreset(self):
        raise NotImplementedError
        return

    def getAmmoInjectViewAlias(self):
        raise NotImplementedError
        return

    def getHangarCarouselSettings(self):
        raise NotImplementedError
        return

    def getHangarVehicleParamsSettings(self):
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


class IDebutBoxesController(IGameController):
    onConfigChanged = None
    onStateChanged = None
    onQuestsChanged = None

    def isEnabled(self):
        raise NotImplementedError
        return

    def isQuestsCompletedOnVehicle(self, vehicle):
        raise NotImplementedError
        return

    def isQuestsAvailableOnVehicle(self, vehicle):
        raise NotImplementedError
        return

    def isQuestsAvailableOnBattle(self):
        raise NotImplementedError
        return

    def getQuestForVehicle(self, vehicle):
        raise NotImplementedError
        return

    def getQuestsIDs(self):
        raise NotImplementedError
        return

    def getGroupID(self):
        raise NotImplementedError
        return

    def getInfoPageUrl(self):
        raise NotImplementedError
        return


class IModeSelectorController(IGameController):

    def getModeSettings(self):
        raise NotImplementedError
        return

    def getColumnSettings(self):
        raise NotImplementedError
        return


class IHangarFeatureStateController(IGameController):
    cgfCameraManager = None

    def enter(self, layoutID, doHideHeader=True):
        raise NotImplementedError
        return

    def exit(self, layoutID):
        raise NotImplementedError
        return


class IEarlyAccessController(IGameController, ISeasonProvider):
    onQuestsUpdated = None
    onBalanceUpdated = None
    onUpdated = None
    cgfCameraManager = None
    onPayed = None
    onStartEvent = None
    onFinishEvent = None
    onStartAnnouncement = None
    onFinishAnnouncement = None
    onFeatureStateChanged = None

    @property
    def sysMessageController(self):
        raise NotImplementedError
        return

    @staticmethod
    def isProgressionQuest(questID):
        raise NotImplementedError
        return

    @staticmethod
    def isPostProgressionQuest(questID):
        raise NotImplementedError
        return

    def getModeSettings(self):
        raise NotImplementedError
        return

    def isEnabled(self):
        raise NotImplementedError
        return

    def getInfoPageLink(self):
        raise NotImplementedError
        return

    def getAffectedVehiclesOrderedList(self):
        raise NotImplementedError
        return

    def getAffectedVehicles(self):
        raise NotImplementedError
        return

    def getBlockedVehicles(self):
        raise NotImplementedError
        return

    def getVehiclePrice(self, intCD):
        raise NotImplementedError
        return

    def getTokensBalance(self):
        raise NotImplementedError
        return

    def getFirstVehicleCD(self):
        raise NotImplementedError
        return

    def getCurrProgressVehicleCD(self):
        raise NotImplementedError
        return

    def getNationID(self):
        raise NotImplementedError
        return

    def getTokenCost(self):
        raise NotImplementedError
        return

    def getTokenCompensation(self, currency):
        raise NotImplementedError
        return

    def getReceivedTokensCount(self):
        raise NotImplementedError
        return

    def getTotalVehiclesPrice(self):
        raise NotImplementedError
        return

    def getTokensForQuest(self, questID):
        raise NotImplementedError
        return

    def getEAToken(self):
        raise NotImplementedError
        return

    def iterProgressionQuests(self):
        raise NotImplementedError
        return

    def iterCycleProgressionQuests(self, cycleID):
        raise NotImplementedError
        return

    def iterAllCycles(self, now=None):
        raise NotImplementedError
        return

    def isQuestActive(self):
        raise NotImplementedError
        return

    def getPostProgressionVehiclesForQuest(self, questID):
        raise NotImplementedError
        return

    def getPostProgressionVehicles(self):
        raise NotImplementedError
        return

    def getRequiredVehicleTypeAndLevelsForQuest(self, questID):
        raise NotImplementedError
        return

    def getState(self):
        raise NotImplementedError
        return

    def getSeasonInterval(self):
        raise NotImplementedError
        return

    def getCurrentSeasonID(self):
        raise NotImplementedError
        return

    def getProgressionTimes(self):
        raise NotImplementedError
        return

    def getPostprogressionTimes(self):
        raise NotImplementedError
        return

    def getCycleProgressionTimes(self, cycleId=None):
        raise NotImplementedError
        return

    def hasPostprogressionVehicle(self):
        raise NotImplementedError
        return

    def getReceivedTokensForQuests(self):
        raise NotImplementedError
        return

    def isGroupQuestsCompleted(self, groupName):
        raise NotImplementedError
        return

    def isPostProgressionQueueSelected(self):
        raise NotImplementedError
        return

    def isAnyQuestAvailable(self):
        raise NotImplementedError
        return

    def isFilterDisabledInQueue(self):
        raise NotImplementedError
        return

    def getVehicleTypeAndLevelsByVehicleCD(self, vehCD):
        raise NotImplementedError
        return


class ILootBoxesController(IGameController):
    onUpdated = None
    onUpdatedConfig = None

    def getLootBoxesByType(self):
        raise NotImplementedError
        return

    def getLootBoxesCountByType(self, lottBoxType):
        raise NotImplementedError
        return

    def getLootBoxesCountByTypeForUI(self, lootBoxType):
        raise NotImplementedError
        return

    def getLootBoxByTypeInInventory(self, lootBoxType):
        raise NotImplementedError
        return

    def getLootBoxLimitsInfo(self, lootBoxType):
        raise NotImplementedError
        return

    def getLootBoxesRewards(self, lootBoxType):
        raise NotImplementedError
        return

    def getLastViewedCount(self):
        raise NotImplementedError
        return

    def updateLastViewedCount(self):
        raise NotImplementedError
        return

    def getCollectionType(self, itemID):
        raise NotImplementedError
        return

    def isCollectionElement(self, intCD, collection):
        raise NotImplementedError
        return

    def claimReRolledReward(self, boxType, count, parentWindow, callbackUpdate=None):
        raise NotImplementedError
        return


class IWhiteTigerSettingsController(IGameController):

    @property
    def disabledSettings(self):
        raise NotImplementedError
        return


class IWhiteTigerController(IGameController, ISeasonProvider):
    onPrimeTimeStatusUpdated = None
    onProgressUpdated = None
    onEventPrbChanged = None
    onUpdated = None
    onTicketsUpdate = None
    onLobbyHeaderUpdate = None

    def isEnabled(self):
        raise NotImplementedError
        return

    def isEventPrbActive(self):
        raise NotImplementedError
        return

    def doSelectEventPrb(self):
        raise NotImplementedError
        return

    def doSelectEventPrbAndCallback(self, callback):
        raise NotImplementedError
        return

    def doLeaveEventPrb(self):
        raise NotImplementedError
        return

    def isModeActive(self):
        raise NotImplementedError
        return

    def isBattlesEnd(self):
        raise NotImplementedError
        return

    def isAvailable(self):
        raise NotImplementedError
        return

    def getConfig(self):
        raise NotImplementedError
        return

    def isHangarAvailable(self):
        raise NotImplementedError
        return

    def isWelcomeScreenShown(self):
        raise NotImplementedError
        return

    def isWtMode(self):
        raise NotImplementedError
        return

    def getCurrentStampsCount(self):
        raise NotImplementedError
        return

    def getCurrentMainPrizeDiscountTokensCount(self):
        raise NotImplementedError
        return

    def getTotalStampsCount(self):
        raise NotImplementedError
        return

    def getStampsCountPerLevel(self):
        raise NotImplementedError
        return

    def getMainPrizeDiscountPerToken(self):
        raise NotImplementedError
        return

    def getTotalLevelsCount(self):
        raise NotImplementedError
        return

    def getFinishedLevelsCount(self):
        raise NotImplementedError
        return

    def getCurrentLevel(self):
        raise NotImplementedError
        return

    def getTicketCount(self):
        raise NotImplementedError
        return

    def getQuickTicketCount(self):
        raise NotImplementedError
        return

    def getLootBoxAreaSoundMgr(self):
        raise NotImplementedError
        return

    def getSelectedVehicleSoundMgr(self):
        raise NotImplementedError
        return

    def hasSpecialBoss(self):
        raise NotImplementedError
        return

    def getSpecialBossBattlesRemaining(self):
        raise NotImplementedError
        return

    def getQuestRewards(self, questID):
        raise NotImplementedError
        return

    def getDisplayedCollectionProgress(self, questID):
        raise NotImplementedError
        return

    def setVehicleForPreview(self, vehicleCD):
        raise NotImplementedError
        return

    @property
    def mainViewLoaded(self):
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
    def banExpiryTime(self):
        raise NotImplementedError
        return

    def analyzeClientSystem(self):
        raise NotImplementedError
        return

    def showIntroVideo(self, onVideoClosed=None):
        raise NotImplementedError
        return

    def isOutroVideoAvailable(self):
        raise NotImplementedError
        return

    def needToShowOutroVideo(self):
        raise NotImplementedError
        return

    def showOutroVideo(self):
        raise NotImplementedError
        return

    def isLastSeasonDay(self):
        raise NotImplementedError
        return

    def hasPrimeTimesPassedForCurrentCycle(self):
        raise NotImplementedError
        return

    def isPrimeStatusBlocked(self, status):
        raise NotImplementedError
        return


class IVersusAIController(IGameController):

    def isEnabled(self):
        raise NotImplementedError
        return

    def isVersusAIPrbActive(self):
        raise NotImplementedError
        return

    def getConfig(self):
        raise NotImplementedError
        return

    def shouldBeDefaultMode(self):
        raise NotImplementedError
        return

    def isLocked(self):
        raise NotImplementedError
        return


class ILobbyCdnController(IGameController):
    onSynced = None

    def resolveCdnImage(self, url):
        raise NotImplementedError
        return


class IPersonalMissionsController(IGameController):
    onQuestsUpdated = None
    onUpdated = None
    cgfCameraManager = None
    onItemCacheUpdated = None
    sysMessageController = None

    def fini(self):
        raise NotImplementedError
        return

    def getPreviousOperationName(self, currentOperationId):
        raise NotImplementedError
        return

    def getMinMaxVehicleLevelForOperation(self, operation):
        raise NotImplementedError
        return

    def getOperationChainsData(self, operation):
        raise NotImplementedError
        return

    def getMainBadgesForOperation(self, operation):
        raise NotImplementedError
        return

    def onLobbyInited(self, event):
        raise NotImplementedError
        return

    def getAddBadgesForOperation(self, operation):
        raise NotImplementedError
        return

    def getPrevQuestId(self, currentQuestId):
        raise NotImplementedError
        return

    def getNextQuestId(self, currentQuestId):
        raise NotImplementedError
        return

    def getLinesIdsByChainAndOperationId(self, chainId, operationId):
        raise NotImplementedError
        return

    def getQuestsChainsByOperationId(self, operationId):
        raise NotImplementedError
        return

    def getCompletedQuestsByChainAndOperationId(self, chainId, operationId):
        raise NotImplementedError
        return

    def getQuestsByChainAndOperationId(self, chainId, operationId):
        raise NotImplementedError
        return

    def getFinalQuestsByChainAndOperationId(self, chainId, operationId):
        raise NotImplementedError
        return

    def getInitialQuestsByChainAndOperationId(self, chainId, operationId):
        raise NotImplementedError
        return

    def getOperationById(self, operationId):
        raise NotImplementedError
        return

    def getQuestFromGeneralID(self, generalID):
        raise NotImplementedError
        return

    def getOperations(self):
        raise NotImplementedError
        return

    def getFinalQuests(self):
        raise NotImplementedError
        return

    def getAllQuests(self):
        raise NotImplementedError
        return

    def getAllQuestsPM3(self):
        raise NotImplementedError
        return

    def getQuest(self, questId):
        raise NotImplementedError
        return

    def getQuestsByOperationId(self, operationId):
        raise NotImplementedError
        return

    def getCompletedQuestsByOperationId(self, operationId):
        raise NotImplementedError
        return

    def getFullCompletedQuestsByOperationId(self, operationId):
        raise NotImplementedError
        return

    def getSelectedQuestForChain(self, chainId, operationId):
        raise NotImplementedError
        return

    def getBadgesForChampionQuestPM3(self):
        raise NotImplementedError
        return

    def getVehiclesForChampionQuestPM3(self):
        raise NotImplementedError
        return

    @staticmethod
    def openVideoRewardAndUpdateAccSettings(operationId, accSettings):
        raise NotImplementedError
        return


class IParagonsController(IGameController, IEntitlementsConsumer):
    onSettingsChanged = None
    onAvailabilityChanged = None
    onLevelIncreased = None
    onProgressPointsChanged = None
    onFeatureStateChanged = None
    onParagonsUnlocksChanged = None
    onParagonsStateChanged = None
    onParagonsUnlocksStateChanged = None
    onSelectedRewardMarked = None
    onSelectedRewardTokenReceived = None

    @property
    def serverSettings(self):
        raise NotImplementedError
        return

    @property
    def isConsumesEntitlements(self):
        raise NotImplementedError
        return

    @property
    def paragons(self):
        raise NotImplementedError
        return

    @property
    def branches(self):
        raise NotImplementedError
        return

    @property
    def config(self):
        raise NotImplementedError
        return

    @property
    def isEnabled(self):
        raise NotImplementedError
        return

    @property
    def isPaused(self):
        raise NotImplementedError
        return

    @property
    def isInactive(self):
        raise NotImplementedError
        return

    @property
    def isBranchResetAvailable(self):
        raise NotImplementedError
        return

    @property
    def wasBranchResetEverAvailable(self):
        raise NotImplementedError
        return

    @property
    def isLimitedUiRuleCompleted(self):
        raise NotImplementedError
        return

    @property
    def chapterID(self):
        raise NotImplementedError
        return

    @property
    def availableChapters(self):
        raise NotImplementedError
        return

    @property
    def isAnyChapterAvailable(self):
        raise NotImplementedError
        return

    def isPreviewChapter(self, chapterID):
        raise NotImplementedError
        return

    @property
    def progress(self):
        raise NotImplementedError
        return

    @property
    def level(self):
        raise NotImplementedError
        return

    @property
    def minUnlockedNecessaryLevelVehiclesCount(self):
        raise NotImplementedError
        return

    @property
    def unlockedNecessaryLevelVehicleCDs(self):
        raise NotImplementedError
        return

    @property
    def unlockedNecessaryLevelVehiclesCount(self):
        raise NotImplementedError
        return

    @property
    def paragonsUnlockIDs(self):
        raise NotImplementedError
        return

    @property
    def lockedItems(self):
        raise NotImplementedError
        return

    @property
    def resetVehicles(self):
        raise NotImplementedError
        return

    @property
    def allChapterIDs(self):
        return NotImplementedError

    @property
    def availableChapterIDs(self):
        return NotImplementedError

    @property
    def completedChapterIDs(self):
        return NotImplementedError

    def clearCache(self):
        raise NotImplementedError
        return

    def getFirstChapterWithAvailableRewards(self):
        return NotImplementedError

    def isAllSelectablesClaimed(self, chapterID):
        return NotImplementedError

    def getProgressPoints(self, chapterID):
        return NotImplementedError

    def getSelectedRewardBonusCD(self, chapterID, levelID, entCode):
        return NotImplementedError

    def isVehicleReset(self, compDescr):
        raise NotImplementedError
        return

    def isNextResetVehUnlocked(self, compDescr):
        raise NotImplementedError
        return

    def isChapterComplete(self, chapterID=None):
        return NotImplementedError

    def isChapterPaused(self, chapterID=None):
        raise NotImplementedError
        return

    def isItemLocked(self, compDescr):
        raise NotImplementedError
        return

    def setChapter(self, chapterID, callback=None):
        raise NotImplementedError
        return

    def getDefaultVehicleProgressPoints(self, vehicleLevel):
        raise NotImplementedError
        return

    def getVehicleProgressPoints(self, compDescr):
        raise NotImplementedError
        return

    def isVehicleFirstUnlockPointsAvailable(self, vehicle, includeParagonsAvailable=True):
        raise NotImplementedError
        return

    def getVehicleFirstUnlockPoints(self, vehicle, includeParagonsAvailable=True):
        raise NotImplementedError
        return

    def getLockedResetVehicles(self, branchID):
        raise NotImplementedError
        return

    def isFirstUnlockBranchAvailable(self, branchID, includeParagonsAvailable=True):
        raise NotImplementedError
        return

    def getVehicleProgressPointsMultiplier(self, compDescr):
        raise NotImplementedError
        return

    def getVehicleResetBonusBlueprintsCount(self, compDescr):
        raise NotImplementedError
        return

    def getBranchResetVehicles(self, branchID):
        raise NotImplementedError
        return

    def getMaxLevelVehicles(self):
        raise NotImplementedError
        return

    def getHiddenUIItems(self):
        raise NotImplementedError
        return

    def getCompleteBonusCoinsForBranch(self, branchID):
        raise NotImplementedError
        return

    def getCoinsForBranchReset(self):
        raise NotImplementedError
        return

    def getChapterCloseoutTimeStamp(self, chapterID):
        raise NotImplementedError
        return

    def getClosestChapterCloseoutTimeStamp(self):
        raise NotImplementedError
        return


class IParagonsRewardsShopController(IGameController):
    onSelectableRewardReceived = None

    def getProducts(self):
        raise NotImplementedError
        return

    def buyProduct(self, productCode):
        raise NotImplementedError
        return

    def fetchProducts(self, callback=(lambda x: x)):
        raise NotImplementedError
        return

    @property
    def entitlements(self):
        raise NotImplementedError
        return

    def selectableRewardReceived(self, data):
        raise NotImplementedError
        return

    def isValidProduct(self, product, entitlementID):
        raise NotImplementedError
        return


class ICosmicEventBattleController(IGameController, ISeasonProvider):
    onPrimeTimeStatusUpdated = None
    onCosmicConfigChanged = None
    onStatusTick = None
    onLobbyRouteChange = None
    onVehicleSelected = None

    @property
    def isEnabled(self):
        raise NotImplementedError
        return

    def getEventVehicle(self):
        raise NotImplementedError
        return

    def getEventVehiclesIntCD(self):
        raise NotImplementedError
        return

    def isAvailable(self):
        raise NotImplementedError
        return

    def isBattleAvailable(self):
        raise NotImplementedError
        return

    def isFrozen(self):
        raise NotImplementedError
        return

    def switchPrb(self):
        raise NotImplementedError
        return

    def onPrbEnter(self):
        raise NotImplementedError
        return

    def onPrbLeave(self):
        raise NotImplementedError
        return

    def getModeSettings(self):
        raise NotImplementedError
        return

    def openQueueView(self):
        raise NotImplementedError
        return

    def openEventLobby(self):
        raise NotImplementedError
        return

    def getTokenProgressionID(self):
        raise NotImplementedError
        return

    def getProgressionQuestPrefix(self):
        raise NotImplementedError
        return

    def getVehicleRentQuestID(self):
        raise NotImplementedError
        return

    def getProgressionFinishedToken(self):
        raise NotImplementedError
        return

    def setClosingState(self):
        raise NotImplementedError
        return

    def isClosing(self):
        raise NotImplementedError
        return

    def isCosmicMode(self):
        raise NotImplementedError
        return

    def getLobbyRoute(self):
        raise NotImplementedError
        return

    def setLobbyRoute(self, route, notify=False):
        raise NotImplementedError
        return

    def isVehicleRentQuest(self, questID):
        raise NotImplementedError
        return

    def closeRewardScreen(self):
        raise NotImplementedError
        return

    def closePostBattleScreen(self):
        raise NotImplementedError
        return

    def getResourceIconForSelectedVehicle(self):
        raise NotImplementedError
        return


class IUnseenEventsCounter(IGameController):
    onUnseenEventUpdated = None
    onSeenEvents = None

    def addUnseenEvent(self, eventID, count):
        raise NotImplementedError
        return

    def updateUnseenEvents(self, eventsData):
        raise NotImplementedError
        return

    def getAllUnseenEventsCount(self):
        raise NotImplementedError
        return

    def isUnseenEvent(self, eventID):
        return eventID in self.__unseenQuests

    def seenEvent(self, eventID, count):
        raise NotImplementedError
        return

    def seenEvents(self, eventsData):
        raise NotImplementedError
        return

    def commitToSettings(self):
        raise NotImplementedError
        return

    def getUnseenEventsCount(self, eventsID):
        raise NotImplementedError
        return

    def cleanUpPremium(self):
        raise NotImplementedError
        return

    def clearBonusDQ(self):
        raise NotImplementedError
        return


class IBlackMarketController(IGameController):
    onStateChanged = None
    onBlackMarketUpdated = None

    def isEnabled(self):
        raise NotImplementedError
        return

    def isPaused(self):
        raise NotImplementedError
        return

    def getStartTime(self):
        raise NotImplementedError
        return

    def isStarted(self):
        raise NotImplementedError
        return

    def isSpecial(self):
        raise NotImplementedError
        return

    def getLastOfferStartDate(self):
        raise NotImplementedError
        return


class IEpicBattleController(IGameController):
    onQuestChanged = None
    onQuestProgressChanged = None
    onCurrentSectorChanged = None
    onOwnSectorsChanged = None
    onSectorProgressionChanged = None
    onProgressionModelChanged = None
    onSupplyActivated = None
    onAirshipCome = None

    def setQuest(self, questName):
        raise NotImplementedError
        return

    def setOwnSectors(self, sectors):
        raise NotImplementedError
        return

    def setCurrentSector(self, sectorID):
        raise NotImplementedError
        return

    def getQuest(self):
        raise NotImplementedError
        return

    def getQuestProgress(self):
        raise NotImplementedError
        return

    def getAimSector(self):
        raise NotImplementedError
        return

    def getOwnSectors(self):
        raise NotImplementedError
        return

    def getCurrentSector(self):
        raise NotImplementedError
        return

    def updateQuestProgress(self, questName, progressesInfo):
        raise NotImplementedError
        return

    def reset(self):
        raise NotImplementedError
        return

    def setSectorProgression(self, progression):
        raise NotImplementedError
        return

    def getSectorProgression(self):
        raise NotImplementedError
        return

    def isOnOwnSector(self):
        raise NotImplementedError
        return

    def getSectorName(self, sectorID):
        raise NotImplementedError
        return


class INewbieEntryPointController(IGameController):

    def setExperienceLevel(self, expLevel):
        raise NotImplementedError
        return

    def isStoryModeEnabled(self):
        raise NotImplementedError
        return

    def isNewbieStartPageEnabled(self):
        raise NotImplementedError
        return

    def goToStoryModeQueue(self, guiCtx):
        raise NotImplementedError
        return

    def goToHangar(self, guiCtx):
        raise NotImplementedError
        return


class ISummerSaleController(IGameController):
    onEventSettingsUpdated = None

    def getStartTime(self):
        raise NotImplementedError
        return

    def getExpiryTime(self):
        raise NotImplementedError
        return

    def getQuestGroupId(self):
        raise NotImplementedError
        return

    def getProductTag(self):
        raise NotImplementedError
        return

    def isEnabled(self):
        raise NotImplementedError
        return

    def isRandomVehicleObtained(self):
        raise NotImplementedError
        return

    def isFinished(self):
        raise NotImplementedError
        return

    def isEnding(self):
        raise NotImplementedError
        return

    def getLocalEndDate(self):
        raise NotImplementedError
        return

    def fetchProducts(self, callback=(lambda x: x)):
        raise NotImplementedError
        return

    def buyProduct(self, productCode, count=1):
        raise NotImplementedError
        return

    def getShopPageUrl(self):
        raise NotImplementedError
        return

    def getSummerSaleSetType(self):
        raise NotImplementedError
        return

    def getSummerSaleSetProductCode(self):
        raise NotImplementedError
        return

    def getSummerSaleSetCategory(self):
        raise NotImplementedError
        return

    def getSummerSaleVehiclesSetType(self):
        raise NotImplementedError
        return

    def getSummerSaleVehicleSetProductCode(self):
        raise NotImplementedError
        return

    def getSummerSaleVehicleSetCategory(self):
        raise NotImplementedError
        return

    def getProductsOrder(self):
        raise NotImplementedError
        return

    def getBalance(self, currency):
        raise NotImplementedError
        return


class IControlPointOverrideController(IGameController):
    pass


class ITankAcademyController(IGameController):
    onStateChanged = None
    onFinish = None

    def isEnabled(self):
        raise NotImplementedError
        return

    def isFinished(self):
        raise NotImplementedError
        return

    def isActive(self):
        raise NotImplementedError
        return

    def isValidConfiguration(self):
        raise NotImplementedError
        return

    def hasUnobtainedDelayedRewards(self):
        raise NotImplementedError
        return

    def hasOfferToken(self, offerToken):
        raise NotImplementedError
        return

    def hasDelayedRewardToken(self, delayedRewardToken):
        raise NotImplementedError
        return

    def hasDelayedRewardsInQuest(self, quest):
        raise NotImplementedError
        return

    def isFinalQuest(self, quest):
        raise NotImplementedError
        return

    def getFinalQuest(self):
        raise NotImplementedError
        return

    def getFirstQuest(self):
        raise NotImplementedError
        return

    def isTankAcademyQuestID(self, questID):
        raise NotImplementedError
        return

    def getQuestByIdx(self, questIdx):
        raise NotImplementedError
        return

    def getCompletedTankAcademyQuests(self):
        raise NotImplementedError
        return

    def getCompletedTankAcademyQuestsCount(self):
        raise NotImplementedError
        return

    def markPostBattleAutoShowSuppressed(self, arenaUniqueID):
        raise NotImplementedError
        return

    def consumePostBattleAutoShowSuppressed(self, arenaUniqueID):
        raise NotImplementedError
        return

    def getNotCompletedTankAcademyQuests(self):
        raise NotImplementedError
        return

    def getTankAcademyQuestsByGroup(self, questGroup):
        raise NotImplementedError
        return

    def getTankAcademyQuests(self, filterFunc=None):
        raise NotImplementedError
        return

    def getTankAcademyQuestGroups(self, filterFunc=None):
        raise NotImplementedError
        return

    def getCountTankAcademyQuests(self):
        raise NotImplementedError
        return

    def showAwardView(self, questsData, clientCtx=None):
        raise NotImplementedError
        return

    def getCurrentQuest(self):
        raise NotImplementedError
        return

    def getCurrentQuestOrder(self):
        raise NotImplementedError
        return

    def getQuestProgress(self, quest):
        raise NotImplementedError
        return

    def getSelectedVehicle(self, offerToken):
        raise NotImplementedError
        return

    def hasAccessToken(self):
        raise NotImplementedError
        return

    def getDelayedRewardCurrencyTokens(self):
        raise NotImplementedError
        return

    def getVehicleOfferTokensWithUnobtainedGifts(self):
        raise NotImplementedError
        return

    def getDelayedRewardExpirationTime(self):
        raise NotImplementedError
        return

    def isTAOfferToken(self, token):
        raise NotImplementedError
        return

    def isDelayedRewardToken(self, token):
        raise NotImplementedError
        return

    def isOfferRewardObtained(self, offerToken):
        raise NotImplementedError
        return

    def isDelayedRewardObtained(self, delayedRewardToken):
        raise NotImplementedError
        return

    def getOfferProperties(self, offerToken):
        raise NotImplementedError
        return

    def getOfferTokenByDelayedRewardCurrencyToken(self, delayedRewardCurrencyToken):
        raise NotImplementedError
        return

    def getABTestConfiguration(self):
        raise NotImplementedError
        return

    def getHangarWidgetAlias(self):
        raise NotImplementedError
        return

    def isFirstQuestCompleted(self):
        raise NotImplementedError
        return


class IMuseumOfGloryController(IGameController):
    onConfigUpdate = None

    @property
    def isEnabled(self):
        raise NotImplementedError
        return

    def getEpochMusics(self, year):
        raise NotImplementedError
        return

    def getVehiclesDto(self):
        raise NotImplementedError
        return

    def getBackgroundImage(self, year):
        raise NotImplementedError
        return

    def getMinYear(self):
        raise NotImplementedError
        return
