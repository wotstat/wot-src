import SoundGroups
from gui_lootboxes.gui.impl.lobby.gui_lootboxes.sounds import BaseVideoRewardsSoundControl
from new_year.ny_constants import NewYearLootBoxes, NewYearLootBoxRewards
from shared_utils import CONST_CONTAINER
from new_year_common.items.components.ny_constants import ToySettings, MAX_ATMOSPHERE_LVL
from gui.sounds.filters import StatesGroup, States
from sound_gui_manager import CommonSoundSpaceSettings
RANDOM_STYLE_BOX = b'random'
GLADE_PREFIX = b'GLADE_'

class NewYearSoundVars(CONST_CONTAINER):
    RTPC_MUSIC_POSITION_CONTROL = b'RTPC_ext_newyear_music_position_control'
    RTPC_LEVEL_ATMOSPHERE = b'RTPC_ext_newyear_level_atmosphere'
    RTPC_LEVEL_TOYS = b'RTPC_ext_newyear_level_toys'
    STATE_NEWYEAR_PLACE = b'STATE_ext_hangar_newyear_place'
    SWITCH_STYLES_BOX = b'SWITCH_ext_newyear_style_box'
    SWITCH_STYLES_TALISMAN = b'SWITCH_ext_newyear_style_talisman'
    RTPC_LOOTBOX_ENTRY_VIEW = b'RTPC_ext_newyear_lootbox_camera'
    RTPC_LOOTBOX_AVAILABILITY = b'RTPC_ext_newyear_lootbox_availability'


class NewYearStylesBoxSwitches(CONST_CONTAINER):
    TALE = b'SWITCH_ext_newyear_style_box_magic'
    MODERN = b'SWITCH_ext_newyear_style_box_europe'
    SOVIET = b'SWITCH_ext_newyear_style_box_soviet'
    CHINESE = b'SWITCH_ext_newyear_style_box_asian'
    RANDOM = b'SWITCH_ext_newyear_style_box_random'


class NewYearStylesTalismanSwitches(CONST_CONTAINER):
    TALE = b'SWITCH_ext_newyear_style_talisman_magic'
    MODERN = b'SWITCH_ext_newyear_style_talisman_europe'
    SOVIET = b'SWITCH_ext_newyear_style_talisman_soviet'
    CHINESE = b'SWITCH_ext_newyear_style_talisman_asian'


class NewYearSoundStates(CONST_CONTAINER):
    HANGAR = b'STATE_ext_hangar_newyear_place_hangar'
    REWARDS_COLLECTIONS = b'STATE_ext_hangar_newyear_place_rewards_collections'
    DEBRIS = b'STATE_ext_hangar_newyear_place_debris'
    ALBUM_SELECT = b'STATE_ext_hangar_newyear_place_collections'
    GLADE_FIR = b'STATE_ext_hangar_newyear_place_glade_tree'
    GLADE_SNOWSLIDE = b'STATE_ext_hangar_newyear_place_glade_rink'
    GLADE_TEREM = b'STATE_ext_hangar_newyear_place_terem'
    GLADE_FIREWORKS = b'STATE_ext_hangar_newyear_place_fireworks'
    GLADE_FAIR = b'STATE_ext_hangar_newyear_place_fair'
    GLADE_INSTALLATIONS = b'STATE_ext_hangar_newyear_place_sculpture'
    CITY = b'STATE_ext_hangar_newyear_place_city'
    LEADERS = b'STATE_ext_hangar_newyear_place_lider'
    SURPRISE_MACHINE = b'STATE_ext_hangar_newyear_place_machine'
    REWARDS_LEVELS = b'STATE_ext_hangar_newyear_place_rewards_levels'
    INFO = b'STATE_ext_hangar_newyear_place_info'
    PET = b'STATE_ext_hangar_newyear_place_pet'
    VEHICLES = b'STATE_ext_hangar_newyear_place_tanks'
    GRIMVAGEN = b'STATE_ext_hangar_newyear_place_grimvagen'
    STATE_PLACE = b'STATE_hangar_place'
    STATE_PLACE_GARAGE = b'STATE_hangar_place_garage'


class NewYearSoundEvents(CONST_CONTAINER):
    HANGAR = b'hangar_newyear_place_hangar_enter'
    HANGAR_EXIT = b'hangar_newyear_place_hangar_exit'
    SIDE_BAR_CLICK = b'hangar_newyear_hud_side_click'
    TREE = b'hangar_newyear_tree_enter'
    TREE_EXIT = b'hangar_newyear_tree_exit'
    TANKS_SCREEN = b'hangar_newyear_tanks_screen_enter'
    TANKS_SCREEN_EXIT = b'hangar_newyear_tanks_screen_exit'
    GLADE = b'hangar_newyear_glade_enter'
    GLADE_EXIT = b'hangar_newyear_glade_exit'
    DEBRIS = b'hangar_newyear_debris_enter'
    DEBRIS_EXIT = b'hangar_newyear_debris_exit'
    TOYS = b'hangar_newyear_toys_enter'
    TOYS_EXIT = b'hangar_newyear_toys_exit'
    GLADE_FIR_ENTER = TREE
    GLADE_FIR_EXIT = TREE_EXIT
    GLADE_SNOWSLIDE_ENTER = b'hangar_newyear_rink_enter'
    GLADE_SNOWSLIDE_EXIT = b'hangar_newyear_rink_exit'
    GLADE_TEREM_ENTER = b'hangar_newyear_terem_enter'
    GLADE_TEREM_EXIT = b'hangar_newyear_terem_exit'
    GLADE_FIREWORKS_ENTER = b'hangar_newyear_fireworks_enter'
    GLADE_FIREWORKS_EXIT = b'hangar_newyear_fireworks_exit'
    GLADE_FAIR_ENTER = b'hangar_newyear_fair_enter'
    GLADE_FAIR_EXIT = b'hangar_newyear_fair_exit'
    GLADE_INSTALLATIONS_ENTER = b'hangar_newyear_sculpture_enter'
    GLADE_INSTALLATIONS_EXIT = b'hangar_newyear_sculpture_exit'
    ALBUM_SELECT = b'hangar_newyear_album_select_enter'
    ALBUM_SELECT_EXIT = b'hangar_newyear_album_select_exit'
    ALBUM_SELECT_2018 = b'hangar_newyear_album_select_2018_enter'
    ALBUM_SELECT_2018_EXIT = b'hangar_newyear_album_select_2018_exit'
    ALBUM_SELECT_2019 = b'hangar_newyear_album_select_2019_enter'
    ALBUM_SELECT_2019_EXIT = b'hangar_newyear_album_select_2019_exit'
    ALBUM_SELECT_2020 = b'hangar_newyear_album_select_2020_enter'
    ALBUM_SELECT_2020_EXIT = b'hangar_newyear_album_select_2020_exit'
    ALBUM_SELECT_2021 = b'hangar_newyear_album_select_2021_enter'
    ALBUM_SELECT_2021_EXIT = b'hangar_newyear_album_select_2021_exit'
    ALBUM_SELECT_2022 = b'hangar_newyear_album_select_2022_enter'
    ALBUM_SELECT_2022_EXIT = b'hangar_newyear_album_select_2022_exit'
    AWARD_STYLE_SCREEN = b'hangar_newyear_award_style_screen_enter'
    AWARD_STYLE_SCREEN_EXIT = b'hangar_newyear_award_style_screen_exit'
    CITY = b'hangar_newyear_city_enter'
    CITY_EXIT = b'hangar_newyear_city_exit'
    LEADERS = b'hangar_newyear_lider_enter'
    LEADERS_EXIT = b'hangar_newyear_lider_exit'
    SURPRISE_MACHINE = b'hangar_newyear_machine_enter'
    SURPRISE_MACHINE_EXIT = b'hangar_newyear_machine_exit'
    REWARDS_LEVELS = b'hangar_newyear_rewards_atmosphere_enter'
    REWARDS_LEVELS_EXIT = b'hangar_newyear_rewards_atmosphere_exit'
    PET = b'hangar_newyear_pet_enter'
    PET_EXIT = b'hangar_newyear_pet_exit'
    PET_TV_ENTER = b'hangar_newyear_pet_tv_enter'
    PET_TV_EXIT = b'hangar_newyear_pet_tv_exit'
    INFO = b'hangar_newyear_info_enter'
    INFO_EXIT = b'hangar_newyear_info_exit'
    GRIMVAGEN = b'hangar_newyear_grimvagen_enter'
    GRIMVAGEN_EXIT = b'hangar_newyear_grimvagen_exit'
    CUSTOMIZATION_SLOT_CLICK = b'highlight_red_butt'
    ADD_TOY_TREE = b'hangar_newyear_add_toy_tree'
    ADD_TOY_TREE_DOWN = b'hangar_newyear_add_toy_tree_down'
    ADD_TOY_TEREM = b'hangar_newyear_add_toy_terem'
    ADD_TOY_FIREWORKS = b'hangar_newyear_add_toy_fireworks'
    ADD_TOY_FAIR_SMALL = b'hangar_newyear_add_toy_fair_small'
    ADD_TOY_FAIR_BIG = b'hangar_newyear_add_toy_fair_big'
    ADD_TOY_INSTALLATIONS = b'hangar_newyear_add_toy_sculpture'
    ADD_TOY_SNOWSLIDE = b'hangar_newyear_add_toy_rink'
    TRANSITION_TREE = b'hangar_newyear_transition_tree'
    TRANSITION_TALISMAN = b'hangar_newyear_transition_talisman'
    ENTER_CUSTOME = b'hangar_newyear_enter_custome'
    ENTER_CUSTOME_FLIGHT = b'hangar_newyear_enter_custome_flight'
    COST_TOYS_UP = b'hangar_newyear_cost_toys_up'
    COST_TOYS_DOWN = b'hangar_newyear_cost_toys_down'
    COST_TOYS_NOT_CHANGE = b'hangar_newyear_cost_toys_not_change'
    LEVEL_UP = b'hangar_newyear_up_atmo'
    MACHINE_BTN_PRESS = b'hangar_newyear_machine_button_press'
    MACHINE_CHOISE_BTN_PRESS = b'hangar_newyear_machine_button_press_choise'
    MACHINE_ZOOM_IN = b'hangar_newyear_machine_zoom_in'
    MACHINE_ZOOM_OUT = b'hangar_newyear_machine_zoom_out'
    MACHINE_COINS = b'coins'
    TANKS_SET = b'hangar_newyear_tanks_set'
    ALBUM_ITEM_STOP = b'hangar_newyear_album_item_stop'
    VIDEO_DONE = b'gui_lootbox_video_stop'
    VIDEO_PAUSE = b'gui_lootbox_video_pause'
    VIDEO_RESUME = b'gui_lootbox_video_resume'
    OLDMAN_ONBOARDING_SKIP = b'ny_vo_terentiy_help_stop'
    ATMO_LEVEL_UP_VO_STOP = b'terentij_vo_atmo_stop'


class NewYearSoundConfigKeys(CONST_CONTAINER):
    ENTRANCE_EVENT = b'entranceEvent'
    LEAVE_EVENT = b'exitEvent'
    STATE_VALUE = b'stateValue'


class EnvSwitcherAnimSounds(CONST_CONTAINER):
    GROUP = b'STATE_hangar_filtered'
    ON = b'STATE_hangar_filtered_on'
    OFF = b'STATE_hangar_filtered_off'
    DAY_CHOICE = b'hangar_newyear_day_choice'
    NIGHT_CHOICE = b'hangar_newyear_night_choice'


class EnvSwitcherSounds(CONST_CONTAINER):
    GROUP = b'STATE_ext_hangar_newyear_spaces'
    DAY = b'STATE_ext_hangar_newyear_day'
    NIGHT = b'STATE_ext_hangar_newyear_night'
    DAY_ENTER = b'hangar_newyear_day_enter'
    DAY_EXIT = b'hangar_newyear_day_exit'
    NIGHT_ENTER = b'hangar_newyear_night_enter'
    NIGHT_EXIT = b'hangar_newyear_night_exit'


class RaccoonStates(CONST_CONTAINER):
    GROUP = b'STATE_ext_hangar_newyear_enot_zone'
    MAIN = b'STATE_ext_hangar_newyear_enot_zone_main'
    ITEMS = b'STATE_ext_hangar_newyear_enot_zone_items'
    SHOP = b'STATE_ext_hangar_newyear_enot_zone_shop'
    RAID = b'STATE_ext_hangar_newyear_enot_zone_raid'
    PROGRESS_FILL_START = b'hangar_newyear_raccoon_progress_bar_start'
    PROGRESS_FILL_STOP = b'hangar_newyear_raccoon_progress_bar_stop'


class RaccoonMood(CONST_CONTAINER):
    GROUP = b'STATE_ext_hangar_newyear_pet_mood'
    FUN = b'STATE_ext_hangar_newyear_pet_mood_funny'
    NORMAL = b'STATE_ext_hangar_newyear_pet_mood_normal'
    SAD = b'STATE_ext_hangar_newyear_pet_mood_sad'


class NewYearCelebVoiceOvers(CONST_CONTAINER):
    REWARD_EPIC = b'celeb_xx_reward_epic'
    REWARD_WEEKLY = b'celeb_xx_reward_weekly'
    REWARD_STOP = b'celeb_xx_reward_stop'


class TreeCameraSounds(CONST_CONTAINER):
    GROUP = b'STATE_ext_hangar_newyear_tree_camera'
    FIR = b'STATE_ext_hangar_newyear_tree_camera_A'
    CHRISTMASTREE = FIR
    CHRISTMASTREE_TOP = b'STATE_ext_hangar_newyear_tree_camera_C'
    CHRISTMASTREE_TOY_DOWN = b'STATE_ext_hangar_newyear_tree_camera_B'
    CAMERA_FLY = b'hangar_newyear_tree_camera_fly'


class RewardSoundEvents(CONST_CONTAINER):
    GROUP = b'STATE_overlay_hangar_general'
    ENTER = b'STATE_overlay_hangar_general_on'
    EXIT = b'STATE_overlay_hangar_general_off'
    REWARD_SOUND_SPACE = b'overlay_hangar'


OVERLAY_HANGAR_SOUND_SPACE = CommonSoundSpaceSettings(name=RewardSoundEvents.REWARD_SOUND_SPACE, entranceStates={(RewardSoundEvents.GROUP): (RewardSoundEvents.ENTER)}, exitStates={(RewardSoundEvents.GROUP): (RewardSoundEvents.EXIT)}, persistentSounds=(), stoppableSounds=(), priorities=(), autoStart=True, enterEvent=b'', exitEvent=b'')
NY_MAIN_VIEW_SOUND_SPACE = CommonSoundSpaceSettings(name=b'new_year_main_view', entranceStates={(StatesGroup.HANGAR_PLACE): (States.HANGAR_PLACE_GARAGE), 
   (StatesGroup.HANGAR_FILTERED): (States.HANGAR_FILTERED_OFF)}, exitStates={}, persistentSounds=(), stoppableSounds=(), priorities=(), autoStart=True, enterEvent=b'', exitEvent=b'')
NY_REWARD_VIDEO_SOUND_SPACE = CommonSoundSpaceSettings(name=b'new_year_video_reward', entranceStates={(StatesGroup.VIDEO_OVERLAY): (States.VIDEO_OVERLAY_ON)}, exitStates={(StatesGroup.VIDEO_OVERLAY): (States.VIDEO_OVERLAY_OFF)}, persistentSounds=(), stoppableSounds=(), priorities=(), autoStart=True, enterEvent=b'', exitEvent=b'')
NY_RAID_SOUND_SPACE = CommonSoundSpaceSettings(name=b'new_year_raid', entranceStates={(RaccoonStates.GROUP): (RaccoonStates.RAID)}, exitStates={(RaccoonStates.GROUP): (RaccoonStates.MAIN)}, persistentSounds=(), stoppableSounds=(), priorities=(), autoStart=True, enterEvent=b'', exitEvent=b'')
NY_LEADERBOARD_TANK_REWARD_SOUND = b'tank_leaderboard'
_STYLES_BOX_SWITCHES_MAP = {(ToySettings.NEW_YEAR): (NewYearStylesBoxSwitches.SOVIET), 
   (ToySettings.CHRISTMAS): (NewYearStylesBoxSwitches.MODERN), 
   (ToySettings.FAIRYTALE): (NewYearStylesBoxSwitches.TALE), 
   (ToySettings.ORIENTAL): (NewYearStylesBoxSwitches.CHINESE), 
   (ToySettings.SOVIET): (NewYearStylesBoxSwitches.SOVIET), 
   (ToySettings.MODERN_WESTERN): (NewYearStylesBoxSwitches.MODERN), 
   (ToySettings.TRADITIONAL_WESTERN): (NewYearStylesBoxSwitches.TALE), 
   (ToySettings.ASIAN): (NewYearStylesBoxSwitches.CHINESE), 
   (ToySettings.MEGA_TOYS): (NewYearStylesBoxSwitches.RANDOM), 
   RANDOM_STYLE_BOX: (NewYearStylesBoxSwitches.RANDOM)}
_STYLES_TALISMAN_SWITCHES_MAP = {(ToySettings.FAIRYTALE): (NewYearStylesTalismanSwitches.TALE), 
   (ToySettings.CHRISTMAS): (NewYearStylesTalismanSwitches.MODERN), 
   (ToySettings.NEW_YEAR): (NewYearStylesTalismanSwitches.SOVIET), 
   (ToySettings.ORIENTAL): (NewYearStylesTalismanSwitches.CHINESE)}
_ENTRY_VIEW_RTPC_VALUES = {lType: 100 for lType in NewYearLootBoxes.PREMIUM}
_HAS_BOX_RTPC_VALUE = 100
_FIRST_ATMOSPHERE_LEVEL = 1
_ATMO_LEVEL_UP_VO = b'terentij_vo_atmo_{:02d}'

def getAtmosphereLevelUpVoiceover(level):
    if _FIRST_ATMOSPHERE_LEVEL < level < MAX_ATMOSPHERE_LVL:
        return _ATMO_LEVEL_UP_VO.format(level)
    return b''


class NewYearSoundsManager(object):

    def __init__(self, viewSoundConfig):
        self.__soundsConfig = viewSoundConfig
        return

    def onEnterView(self):
        self.__playEvent(NewYearSoundConfigKeys.ENTRANCE_EVENT)
        self.setEnterViewState()
        return

    def onExitView(self):
        self.__playEvent(NewYearSoundConfigKeys.LEAVE_EVENT)
        return

    def clear(self):
        self.__soundsConfig = {}
        return

    def setEnterViewState(self):
        stateValue = self.__getValueByKey(NewYearSoundConfigKeys.STATE_VALUE)
        if stateValue:
            SoundGroups.g_instance.setState(NewYearSoundVars.STATE_NEWYEAR_PLACE, stateValue)
        return

    @staticmethod
    def playEvent(eventName):
        SoundGroups.g_instance.playSound2D(eventName)
        return

    @staticmethod
    def setRTPC(name, value):
        SoundGroups.g_instance.setRTCPGlobal(name, value)
        return

    @staticmethod
    def setStylesSwitchBox(toySetting):
        switchValue = _STYLES_BOX_SWITCHES_MAP.get(toySetting)
        if switchValue is not None:
            SoundGroups.g_instance.setSwitch(NewYearSoundVars.SWITCH_STYLES_BOX, switchValue)
        return

    @classmethod
    def setRTPCBoxEntryView(cls, boxType):
        cls.setRTPC(NewYearSoundVars.RTPC_LOOTBOX_ENTRY_VIEW, _ENTRY_VIEW_RTPC_VALUES.get(boxType, 0))
        return

    @classmethod
    def setRTPCBoxAvailability(cls, hasBox):
        cls.setRTPC(NewYearSoundVars.RTPC_LOOTBOX_AVAILABILITY, _HAS_BOX_RTPC_VALUE if hasBox else 0)
        return

    @staticmethod
    def setStylesTalismanSwitchBox(talismanType):
        switchValue = _STYLES_TALISMAN_SWITCHES_MAP.get(talismanType)
        if switchValue is not None:
            SoundGroups.g_instance.setSwitch(NewYearSoundVars.SWITCH_STYLES_TALISMAN, switchValue)
        return

    @staticmethod
    def setHangarFilteredState(on):
        state = States.HANGAR_FILTERED_ON if on else States.HANGAR_FILTERED_OFF
        SoundGroups.g_instance.setState(StatesGroup.HANGAR_FILTERED, state)
        return

    @staticmethod
    def setHangarPlaceGarage():
        SoundGroups.g_instance.setState(NewYearSoundStates.STATE_PLACE, NewYearSoundStates.STATE_PLACE_GARAGE)
        return

    @staticmethod
    def setGladeState(currentObject):
        stateName = getattr(NewYearSoundStates, GLADE_PREFIX + currentObject.upper())
        SoundGroups.g_instance.setState(NewYearSoundVars.STATE_NEWYEAR_PLACE, stateName)
        return

    @staticmethod
    def playGladeEvent(objectName, eventType):
        eventName = getattr(NewYearSoundEvents, GLADE_PREFIX + objectName.upper() + eventType)
        SoundGroups.g_instance.playSound2D(eventName)
        return

    @staticmethod
    def setTreeCameraState(currentObject):
        stateName = getattr(TreeCameraSounds, currentObject.upper())
        SoundGroups.g_instance.setState(TreeCameraSounds.GROUP, stateName)
        return

    @staticmethod
    def setCityState():
        SoundGroups.g_instance.setState(NewYearSoundVars.STATE_NEWYEAR_PLACE, NewYearSoundStates.CITY)
        return

    def __playEvent(self, eventKey):
        eventName = self.__getValueByKey(eventKey)
        if eventName:
            SoundGroups.g_instance.playSound2D(eventName)
        return

    def __getValueByKey(self, keyName):
        value = self.__soundsConfig.get(keyName)
        if callable(value):
            return value()
        return value


class VideoRewardsSoundControl(BaseVideoRewardsSoundControl):
    __slots__ = (b'__lootboxType', b'__rewardType')
    _SOUND_EVENT_TEMPLATE = b'gui_video_ny_lootbox_{}'
    _VIDEO_DONE = NewYearSoundEvents.VIDEO_DONE
    _VIDEO_PAUSE = NewYearSoundEvents.VIDEO_PAUSE
    _VIDEO_RESUME = NewYearSoundEvents.VIDEO_RESUME
    _REWARDS = NewYearLootBoxRewards.ALL
    _CUSTOMIZATION_DEFAULT = b'3dstyle_01'
    _LEGENDARY_TANK_DEFAULT = b'tank_legendary'
    _CUSTOMIZATION_REWARD = b'customizations'

    def __init__(self, bonusName, lootboxType=None, rewardType=None):
        super(VideoRewardsSoundControl, self).__init__(bonusName)
        self.__lootboxType = lootboxType
        self.__rewardType = rewardType
        return

    def setLootboxType(self, lootboxType):
        self.__lootboxType = lootboxType
        return

    def setRewardType(self, rewardType):
        self.__rewardType = rewardType
        return

    def _getSoundSuffix(self, bonusName):
        if bonusName in self._REWARDS:
            return self._REWARDS[bonusName]
        if self.__rewardType == self._CUSTOMIZATION_REWARD:
            return self._CUSTOMIZATION_DEFAULT
        if self.__lootboxType == NewYearLootBoxes.NY_CUR_YEAR_TANKS:
            return self._LEGENDARY_TANK_DEFAULT
        return self._DEFAULT
