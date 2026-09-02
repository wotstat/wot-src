from debug_utils import LOG_DEBUG_DEV
from script_component.DynamicScriptComponent import DynamicScriptComponent

class PublicHealth(DynamicScriptComponent):

    def _onAvatarReady(self):
        for healthInfo in self.healthInfoList:
            self.__setVehicleHealth(healthInfo)

        return

    def setNested_healthInfoList(self, path, prev):
        self.__setVehicleHealth(self.healthInfoList[path[0]])
        return

    def setSlice_healthInfoList(self, path, prev):
        self.__setVehicleHealth(self.healthInfoList[path[0][0]])
        return

    def __setVehicleHealth(self, healthInfo):
        LOG_DEBUG_DEV(b'[PublicHealth] __setVehicleHealth', healthInfo)
        guiSessionProvider = self.entity.sessionProvider
        guiSessionProvider.setVehicleHealth(False, healthInfo.vehicleID, healthInfo.health, 0, 0)
        return
