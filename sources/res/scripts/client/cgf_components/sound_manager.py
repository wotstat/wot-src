import logging, BigWorld, CGF
from helpers import isPlayerAvatar
from cgf_script.managers_registrator import onAddedQuery, onRemovedQuery
from cgf_components import wt_helpers, sound_helpers
from cgf_components.sound_components import ConditionalSound2D, ConditionalSound3D, VehicleSound, VehicleSoundComponent, SoundNotification
from Vehicle import Vehicle
_logger = logging.getLogger(__name__)

class SoundComponentManager(CGF.ComponentManager):
    __TIME_BEETWEN_UNIQUE_EVENT = 0.5

    def __init__(self):
        super(SoundComponentManager, self).__init__()
        self.__pendingVehicles = None
        self.__lastUniqueEventTimeExecution = {}
        return

    def deactivate(self):
        for vehicle in CGF.Query(self.spaceID, Vehicle).values():
            vehicle.appearance.removeTempGameObject(b'sound_object')

        self.__pendingVehicles = None
        self.__lastUniqueEventTimeExecution = {}
        if isPlayerAvatar():
            playerAvatar = BigWorld.player()
            playerAvatar.onVehicleEnterWorld -= self.__onVehicleEnterWorld
        return

    @onAddedQuery(Vehicle)
    def onVehicleAdded(self, vehicle):
        vehicle.appearance.addTempGameObject(VehicleSoundComponent(vehicle), b'sound_object')
        return

    @onAddedQuery(SoundNotification, CGF.GameObject)
    def onEnterSoundNotification(self, sound, go):
        if sound.onlyForPlayerVehicle:
            vehicle = sound_helpers.getVehicle(go, self.spaceID)
            if vehicle and not vehicle.isPlayerVehicle:
                return
        self.__playNotification(sound.onEnterNotification, sound.conditions, sound.isUnique)
        return

    @onRemovedQuery(SoundNotification, CGF.GameObject)
    def onExitSoundNotification(self, sound, go):
        self.__playNotification(sound.onExitNotification, sound.conditions)
        return

    @onAddedQuery(ConditionalSound2D)
    def onEnterSound2D(self, sound):
        self.__play2d(sound.onEnterSound, sound.conditions)
        return

    @onRemovedQuery(ConditionalSound2D)
    def onExitSound2D(self, sound):
        self.__play2d(sound.onExitSound, sound.conditions)
        return

    @onAddedQuery(ConditionalSound3D, CGF.GameObject)
    def onEnterSound3D(self, sound, go):
        self.__play3d(sound.onEnterSound, go, sound.conditions)
        return

    @onRemovedQuery(ConditionalSound3D, CGF.GameObject)
    def onExitSound3D(self, sound, go):
        self.__play3d(sound.onExitSound, go, sound.conditions)
        return

    @onAddedQuery(VehicleSound, CGF.GameObject)
    def onEnterVehicleSound(self, sound, go):
        vehicle = sound_helpers.getVehicle(go, self.spaceID)
        if vehicle:
            soundObjIndex = sound.getSoundObjectIndex()
            enterSound = sound.onEnterSound
            if sound.useNPCEvents and not vehicle.isPlayerVehicle:
                if sound.onEnterSoundNPC:
                    enterSound = sound.onEnterSoundNPC
            soundConditions = sound.conditions
            if not hasattr(vehicle, b'appearance') or vehicle.appearance is None:
                if soundObjIndex is not None:
                    self.__registerPendingVehicle(vehicle.id, self.__playVehiclePart, (
                     enterSound, soundObjIndex, soundConditions))
                else:
                    self.__registerPendingVehicle(vehicle.id, self.__playVehicleRoot, (
                     enterSound, soundConditions))
            elif soundObjIndex is not None:
                self.__playVehiclePart(vehicle, enterSound, soundObjIndex, soundConditions)
            else:
                self.__playVehicleRoot(vehicle, enterSound, soundConditions)
        else:
            _logger.warning(b"Couldn't find vehicle! go=%s, spaceID=%s", go, self.spaceID)
        return

    @onRemovedQuery(VehicleSound, CGF.GameObject)
    def onExitVehicleSound(self, sound, go):
        vehicle = sound_helpers.getVehicle(go, self.spaceID)
        if vehicle:
            soundObjIndex = sound.getSoundObjectIndex()
            if not hasattr(vehicle, b'appearance') or vehicle.appearance is None:
                _logger.info(b"Could't find appearance in the vehicle id=%d", vehicle.id)
            else:
                onExitSound = sound.onExitSound
                if not vehicle.isPlayerVehicle and sound.onExitSoundNPC:
                    onExitSound = sound.onExitSoundNPC
                if soundObjIndex is not None:
                    self.__playVehiclePart(vehicle, onExitSound, soundObjIndex, sound.conditions)
                else:
                    self.__playVehicleRoot(vehicle, onExitSound, sound.conditions)
        else:
            _logger.warning(b"Couldn't find vehicle! go=%s, spaceID=%s", go, self.spaceID)
        return

    def __checkConditions(self, conditionsStr, vehicle=None):
        if not conditionsStr:
            return True
        conditions = conditionsStr.split()
        for condition in conditions:
            if condition.endswith(b'_player'):
                if not self.__checkAvatarCondition(condition, vehicle):
                    return False
            else:
                _logger.warning(b'Found unknown condition: %s', condition)
                return False

        return True

    def __checkAvatarCondition(self, condition, vehicle=None):
        if condition == b'boss_player':
            return wt_helpers.isBoss()
        if condition == b'hunter_player':
            return not wt_helpers.isBoss()
        if condition == b'only_for_player':
            return wt_helpers.isPlayerVehicle(vehicle)
        _logger.warning(b'Found unknown condition: %s', condition)
        return False

    def __playNotification(self, notificationName, conditionsStr, isUnique=False):
        isPlay = True
        if isUnique:
            lastTime = self.__lastUniqueEventTimeExecution.get(notificationName, 0)
            self.__lastUniqueEventTimeExecution[notificationName] = BigWorld.time()
            isPlay = BigWorld.time() - lastTime > self.__TIME_BEETWEN_UNIQUE_EVENT
        if notificationName and self.__checkConditions(conditionsStr) and isPlay:
            sound_helpers.playNotification(notificationName)
        return

    def __play2d(self, soundName, conditionsStr):
        if soundName and self.__checkConditions(conditionsStr):
            sound_helpers.play2d(soundName)
        return

    def __play3d(self, soundName, go, conditionsStr):
        if soundName and self.__checkConditions(conditionsStr):
            sound_helpers.play3d(soundName, go, self.spaceID)
        return

    def __playVehicleRoot(self, vehicle, soundName, conditionsStr):
        if soundName and vehicle and self.__checkConditions(conditionsStr, vehicle):
            sound_helpers.playVehicleSound(soundName, vehicle)
        return

    def __playVehiclePart(self, vehicle, soundName, partIndex, conditionsStr):
        if soundName and vehicle and partIndex and self.__checkConditions(conditionsStr, vehicle):
            sound_helpers.playVehiclePart(soundName, vehicle, partIndex)
        return

    def __registerPendingVehicle(self, vehicleID, cb, arguments):
        if self.__pendingVehicles is None:
            self.__pendingVehicles = {}
            BigWorld.player().onVehicleEnterWorld += self.__onVehicleEnterWorld
        self.__pendingVehicles[vehicleID] = (
         cb, arguments)
        return

    def __onVehicleEnterWorld(self, vehicle):
        vehicleId = vehicle.id
        if vehicleId in self.__pendingVehicles:
            cb, args = self.__pendingVehicles[vehicleId]
            _logger.info(b'Play postponed sound for vehicleID=%s, callback=%cb, arguments=%s', vehicleId, cb, args)
            cb(vehicle, *args)
            del self.__pendingVehicles[vehicleId]
        return
