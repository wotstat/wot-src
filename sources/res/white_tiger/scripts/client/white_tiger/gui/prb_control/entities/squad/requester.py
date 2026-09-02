from debug_utils import LOG_ERROR
from gui.prb_control import prb_getters
from gui.prb_control.entities.base.unit.requester import UnitRequestProcessor

class WhiteTigerUnitRequestProcessor(UnitRequestProcessor):
    __slots__ = UnitRequestProcessor.__slots__ + (b'__callbacks',)

    def __init__(self, entity):
        super(WhiteTigerUnitRequestProcessor, self).__init__(entity)
        self.__callbacks = {}
        self.__requests = {}
        return

    def fini(self):
        super(WhiteTigerUnitRequestProcessor, self).fini()
        self.__callbacks.clear()
        self.__requests.clear()
        return

    def doRequest(self, ctx, methodName, *args, **kwargs):
        if self._sendRequest(ctx, methodName, [], *args, **kwargs):
            ctx.startProcessing()
        return

    def _sendRequest(self, ctx, methodName, chain, *args, **kwargs):
        unitMgr = prb_getters.getClientUnitMgr()
        result = False
        method = getattr(unitMgr, methodName)
        if callable(method):
            callback = kwargs.pop(b'callback', None)
            requestID = method(*args, **kwargs)
            if requestID > 0:
                self.__requests[requestID] = (
                 ctx, chain)
                if callback:
                    self.__callbacks[requestID] = callback
                result = True
            else:
                LOG_ERROR(b'Request ID can not be null')
        else:
            LOG_ERROR(b'Name of method is invalid', methodName)
        return result

    def _onResponseReceived(self, requestID, result):
        if requestID > 0:
            ctx, chain = self.__requests.pop(requestID, (None, None))
            if ctx is not None:
                if result and chain:
                    self._sendNextRequest(ctx, chain)
                    return
                ctx.stopProcessing(result)
            callback = self.__callbacks.pop(requestID, None)
            if callback and callable(callback):
                callback()
        else:
            while self.__requests:
                _, data = self.__requests.popitem()
                data[0].stopProcessing(False)

        return
