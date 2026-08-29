from GlobalMapBase import GlobalMapBase, GM_CLIENT_METHOD
from debug_utils import LOG_DEBUG_DEV
import Event

class ClientGlobalMap(GlobalMapBase):

    def __init__(self, account=None):
        self.__account = account
        self.__eManager = Event.EventManager()
        GlobalMapBase.__init__(self)
        self.__requestID = 0
        return

    def clear(self):
        self.__eManager.clear()
        return

    def setAccount(self, account=None):
        self.__account = account
        return

    def __getNextRequestID(self):
        self.__requestID += 1
        return self.__requestID

    def __callGlobalMapMethod(self, *args):
        requestID = self.__getNextRequestID()
        LOG_DEBUG_DEV(b'base.callGlobalMapMethod', requestID, args)
        self.__account.base.accountGlobalMapConnector_callGlobalMapMethod(requestID, *args)
        return requestID

    def onGlobalMapReply(self, reqID, resultCode, resultString):
        LOG_DEBUG_DEV(b'onGlobalMapReply: reqID=%s, resultCode=%s, resultString=%r' % (reqID, resultCode, resultString))
        return

    def subscribe(self):
        return self.__callGlobalMapMethod(GM_CLIENT_METHOD.SUBSCRIBE, 0, b'')

    def unsubscribe(self):
        return self.__callGlobalMapMethod(GM_CLIENT_METHOD.UNSUBSCRIBE, 0, b'')

    def joinBattle(self, battleID):
        return self.__callGlobalMapMethod(GM_CLIENT_METHOD.JOIN_BATTLE, battleID, b'')

    def setDevMode(self, isOn):
        return self.__callGlobalMapMethod(GM_CLIENT_METHOD.SET_DEV_MODE, int(isOn), b'')

    def keepAlive(self):
        return self.__callGlobalMapMethod(GM_CLIENT_METHOD.KEEP_ALIVE, 0, b'')

    def onGlobalMapUpdate(self, packedOps, packedUpdate):
        LOG_DEBUG_DEV(b'onGlobalMapUpdate: packedOps len=%s, packedUpdate len=%s' % (len(packedOps), len(packedUpdate)))
        if packedUpdate:
            self.unpack(packedUpdate)
        elif packedOps:
            self.unpackOps(packedOps)
        return

    def _unpackBattle(self, packedData):
        LOG_DEBUG_DEV(b'_unpackBattle: packedData len=%s' % (len(packedData),))
        packedData = GlobalMapBase._unpackBattle(self, packedData)
        return packedData

    def _removeBattle(self, battleID):
        LOG_DEBUG_DEV(b'_removeBattle: battleID=%s' % (battleID,))
        GlobalMapBase._removeBattle(self, battleID)
        return

    def _unpackBattleUnit(self, packedData):
        LOG_DEBUG_DEV(b'_unpackBattleUnit: packedData len=%s' % (len(packedData),))
        packedData = GlobalMapBase._unpackBattleUnit(self, packedData)
        return packedData

    def _removeBattleUnit(self, battleID):
        LOG_DEBUG_DEV(b'_removeBattleUnit: battleID=%s' % (battleID,))
        GlobalMapBase._removeBattleUnit(self, battleID)
        return
