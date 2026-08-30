import weakref, BigWorld
from visual_script import ASPECT
from visual_script.dependency import dependencyImporter
from visual_script.slot_types import SLOT_TYPE
from visual_script.tunable_event_block import TunableEventBlock
TriggersManager, = dependencyImporter(b'TriggersManager')
edgeCases = {b'track': (b'leftTrack0', b'rightTrack0', b'leftTrack1', b'rightTrack1'), 
   b'radioman': (b'radioman1', b'radioman2'), 
   b'gunner': (b'gunner1', b'gunner2'), 
   b'loader': (b'loader1', b'loader2'), 
   b'wheel': (b'wheel0', b'wheel1', b'wheel2', b'wheel3', b'wheel4', b'wheel5', b'wheel6', b'wheel7')}

def getPartNames(originalPartName):
    return edgeCases.get(originalPartName, (originalPartName,))


def getPartName(originalPartName):
    for name, names in edgeCases.items():
        if originalPartName in names:
            return name

    return originalPartName


def getPartState(originalPartName):
    available = getPartNames(originalPartName)
    deviceStates = BigWorld.player().deviceStates
    states = [deviceStates.get(name, b'normal') for name in available]
    if b'destroyed' in states:
        return 2
    if b'critical' in states:
        return 1
    return 0


class TriggerListener(TriggersManager.ITriggerListener):

    def __init__(self, *args, **kwargs):
        super(TriggerListener, self).__init__()
        return

    def destroy(self):
        self.unsubscribe()
        return

    def subscribe(self):
        TriggersManager.g_manager.addListener(self)
        return

    def unsubscribe(self):
        TriggersManager.g_manager.delListener(self)
        return

    def onTriggerActivated(self, params):
        triggerType = params.get(b'type')
        if triggerType == TriggersManager.TRIGGER_TYPE.PLAYER_VEHICLE_OBSERVED:
            self.onPlayerDetected(True)
        elif triggerType == TriggersManager.TRIGGER_TYPE.PLAYER_SHOOT:
            aimingInfo = params[b'aimingInfo']
            self.onPlayerShoot(aimingInfo)
        elif triggerType == TriggersManager.TRIGGER_TYPE.PLAYER_SHOT_MISSED:
            self.onPlayerShotMissed()
        elif triggerType == TriggersManager.TRIGGER_TYPE.PLAYER_VEHICLE_IN_FIRE:
            self.onPlayerVehicleFireEvent(True)
        elif triggerType == TriggersManager.TRIGGER_TYPE.PLAYER_TANKMAN_SHOOTED:
            tankmanName = params[b'tankmanName']
            isHealed = params[b'isHealed']
            self.onPlayerVehicleTankmanEvent(tankmanName, not isHealed)
        elif triggerType == TriggersManager.TRIGGER_TYPE.PLAYER_DEVICE_CRITICAL:
            deviceName = params[b'deviceName']
            isCritical = params[b'isCriticalNow']
            isRepaired = params[b'isRepaired']
            self.onPlayerVehicleDeviceEvent(deviceName, isCritical, not isRepaired)
        elif triggerType == TriggersManager.TRIGGER_TYPE.VEHICLE_VISUAL_VISIBILITY_CHANGED:
            isVisible = params[b'isVisible']
            targetId = params[b'vehicleId']
            vehicle = BigWorld.entities.get(targetId)
            if vehicle is not None and vehicle.publicInfo[b'team'] != BigWorld.player().team:
                if isVisible:
                    self.onPlayerDetectEnemy([vehicle], [])
                else:
                    self.onPlayerDetectEnemy([], [vehicle])
        elif triggerType == TriggersManager.TRIGGER_TYPE.AREA:
            self.onPlayerEnterTrigger(params[b'name'], True)
        elif triggerType == TriggersManager.TRIGGER_TYPE.PLAYER_MOVE:
            self.onPlayerMove(params[b'moveCommands'])
        return

    def onTriggerDeactivated(self, params):
        triggerType = params.get(b'type')
        if triggerType == TriggersManager.TRIGGER_TYPE.PLAYER_VEHICLE_OBSERVED:
            self.onPlayerDetected(False)
        elif triggerType == TriggersManager.TRIGGER_TYPE.PLAYER_VEHICLE_IN_FIRE:
            self.onPlayerVehicleFireEvent(False)
        elif triggerType == TriggersManager.TRIGGER_TYPE.AREA:
            self.onPlayerEnterTrigger(params[b'name'], False)
        return

    def onPlayerShoot(self, aimInfo):
        return

    def onPlayerShotMissed(self):
        return

    def onPlayerDetectEnemy(self, new, lost):
        return

    def onPlayerDetected(self, isDetected):
        return

    def onPlayerVehicleFireEvent(self, isStart):
        return

    def onPlayerVehicleTankmanEvent(self, tankmanName, isHit):
        return

    def onPlayerVehicleDeviceEvent(self, deviceName, isCritical, isHit):
        return

    def onPlayerEnterTrigger(self, trigger, enter):
        return

    def onPlayerMove(self, modeCommands):
        return

    def onAutoAim(self, isOn):
        return


class TunablePlayerVehicleEventBlock(TunableEventBlock, TriggerListener):

    def onStartScript(self):
        self.subscribe()
        return

    def onFinishScript(self):
        self.unsubscribe()
        return

    @classmethod
    def blockAspects(cls):
        return [ASPECT.CLIENT]


class TunableVehicleEventBlock(TunableEventBlock):

    def __init__(self, *args, **kwargs):
        super(TunableVehicleEventBlock, self).__init__(*args, **kwargs)
        self._subscriber = VehicleSubscriber(self)
        self._sub = self._makeEventInputSlot(b'subscribe', self._onSubscribe)
        self._unsub = self._makeEventInputSlot(b'unsubscribe', self._onUnsubscribe)
        self._outSub = self._makeEventOutputSlot(b'outSubscribe')
        self._outUnsub = self._makeEventOutputSlot(b'outUnSubscribe')
        self._vehicle = self._makeDataInputSlot(b'vehicle', SLOT_TYPE.VEHICLE)
        return

    def onFinishScript(self):
        self._subscriber.unsubscribeAll()
        return

    def validate(self):
        if not self._vehicle.hasValue():
            return b'Vehicle value is required'
        return super(TunableVehicleEventBlock, self).validate()

    def onEvent(self, *args, **kwargs):
        return self._onEvent(*args, **kwargs)

    @staticmethod
    def event(vehicle):
        return

    @TunableEventBlock.eventProcessor
    def _onEvent(self, *args, **kwargs):
        return

    def _onSubscribe(self):
        vehicle = self._vehicle.getValue()
        self._subscriber.subscribe(vehicle)
        self._outSub.call()
        return

    def _onUnsubscribe(self):
        vehicle = self._vehicle.getValue()
        self._subscriber.unsubscribe(vehicle)
        self._outUnsub.call()
        return


class VehicleSubscriber(object):

    def __init__(self, block):
        self._block = weakref.proxy(block)
        self._subscribedVehicles = []
        return

    @property
    def subscribedVehicles(self):
        return tuple(self._subscribedVehicles)

    def subscribe(self, vehicle):
        if vehicle.id not in self._subscribedVehicles:
            self._subscribedVehicles.append(vehicle.id)
            self._subscribe(vehicle)
        return

    def unsubscribe(self, vehicle):
        if vehicle.id in self._subscribedVehicles:
            self._subscribedVehicles.remove(vehicle.id)
            self._unsubscribe(vehicle)
        return

    def unsubscribeAll(self):
        for vehicleId in self._subscribedVehicles:
            vehicle = BigWorld.entities.get(vehicleId)
            if vehicle:
                self._unsubscribe(vehicle)

        del self._subscribedVehicles[:]
        return

    def _subscribe(self, vehicle):
        event = self._block.event(vehicle)
        event += self._block.onEvent
        return

    def _unsubscribe(self, vehicle):
        event = self._block.event(vehicle)
        event -= self._block.onEvent
        return
