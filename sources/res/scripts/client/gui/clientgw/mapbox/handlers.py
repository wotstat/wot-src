from gui.clientgw.base.handlers import RequestHandlers
from gui.clientgw.settings import WebRequestDataType

class MapboxRequestHandlers(RequestHandlers):

    def get(self):
        handlers = {(WebRequestDataType.MAPBOX_PROGRESSION): (self.__getMapboxProgression), 
           (WebRequestDataType.MAPBOX_CREWBOOK): (self.__selectCrewbook), 
           (WebRequestDataType.MAPBOX_SURVEY_COMPLETE): (self.__completeSurvey), 
           (WebRequestDataType.MAPBOX_SURVEY_URL): (self.__requestAuthorizedSurveyURL)}
        return handlers

    def __getMapboxProgression(self, ctx, callback):
        return self._requester.doRequestEx(ctx, callback, (b'mapbox', b'get_mapbox_progression'))

    def __selectCrewbook(self, ctx, callback):
        return self._requester.doRequestEx(ctx, callback, (b'mapbox', b'select_mapbox_crewbook'), ctx.getItemID)

    def __completeSurvey(self, ctx, callback):
        return self._requester.doRequestEx(ctx, callback, (b'mapbox', b'complete_survey'), ctx.getSurveyData())

    def __requestAuthorizedSurveyURL(self, ctx, callback):
        return self._requester.doRequestEx(ctx, callback, (b'mapbox', b'request_authorized_survey_url'), ctx.getMapURL())
