import typing
from external_strings_utils import truncate_utf8
from gui.prb_control.settings import FUNCTIONAL_FLAG, CTRL_ENTITY_TYPE, convertFlagsToNames, CTRL_ENTITY_TYPE_NAMES, INVITE_COMMENT_MAX_LENGTH, REQUEST_TYPE
from gui.shared.utils.decorators import ReprInjector
from gui.shared.utils.requesters import RequestCtx

@ReprInjector.withParent((b'getCtrlTypeName', b'ctrlType'), (b'getEntityType', b'entityType'), (b'getWaitingID', b'waitingID'), (b'getFlagsToStrings', b'flags'), (b'isForced', b'forced'))
class PrbCtrlRequestCtx(RequestCtx):
    __slots__ = (b'__ctrlType', b'__entityType', b'__entityID', b'__isForced', b'__flags')

    def __init__(self, **kwargs):
        waitingID = kwargs.get(b'waitingID', b'')
        super(PrbCtrlRequestCtx, self).__init__(waitingID)
        if b'ctrlType' in kwargs:
            self.__ctrlType = kwargs[b'ctrlType']
        else:
            self.__ctrlType = CTRL_ENTITY_TYPE.UNKNOWN
        self.__entityType = kwargs.get(b'entityType', 0)
        self.__entityID = kwargs.get(b'entityID', 0)
        self.__isForced = kwargs.get(b'isForced', False)
        self.__flags = kwargs.get(b'flags', FUNCTIONAL_FLAG.UNDEFINED)
        return

    def getCtrlType(self):
        return self.__ctrlType

    def getCtrlTypeName(self):
        if self.__ctrlType in CTRL_ENTITY_TYPE_NAMES:
            return CTRL_ENTITY_TYPE_NAMES[self.__ctrlType]
        return (b'CTRL_ENTITY_TYPE_{}').format(self.__ctrlType)

    def getEntityType(self):
        return self.__entityType

    def getEnityID(self):
        return self.__entityID

    def setForced(self, flag):
        self.__isForced = flag
        return

    def isForced(self):
        return self.__isForced

    def getFlags(self):
        return self.__flags

    def addFlags(self, flags):
        self.__flags |= flags
        return

    def hasFlags(self, flags):
        return self.__flags & flags == flags

    def removeFlags(self, flags):
        result = self.__flags & flags
        if result:
            self.__flags ^= result
        return

    def clearFlags(self):
        self.__flags = FUNCTIONAL_FLAG.UNDEFINED
        return

    def getFlagsToStrings(self):
        return (b', ').join(convertFlagsToNames(self.__flags))


@ReprInjector.simple(b'actionName', b'mmData', b'accountsToInvite', b'extData')
class PrbAction(object):
    __slots__ = (b'actionName', b'mmData', b'accountsToInvite', b'extData')

    def __init__(self, actionName, mmData=0, accountsToInvite=None, extData=None):
        self.actionName = actionName if actionName is not None else b''
        self.mmData = mmData
        self.accountsToInvite = accountsToInvite or ()
        self.extData = extData or {}
        return


@ReprInjector.simple(b'isExit')
class LeavePrbAction(object):
    __slots__ = (b'isExit', b'ignoreConfirmation', b'parent')

    def __init__(self, isExit=True, ignoreConfirmation=False, parent=None):
        self.isExit = isExit
        self.ignoreConfirmation = ignoreConfirmation
        self.parent = parent
        return


@ReprInjector.withParent((b'getDatabaseIDs', b'databaseIDs'), (b'getComment', b'comment'))
class SendInvitesCtx(PrbCtrlRequestCtx):

    def __init__(self, databaseIDs, comment, waitingID=b''):
        super(SendInvitesCtx, self).__init__(waitingID=waitingID)
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


class CreatePrbEntityCtx(PrbCtrlRequestCtx):
    __slots__ = (b'__initCtx',)

    def __init__(self, ctrlType=CTRL_ENTITY_TYPE.UNKNOWN, entityType=0, flags=FUNCTIONAL_FLAG.UNDEFINED, initCtx=None):
        super(CreatePrbEntityCtx, self).__init__(ctrlType=ctrlType, entityType=entityType, flags=flags)
        self.__initCtx = initCtx
        return

    def getInitCtx(self):
        return self.__initCtx

    def clear(self):
        self.__initCtx = None
        super(CreatePrbEntityCtx, self).clear()
        return
