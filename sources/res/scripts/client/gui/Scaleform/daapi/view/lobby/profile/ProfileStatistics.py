from collections import namedtuple
from debug_utils import LOG_ERROR
from stats_params import BATTLE_ROYALE_STATS_ENABLED
from gui.Scaleform.daapi.view.lobby.profile.profile_statistics_vos import getStatisticsVO
from gui.Scaleform.daapi.view.meta.ProfileStatisticsMeta import ProfileStatisticsMeta
from gui.Scaleform.genConsts.BATTLE_TYPES import BATTLE_TYPES
from gui.Scaleform.genConsts.PROFILE_DROPDOWN_KEYS import PROFILE_DROPDOWN_KEYS
from gui.impl import backport
from gui.impl.gen import R
from gui.ranked_battles.constants import RankedDossierKeys, ARCHIVE_SEASON_ID
from gui.shared.formatters import text_styles
from helpers import dependency
from skeletons.gui.game_control import IRankedBattlesController
from skeletons.gui.lobby_context import ILobbyContext
from gui.shared.event_bus import EVENT_BUS_SCOPE
from gui.shared.events import ProfileStatisticEvent
from gui.shared import g_eventBus
from gui.Scaleform.daapi.view.lobby.comp7.comp7_profile_helper import COMP7_ARCHIVE_NAMES, COMP7_SEASON_NUMBERS, isComp7Archive, isComp7Season, getDropdownKeyByArchiveName, getDropdownKeyBySeason
_RankedSeasonsKeys = namedtuple(b'_RankedSeasonsKeys', [b'all', b'current', b'previous'])
_RANKED_SEASONS_ARCHIVE = b'archive'
RANKED_SEASONS_ARCHIVE_10x10 = b'_10x10'
_FRAME_LABELS = {(PROFILE_DROPDOWN_KEYS.ALL): b'random', 
   (PROFILE_DROPDOWN_KEYS.EPIC_RANDOM): b'epicRandom', 
   (PROFILE_DROPDOWN_KEYS.FALLOUT): b'fallout', 
   (PROFILE_DROPDOWN_KEYS.HISTORICAL): b'historical', 
   (PROFILE_DROPDOWN_KEYS.TEAM): b'team7x7', 
   (PROFILE_DROPDOWN_KEYS.STATICTEAM): b'team7x7', 
   (PROFILE_DROPDOWN_KEYS.CLAN): b'clan', 
   (PROFILE_DROPDOWN_KEYS.FORTIFICATIONS): b'fortifications', 
   (PROFILE_DROPDOWN_KEYS.STATICTEAM_SEASON): b'team7x7', 
   (PROFILE_DROPDOWN_KEYS.RANKED): b'ranked_15x15', 
   (PROFILE_DROPDOWN_KEYS.RANKED_10X10): (BATTLE_TYPES.RANKED_10X10), 
   (PROFILE_DROPDOWN_KEYS.BATTLE_ROYALE_SOLO): b'battle_royale', 
   (PROFILE_DROPDOWN_KEYS.BATTLE_ROYALE_SQUAD): b'battle_royale', 
   (PROFILE_DROPDOWN_KEYS.VERSUS_AI): b'versusAI'}
_COMP7_FRAME_LABEL = b'comp7'

def _packProviderType(mainType, addValue=None):
    if addValue is not None:
        return b'%s/%s' % (mainType, str(addValue))
    else:
        return mainType


def _parseProviderType(value):
    return value.split(b'/')


class ProfileStatistics(ProfileStatisticsMeta):
    lobbyContext = dependency.descriptor(ILobbyContext)
    __rankedController = dependency.descriptor(IRankedBattlesController)

    def __init__(self, *args):
        try:
            _, _, _, self.__ctx = args
        except Exception:
            LOG_ERROR(b'There is error while parsing profile stats page arguments', args)
            self.__ctx = {}

        super(ProfileStatistics, self).__init__(*args)
        self.__seasonsManagers = self.__initSeasonsManagers()
        return

    def setSeason(self, seasonId):
        if self.__getSeasonsManager().setSeason(seasonId):
            self.as_updatePlayerStatsBtnS(self.__getSeasonsManager().getPlayersStatsBtnEnabled())
            self.invokeUpdate()
        return

    def onCompletedSeasonsInfoChanged(self):
        self._setInitData()
        return

    def _populate(self):
        event = ProfileStatisticEvent(ProfileStatisticEvent.SELECT_BATTLE_TYPE)
        if self._selectedData and isinstance(self._selectedData, dict):
            event.ctx[b'eventOwner'] = self._selectedData.get(b'eventOwner')
        else:
            event.ctx[b'eventOwner'] = b'achievements'
        g_eventBus.handleEvent(event, scope=EVENT_BUS_SCOPE.LOBBY)
        self._battlesType = event.ctx.get(b'battlesType', self._battlesType)
        super(ProfileStatistics, self)._populate()
        self._setInitData()
        return

    def _dispose(self):
        super(ProfileStatistics, self)._dispose()
        g_eventBus.handleEvent(ProfileStatisticEvent(ProfileStatisticEvent.DISPOSE), scope=EVENT_BUS_SCOPE.LOBBY)
        self.__clearSeasonsManagers()
        return

    def _setInitData(self, accountDossier=None):
        dropDownProvider = [
         self._dataProviderEntryAutoTranslate(PROFILE_DROPDOWN_KEYS.ALL),
         self._dataProviderEntryAutoTranslate(PROFILE_DROPDOWN_KEYS.EPIC_RANDOM)]
        if BATTLE_ROYALE_STATS_ENABLED:
            dropDownProvider += [
             self._dataProviderEntryAutoTranslate(PROFILE_DROPDOWN_KEYS.BATTLE_ROYALE_SOLO),
             self._dataProviderEntryAutoTranslate(PROFILE_DROPDOWN_KEYS.BATTLE_ROYALE_SQUAD)]
        dropDownProvider += [
         self._dataProviderEntryAutoTranslate(PROFILE_DROPDOWN_KEYS.RANKED),
         self._dataProviderEntryAutoTranslate(PROFILE_DROPDOWN_KEYS.RANKED_10X10),
         self._dataProviderEntryAutoTranslate(PROFILE_DROPDOWN_KEYS.FALLOUT)]
        if accountDossier is not None and accountDossier.getHistoricalStats().getVehicles():
            dropDownProvider.append(self._dataProviderEntryAutoTranslate(PROFILE_DROPDOWN_KEYS.HISTORICAL))
        dropDownProvider.append(self._dataProviderEntryAutoTranslate(PROFILE_DROPDOWN_KEYS.TEAM))
        if accountDossier is not None and accountDossier.getRated7x7Stats().getVehicles():
            dropDownProvider.append(self._dataProviderEntryAutoTranslate(PROFILE_DROPDOWN_KEYS.STATICTEAM))
        dropDownProvider.append(self._dataProviderEntryAutoTranslate(PROFILE_DROPDOWN_KEYS.CLAN))
        if self.lobbyContext.getServerSettings().isStrongholdsEnabled():
            dropDownProvider.append(self._dataProviderEntryAutoTranslate(PROFILE_DROPDOWN_KEYS.FORTIFICATIONS))
        for archive in COMP7_ARCHIVE_NAMES:
            dropDownProvider.append(self._dataProviderEntryAutoTranslate(getDropdownKeyByArchiveName(archive)))

        dropDownProvider += [
         self._dataProviderEntryAutoTranslate(PROFILE_DROPDOWN_KEYS.VERSUS_AI)]
        for season in COMP7_SEASON_NUMBERS:
            dropDownProvider.append(self._dataProviderEntryAutoTranslate(getDropdownKeyBySeason(season)))

        self.as_setInitDataS({b'dropDownProvider': dropDownProvider})
        return

    def _sendAccountData(self, targetData, accountDossier):
        super(ProfileStatistics, self)._sendAccountData(targetData, accountDossier)
        self._setInitData(accountDossier)
        vo = getStatisticsVO(battlesType=self._battlesType, targetData=targetData, accountDossier=accountDossier, isCurrentUser=self._userID is None)
        if self._battlesType == PROFILE_DROPDOWN_KEYS.TEAM:
            vo[b'showSeasonDropdown'] = False
        elif self._battlesType == PROFILE_DROPDOWN_KEYS.STATICTEAM or self._battlesType == PROFILE_DROPDOWN_KEYS.STATICTEAM_SEASON:
            self._battlesType = PROFILE_DROPDOWN_KEYS.STATICTEAM
            vo[b'headerText'] = backport.text(R.strings.profile.section.statistics.headerText.staticTeam())
            vo[b'dropdownSeasonLabel'] = text_styles.main(backport.text(R.strings.cyberSport.StaticFormationStatsView.seasonFilter()))
            self.__updateStaticDropdownData(vo)
        elif self._battlesType in (PROFILE_DROPDOWN_KEYS.RANKED, PROFILE_DROPDOWN_KEYS.RANKED_10X10):
            vo[b'seasonDropdownAttachToTitle'] = True
            vo[b'playersStatsLbl'] = backport.text(R.strings.ranked_battles.statistic.playersRaiting())
        self.__getSeasonsManager().addSeasonsDropdown(vo)
        if isComp7Season(self._battlesType) or isComp7Archive(self._battlesType):
            frameLabel = _COMP7_FRAME_LABEL
        else:
            frameLabel = _FRAME_LABELS[self._battlesType]
        self.as_responseDossierS(self._battlesType, vo, frameLabel, b'')
        return

    def _receiveFortDossier(self, accountDossier):
        return accountDossier.getFortSortiesStats()

    def _getNecessaryStats(self, accountDossier=None):
        if accountDossier is None:
            accountDossier = self.itemsCache.items.getAccountDossier(self._userID)
        seasonStats = self.__getSeasonsManager().getStats(accountDossier)
        if seasonStats:
            return seasonStats
        else:
            if self._battlesType == PROFILE_DROPDOWN_KEYS.RANKED:
                return accountDossier.getSeasonRanked15x15Stats(RankedDossierKeys.ARCHIVE, ARCHIVE_SEASON_ID)
            return super(ProfileStatistics, self)._getNecessaryStats(accountDossier)

    def __initSeasonsManagers(self):
        return {b'default': (_BaseSeasonManager()), 
           (PROFILE_DROPDOWN_KEYS.RANKED_10X10): (_RankedSeasonsManager(self._dataProviderEntry))}

    def __getSeasonsManager(self):
        if self._battlesType in self.__seasonsManagers:
            return self.__seasonsManagers[self._battlesType]
        return self.__seasonsManagers[b'default']

    def __clearSeasonsManagers(self):
        for manager in self.__seasonsManagers.values():
            manager.clear()

        self.__seasonsManagers = {}
        return

    @classmethod
    def __updateStaticDropdownData(cls, vo):
        vo[b'showSeasonDropdown'] = True
        vo[b'seasonItems'] = [
         cls._dataProviderEntry(PROFILE_DROPDOWN_KEYS.STATICTEAM, backport.text(R.strings.profile.profile.seasonsdropdown.all()))]
        vo[b'seasonIndex'] = 0
        vo[b'seasonEnabled'] = False
        return


class _BaseSeasonManager(object):

    def __init__(self, entryFactory=None):
        self._entryFactory = entryFactory
        self._seasonKey = None
        return

    def clear(self):
        self._entryFactory = None
        return

    def setSeason(self, seasonId):
        if self._seasonKey == seasonId:
            return False
        self._seasonKey = seasonId
        return True

    def addSeasonsDropdown(self, targetVO):
        return

    def getPlayersStatsBtnEnabled(self):
        return False

    def getStats(self, accountDossier):
        return


class _RankedSeasonsManager(_BaseSeasonManager):
    __rankedController = dependency.descriptor(IRankedBattlesController)

    def addSeasonsDropdown(self, targetVO):
        targetVO[b'showSeasonDropdown'] = False
        targetVO[b'playersStats'] = False
        return

    def getStats(self, accountDossier):
        return accountDossier.getSeasonRankedStats(RANKED_SEASONS_ARCHIVE_10x10, 0)
