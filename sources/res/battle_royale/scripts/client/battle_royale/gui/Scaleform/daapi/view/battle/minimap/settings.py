from __future__ import absolute_import
from constants import LOOT_TYPE

class BattleRoyaleEntries(object):
    BATTLE_ROYALE_DEATH_ZONE = b'DeathZoneEntry'
    VIEW_RANGE_SECTOR = b'ViewRangeSectorEntry'
    BATTLE_ROYALE_MARKER = b'BRMarkerUI'


class ViewRangeSectorAs3Descr(object):
    AS_ADD_SECTOR = b'as_addSector'
    AS_UPDATE_SECTOR_RADIUS = b'as_updateSectorRadius'
    AS_INIT_ARENA_SIZE = b'as_initArenaSize'


class DeathZonesAs3Descr(object):
    AS_UPDATE_DEATH_ZONES = b'as_updateDeathZones'
    AS_INIT_DEATH_ZONE_SIZE = b'as_initDeathZoneSize'


class MarkersAs3Descr(object):
    AS_UPDATE_RADAR_RADIUS = b'updateRadarRadius'
    AS_PLAY_RADAR_ANIMATION = b'play'
    AS_UPDATE_MARKER = b'updateIcon'
    AS_ADD_MARKER = b'show'
    AS_REMOVE_MARKER = b'hide'
    AS_ADD_MARKER_LOOT_BY_TYPE_ID = {(LOOT_TYPE.BASIC): b'loot', (LOOT_TYPE.ADVANCED): b'improved_loot', 
       (LOOT_TYPE.CORPSE): b'corpse_loot', 
       (LOOT_TYPE.AIRDROP): b'airdrop'}
    AS_ADD_MARKER_LOOT_BIG_BY_TYPE_ID = {(LOOT_TYPE.BASIC): b'loot_big', (LOOT_TYPE.ADVANCED): b'improved_loot_big', 
       (LOOT_TYPE.CORPSE): b'corpse_loot_big', 
       (LOOT_TYPE.AIRDROP): b'airdrop_big'}
    AS_ADD_MARKER_ENEMY_VEHICLE = b'enemyVehicle'
    AS_ADD_MARKER_ENEMY_VEHICLE_BIG = b'enemyVehicle_big'
    AS_ADD_MARKER_SQUAD_VEHICLE = b'squadVehicle'
    AS_ADD_MARKER_BOT_VEHICLE = b'ally_bot_vehicle'
    AS_ADD_MARKER_ENEMY_BOT_VEHICLE = b'botVehicle'
    AS_ADD_MARKER_ENEMY_BOT_VEHICLE_BIG = b'botVehicle_big'
