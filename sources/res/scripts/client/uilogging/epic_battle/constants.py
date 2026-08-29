from enum import Enum
FEATURE = b'epic_battle'

class EpicBattleLogActions(Enum):
    OPEN = b'open'
    CLOSE = b'close'
    CLICK = b'click'
    TOOLTIP_WATCHED = b'tooltip_watched'
    VIEW_WATCHED = b'view_watched'


class EpicBattleLogKeys(Enum):
    ABILITIES_CONFIRM = b'abilities_confirm'
    SETUP_VIEW = b'setup_view'
    DROP_SKILL_DIALOG_CONFIRM = b'drop_skill_dialog_confirm'
    BUTTON = b'button'
    HANGAR = b'hangar'
    CONTAINER_VIEW = b'container_view'
    PROGRESS_VIEW = b'progress_view'
    SKILLS_VIEW = b'skills_view'
    REWARDS_VIEW = b'rewards_view'
    INFO_VIEW = b'info_view'
    AFTER_BATTLE_VIEW = b'after_battle_view'
    REWARDS_SELECTION_VIEW = b'rewards_selection_view'
    AWARDS_VIEW = b'awards_view'
    SUPPLY_OBJECTS_VIEW = b'supply_objects_view'


class EpicBattleLogButtons(Enum):
    INSTALL = b'install'
    NOT_INSTALL = b'not_install'
    CLOSE = b'close'
    INFO_PAGE = b'info_page'
    CHECKBOX = b'checkbox'
    CANCEL = b'cancel'
    CONFIRM = b'confirm'
    SHOP = b'shop'
    REWARDS = b'rewards_button'
    NEXT = b'next'
    LEVELUP_NOTIFICATION = b'levelup_notification'
    ENTRY_POINT = b'entry_point'
    REWARDS_SELECTION_CONFIRM = b'rewards_selection_confirm'
    REWARDS_SELECTION_CLOSE = b'rewards_selection_close'


class EpicBattleLogTabs(Enum):
    PROGRESS_TAB = b'progress_tab'
    SKILLS_TAB = b'skills_tab'
    REWARDS_TAB = b'rewards_tab'
    INFO_TAB = b'info_tab'
    SUPPLY_OBJECTS_TAB = b'supply_objects_tab'


class EpicBattleLogAdditionalInfo(Enum):
    APPLY_TO_VEHICLE = b'apply_to_vehicle'
    APPLY_TO_CLASS = b'apply_to_class'


class EpicBattleLogItemStates(Enum):
    ADVANCED = b'advanced'
