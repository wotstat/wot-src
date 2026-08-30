from __future__ import absolute_import
from debug_utils import LOG_ERROR
from gui.Scaleform.daapi.view.lobby.profile.ProfileSection import BattleTypesDropDownItems
from gui.Scaleform.daapi.view.lobby.profile.profile_statistics_vos import getStatisticsVO
from gui.Scaleform.daapi.view.lobby.profile.seasons_manager import makeStatisticsSeasonManagers
from gui.Scaleform.daapi.view.meta.ProfileStatisticsMeta import ProfileStatisticsMeta
from gui.Scaleform.genConsts.BATTLE_TYPES import BATTLE_TYPES
from gui.Scaleform.genConsts.PROFILE_DROPDOWN_KEYS import PROFILE_DROPDOWN_KEYS
from gui.Scaleform.genConsts.RANKEDBATTLES_CONSTS import RANKEDBATTLES_CONSTS
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
   (PROFILE_DROPDOWN_KEYS.BATTLE_ROYALE_SQUAD): b'battle_royale'}

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
        self._seasonsManagers = makeStatisticsSeasonManagers()
        return

    def setSeason(self, seasonId):
        if self._seasonsManagers.setSeason(seasonId):
            self.as_updatePlayerStatsBtnS(self._seasonsManagers.getPlayersStatsBtnEnabled())
            self.invokeUpdate()
        return

    def showPlayersStats(self):
        self.__rankedController.showRankedBattlePage(ctx={b'selectedItemID': (RANKEDBATTLES_CONSTS.RANKED_BATTLES_RATING_ID), 
           b'clientParams': {b'spaID': (self._databaseID)}})
        return

    def onCompletedSeasonsInfoChanged(self):
        self._setInitData()
        return

    def requestDossier(self, bType):
        self._seasonsManagers.onBattleTypeSwitched(bType)
        super(ProfileStatistics, self).requestDossier(bType)
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
        self._seasonsManagers.clear()
        return

    def _setInitData(self, accountDossier=None):
        self.as_setInitDataS({b'dropDownProvider': (self._makeBattleTypesDropDown(accountDossier))})
        return

    def _sendAccountData(self, targetData, accountDossier):
        super(ProfileStatistics, self)._sendAccountData(targetData, accountDossier)
        self._setInitData(accountDossier)
        self._setStatisticsVO(targetData, accountDossier)
        return

    def _setStatisticsVO(self, targetData, accountDossier):
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
        self._seasonsManagers.addSeasonsDropdown(vo)
        frameLabel = _FRAME_LABELS[self._battlesType]
        self.as_responseDossierS(self._battlesType, vo, frameLabel, b'')
        return

    def _receiveFortDossier(self, accountDossier):
        return accountDossier.getFortSortiesStats()

    def _getNecessaryStats(self, accountDossier=None):
        if accountDossier is None:
            accountDossier = self.itemsCache.items.getAccountDossier(self._userID)
        seasonStats = self._seasonsManagers.getStats(accountDossier)
        if seasonStats:
            return seasonStats
        else:
            if self._battlesType == PROFILE_DROPDOWN_KEYS.RANKED:
                return accountDossier.getSeasonRanked15x15Stats(RankedDossierKeys.ARCHIVE, ARCHIVE_SEASON_ID)
            return super(ProfileStatistics, self)._getNecessaryStats(accountDossier)

    @classmethod
    def __updateStaticDropdownData(cls, vo):
        vo[b'showSeasonDropdown'] = True
        seasonItems = BattleTypesDropDownItems()
        seasonItems.addWithKeyAndLabel(PROFILE_DROPDOWN_KEYS.STATICTEAM, backport.text(R.strings.profile.profile.seasonsdropdown.all()))
        vo[b'seasonItems'] = seasonItems
        vo[b'seasonIndex'] = 0
        vo[b'seasonEnabled'] = False
        return
