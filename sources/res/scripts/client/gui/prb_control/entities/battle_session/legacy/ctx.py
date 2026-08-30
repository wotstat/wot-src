from CurrentVehicle import g_currentVehicle
from constants import OBSERVER_VEH_INVENTORY_ID, OBSERVER_VEH_NAME, ARENA_BONUS_TYPE
from gui.prb_control.entities.base.legacy.ctx import JoinLegacyCtx, SetPlayerStateCtx
from gui.prb_control.prb_getters import getPrebattleSettings
from gui.prb_control.settings import FUNCTIONAL_FLAG
from gui.shared.utils.decorators import ReprInjector

@ReprInjector.withParent((b'getID', b'prbID'), (b'getPrbTypeName', b'type'), (b'getPrbClusterId', b'prbClusterID'), (b'getWaitingID', b'waitingID'))
class JoinBattleSessionCtx(JoinLegacyCtx):
    __slots__ = ()

    def __init__(self, prbID, prbType, prbClusterID, waitingID=b'', flags=FUNCTIONAL_FLAG.UNDEFINED):
        super(JoinBattleSessionCtx, self).__init__(prbID, prbType, prbClusterID, waitingID=waitingID, flags=flags)
        return


class BattleSessionSetPlayerStateCtx(SetPlayerStateCtx):

    def getVehicleInventoryID(self):
        bonusType = getPrebattleSettings()[b'bonusType']
        if g_currentVehicle.item.name == OBSERVER_VEH_NAME and bonusType == ARENA_BONUS_TYPE.TOURNAMENT_COMP7:
            return OBSERVER_VEH_INVENTORY_ID
        return super(BattleSessionSetPlayerStateCtx, self).getVehicleInventoryID()
