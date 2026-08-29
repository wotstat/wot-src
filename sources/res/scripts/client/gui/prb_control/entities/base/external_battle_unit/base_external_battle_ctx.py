from gui.prb_control import settings
from gui.prb_control.entities.base.unit.ctx import UnitRequestCtx
from gui.shared.utils.decorators import ReprInjector
from external_strings_utils import truncate_utf8
from gui.prb_control.settings import INVITE_COMMENT_MAX_LENGTH, REQUEST_TYPE
from gui.prb_control.entities.base.ctx import PrbCtrlRequestCtx
_REQUEST_TYPE = settings.REQUEST_TYPE
_UNDEFINED = settings.FUNCTIONAL_FLAG.UNDEFINED

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
class CreateBaseExternalUnitCtx(TimeoutCtx):
    __slots__ = (b'__rosterID',)

    def __init__(self, prbType, flags=_UNDEFINED, waitingID=b'', rosterID=0, onTimeoutCallback=None):
        super(CreateBaseExternalUnitCtx, self).__init__(prbType=prbType, waitingID=waitingID, flags=flags, onTimeoutCallback=onTimeoutCallback)
        self.__rosterID = rosterID
        return

    def getRequestType(self):
        return _REQUEST_TYPE.CREATE

    def getRosterID(self):
        return self.__rosterID


class JoinBaseExternalUnitCtx(TimeoutCtx):
    __slots__ = (b'__unitMgrID', b'__onErrorCallback')

    def __init__(self, unitMgrID, prbType, onErrorCallback=None, waitingID=b''):
        super(JoinBaseExternalUnitCtx, self).__init__(prbType=prbType, waitingID=waitingID)
        self.__unitMgrID = unitMgrID
        self.__onErrorCallback = onErrorCallback
        return

    def getRequestType(self):
        return _REQUEST_TYPE.JOIN

    def getID(self):
        return self.__unitMgrID

    def callErrorCallback(self, errorData):
        onErrorCallback = self.__onErrorCallback
        if onErrorCallback and callable(onErrorCallback):
            onErrorCallback(errorData)
        return


@ReprInjector.withParent((b'__slotIdx', b'slotIdx'), (b'__vehTypes', b'vehTypes'))
class ChangeVehTypesInSlotFilterCtx(UnitRequestCtx):
    __slots__ = (b'__slotIdx', b'__vehTypes')

    def __init__(self, slotIdx, vehTypes, waitingID=b''):
        super(ChangeVehTypesInSlotFilterCtx, self).__init__(waitingID=waitingID)
        self.__slotIdx = slotIdx
        self.__vehTypes = vehTypes
        return

    def getRequestType(self):
        return _REQUEST_TYPE.SET_SLOT_VEHICLE_TYPE_FILTER

    def getSlotIdx(self):
        return self.__slotIdx

    def getVehTypes(self):
        return self.__vehTypes

    def getCooldown(self):
        return 0.2


@ReprInjector.withParent((b'__slotIdx', b'slotIdx'), (b'__vehicles', b'vehicles'))
class ChangeVehiclesInSlotFilterCtx(UnitRequestCtx):
    __slots__ = (b'__slotIdx', b'__vehicles')

    def __init__(self, slotIdx, vehicles, waitingID=b''):
        super(ChangeVehiclesInSlotFilterCtx, self).__init__(waitingID=waitingID)
        self.__slotIdx = slotIdx
        self.__vehicles = vehicles
        return

    def getRequestType(self):
        return _REQUEST_TYPE.SET_SLOT_VEHICLES_FILTER

    def getSlotIdx(self):
        return self.__slotIdx

    def getVehicles(self):
        return self.__vehicles

    def getCooldown(self):
        return 0.2


@ReprInjector.withParent((b'getDatabaseIDs', b'databaseIDs'), (b'getComment', b'comment'))
class SendInvitesExternalBattleUnitCtx(PrbCtrlRequestCtx):

    def __init__(self, databaseIDs, comment, waitingID=b''):
        super(SendInvitesExternalBattleUnitCtx, self).__init__(waitingID=waitingID)
        self.__databaseIDs = databaseIDs[:300]
        if comment:
            self.__comment = truncate_utf8(comment, INVITE_COMMENT_MAX_LENGTH)
        else:
            self.__comment = b''
        return

    def getDatabaseIDs(self):
        return self.__databaseIDs[:]

    def getComment(self):
        return self.__comment

    def getRequestType(self):
        return REQUEST_TYPE.SEND_INVITE


class StopPlayersMatchingBaseExternalUnitCtx(UnitRequestCtx):
    __slots__ = ()

    def getRequestType(self):
        return _REQUEST_TYPE.STOP_PLAYERS_MATCHING
