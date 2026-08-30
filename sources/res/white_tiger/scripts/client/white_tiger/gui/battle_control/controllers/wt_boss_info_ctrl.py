from helpers import dependency
from gui.battle_control.arena_info.interfaces import IArenaVehiclesController
from gui.battle_control.battle_constants import BATTLE_CTRL_ID
from gui.battle_control.view_components import ViewComponentsController
from skeletons.gui.battle_session import IBattleSessionProvider
from wt_settings import g_wt_config

class WTBossInfoController(ViewComponentsController, IArenaVehiclesController):
    __sessionProvider = dependency.descriptor(IBattleSessionProvider)

    def getControllerID(self):
        return BATTLE_CTRL_ID.BOSS_INFO_CTRL

    def startControl(self, *_):
        return

    def stopControl(self):
        return

    def setViewComponents(self, *components):
        super(WTBossInfoController, self).setViewComponents(*components)
        arenaDP = self.__sessionProvider.getArenaDP()
        for vInfo in arenaDP.getVehiclesInfoIterator():
            vehCD = vInfo.vehicleType.compactDescr
            if g_wt_config.isAnyTypeBoss(vehCD):
                self.__setupBossInfo(vInfo)
                break

        return

    def addVehicleInfo(self, vInfo, _):
        vehCD = vInfo.vehicleType.compactDescr
        if g_wt_config.isAnyTypeBoss(vehCD):
            self.__setupBossInfo(vInfo)
        return

    def invalidateVehiclesStats(self, arenaDP):
        for vInfo in arenaDP.getVehiclesInfoIterator():
            vehCD = vInfo.vehicleType.compactDescr
            if g_wt_config.isAnyTypeBoss(vehCD):
                self.__updateBossInfo(vInfo)
                break

        return

    def updateVehiclesStats(self, updated, arenaDP):
        for _, vStatsVO in updated:
            vInfo = arenaDP.getVehicleInfo(vStatsVO.vehicleID)
            vehCD = vInfo.vehicleType.compactDescr
            if g_wt_config.isAnyTypeBoss(vehCD):
                self.__updateBossInfo(vInfo)

        return

    def __setupBossInfo(self, bossInfo):
        for component in self._viewComponents:
            component.setupBossInfo(bossInfo)

        return

    def __updateBossInfo(self, bossInfo):
        for component in self._viewComponents:
            component.updateBossInfo(bossInfo)

        return
