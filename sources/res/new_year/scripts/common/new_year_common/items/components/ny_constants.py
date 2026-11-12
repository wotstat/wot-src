import typing
from enum import Enum, unique
from ExtensionsManager import makeExtensionPath
from constants import ARENA_BONUS_TYPE
_FIRST_YEAR = 18
_CURRENT_YEAR = 27
UNDEFINED_TOY_RANK = 0
MAX_TOY_RANK = 6
MIN_TOY_RANK = 1
MAX_MEGA_TOY_RANK = 1
MAX_PET_TOY_RANK = 1
PREMIUM_TOY = (6,)
NY_FACTOR_BONUS_AVAILABLE_RANGE = (
 ARENA_BONUS_TYPE.REGULAR, ARENA_BONUS_TYPE.EPIC_RANDOM,
 ARENA_BONUS_TYPE.VERSUS_AI, ARENA_BONUS_TYPE.COMP7,
 ARENA_BONUS_TYPE.BATTLE_ROYALE_SOLO, ARENA_BONUS_TYPE.BATTLE_ROYALE_SQUAD,
 ARENA_BONUS_TYPE.SORTIE_2, ARENA_BONUS_TYPE.FORT_BATTLE_2)
PET_TYPE_BY_NAME = {b'nyrfood': b'food', 
   b'nyrfun': b'fun', 
   b'nyractiv': b'activity'}

class ToySettings(object):
    NEW_YEAR = b'NewYear'
    CHRISTMAS = b'Christmas'
    FAIRYTALE = b'Fairytale'
    ORIENTAL = b'Oriental'
    SOVIET = b'soviet'
    TRADITIONAL_WESTERN = b'traditionalWestern'
    MODERN_WESTERN = b'modernWestern'
    ASIAN = b'asian'
    MEGA_TOYS = b'Mega'
    DOG_TOYS = b'Dog'
    RACOON_TOYS = b'Raccoon'
    NEW = (
     NEW_YEAR, CHRISTMAS, FAIRYTALE, ORIENTAL)
    OLD = (SOVIET, TRADITIONAL_WESTERN, MODERN_WESTERN, ASIAN)
    ALL = NEW + OLD
    MEGA = (
     MEGA_TOYS,)
    DOG = (DOG_TOYS,)
    RACOON = (RACOON_TOYS,)
    CURRENT_USUAL = (
     NEW_YEAR,)
    CURRENT_MEGA = ()
    CURRENT_PET = ()


class YEARS(object):
    ALL = tuple(xrange(_FIRST_YEAR, _CURRENT_YEAR + 1))

    @staticmethod
    def getYearNumFromYearStr(yearStr):
        return int(yearStr[-2:])

    @staticmethod
    def getYearStrFromYearNum(yearNum):
        return (b'ny{}').format(yearNum)

    @staticmethod
    def getFullYearNumFromYearStr(yearStr):
        return 2000 + YEARS.getYearNumFromYearStr(yearStr)


for value in YEARS.ALL:
    setattr(YEARS, (b'YEAR{}').format(value), value)

class YEARS_INFO(object):
    FIRST_YEAR = YEARS.ALL[0]
    CURRENT_YEAR = YEARS.ALL[-1]
    CURRENT_YEAR_STR = YEARS.getYearStrFromYearNum(CURRENT_YEAR)
    CURRENT_YEAR_FULL = YEARS.getFullYearNumFromYearStr(CURRENT_YEAR_STR)
    YearType = typing.Union[str, int]
    _COLLECTION_TYPES_BY_YEAR = {(YEARS.YEAR18): (ToySettings.OLD), 
       (YEARS.YEAR19): (ToySettings.NEW), 
       (YEARS.YEAR20): (ToySettings.NEW + ToySettings.MEGA), 
       (YEARS.YEAR21): (ToySettings.NEW + ToySettings.MEGA), 
       (YEARS.YEAR22): (ToySettings.NEW + ToySettings.MEGA), 
       (YEARS.YEAR23): (ToySettings.NEW + ToySettings.DOG), 
       (YEARS.YEAR24): (ToySettings.NEW), 
       (YEARS.YEAR25): ((
                      ToySettings.NEW_YEAR,) + ToySettings.RACOON), 
       (YEARS.YEAR26): ((
                      ToySettings.NEW_YEAR,) + ToySettings.RACOON), 
       (YEARS.YEAR27): ((
                      ToySettings.NEW_YEAR,) + ToySettings.RACOON)}
    _COLLECTION_KEY_BY_YEAR = {year: b'nyToys' if year == _CURRENT_YEAR else (b'ny{}Toys').format(year) for year in YEARS.ALL}
    CURRENT_SETTINGS = _COLLECTION_TYPES_BY_YEAR[CURRENT_YEAR]
    CURRENT_SETTING_IDS_BY_NAME = {name: idx for idx, name in enumerate(CURRENT_SETTINGS)}
    _MAX_TOY_RANK_BY_YEAR = {(YEARS.YEAR18): 5, 
       (YEARS.YEAR19): 5, 
       (YEARS.YEAR20): 5, 
       (YEARS.YEAR21): 5, 
       (YEARS.YEAR22): 1, 
       (YEARS.YEAR23): 1, 
       (YEARS.YEAR24): 5, 
       (YEARS.YEAR25): 6, 
       (YEARS.YEAR26): 6, 
       (YEARS.YEAR27): 6}
    _TOY_COLLECTION_BYTES_BY_YEAR = {(YEARS.YEAR18): 37, 
       (YEARS.YEAR19): 41, 
       (YEARS.YEAR20): 50, 
       (YEARS.YEAR21): 47, 
       (YEARS.YEAR22): 36, 
       (YEARS.YEAR23): 21, 
       (YEARS.YEAR24): 42, 
       (YEARS.YEAR25): 22, 
       (YEARS.YEAR26): 21, 
       (YEARS.YEAR27): 21}
    _YEAR_OFFSET = 4
    _COLLECTION_TYPES_RANGES = None
    _TOY_COLLECTION_OFFSETS = None
    _COLLECTION_SETTING_IDS_BY_NAME = None

    @staticmethod
    def convertYearToNum(year):
        if isinstance(year, str):
            year = YEARS.getYearNumFromYearStr(year)
        return year

    @staticmethod
    def getToyCollectionBytesForYear(year):
        year = YEARS_INFO.convertYearToNum(year)
        return YEARS_INFO._TOY_COLLECTION_BYTES_BY_YEAR[year]

    @classmethod
    def getToyCollectionMaxToyID(cls, year):
        return cls.getToyCollectionBytesForYear(year) * 8 - 1

    @classmethod
    def currYearMaxToyRank(cls):
        return cls.getMaxToyRankByYear(cls.CURRENT_YEAR)

    @staticmethod
    def getMaxToyRankByYear(year):
        year = YEARS_INFO.convertYearToNum(year)
        return YEARS_INFO._MAX_TOY_RANK_BY_YEAR[year]

    @staticmethod
    def getCollectionTypesByYear(year, useMega=True, usePet=True):
        year = YEARS_INFO.convertYearToNum(year)
        collectionTypes = YEARS_INFO._COLLECTION_TYPES_BY_YEAR[year]
        if not useMega:
            collectionTypes = [x for x in collectionTypes if x != ToySettings.MEGA_TOYS]
        if not usePet:
            collectionTypes = [x for x in collectionTypes if x != ToySettings.RACOON_TOYS]
        return collectionTypes

    @staticmethod
    def prevYearsDecreasingIter():
        for year in xrange(YEARS_INFO.CURRENT_YEAR - 1, YEARS_INFO.FIRST_YEAR - 1, -1):
            yield year

        return

    @staticmethod
    def yearsWithCraftDecreasingIter():
        for year in xrange(YEARS.YEAR24, YEARS_INFO.FIRST_YEAR - 1, -1):
            yield year

        return

    @staticmethod
    def allYearsDecreasingIter():
        for year in xrange(YEARS_INFO.CURRENT_YEAR, YEARS_INFO.FIRST_YEAR - 1, -1):
            yield year

        return

    @staticmethod
    def _checkCorrectYearNum(year):
        return YEARS_INFO.FIRST_YEAR <= year <= YEARS_INFO.CURRENT_YEAR

    @staticmethod
    def getCollectionSettingIDsByYear(year):
        if YEARS_INFO._COLLECTION_SETTING_IDS_BY_NAME is None:
            YEARS_INFO._initCollectionSettingIDsByName()
        year = YEARS_INFO.convertYearToNum(year)
        return YEARS_INFO._COLLECTION_SETTING_IDS_BY_NAME[year]

    @staticmethod
    def getToyCollectionOffsetForYear(year):
        if YEARS_INFO._TOY_COLLECTION_OFFSETS is None:
            YEARS_INFO._initToyCollectionOffsets()
        year = YEARS_INFO.convertYearToNum(year)
        return YEARS_INFO._TOY_COLLECTION_OFFSETS[year]

    @staticmethod
    def getCollectionKeyForYear(year):
        year = YEARS_INFO.convertYearToNum(year)
        return YEARS_INFO._COLLECTION_KEY_BY_YEAR[year]

    @staticmethod
    def getYearStrFromToysCollectionKey(collectionKey):
        if collectionKey == YEARS_INFO.getCollectionKeyForYear(YEARS_INFO.CURRENT_YEAR):
            return YEARS_INFO.CURRENT_YEAR_STR
        return collectionKey[:YEARS_INFO._YEAR_OFFSET]

    @staticmethod
    def getToyBonusTagForYear(year):
        year = YEARS_INFO.convertYearToNum(year)
        if year == YEARS_INFO.CURRENT_YEAR:
            return b'nyToy'
        return (b'ny{}Toy').format(year)

    @staticmethod
    def getCollectionDistributionsRangeForYear(year):
        if YEARS_INFO._COLLECTION_TYPES_RANGES is None:
            YEARS_INFO._initCollectionTypesRanges()
        year = YEARS_INFO.convertYearToNum(year)
        return YEARS_INFO._COLLECTION_TYPES_RANGES[year]

    @staticmethod
    def getCollectionIntID(collectionStrID):
        year, collectionID = YEARS_INFO.splitCollectionStrID(collectionStrID)
        beg, _ = YEARS_INFO.getCollectionDistributionsRangeForYear(year)
        return beg + collectionID

    @staticmethod
    def splitCollectionStrID(collectionStrID):
        return (
         collectionStrID[:YEARS_INFO._YEAR_OFFSET], int(collectionStrID[YEARS_INFO._YEAR_OFFSET:]))

    @staticmethod
    def getCollectionSettingID(setting, year):
        settingIDs = YEARS_INFO.getCollectionSettingIDsByYear(year)
        return year + str(settingIDs[setting])

    @staticmethod
    def getCollectionSettingNameAndYear(collectionStrID):
        yearStr, idx = YEARS_INFO.splitCollectionStrID(collectionStrID)
        year = YEARS_INFO.convertYearToNum(yearStr)
        return (YEARS_INFO._COLLECTION_TYPES_BY_YEAR[year][idx], yearStr)

    @staticmethod
    def _initCollectionTypesRanges():
        YEARS_INFO._COLLECTION_TYPES_RANGES = {}
        beg = 0
        for year in YEARS_INFO.allYearsDecreasingIter():
            end = beg + len(YEARS_INFO._COLLECTION_TYPES_BY_YEAR[year])
            YEARS_INFO._COLLECTION_TYPES_RANGES[year] = (beg, end)
            beg = end

        return

    @staticmethod
    def _initToyCollectionOffsets():
        YEARS_INFO._TOY_COLLECTION_OFFSETS = {}
        offset = 0
        for year in YEARS_INFO.allYearsDecreasingIter():
            YEARS_INFO._TOY_COLLECTION_OFFSETS[year] = offset
            offset += YEARS_INFO.getToyCollectionBytesForYear(year)

        return

    @staticmethod
    def _initCollectionSettingIDsByName():
        YEARS_INFO._COLLECTION_SETTING_IDS_BY_NAME = {}
        for year in YEARS_INFO.allYearsDecreasingIter():
            collection = YEARS_INFO._COLLECTION_TYPES_BY_YEAR[year]
            YEARS_INFO._COLLECTION_SETTING_IDS_BY_NAME[year] = {name: idx for idx, name in enumerate(collection)}

        return


COLLECTION_SLOTS_XML_PATH = makeExtensionPath(b'new_year', b'/scripts/item_defs/current_ny/slots.xml')
TOYS_TRANSFORMATIONS_XML_PATH = makeExtensionPath(b'new_year', b'scripts/item_defs/current_ny/slot_toy_pairs.xml')
VARIADIC_DISCOUNTS_XML_PATH = makeExtensionPath(b'new_year', b'scripts/item_defs/current_ny/variadic_discounts.xml')
TOKEN_VARIADIC_DISCOUNT_PREFIX = (b'ny{}:vd').format(YEARS_INFO.CURRENT_YEAR)
NEW_YEAR_QUEST_GROUP_ID = (b'ny{}:groupQuest').format(YEARS_INFO.CURRENT_YEAR)
PREV_NY_TOYS_COLLECTIONS = [(b'ny{}Toys').format(prevYear) for prevYear in YEARS_INFO.prevYearsDecreasingIter()]
ALL_NY_TOYS_BONUSES = [YEARS_INFO.getToyBonusTagForYear(nyYear) for nyYear in YEARS_INFO.allYearsDecreasingIter()]
LEVEL_REWARD_ID_TEMPLATE = b'{}:level:{}'
COLLECTION_REWARD_ID_TEMPLATE = b'{}:cr:{}:complete'
ONBOARDING_QUEST_ID = (b'{}:onboarding_gift').format(YEARS_INFO.CURRENT_YEAR_STR)
RANDOM_TYPE = b'random'
TOKEN_MANDARIN = (b'ny{}_mandarin').format(YEARS_INFO.CURRENT_YEAR)
TOKEN_LOOTBOX_FRAGMENT = b'nyLootboxFragment'
ENT_TAMAGOCHI = b'ny_racoon_unlock'
NY_PET_FOOD_CURRENCY = b'nyPetGoodies'

@unique
class FillerState(Enum):
    INACTIVE = 0
    USE_CHARGES = 1
    USE_SHARDS = 2
    ERROR = -1

    @property
    def isActive(self):
        return self in (self.USE_SHARDS,)


class CurrentNYConstants(object):
    TOYS = b'nyToys'
    TOY_BONUS = b'nyToy'
    TOY_FRAGMENTS = b'nyToyFragments'
    ATMOSPHERE_POINTS = b'nyAtmospherePoints'
    FILLERS = b'nyFillers'
    ANY_OF = b'nyAnyOf'
    ALL_OF = b'nyAllOf'
    NEW_TOYS = b'newNYToys'
    IP_TYPE_CUSTOM_TOYS = (b'custom/{}').format(TOYS)
    IP_TYPE_CUSTOM_ANYOF_TOYS = (b'custom/{}').format(ANY_OF)
    MANDARINS = b'nyMandarins'
    TOY_COMPENSATION = b'NYComp'
    IP_TYPE_CUSTOM_MANDATINS = (b'custom/{}').format(MANDARINS)
    IP_TYPE_CUSTOM_CURRENCIES = b'custom/currencies'
    NY_CELEB_QUESTS_PREFIX = (b'NY{}_clbty:').format(YEARS_INFO.CURRENT_YEAR)
    NY_DAILY_QUESTS_PREFIX = (b'NY{}_clbty:daily').format(YEARS_INFO.CURRENT_YEAR)
    NY_WEEKLY_QUESTS_PREFIX = (b'NY{}_clbty:weekly').format(YEARS_INFO.CURRENT_YEAR)
    NY_WEEKLY_COMMON_QUESTS_PREFIX = (b'NY{}_clbty:weekly_common').format(YEARS_INFO.CURRENT_YEAR)
    NY_QUESTS_PREFIX = (b'NY{}').format(YEARS_INFO.CURRENT_YEAR)
    MAX_CELEB_TEXTS = 8
    HIDDEN_VEHICLE = b'hidden_vehicle'
    NY_STATIC_DOGTAG = b'nyStaticDogTag'
    TOY_REWARD_ITEM_ID = 24


class NewYearObjects(object):
    CITY_VIEW = b'CityView'


class CustomizationObjects(object):
    FIR = b'Fir'
    INSTALLATIONS = b'Installations'
    FAIR = b'Fair'
    TEREM = b'Terem'
    SNOW_SLIDE = b'SnowSlide'
    FIREWORKS = b'Fireworks'
    WITHOUT_MEGA = (
     FIR, TEREM, INSTALLATIONS, FAIR, SNOW_SLIDE, FIREWORKS)
    ALL = WITHOUT_MEGA
    WITH_RANDOM = ALL + (RANDOM_TYPE,)
    PANEL_OBJECTS_ORDER = (
     INSTALLATIONS, FIR, TEREM, SNOW_SLIDE, FAIR, FIREWORKS)


TOY_OBJECTS_IDS_BY_NAME = {name: idx for idx, name in enumerate(CustomizationObjects.ALL)}

class ToyTypes(object):
    ATTRACTION = b'attraction'
    BALL = b'ball'
    DECORATION = b'decoration'
    EXPOSITION = b'exposition'
    FLOOR = b'floor'
    GARLAND = b'garland'
    GARLAND_FIR = b'garland_fir'
    GARLAND_FAIR = b'garland_fair'
    GARLAND_INSTALLATION = b'garland_installation'
    KIOSK = b'kiosk'
    KITCHEN = b'kitchen'
    PAVILION = b'pavilion'
    PYRO = b'pyro'
    SCULPTURE = b'sculpture'
    GROUND_LIGHT = b'ground_light'
    SCULPTURE_LIGHT = b'sculpture_light'
    SNOW_ITEM = b'snow_item'
    TABLE = b'table'
    TENT = b'tent'
    TOP = b'top'
    TREES = b'trees'
    LIGHTS_HOUSES = b'lights_houses'
    LIGHTS_FIR = b'lights_fir'
    SKATING = b'skating'
    FIREWORKS = b'fireworks'
    SNOW_SLIDE = b'snowslide'
    TEREM = b'terem'
    FENCE = b'fence'
    AIR_BALLOON = b'air_balloon'
    BRIDGE = b'bridge'
    AIRSHIP = b'airship'
    CASTLE = b'castle'
    FERRIS_WHEEL = b'ferris_wheel'
    MEGA_COMMON = b'mega'
    MEGA_FIR = b'mega_fir'
    MEGA_ILLUMINATION = b'mega_illumination'
    MEGA_INSTALLATION = b'mega_installation'
    MEGA_TABLEFUL = b'mega_tableful'
    DOG_TOY = b'dog_toy'
    DOG_BOWL = b'dog_bowl'
    DOG_HOUSE = b'dog_house'
    DOG_COLLAR = b'dog_collar'
    PET_TOY = b'pet_toy'
    PET_FOOD = b'pet_food'
    PET_BED = b'pet_bed'
    PET_INTERACTIVE = b'pet_interactive'
    USUAL_TYPES = (
     TOP, GARLAND_FIR, BALL, FLOOR, TEREM, FENCE, SCULPTURE, TENT, TABLE, FIREWORKS, SNOW_SLIDE)
    MEGA = ()
    PET = ()
    ALL = USUAL_TYPES + PET


MEGA_TOY_TYPES = ToyTypes.MEGA
TOY_USUAL_TYPES = ToyTypes.USUAL_TYPES
PET_TOY_TYPES = ToyTypes.PET
TOY_TYPES = ToyTypes.ALL
TOY_TYPE_IDS_BY_NAME = {name: idx for idx, name in enumerate(TOY_TYPES)}
TOY_TYPES_WITH_RANDOM = (RANDOM_TYPE,) + TOY_TYPES
RANDOM_VALUE = -1
INVALID_TOY_ID = -1
OBJECT_MIN_LEVEL = 1
OBJECT_MAX_LEVEL = 5

class NY_STATE(object):
    NOT_STARTED = b'not_started'
    IN_PROGRESS = b'in_progress'
    SUSPENDED = b'suspended'
    POST_EVENT = b'post_event'
    FINISHED = b'finished'
    ENABLED = (
     IN_PROGRESS, SUSPENDED)
    ALL = (NOT_STARTED, IN_PROGRESS, SUSPENDED, POST_EVENT, FINISHED)


MAX_ATMOSPHERE_LVL = 11
MIN_ATMOSPHERE_LVL = 0
MIN_TANK_SLOTS_LVL = 5
MAX_COLLECTION_LEVEL = 5
NY_BRANCH_MIN_LEVEL = 5
NY_BRANCH_MAX_LEVEL = 10
TOY_TYPES_BY_OBJECT_WITHOUT_MEGA = {(CustomizationObjects.FIR): (
                              ToyTypes.TOP,
                              ToyTypes.GARLAND_FIR,
                              ToyTypes.BALL,
                              ToyTypes.FLOOR), 
   (CustomizationObjects.TEREM): (
                                ToyTypes.TEREM,
                                ToyTypes.FENCE), 
   (CustomizationObjects.FAIR): (
                               ToyTypes.TENT,
                               ToyTypes.TABLE), 
   (CustomizationObjects.INSTALLATIONS): (
                                        ToyTypes.SCULPTURE,), 
   (CustomizationObjects.SNOW_SLIDE): (
                                     ToyTypes.SNOW_SLIDE,), 
   (CustomizationObjects.FIREWORKS): (
                                    ToyTypes.FIREWORKS,)}
TOY_TYPES_BY_OBJECT = dict(TOY_TYPES_BY_OBJECT_WITHOUT_MEGA, **{})
TOY_TYPES_BY_OBJECT_WITH_RANDOM = dict(TOY_TYPES_BY_OBJECT_WITHOUT_MEGA, **{RANDOM_TYPE: (
               RANDOM_TYPE,)})
TOY_TYPES_FOR_OBJECTS_WITHOUT_MEGA = tuple(toyType for custObj in CustomizationObjects.WITHOUT_MEGA for toyType in TOY_TYPES_BY_OBJECT_WITHOUT_MEGA[custObj])
TOY_TYPES_FOR_OBJECTS_WITH_RANDOM_WITHOUT_MEGA = (
 RANDOM_TYPE,) + TOY_TYPES_FOR_OBJECTS_WITHOUT_MEGA

class TOY_SEEN_MASK(object):
    NONE = 0
    INVENTORY = 1
    COLLECTION = 16
    ANY = INVENTORY | COLLECTION


class TOY_CRAFT_LOG_OFFSET(object):
    FILLER = 0
    RANK = 1
    SETTING = 2
    TYPE = 3

    @classmethod
    def getLogValue(cls, toyTypeID, settingID, rank, filler):
        sourceID = (toyTypeID != RANDOM_VALUE) << cls.TYPE
        sourceID |= (settingID != RANDOM_VALUE) << cls.SETTING
        sourceID |= (rank != RANDOM_VALUE) << cls.RANK
        sourceID |= filler << cls.FILLER
        return str(sourceID)


INV_TOYS_DEFAULT_VALUE = (0, 0, 0)

class TOY_PARAMETER(object):
    TOY_USUAL_TYPES_RANGE = list(range(len(TOY_USUAL_TYPES)))
    CURRENT_USUAL_RANGE = list(range(len(ToySettings.CURRENT_USUAL)))
    RANK_CURRENT_USUAL_RANGE = list(range(MIN_TOY_RANK, YEARS_INFO.currYearMaxToyRank() + 1))
    USUAL_PARAMS = (
     TOY_USUAL_TYPES_RANGE, CURRENT_USUAL_RANGE, RANK_CURRENT_USUAL_RANGE)
    PET_TOY_START_INDEX = len(TOY_USUAL_TYPES_RANGE)
    PET_TOY_TYPES_RANGE = list(range(PET_TOY_START_INDEX, PET_TOY_START_INDEX + len(PET_TOY_TYPES)))
    PET_SETTINGS_START_INDEX = len(CURRENT_USUAL_RANGE)
    CURRENT_PET_RANGE = list(range(PET_SETTINGS_START_INDEX, PET_SETTINGS_START_INDEX + len(ToySettings.CURRENT_PET)))
    RANK_CURRENT_PET_RANGE = list(range(MIN_TOY_RANK, MAX_PET_TOY_RANK + 1))
    PET_PARAMS = (
     PET_TOY_TYPES_RANGE, CURRENT_PET_RANGE, RANK_CURRENT_PET_RANGE)


DYNAMIC_BONUS_CURRENCY = b'nydeb'

class RaidState(object):
    ACTIVE = 0
    FINISHED = 1
    NOT_ACTIVE = 2
