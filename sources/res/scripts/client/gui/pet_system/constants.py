PET_NAME_FORMAT = b'petName_{0:d}'
EVENT_NAME_FORMAT = b'event_{0:d}'

class PS_PDATA_KEYS(object):
    ACTIVE_PETID = b'activePetID'
    ACTIVE_STATE_BEHAVIOR = b'activeStateBehavior'
    BONUS = b'bonus'
    EVENTS_DATA = b'eventsData'
    STORAGE = b'storage'
    UNLOCKED_PETS_IDS = b'unlockedPetsIds'
    ACTIVE_BONUS = b'activeBonus'
    APPLIED_BONUSES = b'applied'
    ACTIVE_EVENT = b'activeEvent'
    SELECTED_NAME = b'sSelectedName'
    SYNERGY_STORAGE = b'synergy'
    SYNERGY_POINTS = b'points'
    SYNERGY_LEVEL = b'level'
    SYNERGY_FIRST_CLICK = b'fClick'


class PetPlaceName(object):
    DEFAULT = b'default'
    STORAGE = b'storage'
    ALL = (
     DEFAULT, STORAGE)


class StorageStateKey(object):
    ACTIVE = b'active'
    LOCKED = b'locked'
    ALL = (
     ACTIVE, LOCKED)
