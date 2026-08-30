from enum import Enum

class SeniorityAwardsFeatures(str, Enum):
    FEATURE = b'seniority_awards'
    VEHICLE_SELECTION_FEATURE = b'seniority_awards_vehicle_selection'


class SeniorityAwardsLogKeys(str, Enum):
    COINS_NOTIFICATION = b'coins_notification'
    REWARD_NOTIFICATION = b'reward_notification'
    VEHICLE_SELECTION_NOTIFICATION = b'vehicle_selection_notification'
    MULTIPLE_TOKENS_NOTIFICATION_ERROR = b'multiple_tokens_notification_error'
    TIMEOUT_NOTIFICATION_ERROR = b'timeout_notification_error'


class SeniorityAwardsLogSpaces(str, Enum):
    HANGAR = b'hangar'
    NOTIFICATION_CENTER = b'notification_center'


class SeniorityAwardsLogButtons(str, Enum):
    SHOP_BUTTON = b'shop_button'
    CLAIM_BUTTON = b'claim_button'
    SELECT_BUTTON = b'select_button'


class SeniorityAwardsLogActions(str, Enum):
    CLICK = b'click'
    DISPLAYED = b'displayed'
