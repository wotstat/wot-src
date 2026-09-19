from __future__ import absolute_import
from gui.prb_control.entities.base.squad.ctx import SquadSettingsCtx
from gui.prb_control.entities.base.unit.ctx import UnitRequestCtx
from gui.shared.utils.decorators import ReprInjector
from halloween.gui.halloween_gui_constants import FUNCTIONAL_FLAG
from halloween_common.halloween_constants import PREBATTLE_TYPE

@ReprInjector.withParent((b'_queueType',))
class SetDifficultyLevelUnitCtx(UnitRequestCtx):
    __slots__ = (b'_queueType',)

    def __init__(self, queueType, waitingID=b''):
        super(SetDifficultyLevelUnitCtx, self).__init__(waitingID=waitingID)
        self._queueType = queueType
        return

    def getQueueType(self):
        return self._queueType


@ReprInjector.withParent((b'getArenaUniqueID', b'_arenaUniqueID'))
class HalloweenSquadSettingsCtx(SquadSettingsCtx):
    __slots__ = (b'_arenaUniqueID',)

    def __init__(self, entityType=PREBATTLE_TYPE.HALLOWEEN, waitingID=b'', flags=FUNCTIONAL_FLAG.HALLOWEEN, accountsToInvite=None, isForced=False, arenaUniqueID=None):
        super(HalloweenSquadSettingsCtx, self).__init__(entityType=entityType, waitingID=waitingID, flags=flags, accountsToInvite=accountsToInvite, isForced=isForced)
        self._arenaUniqueID = arenaUniqueID
        return

    def getArenaUniqueID(self):
        return self._arenaUniqueID
