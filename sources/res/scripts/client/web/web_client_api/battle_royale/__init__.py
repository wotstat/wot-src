from collections import namedtuple
from web.web_client_api import webApiCollection
from web.web_client_api.request import RequestWebApi
from web.web_client_api.sound import SoundWebApi, SoundStateWebApi, HangarSoundWebApi
from web.web_client_api.ui import NotificationWebApi, OpenWindowWebApi
from web.web_client_api.ui import CloseWindowWebApi, OpenTabWebApi, ContextMenuWebApi, UtilWebApi
from web.web_client_api.quests import QuestsWebApi
from web.web_client_api.shop import ShopWebApi
from web.web_client_api.vehicles import VehiclesWebApi
from web.web_client_api import w2capi, W2CSchema, w2c
from helpers import dependency, time_utils
from skeletons.gui.game_control import IBattleRoyaleController
from skeletons.gui.shared import IItemsCache
from web.web_client_api.frontline import FrontLineWebApi
BattleRoyaleSeasonAchievements = namedtuple(b'BattleRoyaleSeasonAchievements', (b'season_id', b'episode_id', b'battle_count', b'kill_count', b'top1'))

def createBattleRoyaleWebHanlders():
    return webApiCollection(FrontLineWebApi, BattleRoyaleWebApi, VehiclesWebApi, RequestWebApi, ShopWebApi, OpenWindowWebApi, CloseWindowWebApi, OpenTabWebApi, NotificationWebApi, ContextMenuWebApi, UtilWebApi, SoundWebApi, SoundStateWebApi, HangarSoundWebApi, QuestsWebApi)


@w2capi(name=b'battle_royale', key=b'action')
class BattleRoyaleWebApi(W2CSchema):
    __battleRoyale = dependency.descriptor(IBattleRoyaleController)
    __itemsCache = dependency.descriptor(IItemsCache)

    @w2c(W2CSchema, name=b'get_calendar_info')
    def handleGetCalendarInfo(self, _):
        calendarData = dict()
        for season in self.__getSeasons():
            if season is not None:
                calendarData[b'season'] = {b'id': (season.getSeasonID()), b'start': (season.getStartDate()), 
                   b'end': (season.getEndDate())}
                calendarData[b'cycles'] = [{b'id': (cycle.ID), b'start': (cycle.startDate), b'end': (cycle.endDate), b'announce_only': (cycle.announceOnly)} for cycle in season.getAllCycles().values()]

        return calendarData

    @w2c(W2CSchema, name=b'get_seasons_achievements')
    def getSeasonAchievements(self, _):
        dossierDescr = self.__itemsCache.items.getAccountDossier().getDossierDescr()
        seasonsAchievements = self.__getSeasonAchievements(dossierDescr.expand(b'battleRoyaleSeasons'), BattleRoyaleSeasonAchievements)
        currentSeason = self.__battleRoyale.getCurrentSeason()
        if currentSeason and currentSeason.getCycleID():
            now = time_utils.getCurrentLocalServerTimestamp()
            stats = self.__battleRoyale.getStats()
            seasonsAchievements[(currentSeason.getSeasonID(), currentSeason.getCycleID())] = {b'battle_count': (stats.battleCount), 
               b'kill_count': (stats.killCount), 
               b'top1': (stats.topCount), 
               b'season_id': (currentSeason.getSeasonID()), 
               b'episode_id': (currentSeason.getCycleID() or currentSeason.getLastActiveCycleID(now))}
        return seasonsAchievements.values()

    def __getSeasonAchievements(self, achievements, template):
        seasonsAchievements = {}
        for seasonID, cycleID in achievements:
            if not self.__validateSeasonData(seasonID, cycleID):
                continue
            key = (
             seasonID, cycleID)
            seasonsAchievements[key] = template(*(key + achievements[key]))._asdict()

        return seasonsAchievements

    def __validateSeasonData(self, seasonID, cycleID):
        seasons = self.__getSeasons()
        seasonValidationData = {season.getSeasonID(): [cycle.ID for cycle in season.getAllCycles().values()] for season in seasons if season is not None}
        return seasonID in seasonValidationData and cycleID in seasonValidationData.get(seasonID, [])

    def __getSeasons(self):
        return (
         self.__battleRoyale.getCurrentSeason(),
         self.__battleRoyale.getNextSeason(),
         self.__battleRoyale.getPreviousSeason())
