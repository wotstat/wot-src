from __future__ import absolute_import
from gui.prb_control.entities.base.squad.ctx import SquadSettingsCtx
from gui.prb_control.entities.base.unit.ctx import UnitRequestCtx
from gui.shared.utils.decorators import ReprInjector
from last_stand.gui.ls_gui_constants import FUNCTIONAL_FLAG
from last_stand_common.last_stand_constants import PREBATTLE_TYPE

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
class LastStandSquadSettingsCtx(SquadSettingsCtx):
    __slots__ = (b'_arenaUniqueID',)

    def __init__(self, entityType=PREBATTLE_TYPE.LAST_STAND, waitingID=b'', flags=FUNCTIONAL_FLAG.LAST_STAND, accountsToInvite=None, isForced=False, arenaUniqueID=None):
        super(LastStandSquadSettingsCtx, self).__init__(entityType=entityType, waitingID=waitingID, flags=flags, accountsToInvite=accountsToInvite, isForced=isForced)
        self._arenaUniqueID = arenaUniqueID
        return

    def getArenaUniqueID(self):
        return self._arenaUniqueID
