class AccountSettingsKeys(object):
    EVENT_KEY = b'frontline_keys'
    SKILL_POINTS_SHOWN = b'points_shown'
    WELCOME_SCREEN_VIEWED = b'welcome_screen_viewed'


ACCOUNT_DEFAULT_SETTINGS = {(AccountSettingsKeys.EVENT_KEY): {(AccountSettingsKeys.SKILL_POINTS_SHOWN): {}, (AccountSettingsKeys.WELCOME_SCREEN_VIEWED): {}}}
