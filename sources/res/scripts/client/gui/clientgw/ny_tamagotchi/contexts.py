from gui.clientgw.base.contexts import CommonWebRequestCtx
from gui.clientgw.settings import WebRequestDataType

class NyTamagotchiBaseCtx(CommonWebRequestCtx):

    def isAuthorizationRequired(self):
        return True

    def isClanSyncRequired(self):
        return False

    def isCaching(self):
        return False


class NyTamagotchiGetPlayerInfoCtx(NyTamagotchiBaseCtx):

    def getRequestType(self):
        return WebRequestDataType.NY_TAMAGOTCHI_PLAYER_INFO


class NyTamagotchiGetPlayerStatsCtx(NyTamagotchiBaseCtx):

    def getRequestType(self):
        return WebRequestDataType.NY_TAMAGOTCHI_PLAYER_STATS


class NyTamagotchiGetCurrentStateCtx(NyTamagotchiBaseCtx):
    __slots__ = (b'notRecalc',)

    def __init__(self, notRecalc=False, waitingID=b''):
        super(NyTamagotchiGetCurrentStateCtx, self).__init__(waitingID)
        self.notRecalc = notRecalc
        return

    def getRequestType(self):
        return WebRequestDataType.NY_TAMAGOTCHI_CURRENT_STATE


class NyTamagotchiGetLeaderboardPageCtx(NyTamagotchiBaseCtx):
    __slots__ = (b'page', b'isUserPage', b'cumulative')

    def __init__(self, page=0, isUserPage=False, cumulative=False, waitingID=b''):
        super(NyTamagotchiGetLeaderboardPageCtx, self).__init__(waitingID)
        self.page = page
        self.isUserPage = isUserPage
        self.cumulative = cumulative
        return

    def getRequestType(self):
        return WebRequestDataType.NY_TAMAGOTCHI_LEADERBOARD_PAGE


class NyTamagotchiBuyItemsCtx(NyTamagotchiBaseCtx):
    __slots__ = (b'__items',)

    def __init__(self, items=None, waitingID=b''):
        super(NyTamagotchiBuyItemsCtx, self).__init__(waitingID)
        self.__items = items or {}
        return

    def getData(self):
        return [{b'id': (int(key)), b'count': (int(value))} for key, value in self.__items.items()]

    def addItem(self, itemId, count):
        if itemId in self.__items:
            self.__items[itemId] += count
        else:
            self.__items[itemId] = count
        return

    def getItem(self, itemId):
        return self.__items.get(itemId, None)

    def getRequestType(self):
        return WebRequestDataType.NY_TAMAGOTCHI_BUY_ITEMS


class NyTamagotchiActivateItemCtx(NyTamagotchiBaseCtx):
    __slots__ = (b'__id', b'__count')

    def __init__(self, itemId, count, waitingID=b''):
        super(NyTamagotchiActivateItemCtx, self).__init__(waitingID)
        self.__id = itemId
        self.__count = count
        return

    def getData(self):
        return {b'id': (int(self.__id)), b'count': (int(self.__count))}

    def getRequestType(self):
        return WebRequestDataType.NY_TAMAGOTCHI_ACTIVATE_ITEMS
