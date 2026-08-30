import logging
from enum import Enum
import BigWorld, AnimationSequence, Math
from gui.shared import EVENT_BUS_SCOPE, g_eventBus, events
from skeletons.gui.game_control import IPlatoonController
from vehicle_systems.stricted_loading import makeCallbackWeak
from ClientSelectableObject import ClientSelectableObject
from helpers import dependency
_logger = logging.getLogger(__name__)

class _PlatoonLightingStateMachineTriggers(Enum):
    PLATOON_LEFT_ENTER = b'PlatoonLeftEnter'
    PLATOON_LEFT_EXIT = b'PlatoonLeftExit'
    PLATOON_RIGHT_ENTER = b'PlatoonRightEnter'
    PLATOON_RIGHT_EXIT = b'PlatoonRightExit'
    PLATOON_PLAYER_ENTER = b'PlatoonPlayerEnter'
    PLATOON_PLAYER_EXIT = b'PlatoonPlayerExit'


class _PlatoonLightingStateMachineStates(Enum):
    PLAYER_ORIGINAL_LIGHTING = b'PlayerOriginalLighting'
    PLAYER_PLATOON_LIGHTING = b'PlayerPlatoonLighting'
    RIGHT_TANK_READY = b'PlatoonRightTankReady'
    LEFT_TANK_READY = b'PlatoonLeftTankReady'
    FULL_PLATOON = b'PlatoonBothTanksReady'


class PlatoonLighting(ClientSelectableObject):
    __platoonController = dependency.descriptor(IPlatoonController)

    def __init__(self):
        super(PlatoonLighting, self).__init__()
        self.__animator = None
        return

    def onEnterWorld(self, prereqs):
        _logger.debug(b'Starting platoon lighting state machine.')
        if self.animationStateMachine:
            animationLoader = AnimationSequence.Loader(self.animationStateMachine, self.spaceID)
            BigWorld.loadResourceListBG((
             animationLoader,), makeCallbackWeak(self.__onAnimatorLoaded))
        super(PlatoonLighting, self).onEnterWorld(prereqs)
        return

    def onLeaveWorld(self):
        _logger.debug(b'Stopping platoon lighting state machine.')
        super(PlatoonLighting, self).onLeaveWorld()
        if self.__animator is not None:
            self.__animator.stop()
            self.__animator = None
            g_eventBus.removeListener(events.HangarVehicleEvent.ON_PLATOON_TANK_LOADED, self.__onPlatoonTankEnter, scope=EVENT_BUS_SCOPE.LOBBY)
            g_eventBus.removeListener(events.HangarVehicleEvent.ON_PLATOON_TANK_DESTROY, self.__onPlatoonTankLeave, scope=EVENT_BUS_SCOPE.LOBBY)
            self.__platoonController.onPlatoonTankVisualizationChanged -= self.__enablePlatoonLighting
        return

    def __enterPlatoon(self):
        name = self.__animator.getCurrNodeName()
        _logger.debug(b'Entering platoon %s.', name)
        if name == _PlatoonLightingStateMachineStates.PLAYER_ORIGINAL_LIGHTING.value:
            self.__animator.setTrigger(_PlatoonLightingStateMachineTriggers.PLATOON_PLAYER_ENTER.value)
        return

    def __onAnimatorLoaded(self, resourceList):
        if self.animationStateMachine in resourceList.failedIDs:
            return
        self.__animator = resourceList[self.animationStateMachine]
        self.__animator.bindToWorld(Math.Matrix(self.matrix))
        self.__animator.start()
        g_eventBus.addListener(events.HangarVehicleEvent.ON_PLATOON_TANK_LOADED, self.__onPlatoonTankEnter, scope=EVENT_BUS_SCOPE.LOBBY)
        g_eventBus.addListener(events.HangarVehicleEvent.ON_PLATOON_TANK_DESTROY, self.__onPlatoonTankLeave, scope=EVENT_BUS_SCOPE.LOBBY)
        self.__platoonController.onPlatoonTankVisualizationChanged += self.__enablePlatoonLighting
        return

    def __onPlatoonTankEnter(self, event):
        name = self.__animator.getCurrNodeName()
        if name == _PlatoonLightingStateMachineStates.FULL_PLATOON.value:
            return
        _logger.debug(b'Tank entering platoon %s.', name)
        entity = event.ctx[b'entity']
        if entity.slotIndex == 0:
            if name != _PlatoonLightingStateMachineStates.RIGHT_TANK_READY.value:
                self.__animator.setTrigger(_PlatoonLightingStateMachineTriggers.PLATOON_RIGHT_ENTER.value)
        elif name != _PlatoonLightingStateMachineStates.LEFT_TANK_READY.value:
            self.__animator.setTrigger(_PlatoonLightingStateMachineTriggers.PLATOON_LEFT_ENTER.value)
        return

    def __onPlatoonTankLeave(self, event):
        name = self.__animator.getCurrNodeName()
        if name in (_PlatoonLightingStateMachineStates.PLAYER_PLATOON_LIGHTING.value,
         _PlatoonLightingStateMachineStates.PLAYER_ORIGINAL_LIGHTING.value):
            return
        _logger.debug(b'Tank leave platoon %s.', name)
        entity = event.ctx[b'entity']
        if entity.slotIndex == 0:
            if name != _PlatoonLightingStateMachineStates.LEFT_TANK_READY.value:
                self.__animator.setTrigger(_PlatoonLightingStateMachineTriggers.PLATOON_RIGHT_EXIT.value)
        elif name != _PlatoonLightingStateMachineStates.RIGHT_TANK_READY.value:
            self.__animator.setTrigger(_PlatoonLightingStateMachineTriggers.PLATOON_LEFT_EXIT.value)
        return

    def __leavePlatoon(self):
        name = self.__animator.getCurrNodeName()
        _logger.debug(b'Leaving platoon %s.', name)
        if name != _PlatoonLightingStateMachineStates.PLAYER_ORIGINAL_LIGHTING.value:
            self.__animator.setTrigger(_PlatoonLightingStateMachineTriggers.PLATOON_PLAYER_EXIT.value)
        return

    def __enablePlatoonLighting(self, isEnabled):
        if isEnabled:
            self.__enterPlatoon()
        else:
            self.__leavePlatoon()
        return
