from __future__ import absolute_import
import logging, typing
from future.utils import iteritems, viewvalues
from adisp import adisp_process
from gui.shared.event_dispatcher import showOfferGiftsWindow
from shared_utils import findFirst, first
from Event import EventManager, Event
from PlayerEvents import g_playerEvents
from account_helpers.AccountSettings import AccountSettings, INGAME_TOURNAMENT_SECTION, INGAME_TOURNAMENT_WCI_INTRO_SEEN, INGAME_TOURNAMENT_OLS_INTRO_SEEN
from constants import CURRENT_REALM
from constants import Configs
from gui.Scaleform.daapi.view.lobby.store.browser.shop_helpers import getShopURL
from gui.game_control.links import URLMacros
from gui.impl.lobby.user_missions.hangar_widget.services import IEventsService
from gui.prb_control.entities.listener import IGlobalListener
from gui.shared import events, g_eventBus
from gui.shop import showIngameShop
from gui.wgcg import IWebController
from gui.wgcg.ingame_tournaments.context import IngameTournamentGetDataCtx
from helpers import dependency
from helpers.CallbackDelayer import CallbackDelayer
from helpers.ingame_tournament_helper import IngameTournamentState, IngameTournamentMatchState, IngameTournamentUrlType, IngameTournamentLogoSize, IngameTournamentBracketType, IngameTournamentType
from helpers.time_utils import getServerUTCTime
from skeletons.gui.game_control import IIngameTournamentController
from skeletons.gui.lobby_context import ILobbyContext
from skeletons.gui.offers import IOffersDataProvider
_logger = logging.getLogger(__name__)

class _TeamData(typing.NamedTuple(b'_TeamData', (
 (
  b'teamID', int), (b'name', str), (b'logoURLs', dict)))):

    @classmethod
    def fromParamsDict(cls, params):
        teamID = params.get(b'id', 0)
        name = params.get(b'name', b'')
        logoURLs = {}
        for sizeStr, url in iteritems(params.get(b'logo_urls', {})):
            logoSize = cls.__getLogoSizeByStr(sizeStr)
            if logoSize:
                logoURLs[logoSize] = url

        if not teamID or not name or not logoURLs:
            _logger.warning(b'Ingame tournament parsing error - team data error')
        return cls(teamID, name, logoURLs)

    @staticmethod
    def __getLogoSizeByStr(logoSizeStr):
        logoSizeStr = logoSizeStr.replace(b'\xc3\x97', b'x')
        return findFirst((lambda logo: logo.value == logoSizeStr), IngameTournamentLogoSize)


class _MatchData(typing.NamedTuple(b'_MatchData', (
 (
  b'round', int), (b'startTime', int), (b'victories', int), (b'bracketType', IngameTournamentBracketType),
 (
  b'teamID1', int), (b'teamScore1', int), (b'teamID2', int), (b'teamScore2', int), (b'stageIndex', int)))):

    @classmethod
    def fromParamsDict(cls, params, bracketType, stageIndex):
        round = params.get(b'round')
        start = params.get(b'start_at')
        victories = params.get(b'victories')
        if round is None or start is None or victories is None:
            _logger.info(b'Ingame tournament parsing error - match params must be set to valid values')
            return
        else:
            team1 = params.get(b'team_1') or {}
            teamID1 = team1.get(b'id')
            teamScore1 = team1.get(b'score')
            team2 = params.get(b'team_2') or {}
            teamID2 = team2.get(b'id')
            teamScore2 = team2.get(b'score')
            return cls(round, start, victories, bracketType, teamID1, teamScore1, teamID2, teamScore2, stageIndex)

    @property
    def state(self):
        currentTime = getServerUTCTime()
        if currentTime < self.startTime:
            return IngameTournamentMatchState.UPCOMING
        else:
            if self.teamScore1 is not None and self.teamScore2 is not None:
                return IngameTournamentMatchState.COMPLETED
            return IngameTournamentMatchState.IN_LIVE

    @property
    def bestOf(self):
        return self.victories * 2 - 1


class _GroupData(typing.NamedTuple(b'_GroupData', (
 (
  b'groupID', int), (b'matches', list)))):

    @classmethod
    def fromParamsDict(cls, params, bracketType, stageIndex):
        matches = params.get(b'matches', [])
        if not matches:
            _logger.warning(b'Ingame tournament parsing error - matches are missing or empty')
        formattedMatches = []
        for match in matches:
            formattedMatch = _MatchData.fromParamsDict(match, bracketType, stageIndex)
            if formattedMatch is not None:
                formattedMatches.append(formattedMatch)

        formattedMatches.sort(key=(lambda formattedMatch: formattedMatch.startTime))
        groupID = params.get(b'id')
        if not groupID:
            _logger.warning(b'Ingame tournament parsing error - group id not set')
        return cls(groupID, formattedMatches)


class _StageData(typing.NamedTuple(b'_StageData', (
 (
  b'groups', list),))):

    @classmethod
    def fromParamsDict(cls, params, stageIndex):
        groups = params.get(b'groups')
        if not groups:
            _logger.warning(b'Ingame tournament parsing error - groups are missing or empty')
            return cls([])
        bracketTypeStr = params.get(b'bracket_type')
        bracketType = findFirst((lambda bracket: bracket.value == bracketTypeStr), IngameTournamentBracketType)
        if not bracketType:
            _logger.warning(b'Ingame tournament parsing error - bracket_type is missing or incorrect')
        formattedGroups = []
        for group in groups:
            formattedGroups.append(_GroupData.fromParamsDict(group, bracketType, stageIndex))

        return cls(formattedGroups)


class _RewardData(typing.NamedTuple(b'_RewardData', (
 (
  b'fromPosition', int), (b'toPosition', int), (b'amount', int)))):

    @classmethod
    def fromParamsDict(cls, params):
        fromPosition = params.get(b'from_position')
        toPosition = params.get(b'to_position')
        if fromPosition is None or toPosition is None:
            _logger.warning(b'Ingame tournament parsing error - reward positions not set')
        amount = params.get(b'prize_count', 0)
        if amount == 0:
            _logger.warning(b'Ingame tournament parsing error - prize_count is not set')
        return cls(fromPosition, toPosition, amount)


class _LeaderboardData(typing.NamedTuple(b'_LeaderboardData', (
 (
  b'fromPosition', int), (b'toPosition', int), (b'teamIDs', list)))):

    @classmethod
    def fromParamsData(cls, paramsData):
        position = first(paramsData).get(b'position')
        teams = [data.get(b'team_id') for data in paramsData]
        if not position or not teams:
            _logger.warning(b'Ingame tournament parsing error - wrong leaderboard position params')
        return cls(position - len(teams) + 1, position, teams)


class _PrizePoolData(typing.NamedTuple(b'_PrizePoolData', (
 (
  b'qty', int), (b'updated_at', int), (b'is_dynamic', bool)))):

    @classmethod
    def fromParamsData(cls, paramsData):
        amount = paramsData.get(b'qty')
        if amount is None:
            _logger.warning(b'Ingame tournament parsing error - dynamic prize_pool->qty is not set')
        updatedAt = paramsData.get(b'updated_at')
        if updatedAt is None:
            _logger.warning(b'Ingame tournament parsing error - dynamic prize_pool->updated_at is not set')
        return cls(amount, updatedAt, True)


class _IngameTournamentData(typing.NamedTuple(b'_IngameTournamentData', (
 (
  b'stages', list),
 (
  b'rewards', list),
 (
  b'streamURLs', dict),
 (
  b'teams', dict),
 (
  b'leaderboard', list),
 (
  b'prizePool', _PrizePoolData)))):

    @classmethod
    def fromRequestResponse(cls, wgcgResponse):
        if not wgcgResponse or not wgcgResponse.isSuccess():
            _logger.warning(b'Ingame tournament parsing error - WGCG response is in error state')
            return None
        else:
            data = wgcgResponse.data or {}
            stages = data.get(b'stages', [])
            if not stages:
                _logger.warning(b'Ingame tournament parsing error - stages section are missing or empty')
            formattedStages = []
            for i, stage in enumerate(stages):
                formattedStages.append(_StageData.fromParamsDict(stage, i))

            rewards = data.get(b'rewards', [])
            if not rewards:
                _logger.warning(b'Ingame tournament parsing error - rewards section are missing or empty')
            formattedRewards = []
            for reward in rewards:
                formattedRewards.append(_RewardData.fromParamsDict(reward))

            streamURLs = data.get(b'stream_urls', [])
            if not streamURLs:
                _logger.warning(b'Ingame tournament parsing error - stream_urls section are missing or empty')
            formattedURLs = {}
            for streamURL in streamURLs:
                urlType, url = cls.__getStreamUrlData(streamURL)
                if urlType and url:
                    formattedURLs[urlType] = url

            teams = data.get(b'teams', [])
            if not teams:
                _logger.warning(b'Ingame tournament parsing error - teams section are missing or empty')
            formattedTeams = {}
            for team in teams:
                formattedTeam = _TeamData.fromParamsDict(team)
                formattedTeams[formattedTeam.teamID] = formattedTeam

            leaderboard = data.get(b'positions', [])
            leaderboardByPositionData = {}
            for paramsSection in leaderboard:
                leaderboardByPositionData.setdefault(paramsSection.get(b'position'), []).append(paramsSection)

            formattedLeaderboard = []
            for positionData in viewvalues(leaderboardByPositionData):
                formattedLeaderboard.append(_LeaderboardData.fromParamsData(positionData))

            formattedLeaderboard.sort(key=(lambda leaderboardPosition: leaderboardPosition.fromPosition))
            prizePool = data.get(b'prize_pool', {})
            if prizePool:
                formattedPrizePool = _PrizePoolData.fromParamsData(prizePool)
                formattedRewards = [_RewardData(fromPosition=rewardData.fromPosition, toPosition=rewardData.toPosition, amount=rewardData.amount * formattedPrizePool.qty // 100000000) for rewardData in formattedRewards]
                _logger.info(b'Ingame tournament - dynamic prize pool configured')
            else:
                formattedPrizePool = _PrizePoolData(0, 0, False)
                _logger.info(b'Ingame tournament - constant prize pool configured')
            return cls(formattedStages, formattedRewards, formattedURLs, formattedTeams, formattedLeaderboard, formattedPrizePool)

    def getLiveMatch(self):
        for stage in self.stages:
            for group in stage.groups:
                liveMatch = findFirst((lambda match: match.state == IngameTournamentMatchState.IN_LIVE), group.matches)
                if liveMatch is not None:
                    return liveMatch

        return

    def getUpcomingMatches(self):
        matches = []
        for stage in self.stages:
            for group in stage.groups:
                matches.extend([match for match in group.matches if match.state == IngameTournamentMatchState.UPCOMING])

        matches.sort(key=(lambda match: match.startTime))
        return matches

    def getAllMatches(self):
        matches = []
        for stage in self.stages:
            for group in stage.groups:
                matches.extend(group.matches)

        matches.sort(key=(lambda match: match.startTime))
        return matches

    def getTotalRewardAmount(self):
        if self.prizePool.is_dynamic:
            return self.prizePool.qty
        return sum(reward.amount for reward in self.rewards)

    def getLastPrizePoolUpdate(self):
        return self.prizePool.updated_at

    def isDynamicPrizePool(self):
        return self.prizePool.is_dynamic

    def getLeaderboardDataByTeam(self, teamID):
        return findFirst((lambda data: teamID in data.teamIDs), self.leaderboard)

    def getRewardForPosition(self, position):
        return findFirst((lambda reward: reward.fromPosition <= position <= reward.toPosition), self.rewards)

    @classmethod
    def __getStreamUrlData(cls, params):
        url = params.get(b'url', b'')
        urlTypeStr = params.get(b'type')
        urlType = findFirst((lambda urlType: urlType.value == urlTypeStr), IngameTournamentUrlType)
        if not url or not urlType:
            _logger.warning(b'Ingame tournament parsing error - stream URL or type must be set to valid value')
            return (None, None)
        else:
            return (
             urlType, url)


class IngameTournamentController(IIngameTournamentController, IGlobalListener):
    __lobbyContext = dependency.descriptor(ILobbyContext)
    __webCtrl = dependency.descriptor(IWebController)
    __eventsService = dependency.descriptor(IEventsService)
    __offersProvider = dependency.descriptor(IOffersDataProvider)

    def __init__(self):
        super(IngameTournamentController, self).__init__()
        self.__serverSettings = None
        self.__availabilityByTournamentType = {}
        self.__callbackDelayer = CallbackDelayer()
        self.__eventsManager = em = EventManager()
        self.onTournamentEntryPointUpdated = Event(em)
        self.onTournamentWGCGDataUpdated = Event(em)
        return

    def fini(self):
        self.__serverSettings = None
        self.__availabilityByTournamentType = None
        self.__callbackDelayer.destroy()
        self.__callbackDelayer = None
        self.__eventsManager.clear()
        self.__eventsManager = None
        return

    def onAccountBecomePlayer(self):
        self.__serverSettings = self.__lobbyContext.getServerSettings()
        self.__lobbyContext.onServerSettingsChanged += self.__onServerSettingsChanged
        if self.__serverSettings is not None:
            self.__serverSettings.onServerSettingsChange += self.__onConfigUpdated
        self.__updateTournamentEntryPoint()
        return

    def onAccountBecomeNonPlayer(self):
        self.__lobbyContext.onServerSettingsChanged -= self.__onServerSettingsChanged
        if self.__serverSettings is not None:
            self.__serverSettings.onServerSettingsChange -= self.__onConfigUpdated
        self.__serverSettings = None
        self.__callbackDelayer.clearCallbacks()
        return

    def isTournamentAvailable(self, tournamentType):
        config = self.__getConfigByTournamentType(tournamentType)
        return config is not None and config.isEnabled

    def getTournamentState(self, tournamentType):
        config = self.__getConfigByTournamentType(tournamentType)
        if config is None or not config.isEnabled:
            return
        currentTime = getServerUTCTime()
        if currentTime < config.startTime or config.endTime < currentTime:
            return
        if not self.getIsIntroSeen(tournamentType):
            return IngameTournamentState.INTRO
        else:
            if self.getCurrentShowmatch(tournamentType):
                return IngameTournamentState.IN_PROGRESS
            if self.getNextShowmatch(tournamentType):
                return IngameTournamentState.BETWEEN_SHOWMATCHES
            return IngameTournamentState.FINISHED

    def getCurrentShowmatch(self, tournamentType):
        config = self.__getConfigByTournamentType(tournamentType)
        if config is None or not config.isEnabled:
            return
        currentTime = getServerUTCTime()
        return findFirst((lambda showmatch: showmatch.startTime <= currentTime <= showmatch.endTime), config.showmatches)

    def getNextShowmatch(self, tournamentType):
        config = self.__getConfigByTournamentType(tournamentType)
        if config is None or not config.isEnabled:
            return
        currentTime = getServerUTCTime()
        upcomingShowmatches = [showmatch for showmatch in config.showmatches if currentTime < showmatch.startTime]
        upcomingShowmatches.sort(key=(lambda showmatch: showmatch.startTime))
        return first(upcomingShowmatches)

    def getTournamentShowmatchPeriod(self, tournamentType):
        config = self.__getConfigByTournamentType(tournamentType)
        if config is None or not config.isEnabled:
            return (None, None)
        start = min([showmatch.startTime for showmatch in config.showmatches])
        end = max([showmatch.endTime for showmatch in config.showmatches])
        return (start, end)

    def getIsIntroSeen(self, tournamentType):
        settings = AccountSettings.getUIFlag(INGAME_TOURNAMENT_SECTION)
        if tournamentType == IngameTournamentType.WCI:
            return settings.get(INGAME_TOURNAMENT_WCI_INTRO_SEEN, False)
        if tournamentType == IngameTournamentType.OLS:
            return settings.get(INGAME_TOURNAMENT_OLS_INTRO_SEEN, False)
        return False

    def setIsIntroSeen(self, tournamentType):
        settings = AccountSettings.getUIFlag(INGAME_TOURNAMENT_SECTION)
        if tournamentType == IngameTournamentType.WCI:
            settings[INGAME_TOURNAMENT_WCI_INTRO_SEEN] = True
        if tournamentType == IngameTournamentType.OLS:
            settings[INGAME_TOURNAMENT_OLS_INTRO_SEEN] = True
        AccountSettings.setUIFlag(INGAME_TOURNAMENT_SECTION, settings)
        return

    @adisp_process
    def requestTournamentWGCGData(self):
        res = yield self.__webCtrl.sendRequest(IngameTournamentGetDataCtx())
        self.onTournamentWGCGDataUpdated(_IngameTournamentData.fromRequestResponse(res))
        return

    def getTokenStoreOpeningTime(self, tournamentType):
        config = self.__getConfigByTournamentType(tournamentType)
        if config:
            return config.tokenStoreOpeningTime
        return 0

    def getOfferGiftsToken(self, tournamentType):
        config = self.__getConfigByTournamentType(tournamentType)
        if config:
            return config.offerGiftsToken
        return b''

    def openOfferGifts(self, tournamentType, overrideOnBackCallback=None):
        tokenStoreToken = self.getOfferGiftsToken(tournamentType)
        if not tokenStoreToken:
            _logger.warning(b'offerGiftsToken is not defined in tournament config')
            return
        else:
            currentTime = getServerUTCTime()
            config = self.__getConfigByTournamentType(tournamentType)
            if currentTime < config.tokenStoreOpeningTime:
                _logger.warning(b'Token Store is not available yet')
                return
            offer = self.__offersProvider.getOfferByToken(tokenStoreToken)
            offerID = offer.id if offer else None
            if not offerID:
                _logger.warning(b'Could not find offer for token %s', tokenStoreToken)
                return
            showOfferGiftsWindow(offerID=offerID, overrideOnBackCallback=overrideOnBackCallback)
            return

    @adisp_process
    def openShop(self, tournamentType):
        config = self.__getConfigByTournamentType(tournamentType)
        shopConfigs = config.shop if config else []
        realmConfig = findFirst((lambda config: CURRENT_REALM in config.realms), shopConfigs)
        if realmConfig is not None:
            if realmConfig.ingameShopRelativePath:
                url = (b'{}{}').format(getShopURL(), realmConfig.ingameShopRelativePath)
                showIngameShop(url)
            elif realmConfig.shopUrl:
                parsedUrl = yield URLMacros().parse(realmConfig.shopUrl)
                g_eventBus.handleEvent(events.OpenLinkEvent(events.OpenLinkEvent.SPECIFIED, url=parsedUrl))
            else:
                _logger.warning(b'None from ingameShopRelativePath or shorUrl are specified')
        else:
            _logger.warning(b'Could not open Ingame Tournament shop')
        return

    def __onPrbDispatcherCreated(self):
        g_playerEvents.onPrbDispatcherCreated -= self.__onPrbDispatcherCreated
        self.startGlobalListening()
        self.__updateTournamentEntryPoint()
        return

    def __onServerSettingsChanged(self, serverSettings):
        if self.__serverSettings is not None:
            self.__serverSettings.onServerSettingsChange -= self.__onConfigUpdated
        self.__serverSettings = serverSettings
        self.__serverSettings.onServerSettingsChange += self.__onConfigUpdated
        return

    def __onConfigUpdated(self, serverSettingsDiff):
        if Configs.INGAME_TOURNAMENT_CONFIG.value in serverSettingsDiff:
            self.__updateTournamentEntryPoint()
        return

    def __updateTournamentEntryPoint(self):
        self.__callbackDelayer.clearCallbacks()
        nextTimestamp = self.__getNextUpdateTimestamp()
        if nextTimestamp is not None:
            delay = nextTimestamp - getServerUTCTime()
            if delay > 0:
                self.__callbackDelayer.delayCallback(delay, self.__updateTournamentEntryPoint)
        for tournamentType in IngameTournamentType:
            isAvailable = self.isTournamentAvailable(tournamentType)
            if self.__availabilityByTournamentType.get(tournamentType) != isAvailable:
                self.__availabilityByTournamentType[tournamentType] = isAvailable
                self.__eventsService.updateEntries()

        self.onTournamentEntryPointUpdated()
        return

    def __getNextUpdateTimestamp(self):
        timers = []
        for showmatch in (
         self.getCurrentShowmatch(IngameTournamentType.WCI),
         self.getCurrentShowmatch(IngameTournamentType.OLS)):
            if showmatch is not None:
                timers.append(showmatch.endTime)

        for showmatch in (self.getNextShowmatch(IngameTournamentType.WCI),
         self.getNextShowmatch(IngameTournamentType.OLS)):
            if showmatch is not None:
                timers.append(showmatch.startTime)

        if timers:
            return min(timers)
        else:
            return

    def __getConfig(self):
        if self.__serverSettings is not None:
            return self.__serverSettings.ingameTournamentConfig
        else:
            return

    def __getConfigByTournamentType(self, tournamentType):
        config = self.__getConfig()
        if config is not None:
            return getattr(config, tournamentType.value, None)
        else:
            return
