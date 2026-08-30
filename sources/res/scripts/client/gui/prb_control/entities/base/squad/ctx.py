from constants import PREBATTLE_TYPE
from gui.prb_control import settings as prb_settings
from gui.prb_control.entities.base.unit.ctx import UnitRequestCtx
from gui.shared.utils.decorators import ReprInjector

@ReprInjector.withParent((b'getWaitingID', b'waitingID'), (b'getFlagsToStrings', b'flags'))
class SquadSettingsCtx(UnitRequestCtx):
    __slots__ = (b'__accountsToInvite',)

    def __init__(self, entityType=PREBATTLE_TYPE.SQUAD, waitingID=b'', flags=prb_settings.FUNCTIONAL_FLAG.UNDEFINED, accountsToInvite=None, isForced=False):
        super(SquadSettingsCtx, self).__init__(entityType=entityType, waitingID=waitingID, flags=flags, isForced=isForced)
        self.__accountsToInvite = accountsToInvite or []
        return

    def getRequestType(self):
        return prb_settings.REQUEST_TYPE.CREATE

    def getID(self):
        return 0

    def getAccountsToInvite(self):
        return self.__accountsToInvite
