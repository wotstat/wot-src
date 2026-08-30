from enum import Enum
FEATURE = b'advanced_achievement'

class AdvancedAchievementActions(Enum):
    CLICK = b'click'
    DISPLAY = b'display'


class AdvancedAchievementViewKey(Enum):
    HANGAR = b'hangar'
    NOTIFICATION_CENTER = b'notification_center'
    PLAYER_COLLECTION = b'player_collection'
    CATALOG = b'catalog'
    REWARD_SCREEN = b'reward_screen'
    EARNING = b'earning_notification_view'


class AdvancedAchievementButtons(Enum):
    TO_ACHIEVEMENT = b'go_to_achievement_button'
    TO_RECEIVED = b'go_to_received_button'
    MORE_REWARDS = b'more_rewards_button'
    GOBLET = b'goblet_button'
    DOG_TAG_PREVIEW = b'dog_tag_preview_button'
    CATALOG = b'catalog_button'


class AdvancedAchievementKeys(Enum):
    SUBCATEGORY = b'subcategory'
    UPCOMING = b'upcoming_achievement'
    EARNING_NOTIFICATION = b'earning_notification'
    ACHIEVEMENT_CARD = b'achievement_card'
    ANOTHER_PLAYER = b'another_player_click'


class AdvancedAchievementSubcategory(Enum):
    VEHICLE = b'vehicle'
    NATIONS = b'nations'
    CUSTOMIZATION = b'customization'
    TROPHY = b'trophy'


class AdvancedAchievementInfoKeys(Enum):
    MULTIPLE = b'multiple'
    SINGLE = b'single'
    PLAYER = b'player'
    ANOTHER_PLAYER = b'another_player'


class AdvancedAchievementStates(Enum):
    IN_PROGRESS = b'in_progress'
    NO_PROGRESS = b'no_progress'
    COMPLETED = b'completed'
