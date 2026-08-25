import CGF, Math
from script_component.DynamicScriptComponent import DynamicScriptComponent
from Event import SafeEvent, EventManager
from typing import List

class StoryModeLootableComponent(DynamicScriptComponent):
    _PREFAB_URL_BY_STYLE = {b'SM_LOOT_EQUIPMENT': b'content/CGFPrefabs/Storymode/loot.prefab', 
       b'SM_LOOT_PLAN': b'content/CGFPrefabs/Storymode/loot.prefab', 
       b'SM_LOOT_TANK': b'content/CGFPrefabs/Storymode/loot_yellow.prefab'}

    def __init__(self, *args, **kwargs):
        super(StoryModeLootableComponent, self).__init__(*args, **kwargs)
        self._eventManager = EventManager()
        self.onStartCapturing = SafeEvent(self._eventManager)
        self.onStopCapturing = SafeEvent(self._eventManager)
        self._loadPrefab()
        return

    def set_startTime(self, prevValue):
        if self.startTime == -1:
            self.onStopCapturing()
            return
        self.onStartCapturing(self.startTime, self.captureTime)
        return

    def onDestroy(self):
        self._eventManager.clear()
        super(StoryModeLootableComponent, self).onDestroy()
        return

    def _loadPrefab(self):
        if self.markerStyle in self._PREFAB_URL_BY_STYLE:
            CGF.loadAndCreatePrefabWithParent(self._PREFAB_URL_BY_STYLE[self.markerStyle], self.entity.entityGameObject, Math.Vector3(), self._onPrefabLoaded)
        return

    def _onPrefabLoaded(self, objects, queue):
        root = objects[0]
        queue.activateGameObject(root)
        transform = queue.component(root, CGF.TransformComponent)
        if transform:
            transform.scale = Math.Vector3(self.radius, 1.0, self.radius)
        return
