from gui.prb_control import settings
from gui.prb_control.entities.base.unit.ctx import UnitRequestCtx
from gui.shared.utils.decorators import ReprInjector
_REQUEST_TYPE = settings.REQUEST_TYPE
_UNDEFINED = settings.FUNCTIONAL_FLAG.UNDEFINED

class SetReserveUnitCtx(UnitRequestCtx):
    __slots__ = (b'__reserveID', b'__isRemove')

    def __init__(self, reserveID, waitingID=b'', flags=_UNDEFINED, entityType=0, isRemove=False):
        super(SetReserveUnitCtx, self).__init__(waitingID=waitingID, flags=flags, entityType=entityType)
        self.__reserveID = reserveID
        self.__isRemove = isRemove
        return

    def getRequestType(self):
        return _REQUEST_TYPE.SET_RESERVE

    def getReserveID(self):
        return self.__reserveID

    def getIsRemove(self):
        return self.__isRemove


class UnsetReserveUnitCtx(UnitRequestCtx):
    __slots__ = (b'__reserveID', b'__isRemove')

    def __init__(self, reserveID, waitingID=b'', flags=_UNDEFINED, entityType=0, isRemove=False):
        super(UnsetReserveUnitCtx, self).__init__(waitingID=waitingID, flags=flags, entityType=entityType)
        self.__reserveID = reserveID
        self.__isRemove = isRemove
        return

    def getRequestType(self):
        return _REQUEST_TYPE.UNSET_RESERVE

    def getReserveID(self):
        return self.__reserveID

    def getIsRemove(self):
        return self.__isRemove


class TimeoutCtx(UnitRequestCtx):
    __slots__ = (b'__onTimeoutCallback',)

    def __init__(self, prbType, flags=_UNDEFINED, waitingID=b'', onTimeoutCallback=None):
        super(TimeoutCtx, self).__init__(entityType=prbType, waitingID=waitingID, flags=flags)
        self.__onTimeoutCallback = onTimeoutCallback
        return

    def callTimeoutCallback(self):
        onTimeoutCallback = self.__onTimeoutCallback
        if onTimeoutCallback and callable(onTimeoutCallback):
            onTimeoutCallback()
        return


@ReprInjector.withParent((b'__rosterID', b'rosterID'))
class CreateUnitCtx(TimeoutCtx):
    __slots__ = (b'__rosterID',)

    def __init__(self, prbType, flags=_UNDEFINED, waitingID=b'', rosterID=0, onTimeoutCallback=None):
        super(CreateUnitCtx, self).__init__(prbType=prbType, waitingID=waitingID, flags=flags, onTimeoutCallback=onTimeoutCallback)
        self.__rosterID = rosterID
        return

    def getRequestType(self):
        return _REQUEST_TYPE.CREATE

    def getRosterID(self):
        return self.__rosterID


@ReprInjector.withParent((b'__databaseID', b'databaseID'))
class GiveEquipmentCommanderCtx(UnitRequestCtx):
    __slots__ = (b'__databaseID', b'__role')

    def __init__(self, databaseID, role, waitingID=b''):
        super(GiveEquipmentCommanderCtx, self).__init__(waitingID=waitingID)
        self.__databaseID = databaseID
        self.__role = role
        return

    def getRequestType(self):
        return _REQUEST_TYPE.SET_EQUIPMENT_COMMANDER

    def getPlayerID(self):
        return self.__databaseID

    def getRole(self):
        return self.__role
