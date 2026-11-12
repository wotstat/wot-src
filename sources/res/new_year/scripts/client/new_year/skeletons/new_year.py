import typing
from adisp import adisp_async, adisp_process
from skeletons.gui.game_control import IFestivityController, IGameController, IFestivityFirstEnterVideoController
if typing.TYPE_CHECKING:
    from Event import Event
    from ..tamagotchi.dto.leaderboard import Leaderboard
    from ..tamagotchi.dto.config import Config
    from ..tamagotchi.dto.player_info import PlayerInfo
    from ..tamagotchi.dto.player_stats import PlayerStats

class INewYearController(IFestivityController):
    onDataUpdated = None
    onUpdateSlot = None
    onSetHangToyEffectEnabled = None
    onVariadicDiscountsUpdated = None
    onCustomizationObjectUpdated = None
    onSpaceObjectHover = None
    onGUIObjectHover = None
    onNySettingsChanged = None
    onOnboardingFinished = None
    onUIControlsLockChanged = None
    onPetVisibilityUpdated = None
    onPetRaidVisibilityUpdated = None

    def isEnabled(self):
        raise NotImplementedError
        return

    def isInProgress(self):
        raise NotImplementedError
        return

    def isPostEvent(self):
        raise NotImplementedError
        return

    def isFinished(self):
        raise NotImplementedError
        return

    def isSuspended(self):
        raise NotImplementedError
        return

    def isFirstEntrance(self):
        raise NotImplementedError
        return

    def isOnboardingOpen(self):
        raise NotImplementedError
        return

    def isMaxAtmosphereLevel(self):
        raise NotImplementedError
        return

    def getHangarQuestsFlagData(self):
        raise NotImplementedError
        return

    def getHangarWidgetLinkage(self):
        raise NotImplementedError
        return

    def getHangarEdgeColor(self):
        raise NotImplementedError
        return

    def getSlotDescrs(self):
        raise NotImplementedError
        return

    def getToyDescr(self, toyID):
        raise NotImplementedError
        return

    def getToyByID(self, toyID):
        raise NotImplementedError
        return

    def getToysByType(self, slotID):
        raise NotImplementedError
        return

    def getAllToysByTypeFromCache(self, typeID):
        raise NotImplementedError
        return

    def getAllCollectedToysId(self, year=None):
        raise NotImplementedError
        return

    @adisp_async
    def hangToy(self, toyID, slotID, callback=None):
        raise NotImplementedError
        return

    @adisp_async
    def buyToy(self, toyID, callback=None):
        raise NotImplementedError
        return

    def getLevel(self, level):
        raise NotImplementedError
        return

    def checkForNewToys(self, slot=None, objectType=None):
        raise NotImplementedError
        return

    def isCollectionCompleted(self, collectionID=None):
        raise NotImplementedError
        return

    def getFinishTime(self):
        raise NotImplementedError
        return

    def showStateMessage(self):
        raise NotImplementedError
        return

    def sendSeenToys(self, toyIDs):
        raise NotImplementedError
        return

    def sendSeenToysInCollection(self, toyIDs):
        raise NotImplementedError
        return

    def sendViewAlbum(self, settingID, rank):
        raise NotImplementedError
        return

    def getUniqueMegaToysCount(self):
        raise NotImplementedError
        return

    def isFullRegularToysGroup(self, typeID, settingID, rank):
        raise NotImplementedError
        return

    def isRegularToysCollected(self):
        raise NotImplementedError
        return

    def getMaxToysStyle(self):
        raise NotImplementedError
        return

    def getActiveSettingBonusValue(self):
        raise NotImplementedError
        return

    def getMaxBonusValue(self):
        raise NotImplementedError
        return

    def getVariadicDiscountCount(self):
        raise NotImplementedError
        return

    def updateVariadicDiscounts(self):
        raise NotImplementedError
        return

    def markPreviousYearTabVisited(self, yearName, settingsKey):
        raise NotImplementedError
        return

    def getCollectionAwardQuest(self, collectionTypeToQuest, collectionType, filterFunc):
        raise NotImplementedError
        return

    @property
    def firstEnterVideo(self):
        raise NotImplementedError
        return

    @property
    def leaderboardTankReward(self):
        raise NotImplementedError
        return

    def isWidgetVisible(self, prbState):
        raise NotImplementedError
        return

    def isCreditBonusVisible(self, prbState):
        raise NotImplementedError
        return

    def setSpaceObjectHover(self, gameObject, value):
        raise NotImplementedError
        return

    def setGuiObjectHover(self, objectName, value):
        raise NotImplementedError
        return

    def lockUIControls(self, lockID):
        raise NotImplementedError
        return

    def unlockUIControls(self, lockID):
        raise NotImplementedError
        return

    def isUIControlsLocked(self):
        raise NotImplementedError
        return

    def isLootboxBigType(self, lbType):
        raise NotImplementedError
        return

    def isLootboxTankType(self, lbType):
        raise NotImplementedError
        return

    @adisp_async
    @adisp_process
    def switchToNewYearPrebattle(self, callback):
        raise NotImplementedError
        return

    @adisp_process
    def switchFromNewYearPrebattle(self):
        raise NotImplementedError
        return

    def isNewYearBattleMode(self):
        raise NotImplementedError
        return

    @property
    def prbNewYearActionName(self):
        raise NotImplementedError
        return

    def isCelebVoiceoverEnabled(self):
        raise NotImplementedError
        return

    def isQuestsCelebVoiceoverEnabled(self):
        raise NotImplementedError
        return

    def isMachineCelebVoiceoverEnabled(self):
        raise NotImplementedError
        return


class INewYearFirstEnterVideoController(IFestivityFirstEnterVideoController):
    pass


class INewYearSurpriseMachine(IGameController):
    onStateUpdate = None
    onMachineButtonPress = None
    onScreenButtonClick = None
    onUpdateApplyCoin = None
    onMachineButtonHovered = None
    onActivationChanged = None
    onMachineBusyStatusUpdated = None

    @property
    def machineState(self):
        raise NotImplementedError
        return

    @property
    def canApplyCoin(self):
        raise NotImplementedError
        return

    @property
    def canBuyCoin(self):
        raise NotImplementedError
        return

    @property
    def isMachineBusy(self):
        raise NotImplementedError
        return

    @property
    def isMachineActivated(self):
        raise NotImplementedError
        return

    @property
    def selectedAmountButton(self):
        raise NotImplementedError
        return

    def setState(self, state):
        raise NotImplementedError
        return

    def setViewState(self, state):
        raise NotImplementedError
        return

    def refreshApplyCoinState(self):
        raise NotImplementedError
        return

    def updateSurpriseMachineBusyStatus(self, isBusy):
        raise NotImplementedError
        return

    def tryActivateMachine(self):
        raise NotImplementedError
        return

    def deactivateMachine(self):
        raise NotImplementedError
        return

    def selectAmountButton(self, button):
        raise NotImplementedError
        return

    def resetSelection(self):
        raise NotImplementedError
        return


class IRaccoonAnimationController(IGameController):
    onRaidStateChanged = None
    onTvRaidPresentationChanged = None
    onTvAnimationChanged = None

    @property
    def isRaidStarted(self):
        raise NotImplementedError
        return

    @property
    def isRaidActive(self):
        raise NotImplementedError
        return

    @property
    def tvAnimation(self):
        raise NotImplementedError
        return

    def setRaidActive(self, isActive):
        raise NotImplementedError
        return

    def beginTvRaidPresentation(self):
        raise NotImplementedError
        return

    def endRaidTvPresentation(self):
        raise NotImplementedError
        return

    def onTvPresentationFinished(self):
        raise NotImplementedError
        return

    def setTvAnimation(self, animation):
        raise NotImplementedError
        return

    def activateItem(self, name):
        raise NotImplementedError
        return

    def updateMoodState(self, state):
        raise NotImplementedError
        return

    def setAnimationsEnabled(self, enabled):
        raise NotImplementedError
        return


class INewYearEnvironmentSwitchController(IGameController):
    onEnvironmentSwitched = None

    @property
    def userEnvState(self):
        raise NotImplementedError
        return

    @property
    def resolvedUserEnvState(self):
        raise NotImplementedError
        return

    @property
    def needToShowTip(self):
        raise NotImplementedError
        return

    @property
    def currentDayNightMode(self):
        raise NotImplementedError
        return

    @property
    def currentAppliedDayNightMode(self):
        raise NotImplementedError
        return

    @property
    def isAppliedDay(self):
        raise NotImplementedError
        return

    def notifyTipShouldClose(self):
        raise NotImplementedError
        return

    def skipSwitcherTip(self):
        raise NotImplementedError
        return

    def applyCurrentEnvironment(self):
        raise NotImplementedError
        return

    def switchEnvironment(self, envState, setCallback=True):
        raise NotImplementedError
        return

    def switchDayNightMode(self, envState):
        raise NotImplementedError
        return

    def resolveDayNightMode(self, envState):
        raise NotImplementedError
        return

    def getTimeAngle(self):
        raise NotImplementedError
        return


class INewYearCurrencyController(IGameController):
    onCurrencyUpdated = None
    onVisibleCurrenciesChanged = None

    @property
    def getCurrencies(self):
        raise NotImplementedError
        return

    @property
    def getGiftMachineTokenCount(self):
        raise NotImplementedError
        return

    @property
    def getMandarinTokenCount(self):
        raise NotImplementedError
        return

    @property
    def getGoldCount(self):
        raise NotImplementedError
        return

    def getCurrencyCount(self, currency):
        raise NotImplementedError
        return

    def getCurrencyClickHandler(self, currency):
        raise NotImplementedError
        return

    def setVisibleCurrencies(self, currencies=None):
        raise NotImplementedError
        return


class INewYearTamagotchiController(IGameController):
    onRaidDataUpdated = None

    @property
    def isEntObtained(self):
        raise NotImplementedError
        return

    @property
    def isPetVisible(self):
        raise NotImplementedError
        return

    def getRaidData(self):
        raise NotImplementedError
        return

    def getRaidState(self):
        raise NotImplementedError
        return

    def getRaidMetaData(self):
        raise NotImplementedError
        return

    def getRaidBoostAmount(self):
        raise NotImplementedError
        return

    def onLobbyInited(self, event):
        raise NotImplementedError
        return


class INewYearMetricsLogger(object):
    __slots__ = ()

    def logSwitcherOpened(self):
        raise NotImplementedError
        return

    def logQuestsScreenClosed(self, animation):
        raise NotImplementedError
        return

    def logQuestsVoiceoverSwitch(self, isEnabled):
        raise NotImplementedError
        return

    def logMachineScreenOpened(self, animation):
        raise NotImplementedError
        return

    def logMachineScreenClosed(self, animation):
        raise NotImplementedError
        return

    def logMachineCoinExchange(self, count):
        raise NotImplementedError
        return

    def logMachineTokenUsed(self, count):
        raise NotImplementedError
        return

    def logLeaderboardScreenOpened(self):
        raise NotImplementedError
        return

    def logWeeklyRewardsScreenOpened(self):
        raise NotImplementedError
        return

    def logPetScreenOpened(self):
        raise NotImplementedError
        return

    def logPetRepeatOnboardingClick(self, count):
        raise NotImplementedError
        return

    def logRaidRepeatOnboardingClick(self, count):
        raise NotImplementedError
        return

    def logEasterEggVideoOpened(self, videoId):
        raise NotImplementedError
        return


class ITamagotchiWebRequester(object):
    __slots__ = ()

    def requestPlayerInfo(self, callback=None):
        raise NotImplementedError
        return

    def requestLeaderboardPage(self, page=0, isUserPage=False, cumulative=False):
        raise NotImplementedError
        return

    def requestPlayerStats(self, forFinalCache=False):
        raise NotImplementedError
        return

    def buyItems(self, itemsDict):
        raise NotImplementedError
        return

    def activateItem(self, itemId, count):
        raise NotImplementedError
        return


class ITamagotchiDataProvider(object):
    __slots__ = (b'onLeaderBoardUpdated', b'onPlayerInfoUpdated', b'onPlayerStatsUpdated', b'onRaccoonStateUpdated', b'onBonusUpdated', b'onSimulationEnd', b'onItemsActivateRequested', b'onItemsActivated', b'onItemsPurchased', b'onOnboardingChanged', b'onViewVisibilityChanged', b'onUpdateTipsRequested', b'onNextSeasonStarted', b'onSeasonEnded', b'onOnboardingSkipped', b'onRaidReadyUpdated', b'onTamagotchiRaidViewEnabledChanged', b'onDecreasedIndicatorsPoints')

    def __init__(self):
        super(ITamagotchiDataProvider, self).__init__()
        self.onLeaderBoardUpdated = None
        self.onPlayerStatsUpdated = None
        self.onRaccoonStateUpdated = None
        self.onBonusUpdated = None
        self.onSimulationEnd = None
        self.onItemsActivateRequested = None
        self.onItemsActivated = None
        self.onItemsPurchased = None
        self.onOnboardingChanged = None
        self.onOnboardingSkipped = None
        self.onViewVisibilityChanged = None
        self.onPlayerInfoUpdated = None
        self.onUpdateTipsRequested = None
        self.onNextSeasonStarted = None
        self.onSeasonEnded = None
        self.onRaidReadyUpdated = None
        self.onTamagotchiRaidViewEnabledChanged = None
        self.onDecreasedIndicatorsPoints = None
        return

    @property
    def isValidConfig(self):
        raise NotImplementedError
        return

    @property
    def raccoonState(self):
        raise NotImplementedError
        return

    @raccoonState.setter
    def raccoonState(self, value):
        raise NotImplementedError
        return

    @property
    def leaderboard(self):
        raise NotImplementedError
        return

    @leaderboard.setter
    def leaderboard(self, value):
        raise NotImplementedError
        return

    @property
    def cumulativeLeaderboard(self):
        raise NotImplementedError
        return

    @cumulativeLeaderboard.setter
    def cumulativeLeaderboard(self, value):
        raise NotImplementedError
        return

    @property
    def config(self):
        raise NotImplementedError
        return

    @config.setter
    def config(self, value):
        raise NotImplementedError
        return

    @property
    def playerInfo(self):
        raise NotImplementedError
        return

    @playerInfo.setter
    def playerInfo(self, value):
        raise NotImplementedError
        return

    @property
    def initialPlayerInfo(self):
        raise NotImplementedError
        return

    @property
    def isOnboarding(self):
        raise NotImplementedError
        return

    @isOnboarding.setter
    def isOnboarding(self, value):
        raise NotImplementedError
        return

    @property
    def isLeaderboardFinished(self):
        raise NotImplementedError
        return

    @property
    def isLeaderboardRecalcPeriod(self):
        raise NotImplementedError
        return

    @property
    def isCumulativeFinished(self):
        raise NotImplementedError
        return

    def canCacheFinalPlayerStats(self):
        raise NotImplementedError
        return

    @property
    def hasCumulativeLeaderboard(self):
        raise NotImplementedError
        return

    def reset(self):
        raise NotImplementedError
        return

    def resetData(self):
        raise NotImplementedError
        return

    def getIndicatorCurrency(self, name):
        raise NotImplementedError
        return

    def getDeb(self):
        raise NotImplementedError
        return

    def getIndicatorDeb(self, name):
        raise NotImplementedError
        return

    def getNeeds(self):
        raise NotImplementedError
        return

    def isIndicatorLocked(self, name):
        raise NotImplementedError
        return

    def syncOpenedIndicators(self):
        raise NotImplementedError
        return

    def setRaidReady(self, isReady=None):
        raise NotImplementedError
        return

    @property
    def isRaidReady(self):
        raise NotImplementedError
        return

    def getRaidState(self):
        raise NotImplementedError
        return

    def getRaidRemainingTime(self):
        raise NotImplementedError
        return

    def isRaidActive(self):
        raise NotImplementedError
        return

    def hasRaidLoot(self):
        raise NotImplementedError
        return

    def isReadyForRaid(self):
        raise NotImplementedError
        return

    def getIndicatorStateDecayTime(self, name):
        raise NotImplementedError
        return

    def getIndicatorDecayTime(self, name):
        raise NotImplementedError
        return

    def getIndicatorStates(self):
        raise NotImplementedError
        return

    @property
    def playerStats(self):
        raise NotImplementedError
        return

    @playerStats.setter
    def playerStats(self, value):
        raise NotImplementedError
        return

    @property
    def playerStatsGeneration(self):
        raise NotImplementedError
        return

    def tryStartFinalPlayerStatsRequest(self):
        raise NotImplementedError
        return

    def allocatePlayerStatsRequestSeq(self):
        raise NotImplementedError
        return

    def applyPlayerStats(self, value, asFinalCache=False, startedWhenFinalReady=False, requestGeneration=None, requestSeq=None):
        raise NotImplementedError
        return

    @property
    def hasFinalPlayerStatsCache(self):
        raise NotImplementedError
        return

    @property
    def wasInLeaderboard(self):
        raise NotImplementedError
        return

    def getRewardedTopThreshold(self, seasonId, playerPos):
        raise NotImplementedError
        return

    def getCumulativeReward(self):
        raise NotImplementedError
        return

    def getPlayerStat(self, seasonId):
        raise NotImplementedError
        return

    def getLeaderboard(self, seasonId):
        raise NotImplementedError
        return
