from gui.prb_control.entities.base.legacy.ctx import JoinLegacyCtx
from gui.prb_control.settings import FUNCTIONAL_FLAG
from gui.shared.utils.decorators import ReprInjector

@ReprInjector.withParent((b'getID', b'prbID'), (b'getPrbTypeName', b'type'), (b'getWaitingID', b'waitingID'))
class JoinBattleSessionCtx(JoinLegacyCtx):
    __slots__ = ()

    def __init__(self, prbID, prbType, waitingID=b'', flags=FUNCTIONAL_FLAG.UNDEFINED):
        super(JoinBattleSessionCtx, self).__init__(prbID, prbType, waitingID=waitingID, flags=flags)
        return
