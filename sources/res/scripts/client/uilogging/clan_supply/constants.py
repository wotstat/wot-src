from enum import Enum
FEATURE = b'clan_supply'

class ClanSupplyLogAction(Enum):
    CLOSE = b'close'
    OPEN = b'open'


class ClanSupplyLogKeys(Enum):
    QUESTS_SCREEN = b'tour_task_screen_window'
    PROGRESSION_SCREEN = b'map_screen_window'
    CLAN_LANDING = b'clan_landing'
    NOTIFICATION = b'notification'
    HANGAR_HEADER = b'hangar_header'
    BACK_BUTTON = b'back_button'
    SIDEBAR_PROGRESSION = b'sidebar_map'
    SIDEBAR_QUEST = b'sidebar_quest'
