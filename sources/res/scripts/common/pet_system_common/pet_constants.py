from __future__ import absolute_import
from future.utils import viewitems
from dossiers2.custom.records import RECORD_DB_IDS
PETS_SYSTEM_CONFIG = b'pets_system_config'
PETS_SYSTEM_PDATA_KEY = b'pets_system'
PET_STORAGE_CAMERA_NAME = b'DogStorage'
PET_CAMERA_NAME = b'Dog'
PET_RTPC_DOG_TYPE = b'RTPC_ext_pet_system_dog_type'

class PetSystemGeneralConsts(object):
    CONFIG_NAME = b'pets_general_config'
    ENABLED = b'isEnabled'
    EVENT_PER_DAY = b'eventsMaxPerDay'
    EVENT_MIN_BATTLES = b'eventsMinBattles'
    EVENT_MAX_BATTLES = b'eventsMaxBattles'
    BONUSES_PER_DAY = b'bonusesPerDay'
    SHOW_CASE_ENABLED = b'isShowCaseEnabled'


class PetsConsts(object):
    CONFIG_NAME = b'pets_config'
    PETS = b'pets'
    PET = b'pet'
    PET_ID = b'id'
    PET_TYPE = b'type'
    PET_PREFAB = b'prefab'
    PET_BATTLE_PREFAB = b'battlePrefab'
    PET_BREED = b'breed'
    PET_EVENTS = b'events'
    PET_EVENT_IDS = b'eventIDs'
    PET_BONUSES = b'bonuses'
    PET_BONUS_IDS = b'bonusIDs'
    PET_NAMES = b'names'
    PET_NAMES_DEFAULT = b'default'
    PET_NAMES_DEFAULT_LOCKED = b'defaultLocked'
    PET_NAMES_UNLOCKED = b'unlockedNamesIDs'
    PET_SYNERGY_GROUP_ID = b'synergyGroupID'
    PET_PRICE = b'price'
    PET_NOT_IN_SHOP = b'notInShop'
    STOCK_NAMES = b'stockNames'


class PetPromoConsts(object):
    CONFIG_NAME = b'pet_promotion'
    IS_ENABLED = b'isEnabled'
    PETS = b'pets'
    PET = b'pet'
    PET_ID = b'id'
    URL = b'url'
    SOURCES = b'sources'
    SHOP_URL = b'shopUrl'
    INGAME_LINK = b'ingameLink'


class PetEventTypeConsts(object):
    BASIC = b'basic'
    UNIQUE = b'unique'


class PetEventsConsts(object):
    CONFIG_NAME = b'pets_events'
    EVENTS = b'events'
    EVENT = b'event'
    EVENT_ID = b'id'
    EVENT_TYPE = b'type'
    EVENT_REWARD = b'rewardID'


class PetBonusesConsts(object):
    CONFIG_NAME = b'pets_bonuses'
    BONUSES = b'bonuses'
    BONUS = b'bonus'
    BONUS_ID = b'id'
    BONUS_RESOURCE = b'bonusResource'
    EMPTY_BONUS = (
     0, 0, False)


class PET_SYSTEM_BONUS_RESOURCE_TYPE(object):
    UNKNOWN = 0
    CREDITS = 1


PET_SYSTEM_BONUS_TEXT_TO_RESOURCE = {b'unknown': (PET_SYSTEM_BONUS_RESOURCE_TYPE.UNKNOWN), 
   b'credits': (PET_SYSTEM_BONUS_RESOURCE_TYPE.CREDITS)}
PET_SYSTEM_RESOURCE_TO_TEXT = {v: k for k, v in viewitems(PET_SYSTEM_BONUS_TEXT_TO_RESOURCE)}

class SYNERGY_POINTS_TYPE(object):
    EVENT_INTERACTION = b'eventInteraction'
    FIRST_CLICK = b'firstClick'
    SERVER_ONLY = (
     EVENT_INTERACTION,)
    ALL = (
     EVENT_INTERACTION, FIRST_CLICK)


SYNERGY_POINTS_TYPE_TO_IDX = {key: idx for idx, key in enumerate(SYNERGY_POINTS_TYPE.ALL, 1)}
SYNERGY_POINTS_IDX_TO_TYPE = {idx: key for key, idx in viewitems(SYNERGY_POINTS_TYPE_TO_IDX)}

class PetSynergyConsts(object):
    CONFIG_NAME = b'pets_synergy'
    POINTS = b'points'
    SYNERGIES = b'synergies'
    SYNERGY = b'synergy'
    SYNERGY_ID = b'id'
    SYNERGY_LEVELS = b'levels'
    DECAY_DAYS = b'decayDays'
    DECAY_POINTS = b'decayPoints'


class PetStateBehavior(object):
    BASIC = 0
    CALM = 1
    HIDDEN = 2
    ALL = (
     BASIC, CALM, HIDDEN)


class PetTrigger(object):
    LOGIN = b'login'
    TO_STORAGE = b'toStorage'
    FROM_STORAGE = b'fromStorage'
    MEDAL = b'medal'
    FIRST_CLICK = b'firstClick'
    TO_EVENT_SCREEN = b'toEventScreen'
    FROM_EVENT_SCREEN = b'fromEventScreen'
    PBH_HIGHLIGHT = b'pbhHighlight'
    ALL = (
     LOGIN, TO_STORAGE, FROM_STORAGE, MEDAL, FIRST_CLICK, TO_EVENT_SCREEN, FROM_EVENT_SCREEN, PBH_HIGHLIGHT)


class StorageStaticTrigger(object):
    EMPTY = 0
    DISABLED = 1
    IDLE = 2


class AnimationStateName(object):
    DEFAULT = b'default'
    DISABLED = b'disabled'
    HIDDEN = b'hidden'
    PROMOTION = b'promotion'
    ALL = (
     DEFAULT, DISABLED, HIDDEN, PROMOTION)


class PetStaticTrigger(object):
    AFK = 0
    IDLE = 1
    EVENT = 2


class PetHangarObject(object):
    STORAGE = b'petStorage'
    PET = b'pet'
    ALL = (
     STORAGE, PET)


class PetAchievementAnimation(object):
    Warrior = RECORD_DB_IDS[(b'achievements', b'warrior')]


class PetSounds(object):
    PET_EVENT_HIGHLIGHT = b'pet_system_event_highlight'
    HIGHLIGHT = b'highlight'
