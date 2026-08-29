from collections import namedtuple
from enum import Enum
InfoPageInfo = namedtuple(b'InfoPageInfo', b'item, parent_screen')
FEATURE = b'wot_plus'
MIN_VIEW_TIME = 2.0

class WotPlusLogActions(Enum):
    CLOSE = b'close'
    CLICK = b'click'
    VIEWED = b'viewed'


class WotPlusKeys(Enum):
    HANGAR = b'hangar'
    REWARD_SCREEN = b'reward_screen'
    RESERVE_VIEW = b'reserve_view'
    RESERVE_AWARD_VIEW = b'reserve_award_view'
    HEADER_TOOLTIP = b'header_tooltip'
    CLOSE_BUTTON = b'close_button'
    DETAILS_BUTTON = b'details_button'
    INFO_BUTTON = b'info_button'
    NOTIFICATION_CENTER = b'notification_center'
    ATTENDANCE_REWARD_SCREEN = b'attendance_reward_screen'
    ACCOUNT_DASHBOARD = b'account_dashboard'
    SUBSCRIPTION_PAGE = b'subscription_page'


class RewardScreenTooltips(Enum):
    EXCLUSIVE_VEHICLE = b'exclusive_vehicle_tooltip'
    GOLD_RESERVE = b'gold_reserve_tooltip'
    PASSIVE_CREW_XP = b'passive_crew_xp_tooltip'
    EXCLUDED_MAP = b'excluded_map_tooltip'
    FREE_EQUIPMENT_MOVEMENT = b'free_equipment_movement_tooltip'
    ATTENDANCE_REWARD = b'attendance_reward_tooltip'
    TEAM_CREDITS_BONUS = b'team_credits_bonus_tooltip'
    DAILY_QUESTS_REWARDS = b'daily_quests_rewards_tooltip'


class ReservesKeys(Enum):
    GOLD_ACTIVATE = b'activate_wp_button'
    CREDITS_ACTIVATE = b'activate_pa_button'
    INFO_TOOLTIP = b'info_tooltip'
    GOLD_INFO = b'wp_info_button'
    CREDITS_INFO = b'pa_info_button'


class WotPlusStateStr(Enum):
    ACTIVE = b'active'
    INACTIVE = b'inactive'
    TRIAL = b'trial'
    SUSPENDED = b'suspended'
    ERROR = b'error'


class PremiumAccountStateStr(Enum):
    ACTIVE = b'active'
    INACTIVE = b'inactive'


class HeaderAdditionalData(Enum):
    NEW_ATTENDANCE_REWARD = b'new'


class NotificationAdditionalData(Enum):
    RELEASE_NOTIFICATION = b'release_notification'
    SPECIAL_NOTIFICATION = b'special_notification'


class WotPlusInfoPageSource(Enum):
    SHOP = InfoPageInfo(b'card_details_button', b'shop')
    REWARD_SCREEN = InfoPageInfo(WotPlusKeys.DETAILS_BUTTON, WotPlusKeys.REWARD_SCREEN)
    SUBSCRIPTION_PAGE = InfoPageInfo(WotPlusKeys.INFO_BUTTON, WotPlusKeys.SUBSCRIPTION_PAGE)
    GOLD_RESERVES = InfoPageInfo(ReservesKeys.GOLD_INFO, WotPlusKeys.RESERVE_VIEW)
    ATTENDANCE_REWARDS_SCREEN = InfoPageInfo(WotPlusKeys.INFO_BUTTON, WotPlusKeys.ATTENDANCE_REWARD_SCREEN)


class AccountDashboardFeature(Enum):
    SUBSCRIPTION_WIDGET = b'subscription_widget'
    RESERVE_WIDGET = b'reserve_widget'
    EXCLUDED_MAPS_WIDGET = b'excluded_maps_widget'


class SubscriptionPageKeys(Enum):
    INFO_BUTTON = WotPlusKeys.INFO_BUTTON
    CTA_BUTTON = b'cta_button'


class SubscriptionStateMixinKeys(Enum):
    WOT_PLUS = b'wotp'
    PREMIUM = b'pa'
