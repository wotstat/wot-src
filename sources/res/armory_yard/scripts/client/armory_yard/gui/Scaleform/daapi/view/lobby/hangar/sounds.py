import SoundGroups
from gui.impl.gen import R
from gui.impl.lobby.video.video_sound_manager import IVideoSoundManager, SoundManagerStates
from shared_utils import CONST_CONTAINER

class ArmoryYardSounds(CONST_CONTAINER):
    VIDEO_ARMOUR = b'ay_vid_stage_armour'
    VIDEO_GUN = b'ay_vid_stage_gun'
    VIDEO_TURRET = b'ay_vid_stage_turret'
    VIDEO_TRACKS = b'ay_vid_stage_tracks'
    VIDEO_REWARD = b'ay_vid_stage_reward'
    VIDEO_INTRO = b'ay_vid_stage_intro'
    VIDEO_PAUSE = b'ay_video_pause'
    VIDEO_RESUME = b'ay_video_resume'
    VIDEO_STOP = b'ay_video_stop'


class ArmoryYardVideoSoundControl(IVideoSoundManager):
    __VIDEO_TO_SOUND = {b'ay_armour': (ArmoryYardSounds.VIDEO_ARMOUR), 
       b'ay_gun': (ArmoryYardSounds.VIDEO_GUN), 
       b'ay_turret': (ArmoryYardSounds.VIDEO_TURRET), 
       b'ay_tracks': (ArmoryYardSounds.VIDEO_TRACKS), 
       b'ay_reward': (ArmoryYardSounds.VIDEO_REWARD), 
       b'ay_intro': (ArmoryYardSounds.VIDEO_INTRO)}

    def __init__(self, videoID):
        self.__videoID = videoID
        self.__state = None
        return

    @property
    def videoSoundEvent(self):
        return self.__getMapping().get(self.__videoID)

    def isVideoStarted(self):
        return self.__state is not None

    def start(self):
        sound = self.videoSoundEvent
        if sound:
            SoundGroups.g_instance.playSound2D(sound)
            self.__state = SoundManagerStates.PLAYING
        return

    def stop(self):
        if self.__state != SoundManagerStates.STOPPED:
            SoundGroups.g_instance.playSound2D(ArmoryYardSounds.VIDEO_STOP)
            self.__state = SoundManagerStates.STOPPED
        return

    def pause(self):
        SoundGroups.g_instance.playSound2D(ArmoryYardSounds.VIDEO_PAUSE)
        self.__state = SoundManagerStates.PAUSE
        return

    def unpause(self):
        SoundGroups.g_instance.playSound2D(ArmoryYardSounds.VIDEO_RESUME)
        self.__state = SoundManagerStates.PLAYING
        return

    def __getMapping(self):
        mapping = {}
        for video, sound in self.__VIDEO_TO_SOUND.iteritems():
            videoSource = R.videos.armory_yard.dyn(video)
            if videoSource.exists():
                mapping[videoSource()] = sound

        return mapping


class ArmoryYardRewardVideoSoundControl(ArmoryYardVideoSoundControl):

    def __init__(self):
        super(ArmoryYardRewardVideoSoundControl, self).__init__(b'')
        return

    @property
    def videoSoundEvent(self):
        return ArmoryYardSounds.VIDEO_REWARD
