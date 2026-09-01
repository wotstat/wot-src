from __future__ import absolute_import
import functools, BigWorld, CGF
from helpers import dependency
from helpers.CallbackDelayer import CallbackDelayer
from items import vehicles
import GenericComponents
from gui.shared import EVENT_BUS_SCOPE, g_eventBus
from script_component.DynamicScriptComponent import DynamicScriptComponent
from battle_royale.gui.shared.events import AirDropEvent
from typing import List
from skeletons.gui.battle_session import IBattleSessionProvider
from debug_utils import LOG_DEBUG_DEV

class ArenaInfoBRComponent(DynamicScriptComponent, CallbackDelayer):
    __guiSessionProvider = dependency.descriptor(IBattleSessionProvider)

    def __init__(self):
        DynamicScriptComponent.__init__(self)
        CallbackDelayer.__init__(self)
        return

    def _onAvatarReady(self):
        self.set_nextDropWave(None)
        self.set_defeatedTeams(None)
        return

    def onLeaveWorld(self, *args):
        self.destroy()
        return

    def notifyLaunchPosition(self, equipmentId, position, launchTime, duration):
        delay = launchTime - BigWorld.serverTime()
        equipment = vehicles.g_cache.equipments()[equipmentId]
        self.__showGuiMarker(equipment, position, delay)
        self.delayCallback(delay, functools.partial(self.__launch, equipment, position, duration))
        return

    @property
    def battleRoyaleComponent(self):
        return self.__guiSessionProvider.arenaVisitor.getComponentSystem().battleRoyaleComponent

    def __showGuiMarker(self, equipment, position, delay):
        ctrl = self.__guiSessionProvider.shared.equipments
        if ctrl is not None:
            ctrl.showMarker(equipment, position, (0, 0, 0), delay)
        return

    def __launch(self, equipment, position, duration):

        def postloadSetup(objects, queue):
            go = objects[0]
            queue.assignComponent(go, equipment)
            queue.createComponent(go, GenericComponents.RemoveGoDelayedComponent, duration)
            return

        CGF.loadAndCreatePrefab(equipment.usagePrefab, self.entity.spaceID, position, postloadSetup)
        return

    def set_nextDropWave(self, prev):
        LOG_DEBUG_DEV(b'set_nextDropWave', self.nextDropWave)
        event = AirDropEvent(AirDropEvent.AIR_DROP_NXT_SPAWNED, ctx={b'timeout': (self.nextDropWave)})
        g_eventBus.handleEvent(event, scope=EVENT_BUS_SCOPE.BATTLE)
        return

    def set_defeatedTeams(self, _prev):
        self.battleRoyaleComponent.setDefeatedTeams(self.defeatedTeams)
        return

    def set_isRespawnTimeFinished(self, prev):
        if self.isRespawnTimeFinished:
            self.battleRoyaleComponent.onRespawnTimeFinished()
        return
