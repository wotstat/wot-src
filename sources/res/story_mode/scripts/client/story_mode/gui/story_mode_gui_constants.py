from constants_utils import ConstInjector
from gui.Scaleform.daapi.settings import views
from gui.prb_control import settings

class PREBATTLE_ACTION_NAME(settings.PREBATTLE_ACTION_NAME, ConstInjector):
    _const_type = str
    STORY_MODE = b'story_mode'


class FUNCTIONAL_FLAG(settings.FUNCTIONAL_FLAG, ConstInjector):
    STORY_MODE = 2147483648L


class SELECTOR_BATTLE_TYPES(settings.SELECTOR_BATTLE_TYPES, ConstInjector):
    _const_type = str
    STORY_MODE = b'StoryMode'


class VIEW_ALIAS(views.VIEW_ALIAS, ConstInjector):
    _const_type = str
    STORY_MODE_BATTLE_PAGE = b'StoryModeBattlePage'
    ONBOARDING_BATTLE_PAGE = b'OnboardingBattlePage'
    ONBOARDING_SETTINGS_WINDOW = b'onboardingSettingsWindow'
    STORY_MODE_INTRO_VIDEO_WINDOW = b'storyModeIntroVideoWindow'
    STORY_MODE_WEB_VIEW_TRANSPARENT = b'StoryModeWebViewTransparent'
    STORY_MODE_OUTRO_VIDEO_WINDOW = b'storyModeOutroVideoWindow'
    STORY_MODE_BATTLE_RESULTS = b'storyModeBattleResults'


IS_ONBOARDING_SEAMLESS_MISSION_CHANGING_ON = True
IS_STORY_MODE_FADE_IN_OUT_ON = True
STORY_MODE_FADE_IN_DURATION = 0.4
STORY_MODE_FADE_OUT_DURATION = 0.4
BONUS_ORDER = [
 13, 
 14, 
 15, 
 16, 
 17, 
 18, 
 19, 
 20, 
 21, 
 22, 
 23]
INFO_PAGE_STORY_MODE = b'infoPageStoryMode'
INFO_PAGE_STORY_MODE_EVENT = b'infoPageStoryMode_event'
ABILITY_ON_COOLDOWN_ACTIVATION_ERROR_KEY = b'ability_on_cooldown'
