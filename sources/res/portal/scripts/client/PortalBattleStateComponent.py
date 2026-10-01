from cache import cached_property
import Event
from script_component.DynamicScriptComponent import DynamicScriptComponent
from CampReplicableComponent import CampReplicableComponent
from portal_common.portal_constants import BattleState

class PortalBattleStateComponent(DynamicScriptComponent):
    onBattleStateChanged = Event.Event()
    onBattleFinishTimeChanged = Event.Event()
    onBotVehiclePreparing = Event.Event()
    onWaveStarted = Event.Event()
    onWavesBuffed = Event.Event()
    onLaneInfoChanged = Event.Event()
    onAllCampsInited = Event.Event()
    onCampInfoUpdated = Event.Event()
    onCampCanBeCaptured = Event.Event()
    onCampCaptured = Event.Event()
    onCampCapturing = Event.Event()
    onCampStopCapturing = Event.Event()
    onAllBossesInited = Event.Event()
    onBossInfoUpdated = Event.Event()
    onBossFightFinished = Event.Event()
    onCampCaptureHealApplied = Event.Event()

    def __init__(self):
        super(PortalBattleStateComponent, self).__init__()
        CampReplicableComponent.onCapturing += self.__onCampCapturing
        CampReplicableComponent.onStopCapturing += self.__onCampStopCapturing
        CampReplicableComponent.onCanBeCaptured += self.__onCampCanBeCaptured
        CampReplicableComponent.onCaptured += self.__onCampCaptured
        return

    def onDestroy(self):
        CampReplicableComponent.onCapturing -= self.__onCampCapturing
        CampReplicableComponent.onStopCapturing -= self.__onCampStopCapturing
        CampReplicableComponent.onCanBeCaptured -= self.__onCampCanBeCaptured
        CampReplicableComponent.onCaptured -= self.__onCampCaptured
        super(PortalBattleStateComponent, self).onDestroy()
        return

    def _onAvatarReady(self):
        super(PortalBattleStateComponent, self)._onAvatarReady()
        if self.battleState and self.battleState != BattleState.OUT_OF_BATTLE:
            self.onBattleStateChanged(self.battleState)
        return

    def set_battleEvent(self, _):
        name = self.battleEvent.eventName
        handler = getattr(self, (b'_{}__on{}').format(self.__class__.__name__, name), None)
        if handler:
            kwargs = self.battleEvent.kwargs
            handler(**kwargs)
        return

    def set_campInfo(self, _):
        self.onAllCampsInited()
        return

    def setNested_campInfo(self, changePath, oldValue):
        index = changePath[0]
        info = self.campInfo[index]
        campName = info.campName
        self.onCampInfoUpdated(campName)
        return

    def set_bossInfo(self, _):
        self.onAllBossesInited()
        return

    def setNested_bossInfo(self, changePath, oldValue):
        index = changePath[0]
        info = self.bossInfo[index]
        bossID = info.bossID
        self.onBossInfoUpdated(bossID)
        return

    def set_battleState(self, prev):
        self.onBattleStateChanged(self.battleState)
        return

    def set_battleFinishTime(self, _):
        self.onBattleFinishTimeChanged(self.battleFinishTime)
        return

    def set_currentWave(self, _):
        self.onWaveStarted(self.currentWave, self.wavesCount)
        return

    def set_wavesBuffed(self, _):
        self.onWavesBuffed(self.wavesBuffed)
        return

    def setSlice_lanesInfo(self, changePath, _):
        index = changePath[0]
        laneInfo = self.lanesInfo[index]
        self.onLaneInfoChanged(index + 1, laneInfo)
        return

    def getLanesInfo(self):
        return {laneIndex: laneInfo for laneIndex, laneInfo in enumerate(self.lanesInfo, start=1)}

    def isAllCampsCaptured(self):
        return all(info[b'status'] for info in self.campInfo)

    def getCampsCount(self):
        return len(self.campInfo)

    def getCapturedCampsCount(self):
        return sum(info[b'status'] for info in self.campInfo)

    def getCampFrontier(self, campName):
        frontiers = self.__config[b'campsSettings'][b'frontiers']
        for frontier, frontierInfo in frontiers.iteritems():
            if campName in frontierInfo[b'camps']:
                return frontier

        return

    def getTeleportFrontier(self, teleportName):
        campTeleports = self.__config[b'teleportSettings'][b'campTeleports']
        campName = campTeleports.get(teleportName)
        return self.getCampFrontier(campName)

    def areWavesEnded(self):
        if self.currentWave == 0:
            return False
        if self.currentWave != self.wavesCount:
            return False
        return sum([len(laneInfo) for laneInfo in self.lanesInfo]) == 0

    def __onBotVehiclePreparing(self, spawnData):
        self.onBotVehiclePreparing(spawnData)
        return

    def __onBossFightFinished(self):
        self.onBossFightFinished()
        return

    def __onCampCapturing(self, info):
        self.onCampCapturing(info)
        return

    def __onCampStopCapturing(self, campGO):
        self.onCampStopCapturing(campGO)
        return

    def __onCampCanBeCaptured(self, campGO):
        self.onCampCanBeCaptured(campGO)
        return

    def __onCampCaptured(self, campGO):
        self.onCampCaptured(campGO)
        return

    def __onCampCaptureHealApplied(self, heals):
        self.onCampCaptureHealApplied(heals)
        return

    @cached_property
    def __config(self):
        from helpers import dependency
        from skeletons.gui.lobby_context import ILobbyContext
        from portal_common.portal_constants import PORTAL_GAME_PARAMS_KEY
        lobbyContext = dependency.instance(ILobbyContext)
        portalConfig = lobbyContext.getServerSettings().getSettings()[PORTAL_GAME_PARAMS_KEY]
        return portalConfig[b'scenario']
