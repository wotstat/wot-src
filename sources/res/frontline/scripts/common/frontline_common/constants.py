from __future__ import absolute_import

class AccountSettingsKeys(object):
    EVENT_KEY = b'frontline_keys'
    SKILL_POINTS_SHOWN = b'points_shown'
    WELCOME_SCREEN_VIEWED = b'welcome_screen_viewed'
    RENT_BANNER_CLICKED = b'rent_banner_clicked'
    REWARD_TOKENS_RECEIVED = b'rewardTokensReceived'


class CallbackDataNames(object):
    FL_MODIFIER = b'fl_modifier'


ACCOUNT_DEFAULT_SETTINGS = {(AccountSettingsKeys.EVENT_KEY): {(AccountSettingsKeys.SKILL_POINTS_SHOWN): {}, (AccountSettingsKeys.WELCOME_SCREEN_VIEWED): {}, (AccountSettingsKeys.RENT_BANNER_CLICKED): False, 
                                     (AccountSettingsKeys.REWARD_TOKENS_RECEIVED): []}}
