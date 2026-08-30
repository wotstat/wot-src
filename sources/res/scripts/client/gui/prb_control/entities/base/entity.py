import typing
from adisp import adisp_process
from constants import QUEUE_TYPE
from debug_utils import LOG_ERROR
from gui.prb_control.entities.base.actions_validator import IActionsValidator
from gui.prb_control.entities.base.actions_validator import NotSupportedActionsValidator, BaseActionsValidator
from gui.prb_control.entities.base.permissions import IPrbPermissions
from gui.prb_control.entities.base.scheduler import BaseScheduler
from gui.prb_control.events_dispatcher import g_eventDispatcher
from gui.prb_control.items import SelectResult, ValidationResult
from gui.prb_control.settings import FUNCTIONAL_FLAG, CTRL_ENTITY_TYPE
from gui.shared.utils.listeners_collection import IListenersCollection
if typing.TYPE_CHECKING:
    from gui.prb_control.entities.base.ctx import PrbAction, PrbCtrlRequestCtx
    from gui.prb_control.entities.base.cooldown import PrbCooldownManager
    from gui.Scaleform.daapi.view.dialogs import IDialogMeta

class PrbFunctionalFlags(object):
    __slots__ = (b'_entityFlags', b'_modeFlags')

    def __init__(self, entityFlags, modeFlags, **kwargs):
        super(PrbFunctionalFlags, self).__init__()
        self._entityFlags = entityFlags
        self._modeFlags = modeFlags
        return

    def getModeFlags(self):
        return self._modeFlags

    def getEntityFlags(self):
        return self._entityFlags

    def getFunctionalFlags(self):
        return self._modeFlags | self._entityFlags


class BasePrbEntryPoint(PrbFunctionalFlags):

    def isVisualOnly(self):
        return False

    def makeDefCtx(self):
        return

    def create(self, ctx, callback=None):
        return

    def canCreate(self):
        return True

    def join(self, ctx, callback=None):
        return

    def canJoin(self):
        return True

    def select(self, ctx, callback=None):
        return

    def setExtData(self, extData):
        return

    def setAccountsToInvite(self, accountsToInvite):
        return

    def setKeepCurrentView(self, keepCurrentView):
        return

    def configure(self, action):
        self.setAccountsToInvite(action.accountsToInvite)
        self.setExtData(action.extData)
        return


class BasePrbEntity(IActionsValidator, PrbFunctionalFlags):

    def __init__(self, entityFlags, modeFlags):
        super(BasePrbEntity, self).__init__(entityFlags=entityFlags, modeFlags=modeFlags)
        self._actionsValidator = self._createActionsValidator()
        self._scheduler = self._createScheduler()
        self._isActive = False
        self._cooldown = self._createCooldownManager()
        return

    def init(self, **kwargs):
        self._scheduler.init()
        self._isActive = True
        return FUNCTIONAL_FLAG.UNDEFINED

    def fini(self, **kwargs):
        self._scheduler.fini()
        self._isActive = False
        return FUNCTIONAL_FLAG.UNDEFINED

    def invalidate(self):
        return

    def restore(self):
        return

    def rejoin(self):
        return

    def canSwitch(self, ctx):
        flags = self.getModeFlags()
        return ctx is not None and flags & FUNCTIONAL_FLAG.MODES_BITMASK > 0 and ctx.hasFlags(flags)

    def isActive(self):
        return self._isActive

    def isPlayerJoined(self, ctx):
        return False

    def canInvite(self, prbType):
        return True

    def isInQueue(self):
        return False

    def canKeepMode(self):
        return True

    def resetPlayerState(self):
        return

    def canPlayerDoAction(self):
        return self._actionsValidator.canPlayerDoAction() or ValidationResult()

    def doAction(self, action=None):
        return False

    def doSelectAction(self, action):
        return SelectResult()

    def showGUI(self, ctx=None):
        return False

    def getConfirmDialogMeta(self, ctx):
        return

    def showDialog(self, meta, callback, parent=None):
        self.__showDefaultDialog(meta, callback, parent=parent)
        return

    def getID(self):
        return 0

    def getCtrlType(self):
        return CTRL_ENTITY_TYPE.UNKNOWN

    def getEntityType(self):
        return 0

    def getIntroType(self):
        return 0

    def getRequestCtx(self):
        return

    def getQueueType(self):
        return QUEUE_TYPE.UNKNOWN

    def hasLockedState(self):
        return False

    def getPermissions(self, pID=None, **kwargs):
        return IPrbPermissions()

    def isCommander(self, dbID=None):
        return False

    def leave(self, ctx, callback=None):
        return

    def request(self, ctx, callback=None):
        return

    def isInCoolDown(self, requestType):
        return self._cooldown and self._cooldown.isInProcess(requestType)

    def setCoolDown(self, requestType, coolDown):
        if self._cooldown:
            self._cooldown.process(requestType, coolDown=coolDown)
        return

    def resetCoolDown(self, requestType):
        if self._cooldown:
            self._cooldown.reset(requestType)
        return

    def canDoActionWithoutVehicle(self):
        return False

    def _createActionsValidator(self):
        return BaseActionsValidator(self)

    def _createScheduler(self):
        return BaseScheduler(self)

    def _createCooldownManager(self):
        return

    def _goToHangar(self):
        g_eventDispatcher.loadHangar()
        return

    @adisp_process
    def __showDefaultDialog(self, meta, callback, parent=None):
        from gui import DialogsInterface
        result = yield DialogsInterface.showDialog(meta, parent=parent)
        if callback is not None:
            callback(result)
        return


class NotSupportedEntryPoint(BasePrbEntryPoint):

    def __init__(self):
        super(NotSupportedEntryPoint, self).__init__(entityFlags=FUNCTIONAL_FLAG.UNDEFINED, modeFlags=FUNCTIONAL_FLAG.UNDEFINED)
        return

    def create(self, ctx, callback=None):
        LOG_ERROR(b'NotSupportedEntry.create', ctx)
        return

    def join(self, ctx, callback=None):
        LOG_ERROR(b'NotSupportedEntry.join', ctx)
        return


class NotSupportedEntity(BasePrbEntity, IListenersCollection):

    def __init__(self):
        super(NotSupportedEntity, self).__init__(entityFlags=FUNCTIONAL_FLAG.UNDEFINED, modeFlags=FUNCTIONAL_FLAG.UNDEFINED)
        return

    def _createActionsValidator(self):
        return NotSupportedActionsValidator()

    def _goToHangar(self):
        return
