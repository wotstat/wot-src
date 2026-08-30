import BigWorld
from constants import DEFAULT_GUN_INSTALLATION_INDEX
from visual_script import ASPECT
from visual_script.dependency import dependencyImporter
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
        elif triggerType == TriggersManager.TRIGGER_TYPE.PLAYER_DISCRETE_SHOOT:
            gunInstallationIndex = params.get(b'gunInstallationIndex', DEFAULT_GUN_INSTALLATION_INDEX)
            self.onPlayerDiscreteShoot(gunInstallationIndex)
        elif triggerType == TriggersManager.TRIGGER_TYPE.PLAYER_SHOT_MISSED:
            gunInstallationIndex = params[b'gunInstallationIndex']
            self.onPlayerShotMissed(gunInstallationIndex)
        elif triggerType == TriggersManager.TRIGGER_TYPE.PLAYER_SHOT_HIT:
            targetId = params[b'targetId']
            target = BigWorld.entities.get(targetId)
            flags = params[b'flags']
            gunInstallationIndex = params[b'gunInstallationIndex']
            self.onPlayerShotHit(target, flags, gunInstallationIndex)
        elif triggerType == TriggersManager.TRIGGER_TYPE.PLAYER_VEHICLE_IN_FIRE:
            self.onPlayerVehicleFireEvent(True)
        elif triggerType == TriggersManager.TRIGGER_TYPE.PLAYER_CONTINUOUS_BURST_START:
            gunInstallationIndex = params.get(b'gunInstallationIndex', DEFAULT_GUN_INSTALLATION_INDEX)
            self.onPlayerContinuousBurstStart(gunInstallationIndex)
        elif triggerType == TriggersManager.TRIGGER_TYPE.PLAYER_CONTINUOUS_BURST_STOP:
            gunInstallationIndex = params.get(b'gunInstallationIndex', DEFAULT_GUN_INSTALLATION_INDEX)
            self.onPlayerContinuousBurstStop(gunInstallationIndex)
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
        elif triggerType == TriggersManager.TRIGGER_TYPE.SHOW_TRACER:
            attackerId = params[b'attackerId']
            attacker = BigWorld.entities.get(attackerId)
            isRicochet = params[b'isRicochet']
            startPoint = params[b'startPoint']
            velocity = params[b'velocity']
            gravity = params[b'gravity']
            maxShotDist = params[b'maxShotDist']
            gunInstallationIndex = params[b'gunInstallationIndex']
            self.onShowTracer(attacker, isRicochet, startPoint, velocity, gravity, maxShotDist, gunInstallationIndex)
        elif triggerType == TriggersManager.TRIGGER_TYPE.STUN:
            self.onStunInfoUpdated(params[b'stunInfo'])
        elif triggerType == TriggersManager.TRIGGER_TYPE.SIXTH_SENSE:
            self.onSixthSenceActivated()
        elif triggerType == TriggersManager.TRIGGER_TYPE.PLAYER_USED_AOE_EQUIPMENT:
            self.onPlayerUsedAoEEquipment(params[b'name'], params[b'position'])
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

    def onPlayerDiscreteShoot(self, gunInstallationIndex):
        return

    def onPlayerShotMissed(self, gunInstallationIndex):
        return

    def onPlayerShotHit(self, target, flags, gunInstallationIndex):
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

    def onPlayerContinuousBurstStart(self, gunInstallationIndex):
        return

    def onPlayerContinuousBurstStop(self, gunInstallationIndex):
        return

    def onAutoAim(self, isOn):
        return

    def onShowTracer(self, attacker, isRicochet, startPoint, velocity, gravity, maxShotDist, gunInstallationIndex):
        return

    def onStunInfoUpdated(self, stunInfo):
        return

    def onSixthSenceActivated(self):
        return

    def onPlayerUsedAoEEquipment(self, name, position):
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
