import WWISE
from constants import DEFAULT_LANGUAGE
from gui.impl.gen import R
from gui.impl.lobby.video.video_sound_manager import IVideoSoundManager, SoundManagerStates
from helpers import getClientLanguage
from math_utils import clamp
from shared_utils import CONST_CONTAINER
from sound_gui_manager import CommonSoundSpaceSettings

class SOUNDS(CONST_CONTAINER):
    ACTIVATE_CHAPTER_STATE = b'STATE_overlay_hangar_general'
    ACTIVATE_CHAPTER_STATE_ON = b'STATE_overlay_hangar_general_on'
    ACTIVATE_CHAPTER_STATE_OFF = b'STATE_overlay_hangar_general_off'


ACTIVATE_CHAPTER_SOUND_SPACE = CommonSoundSpaceSettings(name=SOUNDS.ACTIVATE_CHAPTER_STATE, entranceStates={(SOUNDS.ACTIVATE_CHAPTER_STATE): (SOUNDS.ACTIVATE_CHAPTER_STATE_ON)}, exitStates={(SOUNDS.ACTIVATE_CHAPTER_STATE): (SOUNDS.ACTIVATE_CHAPTER_STATE_OFF)}, persistentSounds=(), stoppableSounds=(), priorities=(), autoStart=True, enterEvent=b'', exitEvent=b'')

class BattlePassSounds(CONST_CONTAINER):
    _OVERLAY = b'bp_overlay'
    CONFIRM_BUY = b'bp_overlay_pay'
    REWARD_SCREEN = b'bp_reward_screen'
    TANK_POINTS_CAP = b'bp_tank_point_done'
    VIDEO_STYLE_J20_Type_2605_2 = b'bp_s11_video_type_5_level_2_start'
    VIDEO_STYLE_J20_Type_2605_3 = b'bp_s11_video_type_5_level_3_start'
    VIDEO_STYLE_J20_Type_2605_4 = b'bp_s11_video_type_5_level_4_start'
    VIDEO_STYLE_F64_AMX_50_FOCH_B_2 = b'bp_s11_video_foch_b_level_2_start'
    VIDEO_STYLE_F64_AMX_50_FOCH_B_3 = b'bp_s11_video_foch_b_level_3_start'
    VIDEO_STYLE_F64_AMX_50_FOCH_B_4 = b'bp_s11_video_foch_b_level_4_start'
    VIDEO_STYLE_A67_T57_58_2 = b'bp_s11_video_t57_level_2_start'
    VIDEO_STYLE_A67_T57_58_3 = b'bp_s11_video_t57_level_3_start'
    VIDEO_STYLE_A67_T57_58_4 = b'bp_s11_video_t57_level_4_start'
    VIDEO_PAUSE = b'lesta_bp_video_pause'
    VIDEO_RESUME = b'lesta_bp_video_resume'
    VIDEO_STOP = b'lesta_bp_video_stop'

    @classmethod
    def getOverlay(cls, count):
        return (b'_').join([cls._OVERLAY, str(clamp(1, 3, count))])


class BattlePassLanguageSwitch(CONST_CONTAINER):
    GROUP_NAME = b'SWITCH_ext_battle_pass_video_language'
    RU = b'SWITCH_ext_battle_pass_video_language_RU'
    EN = b'SWITCH_ext_battle_pass_video_language_EN'
    CN = b'SWITCH_ext_battle_pass_video_language_CN'


class AwardVideoSoundControl(IVideoSoundManager):
    __LANGUAGE_STATES = {b'ru': (BattlePassLanguageSwitch.RU), 
       b'en': (BattlePassLanguageSwitch.EN), 
       b'cn': (BattlePassLanguageSwitch.CN)}
    __VIDEO_TO_SOUND = {b'c_201292_2': (BattlePassSounds.VIDEO_STYLE_J20_Type_2605_2), 
       b'c_201292_3': (BattlePassSounds.VIDEO_STYLE_J20_Type_2605_3), 
       b'c_201292_4': (BattlePassSounds.VIDEO_STYLE_J20_Type_2605_4), 
       b'c_201548_2': (BattlePassSounds.VIDEO_STYLE_F64_AMX_50_FOCH_B_2), 
       b'c_201548_3': (BattlePassSounds.VIDEO_STYLE_F64_AMX_50_FOCH_B_3), 
       b'c_201548_4': (BattlePassSounds.VIDEO_STYLE_F64_AMX_50_FOCH_B_4), 
       b'c_202316_2': (BattlePassSounds.VIDEO_STYLE_A67_T57_58_2), 
       b'c_202316_3': (BattlePassSounds.VIDEO_STYLE_A67_T57_58_3), 
       b'c_202316_4': (BattlePassSounds.VIDEO_STYLE_A67_T57_58_4)}

    def __init__(self, videoID):
        self.__videoID = videoID
        self.__state = None
        return

    def start(self):
        sound = self.__getMapping().get(self.__videoID)
        if sound:
            WWISE.WW_setSwitch(BattlePassLanguageSwitch.GROUP_NAME, self.__selectLanguageState())
            WWISE.WW_eventGlobal(sound)
            self.__state = SoundManagerStates.PLAYING
        return

    def stop(self):
        if self.__state != SoundManagerStates.STOPPED:
            WWISE.WW_eventGlobal(BattlePassSounds.VIDEO_STOP)
            self.__state = SoundManagerStates.STOPPED
        return

    def pause(self):
        WWISE.WW_eventGlobal(BattlePassSounds.VIDEO_PAUSE)
        self.__state = SoundManagerStates.PAUSE
        return

    def unpause(self):
        WWISE.WW_eventGlobal(BattlePassSounds.VIDEO_RESUME)
        self.__state = SoundManagerStates.PLAYING
        return

    def __selectLanguageState(self):
        language = getClientLanguage()
        if language not in self.__LANGUAGE_STATES:
            language = DEFAULT_LANGUAGE
        if language not in self.__LANGUAGE_STATES:
            language = b'en'
        return self.__LANGUAGE_STATES[language]

    def __getMapping(self):
        mapping = {}
        for video, sound in self.__VIDEO_TO_SOUND.iteritems():
            videoSource = R.videos.battle_pass.dyn(video)
            if videoSource.exists():
                mapping[videoSource()] = sound

        return mapping
