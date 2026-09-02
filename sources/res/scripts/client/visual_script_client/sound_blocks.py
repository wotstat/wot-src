import BigWorld
from visual_script import ASPECT
from visual_script.block import Block, Meta
from visual_script.dependency import dependencyImporter
from visual_script.misc import errorVScript, EDITOR_TYPE
from visual_script.slot_types import SLOT_TYPE, arrayOf
from vehicle_systems.tankStructure import TankSoundObjectsIndexes
BattleReplay, SoundGroups, MusicControllerWWISE, helpers = dependencyImporter(b'BattleReplay', b'SoundGroups', b'MusicControllerWWISE', b'helpers')

class SoundMeta(Meta):

    @classmethod
    def blockColor(cls):
        return 16776960

    @classmethod
    def blockCategory(cls):
        return b'Sound'

    @classmethod
    def blockIcon(cls):
        return b':vse/blocks/sound'

    @classmethod
    def blockAspects(cls):
        return [ASPECT.CLIENT, ASPECT.HANGAR]


class PlaySound(Block, SoundMeta):

    def __init__(self, *args, **kwargs):
        super(PlaySound, self).__init__(*args, **kwargs)
        self._in = self._makeEventInputSlot(b'in', self._execute)
        self._sound = self._makeDataInputSlot(b'soundToPlay', SLOT_TYPE.SOUND)
        self._out = self._makeEventOutputSlot(b'out')
        self._onSoundStop = self._makeEventOutputSlot(b'onSoundStop')
        return

    def _execute(self):
        sound = self._sound.getValue()
        if sound:
            sound.setCallback(self.__onSoundEnd)
            if not sound.play():
                self._onSoundStop.call()
        self._out.call()
        return

    def __onSoundEnd(self, sound):
        self._onSoundStop.call()
        return


class StopSound(Block, SoundMeta):

    def __init__(self, *args, **kwargs):
        super(StopSound, self).__init__(*args, **kwargs)
        self._in = self._makeEventInputSlot(b'in', self._execute)
        self._sound = self._makeDataInputSlot(b'sound', SLOT_TYPE.SOUND)
        self._out = self._makeEventOutputSlot(b'out')
        return

    def _execute(self):
        sound = self._sound.getValue()
        if sound:
            sound.stop()
        self._out.call()
        return


class Create2DSound(Block, SoundMeta):

    def __init__(self, *args, **kwargs):
        super(Create2DSound, self).__init__(*args, **kwargs)
        self._soundName = self._makeDataInputSlot(b'soundName', SLOT_TYPE.STR)
        self._sound = self._makeDataOutputSlot(b'sound', SLOT_TYPE.SOUND, self._execute)
        return

    def _execute(self):
        sound = SoundGroups.g_instance.getSound2D(self._soundName.getValue())
        if sound:
            self._sound.setValue(sound)
        return


class Create3DSound(Block, SoundMeta):

    def __init__(self, *args, **kwargs):
        super(Create3DSound, self).__init__(*args, **kwargs)
        self._soundName = self._makeDataInputSlot(b'soundName', SLOT_TYPE.STR)
        self._soundObjectName = self._makeDataInputSlot(b'soundObjectName', SLOT_TYPE.STR)
        self._position = self._makeDataInputSlot(b'position', SLOT_TYPE.VECTOR3)
        self._sound = self._makeDataOutputSlot(b'sound', SLOT_TYPE.SOUND, self._execute)
        return

    def _execute(self):
        sound = SoundGroups.g_instance.WWgetSoundPos(self._soundName.getValue(), self._soundObjectName.getValue(), self._position.getValue())
        if sound:
            self._sound.setValue(sound)
        return


class SetMutedSounds(Block, SoundMeta):

    def __init__(self, *args, **kwargs):
        super(SetMutedSounds, self).__init__(*args, **kwargs)
        self._in = self._makeEventInputSlot(b'in', self._execute)
        self._soundNames = self._makeDataInputSlot(b'soundNames', arrayOf(SLOT_TYPE.STR))
        self._out = self._makeEventOutputSlot(b'out')
        return

    def validate(self):
        return super(SetMutedSounds, self).validate()

    def _execute(self):
        avatar = BigWorld.player()
        if avatar:
            if self._soundNames.hasValue():
                avatar.muteSounds(self._soundNames.getValue())
            else:
                avatar.muteSounds(())
        self._out.call()
        return

    @classmethod
    def blockAspects(cls):
        return [ASPECT.CLIENT]


class PlayCombatMusic(Block, SoundMeta):

    def __init__(self, *args, **kwargs):
        super(PlayCombatMusic, self).__init__(*args, **kwargs)
        self._play = self._makeEventInputSlot(b'play', self._doPlay)
        self._stop = self._makeEventInputSlot(b'stop', self._doMute)
        self._musicId = self._makeDataInputSlot(b'music', SLOT_TYPE.STR, EDITOR_TYPE.ENUM_SELECTOR)
        self._musicId.setEditorData([4, 5, 6, 7, 
         8, 9, 10, 
         11])
        self._out = self._makeEventOutputSlot(b'out')
        return

    def _doPlay(self):
        self._execute(True)
        self._out.call()
        return

    def _doMute(self):
        self._execute(False)
        self._out.call()
        return

    def _execute(self, play):
        if helpers.isPlayerAvatar():
            avatar = BigWorld.player()
            arenaType = avatar.arena.arenaType
            if arenaType.wwmusicSetup is not None:
                musicId = self._musicId.getValue()
                soundEventName = arenaType.wwmusicSetup.get(musicId, None)
                if soundEventName:
                    self.__combatMusic = SoundGroups.g_instance.getSound2D(soundEventName)
                    if self.__combatMusic is not None:
                        if play:
                            if not self.__combatMusic.isPlaying and not BattleReplay.g_replayCtrl.isTimeWarpInProgress:
                                self.__combatMusic.play()
                        elif self.__combatMusic.isPlaying:
                            self.__combatMusic.stop()
                        return
                elif musicId in arenaType.wwmusicSetup:
                    return
        errorVScript(self, b"Can't play combat music")
        return

    @classmethod
    def blockAspects(cls):
        return [ASPECT.CLIENT]


class SetMusicSkipArenaChanges(Block, SoundMeta):

    def __init__(self, *args, **kwargs):
        super(SetMusicSkipArenaChanges, self).__init__(*args, **kwargs)
        self._set = self._makeEventInputSlot(b'play', self._execute)
        self._skip = self._makeDataInputSlot(b'skip', SLOT_TYPE.BOOL)
        self._out = self._makeEventOutputSlot(b'out')
        return

    def _execute(self):
        MusicControllerWWISE.g_musicController.skipArenaChanges = self._skip.getValue()
        self._out.call()
        return

    @classmethod
    def blockAspects(cls):
        return [ASPECT.CLIENT]


class SetSoundRTPC(Block, SoundMeta):

    def __init__(self, *args, **kwargs):
        super(SetSoundRTPC, self).__init__(*args, **kwargs)
        self._in = self._makeEventInputSlot(b'in', self._setValue)
        self._out = self._makeEventOutputSlot(b'out')
        self._soundIn = self._makeDataInputSlot(b'soundIn', SLOT_TYPE.SOUND)
        self._soundOut = self._makeDataOutputSlot(b'soundOut', SLOT_TYPE.SOUND, None)
        self._rtpcName = self._makeDataInputSlot(b'rtpcName', SLOT_TYPE.STR)
        self._rtpcValue = self._makeDataInputSlot(b'rtpcValue', SLOT_TYPE.FLOAT)
        return

    def _setValue(self):
        sound = self._soundIn.getValue()
        if sound:
            sound.setRTPC(self._rtpcName.getValue(), self._rtpcValue.getValue())
        self._soundOut.setValue(sound)
        self._out.call()
        return


class SetSoundSwitch(Block, SoundMeta):

    def __init__(self, *args, **kwargs):
        super(SetSoundSwitch, self).__init__(*args, **kwargs)
        self._in = self._makeEventInputSlot(b'in', self._setValue)
        self._out = self._makeEventOutputSlot(b'out')
        self._soundIn = self._makeDataInputSlot(b'soundIn', SLOT_TYPE.SOUND)
        self._soundOut = self._makeDataOutputSlot(b'soundOut', SLOT_TYPE.SOUND, None)
        self._switchName = self._makeDataInputSlot(b'switchName', SLOT_TYPE.STR)
        self._switchValue = self._makeDataInputSlot(b'switchValue', SLOT_TYPE.STR)
        return

    def _setValue(self):
        sound = self._soundIn.getValue()
        if sound:
            sound.setSwitch(self._switchName.getValue(), self._switchValue.getValue())
        self._soundOut.setValue(sound)
        self._out.call()
        return


class GetSoundName(Block, SoundMeta):

    def __init__(self, *args, **kwargs):
        super(GetSoundName, self).__init__(*args, **kwargs)
        self._sound = self._makeDataInputSlot(b'sound', SLOT_TYPE.SOUND)
        self._name = self._makeDataOutputSlot(b'name', SLOT_TYPE.STR, self._execute)
        return

    def _execute(self):
        sound = self._sound.getValue()
        if sound:
            self._name.setValue(sound.name)
        else:
            self._name.setValue(b'')
        return


class IsSoundPlaying(Block, SoundMeta):

    def __init__(self, *args, **kwargs):
        super(IsSoundPlaying, self).__init__(*args, **kwargs)
        self._sound = self._makeDataInputSlot(b'sound', SLOT_TYPE.SOUND)
        self._isPlaying = self._makeDataOutputSlot(b'isPlaying', SLOT_TYPE.BOOL, self._execute)
        return

    def _execute(self):
        sound = self._sound.getValue()
        if sound:
            self._isPlaying.setValue(sound.isPlaying)
        else:
            self._isPlaying.setValue(False)
        return


class PlayGlobalSound(Block, SoundMeta):

    def __init__(self, *args, **kwargs):
        super(PlayGlobalSound, self).__init__(*args, **kwargs)
        self._in = self._makeEventInputSlot(b'in', self._execute)
        self._sound = self._makeDataInputSlot(b'soundToPlay', SLOT_TYPE.STR)
        self._out = self._makeEventOutputSlot(b'out')
        return

    def _execute(self):
        SoundGroups.g_instance.playSound2D(self._sound.getValue())
        self._out.call()
        return


class SetGlobalSoundSwitch(Block, SoundMeta):

    def __init__(self, *args, **kwargs):
        super(SetGlobalSoundSwitch, self).__init__(*args, **kwargs)
        self._in = self._makeEventInputSlot(b'in', self._setValue)
        self._out = self._makeEventOutputSlot(b'out')
        self._switchName = self._makeDataInputSlot(b'switchName', SLOT_TYPE.STR)
        self._switchValue = self._makeDataInputSlot(b'switchValue', SLOT_TYPE.STR)
        return

    def _setValue(self):
        SoundGroups.g_instance.setSwitch(self._switchName.getValue(), self._switchValue.getValue())
        self._out.call()
        return


class PlaySoundOnVehicleSoundObject(Block, SoundMeta):

    def __init__(self, *args, **kwargs):
        super(PlaySoundOnVehicleSoundObject, self).__init__(*args, **kwargs)
        self._soundObjNameToObjIndex = {b'chassis': (TankSoundObjectsIndexes.CHASSIS), 
           b'engine': (TankSoundObjectsIndexes.ENGINE), 
           b'gun': (TankSoundObjectsIndexes.GUN), 
           b'hit': (TankSoundObjectsIndexes.HIT), 
           b'count': (TankSoundObjectsIndexes.COUNT)}
        self._in = self._makeEventInputSlot(b'in', self._execute)
        self._vehicle = self._makeDataInputSlot(b'vehicle', SLOT_TYPE.VEHICLE)
        self._sndObjName = self._makeDataInputSlot(b'vehicleSoundObjName', SLOT_TYPE.STR)
        self._sndName = self._makeDataInputSlot(b'soundName', SLOT_TYPE.STR)
        self._out = self._makeEventOutputSlot(b'out')
        return

    def _execute(self):
        vehicle = self._vehicle.getValue()
        if vehicle and vehicle.appearance:
            soundObjectIndex = self._soundObjNameToObjIndex.get(self._sndObjName.getValue(), None)
            if soundObjectIndex is None:
                soundObjectIndex = TankSoundObjectsIndexes.CHASSIS
            soundObject = vehicle.appearance.engineAudition.getSoundObject(soundObjectIndex)
            if soundObject:
                soundObject.play(self._sndName.getValue())
        self._out.call()
        return


class SetGlobalSoundState(Block, SoundMeta):

    def __init__(self, *args, **kwargs):
        super(SetGlobalSoundState, self).__init__(*args, **kwargs)
        self._in = self._makeEventInputSlot(b'in', self._setValue)
        self._out = self._makeEventOutputSlot(b'out')
        self._stateGroupName = self._makeDataInputSlot(b'stateGroupName', SLOT_TYPE.STR)
        self._stateName = self._makeDataInputSlot(b'stateName', SLOT_TYPE.STR)
        return

    def _setValue(self):
        SoundGroups.g_instance.setState(self._stateGroupName.getValue(), self._stateName.getValue())
        self._out.call()
        return
