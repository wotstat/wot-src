from __future__ import absolute_import
import typing
from constants import DUPLET_GUN_INDEXES_TUPLE
from events_handler import eventHandler
from gui.shared.utils.decorators import ReprInjector
from gui.battle_control.components_states.ammo import DefaultComponentAmmoState
from vehicle_appearance.constants import AppearanceState
from vehicles.components.component_wrappers import ifAppearanceReady
from vehicles.components.vehicle_component import VehicleDynamicComponent
from vehicles.entities import ShotParams
from vehicles.mechanics.common import IMechanicComponentLogic
from vehicles.mechanics.mechanic_constants import VehicleMechanic
from vehicles.parts.guns.twin_shoot import ITwinShootGunComponent, createTwinShootingEvents
if typing.TYPE_CHECKING:
    from vehicles.parts.guns.twin_shoot import ITwinShootingEvents

class TwinGunAmmoState(DefaultComponentAmmoState):

    def __init__(self, shotsAmount):
        super(TwinGunAmmoState, self).__init__()
        self.__shotsAmount = shotsAmount
        return

    def getShotsAmount(self):
        return self.__shotsAmount


@ReprInjector.withParent()
class TwinGunController(VehicleDynamicComponent, ITwinShootGunComponent, IMechanicComponentLogic):
    APPEARANCE_READY_STATE = AppearanceState.COMPONENTS_CREATED

    def __init__(self):
        super(TwinGunController, self).__init__()
        self.__afterShotDelay = 0.0
        self.__shootingEvents = createTwinShootingEvents(self.entity, self)
        self._initComponent()
        return

    @property
    def vehicleMechanic(self):
        return VehicleMechanic.TWIN_GUN

    @property
    def shootingEvents(self):
        return self.__shootingEvents

    def isDoubleBarrelMode(self):
        return len(self.getActiveGunIndexes()) > 1

    def getActiveGunIndexes(self):
        return tuple(self.activeGunIndexes)

    def getAfterShotDelay(self):
        return self.__afterShotDelay

    def getComponentParams(self):
        return self.getAfterShotDelay()

    def getNextGunIndexes(self):
        return tuple(self.nextGunIndexes or self.activeGunIndexes)

    @ifAppearanceReady
    def set_activeGunIndexes(self, _=None):
        self.__updateActiveGunIndexes()
        return

    @ifAppearanceReady
    def set_nextGunIndexes(self, _=None):
        self.__updateNextGunIndexes()
        return

    def onDestroy(self):
        self.__shootingEvents.destroy()
        super(TwinGunController, self).onDestroy()
        return

    def onDiscreteShot(self, gunIndex):
        self.__shootingEvents.processDiscreteShot(gunIndex)
        return

    def onDoubleShot(self):
        self.__shootingEvents.processMultiShot(DUPLET_GUN_INDEXES_TUPLE)
        return

    @eventHandler
    def onCollectAmmoStates(self, ammoStates):
        ammoStates[self.vehicleMechanic.value] = TwinGunAmmoState(self.shotsCount)
        return

    @eventHandler
    def onCollectShotParams(self, shotParamsList):
        shotParamsList.append(ShotParams(self.vehicleMechanic, 0, 0, False))
        return

    def _onAppearanceReady(self):
        super(TwinGunController, self)._onAppearanceReady()
        self.__shootingEvents.processAppearanceReady()
        return

    def _onAppearanceReset(self):
        super(TwinGunController, self)._onAppearanceReset()
        self.__shootingEvents.processAppearanceReset()
        return

    def _onComponentAppearanceUpdate(self, **kwargs):
        super(TwinGunController, self)._onComponentAppearanceUpdate(**kwargs)
        self.__updateActiveGunIndexes()
        self.__updateNextGunIndexes()
        return

    def _collectComponentParams(self, typeDescriptor):
        super(TwinGunController, self)._collectComponentParams(typeDescriptor)
        self.__afterShotDelay = typeDescriptor.gun.twinGun.afterShotDelay
        return

    def __updateActiveGunIndexes(self):
        self.__shootingEvents.onActiveGunsUpdate(self.getActiveGunIndexes())
        return

    def __updateNextGunIndexes(self):
        self.__shootingEvents.processNextGunsUpdate(self.getNextGunIndexes())
        return
