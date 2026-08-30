from __future__ import absolute_import
from enum import IntEnum
from Math import Vector3
from gui.shared import EVENT_BUS_SCOPE
SCOPE = EVENT_BUS_SCOPE.BATTLE
MARKER_POSITION_ADJUSTMENT = Vector3(0.0, 12.0, 0.0)
MARKERS_COLOR_SCHEME_PREFIX = b'vm_'

class MARKER_SYMBOL_NAME(object):
    VEHICLE_MARKER = b'VehicleMarker'
    TARGET_MARKER = b'TargetMarker'
    EQUIPMENT_MARKER = b'FortConsumablesMarker'
    LOCATION_MARKER = b'LocationMarkerUI'
    ATTENTION_MARKER = b'AttentionMarkerUI'
    SHOOTING_MARKER = b'AimMarkerUI'
    NAVIGATION_MARKER = b'NavigationMarkerUI'
    FLAG_MARKER = b'FlagMarkerUI'
    UNSPOTTED_MARKER_HIT = b'UnspottedMarkerUI'
    SAFE_ZONE_MARKER = b'SafeZoneIndicatorUI'
    STATIC_OBJECT_MARKER = b'StaticObjectMarker'
    TARGET_POINT_MARKER = b'TargetPointMarkerUI'
    STATIC_ARTY_MARKER = b'StaticArtyMarkerUI'
    SECTOR_BASE_TYPE = b'SectorBaseMarkerUI'
    HEADQUARTER_TYPE = b'HeadquarterMarkerUI'
    STEP_REPAIR_MARKER_TYPE = b'ResupplyMarkerUI'
    WAYPOINT_MARKER = b'SectorWaypointMarkerUI'
    SECTOR_WARNING_MARKER = b'SectorWarningMarkerUI'


class DamageType(object):
    FROM_OTHER = 0
    FROM_SQUAD = 1
    FROM_PLAYER = 2


class CommonMarkerType(IntEnum):
    NORMAL = 0
    BASE = 1
    FRONTLINE_BASE = 2
    FRONTLINE_WAYPOINT = 3
    FRONTLINE_HEADQUARTER = 4
    FRONTLINE_WARNING = 5
    LOCATION = 6
    VEHICLE = 7
    TARGET_POINT = 8
