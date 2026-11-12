from enum import Enum
FEATURE = b'newyear'
DEFAULT_TIME_LIMIT = 1.0

class Actions(str, Enum):
    OPEN = b'open'
    CLICK = b'click'
    CLOSE = b'close'


class Items(str, Enum):
    ENV_SWITCHER = b'env_switcher'
    QUESTS = b'quests'
    VOICEOVER_SWITCH = b'voiceover_switch'
    MACHINE = b'machine'
    MACHINE_BUY_BTN = b'machine_buy_btn'
    MACHINE_APPLY_BTN = b'machine_apply_btn'
    LEADERBOARD = b'leaderboard'
    WEEKLY_REWARDS = b'weekly_rewards'
    PET = b'pet'
    PET_REPEAT_ONBOARDING_BTN = b'pet_repeat_onboarding_btn'
    RAID_REPEAT_ONBOARDING_BTN = b'raid_repeat_onboarding_btn'
    EASTER_EGG_VIDEO = b'easter_egg_video'


class Views(str, Enum):
    HANGAR = b'hangar'
    SURPRISE_MACHINE = b'surprise_machine'
    LEADERBOARD = b'leaderboard'
    QUESTS = b'quests'
    PET = b'pet'
    PET_RAID = b'pet_raid'
