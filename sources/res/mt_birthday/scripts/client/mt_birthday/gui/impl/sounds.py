import SoundGroups
from gui.impl.lobby.video.video_sound_manager import IVideoSoundManager, SoundManagerStates
from shared_utils import CONST_CONTAINER
from gui.sounds.filters import StatesGroup, States
from sound_gui_manager import CommonSoundSpaceSettings

class BirthdaySoundEvents(CONST_CONTAINER):
    VIDEO_START = b'mt_bday_2026_lb_video_start'
    VIDEO_DONE = b'mt_bday_2026_lb_video_stop'
    VIDEO_PAUSE = b'mt_bday_2026_lb_video_pause'
    VIDEO_RESUME = b'mt_bday_2026_lb_video_resume'
    MAIN_VIEW_ENTER = b'mt_bday_2026_enter'
    MAIN_VIEW_EXIT = b'mt_bday_2026_exit'
    REWARD_SCREEN_ANIMATION_SKIP = b'mt_bday_2026_quest_giver_reward_skip'
    OVERLAY_HANGAR_GENERAL = b'STATE_overlay_hangar_general'
    OVERLAY_HANGAR_GENERAL_ON = b'STATE_overlay_hangar_general_on'
    OVERLAY_HANGAR_GENERAL_OFF = b'STATE_overlay_hangar_general_off'


BIRTHDAY_REWARD_VIDEO_SOUND_SPACE = CommonSoundSpaceSettings(name=b'birthday_video_reward', entranceStates={(StatesGroup.VIDEO_OVERLAY): (States.VIDEO_OVERLAY_ON)}, exitStates={(StatesGroup.VIDEO_OVERLAY): (States.VIDEO_OVERLAY_OFF)}, persistentSounds=(), stoppableSounds=(), priorities=(), autoStart=True, enterEvent=b'', exitEvent=b'')
BIRTHDAY_REWARD_SCREEN_SOUND_SPACE = CommonSoundSpaceSettings(name=b'birthday_reward_screen', entranceStates={(BirthdaySoundEvents.OVERLAY_HANGAR_GENERAL): (BirthdaySoundEvents.OVERLAY_HANGAR_GENERAL_ON)}, exitStates={(BirthdaySoundEvents.OVERLAY_HANGAR_GENERAL): (BirthdaySoundEvents.OVERLAY_HANGAR_GENERAL_OFF)}, persistentSounds=(), stoppableSounds=(), priorities=(), autoStart=True)
BIRTHDAY_PLAYER_SELECT_SOUND_SPACE = CommonSoundSpaceSettings(name=b'birthday_player_select_screen', entranceStates={(BirthdaySoundEvents.OVERLAY_HANGAR_GENERAL): (BirthdaySoundEvents.OVERLAY_HANGAR_GENERAL_ON)}, exitStates={(BirthdaySoundEvents.OVERLAY_HANGAR_GENERAL): (BirthdaySoundEvents.OVERLAY_HANGAR_GENERAL_OFF)}, persistentSounds=(), stoppableSounds=(), priorities=(), autoStart=True)
BIRTHDAY_SOUND_SPACE = CommonSoundSpaceSettings(name=b'birthday', entranceStates={}, exitStates={}, persistentSounds=(), stoppableSounds=(), priorities=(), autoStart=True, enterEvent=b'mt_bday_2026_enter', exitEvent=b'mt_bday_2026_exit')

class VideoRewardsSoundControl(IVideoSoundManager):
    __slots__ = (b'__bonusName', b'__state')

    def __init__(self, bonusName):
        self.__bonusName = bonusName
        self.__state = None
        return

    def setBonusName(self, bonusName):
        self.__bonusName = bonusName
        return

    def start(self):
        SoundGroups.g_instance.playSound2D(BirthdaySoundEvents.VIDEO_START)
        self.__state = SoundManagerStates.PLAYING
        return

    def stop(self):
        if self.__state != SoundManagerStates.STOPPED:
            SoundGroups.g_instance.playSound2D(BirthdaySoundEvents.VIDEO_DONE)
            self.__state = SoundManagerStates.STOPPED
        return

    def pause(self):
        SoundGroups.g_instance.playSound2D(BirthdaySoundEvents.VIDEO_PAUSE)
        self.__state = SoundManagerStates.PAUSE
        return

    def unpause(self):
        SoundGroups.g_instance.playSound2D(BirthdaySoundEvents.VIDEO_RESUME)
        self.__state = SoundManagerStates.PLAYING
        return
