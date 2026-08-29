import GUI
from gui.Scaleform.daapi.view.battle.epic.minimap import _FRONT_LINE_DEV_VISUALIZATION_SUPPORTED, DevelopmentRespawnEntriesPlugin, EpicGlobalSettingsPlugin, HeadquartersStatusEntriesPlugin, MINIMAP_SCALE_TYPES, METERS_IN_1X_ZOOM, ProtectionZoneEntriesPlugin, RespawningPersonalEntriesPlugin, EpicArenaVehiclesPlugin, SectorBaseEntriesPlugin, SectorOverlayEntriesPlugin, SectorStatusEntriesPlugin, StepRepairPointEntriesPlugin, EpicMinimapPingPlugin, OwnDirectionPlugin
from gui.Scaleform.daapi.view.battle.shared.minimap import settings
from gui.Scaleform.daapi.view.battle.shared.minimap.component import _IMAGE_PATH_FORMATTER
from gui.Scaleform.daapi.view.meta.EpicDeploymentMapMeta import EpicDeploymentMapMeta
from gui.Scaleform.genConsts.LAYER_NAMES import LAYER_NAMES
from gui.battle_control import minimap_utils
from gui.shared.events import RespawnViewEvent
_S_NAME = settings.ENTRY_SYMBOL_NAME
_C_NAME = settings.CONTAINER_NAME
_DEPLOY_MAP_PATH = (b'_level0.root.{}.main.epicDeploymentMap.mapContainer.entriesContainer').format(LAYER_NAMES.VIEWS)

class EpicDeploymentMapComponent(EpicDeploymentMapMeta):

    def __init__(self):
        super(EpicDeploymentMapComponent, self).__init__()
        self._size = (210, 210)
        self._bounds = None
        self._hitAreaSize = minimap_utils.EPIC_MINIMAP_HIT_AREA
        return

    def _populate(self):
        super(EpicDeploymentMapComponent, self)._populate()
        self._updateThermalSectorSize(METERS_IN_1X_ZOOM, MINIMAP_SCALE_TYPES.REAL_SCALE)
        self.addListener(RespawnViewEvent.ON_RESPAWN_VIEW_SHOW, self.__onRespawnViewShow)
        self.addListener(RespawnViewEvent.ON_RESPAWN_VIEW_HIDE, self.__onRespawnViewHide)
        return

    def _dispose(self):
        super(EpicDeploymentMapComponent, self)._dispose()
        self.removeListener(RespawnViewEvent.ON_RESPAWN_VIEW_SHOW, self.__onRespawnViewShow)
        self.removeListener(RespawnViewEvent.ON_RESPAWN_VIEW_HIDE, self.__onRespawnViewHide)
        return

    def __setRespawnMode(self, respawnMode):
        self.getPlugin(b'own_direction').setRespawnMode(respawnMode)
        return

    def getVisualBounds(self):
        if not self._bounds:
            return (0, 0, 0, 0)
        minSize, maxSize = self._bounds
        return (minSize[0], maxSize[1], maxSize[0], minSize[1])

    def getRangeScale(self):
        return 0.6

    def canChangeAlpha(self):
        return False

    def setMinimapCenterEntry(self, entryID):
        return

    def changeMinimapZoom(self, mode):
        return

    def setEntryParameters(self, id_, doClip=True, scaleType=MINIMAP_SCALE_TYPES.REAL_SCALE):
        return

    def onZoomModeChanged(self, mode):
        return

    def updateSectorStates(self, states):
        return

    def _getFlashName(self):
        return b'ovmap'

    def _setupPlugins(self, visitor):
        setup = super(EpicDeploymentMapComponent, self)._setupPlugins(visitor)
        setup[b'settings'] = EpicGlobalSettingsPlugin
        setup[b'personal'] = RespawningPersonalEntriesPlugin
        setup[b'pinging'] = EpicMinimapPingPlugin
        if visitor.hasSectors():
            setup[b'epic_bases'] = DeploymentSectorBaseEntriesPlugin
            setup[b'epic_sector_overlay'] = SectorOverlayEntriesPlugin
        if visitor.hasRespawns() and visitor.hasSectors():
            setup[b'epic_sector_states'] = SectorStatusEntriesPlugin
            setup[b'protection_zones'] = ProtectionZoneEntriesPlugin
            setup[b'vehicles'] = EpicArenaVehiclesPlugin
            setup[b'own_direction'] = OwnDirectionPlugin
        if visitor.hasDestructibleEntities():
            setup[b'epic_hqs'] = DeploymentHeadquartersStatusEntriesPlugin
        if visitor.hasStepRepairPoints():
            setup[b'repairs'] = StepRepairPointEntriesPlugin
        if _FRONT_LINE_DEV_VISUALIZATION_SUPPORTED:
            setup[b'epic_frontline'] = DevelopmentRespawnEntriesPlugin
        return setup

    def _createFlashComponent(self):
        return GUI.MinimapFlashAS3(self.app.movie, _DEPLOY_MAP_PATH)

    def _getMinimapSize(self):
        return self._size

    def _processMinimapSize(self, minSize, maxSize):
        mapWidthPx, mapHeightPx = minimap_utils.metersToMinimapPixels(minSize, maxSize)
        self.as_setMapDimensionsS(mapWidthPx, mapHeightPx)
        self._size = (mapWidthPx, mapHeightPx)
        self._bounds = (minSize, maxSize)
        self._hitAreaSize = mapWidthPx
        return

    def _getMinimapTexture(self, arenaVisitor):
        return _IMAGE_PATH_FORMATTER.format(arenaVisitor.type.getOverviewMapTexture())

    def __onRespawnViewShow(self, *args):
        self.__setRespawnMode(True)
        return

    def __onRespawnViewHide(self, *args):
        self.__setRespawnMode(False)
        return


class DeploymentSectorBaseEntriesPlugin(SectorBaseEntriesPlugin):

    def __init__(self, parentObj):
        super(DeploymentSectorBaseEntriesPlugin, self).__init__(parentObj, _S_NAME.EPIC_DEPLOY_SECTOR_BASE_ALLY, _S_NAME.EPIC_DEPLOY_SECTOR_BASE_ENEMY)
        return


class DeploymentHeadquartersStatusEntriesPlugin(HeadquartersStatusEntriesPlugin):

    def __init__(self, parentObj):
        super(DeploymentHeadquartersStatusEntriesPlugin, self).__init__(parentObj, _S_NAME.EPIC_DEPLOY_HQ_ALLY, _S_NAME.EPIC_DEPLOY_HQ_ENEMY)
        return
