import SoundGroups, WWISE, Windowing
from gui.impl.gen import R
from gui.impl.lobby.video.video_sound_manager import IVideoSoundManager, SoundManagerStates
from gui.sounds.filters import StatesGroup, States
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


class BaseVideoRewardsSoundControl(IVideoSoundManager):
    __slots__ = (b'__bonusName', b'__state')
    _SOUND_EVENT_TEMPLATE = b'{}'
    _VIDEO_DONE = b'gui_lootbox_video_stop'
    _VIDEO_PAUSE = b'gui_lootbox_video_pause'
    _VIDEO_RESUME = b'gui_lootbox_video_resume'
    _REWARDS = {}
    _DEFAULT = b'tank_default'

    def __init__(self, bonusName):
        self.__bonusName = bonusName
        self.__state = None
        return

    def setBonusName(self, bonusName):
        self.__bonusName = bonusName
        return

    def start(self):
        if self.__state == SoundManagerStates.PLAYING:
            return
        if self.__state == SoundManagerStates.PAUSE:
            self.unpause()
            return
        soundSuffix = self._getSoundSuffix(self.__bonusName)
        SoundGroups.g_instance.playSound2D(self._SOUND_EVENT_TEMPLATE.format(soundSuffix))
        SoundGroups.g_instance.setState(StatesGroup.VIDEO_OVERLAY, States.VIDEO_OVERLAY_ON)
        self.__state = SoundManagerStates.PLAYING
        if not Windowing.isWindowAccessible():
            self.pause()
        return

    def _getSoundSuffix(self, bonusName):
        return self._REWARDS.get(bonusName, self._DEFAULT)

    def stop(self):
        if self.__state != SoundManagerStates.STOPPED:
            SoundGroups.g_instance.playSound2D(self._VIDEO_DONE)
            SoundGroups.g_instance.setState(StatesGroup.VIDEO_OVERLAY, States.VIDEO_OVERLAY_OFF)
            self.__state = SoundManagerStates.STOPPED
        return

    def pause(self):
        if self.__state != SoundManagerStates.PLAYING:
            return
        SoundGroups.g_instance.playSound2D(self._VIDEO_PAUSE)
        self.__state = SoundManagerStates.PAUSE
        return

    def unpause(self):
        if self.__state != SoundManagerStates.PAUSE:
            return
        SoundGroups.g_instance.playSound2D(self._VIDEO_RESUME)
        self.__state = SoundManagerStates.PLAYING
        return

    def handleWindowFocus(self, isWindowAccessible):
        if not isWindowAccessible:
            if self.__state == SoundManagerStates.PLAYING:
                self.pause()
            return
        if self.__state == SoundManagerStates.PAUSE:
            self.unpause()
            return
        return


class LootboxRewardVideoSoundControl(LootboxVideoSoundControl):

    def __init__(self):
        super(LootboxRewardVideoSoundControl, self).__init__(b'')
        return

    @property
    def videoSoundEvent(self):
        return ArmoryYardSounds.VIDEO_REWARD
