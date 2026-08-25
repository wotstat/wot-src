from account_helpers import gameplay_ctx
from external_strings_utils import truncate_utf8
from UnitBase import UNIT_SLOT
from gui.prb_control import settings, prb_getters
from gui.prb_control.entities.base.ctx import PrbCtrlRequestCtx
from gui.shared.utils.decorators import ReprInjector
_CTRL_ENTITY_TYPE = settings.CTRL_ENTITY_TYPE
_REQUEST_TYPE = settings.REQUEST_TYPE
_UNDEFINED = settings.FUNCTIONAL_FLAG.UNDEFINED

@ReprInjector.withParent((b'getID', b'unitMgrID'))
class UnitRequestCtx(PrbCtrlRequestCtx):
    __slots__ = ()

    def __init__(self, **kwargs):
        super(UnitRequestCtx, self).__init__(ctrlType=_CTRL_ENTITY_TYPE.UNIT, **kwargs)
        return

    def getID(self):
        return prb_getters.getUnitMgrID()

    def getCooldown(self):
        return 5.0


@ReprInjector.withParent((b'__rosterID', b'rosterID'))
class CreateUnitCtx(UnitRequestCtx):
    __slots__ = (b'__rosterID',)

    def __init__(self, prbType, flags=_UNDEFINED, waitingID=b'', rosterID=0):
        super(CreateUnitCtx, self).__init__(entityType=prbType, waitingID=waitingID, flags=flags)
        self.__rosterID = rosterID
        return

    def getRequestType(self):
        return _REQUEST_TYPE.CREATE

    def getRosterID(self):
        return self.__rosterID


class JoinUnitModeCtx(UnitRequestCtx):
    __slots__ = ()

    def __init__(self, prbType, waitingID=b'', flags=_UNDEFINED):
        super(JoinUnitModeCtx, self).__init__(entityType=prbType, waitingID=waitingID, flags=flags)
        return

    def getID(self):
        return prb_getters.getUnitMgrID()


@ReprInjector.withParent((b'__unitMgrID', b'unitMgrID'), (b'__slotIdx', b'slotIdx'))
class JoinUnitCtx(UnitRequestCtx):
    __slots__ = (b'__unitMgrID', b'__slotIdx')

    def __init__(self, unitMgrID, prbType, slotIdx=None, waitingID=b''):
        super(JoinUnitCtx, self).__init__(entityType=prbType, waitingID=waitingID)
        self.__unitMgrID = unitMgrID
        self.__slotIdx = slotIdx
        return

    def getRequestType(self):
        return _REQUEST_TYPE.JOIN

    def getID(self):
        return self.__unitMgrID

    def getSlotIdx(self):
        return self.__slotIdx


class LeaveUnitCtx(UnitRequestCtx):

    def __init__(self, waitingID=b'', flags=_UNDEFINED, entityType=0):
        super(LeaveUnitCtx, self).__init__(waitingID=waitingID, flags=flags, entityType=entityType)
        return

    def getRequestType(self):
        return _REQUEST_TYPE.LEAVE

    def getCooldown(self):
        return 0.3


@ReprInjector.withParent((b'__isLocked', b'isLocked'))
class LockUnitCtx(UnitRequestCtx):
    __slots__ = (b'__isLocked',)

    def __init__(self, isLocked=True, waitingID=b''):
        super(LockUnitCtx, self).__init__(waitingID=waitingID)
        self.__isLocked = isLocked
        return

    def getRequestType(self):
        return _REQUEST_TYPE.LOCK

    def isLocked(self):
        return self.__isLocked


@ReprInjector.withParent((b'__slotIdx', b'slotIdx'), (b'__isClosed', b'isClosed'))
class CloseSlotUnitCtx(UnitRequestCtx):
    __slots__ = (b'__slotIdx', b'__isClosed')

    def __init__(self, slotIdx, isClosed=True, waitingID=b''):
        super(CloseSlotUnitCtx, self).__init__(waitingID=waitingID)
        self.__slotIdx = slotIdx
        self.__isClosed = isClosed
        return

    def getRequestType(self):
        return _REQUEST_TYPE.CLOSE_SLOT

    def getSlotIdx(self):
        return self.__slotIdx

    def isClosed(self):
        return self.__isClosed


@ReprInjector.withParent((b'__vehTypeCD', b'vTypeCD'), (b'__vehInvID', b'vehInvID'))
class SetVehicleUnitCtx(UnitRequestCtx):
    __slots__ = (b'__vehTypeCD', b'__vehInvID', b'setReady')

    def __init__(self, vTypeCD=0, vehInvID=0, waitingID=b''):
        super(SetVehicleUnitCtx, self).__init__(waitingID=waitingID)
        self.__vehTypeCD = vTypeCD
        self.__vehInvID = vehInvID
        self.setReady = False
        return

    def getRequestType(self):
        return _REQUEST_TYPE.SET_VEHICLE

    def getVehTypeCD(self):
        return self.__vehTypeCD

    def getVehInvID(self):
        return self.__vehInvID


@ReprInjector.withParent((b'__isOpened', b'isOpened'))
class ChangeOpenedUnitCtx(UnitRequestCtx):
    __slots__ = (b'__isOpened',)

    def __init__(self, isOpened, waitingID=b''):
        super(ChangeOpenedUnitCtx, self).__init__(waitingID=waitingID)
        self.__isOpened = isOpened
        return

    def getRequestType(self):
        return settings.REQUEST_TYPE.CHANGE_OPENED

    def isOpened(self):
        return self.__isOpened


@ReprInjector.withParent((b'__comment', b'comment'))
class ChangeCommentUnitCtx(UnitRequestCtx):
    __slots__ = (b'__comment',)

    def __init__(self, comment, waitingID=b''):
        super(ChangeCommentUnitCtx, self).__init__(waitingID=waitingID)
        self.__comment = truncate_utf8(comment, settings.UNIT_COMMENT_MAX_LENGTH)
        return

    def getRequestType(self):
        return _REQUEST_TYPE.CHANGE_COMMENT

    def getComment(self):
        return self.__comment

    def isCommentChanged(self, unit):
        return self.__comment != unit.getComment()


@ReprInjector.withParent((b'resetVehicle', b'resetVehicle'), (b'__isReady', b'isReady'))
class SetReadyUnitCtx(UnitRequestCtx):
    __slots__ = (b'__isReady', b'resetVehicle')

    def __init__(self, isReady=True, waitingID=b''):
        super(SetReadyUnitCtx, self).__init__(waitingID=waitingID)
        self.__isReady = isReady
        self.resetVehicle = False
        return

    def getRequestType(self):
        return _REQUEST_TYPE.SET_PLAYER_STATE

    def isReady(self):
        return self.__isReady


@ReprInjector.withParent((b'__pID', b'pID'), (b'__slotIdx', b'slotIdx'))
class AssignUnitCtx(UnitRequestCtx):
    __slots__ = (b'__pID', b'__slotIdx')

    def __init__(self, pID, slotIdx, waitingID=b''):
        super(AssignUnitCtx, self).__init__(waitingID=waitingID)
        self.__pID = pID
        self.__slotIdx = slotIdx
        return

    def getRequestType(self):
        return _REQUEST_TYPE.ASSIGN

    def getPlayerID(self):
        return self.__pID

    def getSlotIdx(self):
        return self.__slotIdx

    def isRemove(self):
        return self.__slotIdx == UNIT_SLOT.REMOVE


@ReprInjector.withParent((b'__action', b'action'), (b'__vehTypes', b'vehTypes'))
class AutoSearchUnitCtx(UnitRequestCtx):
    __slots__ = (b'__action', b'__vehTypes')

    def __init__(self, waitingID=b'', action=1, vehTypes=None):
        super(AutoSearchUnitCtx, self).__init__(waitingID=waitingID)
        self.__action = action
        self.__vehTypes = [] if vehTypes is None else vehTypes
        return

    def getRequestType(self):
        return _REQUEST_TYPE.AUTO_SEARCH

    def getAction(self):
        return self.__action

    def getActionName(self):
        if self.__action > 0:
            return b'start'
        return b'stop'

    def isRequestToStart(self):
        return self.__action > 0

    def getVehTypes(self):
        return self.__vehTypes


class AcceptSearchUnitCtx(UnitRequestCtx):
    __slots__ = ()

    def getRequestType(self):
        return _REQUEST_TYPE.ACCEPT_SEARCH


class DeclineSearchUnitCtx(UnitRequestCtx):
    __slots__ = ()

    def getRequestType(self):
        return _REQUEST_TYPE.DECLINE_SEARCH


@ReprInjector.withParent((b'selectVehInvID', b'selectVehInvID'), (b'getGamePlayMask', b'gamePlayMask'), (b'getDemoArenaTypeID', b'getDemoArenaTypeID'), (b'getRandomFlags', b'randomFlags'))
class BattleQueueUnitCtx(AutoSearchUnitCtx):
    __slots__ = (b'selectVehInvID', b'__isActionStartBattle', b'mmData')

    def __init__(self, waitingID=b'', action=1, vehTypes=None):
        super(BattleQueueUnitCtx, self).__init__(waitingID=waitingID, action=action, vehTypes=vehTypes)
        self.selectVehInvID = 0
        self.mmData = 0
        return

    def getRequestType(self):
        return _REQUEST_TYPE.BATTLE_QUEUE

    def getGamePlayMask(self):
        return gameplay_ctx.getMask()

    def getDemoArenaTypeID(self):
        return self.mmData

    def getRandomFlags(self):
        return gameplay_ctx.getRandomFlags()


class RosterSlotCtx(object):

    def __init__(self, vehTypeCD=None, nationNames=None, levels=None, vehClassNames=None):
        self.__vehTypeCD = vehTypeCD
        self.__nationNames = nationNames
        self.__vehLevels = levels
        self.__vehClassNames = vehClassNames
        return

    def getCriteria(self):
        criteria = {}
        if self.__vehTypeCD:
            criteria[b'vehTypeID'] = self.__vehTypeCD
        elif self.__nationNames:
            criteria[b'nationNames'] = self.__nationNames
        if self.__vehLevels:
            criteria[b'levels'] = self.__vehLevels
        if self.__vehClassNames:
            criteria[b'vehClassNames'] = self.__vehClassNames
        return criteria


@ReprInjector.withParent((b'__items', b'rostersSlots'))
class SetRostersSlotsUnitCtx(UnitRequestCtx):
    __slots__ = (b'__items',)

    def __init__(self, waitingID=b''):
        super(SetRostersSlotsUnitCtx, self).__init__(waitingID=waitingID)
        self.__items = {}
        return

    def getRequestType(self):
        return _REQUEST_TYPE.SET_ROSTERS_SLOTS

    def addRosterSlot(self, rosterSlotIdx, ctx):
        self.__items[rosterSlotIdx] = ctx.getCriteria()
        return

    def getRosterSlots(self):
        return self.__items.copy()


@ReprInjector.withParent((b'__databaseID', b'databaseID'))
class KickPlayerUnitCtx(UnitRequestCtx):
    __slots__ = (b'__databaseID',)

    def __init__(self, databaseID, waitingID=b''):
        super(KickPlayerUnitCtx, self).__init__(waitingID=waitingID)
        self.__databaseID = databaseID
        return

    def getRequestType(self):
        return _REQUEST_TYPE.KICK

    def getPlayerID(self):
        return self.__databaseID


@ReprInjector.withParent((b'__databaseID', b'databaseID'))
class GiveLeadershipUnitCtx(UnitRequestCtx):
    __slots__ = (b'__databaseID',)

    def __init__(self, databaseID, waitingID=b''):
        super(GiveLeadershipUnitCtx, self).__init__(waitingID=waitingID)
        self.__databaseID = databaseID
        return

    def getRequestType(self):
        return _REQUEST_TYPE.GIVE_LEADERSHIP

    def getPlayerID(self):
        return self.__databaseID


@ReprInjector.withParent((b'__division', b'division'))
class ChangeDivisionUnitCtx(UnitRequestCtx):
    __slots__ = (b'__divisionID',)

    def __init__(self, divisionID, waitingID=b''):
        super(ChangeDivisionUnitCtx, self).__init__(waitingID=waitingID)
        self.__divisionID = divisionID
        return

    def getRequestType(self):
        return _REQUEST_TYPE.CHANGE_DIVISION

    def getDivisionID(self):
        return self.__divisionID


@ReprInjector.withParent((b'__vehsList', b'vehsList'))
class SetVehiclesUnitCtx(UnitRequestCtx):
    __slots__ = (b'__vehsList',)

    def __init__(self, vehsList, waitingID=b''):
        super(SetVehiclesUnitCtx, self).__init__(waitingID=waitingID)
        self.__vehsList = vehsList
        return

    def getRequestType(self):
        return _REQUEST_TYPE.SET_VEHICLE_LIST

    def getCooldown(self):
        return 2.0

    def getVehsList(self):
        return self.__vehsList
