from gui.clientgw.base.handlers import RequestHandlers
from gui.clientgw.settings import WebRequestDataType

class UILoggingRequestHandlers(RequestHandlers):

    def get(self):
        return {(WebRequestDataType.UI_LOGGING_SESSION): (self.__getSession)}

    def __getSession(self, ctx, callback):
        return self._requester.doRequestEx(ctx, callback, (b'uilogging', b'get_uilogging_session'))
