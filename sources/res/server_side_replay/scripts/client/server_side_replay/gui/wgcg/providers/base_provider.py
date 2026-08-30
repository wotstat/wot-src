from __future__ import absolute_import
import logging, time
from collections import defaultdict, namedtuple
from enum import Enum
from typing import Dict, Optional, NamedTuple, Type, TYPE_CHECKING
import BigWorld, Event, ResMgr
from adisp import adisp_process, adisp_async
from data_structures import DictObj
from client_request_lib.requester import Requester as WebRequester
from gui.wgcg.base.contexts import CommonWebRequestCtx
from AccountCommands import CMD_GENERATE_SSR_JWT_TOKEN
from server_side_replay.gui.wgcg.requests import ServerSideReplayRequester, ServerSideReplayRequestsController, ServerSideReplayRequestResponse
from helpers import time_utils, getClientLanguage
if TYPE_CHECKING:
    from typing import DefaultDict, Any
    from shared_utils import CONST_CONTAINER
_logger = logging.getLogger(__name__)

class UpdatePeriodType(Enum):
    BY_TIME = b'BY_TIME'
    AFTER_BATTLE = b'AFTER_BATTLE'
    NONE = b'NONE'


RequestSettings = NamedTuple(b'RequestSettings', [
 (
  b'contextClazz', Type[CommonWebRequestCtx]),
 (
  b'isCached', bool),
 (
  b'updatePeriodType', UpdatePeriodType),
 (
  b'updateKwargs', Optional[Dict])])

class IBaseProvider(object):

    def start(self):
        raise NotImplementedError
        return

    def stop(self, withClear=False):
        raise NotImplementedError
        return


def _webUrlFetcher(url, callback, headers=None, timeout=30.0, method=b'GET', postData=b''):
    return BigWorld.fetchURL(url, callback, headers, timeout, method, postData)


ServerSideReplayServerSettings = namedtuple(b'ServerSideReplayServerSettings', (b'url', b'type'))

class JwtRequestor(object):

    def __init__(self):
        self.__jwtData = None
        self.__waitAnswer = False
        self.__callbacks = []
        return

    @adisp_async
    def requestJwt(self, callback):
        if self.__jwtData and self.__jwtData[b'expirationTime'] > time.time():
            callback(self.__jwtData)
            return
        else:
            self.__callbacks.append(callback)
            if self.__waitAnswer:
                return
            self.__waitAnswer = True

            def cmdCallback(requestID, resultID, errorStr, ext=None):
                self.__jwtData = ext or {}
                for cb in self.__callbacks:
                    cb(ext)

                self.__waitAnswer = False
                self.__callbacks = []
                return

            BigWorld.player()._doCmdNoArgs(CMD_GENERATE_SSR_JWT_TOKEN, cmdCallback)
            return


_g_jwtRequestor = JwtRequestor()

class BaseProvider(IBaseProvider):

    def __init__(self):
        super(BaseProvider, self).__init__()
        self._eManager = Event.EventManager()
        self.onDataReceived = Event.Event(self._eManager)
        self.onDataFailed = Event.Event(self._eManager)
        self.__isStarted = False
        self.__data = defaultdict((lambda : DictObj(isSynced=False, data=None, isWaitingResponse=False, lastUpdate=None)))
        hostUrl = ResMgr.openSection(b'gui/replayer_host_url.xml').readString(b'url')
        settings = ServerSideReplayServerSettings(hostUrl, b'gateway')
        self.__webRequester = WebRequester.create_requester(_webUrlFetcher, settings, client_lang=getClientLanguage())
        self.__requester = ServerSideReplayRequester(self.__webRequester)
        self.__serverSideRequestsController = ServerSideReplayRequestsController(self.__requester)
        return

    def start(self):
        self.__isStarted = True
        return

    def stop(self, withClear=False):
        self.__isStarted = False
        self._eManager.clear()
        for dataName, dataObj in self.__data.items():
            settings = self._getSettingsByDataName(dataName)
            if settings.updatePeriodType is not UpdatePeriodType.BY_TIME:
                dataObj.isSynced = False

        if withClear:
            self.__data.clear()
        return

    @property
    def _isEnabled(self):
        raise NotImplementedError
        return

    @property
    def _dataNameContainer(self):
        raise NotImplementedError
        return

    @property
    def _fakeDataStorage(self):
        return {}

    def _getSettings(self):
        raise NotImplementedError
        return

    def _dataReceived(self, dataName, data):
        self.onDataReceived(dataName, data)
        return

    def _getData(self, dataName, useFake=False, *args, **kwargs):
        dataObj = self.__data[dataName]
        settings = self._getSettingsByDataName(dataName)
        if self.__isRequestingAvailable(settings, dataObj):
            self._requestData(dataName, useFake=useFake, *args, **kwargs)
        return dataObj

    @adisp_process
    def _requestData(self, dataName, useFake=False, *args, **kwargs):
        if not self.__isStarted:
            return
        else:
            if not self._dataNameContainer.hasValue(dataName):
                return
            dataObj = self.__data[dataName]
            settings = self._getSettingsByDataName(dataName)
            if not self._isEnabled or not self.__isRequestingAvailable(settings, dataObj):
                return
            if useFake and dataName not in self._fakeDataStorage:
                _logger.error(b'There are not %s in fake data storage. Check _fakeDataStorage', dataName)
                return
            ctx = settings.contextClazz(*args, **kwargs)
            dataObj.isWaitingResponse = True
            jwtData = yield _g_jwtRequestor.requestJwt()
            if jwtData:
                ctx.jwtToken = jwtData[b'token']
            if not useFake:
                response = yield self._sendRequest(ctx=ctx, allowDelay=True)
            else:
                response = ServerSideReplayRequestResponse(code=0, txtStr=b'', data=self._fakeDataStorage[dataName], extraCode=0, headers={})
            if response.isSuccess():
                formattedData = ctx.getDataObj(response.data)
                isSynced = True
            else:
                formattedData = ctx.getDefDataObj() if dataObj.data is None else dataObj.data
                isSynced = False
                _logger.info(b'Failed to get data: %s. Code: %s', dataName, response.getCode())
            dataObj.isWaitingResponse = False
            dataObj.lastUpdate = time_utils.getServerUTCTime() if isSynced else None
            dataObj.isSynced = isSynced
            dataObj.data = formattedData
            if isSynced:
                self._dataReceived(dataName, formattedData)
            else:
                self.onDataFailed(dataName)
            return

    @adisp_async
    def _sendRequest(self, ctx, callback, allowDelay=None):
        requestsController = self.__serverSideRequestsController

        def _cbWrapper(result):
            _logger.debug(b'Response is received: %s %s', ctx, result)
            callback(result)
            return

        requestsController.request(ctx, callback=_cbWrapper, allowDelay=allowDelay)
        return

    def _getSettingsByDataName(self, dataName):
        return self._getSettings().get(dataName)

    def _updateDataCache(self, dataName, updater):
        dataObj = self.__data[dataName]
        if not dataObj.isSynced or not callable(updater):
            return
        if not updater(dataObj.data):
            return
        self.onDataReceived(dataName, dataObj.data)
        return

    @staticmethod
    def __isRequestingAvailable(settings, dataObj):
        if dataObj.isWaitingResponse:
            return False
        else:
            if settings.updatePeriodType is UpdatePeriodType.AFTER_BATTLE:
                return not dataObj.isSynced
            if settings.updatePeriodType is UpdatePeriodType.BY_TIME:
                if dataObj.lastUpdate is None:
                    return True
                return time_utils.getServerUTCTime() - dataObj.lastUpdate > settings.updateKwargs.get(b'updateTime', 0)
            return True
