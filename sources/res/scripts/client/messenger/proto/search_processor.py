import weakref, BigWorld
from interfaces import ISearchHandler, ISearchProcessor
from debug_utils import LOG_DEBUG, LOG_ERROR
from soft_exception import SoftException

class SearchProcessor(ISearchProcessor):

    def __init__(self):
        super(SearchProcessor, self).__init__()
        self._handlers = set()
        self._lastRequestID = None
        return

    def __del__(self):
        LOG_DEBUG(b'SearchProcessor deleted:', self)
        return

    def init(self):
        return

    def fini(self):
        self._lastRequestID = None
        self._handlers.clear()
        return

    def addHandler(self, handler):
        if isinstance(handler, ISearchHandler):
            self._handlers.add(weakref.ref(handler))
        else:
            raise SoftException(b'Handler must implement ISearchHandler')
        return

    def removeHandler(self, handler):
        handlerRef = weakref.ref(handler)
        if handlerRef in self._handlers:
            self._handlers.remove(handlerRef)
        return

    def find(self, token, **kwargs):
        raise NotImplementedError(b'Routine SearchProcessor.find must be implemented')
        return

    def getSearchResultLimit(self):
        raise NotImplementedError(b'Routine SearchProcessor.getSearchResultLimit must be implemented')
        return

    def getSearchCoolDown(self):
        raise NotImplementedError(b'Routine SearchProcessor.getSearchCoolDown must be implemented')
        return

    def _makeRequestID(self):
        return BigWorld.player().acquireRequestID()

    def _invokeHandlerMethod(self, methodName, *args):
        for handlerRef in self._handlers.copy():
            handler = handlerRef()
            if handler:
                method = getattr(handler, methodName, None)
                if method and callable(method):
                    method(*args)
                else:
                    LOG_ERROR(b'Method is not found', handler, methodName)

        return

    def _onSearchTokenComplete(self, requestID, result):
        if self._lastRequestID != requestID:
            return
        self._invokeHandlerMethod(b'onSearchComplete', result)
        return

    def _onSearchFailed(self, reason):
        self._invokeHandlerMethod(b'onSearchFailed', reason)
        return

    def _onExcludeFromSearch(self, entity):
        self._invokeHandlerMethod(b'onExcludeFromSearch', entity)
        return
