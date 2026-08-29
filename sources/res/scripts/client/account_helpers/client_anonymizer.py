import logging
from functools import partial
import AccountCommands
from shared_utils.account_helpers.diff_utils import synchronizeDicts
_logger = logging.getLogger(__name__)
_ANONYMIZER_KEY = b'anonymizer'

def _printResponse(resultID, errorCode):
    _logger.debug(b'response: %s', (resultID, errorCode))
    return


class ClientAnonymizer(object):

    def __init__(self, syncData):
        self.__syncData = syncData
        self.__account = None
        self.__cache = {}
        self.__ignore = True
        return

    def clear(self):
        if self.__cache:
            self.__cache.clear()
        return

    def onAccountBecomePlayer(self):
        self.__ignore = False
        return

    def onAccountBecomeNonPlayer(self):
        self.__ignore = True
        return

    def setAccount(self, account):
        self.__account = account
        return

    def setAnonymized(self, anonymized=True, callback=_printResponse):
        self.__account._doCmdIntArr(AccountCommands.CMD_SET_ANONYMIZER_STATE, [
         int(anonymized)], (lambda requestID, resultID, errorCode: callback(resultID, errorCode)))
        return

    def synchronize(self, isFullSync, diff):
        _logger.debug(b'Synchronize Anonymizer')
        if isFullSync:
            self.clear()
        synchronizeDicts(diff.get(_ANONYMIZER_KEY, {}), self.__cache)
        _logger.debug(b'Anonymizer info: %s', self.__cache)
        return

    def getCache(self, callback=None):
        if self.__ignore:
            if callback is not None:
                callback(AccountCommands.RES_NON_PLAYER, None)
            return
        self.__syncData.waitForSync(partial(self.__onGetCacheResponse, callback))
        return

    def __onGetCacheResponse(self, callback, resultID):
        if resultID < 0:
            if callback is not None:
                callback(resultID, None)
            return
        if callback is not None:
            callback(resultID, self.__cache)
        return
