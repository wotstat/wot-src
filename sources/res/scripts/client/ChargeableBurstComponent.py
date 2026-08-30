from __future__ import absolute_import
import typing
from collections import namedtuple
from events_handler import eventHandler
from gui.battle_control.components_states.ammo import DefaultComponentAmmoState
from gui.shared.utils.decorators import ReprInjector
from vehicles.components.vehicle_component import VehicleDynamicComponent
from vehicles.mechanics.gun_mechanics.common import IGunMechanicComponent
from vehicles.mechanics.mechanic_constants import VehicleMechanic
from vehicles.mechanics.mechanic_helpers import getVehicleDescrMechanicParams
from vehicles.mechanics.mechanic_states import IMechanicState, IMechanicStatesComponent, createMechanicStatesEvents, IMechanicStatesEvents

class ChargeableBurstAmmoState(DefaultComponentAmmoState):

    def __init__(self, isBurstActive, shots, burstCount):
        super(ChargeableBurstAmmoState, self).__init__()
        self.__isBurstActive = isBurstActive
        self.__burstCount = burstCount
        self.__shots = shots
        return

    @property
    def isBurstActive(self):
        return self.__isBurstActive

    @property
    def burstCount(self):
        return self.__burstCount

    @property
    def shots(self):
        return self.__shots


@ReprInjector.simple(b'isBurstActive', b'charges', b'shots')
class ChargeableBurstModeState(namedtuple(b'ChargeableBurstModeState', (b'isBurstActive', b'charges', b'shots', b'penetrationCount', b'burstCount')), IMechanicState):

    def isTransition(self, other):
        return self.isBurstActive != other.isBurstActive


@ReprInjector.withParent()
class ChargeableBurstComponent(VehicleDynamicComponent, IGunMechanicComponent, IMechanicStatesComponent):

    def __init__(self):
        super(ChargeableBurstComponent, self).__init__()
        self.__penetrationCount = 0
        self.__burstCount = 0
        self.__statesEvents = createMechanicStatesEvents(self)
        self._initComponent()
        return

    @property
    def vehicleMechanic(self):
        return VehicleMechanic.CHARGEABLE_BURST

    @property
    def statesEvents(self):
        return self.__statesEvents

    def getComponentParams(self):
        return (
         self.__penetrationCount, self.__burstCount)

    def getMechanicState(self):
        return ChargeableBurstModeState(self.isBurstActive, self.charges, self.shots, self.__penetrationCount, self.__burstCount)

    def set_charges(self, prev):
        self._updateComponentAppearance()
        return

    def set_shots(self, prev):
        self._updateComponentAppearance()
        return

    def set_isBurstActive(self, prev):
        self._updateComponentAppearance()
        self._updateComponentAvatar()
        return

    def onDestroy(self):
        self.__statesEvents.destroy()
        super(ChargeableBurstComponent, self).onDestroy()
        return

    @eventHandler
    def onCollectAmmoStates(self, ammoStates):
        ammoStates[self.vehicleMechanic.value] = ChargeableBurstAmmoState(self.isBurstActive, self.shots, self.__burstCount)
        return

    def _onAppearanceReady(self):
        super(ChargeableBurstComponent, self)._onAppearanceReady()
        self.__statesEvents.processStatePrepared()
        return

    def _onComponentAppearanceUpdate(self, **kwargs):
        super(ChargeableBurstComponent, self)._onComponentAppearanceUpdate(**kwargs)
        mechanicState = self.getMechanicState()
        self.__statesEvents.updateMechanicState(mechanicState)
        return

    def _onComponentAvatarUpdate(self, player):
        super(ChargeableBurstComponent, self)._onComponentAvatarUpdate(player)
        player.updateVehicleAmmoStates()
        return

    def _collectComponentParams(self, typeDescriptor):
        super(ChargeableBurstComponent, self)._collectComponentParams(typeDescriptor)
        mechanicParams = getVehicleDescrMechanicParams(typeDescriptor, self.vehicleMechanic)
        self.__penetrationCount = mechanicParams.penetrationCount
        self.__burstCount, _, _ = typeDescriptor.gun.burst
        return
