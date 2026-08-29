from gui.clans import items
from gui.clans.settings import DEFAULT_COOLDOWN
from gui.shared.utils.decorators import ReprInjector
from gui.shared.utils.requesters import RequestCtx
from gui.clientgw.settings import WebRequestDataType
from helpers import dependency
from shared_utils import makeTupleByDict
from skeletons.gui.shared import IItemsCache

@ReprInjector.withParent()
class CommonWebRequestCtx(RequestCtx):
    itemsCache = dependency.descriptor(IItemsCache)

    def __init__(self, waitingID=b''):
        super(CommonWebRequestCtx, self).__init__(waitingID=waitingID)
        return

    def getCooldown(self):
        return DEFAULT_COOLDOWN

    def isCaching(self):
        return True

    def isAuthorizationRequired(self):
        return False

    def getFields(self):
        return

    def isClanSyncRequired(self):
        return True

    def _getOwnClanDbID(self):
        return self.itemsCache.items.stats.clanDBID


@ReprInjector.withParent((b'getTokenID', b'token'), (b'getUserDatabaseID', b'dbID'), (b'isJwt', b'jwt'))
class LogInCtx(CommonWebRequestCtx):

    def __init__(self, databaseID, tokenID, isJwt):
        super(LogInCtx, self).__init__()
        self.__tokenID = tokenID
        self.__databaseID = databaseID
        self.__isJwt = isJwt
        return

    def getTokenID(self):
        return self.__tokenID

    def getUserDatabaseID(self):
        return self.__databaseID

    def isJwt(self):
        return self.__isJwt

    def getRequestType(self):
        return WebRequestDataType.LOGIN


@ReprInjector.withParent()
class LogOutCtx(CommonWebRequestCtx):

    def getRequestType(self):
        return WebRequestDataType.LOGOUT


@ReprInjector.withParent((b'getClanDbIDs', b'clanDbIDs'), (b'getComment', b'comment'))
class CreateApplicationCtx(CommonWebRequestCtx):

    def __init__(self, clanDbIDs, comment=b'', waitingID=b''):
        super(CreateApplicationCtx, self).__init__(waitingID)
        self.__clanDbIDs = clanDbIDs
        self.__comment = comment
        return

    def getClanDbIDs(self):
        return self.__clanDbIDs

    def getComment(self):
        return self.__comment

    def getRequestType(self):
        return WebRequestDataType.CREATE_APPLICATIONS

    def getDataObj(self, incomeData):
        data = incomeData or []
        return [makeTupleByDict(items.ClanCreateInviteData, item) for item in data]

    def getDefDataObj(self):
        return list()

    def isAuthorizationRequired(self):
        return True


@ReprInjector.withParent()
class PingCtx(CommonWebRequestCtx):

    def __init__(self, waitingID=b''):
        super(PingCtx, self).__init__(waitingID=waitingID)
        return

    def getRequestType(self):
        return WebRequestDataType.PING

    def getDataObj(self, incomeData):
        return incomeData

    def getDefDataObj(self):
        return

    def isCaching(self):
        return False


@ReprInjector.withParent((b'getAccountsIDs', b'ids'))
class AccountsInfoBaseCtx(CommonWebRequestCtx):

    def __init__(self, accIDs, waitingID=b''):
        super(AccountsInfoBaseCtx, self).__init__(waitingID)
        self.__accountsIDs = accIDs
        return

    def getAccountsIDs(self):
        return self.__accountsIDs


@ReprInjector.withParent((b'getOffset', b'offset'), (b'getLimit', b'limit'), (b'isGetTotalCount', b'isGetTotalCount'), (b'getFields', b'fields'))
class PaginatorCtx(CommonWebRequestCtx):

    def __init__(self, offset, limit, getTotalCount=False, fields=None, waitingID=b''):
        super(PaginatorCtx, self).__init__(waitingID)
        self.__offset = offset
        self.__limit = limit
        self.__getTotalCount = getTotalCount
        self.__fields = fields
        return

    def getOffset(self):
        return self.__offset

    def getLimit(self):
        return self.__limit

    def isGetTotalCount(self):
        return self.__getTotalCount

    def getFields(self):
        return self.__fields

    def getTotalCount(self, incomeData):
        if incomeData:
            return incomeData.get(b'total', None)
        else:
            return

    def getDataObj(self, incomeData):
        data = incomeData.get(b'items', self.getDefDataObj()) if incomeData else self.getDefDataObj()
        return data

    def getDefDataObj(self):
        return list()


@ReprInjector.withParent((b'getID', b'id'))
class TotalInfoCtx(CommonWebRequestCtx):

    def __init__(self, itemID, waitingID=b''):
        super(TotalInfoCtx, self).__init__(waitingID)
        self.__itemID = itemID
        return

    def getID(self):
        return self.__itemID

    def getDataObj(self, incomeData):
        if incomeData:
            return incomeData[b'total']
        return self.getDefDataObj()

    def getDefDataObj(self):
        return 0
