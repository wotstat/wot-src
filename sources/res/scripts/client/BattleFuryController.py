from __future__ import absolute_import, division
import BigWorld, typing
from gui.shared.utils.decorators import ReprInjector
from vehicles.components.vehicle_component import VehicleDynamicComponent
from vehicles.components.vehicle_prefabs import createMechanicPrefabSpawner
from vehicles.mechanics.common import IMechanicComponent
from vehicles.mechanics.mechanic_constants import VehicleMechanic
from vehicles.mechanics.mechanic_states import createMechanicStatesEvents, IMechanicStatesComponent, IMechanicState
if typing.TYPE_CHECKING:
    from vehicles.mechanics.mechanic_states import IMechanicStatesEvents
    from typing import Optional, Dict, Any

class BattleFuryState(typing.NamedTuple(b'BattleFuryState', (
 (
  b'level', int), (b'maxLevel', int), (b'startTime', float), (b'endTime', float))), IMechanicState):

    @classmethod
    def fromComponentStatus(cls, status):
        return cls(status.currentLevel, status.maxLevel, status.timeInterval[b'startTime'], status.timeInterval[b'endTime'])

    @property
    def progress(self):
        if self.level > 0 and self.duration > 0:
            return max(self.endTime - BigWorld.serverTime(), 0.0) / self.duration
        return 0.0

    @property
    def duration(self):
        return self.endTime - self.startTime

    def isTransition(self, other):
        return self.level != other.level


@ReprInjector.withParent()
class BattleFuryController(VehicleDynamicComponent, IMechanicComponent, IMechanicStatesComponent):

    def __init__(self):
        super(BattleFuryController, self).__init__()
        self.__mechanicPrefabSpawner = createMechanicPrefabSpawner(self.entity, self)
        self.__statesEvents = createMechanicStatesEvents(self)
        self._initComponent()
        return

    @property
    def vehicleMechanic(self):
        return VehicleMechanic.BATTLE_FURY

    @property
    def statesEvents(self):
        return self.__statesEvents

    def getMechanicState(self):
        return BattleFuryState.fromComponentStatus(self.abilityState)

    def set_abilityState(self, *_):
        self._updateComponentAppearance()
        return

    def onDestroy(self):
        self.__statesEvents.destroy()
        super(BattleFuryController, self).onDestroy()
        return

    def _onAppearanceReady(self):
        super(BattleFuryController, self)._onAppearanceReady()
        self.__statesEvents.processStatePrepared()
        return

    def _onComponentAppearanceUpdate(self, **kwargs):
        super(BattleFuryController, self)._onComponentAppearanceUpdate(**kwargs)
        self.__statesEvents.updateMechanicState(self.getMechanicState())
        return
