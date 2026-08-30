from typing import List, TYPE_CHECKING
import weakref
from story_mode.visual_script.enums import SMAwarenessStateEnum
from visual_script.slot_types import SLOT_TYPE, arrayOf
from visual_script.tunable_event_block import TunableEventBlock
from visual_script_client.player_blocks import PlayerEventMeta
from visual_script_client.vehicle_common import TunablePlayerVehicleEventBlock
if TYPE_CHECKING:
    from Math import Vector3
    import Vehicle

class OnPlayerAwarenessStateChange(TunablePlayerVehicleEventBlock, PlayerEventMeta):
    _EVENT_SLOT_NAMES = [
     b'onChanged']

    def __init__(self, *args, **kwargs):
        super(OnPlayerAwarenessStateChange, self).__init__(*args, **kwargs)
        self._state = self._makeDataOutputSlot(b'state', SMAwarenessStateEnum.slotType(), None)
        return

    def onStartScript(self):
        from SMDetectionDelayObservableComponent import SMDetectionDelayObservableComponent
        SMDetectionDelayObservableComponent.onAwarenessStateChanged += self.onAwarenessStateChanged
        return

    def onFinishScript(self):
        from SMDetectionDelayObservableComponent import SMDetectionDelayObservableComponent
        SMDetectionDelayObservableComponent.onAwarenessStateChanged -= self.onAwarenessStateChanged
        return

    @TunableEventBlock.eventProcessor
    def onAwarenessStateChanged(self, state):
        self._state.setValue(state)
        return


class OnSMReconAbilityActivated(TunablePlayerVehicleEventBlock, PlayerEventMeta):
    _EVENT_SLOT_NAMES = [
     b'onDeactivate', b'onActivate']

    def onStartScript(self):
        from SMReconAbilityVehicleComponent import SMReconAbilityVehicleComponent
        SMReconAbilityVehicleComponent.onSMReconAbilityActivated += self.onSMReconAbilityActivated
        return

    def onFinishScript(self):
        from SMReconAbilityVehicleComponent import SMReconAbilityVehicleComponent
        SMReconAbilityVehicleComponent.onSMReconAbilityActivated -= self.onSMReconAbilityActivated
        return

    @TunableEventBlock.eventProcessor
    def onSMReconAbilityActivated(self, isActivated):
        self._index = int(isActivated)
        return


class OnSMReconAbilitySpottedVehicles(TunablePlayerVehicleEventBlock, PlayerEventMeta):
    _EVENT_SLOT_NAMES = [
     b'onReconSpotVehicle']

    def __init__(self, *args, **kwargs):
        super(OnSMReconAbilitySpottedVehicles, self).__init__(*args, **kwargs)
        self._vehicleIDs = self._makeDataOutputSlot(b'vehicleIDs', arrayOf(SLOT_TYPE.INT), None)
        return

    def onStartScript(self):
        from SMReconAbilityEntityComponent import SMReconAbilityEntityComponent
        SMReconAbilityEntityComponent.onSMReconAbilitySpottedVehicles += self.onSMReconAbilitySpottedVehicles
        return

    def onFinishScript(self):
        from SMReconAbilityEntityComponent import SMReconAbilityEntityComponent
        SMReconAbilityEntityComponent.onSMReconAbilitySpottedVehicles -= self.onSMReconAbilitySpottedVehicles
        return

    @TunableEventBlock.eventProcessor
    def onSMReconAbilitySpottedVehicles(self, spottedVehiclesIDs):
        self._vehicleIDs.setValue(spottedVehiclesIDs)
        return


class OnSMDistractionAbilityActivated(TunablePlayerVehicleEventBlock, PlayerEventMeta):
    _EVENT_SLOT_NAMES = [
     b'onActivate']

    def __init__(self, *args, **kwargs):
        super(OnSMDistractionAbilityActivated, self).__init__(*args, **kwargs)
        self._vehicles = self._makeDataOutputSlot(b'vehicles', arrayOf(SLOT_TYPE.VEHICLE), None)
        return

    def onStartScript(self):
        from SMDistractionAbilityEntityComponent import SMDistractionAbilityEntityComponent
        SMDistractionAbilityEntityComponent.onSMDistractionAbilityActivated += self.onSMDistractionAbilityActivated
        return

    def onFinishScript(self):
        from SMDistractionAbilityEntityComponent import SMDistractionAbilityEntityComponent
        SMDistractionAbilityEntityComponent.onSMDistractionAbilityActivated -= self.onSMDistractionAbilityActivated
        return

    @TunableEventBlock.eventProcessor
    def onSMDistractionAbilityActivated(self, spottedVehicles):
        self._vehicles.setValue(list(map(weakref.proxy, spottedVehicles)))
        return


class OnSMAbilityWrongPoint(TunablePlayerVehicleEventBlock, PlayerEventMeta):
    _EVENT_SLOT_NAMES = [
     b'onPlaced']

    def __init__(self, *args, **kwargs):
        super(OnSMAbilityWrongPoint, self).__init__(*args, **kwargs)
        self._point = self._makeDataOutputSlot(b'point', SLOT_TYPE.VECTOR3, None)
        return

    def onStartScript(self):
        from StoryModeAvatarComponent import StoryModeAvatarComponent
        StoryModeAvatarComponent.onSMAbilityWrongPoint += self.onSMAbilityWrongPoint
        return

    def onFinishScript(self):
        from StoryModeAvatarComponent import StoryModeAvatarComponent
        StoryModeAvatarComponent.onSMAbilityWrongPoint -= self.onSMAbilityWrongPoint
        return

    @TunableEventBlock.eventProcessor
    def onSMAbilityWrongPoint(self, point):
        self._point.setValue(point)
        return
