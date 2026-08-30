from __future__ import absolute_import
import functools, CGF, Triggers, Physics
from cgf_demo.demo_category import DEMO_CATEGORY
from cgf_script.registration import ComponentProperty, registerComponent

@registerComponent
class TestEntranceSpawner(object):
    group = DEMO_CATEGORY
    editorTitle = b'Test Entrance Spawner'
    domain = CGF.Domain.Client
    trigger = ComponentProperty(type=CGF.PropertyType.Link, editorName=b'AreaTrigger to subscribe', value=Triggers.AreaTriggerComponent)
    debrisSpawner = ComponentProperty(type=CGF.PropertyType.Link, editorName=b'Spawner to subscribe', value=Physics.PhysicalDebrisSpawnerComponent)


class EntranceSpawnerSystem(CGF.System):
    EntranceSpawnerActivated = CGF.ActivateReaction(CGF.ReactRw(TestEntranceSpawner))
    AreaTriggerAccess = CGF.AccessReaction(CGF.Rw(Triggers.AreaTriggerComponent))
    DebrisSpawnerAccess = CGF.AccessReaction(CGF.Rw(Physics.PhysicalDebrisSpawnerComponent))
    Reactions = CGF.Reactions(EntranceSpawnerActivated, AreaTriggerAccess, DebrisSpawnerAccess)

    def update(self):
        triggerAccess = self.reaction(self.AreaTriggerAccess)
        for entrance in self.reaction(self.EntranceSpawnerActivated):
            self._onEntranceAdded(entrance, triggerAccess)

        return

    def _onEntranceAdded(self, entrance, triggerAccess):
        trigger = triggerAccess.find(entrance.trigger)
        if trigger:
            debrisSpawner = entrance.debrisSpawner
            trigger.addEnterReaction(functools.partial(self.__onEnter, debrisSpawner))
            trigger.addExitReaction(functools.partial(self.__onExit, debrisSpawner))
        return

    def __onEnter(self, debrisSpawnerUuid, who, where):
        debrisSpawnerAccess = self.reaction(self.DebrisSpawnerAccess)
        spawner = debrisSpawnerAccess.find(debrisSpawnerUuid)
        if spawner:
            spawner.spawnDebris()
        return

    def __onExit(self, debrisSpawnerUuid, who, where):
        debrisSpawnerAccess = self.reaction(self.DebrisSpawnerAccess)
        spawner = debrisSpawnerAccess.find(debrisSpawnerUuid)
        if spawner:
            spawner.removeDebris()
        return
