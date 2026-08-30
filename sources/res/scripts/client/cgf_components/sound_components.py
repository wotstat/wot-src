import logging
from cgf_script.component_meta_class import ComponentProperty, CGFMetaTypes, registerComponent
from vehicle_systems.tankStructure import TankSoundObjectsIndexes
import SoundGroups
_logger = logging.getLogger(__name__)

@registerComponent
class SoundNotification(object):
    onEnterNotification = ComponentProperty(type=CGFMetaTypes.STRING, editorName=b'onEnterNotification', value=b'')
    onExitNotification = ComponentProperty(type=CGFMetaTypes.STRING, editorName=b'onExitNotification', value=b'')
    conditions = ComponentProperty(type=CGFMetaTypes.STRING, editorName=b'conditions', value=b'')
    isUnique = ComponentProperty(type=CGFMetaTypes.BOOL, editorName=b'isUnique', value=False)
    onlyForPlayerVehicle = ComponentProperty(type=CGFMetaTypes.BOOL, editorName=b'onlyForPlayerVehicle', value=False)


@registerComponent
class ConditionalSound2D(object):
    onEnterSound = ComponentProperty(type=CGFMetaTypes.STRING, editorName=b'onEnterSound', value=b'')
    onExitSound = ComponentProperty(type=CGFMetaTypes.STRING, editorName=b'onExitSound', value=b'')
    conditions = ComponentProperty(type=CGFMetaTypes.STRING, editorName=b'conditions', value=b'')


@registerComponent
class ConditionalSound3D(object):
    onEnterSound = ComponentProperty(type=CGFMetaTypes.STRING, editorName=b'onEnterSound', value=b'')
    onExitSound = ComponentProperty(type=CGFMetaTypes.STRING, editorName=b'onExitSound', value=b'')
    conditions = ComponentProperty(type=CGFMetaTypes.STRING, editorName=b'conditions', value=b'')


@registerComponent
class VehicleSound(ConditionalSound3D):
    _SOUND_OBJ_NAMES_TO_INDEXES = {b'chassis': (TankSoundObjectsIndexes.CHASSIS), 
       b'engine': (TankSoundObjectsIndexes.ENGINE), 
       b'gun': (TankSoundObjectsIndexes.GUN), 
       b'hit': (TankSoundObjectsIndexes.HIT)}
    onEnterSoundNPC = ComponentProperty(type=CGFMetaTypes.STRING, editorName=b'onEnterSoundNPC', value=b'')
    onExitSoundNPC = ComponentProperty(type=CGFMetaTypes.STRING, editorName=b'onExitSoundNPC', value=b'')
    soundObjectName = ComponentProperty(type=CGFMetaTypes.STRING, editorName=b'soundObjectName', value=b'')
    useNPCEvents = ComponentProperty(type=CGFMetaTypes.BOOL, editorName=b'useNPCEvents', value=False)

    def getSoundObjectIndex(self):
        return self._SOUND_OBJ_NAMES_TO_INDEXES.get(self.soundObjectName)


@registerComponent
class VehicleSoundComponent(object):

    def __init__(self, parent):
        super(VehicleSoundComponent, self).__init__()
        self.parent = parent
        self.soundObjects = []
        self.__matrix = parent.matrix
        self.__soundObjectName = self.__getSoundObjectName(parent.isPlayerVehicle, parent.id)
        self.__soundObject = None
        return

    def play(self, event):
        if self.__soundObject:
            self.__soundObject.play(event)
        else:
            self.__soundObject = self.__createSoundObject()
            if self.__soundObject:
                self.__soundObject.play(event)
            else:
                _logger.warning(b'SoundOjbect is not valid!')
        return

    def setRTPC(self, nameRTPC, value):
        if self.__soundObject:
            self.__soundObject.setRTPC(nameRTPC, value)
        else:
            _logger.warning(b'SoundOjbect is not valid!')
        return

    def deactivate(self):
        if self.__soundObject:
            self.__soundObject.stopAll()
        while self.soundObjects:
            soundObj = self.soundObjects.pop()
            if soundObj.isPlaying:
                soundObj.stop()
            soundObj.releaseMatrix()

        return

    def destroy(self):
        if self.__soundObject:
            self.__soundObject.stopAll()
        self.__soundObject = None
        self.parent = None
        return

    def __getSoundObjectName(self, isPlayerVehicle, id):
        soundObjectName = b'VehicleSoundComponent_NPC_'
        if isPlayerVehicle:
            soundObjectName = b'VehicleSoundComponent_PC_'
        soundObjectName += str(id)
        return soundObjectName

    def __createSoundObject(self):
        return SoundGroups.g_instance.WWgetSoundObject(self.__soundObjectName, self.__matrix)

    def __destroySound(self, soundObj):
        if soundObj in self.soundObjects:
            self.soundObjects.remove(soundObj)
        soundObj.releaseMatrix()
        return
