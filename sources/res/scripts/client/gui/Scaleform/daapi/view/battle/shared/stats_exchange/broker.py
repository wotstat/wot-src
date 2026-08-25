from __future__ import absolute_import
import weakref
from contextlib import contextmanager
import Event
from constants import IGR_TYPE
from messenger.m_constants import USER_TAG, UserEntityScope
from messenger.storage import storage_getter
from shared_utils import AlwaysValidObject

class IExchangeComponent(object):
    __slots__ = (b'__weakref__',)

    def get(self, forced=False):
        raise NotImplementedError
        return

    def clear(self):
        raise NotImplementedError
        return

    def destroy(self):
        return


class IExchangeComposer(object):
    __slots__ = ()

    def clear(self):
        raise NotImplementedError
        return

    def compose(self, data):
        raise NotImplementedError
        return


class IExternalExchangeComponent(IExchangeComponent):
    __slots__ = ()

    def clear(self):
        raise NotImplementedError
        return

    def get(self, forced=False):
        raise NotImplementedError
        return


class CollectableStats(object):
    __slots__ = (b'onTotalScoreUpdated', b'__score', b'__weakref__')

    def __init__(self):
        super(CollectableStats, self).__init__()
        self.__score = (0, 0)
        self.onTotalScoreUpdated = Event.Event()
        return

    def clear(self):
        self.onTotalScoreUpdated.clear()
        return

    def addVehicleStatsUpdate(self, vInfoVO, vStatsVO):
        raise NotImplementedError
        return

    def addVehicleStatusUpdate(self, vInfoVO):
        raise NotImplementedError
        return

    def getTotalStats(self, arenaVisitor, sessionProvider):
        raise NotImplementedError
        return

    def getTotalScore(self):
        return self.__score

    def _setTotalScore(self, leftScope, rightScope):
        self.__score = (
         leftScope, rightScope)
        self.onTotalScoreUpdated(leftScope, rightScope)
        return


class NoCollectableStats(CollectableStats):
    __slots__ = ()

    def clear(self):
        return

    def addVehicleStatsUpdate(self, vInfoVO, vStatsVO):
        return

    def addVehicleStatusUpdate(self, vInfoVO):
        return

    def getTotalStats(self, arenaVisitor, sessionProvider):
        return

    def getTotalScore(self):
        return (0, 0)


class ExchangeComponent(IExchangeComponent):
    __slots__ = (b'_ctx', b'_isEnemy')

    def __init__(self):
        super(ExchangeComponent, self).__init__()
        self._ctx = None
        self._isEnemy = True
        return

    def clear(self):
        self._isEnemy = True
        return

    def destroy(self):
        self._ctx = None
        self.clear()
        return

    def getCtx(self):
        return self._ctx

    def setCtx(self, ctx):
        self._ctx = ctx
        return

    def isEnemy(self):
        return self._isEnemy

    def setEnemy(self, isEnemy):
        self._isEnemy = isEnemy
        return

    def get(self, forced=False):
        raise NotImplementedError
        return


class SingleSideComposer(IExchangeComposer):
    __slots__ = (b'_items', b'_voField', b'_sortKey')

    def __init__(self, voField=b'items', sortKey=None):
        super(SingleSideComposer, self).__init__()
        self._items = []
        self._voField = voField
        self._sortKey = sortKey
        return

    def clear(self):
        self._items = []
        return

    def compose(self, data):
        if self._items:
            data[self._voField] = self._items
        return data

    def addItem(self, _, data):
        self._items.append(data)
        return


class BiDirectionComposer(IExchangeComposer):
    __slots__ = (b'_left', b'_right')

    def __init__(self, left=None, right=None):
        super(BiDirectionComposer, self).__init__()
        self._left = left or SingleSideComposer(voField=b'leftItems')
        self._right = right or SingleSideComposer(voField=b'rightItems')
        return

    def clear(self):
        self._left.clear()
        self._right.clear()
        return

    def compose(self, data):
        self._left.compose(data)
        self._right.compose(data)
        return data

    def addItem(self, isEnemy, data):
        if isEnemy:
            self._right.addItem(isEnemy, data)
        else:
            self._left.addItem(isEnemy, data)
        return


class ExchangeBlock(IExternalExchangeComponent):
    __slots__ = (b'_component', b'_composer')

    def __init__(self, component, composer=None):
        self._component = component
        self._composer = composer or BiDirectionComposer()
        super(ExchangeBlock, self).__init__()
        return

    def clear(self):
        self._composer.clear()
        return

    def destroy(self):
        if self._component is not None:
            self._component.destroy()
            self._component = None
        if self._composer is not None:
            self._composer.clear()
            self._composer = None
        return

    def setCtx(self, ctx):
        self._component.setCtx(ctx)
        return

    def get(self, forced=False):
        return self._composer.compose({})

    def getComponent(self):
        self._component.clear()
        return self._component

    @contextmanager
    def getCollectedComponent(self, isEnemy, forced=False):
        self._component.clear()
        self._component.setEnemy(isEnemy)
        yield self._component
        data = self._component.get(forced=forced)
        if data:
            self._composer.addItem(isEnemy, data)
        return

    def addSortIDs(self, arenaDP, *flags):
        raise NotImplementedError
        return

    def addTotalStats(self, stats):
        raise NotImplementedError
        return


class VehicleComponent(ExchangeComponent):
    __slots__ = (b'_vehicleID',)

    def __init__(self):
        super(VehicleComponent, self).__init__()
        self._vehicleID = 0
        return

    def clear(self):
        self._vehicleID = 0
        super(VehicleComponent, self).clear()
        return

    def get(self, forced=False):
        return {b'isEnemy': (self._isEnemy), 
           b'vehicleID': (self._vehicleID)}

    def setVehicleID(self, vehicleID):
        self._vehicleID = vehicleID
        return


class StatusComponent(VehicleComponent):
    __slots__ = (b'_status',)

    def __init__(self, status=0):
        super(StatusComponent, self).__init__()
        self._status = status
        return

    def clear(self):
        self._status = 0
        super(StatusComponent, self).clear()
        return

    def get(self, forced=False):
        return {b'isEnemy': (self._isEnemy), 
           b'vehicleID': (self._vehicleID), 
           b'status': (self._status)}

    def setStatus(self, status):
        self._status = status
        return


class NoExchangeComponent(ExchangeComponent, AlwaysValidObject):
    __slots__ = ()

    def get(self, forced=False):
        return

    def clear(self):
        return


class NoExchangeBlock(ExchangeBlock, AlwaysValidObject):
    __slots__ = ()

    def __init__(self):
        super(NoExchangeBlock, self).__init__(NoExchangeComponent())
        return

    def get(self, forced=False):
        return

    @contextmanager
    def getCollectedComponent(self, isEnemy, forced=False):
        yield self._component
        return

    def addSortIDs(self, arenaDP, *flags):
        return

    def addTotalStats(self, stats):
        return


class ExchangeCtx(object):
    __slots__ = (b'__weakref__', b'__playerFormatter')

    def __init__(self, playerFormatter):
        super(ExchangeCtx, self).__init__()
        self.__playerFormatter = playerFormatter
        return

    @storage_getter(b'users')
    def usersStorage(self):
        return

    def clear(self):
        self.__playerFormatter = None
        return

    def getPlayerFullName(self, vInfoVO):
        return self.__playerFormatter.format(vInfoVO)

    def getUserTags(self, avatarSessionID, igrType):
        contact = self.usersStorage.getUser(avatarSessionID, scope=UserEntityScope.BATTLE)
        if contact is not None and avatarSessionID:
            userTags = contact.getTags()
        else:
            userTags = set()
        return self.addTagByIGRType(userTags, igrType)

    @staticmethod
    def addTagByIGRType(userTags, igrType):
        if igrType == IGR_TYPE.BASE:
            userTags.add(USER_TAG.IGR_BASE)
        elif igrType == IGR_TYPE.PREMIUM:
            userTags.add(USER_TAG.IGR_PREMIUM)
        return userTags


class ExchangeBroker(object):
    __slots__ = (b'_ctx', b'_vehiclesInfo', b'_vehiclesStatus', b'_vehiclesStats', b'_playerStatus', b'_usersTags', b'_invitations')

    def __init__(self, ctx):
        super(ExchangeBroker, self).__init__()
        self._ctx = ctx
        self._vehiclesInfo = NoExchangeBlock()
        self._vehiclesStatus = NoExchangeComponent()
        self._vehiclesStats = NoExchangeBlock()
        self._playerStatus = NoExchangeComponent()
        self._usersTags = NoExchangeBlock()
        self._invitations = NoExchangeBlock()
        return

    def destroy(self):
        if self._vehiclesInfo is not None:
            self._vehiclesInfo.destroy()
            self._vehiclesInfo = None
        if self._vehiclesStatus is not None:
            self._vehiclesStatus.destroy()
            self._vehiclesStatus = None
        if self._playerStatus is not None:
            self._playerStatus.destroy()
            self._playerStatus = None
        if self._vehiclesStats is not None:
            self._vehiclesStats.destroy()
            self._vehiclesStats = None
        if self._usersTags is not None:
            self._usersTags.destroy()
            self._usersTags = None
        if self._invitations is not None:
            self._invitations.destroy()
            self._invitations = None
        if self._ctx is not None:
            self._ctx.clear()
            self._ctx = None
        return

    def getVehiclesInfoExchange(self):
        self._vehiclesInfo.clear()
        return self._vehiclesInfo

    def setVehiclesInfoExchange(self, exchange):
        self._vehiclesInfo = exchange
        self._vehiclesInfo.setCtx(weakref.proxy(self._ctx))
        return

    def getVehicleStatusExchange(self, isEnemy):
        self._vehiclesStatus.clear()
        self._vehiclesStatus.setEnemy(isEnemy)
        return self._vehiclesStatus

    def setVehicleStatusExchange(self, exchange):
        self._vehiclesStatus = exchange
        return

    def getVehiclesStatsExchange(self):
        self._vehiclesStats.clear()
        return self._vehiclesStats

    def setVehiclesStatsExchange(self, exchange):
        self._vehiclesStats = exchange
        self._vehiclesStats.setCtx(weakref.proxy(self._ctx))
        return

    def getPlayerStatusExchange(self, isEnemy):
        self._playerStatus.clear()
        self._playerStatus.setEnemy(isEnemy)
        return self._playerStatus

    def setPlayerStatusExchange(self, exchange):
        self._playerStatus = exchange
        self._playerStatus.setCtx(weakref.proxy(self._ctx))
        return

    def getUsersTagsExchange(self):
        self._usersTags.clear()
        return self._usersTags

    def setUsersTagsExchange(self, exchange):
        self._usersTags = exchange
        self._usersTags.setCtx(weakref.proxy(self._ctx))
        return

    def getUserTagsItemExchange(self, isEnemy):
        component = self._usersTags.getComponent()
        component.setEnemy(isEnemy)
        return component

    def getInvitationsExchange(self):
        self._invitations.clear()
        return self._invitations

    def setInvitationsExchange(self, exchange):
        self._invitations = exchange
        self._invitations.setCtx(weakref.proxy(self._ctx))
        return
