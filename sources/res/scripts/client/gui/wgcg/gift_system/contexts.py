import logging, time, typing
from gui.gift_system.wrappers import GiftsWebState, SendGiftResponse
from gui.wgcg.base.contexts import CommonWebRequestCtx
from gui.wgcg.settings import WebRequestDataType
from shared_utils import makeTupleByDict
_logger = logging.getLogger(__name__)

def _packEventWebState(eventData):
    if eventData is None or not isinstance(eventData, dict):
        return
    try:
        result = {b'sendLimit': (eventData[b'send_limit']), 
           b'expireTime': (eventData[b'expiration_time']), 
           b'expireDelta': (eventData[b'expiration_delta']), 
           b'executionTime': (eventData[b'execution_time']), 
           b'state': (eventData[b'state'])}
        result = makeTupleByDict(GiftsWebState, result)
    except (KeyError, TypeError):
        _logger.exception(b'Can not _packEventWebState because of invalid eventData')
        result = None

    return result


class GiftSystemStateCtx(CommonWebRequestCtx):

    def __init__(self, reqEventIds, waitingID=b''):
        super(GiftSystemStateCtx, self).__init__(waitingID)
        self.__reqEventIds = reqEventIds
        return

    def isAuthorizationRequired(self):
        return True

    def isClanSyncRequired(self):
        return False

    def isCaching(self):
        return False

    def getRequestType(self):
        return WebRequestDataType.GIFT_SYSTEM_STATE

    def getReqEventIds(self):
        return self.__reqEventIds

    def getDataObj(self, incomeData):
        if incomeData is None or not isinstance(incomeData, dict):
            return self.getDefDataObj()
        else:
            return {eventID: _packEventWebState(incomeData.get(str(eventID))) for eventID in self.__reqEventIds}

    def getDefDataObj(self):
        return {eventID: None for eventID in self.__reqEventIds}


class GiftSystemSendGiftCtx(CommonWebRequestCtx):

    def __init__(self, entitlementCode, receiverID=0, metaInfo=None, waitingID=b''):
        super(GiftSystemSendGiftCtx, self).__init__(waitingID)
        self.__entitlementCode = entitlementCode
        self.__metaInfo = metaInfo or {}
        self.__receiverID = receiverID
        return

    def isAuthorizationRequired(self):
        return True

    def isClanSyncRequired(self):
        return False

    def isCaching(self):
        return False

    def getRequestType(self):
        return WebRequestDataType.GIFT_SYSTEM_POST_GIFT

    def getEntitlementCode(self):
        return self.__entitlementCode

    def getMetaInfo(self):
        return self.__metaInfo

    def getReceiverID(self):
        return self.__receiverID

    def getDataObj(self, state, incomeData=None):
        resultData = self.getDefDataObj(state)
        if incomeData is not None and isinstance(incomeData, dict):
            resultData[b'outCount'] = incomeData.get(b'outcoming', resultData[b'outCount'])
            resultData[b'executionTime'] = incomeData.get(b'execution_time', resultData[b'executionTime'])
        return makeTupleByDict(SendGiftResponse, resultData)

    def getDefDataObj(self, state):
        return {b'state': state, 
           b'outCount': None, 
           b'meta': (self.__metaInfo), 
           b'receiverID': (self.__receiverID), 
           b'entitlementCode': (self.__entitlementCode), 
           b'executionTime': (int(time.time()))}
