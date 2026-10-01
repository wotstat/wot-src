import constants
from constants_utils import ConstInjector
from enum import IntEnum
from portal.gui.impl.gen.view_models.views.lobby.tooltips.vehicle_crew import CrewId
from portal_common.portal_constants import CampMarkerStatesIDs, TeleportMarkerStatesIDs
PORTAL_BANNER_ENTRY_POINT = b'PortalBannerEntryPoint'
PORTAL_HANGAR_SCENE = b'PORTAL'
PORTAL_HANGAR_SPACE_PATH = b'spaces/h13_mt_portal_2025'
PORTAL_PROGRESSION_CURRENCY = b'razlom_coin'

class ARENA_GUI_TYPE(constants.ARENA_GUI_TYPE, ConstInjector):
    PORTAL = 301


class PORTAL_BATTLE_CTRL_ID(IntEnum):
    PORTAL_MARKERS_CTRL = 100
    EFFECTS_CTRL = 101
    SUPER_BOSS_TRANSITION_CTRL = 102


class PORTAL_GUI_MARKERS_2D(object):
    NO_MARKER = None
    PORTAL_MARKER = b'PortalMarkerUI'
    TRAP_MARKER = b'PortalTrapMarkerUI'
    BASE_MARKER = b'PortalPlayersBaseMarkerUI'
    HOOK_CAMP_MARKER = b'PortalHookCampMarkerUI'
    HORSE_CAMP_MARKER = b'PortalHorseCampMarkerUI'
    PERSPECTIVE_CAMP_MARKER = b'PortalPerspectiveCampMarkerUI'
    SATELITE_CAMP_MARKER = b'PortalSateliteCampMarkerUI'
    HOOK_TP_READY_MARKER = b'PortalHookTpReadyMarkerUI'
    HORSE_TP_READY_MARKER = b'PortalHorseTpReadyMarkerUI'
    PERSPECTIVE_TP_READY_MARKER = b'PortalPerspectiveTpReadyMarkerUI'
    SATELITE_TP_READY_MARKER = b'PortalSateliteTpReadyMarkerUI'
    HOOK_TP_USED_MARKER = b'PortalHookTpMarkerUI'
    HORSE_TP_USED_MARKER = b'PortalHorseTpMarkerUI'
    PERSPECTIVE_TP_USED_MARKER = b'PortalPerspectiveTpMarkerUI'
    SATELITE_TP_USED_MARKER = b'PortalSateliteTpMarkerUI'
    HOOK_TP_COOLDOWN_MARKER = b'PortalHookTpCooldownMarkerUI'
    HORSE_TP_COOLDOWN_MARKER = b'PortalHorseTpCooldownMarkerUI'
    PERSPECTIVE_TP_COOLDOWN_MARKER = b'PortalPerspectiveTpCooldownMarkerUI'
    SATELITE_TP_COOLDOWN_MARKER = b'PortalSateliteTpCooldownMarkerUI'
    BOSS_HP_MARKER = b'PortalVehicleMarker'


class PORTAL_GUI_MARKERS_MINIMAP(object):
    NO_MARKER = None
    BASE_MARKER = b'PortalPlayersBaseMinimapEntryUI'
    PORTAL_MINIMAP_ENTRY = b'PortalMinimapEntryUI'
    TRAP_MINIMAP_ENTRY = b'PortalTrapMinimapEntryUI'
    MINEFIELD_MINIMAP_ENTRY = b'PortalMinefieldMinimapEntryUI'
    BASE_MINIMAP_ENTRY = b'PortalPlayersBaseMinimapEntryUI'
    HOOK_CAMP_MINIMAP_ENTRY = b'PortalHookCampMinimapEntryUI'
    HORSE_CAMP_MINIMAP_ENTRY = b'PortalHorseCampMinimapEntryUI'
    PERSPECTIVE_CAMP_MINIMAP_ENTRY = b'PortalPerspectiveCampMinimapEntryUI'
    SATELITE_CAMP_MINIMAP_ENTRY = b'PortalSateliteCampMinimapEntryUI'
    HOOK_TP_USED_MINIMAP_ENTRY = b'PortalHookTpMinimapEntryUI'
    HORSE_TP_USED_MINIMAP_ENTRY = b'PortalHorseTpMinimapEntryUI'
    PERSPECTIVE_TP_USED_MINIMAP_ENTRY = b'PortalPerspectiveTpMinimapEntryUI'
    SATELITE_TP_USED_MINIMAP_ENTRY = b'PortalSateliteTpMinimapEntryUI'
    HOOK_TP_COOLDOWN_MINIMAP_ENTRY = b'PortalHookTpCooldownMinimapEntryUI'
    HORSE_TP_COOLDOWN_MINIMAP_ENTRY = b'PortalHorseTpCooldownMinimapEntryUI'
    PERSPECTIVE_TP_COOLDOWN_MINIMAP_ENTRY = b'PortalPerspectiveTpCooldownMinimapEntryUI'
    SATELITE_TP_COOLDOWN_MINIMAP_ENTRY = b'PortalSateliteTpCooldownMinimapEntryUI'
    FRONTIER_OBSERVER_INACTIVE = b'PortalFrontierObserverInactiveMinimapEntryUI'
    FRONTIER_OBSERVER_ACTIVE = b'PortalFrontierObserverActiveMinimapEntryUIcopy'


class PORTAL_FRONTIER_MARKERS(object):
    VASILIEVA = {b'camp': {b'markers2d': {(CampMarkerStatesIDs.DEFAULT_CAMP): (PORTAL_GUI_MARKERS_2D.SATELITE_CAMP_MARKER), 
                                (CampMarkerStatesIDs.CAN_BE_CAPTURED): (PORTAL_GUI_MARKERS_2D.SATELITE_CAMP_MARKER), 
                                (CampMarkerStatesIDs.CAPTURED): None}, 
                 b'markersMinimap': {(CampMarkerStatesIDs.DEFAULT_CAMP): (PORTAL_GUI_MARKERS_MINIMAP.SATELITE_CAMP_MINIMAP_ENTRY), 
                                     (CampMarkerStatesIDs.CAN_BE_CAPTURED): (PORTAL_GUI_MARKERS_MINIMAP.SATELITE_CAMP_MINIMAP_ENTRY), 
                                     (CampMarkerStatesIDs.CAPTURED): (PORTAL_GUI_MARKERS_MINIMAP.NO_MARKER)}}, 
       b'teleport': {b'markers2d': {(TeleportMarkerStatesIDs.DEFAULT_TELEPORT): (PORTAL_GUI_MARKERS_2D.SATELITE_TP_READY_MARKER), 
                                    (TeleportMarkerStatesIDs.TELEPORT_OCCUPIED): (PORTAL_GUI_MARKERS_2D.SATELITE_TP_USED_MARKER), 
                                    (TeleportMarkerStatesIDs.TELEPORT_COOLDOWN): (PORTAL_GUI_MARKERS_2D.SATELITE_TP_COOLDOWN_MARKER)}, 
                     b'markersMinimap': {(TeleportMarkerStatesIDs.DEFAULT_TELEPORT): (PORTAL_GUI_MARKERS_MINIMAP.SATELITE_TP_USED_MINIMAP_ENTRY), 
                                         (TeleportMarkerStatesIDs.TELEPORT_OCCUPIED): (PORTAL_GUI_MARKERS_MINIMAP.SATELITE_TP_USED_MINIMAP_ENTRY), 
                                         (TeleportMarkerStatesIDs.TELEPORT_COOLDOWN): (PORTAL_GUI_MARKERS_MINIMAP.SATELITE_TP_COOLDOWN_MINIMAP_ENTRY)}}}
    KOSHCHEEVA = {b'camp': {b'markers2d': {(CampMarkerStatesIDs.DEFAULT_CAMP): (PORTAL_GUI_MARKERS_2D.PERSPECTIVE_CAMP_MARKER), 
                                (CampMarkerStatesIDs.CAN_BE_CAPTURED): (PORTAL_GUI_MARKERS_2D.PERSPECTIVE_CAMP_MARKER), 
                                (CampMarkerStatesIDs.CAPTURED): None}, 
                 b'markersMinimap': {(CampMarkerStatesIDs.DEFAULT_CAMP): (PORTAL_GUI_MARKERS_MINIMAP.PERSPECTIVE_CAMP_MINIMAP_ENTRY), 
                                     (CampMarkerStatesIDs.CAN_BE_CAPTURED): (PORTAL_GUI_MARKERS_MINIMAP.PERSPECTIVE_CAMP_MINIMAP_ENTRY), 
                                     (CampMarkerStatesIDs.CAPTURED): (PORTAL_GUI_MARKERS_MINIMAP.NO_MARKER)}}, 
       b'teleport': {b'markers2d': {(TeleportMarkerStatesIDs.DEFAULT_TELEPORT): (PORTAL_GUI_MARKERS_2D.PERSPECTIVE_TP_READY_MARKER), 
                                    (TeleportMarkerStatesIDs.TELEPORT_OCCUPIED): (PORTAL_GUI_MARKERS_2D.PERSPECTIVE_TP_USED_MARKER), 
                                    (TeleportMarkerStatesIDs.TELEPORT_COOLDOWN): (PORTAL_GUI_MARKERS_2D.PERSPECTIVE_TP_COOLDOWN_MARKER)}, 
                     b'markersMinimap': {(TeleportMarkerStatesIDs.DEFAULT_TELEPORT): (PORTAL_GUI_MARKERS_MINIMAP.PERSPECTIVE_TP_USED_MINIMAP_ENTRY), 
                                         (TeleportMarkerStatesIDs.TELEPORT_OCCUPIED): (PORTAL_GUI_MARKERS_MINIMAP.PERSPECTIVE_TP_USED_MINIMAP_ENTRY), 
                                         (TeleportMarkerStatesIDs.TELEPORT_COOLDOWN): (PORTAL_GUI_MARKERS_MINIMAP.PERSPECTIVE_TP_COOLDOWN_MINIMAP_ENTRY)}}}
    YAGINSKAYA = {b'camp': {b'markers2d': {(CampMarkerStatesIDs.DEFAULT_CAMP): (PORTAL_GUI_MARKERS_2D.HOOK_CAMP_MARKER), 
                                (CampMarkerStatesIDs.CAN_BE_CAPTURED): (PORTAL_GUI_MARKERS_2D.HOOK_CAMP_MARKER), 
                                (CampMarkerStatesIDs.CAPTURED): None}, 
                 b'markersMinimap': {(CampMarkerStatesIDs.DEFAULT_CAMP): (PORTAL_GUI_MARKERS_MINIMAP.HOOK_CAMP_MINIMAP_ENTRY), 
                                     (CampMarkerStatesIDs.CAN_BE_CAPTURED): (PORTAL_GUI_MARKERS_MINIMAP.HOOK_CAMP_MINIMAP_ENTRY), 
                                     (CampMarkerStatesIDs.CAPTURED): (PORTAL_GUI_MARKERS_MINIMAP.NO_MARKER)}}, 
       b'teleport': {b'markers2d': {(TeleportMarkerStatesIDs.DEFAULT_TELEPORT): (PORTAL_GUI_MARKERS_2D.HOOK_TP_READY_MARKER), 
                                    (TeleportMarkerStatesIDs.TELEPORT_OCCUPIED): (PORTAL_GUI_MARKERS_2D.HOOK_TP_USED_MARKER), 
                                    (TeleportMarkerStatesIDs.TELEPORT_COOLDOWN): (PORTAL_GUI_MARKERS_2D.HOOK_TP_COOLDOWN_MARKER)}, 
                     b'markersMinimap': {(TeleportMarkerStatesIDs.DEFAULT_TELEPORT): (PORTAL_GUI_MARKERS_MINIMAP.HOOK_TP_USED_MINIMAP_ENTRY), 
                                         (TeleportMarkerStatesIDs.TELEPORT_OCCUPIED): (PORTAL_GUI_MARKERS_MINIMAP.HOOK_TP_USED_MINIMAP_ENTRY), 
                                         (TeleportMarkerStatesIDs.TELEPORT_COOLDOWN): (PORTAL_GUI_MARKERS_MINIMAP.HOOK_TP_COOLDOWN_MINIMAP_ENTRY)}}}
    TSAREV = {b'camp': {b'markers2d': {(CampMarkerStatesIDs.DEFAULT_CAMP): (PORTAL_GUI_MARKERS_2D.HORSE_CAMP_MARKER), 
                                (CampMarkerStatesIDs.CAN_BE_CAPTURED): (PORTAL_GUI_MARKERS_2D.HORSE_CAMP_MARKER), 
                                (CampMarkerStatesIDs.CAPTURED): None}, 
                 b'markersMinimap': {(CampMarkerStatesIDs.DEFAULT_CAMP): (PORTAL_GUI_MARKERS_MINIMAP.HORSE_CAMP_MINIMAP_ENTRY), 
                                     (CampMarkerStatesIDs.CAN_BE_CAPTURED): (PORTAL_GUI_MARKERS_MINIMAP.HORSE_CAMP_MINIMAP_ENTRY), 
                                     (CampMarkerStatesIDs.CAPTURED): (PORTAL_GUI_MARKERS_MINIMAP.NO_MARKER)}}, 
       b'teleport': {b'markers2d': {(TeleportMarkerStatesIDs.DEFAULT_TELEPORT): (PORTAL_GUI_MARKERS_2D.HORSE_TP_READY_MARKER), 
                                    (TeleportMarkerStatesIDs.TELEPORT_OCCUPIED): (PORTAL_GUI_MARKERS_2D.HORSE_TP_USED_MARKER), 
                                    (TeleportMarkerStatesIDs.TELEPORT_COOLDOWN): (PORTAL_GUI_MARKERS_2D.HORSE_TP_COOLDOWN_MARKER)}, 
                     b'markersMinimap': {(TeleportMarkerStatesIDs.DEFAULT_TELEPORT): (PORTAL_GUI_MARKERS_MINIMAP.HORSE_TP_USED_MINIMAP_ENTRY), 
                                         (TeleportMarkerStatesIDs.TELEPORT_OCCUPIED): (PORTAL_GUI_MARKERS_MINIMAP.HORSE_TP_USED_MINIMAP_ENTRY), 
                                         (TeleportMarkerStatesIDs.TELEPORT_COOLDOWN): (PORTAL_GUI_MARKERS_MINIMAP.HORSE_TP_COOLDOWN_MINIMAP_ENTRY)}}}


PORTAL_VEHICLE_TOOLTIP_DATA = {5120257: {b'damage': 4, 
             b'mobility': 1, 
             b'armor': 4, 
             b'reload': 1, 
             b'hp': 4, 
             b'crewID': (CrewId.KOSHCHEYEV)}, 
   5120321: {b'damage': 2, 
             b'mobility': 4, 
             b'armor': 1, 
             b'reload': 4, 
             b'hp': 2, 
             b'crewID': (CrewId.VASILIEVA)}, 
   5120337: {b'damage': 3, 
             b'mobility': 2, 
             b'armor': 3, 
             b'reload': 3, 
             b'hp': 3, 
             b'crewID': (CrewId.TSAREV)}, 
   5120401: {b'damage': 3, 
             b'mobility': 3, 
             b'armor': 2, 
             b'reload': 3, 
             b'hp': 3, 
             b'crewID': (CrewId.YAGINSKAYA)}}

class PORTAL_VIDEO(object):
    INTRO = b'portal_intro'
    OUTRO = b'portal_outro'
