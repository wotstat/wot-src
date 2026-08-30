from __future__ import absolute_import
from enum import Enum
from gui.impl.gen.resources import R
CONDITION_TEXT_RES = R.strings.challenges.condition
DEFAULT_CONDITION_TEXT_RES = R.strings.challenges.condition.unknown
DEFAULT_CONDITION_TITLE_TEXT_RES = R.strings.challenges.condition.unknown.title
ACHIEVEMENT_TEXT_RES = R.strings.achievements

class TextResKey(str, Enum):
    EVENT_COUNT = b'eventCount'
    MIN_DISTANCE = b'minDistance'
    MAX_DISTANCE = b'maxDistance'
    TITLE = b'title'
    LIMITED_TIME = b'limittedTime'
    WHILE_ENEMY_INVISIBLE = b'whileEnemyInvisible'
    WHILE_INVISIBLE = b'whileInvisible'
    WHILE_FULL_HEALTH = b'whileFullHealth'
    RAMMING = b'ramming'
    TOTAL = b'total'
    WITHIN_VIEW_RANGE = b'withinViewRange'
    COMPARE_WITH_MAX_HEALTH = b'compareWithMaxHealth'
    CLASSES_DIVERSITY = b'classesDiversity'
    CLASSES = b'classes'


class TemplateParam(str, Enum):
    GOAL = b'goal'
    DISTANCE = b'distance'
    TIME_LIMIT = b'timeLimit'
    CLASS_COUNT = b'classCount'
    VEHICLE_CLASS = b'vehicleClass'


class ConditionIcon(str, Enum):
    DEFAULT = b'folder'
    COMPLEX = b'folder'
    DAMAGE_BLOCK = b'damage_block'
    TOP = b'top'
    KILL_VEHICLES = b'kill_vehicles'
    DISCOVER = b'discover'
    HURT_VEHICLES = b'hurt_vehicles'
    RAM = b'ram'
    HIT = b'hit'
    ACHIEVEMENT = b'achievement'
    MODULE_CRIT = b'module_crit'


CHALLENGES_BATTLE_RESULT_ICONS = {b'damageBlockedByArmor': (ConditionIcon.DAMAGE_BLOCK), 
   b'damageDealt': (ConditionIcon.HURT_VEHICLES), 
   b'kills': (ConditionIcon.KILL_VEHICLES), 
   b'spotted': (ConditionIcon.DISCOVER), 
   b'critsCount': (ConditionIcon.MODULE_CRIT), 
   b'spottedBeforeWeBecameSpotted': (ConditionIcon.DISCOVER), 
   b'percentFromTotalTeamDamage': (ConditionIcon.HURT_VEHICLES), 
   b'piercingEnemyHits': (ConditionIcon.HIT)}
