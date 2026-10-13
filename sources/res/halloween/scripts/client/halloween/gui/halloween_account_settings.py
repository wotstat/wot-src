from __future__ import absolute_import
from copy import deepcopy
from account_helpers import AccountSettings
from halloween.gui.halloween_gui_constants import DifficultyLevel, AmmoPanelSwitchPreset

class AccountSettingsKeys(object):
    EVENT_KEY = b'hw26'
    SELECTED_LEVEL = b'selected_level'
    UNLOCK_LEVELS = b'unlock_levels'
    AWARD_UNLOCK_LEVELS = b'award_unlock_level'
    META_INTRO_VIEW_SHOWED = b'meta_into_view_showed'
    FAVORITES_VEHICLE = b'favorites'
    AMMO_PANEL_PRESET = b'ammo_preset'
    SOUND = b'sound'
    CHAT_FIRST_SEEN = b'chat_first_seen'
    ARTEFACT_VOICEOVER_MUTED = b'artefact_voiceover_muted'
    PROMO_SCREEN_SHOWED = b'promo_screen_showed'
    IS_EVENT_NEW = b'event_is_new'
    IS_BANNER_FIRST_APPEARANCE_SEEN = b'bannerFirstAppearanceSeen'
    BESTIARY_ENEMIES_SEEN = b'bestiaryEnemiesSeen'
    LAST_SELECTED_BESTIARY_ENEMIES = b'lastSelectedBestiaryEnemiesSeen'
    ANOMALIES_SYSTEM_AVAILABLE = b'anomaliesSystemAvailable'
    ANOMALIES_SHOWED = b'anomaliesShowed'


ACCOUNT_DEFAULT_SETTINGS = {(AccountSettingsKeys.EVENT_KEY): {(AccountSettingsKeys.SELECTED_LEVEL): (DifficultyLevel.EASY.value), 
                                     (AccountSettingsKeys.UNLOCK_LEVELS): {}, (AccountSettingsKeys.AWARD_UNLOCK_LEVELS): [], (AccountSettingsKeys.META_INTRO_VIEW_SHOWED): False, 
                                     (AccountSettingsKeys.FAVORITES_VEHICLE): 0, 
                                     (AccountSettingsKeys.SOUND): {}, (AccountSettingsKeys.AMMO_PANEL_PRESET): (AmmoPanelSwitchPreset.PRESET_1), 
                                     (AccountSettingsKeys.CHAT_FIRST_SEEN): False, 
                                     (AccountSettingsKeys.ARTEFACT_VOICEOVER_MUTED): False, 
                                     (AccountSettingsKeys.PROMO_SCREEN_SHOWED): False, 
                                     (AccountSettingsKeys.IS_EVENT_NEW): True, 
                                     (AccountSettingsKeys.IS_BANNER_FIRST_APPEARANCE_SEEN): False, 
                                     (AccountSettingsKeys.BESTIARY_ENEMIES_SEEN): (set()), 
                                     (AccountSettingsKeys.LAST_SELECTED_BESTIARY_ENEMIES): 0, 
                                     (AccountSettingsKeys.ANOMALIES_SYSTEM_AVAILABLE): False, 
                                     (AccountSettingsKeys.ANOMALIES_SHOWED): (set())}}

def getSettings(name):
    settings = AccountSettings.getSettings(AccountSettingsKeys.EVENT_KEY)
    value = settings.get(name, None)
    if value is None:
        value = deepcopy(AccountSettings.getSettingsDefault(AccountSettingsKeys.EVENT_KEY)[name])
    return value


def setSettings(name, value):
    settings = AccountSettings.getSettings(AccountSettingsKeys.EVENT_KEY)
    settings[name] = value
    AccountSettings.setSettings(AccountSettingsKeys.EVENT_KEY, settings)
    return


def isSoundPlayed(name, difficultyLevel):
    soundsSettings = getSettings(AccountSettingsKeys.SOUND)
    soundsByDifficultyLevel = soundsSettings.get(difficultyLevel.value)
    if soundsByDifficultyLevel:
        return name in soundsByDifficultyLevel
    return False


def setSoundPlayed(name, difficultyLevel):
    soundsSettings = getSettings(AccountSettingsKeys.SOUND)
    soundsByDifficultyLevel = soundsSettings.setdefault(difficultyLevel.value, set())
    soundsByDifficultyLevel.add(name)
    setSettings(AccountSettingsKeys.SOUND, soundsSettings)
    return


def setAwardUnlockedLevel(level):
    settings = AccountSettings.getSettings(AccountSettingsKeys.EVENT_KEY)
    unlockedLevels = settings[AccountSettingsKeys.AWARD_UNLOCK_LEVELS]
    if level.value not in unlockedLevels:
        unlockedLevels.append(level.value)
        settings[AccountSettingsKeys.AWARD_UNLOCK_LEVELS] = unlockedLevels
        AccountSettings.setSettings(AccountSettingsKeys.EVENT_KEY, settings)
    return


def setNewStatusUnlockLevel(level, status):
    settings = AccountSettings.getSettings(AccountSettingsKeys.EVENT_KEY)
    unlockedLevels = settings[AccountSettingsKeys.UNLOCK_LEVELS]
    unlockedLevels[level.value] = {b'isNew': status}
    settings[AccountSettingsKeys.UNLOCK_LEVELS] = unlockedLevels
    AccountSettings.setSettings(AccountSettingsKeys.EVENT_KEY, settings)
    return
