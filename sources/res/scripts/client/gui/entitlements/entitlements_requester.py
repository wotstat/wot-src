import copy, logging, typing
from adisp import adisp_process, adisp_async
from gui.clientgw.agate.contexts import AgateGetInventoryEntitlementsCtx
from helpers import dependency
from helpers.CallbackDelayer import CallbackDelayer
from skeletons.gui.web import IWebController
if typing.TYPE_CHECKING:
    from typing import List, Optional
_logger = logging.getLogger(__name__)

class EntitlementsRequester(object):

    def __init__(self):
        self.__requests = []
        return

    def clear(self):
        for request in self.__requests:
            request.clear()

        self.__requests = []
        return

    @adisp_async
    def requestByCodes(self, codes, retryTimes=None, callback=None):
        ctx = AgateGetInventoryEntitlementsCtx(AgateGetInventoryEntitlementsCtx.createFilterByCodes(codes))
        existingRequest = self.__findRequest(ctx)
        if existingRequest:
            existingRequest.addCallback(callback)
        else:
            request = _EntitlementsRequest(ctx, callback, retryTimes, self.__onRequestDone)
            self.__requests.append(request)
            request.send()
        return

    def __onRequestDone(self, ctx):
        request = self.__findRequest(ctx)
        if not request:
            return
        request.clear()
        self.__requests.remove(request)
        return

    def __findRequest(self, ctx):
        for request in self.__requests:
            if request.hasSameContext(ctx):
                return request

        return


class _EntitlementsRequest(object):
    __DEFAULT_RETRY_TIMES = [
     0, 1, 2, 3, 4]
    __web = dependency.descriptor(IWebController)

    def __init__(self, ctx, callback, retryTimes, finishedCallback):
        self.__ctx = ctx
        self.__retryTimes = copy.copy(self.__DEFAULT_RETRY_TIMES) if retryTimes is None else retryTimes
        self.__callbacks = [callback]
        self.__onFinished = finishedCallback
        self.__delayer = None
        return

    def clear(self):
        self.__clear()
        return

    def hasSameContext(self, ctx):
        return self.__ctx.getRequestType() == ctx.getRequestType() and ctx.getEntitlementsFilter() == self.__ctx.getEntitlementsFilter()

    def addCallback(self, callback):
        self.__callbacks.append(callback)
        return

    @adisp_process
    def send(self):
        _logger.debug(b'Sending request entitlements request: %r, retry times left: %r', self.__ctx.getRequestType(), self.__retryTimes)
        response = yield self.__web.sendRequest(ctx=self.__ctx)
        if response.isSuccess():
            result = self.__formatResult(response.data)
            self.__sendResult(True, result)
        else:
            retryTime = self.__getNextRetryTime()
            if retryTime:
                self.__getDelayer().delayCallback(retryTime, self.send)
            else:
                self.__sendResult(False, {})
        return

    def __getDelayer(self):
        if self.__delayer is None:
            self.__delayer = CallbackDelayer()
        return self.__delayer

    def __sendResult(self, isSuccess, result):
        for callback in self.__callbacks:
            callback((isSuccess, result))

        self.__onFinished(self.__ctx)
        return

    def __getNextRetryTime(self):
        if self.__retryTimes:
            return self.__retryTimes.pop(0)
        return 0

    def __clear(self):
        self.__ctx = None
        self.__retryTimes = []
        self.__callbacks = []
        if self.__delayer:
            self.__delayer.destroy()
            self.__delayer = None
        return

    @staticmethod
    def __formatResult(result):
        balance = result.get(b'balance', [])
        return {entInfo[b'code']: entInfo for entInfo in balance}
