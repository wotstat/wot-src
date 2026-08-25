from __future__ import absolute_import, division
import typing, BigWorld
from constants import TARGET_DESIGNATOR_STATE as STATE
from gui.shared.utils.decorators import ReprInjector
from vehicles.components.vehicle_component import VehicleDynamicComponent
from vehicles.components.vehicle_prefabs import createMechanicPrefabSpawner
from vehicles.mechanics.common import IMechanicComponent
from vehicles.mechanics.mechanic_commands import IMechanicCommandsComponent, createMechanicCommandsEvents
from vehicles.mechanics.mechanic_constants import VehicleMechanic, VehicleMechanicCommand
from vehicles.mechanics.mechanic_helpers import getVehicleDescrMechanicParams
from vehicles.mechanics.mechanic_states import IMechanicState, IMechanicStatesComponent, createMechanicStatesEvents
if typing.TYPE_CHECKING:
    from typing import Optional
    from items.components.shared_components import TargetDesignatorParams
    from vehicles.mechanics.mechanic_commands import IMechanicCommandsEvents
    from vehicles.mechanics.mechanic_states import IMechanicStatesEvents

@ReprInjector.simple(b'state', b'startTime', b'endTime')
class TargetDesignatorState(IMechanicState):
    __slots__ = (b'state', b'params', b'baseTime', b'startTime', b'endTime')

    def __init__(self, state, params, startTime=0.0, endTime=0.0):
        self.state = state
        self.params = params
        self.baseTime = endTime - startTime
        self.startTime = startTime
        self.endTime = endTime
        return

    def timeLeft(self):
        if self.state == STATE.PRE_BATTLE:
            if self.params is not None:
                return self.params.deployTime
            return 0
        return max(0.0, self.endTime - BigWorld.serverTime() if self.endTime > 0 else self.baseTime)

    def baseTimeLeft(self):
        return max(0.0, self.startTime + self.baseTime - BigWorld.serverTime() if self.endTime > 0 else self.baseTime)

    def progress(self, timeLeft):
        if self.baseTime > 0:
            return 1.0 - timeLeft / self.baseTime
        return 1.0

    def isTransition(self, other):
        return self.state != other.state


@ReprInjector.withParent()
class TargetDesignatorController(VehicleDynamicComponent, IMechanicComponent, IMechanicCommandsComponent, IMechanicStatesComponent):

    def __init__(self):
        super(TargetDesignatorController, self).__init__()
        self.__mechanicPrefabSpawner = createMechanicPrefabSpawner(self.entity, self)
        self.__commandsEvents = createMechanicCommandsEvents(self)
        self.__statesEvents = createMechanicStatesEvents(self)
        self.__params = None
        self.__state = self.__updateState()
        self._initComponent()
        return

    @property
    def vehicleMechanic(self):
        return VehicleMechanic.TARGET_DESIGNATOR

    @property
    def commandsEvents(self):
        return self.__commandsEvents

    @property
    def statesEvents(self):
        return self.__statesEvents

    def getComponentParams(self):
        return self.__params

    def getMechanicState(self):
        return self.__state

    def set_abilityState(self, _):
        self._updateComponentAppearance()
        return

    def onDestroy(self):
        self.__params = None
        self.__commandsEvents.destroy()
        self.__statesEvents.destroy()
        super(TargetDesignatorController, self).onDestroy()
        return

    def tryActivate(self):
        self.__commandsEvents.processMechanicCommand(VehicleMechanicCommand.ACTIVATE)
        if self.__state.state != STATE.READY:
            return
        self.cell.tryActivate()
        return

    def _onAppearanceReady(self):
        super(TargetDesignatorController, self)._onAppearanceReady()
        self.__state = self.__updateState()
        self.__statesEvents.processStatePrepared()
        return

    def _onComponentAppearanceUpdate(self, **kwargs):
        super(TargetDesignatorController, self)._onComponentAppearanceUpdate(**kwargs)
        self.__state = newState = self.__updateState()
        self.__statesEvents.updateMechanicState(newState)
        return

    def _collectComponentParams(self, typeDescriptor):
        super(TargetDesignatorController, self)._collectComponentParams(typeDescriptor)
        self.__params = getVehicleDescrMechanicParams(typeDescriptor, self.vehicleMechanic)
        return

    def __updateState(self):
        if self.abilityState is None:
            return TargetDesignatorState(STATE.PRE_BATTLE, self.__params)
        else:
            return TargetDesignatorState(self.abilityState.state, self.__params, self.abilityState.startTime, self.abilityState.endTime)
