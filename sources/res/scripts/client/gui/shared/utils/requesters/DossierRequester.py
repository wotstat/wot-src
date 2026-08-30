import time
from functools import partial
import BigWorld, constants, dossiers2, AccountCommands
from adisp import adisp_async
from debug_utils import LOG_ERROR
from gui.shared.utils import code2str
from gui.shared.utils.requesters.abstract import AbstractSyncDataRequester
from gui.shared.utils.requesters.common import RequestProcessor
from skeletons.gui.shared.utils.requesters import IDossierRequester

class UserDossier(object):
    __queue = []
    __lastResponseTime = 0
    __request = None

    def __init__(self, databaseID):
        self.__cache = {b'databaseID': (int(databaseID)), 
           b'account': None, 
           b'vehicles': {}, b'clan': None, 
           b'hidden': False, 
           b'available': True, 
           b'rating': None, 
           b'rated7x7Seasons': {}, b'ranked': None}
        return

    def __setLastResponseTime(self):
        self.__lastResponseTime = time.time()
        return

    def __nextRequestTime(self):
        t = constants.REQUEST_COOLDOWN.PLAYER_DOSSIER - (time.time() - self.__lastResponseTime)
        if t > 0:
            return t
        return 0

    def __processQueue(self):
        if self.__request is not None:
            return
        else:
            if self.__queue:
                self.__request = RequestProcessor(self.__nextRequestTime(), self.__queue.pop())
                return
            return

    def __requestPlayerInfo(self, callback):

        def proxyCallback(value):
            if value is not None and len(value) > 1:
                self.__cache[b'databaseID'] = value[0]
                self.__cache[b'account'] = dossiers2.getAccountDossierDescr(value[1])
                self.__cache[b'clan'] = value[2]
                self.__cache[b'rating'] = value[3]
                self.__cache[b'rated7x7Seasons'] = seasons = {}
                self.__cache[b'ranked'] = value[5]
                self.__cache[b'dogTag'] = value[6]
                self.__cache[b'battleRoyaleStats'] = value[7]
                self.__cache[b'wtr'] = value[8]
                self.__cache[b'layout'] = value[9]
                self.__cache[b'layoutState'] = value[10]
                for sID, d in (value[4] or {}).iteritems():
                    seasons[sID] = dossiers2.getRated7x7DossierDescr(d)

            callback(self.__cache[b'account'])
            return

        def callBackMethod(c, code, databaseID, dossier, clanID, clanInfo, gRating, eSportSeasons, ranked, dogTag, br, wtr, layout, layoutState):
            value = (
             databaseID, dossier, (clanID, clanInfo), gRating, eSportSeasons, ranked, dogTag, br, wtr, layout,
             layoutState)
            self.__processValueResponse(c, code, value)
            return

        self.__queue.append((lambda : BigWorld.player().requestPlayerInfo(self.__cache[b'databaseID'], partial(callBackMethod, proxyCallback))))
        self.__processQueue()
        return

    def __requestAccountDossier(self, callback):

        def proxyCallback(dossier):
            self.__cache[b'account'] = dossiers2.getAccountDossierDescr(dossier)
            callback(self.__cache[b'account'])
            return

        self.__queue.append((lambda : BigWorld.player().requestAccountDossier(self.__cache[b'databaseID'], partial(self.__processValueResponse, proxyCallback))))
        self.__processQueue()
        return

    def __requestVehicleDossier(self, vehCompDescr, callback):

        def proxyCallback(dossier):
            self.__cache[b'vehicles'][vehCompDescr] = dossiers2.getVehicleDossierDescr(dossier)
            callback(self.__cache[b'vehicles'][vehCompDescr])
            return

        self.__queue.append((lambda : BigWorld.player().requestVehicleDossier(self.__cache[b'databaseID'], vehCompDescr, partial(self.__processValueResponse, proxyCallback))))
        self.__processQueue()
        return

    def __requestClanInfo(self, callback):
        self.__queue.append((lambda : BigWorld.player().requestPlayerClanInfo(self.__cache[b'databaseID'], partial((lambda c, code, str, clanDBID, clanInfo: self.__processValueResponse(c, code, (clanDBID, clanInfo))), callback))))
        self.__processQueue()
        return

    def __processValueResponse(self, callback, code, value):
        self.__setLastResponseTime()
        self.__request = None
        if code < 0:
            LOG_ERROR(b'Error while server request (code=%s): %s' % (code, code2str(code)))
            if code == AccountCommands.RES_HIDDEN_DOSSIER:
                self.__cache[b'hidden'] = True
            elif code == AccountCommands.RES_CENTER_DISCONNECTED:
                self.__cache[b'available'] = False
            callback(b'')
        else:
            callback(value)
        self.__processQueue()
        return

    @adisp_async
    def getAccountDossier(self, callback):
        if not self.isValid:
            callback(None)
        if self.__cache.get(b'account') is None:
            self.__requestPlayerInfo(callback)
            return
        else:
            callback(self.__cache[b'account'])
            return

    @adisp_async
    def getClanInfo(self, callback):
        if not self.isValid:
            callback(None)
        if self.__cache.get(b'clan') is None:
            self.__requestClanInfo(callback)
            return
        else:
            callback(self.__cache[b'clan'])
            return

    @adisp_async
    def getRated7x7Seasons(self, callback):
        if not self.isValid:
            callback({})
        if self.__cache.get(b'rated7x7Seasons') is None:
            self.__requestPlayerInfo((lambda accDossier: callback(self.__cache[b'rated7x7Seasons'])))
            return
        else:
            callback(self.__cache[b'rated7x7Seasons'])
            return

    @adisp_async
    def getRankedInfo(self, callback):
        if not self.isValid:
            callback({})
        if self.__cache.get(b'ranked') is None:
            self.__requestPlayerInfo((lambda accDossier: callback(self.__cache[b'ranked'])))
            return
        else:
            callback(self.__cache[b'ranked'])
            return

    @adisp_async
    def getGlobalRating(self, callback):
        if not self.isValid:
            callback(None)
        if self.__cache.get(b'rating') is None:
            self.__requestPlayerInfo((lambda accDossier: callback(self.__cache[b'rating'])))
            return
        else:
            callback(self.__cache[b'rating'])
            return

    @adisp_async
    def getVehicleDossier(self, vehCompDescr, callback):
        if not self.isValid:
            callback(None)
        if self.__cache.get(b'vehicles', {}).get(vehCompDescr, None) is None:
            self.__requestVehicleDossier(vehCompDescr, callback)
            return
        else:
            callback(self.__cache[b'vehicles'][vehCompDescr])
            return

    @adisp_async
    def getDogTag(self, callback):
        if not self.isValid:
            callback(None)
        if self.__cache.get(b'dogTag') is None:
            self.__requestPlayerInfo(callback)
            return
        else:
            callback(self.__cache[b'dogTag'])
            return

    @adisp_async
    def getBattleRoyaleStats(self, callback):
        if not self.isValid:
            callback({})
        if self.__cache.get(b'battleRoyaleStats') is None:
            self.__requestPlayerInfo((lambda accDossier: callback(self.__cache[b'battleRoyaleStats'])))
            return
        else:
            callback(self.__cache[b'battleRoyaleStats'])
            return

    @adisp_async
    def getWTR(self, callback):
        if not self.isValid:
            callback(None)
        if self.__cache.get(b'wtr') is None:
            self.__requestPlayerInfo(callback)
            return
        else:
            callback(self.__cache[b'wtr'])
            return

    @adisp_async
    def getLayout(self, callback):
        if not self.isValid:
            callback(None)
        if self.__cache.get(b'layout') is None:
            self.__requestPlayerInfo(callback)
            return
        else:
            callback(self.__cache[b'layout'])
            return

    @adisp_async
    def getLayoutState(self, callback):
        if not self.isValid:
            callback(None)
        if self.__cache.get(b'layoutState') is None:
            self.__requestPlayerInfo(callback)
            return
        else:
            callback(self.__cache[b'layoutState'])
            return

    @property
    def isHidden(self):
        return self.__cache.get(b'hidden', False)

    @property
    def isAvailable(self):
        return self.__cache.get(b'available', False)

    @property
    def isValid(self):
        return not self.isHidden and self.isAvailable


class DossierRequester(AbstractSyncDataRequester, IDossierRequester):

    def __init__(self):
        super(DossierRequester, self).__init__()
        self.__users = {}
        return

    @adisp_async
    def _requestCache(self, callback):
        BigWorld.player().dossierCache.getCache((lambda resID, value: self._response(resID, value, callback)))
        return

    def getVehicleDossier(self, vehTypeCompDescr):
        return self.getCacheValue((
         constants.DOSSIER_TYPE.VEHICLE, vehTypeCompDescr), (0, b''))[1]

    def getVehDossiersIterator(self):
        for (dossierType, vehIntCD), records in self._data.iteritems():
            if dossierType == constants.DOSSIER_TYPE.VEHICLE:
                yield (
                 vehIntCD, records[1])

        return

    def getUserDossierRequester(self, databaseID):
        databaseID = int(databaseID)
        return self.__users.setdefault(databaseID, UserDossier(databaseID))

    def closeUserDossier(self, databaseID):
        if databaseID in self.__users:
            del self.__users[databaseID]
        return

    def onCenterIsLongDisconnected(self, isLongDisconnected):
        if isLongDisconnected:
            return
        self.__users = dict(item for item in self.__users.iteritems() if item[1].isAvailable)
        return
