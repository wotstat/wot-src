from __future__ import absolute_import
import CGF
from cgf_script.registration import ComponentProperty, registerComponent
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from typing import List

@registerComponent
class OnDisappearPrefabSpawnComponent(object):
    category = b'Sequence'
    editorTitle = b'On Disappear Prefab Spawner'
    domain = CGF.Domain.ClientEditor
    prefab = ComponentProperty(type=CGF.PropertyType.String, editorName=b'prefab', value=b'', annotations={b'path': b'*.prefab'})


@registerComponent
class OnAppearPrefabSpawnComponent(object):
    category = b'Sequence'
    editorTitle = b'On Appear Prefab Spawner'
    domain = CGF.Domain.ClientEditor
    prefab = ComponentProperty(type=CGF.PropertyType.String, editorName=b'prefab', value=b'', annotations={b'path': b'*.prefab'})


@registerComponent
class SequenceSnapshotComponent(object):
    editorTitle = b'Sequence Snapshot'
    domain = CGF.Domain.Client


@registerComponent
class SequencePauseComponent(object):
    editorTitle = b'Sequence Pause'
    domain = CGF.Domain.Client


class PrefabSpawnerSystem(CGF.System):
    SpawnerActivated = CGF.ActivateReaction(CGF.ReactRw(OnAppearPrefabSpawnComponent), CGF.TransformComponent)
    SpawnerDeactivated = CGF.DeactivateReaction(CGF.ReactRw(OnDisappearPrefabSpawnComponent), CGF.TransformComponent)
    Reactions = CGF.Reactions(SpawnerActivated, SpawnerDeactivated)

    def update(self):
        for spawner, tr in self.reaction(self.SpawnerDeactivated):
            CGF.loadAndCreatePrefab(spawner.prefab, self.spaceID, tr.worldTransform, self._onLoaded)

        for spawner, tr in self.reaction(self.SpawnerActivated):
            CGF.loadAndCreatePrefab(spawner.prefab, self.spaceID, tr.worldTransform, self._onLoaded)

        return

    @staticmethod
    def _onLoaded(objects, queue):
        root = objects[0]
        queue.activateGameObject(root)
        return
