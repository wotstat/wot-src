import logging, time, typing
from gui.gift_system.wrappers import GiftsWebState, SendGiftResponse, GiftsWaitResponse
from gui.clientgw.base.contexts import CommonWebRequestCtx
from gui.clientgw.settings import WebRequestDataType
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
           b'state': (eventData[b'state']), 
           b'common': (eventData.get(b'common', {}))}
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


class GiftSystemBaseSendGiftCtx(CommonWebRequestCtx):

    def __init__(self, entitlementCode, receiverIDs, metaInfo=None, waitingID=b''):
        super(GiftSystemBaseSendGiftCtx, self).__init__(waitingID)
        self.__entitlementCode = entitlementCode
        self.__metaInfo = metaInfo or {}
        self.__receiverIDs = receiverIDs
        return

    def isAuthorizationRequired(self):
        return True

    def isClanSyncRequired(self):
        return False

    def isCaching(self):
        return False

    def getEntitlementCode(self):
        return self.__entitlementCode

    def getMetaInfo(self):
        return self.__metaInfo

    def getReceiverIDs(self):
        return self.__receiverIDs

    def getDataObj(self, state, incomeData=None, code=200):
        resultData = self.getDefDataObj(state, code)
        if incomeData is not None and isinstance(incomeData, dict):
            resultData[b'outCount'] = incomeData.get(b'outcoming', resultData[b'outCount'])
            resultData[b'executionTime'] = incomeData.get(b'execution_time', resultData[b'executionTime'])
            resultData[b'description'] = incomeData.get(b'description', resultData[b'description'])
            resultData[b'declinedReceivers'] = incomeData.get(b'declined_receivers', resultData[b'declinedReceivers'])
        return makeTupleByDict(SendGiftResponse, resultData)

    def getDefDataObj(self, state, code=200):
        return {b'state': state, 
           b'outCount': None, 
           b'meta': (self.__metaInfo), 
           b'receiverIDs': (self.__receiverIDs), 
           b'entitlementCode': (self.__entitlementCode), 
           b'declinedReceivers': [], b'executionTime': (int(time.time())), 
           b'description': None, 
           b'statusCode': code}


class GiftSystemSendGiftCtx(GiftSystemBaseSendGiftCtx):

    def __init__(self, entitlementCode, receiverID=0, metaInfo=None, waitingID=b''):
        super(GiftSystemSendGiftCtx, self).__init__(entitlementCode=entitlementCode, receiverIDs=[receiverID], metaInfo=metaInfo, waitingID=waitingID)
        return

    def getRequestType(self):
        return WebRequestDataType.GIFT_SYSTEM_POST_GIFT

    def getReceiverID(self):
        return self.getReceiverIDs()[0]


class GiftSystemSendGiftMultipleCtx(GiftSystemBaseSendGiftCtx):

    def getRequestType(self):
        return WebRequestDataType.GIFT_SYSTEM_POST_GIFT_MULTIPLE


class GiftSystemWaitResponseCtx(CommonWebRequestCtx):

    def __init__(self, reqEventId, spaID, metaInfo=None, waitingID=b''):
        super(GiftSystemWaitResponseCtx, self).__init__(waitingID)
        self.__reqEventId = reqEventId
        self.__spaID = spaID
        self.__metaInfo = metaInfo or {}
        return

    def isAuthorizationRequired(self):
        return True

    def isClanSyncRequired(self):
        return False

    def isCaching(self):
        return False

    def getReqEventId(self):
        return self.__reqEventId

    def getRequestType(self):
        return WebRequestDataType.GIFT_SYSTEM_WAIT_RESPONSE

    def getSpaID(self):
        return self.__spaID

    def getMetaInfo(self):
        return self.__metaInfo

    def getDataObj(self, incomeData):
        resultData = self.getDefDataObj()
        if incomeData is not None and isinstance(incomeData, dict):
            try:
                resultData[b'players'] = incomeData[b'players']
                resultData[b'lastPlayerUpdatedAt'] = incomeData[b'last_player_updated_at']
                resultData[b'firstPlayerUpdatedAt'] = incomeData[b'first_player_updated_at']
            except (KeyError, TypeError):
                _logger.exception(b'Can not pack event waiting response players because of invalid incomeData')

        return makeTupleByDict(GiftsWaitResponse, resultData)

    def getDefDataObj(self):
        return {b'players': [], b'lastPlayerUpdatedAt': None, 
           b'firstPlayerUpdatedAt': None}
