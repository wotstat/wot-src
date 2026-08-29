import WWISE
from gui.impl.gen import R
from gui.impl.lobby.video.video_sound_manager import IVideoSoundManager, SoundManagerStates
from shared_utils import CONST_CONTAINER

class ArmoryYardSounds(CONST_CONTAINER):
    VIDEO_INTRO = b'ay_video_intro_01'
    VIDEO_ARMOUR = b'ay_video_armour_02'
    VIDEO_TRACKS = b'ay_video_tracks_03'
    VIDEO_REWARD = b'ay_video_reward_04'
    VIDEO_PAUSE = b'ay_video_pause'
    VIDEO_RESUME = b'ay_video_resume'
    VIDEO_STOP = b'ay_video_stop'


class LootboxVideoSoundControl(IVideoSoundManager):
    __VIDEO_TO_SOUND = {b'ay_intro': (ArmoryYardSounds.VIDEO_INTRO), 
       b'ay_armour': (ArmoryYardSounds.VIDEO_ARMOUR), 
       b'ay_tracks': (ArmoryYardSounds.VIDEO_TRACKS), 
       b'ay_reward': (ArmoryYardSounds.VIDEO_REWARD)}

    def __init__(self, videoID):
        self.__videoID = videoID
        self.__state = None
        return

    @property
    def videoSoundEvent(self):
        return self.__getMapping().get(self.__videoID)

    def start(self):
        sound = self.videoSoundEvent
        if sound:
            WWISE.WW_eventGlobal(sound)
            self.__state = SoundManagerStates.PLAYING
        return

    def stop(self):
        if self.__state != SoundManagerStates.STOPPED:
            WWISE.WW_eventGlobal(ArmoryYardSounds.VIDEO_STOP)
            self.__state = SoundManagerStates.STOPPED
        return

    def pause(self):
        WWISE.WW_eventGlobal(ArmoryYardSounds.VIDEO_PAUSE)
        self.__state = SoundManagerStates.PAUSE
        return

    def unpause(self):
        WWISE.WW_eventGlobal(ArmoryYardSounds.VIDEO_RESUME)
        self.__state = SoundManagerStates.PLAYING
        return

    def __getMapping(self):
        mapping = {}
        for video, sound in self.__VIDEO_TO_SOUND.iteritems():
            videoSource = R.videos.armory_yard.dyn(video)
            if videoSource.exists():
                mapping[videoSource()] = sound

        return mapping


class LootboxRewardVideoSoundControl(LootboxVideoSoundControl):

    def __init__(self):
        super(LootboxRewardVideoSoundControl, self).__init__(b'')
        return

    @property
    def videoSoundEvent(self):
        return ArmoryYardSounds.VIDEO_REWARD
