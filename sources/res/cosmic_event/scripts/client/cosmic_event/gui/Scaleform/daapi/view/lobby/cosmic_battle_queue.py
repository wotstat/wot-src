from gui.Scaleform.daapi.view.lobby.battle_queue import RandomQueueProvider

class CosmicEventQueueProvider(RandomQueueProvider):

    def processQueueInfo(self, qInfo):
        self._proxy.setPlayersTypeCDs(qInfo.get(b'vehTypeCompDescrs', {}))
        self._proxy.setSelectedVehicle()
        return

    def _createCommonPlayerString(self, playerCount):
        return
