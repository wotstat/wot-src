from enum import Enum
from account_helpers.settings_core.options import AimSetting
from account_helpers.settings_core import settings_constants
FEATURE_NEWBIE_HINTS = b'newbie_hints'
FEATURE_NEWBIE_HINTS_SETTINGS = b'newbie_hints_settings'
TOOLTIP_MIN_VIEW_TIME = 2.0

class NewbieHintsLogActions(str, Enum):
    APPLY = b'apply'
    WATCHED = b'watched'
    CLICK = b'click'


class NewbieHintsLogViews(str, Enum):
    SETTINGS = b'settings'
    SETTINGS_ARCADE = b'settings_arcade'
    SETTINGS_SNIPER = b'settings_sniper'
    BATTLE = b'battle'


class SettingsNewbieTooltips(str, Enum):
    PREBATTLE_HINTS = b'#tooltips:newbiePrebattleHints'
    INBATTLE_HINTS = b'#tooltips:newbieBattleHints'
    INBATTLE_HINTS_RESET = b'restartNewbieBattleHints'


class CheckBoxState(str, Enum):
    ENABLE = b'enable'
    DISABLE = b'disable'


class NewbieHintsLogItems(str, Enum):
    BTN_RESET_VIEWED_HINTS = b'inbattle_hints_reset_btn'
    CHECKBOX_PREBATTLE_HINTS = b'prebattle_hints_checkbox'
    CHECKBOX_INBATTLE_HINTS = b'inbattle_hints_checkbox'
    TOOLTIP_SETTINGS_PREBATTLE_HINTS = b'prebattle_hints_tooltip'
    TOOLTIP_SETTINGS_INBATTLE_HINTS = b'inbattle_hints_tooltip'
    TOOLTIP_SETTINGS_INBATTLE_HINTS_RESET = b'inbattle_reset_tooltip'


SETTINGS_CHECKBOX_KEYS_MAPPING = {(settings_constants.GAME.NEWBIE_PREBATTLE_HINTS): (NewbieHintsLogItems.CHECKBOX_PREBATTLE_HINTS), 
   (settings_constants.GAME.NEWBIE_BATTLE_HINTS): (NewbieHintsLogItems.CHECKBOX_INBATTLE_HINTS)}
TOOLTIP_ID_MAPPING = {(SettingsNewbieTooltips.PREBATTLE_HINTS): (NewbieHintsLogItems.TOOLTIP_SETTINGS_PREBATTLE_HINTS), 
   (SettingsNewbieTooltips.INBATTLE_HINTS): (NewbieHintsLogItems.TOOLTIP_SETTINGS_INBATTLE_HINTS), 
   (SettingsNewbieTooltips.INBATTLE_HINTS_RESET): (NewbieHintsLogItems.TOOLTIP_SETTINGS_INBATTLE_HINTS_RESET)}
NEWBIE_HINTS_RETICLE_MAPPING = {(settings_constants.AIM.ARCADE): (NewbieHintsLogViews.SETTINGS_ARCADE), 
   (settings_constants.AIM.SNIPER): (NewbieHintsLogViews.SETTINGS_SNIPER)}
NEWBIE_SETTINGS_RETICLE_PARAMS = [
 AimSetting.OPTIONS.GUN_TAG_TYPE]
