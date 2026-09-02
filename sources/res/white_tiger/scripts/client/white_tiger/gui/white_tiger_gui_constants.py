from __future__ import absolute_import
from gui.Scaleform.daapi.settings import views
from constants_utils import ConstInjector
from gui.prb_control import settings
from gui.battle_control import battle_constants
from gui.battle_control.battle_constants import FEEDBACK_EVENT_ID as _FET
from white_tiger.gui.impl.gen.view_models.views.lobby.hangar_view_model import WhiteTigerVehicles
from white_tiger.gui.impl.gen.view_models.views.lobby.mode_selector.tooltips.mode_selector_tooltips_constants import ModeSelectorTooltipsConstants
from enum import Enum

class FUNCTIONAL_FLAG(settings.FUNCTIONAL_FLAG, ConstInjector):
    WHITE_TIGER = 8589934592L


class PREBATTLE_ACTION_NAME(settings.PREBATTLE_ACTION_NAME, ConstInjector):
    _const_type = str
    WHITE_TIGER = b'whiteTiger'
    WHITE_TIGER_SQUAD = b'whiteTigerSquad'


class SELECTOR_BATTLE_TYPES(settings.SELECTOR_BATTLE_TYPES, ConstInjector):
    _const_type = str
    WHITE_TIGER = b'whiteTiger'


class VIEW_ALIAS(views.VIEW_ALIAS, ConstInjector):
    _const_type = str
    WHITE_TIGER_BATTLE_PAGE = b'whiteTigerBattlePage'
    WHITE_TIGER_SETTINGS_WINDOW = b'whiteTigerSettingsWindow'


class BATTLE_CTRL_ID(battle_constants.BATTLE_CTRL_ID, ConstInjector):
    WT_BATTLE_GUI_CTRL = 103


class FEEDBACK_EVENT_ID(_FET, ConstInjector):
    WT_GAMEPLAY_ACTION = 103
    WT_VEHICLE_MARKER_HEALTH = 104
    WT_VEHICLE_DISCRETE_DAMAGE_RECEIVED = 105


class MINIMAP_CONTAINER_NAME(object):
    WT_DEPLOY = b'deploymentPoints'


WT_HANGAR_SELECTED_VEHICLE = {b'germany:G98_Waffentrager_E100_TLXXL': (WhiteTigerVehicles.BT110), 
   b'germany:G98_Waffentrager_E100_TLXXL_S': (WhiteTigerVehicles.BT220), 
   b'usa:A120_M48A5_hound_TLXXL': (WhiteTigerVehicles.THUNDERBOLT), 
   b'ussr:R97_Object_140_hound_TLXXL': (WhiteTigerVehicles.RESISTOR), 
   b'france:F18_Bat_Chatillon25t_hound_TLXXL': (WhiteTigerVehicles.FOUDRE), 
   b'czech:Cz04_T50_51_Waf_Hound_3DSt': (WhiteTigerVehicles.POJISTKA)}
OVERTIME_COMPONENT_NAME = b'overtimeComponent'
SOUND_REMAPPING_LABEL = b'white_tiger'

class VehicleCharacteristics(Enum):
    PROS = b'pros'
    CONS = b'cons'


WHITE_TIGER_BATTLES_TICKET = b'whiteTigerBattlesTicket'
WHITE_TIGER_STAMP = b'whiteTigerStamp'
WHITE_TIGER_BATTLES_SET = [WHITE_TIGER_BATTLES_TICKET, WHITE_TIGER_STAMP,
 ModeSelectorTooltipsConstants.WHITE_TIGER_BATTLES_CALENDAR_TOOLTIP]
WHITE_TIGER_EARNED_CURRENCY = b'whiteTigerEarnedCurrency'
WT_QUEST_PREFIX = b'wtevent'
WT_BATTLE_QUEST_PREFIX = b'wtevent:battle_quest'
WT_QUEST_BOSS_GROUP_ID = b'wt_group_boss'
WT_QUEST_HUNTER_GROUP_ID = b'wt_group_hunter'
WT_QUEST_HUNTER_SPECIAL_ID = WT_QUEST_HUNTER_GROUP_ID + b'_special'
MAX_VISIBLE_QUESTS = 4
HUNTER_QUEST_CHAINS = [
 WT_QUEST_HUNTER_GROUP_ID + b'_1',
 WT_QUEST_HUNTER_GROUP_ID + b'_2',
 WT_QUEST_HUNTER_GROUP_ID + b'_3',
 WT_QUEST_HUNTER_SPECIAL_ID]
SPECIAL_QUEST_GROUP_IDS = frozenset({WT_QUEST_HUNTER_SPECIAL_ID})

class WTDailyQuestsDecorations(object):
    COUNTER_ICON_KEY = b'counter'


WTDailyQuestDecorationMap = {17740: (WTDailyQuestsDecorations.COUNTER_ICON_KEY)}
TICKET_UI_NAME = b'wtevent_ticket'
LOOTBOX_UI_NAME = b'wtevent_lootBox'
PROGRESSION_COMPLETE_TOKEN = b'wtevent:completed_progress'
