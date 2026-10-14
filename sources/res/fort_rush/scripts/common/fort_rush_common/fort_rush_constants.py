from __future__ import absolute_import
import enum, UnitBase, arena_bonus_type_caps, constants
from constants_utils import ConstInjector, AbstractBattleMode
from enum import Enum
from fort_rush_common.battle_results import fort_rush
from BattleFeedbackCommon import BATTLE_EVENT_TYPE as BET
FORT_RUSH_SCORE_COMPONENT = b'FortRushScoreComponent'
FORT_RUSH_DEVELOPMENT_HELPER = b'FortRushDevelopmentHelper'
FORT_RUSH_VEHICLE_RESPAWN_COMPONENT = b'FortRushVehicleRespawnComponent'
FORT_RUSH_VEHICLE_BATTLE_FEEDBACK_COMPONENT = b'FortRushVehicleBattleFeedbackComponent'
FORT_RUSH_HIGHLIGHTER = b'FortRushHighlighter'
VEHICLE_RESPAWN_COMPONENT = b'VehicleRespawnComponent'
SCORE_COMPONENT = b'ScoreComponent'
CAPTURE_POINT_INVADER_COMPONENT = b'CapturePointInvaderComponent'
FORT_RUSH_VEHICLE_STATS_COLLECTOR = b'FortRushVehicleStatsCollector'
FORT_RUSH_SOUND_PLAYER = b'FortRushSoundPlayerComponent'
FORT_RUSH_PDATA_KEY = b'fortRush'
FORT_RUSH_DAILY_GROUP_KEY = b'fortRushDailyGroup'
CAPTURE_POINT_NO_TEAM = 0

class CaptureStates(enum.IntEnum):
    NEUTRAL = 0
    CAPTURED = 1
    CAPTURING = 3
    DECREASING = 4
    CONTESTED = 5


class FortRushStats(enum.IntEnum):
    CAPTURES = 0
    NEUTRALIZES = 1
    FIRST_CAPTURES = 2
    CAPTOR_KILLS = 3
    ZONE_DAMAGE_DEALT = 4
    LT_NEUTRALIZES = 5
    RAMMING = 6
    HT_DAMAGE = 7
    ATSPG_DAMAGE = 8

    @staticmethod
    def getStringKey(value):
        return _STATS_KEY_MAPPING.get(value)


_STATS_KEY_MAPPING = {(FortRushStats.CAPTURES): b'captures', 
   (FortRushStats.NEUTRALIZES): b'neutralizes', 
   (FortRushStats.FIRST_CAPTURES): b'firstCaptures', 
   (FortRushStats.CAPTOR_KILLS): b'captorKills', 
   (FortRushStats.ZONE_DAMAGE_DEALT): b'zoneDamageDealt', 
   (FortRushStats.LT_NEUTRALIZES): b'LTNeutralizes', 
   (FortRushStats.ATSPG_DAMAGE): b'ATSPGDamage', 
   (FortRushStats.HT_DAMAGE): b'HTDamage', 
   (FortRushStats.RAMMING): b'ramming'}

class CapturePointStateCtxKeys(Enum):
    PREVIOUS_STATE = b'previousState'
    CAPTURABLE_POINT_OWNER_TEAM = b'capturablePointOwnerTeam'
    POINT_NAME = b'pointName'


CAPTURE_POINT_STATE_CONTEXT_TEMPLATE = {(CapturePointStateCtxKeys.PREVIOUS_STATE.value): (CaptureStates.NEUTRAL.name), 
   (CapturePointStateCtxKeys.CAPTURABLE_POINT_OWNER_TEAM.value): CAPTURE_POINT_NO_TEAM, 
   (CapturePointStateCtxKeys.POINT_NAME.value): b''}

class EventStates(enum.Enum):
    START = 0
    PAUSE = 1
    RESUME = 2
    ENDED = 3


class ARENA_GUI_TYPE(constants.ARENA_GUI_TYPE, ConstInjector):
    FORT_RUSH = 103


class ARENA_BONUS_TYPE(constants.ARENA_BONUS_TYPE, ConstInjector):
    FORT_RUSH = 111


class QUEUE_TYPE(constants.QUEUE_TYPE, ConstInjector):
    FORT_RUSH = 112


class PREBATTLE_TYPE(constants.PREBATTLE_TYPE, ConstInjector):
    FORT_RUSH = 111


class UNIT_MGR_FLAGS(UnitBase.UNIT_MGR_FLAGS, ConstInjector):
    FORT_RUSH = 33554432


class ROSTER_TYPE(UnitBase.ROSTER_TYPE, ConstInjector):
    FORT_RUSH = UNIT_MGR_FLAGS.SQUAD | UNIT_MGR_FLAGS.FORT_RUSH


class INVITATION_TYPE(constants.INVITATION_TYPE, ConstInjector):
    FORT_RUSH = PREBATTLE_TYPE.FORT_RUSH


class CLIENT_UNIT_CMD(UnitBase.CLIENT_UNIT_CMD, ConstInjector):
    START_UNIT_FORT_RUSH_BATTLE = 1102


class GameSeasonType(constants.GameSeasonType, ConstInjector):
    FORT_RUSH = 11


class ARENA_BONUS_TYPE_CAPS(arena_bonus_type_caps.ARENA_BONUS_TYPE_CAPS, ConstInjector):
    _const_type = str
    FORT_RUSH = b'FORT_RUSH'


class FINISH_REASON(constants.FINISH_REASON, ConstInjector):
    FORT_RUSH_DRAW = 210
    FORT_RUSH_REASONS = (210,)


class BATTLE_EVENT_TYPE(BET, ConstInjector):
    FORT_RUSH_PERSONAL_SCORE_UPDATE = 103


def injectFinishReasonConst(personality):
    if not any(reason in FINISH_REASON.getExtraAttrs().values() for reason in FINISH_REASON.FORT_RUSH_REASONS):
        FINISH_REASON.inject(personality)
    return


EXTENSION_NAME = b'fort_rush'
EXT_GAME_PARAMS_KEY = b'fort_rush_battles_config'
EXT_MATCHMAKER_GAME_PARAMS_KEY = b'fort_rush_matchmaker_config'
EXT_VISUAL_SCRIPT_PARAMS_KEY = b'fort_rush_visual_script_config'
FORT_RUSH_VEHICLE_TAG = b'fort_rush'
FORT_RUSH_EXCLUDED_TAGS = constants.BATTLE_MODE_VEH_TAGS_EXCEPT_EVENT | {b'testTank', b'maps_training'}
MAX_ELIGIBLE_VEHICLES = 256

class FortRushBattleMode(AbstractBattleMode):
    _PREBATTLE_TYPE = PREBATTLE_TYPE.FORT_RUSH
    _QUEUE_TYPE = QUEUE_TYPE.FORT_RUSH
    _ARENA_BONUS_TYPE = ARENA_BONUS_TYPE.FORT_RUSH
    _ARENA_GUI_TYPE = ARENA_GUI_TYPE.FORT_RUSH
    _INVITATION_TYPE = INVITATION_TYPE.FORT_RUSH
    _BATTLE_MGR_NAME = b'FortRushBattlesMgr'
    _UNIT_MGR_NAME = b'FortRushUnitMgr'
    _UNIT_MGR_FLAGS = UNIT_MGR_FLAGS.FORT_RUSH
    _ROSTER_TYPE = ROSTER_TYPE.FORT_RUSH
    _FAIRPLAY_VEHICLE_BATTLE_STATS_COMPONENT = b'FortRushFairplayVehicleBattleStatsComponent'
    _GAME_PARAMS_KEY = EXT_GAME_PARAMS_KEY
    _SEASON_TYPE_BY_NAME = b'fort_rush_battle'
    _SEASON_TYPE = GameSeasonType.FORT_RUSH
    _BATTLE_RESULTS_CONFIG = fort_rush
    _SM_TYPE_BATTLE_RESULT = b'fortRushBattleResults'
    _SM_TYPES = [_SM_TYPE_BATTLE_RESULT]
    _CLIENT_BANNER_ENTRY_POINT_ALIAS = b'FortRushEntryPoint'
    _NEW_VEHICLES_TAGS = (
     FORT_RUSH_VEHICLE_TAG,)
    _FORBIDDEN_VEHICLE_TAGS = FORT_RUSH_EXCLUDED_TAGS

    @property
    def _rosterClass(self):
        from fort_rush_common.fort_rush_roster_config import FortRushRoster
        return FortRushRoster
