from __future__ import absolute_import
from account_helpers import AccountSettings

class AccountSettingsKeys(object):
    EVENT_KEY = b'wt_keys'
    WT_BATTLES_DONE_HUNTER = b'wtBattlesDoneHunter'
    WT_BATTLES_DONE_BOSS = b'wtBattlesDoneBoss'
    WT_LAST_SEEN_STAMPS = b'wtLastSeenStamp'
    WT_LAST_SEEN_TICKETS = b'wtLastSeenTickets'
    WT_LAST_SEEN_LEVEL = b'wtLastSeenLevel'
    WT_PROGRESSION_QUESTS_TAB = b'wtProgressionQuestsTab'
    WT_SEEN_WELCOME_SCREEN = b'wtWelcomeScreenSeen'
    WT_BANNER_SEEN = b'wtBannerSeen'
    WT_FINAL_NARRATIVE_VOICE_ACTIVE = b'wtFinalNarrativeVoice'


class AccountFavoriteKeys(object):
    WHITE_TIGER_VEHICLE = b'WHITE_TIGER_VEHICLE'


ACCOUNT_DEFAULT_SETTINGS = {(AccountSettingsKeys.EVENT_KEY): {(AccountSettingsKeys.WT_BATTLES_DONE_HUNTER): 0, 
                                     (AccountSettingsKeys.WT_BATTLES_DONE_BOSS): 0, 
                                     (AccountSettingsKeys.WT_LAST_SEEN_STAMPS): 0, 
                                     (AccountSettingsKeys.WT_LAST_SEEN_TICKETS): 0, 
                                     (AccountSettingsKeys.WT_SEEN_WELCOME_SCREEN): False, 
                                     (AccountSettingsKeys.WT_FINAL_NARRATIVE_VOICE_ACTIVE): True}}
ACCOUNT_DEFAULT_FAVORITES = {(AccountFavoriteKeys.WHITE_TIGER_VEHICLE): 0}

def getSettings(name):
    settings = AccountSettings.getSettings(AccountSettingsKeys.EVENT_KEY)
    return settings.get(name, ACCOUNT_DEFAULT_SETTINGS[AccountSettingsKeys.EVENT_KEY].get(name))


def setSettings(name, value):
    settings = AccountSettings.getSettings(AccountSettingsKeys.EVENT_KEY)
    settings[name] = value
    AccountSettings.setSettings(AccountSettingsKeys.EVENT_KEY, settings)
    return


def getWTFavorites():
    return AccountSettings.getFavorites(AccountFavoriteKeys.WHITE_TIGER_VEHICLE)


def setWTFavorites(value):
    favorites = AccountSettings.getFavorites(AccountFavoriteKeys.WHITE_TIGER_VEHICLE)
    if value != favorites:
        AccountSettings.setFavorites(AccountFavoriteKeys.WHITE_TIGER_VEHICLE, value)
    return


def isWelcomeScreenSeen():
    return getSettings(AccountSettingsKeys.WT_SEEN_WELCOME_SCREEN)


def setWelcomeScreenSeen(seen=True):
    return setSettings(AccountSettingsKeys.WT_SEEN_WELCOME_SCREEN, seen)


def isBannerSeen():
    return getSettings(AccountSettingsKeys.WT_BANNER_SEEN)


def setBannerSeen(seen=True):
    return setSettings(AccountSettingsKeys.WT_BANNER_SEEN, seen)


def setFinalNarrativeVoiceActive(active):
    return setSettings(AccountSettingsKeys.WT_FINAL_NARRATIVE_VOICE_ACTIVE, active)


def isFinalNarrativeVoiceActive():
    return getSettings(AccountSettingsKeys.WT_FINAL_NARRATIVE_VOICE_ACTIVE)
