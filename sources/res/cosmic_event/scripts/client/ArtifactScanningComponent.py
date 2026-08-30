import typing, CGF, Math, cosmic_prefabs
from cosmic_event_common.cosmic_event_common import ArtifactComponentStages
from script_component.DynamicScriptComponent import DynamicScriptComponent
if typing.TYPE_CHECKING:
    from typing import Optional, List, Dict
    from CGF import GameObject
    from gui.shared.events import HasCtxEvent

class ArtifactScanningComponent(DynamicScriptComponent):

    def __init__(self):
        super(ArtifactScanningComponent, self).__init__()
        self._prefabs = []
        return

    def _onAvatarReady(self):
        from cosmic_event.gui.shared.events import ArtifactScanningEvent
        self._sendEvent(ArtifactScanningEvent.ANNOUNCEMENT_CREATED, self._getCreatedCtx())
        if self.stage == ArtifactComponentStages.ANNOUNCEMENT:
            self._loadAnnouncementPrefab()
        elif self.stage == ArtifactComponentStages.SCANNING:
            self._sendEvent(ArtifactScanningEvent.ARTIFACT_SCANNING_READY, self._getStartScanningCtx())
            self._loadArtifactPrefab()
        return

    def onDestroy(self):
        if self._prefabs:
            for prefab in self._prefabs:
                CGF.removeGameObject(prefab)

            self._prefabs = None
        from cosmic_event.gui.shared.events import ArtifactScanningEvent
        self._sendEvent(ArtifactScanningEvent.ARTIFACT_DESTROYED, {b'id': (self.entity.id)})
        super(ArtifactScanningComponent, self).onDestroy()
        return

    def set_vehiclesInZone(self, *args, **kwargs):
        from cosmic_event.gui.shared.events import ArtifactScanningEvent
        self._sendEvent(ArtifactScanningEvent.VEHICLES_IN_ZONE_CHANGED, {b'vehicles': (self.vehiclesInZone), b'id': (self.entity.id)})
        return

    def set_stage(self, *args, **kwargs):
        from cosmic_event.gui.shared.events import ArtifactScanningEvent
        if self.stage == ArtifactComponentStages.SCANNING:
            self._sendEvent(ArtifactScanningEvent.ARTIFACT_SCANNING_READY, self._getStartScanningCtx())
            for prefab in self._prefabs:
                CGF.removeGameObject(prefab)

            self._loadArtifactPrefab()
        return

    def _onPrefabLoaded(self, prefab):
        self._prefabs.append(prefab)
        return

    def _getStartScanningCtx(self):
        return {b'id': (self.entity.id), 
           b'vehicles': (self.vehiclesInZone), 
           b'endLifeTime': (self.endLifeTime), 
           b'duration': (self.duration), 
           b'isLastOne': (bool(self.isLastOne))}

    def _getCreatedCtx(self):
        return {b'id': (self.entity.id), 
           b'position': (self.entity.position)}

    @staticmethod
    def _sendEvent(event, ctx):
        from gui.shared import g_eventBus, EVENT_BUS_SCOPE
        from cosmic_event.gui.shared.events import ArtifactScanningEvent
        g_eventBus.handleEvent(ArtifactScanningEvent(event, ctx=ctx or {}), scope=EVENT_BUS_SCOPE.BATTLE)
        return

    def _loadAnnouncementPrefab(self):
        prefab = cosmic_prefabs.Artifact.BIG_HINT if self.isLastOne else cosmic_prefabs.Artifact.SMALL_HINT
        CGF.loadGameObjectIntoHierarchy(prefab, self.entity.entityGameObject, Math.Vector3(), self._onPrefabLoaded)
        return

    def _loadArtifactPrefab(self):
        prefabs = cosmic_prefabs.Artifact.BIG_APPEARANCE_RANGE if self.isLastOne else cosmic_prefabs.Artifact.SMALL_APPEARANCE_RANGE
        for prefab in prefabs:
            CGF.loadGameObjectIntoHierarchy(prefab, self.entity.entityGameObject, Math.Vector3(), self._onPrefabLoaded)

        return
