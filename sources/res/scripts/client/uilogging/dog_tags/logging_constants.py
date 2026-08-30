from enum import Enum
FEATURE = b'dog_tags'
MIN_VIEW_TIME = 2

class DogTagActions(Enum):
    CLICK = b'click'
    VIEWED = b'viewed'
    DISPLAY = b'display'


class DogTagsViewKeys(Enum):
    HANGAR = b'hangar'
    DOG_TAG = b'dog_tag_view'
    ACCOUNT_DASHBOARD = b'account_dashboard'
    ANIMATED_DOG_TAG = b'animated_dog_tag'


class DogTagButtons(Enum):
    INFO = b'dog_tag_info_button'


class DogTagKeys(Enum):
    ANIMATION_TOOLTIP = b'animated_dog_tag_tooltip'
    ACHIEVEMENT_CARD = b'achievement_card'


class DogTagAchievementStates(Enum):
    IN_PROGRESS = b'in_progress'
    NO_PROGRESS = b'no_progress'
    COMPLETED = b'completed'
