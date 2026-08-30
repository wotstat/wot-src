from helpers import dependency
from skeletons.gui.game_control import IEpicBattleMetaGameController
from web.web_client_api import w2c, w2capi, W2CSchema

@w2capi(name=b'frontline', key=b'action')
class FrontLineWebApi(W2CSchema):
    __epicController = dependency.descriptor(IEpicBattleMetaGameController)

    @w2c(W2CSchema, name=b'get_player_discount')
    def handleGetPlayerDiscount(self, _):
        return self.__epicController.getStoredEpicDiscount()

    @w2c(W2CSchema, name=b'get_calendar_info')
    def handleGetCalendarInfo(self, _):
        calendarData = dict()
        seasons = (
         self.__epicController.getCurrentSeason(),
         self.__epicController.getNextSeason(),
         self.__epicController.getPreviousSeason())
        for season in seasons:
            if season is not None:
                calendarData[b'season'] = {b'id': (season.getSeasonID()), b'start': (season.getStartDate()), 
                   b'end': (season.getEndDate())}
                calendarData[b'cycles'] = [{b'id': (cycle.ID), b'start': (cycle.startDate), b'end': (cycle.endDate), b'announce_only': (cycle.announceOnly)} for cycle in season.getAllCycles().values()]
                break

        return calendarData
