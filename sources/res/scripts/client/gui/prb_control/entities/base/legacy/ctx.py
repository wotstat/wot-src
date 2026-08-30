from CurrentVehicle import g_currentVehicle
from constants import ARENA_BONUS_TYPE, PREBATTLE_COMMENT_MAX_LENGTH
from external_strings_utils import truncate_utf8
from gui.prb_control import prb_getters
from gui.prb_control import settings as prb_settings
from gui.prb_control.entities.base.ctx import PrbCtrlRequestCtx
from gui.prb_control.settings import CTRL_ENTITY_TYPE
from gui.shared.utils.decorators import ReprInjector
_REQUEST_TYPE = prb_settings.REQUEST_TYPE
_CTRL_ENTITY_TYPE = prb_settings.CTRL_ENTITY_TYPE
_FUNCTIONAL_FLAG = prb_settings.FUNCTIONAL_FLAG

class LegacyRequestCtx(PrbCtrlRequestCtx):
    __slots__ = ()

    def __init__(self, **kwargs):
        super(LegacyRequestCtx, self).__init__(ctrlType=CTRL_ENTITY_TYPE.LEGACY, **kwargs)
        return

    def getPrbTypeName(self):
        return prb_getters.getPrebattleTypeName(self.getEntityType())


@ReprInjector.withParent((b'isOpened', b'isOpened'), (b'getComment', b'comment'))
class TeamSettingsCtx(LegacyRequestCtx):
    __slots__ = (b'__isOpened', b'__comment', b'_isRequestToCreate')

    def __init__(self, prbType, waitingID=b'', isOpened=True, comment=b'', isRequestToCreate=True, flags=_FUNCTIONAL_FLAG.UNDEFINED):
        super(TeamSettingsCtx, self).__init__(entityType=prbType, waitingID=waitingID, flags=flags)
        self.__isOpened = isOpened
        self.__comment = truncate_utf8(comment, PREBATTLE_COMMENT_MAX_LENGTH)
        self._isRequestToCreate = isRequestToCreate
        return

    def getRequestType(self):
        if self._isRequestToCreate:
            return _REQUEST_TYPE.CREATE
        return _REQUEST_TYPE.CHANGE_SETTINGS

    def isOpened(self):
        return self.__isOpened

    def setOpened(self, isOpened):
        self.__isOpened = isOpened
        return

    def getComment(self):
        return self.__comment

    def setComment(self, comment):
        self.__comment = truncate_utf8(comment, PREBATTLE_COMMENT_MAX_LENGTH)
        return

    def isOpenedChanged(self, settings):
        return self.__isOpened != settings[prb_settings.PREBATTLE_SETTING_NAME.IS_OPENED]

    def isCommentChanged(self, settings):
        return self.__comment != settings[prb_settings.PREBATTLE_SETTING_NAME.COMMENT]

    def areSettingsChanged(self, settings):
        return self.isOpenedChanged(settings) or self.isCommentChanged(settings)


@ReprInjector.withParent((b'__prbID', b'id'), (b'__prbType', b'type'))
class JoinLegacyCtx(LegacyRequestCtx):
    __slots__ = (b'__prbID',)

    def __init__(self, prbID, prbType, waitingID=b'', flags=_FUNCTIONAL_FLAG.UNDEFINED):
        super(JoinLegacyCtx, self).__init__(entityType=int(prbType), waitingID=waitingID, flags=flags)
        self.__prbID = int(prbID)
        return

    def getID(self):
        return self.__prbID

    def getRequestType(self):
        return _REQUEST_TYPE.JOIN

    def getBonusType(self):
        return ARENA_BONUS_TYPE.UNKNOWN


@ReprInjector.withParent((b'getID', b'prbID'), (b'getPrbTypeName', b'prbType'), (b'getWaitingID', b'waitingID'), (b'getFlagsToStrings', b'flags'))
class LeaveLegacyCtx(LegacyRequestCtx):
    __slots__ = ()

    def getID(self):
        return prb_getters.getPrebattleID()

    def getRequestType(self):
        return _REQUEST_TYPE.LEAVE


@ReprInjector.withParent((b'__pID', b'pID'), (b'__roster', b'roster'), (b'getPrbTypeName', b'prbType'), (b'getWaitingID', b'waitingID'))
class AssignLegacyCtx(LegacyRequestCtx):
    __slots__ = (b'__pID', b'__roster', b'__errorString')

    def __init__(self, pID, roster, waitingID=b''):
        super(AssignLegacyCtx, self).__init__(entityType=prb_getters.getPrebattleType(), waitingID=waitingID)
        self.__pID = pID
        self.__roster = roster
        self.__errorString = b''
        return

    def getPlayerID(self):
        return self.__pID

    def getRoster(self):
        return self.__roster

    def getLastErrorString(self):
        return self.__errorString

    def getRequestType(self):
        return _REQUEST_TYPE.ASSIGN

    def setErrorString(self, errorString):
        self.__errorString = errorString
        return

    def onResponseReceived(self, code, errorStr=b''):
        self.__errorString = errorStr
        super(AssignLegacyCtx, self).onResponseReceived(code)
        return


@ReprInjector.withParent((b'__roster', b'roster'), (b'__fromLane', b'fromLane'), (b'__toLane', b'toLane'), (b'getPrbTypeName', b'prbType'), (b'getWaitingID', b'waitingID'))
class GroupSwapInTeamLegacyCtx(LegacyRequestCtx):
    __slots__ = (b'__roster', b'__fromLane', b'__toLane')

    def __init__(self, roster, fLane, tLane, waitingID=b''):
        super(GroupSwapInTeamLegacyCtx, self).__init__(entityType=prb_getters.getPrebattleType(), waitingID=waitingID)
        self.__roster = roster
        self.__fromLane = fLane
        self.__toLane = tLane
        return

    def getRoster(self):
        return self.__roster

    def getGroups(self):
        return (
         self.__fromLane, self.__toLane)

    def getRequestType(self):
        return _REQUEST_TYPE.EPIC_SWAP_IN_TEAM


@ReprInjector.withParent((b'__lane', b'toLane'), (b'getPrbTypeName', b'prbType'), (b'getWaitingID', b'waitingID'))
class GroupSwapBetweenTeamLegacyCtx(LegacyRequestCtx):
    __slots__ = (b'__lane',)

    def __init__(self, lane, waitingID=b''):
        super(GroupSwapBetweenTeamLegacyCtx, self).__init__(entityType=prb_getters.getPrebattleType(), waitingID=waitingID)
        self.__lane = lane
        return

    def getGroup(self):
        return self.__lane

    def getRequestType(self):
        return _REQUEST_TYPE.EPIC_SWAP_BETWEEN_TEAM


@ReprInjector.withParent((b'__pID', b'pID'), (b'__roster', b'roster'), (b'__group', b'group'), (b'getPrbTypeName', b'prbType'), (b'getWaitingID', b'waitingID'))
class GroupAssignLegacyCtx(LegacyRequestCtx):
    __slots__ = (b'__pID', b'__roster', b'__group')

    def __init__(self, pID, roster, group, waitingID=b''):
        super(GroupAssignLegacyCtx, self).__init__(entityType=prb_getters.getPrebattleType(), waitingID=waitingID)
        self.__group = group
        self.__pID = pID
        self.__roster = roster
        return

    def getPlayerID(self):
        return self.__pID

    def getRoster(self):
        return self.__roster

    def getRequestType(self):
        return _REQUEST_TYPE.ASSIGN

    def getGroup(self):
        return self.__group


@ReprInjector.withParent((b'__team', b'team'), (b'__isReadyState', b'isReadyState'), b'getPrbTypeName', (b'getWaitingID', b'waitingID'), (b'__isForced', b'isForced'), (b'__gamePlayMask', b'gamePlayMask'))
class SetTeamStateCtx(LegacyRequestCtx):
    __slots__ = (b'__team', b'__isReadyState', b'__gamePlayMask')

    def __init__(self, team, isReadyState, waitingID=b'', isForced=True, gamePlayMask=0):
        super(SetTeamStateCtx, self).__init__(entityType=prb_getters.getPrebattleType(), waitingID=waitingID, isForced=isForced)
        self.__team = team
        self.__isReadyState = isReadyState
        self.__gamePlayMask = gamePlayMask
        return

    def getTeam(self):
        return self.__team

    def isReadyState(self):
        return self.__isReadyState

    def getGamePlayMask(self):
        return self.__gamePlayMask

    def getRequestType(self):
        return _REQUEST_TYPE.SET_TEAM_STATE


@ReprInjector.withParent((b'getVehicleInventoryID', b'vInventoryID'), (b'__isReadyState', b'isReadyState'), (b'__isInitial', b'isInitial'), (b'getWaitingID', b'waitingID'))
class SetPlayerStateCtx(LegacyRequestCtx):
    __slots__ = (b'__isReadyState', b'__isInitial', b'__errorString')

    def __init__(self, isReadyState, isInitial=False, waitingID=b''):
        super(SetPlayerStateCtx, self).__init__(entityType=prb_getters.getPrebattleType(), waitingID=waitingID)
        self.__isReadyState = isReadyState
        self.__isInitial = isInitial
        self.__errorString = b''
        return

    def doVehicleValidation(self):
        return True

    def isReadyState(self):
        return self.__isReadyState

    def isInitial(self):
        return self.__isInitial

    def getRequestType(self):
        return _REQUEST_TYPE.SET_PLAYER_STATE

    def getVehicleInventoryID(self):
        return g_currentVehicle.invID

    def getLastErrorString(self):
        return self.__errorString

    def setErrorString(self, errorString):
        self.__errorString = errorString
        return

    def onResponseReceived(self, code, errorStr=b''):
        self.__errorString = errorStr
        super(SetPlayerStateCtx, self).onResponseReceived(code)
        return


class SwapTeamsCtx(LegacyRequestCtx):
    __slots__ = ()

    def __init__(self, **kwargs):
        super(SwapTeamsCtx, self).__init__(entityType=prb_getters.getPrebattleType(), **kwargs)
        return

    def getRequestType(self):
        return _REQUEST_TYPE.SWAP_TEAMS


@ReprInjector.withParent((b'__isOpened', b'isOpened'), (b'getWaitingID', b'waitingID'))
class ChangeOpenedCtx(LegacyRequestCtx):
    __slots__ = (b'__isOpened',)

    def __init__(self, isOpened, waitingID=b''):
        super(ChangeOpenedCtx, self).__init__(entityType=prb_getters.getPrebattleType(), waitingID=waitingID)
        self.__isOpened = isOpened
        return

    def isOpened(self):
        return self.__isOpened

    def isOpenedChanged(self, settings):
        return self.__isOpened != settings[prb_settings.PREBATTLE_SETTING_NAME.IS_OPENED]

    def getRequestType(self):
        return _REQUEST_TYPE.CHANGE_OPENED


@ReprInjector.withParent((b'__comment', b'comment'), (b'getWaitingID', b'waitingID'))
class ChangeCommentCtx(LegacyRequestCtx):
    __slots__ = (b'__comment',)

    def __init__(self, comment, waitingID=b''):
        super(ChangeCommentCtx, self).__init__(entityType=prb_getters.getPrebattleType(), waitingID=waitingID)
        self.__comment = truncate_utf8(comment, PREBATTLE_COMMENT_MAX_LENGTH)
        return

    def getComment(self):
        return self.__comment

    def isCommentChanged(self, settings):
        return self.__comment != settings[prb_settings.PREBATTLE_SETTING_NAME.COMMENT]

    def getRequestType(self):
        return _REQUEST_TYPE.CHANGE_COMMENT


@ReprInjector.withParent((b'__division', b'division'), (b'getWaitingID', b'waitingID'))
class ChangeDivisionCtx(LegacyRequestCtx):
    __slots__ = (b'__division',)

    def __init__(self, division, waitingID=b''):
        super(ChangeDivisionCtx, self).__init__(entityType=prb_getters.getPrebattleType(), waitingID=waitingID)
        self.__division = int(division)
        return

    def getDivision(self):
        return self.__division

    def isDivisionChanged(self, settings):
        return self.__division != settings[prb_settings.PREBATTLE_SETTING_NAME.DIVISION]

    def getRequestType(self):
        return _REQUEST_TYPE.CHANGE_DIVISION


@ReprInjector.withParent((b'__pID', b'pID'))
class KickPlayerCtx(LegacyRequestCtx):
    __slots__ = (b'__pID',)

    def __init__(self, pID, waitingID=b''):
        super(KickPlayerCtx, self).__init__(entityType=prb_getters.getPrebattleType(), waitingID=waitingID)
        self.__pID = pID
        return

    def getPlayerID(self):
        return self.__pID

    def getRequestType(self):
        return _REQUEST_TYPE.KICK


@ReprInjector.withParent((b'__prbID', b'prbID'), (b'getWaitingID', b'waitingID'))
class GetLegacyRosterCtx(LegacyRequestCtx):
    __slots__ = (b'__prbID',)

    def __init__(self, prbID, prbType, waitingID=b''):
        super(GetLegacyRosterCtx, self).__init__(entityType=prbType, waitingID=waitingID)
        self.__prbID = prbID
        return

    def getPrbID(self):
        return self.__prbID

    def getRequestType(self):
        return _REQUEST_TYPE.GET_ROSTER


class JoinLegacyModeCtx(LegacyRequestCtx):
    __slots__ = ()

    def __init__(self, prbType, waitingID=b'', flags=_FUNCTIONAL_FLAG.UNDEFINED):
        super(JoinLegacyModeCtx, self).__init__(entityType=prbType, waitingID=waitingID, flags=flags)
        return

    def getID(self):
        return 0

    def getBonusType(self):
        return ARENA_BONUS_TYPE.UNKNOWN
