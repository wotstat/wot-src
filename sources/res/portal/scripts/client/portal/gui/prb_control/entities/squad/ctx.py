from gui.prb_control.entities.base.unit.ctx import UnitRequestCtx
from gui.shared.utils.decorators import ReprInjector
from portal.gui.portal_gui_constants import REQUEST_TYPE

@ReprInjector.withParent((b'_battleLevel',))
class SetUnitBattleLevelCtx(UnitRequestCtx):
    __slots__ = (b'_battleLevel',)

    def __init__(self, battleLevel, waitingID=b''):
        super(SetUnitBattleLevelCtx, self).__init__(waitinID=waitingID)
        self._battleLevel = battleLevel
        return

    def getBattleLevel(self):
        return self._battleLevel

    def getRequestType(self):
        return REQUEST_TYPE.PORTAL_SET_BATTLE_LEVEL

    def getCooldown(self):
        return 1.0
