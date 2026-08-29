from web.web_client_api import w2c, w2capi, W2CSchema
from gui.shared import g_eventBus
from gui.shared.events import SurveyEvent

@w2capi(name=b'survey', key=b'action')
class SurveyWebApi(object):

    @w2c(W2CSchema, name=b'finish_survey')
    def finishSurvey(self, _):
        g_eventBus.handleEvent(SurveyEvent(SurveyEvent.SURVEY_FINISHED))
        return
