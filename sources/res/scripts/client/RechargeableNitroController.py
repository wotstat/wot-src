from __future__ import absolute_import, division
import typing, BigWorld
from constants import RECHARGEABLE_NITRO_STATE
from gui.shared.utils.decorators import ReprInjector
from items.components.shared_components import RechargeableNitroParams
from vehicles.components.vehicle_component import VehicleDynamicComponent
from vehicles.components.vehicle_prefabs import createMechanicPrefabSpawner
from vehicles.mechanics.common import IMechanicComponent
from vehicles.mechanics.mechanic_commands import IMechanicCommandsComponent, createMechanicCommandsEvents
from vehicles.mechanics.mechanic_constants import VehicleMechanic, VehicleMechanicCommand
from vehicles.mechanics.mechanic_states import IMechanicState, IMechanicStatesComponent, createMechanicStatesEvents
from vehicles.mechanics.mechanic_helpers import getVehicleDescrMechanicParams
if typing.TYPE_CHECKING:
    from typing import Any, Optional
    from vehicles.mechanics.mechanic_commands import IMechanicCommandsEvents
    from vehicles.mechanics.mechanic_states import IMechanicStatesEvents

@ReprInjector.simple(b'state', b'endTime', b'remainingTime', b'isCharged', b'isEmpty')
class RechargeableNitroState(typing.NamedTuple(b'RechargeableNitroState', (
 (
  b'state', RECHARGEABLE_NITRO_STATE),
 (
  b'endTime', float),
 (
  b'remainingTime', float),
 (
  b'isCharged', bool),
 (
  b'isEmpty', bool),
 (
  b'isBelowThreshold', bool),
 (
  b'params', typing.Optional[RechargeableNitroParams]))), IMechanicState):

    @classmethod
    def fromComponentStatus(cls, status, params):
        return cls(status.status, status.endTime, status.remainingTime, bool(status.isCharged), bool(status.isEmpty), status.isBelowThreshold, params)

    @property
    def progress(self):
        progress = 1.0
        if not self.params:
            return progress
        if self.timeLeft:
            if self.state in [RECHARGEABLE_NITRO_STATE.DEPLETING, RECHARGEABLE_NITRO_STATE.ACTIVE]:
                progress = min(1.0, self.timeLeft / self.params.duration)
            elif self.state == RECHARGEABLE_NITRO_STATE.PREPARING:
                reloadFactor = self.params.reloadTime / self.params.duration
                remainingReload = (self.params.duration - self.remainingTime) * reloadFactor
                cooldownCalc = (self.params.duration * self.params.threshold - self.remainingTime) * reloadFactor
                cooldown = max(self.params.cooldown, cooldownCalc)
                reloadDiff = remainingReload - (cooldown - self.timeLeft)
                progress = max(0.0, 1.0 - reloadDiff / self.params.reloadTime)
            elif self.state in [RECHARGEABLE_NITRO_STATE.DEPLOYING, RECHARGEABLE_NITRO_STATE.READY]:
                progress = 1.0
            else:
                progress = max(0.0, 1.0 - self.timeLeft / self.params.reloadTime)
        return progress

    @property
    def timeLeft(self):
        return max(0.0, self.endTime - BigWorld.serverTime())

    def isTransition(self, other):
        return self.state != other.state


@ReprInjector.withParent()
class RechargeableNitroController(VehicleDynamicComponent, IMechanicComponent, IMechanicCommandsComponent, IMechanicStatesComponent):

    def __init__(self):
        super(RechargeableNitroController, self).__init__()
        self.__params = None
        self.__currentState = RechargeableNitroState(RECHARGEABLE_NITRO_STATE.NOT_RUNNING, 0.0, 0.0, False, False, False, None)
        self.__mechanicPrefabSpawner = createMechanicPrefabSpawner(self.entity, self)
        self.__commandsEvents = createMechanicCommandsEvents(self)
        self.__statesEvents = createMechanicStatesEvents(self)
        self._initComponent()
        return

    @property
    def vehicleMechanic(self):
        return VehicleMechanic.RECHARGEABLE_NITRO

    @property
    def commandsEvents(self):
        return self.__commandsEvents

    @property
    def statesEvents(self):
        return self.__statesEvents

    def getMechanicState(self):
        return self.__currentState

    def set_stateStatus(self, _):
        self._updateComponentAppearance()
        return

    def onDestroy(self):
        self.__commandsEvents.destroy()
        self.__statesEvents.destroy()
        super(RechargeableNitroController, self).onDestroy()
        return

    def tryActivate(self):
        self.__commandsEvents.processMechanicCommand(VehicleMechanicCommand.ACTIVATE)
        if self.__currentState.state in RECHARGEABLE_NITRO_STATE.READY_STATES:
            self.cell.tryActivate()
        return

    def tryDeactivate(self):
        self.__commandsEvents.processMechanicCommand(VehicleMechanicCommand.DEACTIVATE)
        if self.__currentState.state in RECHARGEABLE_NITRO_STATE.ACTIVE_STATES:
            self.cell.tryDeactivate()
        return

    def alternateOnState(self):
        if self.__currentState.state in RECHARGEABLE_NITRO_STATE.ACTIVE_STATES:
            self.tryDeactivate()
        else:
            self.tryActivate()
        return

    def _onAppearanceReady(self):
        super(RechargeableNitroController, self)._onAppearanceReady()
        self.__statesEvents.processStatePrepared()
        return

    def _onComponentAppearanceUpdate(self, **kwargs):
        super(RechargeableNitroController, self)._onComponentAppearanceUpdate(**kwargs)
        if self.stateStatus:
            self.__currentState = RechargeableNitroState.fromComponentStatus(self.stateStatus, self.__params)
        self.__statesEvents.updateMechanicState(self.__currentState)
        return

    def _collectComponentParams(self, typeDescriptor):
        super(RechargeableNitroController, self)._collectComponentParams(typeDescriptor)
        self.__params = getVehicleDescrMechanicParams(typeDescriptor, self.vehicleMechanic)
        return
