import enum
from items.components.ny_constants import YEARS_INFO, ToySettings
NY_CONFIG_NAME = b'ny_config'
IS_ENABLED = b'isEnabled'

class NyFeaturesConsts(object):
    MACHINE = b'machine'
    CRAFT = b'craft'
    TOY_DESTROY = b'toy_destroy'
    TOY_BUYING = b'toy_buying'
    RAID = b'raid'
    ALL = (
     MACHINE, CRAFT, TOY_DESTROY, TOY_BUYING, RAID)


class NYGeneralConsts(object):
    CONFIG_NAME = b'general_config'
    ATMOSPHERE_LEVEL_LIMITS = b'atmosphereLevelLimits'
    ATMOSPHERE_POINTS_PER_RANK = b'atmospherePointsPerUsedToyRank'
    SMALL_LOOTBOX_ID = b'smallLootBoxId'
    FIRST_ENTRANCE_TOKEN = b'firstEntranceToken'
    PET_VISIBLE = b'petVisible'
    NEW_YEAR_START_DATE = b'newYearStartDate'
    NEW_YEAR_END_DATE = b'newYearEndDate'
    EMERGENCY_DEB = b'emergencyDEB'
    RACCOON_LEVEL_OPEN = b'raccoonLevelOpen'
    RACCOON_INDICATOR_LEVEL_OPEN = b'raccoonIndicatorLevelOpen'
    MAX_DYNAMIC_BONUS_VALUE = b'maxDynamicBonusValue'
    ENABLE_TAMAGOTCHI_SIMULATION = b'enableTamagotchiSimulation'


class MachineConsts(object):
    CONFIG_NAME = b'machine_config'
    ENABLED = IS_ENABLED
    COIN_LOOTBOX_ID = b'coinLootboxId'
    COIN_PRICE = b'coinPrice'


class CraftProbsConsts(object):
    CONFIG_NAME = b'craft_probabilities_config'
    RANK = b'rank'
    SETTING = b'setting'
    TYPE = b'type'
    PROBABILITY = b'probability'
    RANK_PROBABILITIES = b'rankProbabilities'
    SETTING_PROBABILITIES = b'settingProbabilities'
    TYPE_PROBABILITIES = b'typeProbabilities'


class SettingBonusConsts(object):
    CONFIG_NAME = b'settingBonus_config'
    TOY_RATINGS = b'toyRatingByRank'
    COLLECTION_LEVELS_RATING = b'collectionLevelsRating'
    UNIQUE_TOY_LEVELS_RATING = b'uniqueToysLevelsRating'
    ATMOSPHERE_MULTIPLIERS = b'multiplierByAtmosphereLevel'
    BATTLE_BONUSES = b'battleBonuses'
    COLLECTION_BONUSES = b'collectionBonuses'
    UNIQUE_TOYS_BONUSES = b'uniqueToysBonus'


class ToyDecayCostConsts(object):
    CONFIG_NAME = b'toy_decay_cost_config'
    RANKS = b'ranks'
    FRAGMENTS = b'fragments'
    TYPE = b'type'
    TOY_TYPE = b'toyType'
    TOY_TYPES = b'toyTypes'


class CraftCostConsts(object):
    CONFIG_NAME = b'craft_cost_config'
    FILLER_CONVERT_COST = b'fillerConvertCost'
    USUAL_TOYS_COST = b'usualToysCost'
    CRAFT_COST_SECTION = b'craftCost'
    CRAFT_COST_RANDOM_TYPE = b'randomType'
    CRAFT_COST_SPECIFIED_TYPE = b'specifiedType'
    CRAFT_COST_RANDOM_SETTING = b'randomSetting'
    CRAFT_COST_SPECIFIED_SETTING = b'specifiedSetting'
    CRAFT_COST_RANDOM_RANK = b'randomRank'
    CRAFT_COST_SPECIFIED_RANK = b'specifiedRank'
    CRAFT_COST_PAID_FILLER = b'paidFiller'
    CRAFT_COST_SETTINGS = (
     CRAFT_COST_RANDOM_TYPE, CRAFT_COST_SPECIFIED_TYPE,
     CRAFT_COST_RANDOM_SETTING, CRAFT_COST_SPECIFIED_SETTING,
     CRAFT_COST_RANDOM_RANK, CRAFT_COST_PAID_FILLER)
    USUAL_TOYS = {year: (b'ny{}costByRank').format(year) for year in YEARS_INFO.yearsWithCraftDecreasingIter()}
    MEGA_TOYS_COST = b'megaToysCost'
    MEGA_COST_BY_COUNT = b'megaCostByCount'
    MEGA_TOYS = {year: (b'ny{}megaCost').format(year) for year in YEARS_INFO.prevYearsDecreasingIter() if set(ToySettings.MEGA) & set(YEARS_INFO.getCollectionTypesByYear(year))}
    MEGA_TOYS_COSTS = ()
    QUEST_COUNT = b'questCount'


class NyObjectsConsts(object):
    CONFIG_NAME = b'objects_config'
    OBJECTS = b'objects'
    OBJECT_LEVELS = b'levels'
    OBJECT_LEVEL_ID = b'id'
    OBJECT_LEVEL_PRICE = b'price'
    OBJECT_LEVEL_BONUS = b'bonus'
    OBJECT_TOKEN = b'token'


class NyBuyToyConsts(object):
    CONFIG_NAME = b'buy_toy_config'
    TOY_COUNT_FOR_ONE_PURCHASE = b'toyCountForOnePurchase'


class NyRaidConsts(object):
    CONFIG_NAME = b'raid_config'
    COMPONENTS_CONFIG_NAME = b'receipt_components_config'
    RECEIPTS_CONFIG_NAME = b'receipts_config'


@enum.unique
class ReceiptType(enum.IntEnum):
    PUBLIC = 1
    SECRET = 2
    COMPONENT_RECEIPT = 3


class FirstEnterVideosConsts(object):
    CONFIG_NAME = b'first_enter_videos_config'
    VIDEOS = b'videos'
    VIDEO_ID = b'id'
    PRIORITY = b'priority'
    VIDEO_NAME = b'videoName'
    START_DATE = b'startDate'
    END_DATE = b'endDate'
    VISIBLE = b'visible'
    CAN_ESCAPE = b'canEscape'
    UTC = b'utc'
    PRIORITY_GREETING = 1
    PRIORITY_WEEKLY_REPORT = 3


CURRENT_PDATA_KEY = (b'newYear{}').format(YEARS_INFO.CURRENT_YEAR)
