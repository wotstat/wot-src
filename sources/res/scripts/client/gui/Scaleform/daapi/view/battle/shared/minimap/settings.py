from enum import Enum
from account_helpers.settings_core.options import MinimapVehModelsSetting, MinimapHPSettings
from gui.Scaleform.genConsts.LAYER_NAMES import LAYER_NAMES
from shared_utils import BitmaskHelper
MINIMAP_COMPONENT_PATH = (b'_level0.root.{}.main.minimap.entriesContainer').format(LAYER_NAMES.VIEWS)
MINIMAP_MIN_SIZE_INDEX = 0
MINIMAP_MAX_SIZE_INDEX = 5
MINIMAP_WAS_SPOTTED_RESET_DELAY = 5.0

class CONTAINER_NAME(object):
    TEAM_POINTS = b'points'
    ICONS = b'icons'
    EQUIPMENTS = b'equipments'
    DEAD_VEHICLES = b'deadVehicles'
    ALIVE_VEHICLES = b'aliveVehicles'
    PERSONAL = b'personal'
    FLAGS = b'flags'
    ZONES = b'zones'
    PROTECTION_ZONE = b'landingZone'
    HQS = b'hqs'
    WT_DEPLOY = b'deploymentPoints'


class ENTRY_SYMBOL_NAME(object):
    ALLY_TEAM_BASE = b'AllyTeamBaseEntry'
    ENEMY_TEAM_BASE = b'EnemyTeamBaseEntry'
    ALLY_TEAM_SPAWN = b'AllyTeamSpawnEntry'
    ENEMY_TEAM_SPAWN = b'EnemyTeamSpawnEntry'
    CONTROL_POINT = b'ControlPointEntry'
    BOOTCAMP_TARGET = b'BootcampTargetEntry'
    ARTILLERY_ENTRY = b'ArtilleryEntry'
    ARTILLERY_YELLOW_ENTRY = b'ArtilleryYellowEntry'
    AOE_ARTILLERY_ENTRY = b'AOEArtilleryMinimapEntry'
    BOMBER_ENTRY = b'BomberEntry'
    RECON_ENTRY = b'ReconEntry'
    SMOKE_ENTRY = b'SmokeEntry'
    VEHICLE = b'VehicleEntry'
    VIEW_POINT = b'ViewPointEntry'
    DEAD_POINT = b'DeadPointEntry'
    VIDEO_CAMERA = b'VideoCameraEntry'
    DIRECTION_ENTRY = b'DirectionEntry'
    RECTANGLE_AREA = b'RectangleAreaMinimapEntry'
    VIEW_RANGE_CIRCLES = b'ViewRangeCirclesEntry'
    ANIMATION = b'AnimationEntry'
    MARK_OBJECTIVE_DEF = b'PositionDefendEntry'
    MARK_OBJECTIVE_ATK = b'PositionAttackEntry'
    MARK_OBJECTIVE_REPLY_DEF = b'PositionDefendReplyEntry'
    MARK_OBJECTIVE_REPLY_ATK = b'PositionAttackReplyEntry'
    MARK_POSITION = b'PositionFlashEntry'
    THERMAL_VISION_ENTRY = b'ThermalVisionEntry'
    ARTY_MARKER = b'ArtyMarkerMinimapEntry'
    ARTY_HIT_DOT_MARKER = b'ArtyHitDotMarkerUI'
    LOCATION_MARKER = b'MarkGoingToPositionEntryUI'
    ATTENTION_MARKER = b'MarkAttentionEntryUI'
    SHOOTING_POINT_MARKER = b'ShootingPointEntryUI'
    NAVIGATION_POINT_MARKER = b'NavigationPointEntryUI'
    FLAG_POINT_MARKER = b'FlagPointEntryUI'
    EPIC_SECTOR_ENEMY_BASE = b'SectorBaseEnemyEntry'
    EPIC_SECTOR_ALLY_BASE = b'SectorBaseAllyEntry'
    EPIC_HQ_ENEMY = b'HeadquarterEnemyEntry'
    EPIC_HQ_ALLY = b'HeadquarterAllyEntry'
    EPIC_SECTOR = b'SectorEntry'
    EPIC_SECTOR_OVERLAY = b'SectorOverlayEntry'
    EPIC_HQ = b'HeadquarterEntry'
    EPIC_FLP = b'FrontLinePointEntry'
    EPIC_REPAIR = b'ResupplyEntry'
    EPIC_PROTECTION_ZONE = b'LandingZoneEntry'
    EPIC_DEPLOY_SECTOR_BASE_ALLY = b'SectorBaseEntryDeploymentAlly'
    EPIC_DEPLOY_SECTOR_BASE_ENEMY = b'SectorBaseEntryDeploymentEnemy'
    EPIC_DEPLOY_HQ_ALLY = b'HeadquarterEntryDeploymentAlly'
    EPIC_DEPLOY_HQ_ENEMY = b'HeadquarterEntryDeploymentEnemy'
    RADAR_ANIM = b'RadarUI'
    DISCOVERED_ITEM_MARKER = b'net.wg.gui.battle.views.minimap.components.entries.battleRoyale.DiscoveredItemMarker'
    COMP7_RECON = b'Comp7PointReconMinimapEntryUI'


class TRANSFORM_FLAG(object):
    FULL = 4294967295L
    NO_POSITION = 1
    NO_ROTATION = 2
    NO_SCALE = 4
    DEFAULT = FULL ^ NO_SCALE


class CIRCLE_TYPE(object):
    EMPTY = 0
    DRAW_RANGE = 1
    MAX_VIEW_RANGE = 2
    VIEW_RANGE = 4
    MIN_SPOTTING_RANGE = 8


class CIRCLE_STYLE(object):
    ALPHA = 50

    class COLOR(object):
        DRAW_RANGE = 16776960
        MAX_VIEW_RANGE = 16777215
        VIEW_RANGE = 2621223
        MIN_SPOTTING_RANGE = 4499630


class THERMAL_VISION_SECTOR_AS3_DESCR(object):
    AS_INIT_MAP_SIZE = b'as_initMapSize'
    AS_SET_SETTINGS = b'as_setSectorSettings'
    AS_UPDATE_STATE = b'as_updateSectorState'
    AS_UPDATE_VISIBILITY = b'as_updateSectorVisibility'


class VIEW_RANGE_CIRCLES_AS3_DESCR(object):
    AS_ADD_MAX_DRAW_CIRCLE = b'as_addDrawRange'
    AS_ADD_DYN_CIRCLE = b'as_addDynamicViewRange'
    AS_ADD_MAX_VIEW_CIRCLE = b'as_addMaxViewRage'
    AS_ADD_MIN_SPOTTING_CIRCLE = b'as_addMinSpottingRange'
    AS_UPDATE_DYN_CIRCLE = b'as_updateDynRange'
    AS_DEL_MAX_DRAW_CIRCLE = b'as_delDrawRange'
    AS_DEL_DYN_CIRCLE = b'as_delDynRange'
    AS_DEL_MAX_VIEW_CIRCLE = b'as_delMaxViewRage'
    AS_DEL_MIN_SPOTTING_CIRCLE = b'as_delMinSpottingRange'
    AS_INIT_ARENA_SIZE = b'as_initArenaSize'
    AS_REMOVE_ALL_CIRCLES = b'as_removeAllCircles'


EQ_MARKER_TO_SYMBOL = {b'artillery': (ENTRY_SYMBOL_NAME.ARTILLERY_ENTRY), 
   b'artillery_yellow': (ENTRY_SYMBOL_NAME.ARTILLERY_YELLOW_ENTRY), 
   b'artillery_fort_ally': (ENTRY_SYMBOL_NAME.AOE_ARTILLERY_ENTRY), 
   b'artillery_fort_enemy': (ENTRY_SYMBOL_NAME.AOE_ARTILLERY_ENTRY), 
   b'bomber': (ENTRY_SYMBOL_NAME.BOMBER_ENTRY), 
   b'recon': (ENTRY_SYMBOL_NAME.RECON_ENTRY), 
   b'smoke': (ENTRY_SYMBOL_NAME.SMOKE_ENTRY)}

class SettingsTypes(Enum):
    MinimapVehicles = 0
    MinimapHitPoint = 1


class ADDITIONAL_FEATURES(BitmaskHelper):
    OFF = 0
    BY_REQUEST = 1
    DO_REQUEST = 2
    ALWAYS = 4

    @classmethod
    def isOn(cls, mask):
        return cls.DO_REQUEST & mask > 0 or cls.ALWAYS & mask > 0

    @classmethod
    def isChanged(cls, mask):
        return cls.BY_REQUEST & mask > 0


def convertSettingToFeatures(value, previous, settingsType):
    if settingsType == SettingsTypes.MinimapVehicles:
        options = MinimapVehModelsSetting.OPTIONS
        indices = MinimapVehModelsSetting.VEHICLE_MODELS_TYPES
        selected = indices[value]
    else:
        options = MinimapHPSettings.Options
        selected = MinimapHPSettings.Options(value)
    result = ADDITIONAL_FEATURES.OFF
    if selected == options.ALT:
        result = ADDITIONAL_FEATURES.BY_REQUEST
    elif selected == options.ALWAYS:
        result = ADDITIONAL_FEATURES.ALWAYS
    if previous & ADDITIONAL_FEATURES.DO_REQUEST > 0:
        result |= ADDITIONAL_FEATURES.DO_REQUEST
    return result


def clampMinimapSizeIndex(index):
    return min(max(index, MINIMAP_MIN_SIZE_INDEX), MINIMAP_MAX_SIZE_INDEX)


MINIMAP_ATTENTION_SOUND_ID = b'minimap_attention'
