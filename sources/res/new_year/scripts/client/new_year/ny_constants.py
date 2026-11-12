import itertools
from enum import Enum
from new_year.interactive_state_machine.constants import PersonaTypes
from new_year_common.items.components.ny_constants import CurrentNYConstants, CustomizationObjects, PREV_NY_TOYS_COLLECTIONS, YEARS, YEARS_INFO, ToyTypes
from shared_utils import CONST_CONTAINER

class NewYearLootBoxes(CONST_CONTAINER):
    PREMIUM_OLD = b'newYear_premium'
    SPECIAL_OLD = b'newYear_special'
    SPECIAL_AUTO = b'newYear_special_auto'
    COMMON_OLD = b'newYear_usual'
    NY_24_STANDARD = b'ny_2024_VI'
    NY_24_NEW_YEAR = b'ny_2024_newyear'
    NY_24_XMAS = b'ny_2024_christmas'
    NY_24_EASTERN = b'ny_2024_eastern'
    NY_24_MAGIC = b'ny_2024_magic'
    NY_CUR_YEAR_SMALL = (b'ny_{}_small').format(YEARS_INFO.CURRENT_YEAR_FULL)
    NY_CUR_YEAR_TANKS = (b'ny_{}_tanks').format(YEARS_INFO.CURRENT_YEAR_FULL)
    NY_CUR_YEAR_BIG = (b'ny_{}_big').format(YEARS_INFO.CURRENT_YEAR_FULL)
    PREMIUM = (
     PREMIUM_OLD, NY_24_NEW_YEAR, NY_24_XMAS, NY_24_EASTERN, NY_24_MAGIC)
    COMMON = (COMMON_OLD, NY_24_STANDARD)
    SPECIAL = (SPECIAL_OLD, SPECIAL_AUTO)

    @classmethod
    def getIterator(cls):
        return itertools.chain(cls.PREMIUM, cls.COMMON, cls.SPECIAL)

    @classmethod
    def ALL(cls):
        return tuple(cls.getIterator())


class NewYearLootBoxRewards(object):
    NY_CUR_YEAR_TANKS = (b'ny_{}_tanks').format(YEARS_INFO.CURRENT_YEAR_FULL)
    VEHICLES = {NY_CUR_YEAR_TANKS: b'legendary', 
       b'A175_OTAC_MT_58_02': b'tank_main', 
       b'tank_leaderboard': b'tank_leaderboard'}
    CUSTOMIZATIONS = {b'customizations_7990860': b'3dstyle_02', 
       b'customizations_8001356': b'3dstyle_03'}
    ALL = {}
    for rewards in (VEHICLES, CUSTOMIZATIONS):
        ALL.update(rewards)


class NewYearCategories(CONST_CONTAINER):
    NEWYEAR_24 = b'ny_2024'
    NEWYEAR_25 = b'ny_2025'
    NEWYEAR_26 = b'ny_2026'
    NEWYEAR_27 = b'ny_2027'


ALL_LUNAR_NY_LOOT_BOX_TYPES = (b'lunar_base', b'lunar_simple', b'lunar_special')
LUNAR_NY_LOOT_BOXES_CATEGORIES = b'LunarNY'

class AnchorNames(CONST_CONTAINER):
    SNOW_SCULPTURE = b'SnowSculpture'
    TREE = b'ChristmasTree'
    TEREM = b'Terem'
    SNOW_SLIDE = b'SnowSlide'
    FIELD_KITCHEN = b'FieldKitchen'
    FIREWORKS = b'Fireworks'
    HEROTANK = b'HeroTank'
    LEVEL_UP_CAMERA = b'LevelUpCamera'
    CHALLENGE = b'Challenge'
    RACCOON = b'Raccoon'
    GRIMVAGEN = b'Grimvagen'
    MACHINE = b'Machine'


class InternalViewState(CONST_CONTAINER):
    DEFAULT = b''
    TREE = b'ChristmasTree'
    TREE_TOP = b'ChristmasTree_Top'
    TREE_DOWN = b'ChristmasTree_Toy_Down'
    FIELD_KITCHEN = b'FieldKitchen'
    TEREM = b'Terem'
    SNOW_SLIDE = b'SnowSlide'
    SNOW_SCULPTURE = b'SnowSculpture'
    FIREWORKS = b'Fireworks'
    MACHINE_MAIN = b'MachineMain'
    MACHINE_REWARDING = b'MachineRewarding'
    VEHICLE_MACHINE_REWARDING = b'VehicleMachineRewarding'
    CHALLENGE = b'Challenge'
    RACCOON = b'Raccoon'
    RACCOON_FLY = b'Raccoon_fly'
    RACCOON_TV = b'RaccoonTV'
    GRIMVAGEN_MAIN = b'GrimvagenMain'
    ONBOARDING_DEFAULT = b'onboarding_default'
    ONBOARDING_FIR = b'onboarding_fir'
    ONBOARDING_PANORAMA = b'onboarding_panorama'


class InternalViewStateID(object):
    DEFAULT = 0
    TREE = 1
    FIELD_KITCHEN = 2
    TEREM = 3
    SNOW_SLIDE = 4
    SNOW_SCULPTURE = 5
    FIREWORKS = 6
    MACHINE_MAIN = 7
    MACHINE_REWARDING = 9
    VEHICLE_MACHINE_REWARDING = 10
    CHALLENGE = 11
    RACCOON = 12

    @classmethod
    def stateToID(cls, name, default=None):
        stateKey = InternalViewState.getKeyByValue(name)
        return getattr(cls, stateKey, default)


ANCHOR_TO_OBJECT = {(AnchorNames.SNOW_SCULPTURE): (CustomizationObjects.INSTALLATIONS), 
   (AnchorNames.TREE): (CustomizationObjects.FIR), 
   (AnchorNames.TEREM): (CustomizationObjects.TEREM), 
   (AnchorNames.SNOW_SLIDE): (CustomizationObjects.SNOW_SLIDE), 
   (AnchorNames.FIELD_KITCHEN): (CustomizationObjects.FAIR), 
   (AnchorNames.FIREWORKS): (CustomizationObjects.FIREWORKS)}
OBJECT_TO_ANCHOR = {v: k for k, v in ANCHOR_TO_OBJECT.iteritems()}
OBJECT_TO_VIEW_SATE = {(CustomizationObjects.FIR): (InternalViewState.TREE), 
   (CustomizationObjects.FAIR): (InternalViewState.FIELD_KITCHEN), 
   (CustomizationObjects.INSTALLATIONS): (InternalViewState.SNOW_SCULPTURE), 
   (CustomizationObjects.TEREM): (InternalViewState.TEREM), 
   (CustomizationObjects.SNOW_SLIDE): (InternalViewState.SNOW_SLIDE), 
   (CustomizationObjects.FIREWORKS): (InternalViewState.FIREWORKS)}
MAX_LEVEL = 11
TOY_PREFIX = b'toy_'
NY_LEVEL_PREFIX = (b'ny{}:level').format(YEARS_INFO.CURRENT_YEAR)
NY_PREORDER_REWARDS_QUEST_ID = b'pre_ny_rewards_quest'
TOY_COLLECTIONS = PREV_NY_TOYS_COLLECTIONS + [CurrentNYConstants.TOYS]
NY_COLLECTION_PREFIXES = (b'ny19:cr', b'ny20:cr', b'ny21:cr', b'ny22:cr', b'ny23:cr', b'ny24:cr')
NY_COLLECTION_MEGA_PREFIX = b'ny22:cr:mega'
NY_OLD_COLLECTION_PREFIX = b'ny18:cr'
NY_MARKETPLACE_UNLOCK_ENTITLEMENT = (b'ny{}_marketplace_unlock').format(YEARS_INFO.CURRENT_YEAR)
TANK_SLOT_BONUS_ORDER = [
 b'xpFactor', b'tankmenXPFactor', b'freeXPFactor']
NY_EMBEDDED_AUDIO_VIDEO_NOTIFICATION_LOCK_KEY = b'nyEmbeddedAudioVideo'
NY_ONBOARDING_NOTIFICATION_LOCK_KEY = b'nyOnboarding'
NY_INVOICE_TAG_PREFIX = (b'ny{}').format(YEARS_INFO.CURRENT_YEAR)
NY_INVOICE_LEADERBOARD_REWARD_PREFIX = (b'{}_leaderboard_').format(NY_INVOICE_TAG_PREFIX)
NY_INVOICE_PET_RAID_REWARD_PREFIX = (b'{}_pet_raid').format(NY_INVOICE_TAG_PREFIX)
NY_LEADERBOARD_CUMULATIVE_TAG_SUFFIXES = (b'cumulative',)
NY_CUMULATIVE_LEADERBOARD_SEASON_ID = 0

class Collections(CONST_CONTAINER):
    NewYear27 = YEARS.getYearStrFromYearNum(27)
    NewYear26 = YEARS.getYearStrFromYearNum(26)
    NewYear25 = YEARS.getYearStrFromYearNum(25)
    NewYear24 = YEARS.getYearStrFromYearNum(24)
    NewYear23 = YEARS.getYearStrFromYearNum(23)
    NewYear22 = YEARS.getYearStrFromYearNum(22)
    NewYear21 = YEARS.getYearStrFromYearNum(21)
    NewYear20 = YEARS.getYearStrFromYearNum(20)
    NewYear19 = YEARS.getYearStrFromYearNum(19)
    NewYear18 = YEARS.getYearStrFromYearNum(18)
    CURRENT = YEARS.getYearStrFromYearNum(YEARS_INFO.CURRENT_YEAR)


class SyncDataKeys(CONST_CONTAINER):
    INVENTORY_TOYS = b'inventoryToys'
    SLOTS = b'slots'
    TOY_FRAGMENTS = b'toyFragments'
    MAX_LEVEL = b'maxLevel'
    POINTS = b'atmospherePoints'
    TOY_COLLECTION = b'toyCollection'
    COLLECTION_DISTRIBUTIONS = b'collectionDistributions'
    ALBUMS = b'albums'
    FILLERS = b'fillers'
    MAX_BONUS = b'maxReachedSettingBonus'
    MAX_BONUS_VALUE = b'value'
    MAX_BONUS_INFO = b'info'
    SELECTED_DISCOUNTS = b'selectedDiscounts'
    NY_TAMAGOTCHI_RAID = b'tamagotchiRaidW'
    RAID_CURRENT = b'currentRaid'
    RAID_DISCLOSED_RECEIPTS = b'disclosedReceipts'
    RAID_RECEIPT_LIMITS = b'receiptLimits'
    RAID_STATISTICS = b'statistics'
    RAID_BOOST_AMOUNT = b'boostAmount'


class FormulaInfo(object):
    MULTIPLIER = 0
    COLLECTION_BONUS = 1
    MEGA_TOYS_BONUS = 2


class NyWidgetTopMenu(object):
    CITY = b'city'
    SURPRISE_MACHINE = b'surprise_machine'
    LEADERS = b'leaders'
    QUESTS = b'quests'
    PET = b'pet'
    INFO = b'info'
    LEFT = ()
    RIGHT = (CITY, PET, LEADERS, SURPRISE_MACHINE, QUESTS, INFO)
    ALL = LEFT + RIGHT


class NyTabBarRewardsView(object):
    FOR_LEVELS = b'forLevels'
    COLLECTION_NY27 = Collections.NewYear27
    COLLECTIONS = (
     COLLECTION_NY27,)
    ALL = (
     FOR_LEVELS,) + COLLECTIONS


class NyTabBarAlbumsView(object):
    NY_2027 = Collections.NewYear27
    ALL = (
     NY_2027,)


PERCENT = 100.0

class ViewAliases(CONST_CONTAINER):
    CITY_VIEW = b'NyCityView'
    LEADERS_VIEW = b'NyLeaderboardView'
    QUESTS_VIEW = b'NyQuestView'
    SURPRISE_MACHINE_VIEW = b'NySurpriseMachineView'
    REWARDS_VIEW = b'NyRewardsInfoView'
    PET_VIEW = b'NyPetView'
    INFO_VIEW = b'NyInfoView'
    ONBOARDING_VIEW = b'NyOnboardingView'
    TANK_CUSTOMIZATION = b'Customization'


ANCHOR_TO_VIEW_ALIAS = {(AnchorNames.MACHINE): (ViewAliases.SURPRISE_MACHINE_VIEW), 
   (AnchorNames.CHALLENGE): (ViewAliases.LEADERS_VIEW), 
   (AnchorNames.RACCOON): (ViewAliases.PET_VIEW), 
   (AnchorNames.GRIMVAGEN): (ViewAliases.QUESTS_VIEW)}
NEW_YEAR = (b'{}newYearSettings').format(YEARS_INFO.CURRENT_YEAR)
NY_LEADERBOARD_INFO_SEEN = b'NyLeaderboardInfoSeen'
NY_CAN_BUY_ZONE = b'NyCanBuyZone'
NY_QUESTS_UPDATED_AT = b'NyQuestsUpdatedAt'
NY_IS_FIRST_MACHINE_TOKEN = b'NyIsFirstMachineToken'
NY_DAILY_QUESTS_VISITED = b'NYDailyQuestsVisited'
NY_OLD_COLLECTIONS_BY_YEAR_VISITED = b'NYOldCollectionsByYearVisited'
NY_OLD_REWARDS_BY_YEAR_VISITED = b'NYOldRewardsByYearVisited'
NY_LAST_SEEN_LEVEL_INFO = b'NYLastSeenLevelInfo'
NY_LAST_SEEN_TOTAL_BONUS = b'NYLastSeenTotalBonus'
NY_ACTIVE_WIDGET_TRANSITION_SHOWN = b'NyActiveWidgetTransitionShown'
NY_FIRST_ENTER_VIDEOS_SEEN = b'NYFirstEnterVideosSeen'
NY_LEADERBOARD_TANK_REWARD_STATE = b'NYLeaderboardTankRewardState'
NY_ENVIRONMENT_STATE = b'NYEnvironmentState'
NY_ENV_SWITCHER_BTN_TIP_SKIPPED = b'NYSwitcherBtnTipSkipped'
NY_HAS_PET_ANIMATION = b'NYHasPetAnimation'
NY_IS_CELEB_VOICEOVERS_ENABLED = b'NyIsCelebVoiceoversEnabled'
NY_IS_QUESTS_CELEB_VOICEOVERS_ENABLED = b'NyIsQuestsCelebVoiceoversEnabled'
NY_IS_MACHINE_CELEB_VOICEOVERS_ENABLED = b'NyIsMachineCelebVoiceoversEnabled'
NY_WEEK_IN_QUESTS_VISITED = b'NyWeekInQuestsVisited'
NY_IS_LEADERBOARD_REWARDS_CHECKED = b'NyIsLeaderboardRewardsChecked'
NY_IS_SECRET_REWARDS_CHECKED = b'NyIsSecretRewardsChecked'
NY_BIG_BOX_COUNT = b'NyBigBoxCount'
NY_SEEN_QUESTS = b'NySeenQuests'
NY_TAMAGOTCHI_SEEN_TIPS = b'nyTamagotchiSeenTips'
NY_TAMAGOTCHI_REPEAT_ONBOARDING_COUNT = b'nyTamagotchiRepeatOnboardingCount'
NY_TAMAGOTCHI_RAID_REPEAT_ONBOARDING_COUNT = b'nyTamagotchiRaidRepeatOnboardingCount'
INTERACTIVE_STATE_MACHINE = b'interactiveStateMachine'
FIRST_ENTRANCE = b'firstEntrance'
GREETINGS_TIMESTAMP = b'greetingsTimestamp'
WEEKLY_GREETINGS_COUNT = b'weeklyGreetingsCount'
COOL_REWARD_COUNT = b'coolRewardCount'
SIMPLE_REWARD_COUNT = b'simpleRewardCount'
ACCOUNT_DEFAULT_SETTINGS = {NEW_YEAR: {NY_CAN_BUY_ZONE: {customizationZone: False for customizationZone in CustomizationObjects.ALL}, NY_QUESTS_UPDATED_AT: 0, 
              NY_IS_FIRST_MACHINE_TOKEN: False, 
              NY_LEADERBOARD_INFO_SEEN: False, 
              NY_DAILY_QUESTS_VISITED: False, 
              NY_OLD_COLLECTIONS_BY_YEAR_VISITED: {18: False, 
                                                   19: False, 
                                                   20: False, 
                                                   21: False, 
                                                   22: False, 
                                                   23: False, 
                                                   24: False}, 
              NY_OLD_REWARDS_BY_YEAR_VISITED: {18: False, 
                                               19: False, 
                                               20: False, 
                                               21: False, 
                                               22: False, 
                                               23: False, 
                                               24: False}, 
              NY_LAST_SEEN_LEVEL_INFO: {b'level': 1, 
                                        b'points': 0}, 
              NY_SEEN_QUESTS: (list()), 
              NY_LAST_SEEN_TOTAL_BONUS: 0, 
              NY_ACTIVE_WIDGET_TRANSITION_SHOWN: False, 
              NY_FIRST_ENTER_VIDEOS_SEEN: (set()), 
              NY_LEADERBOARD_TANK_REWARD_STATE: {}, NY_ENV_SWITCHER_BTN_TIP_SKIPPED: False, 
              NY_HAS_PET_ANIMATION: True, 
              NY_IS_CELEB_VOICEOVERS_ENABLED: True, 
              NY_IS_QUESTS_CELEB_VOICEOVERS_ENABLED: True, 
              NY_IS_MACHINE_CELEB_VOICEOVERS_ENABLED: True, 
              NY_WEEK_IN_QUESTS_VISITED: 0, 
              NY_ENVIRONMENT_STATE: None, 
              NY_IS_LEADERBOARD_REWARDS_CHECKED: False, 
              NY_IS_SECRET_REWARDS_CHECKED: False, 
              NY_BIG_BOX_COUNT: 0, 
              NY_TAMAGOTCHI_SEEN_TIPS: (set()), 
              NY_TAMAGOTCHI_REPEAT_ONBOARDING_COUNT: 0, 
              NY_TAMAGOTCHI_RAID_REPEAT_ONBOARDING_COUNT: 0, 
              INTERACTIVE_STATE_MACHINE: {(PersonaTypes.CELEB_MAN): {FIRST_ENTRANCE: True, 
                                                                     GREETINGS_TIMESTAMP: 0, 
                                                                     WEEKLY_GREETINGS_COUNT: (-1), 
                                                                     COOL_REWARD_COUNT: (-1), 
                                                                     SIMPLE_REWARD_COUNT: (-1)}, 
                                          (PersonaTypes.CELEB_WOMAN): {FIRST_ENTRANCE: True, 
                                                                       GREETINGS_TIMESTAMP: 0, 
                                                                       WEEKLY_GREETINGS_COUNT: (-1)}, 
                                          (PersonaTypes.OLD_MAN): {FIRST_ENTRANCE: False, 
                                                                   GREETINGS_TIMESTAMP: 0, 
                                                                   WEEKLY_GREETINGS_COUNT: (-1)}}}}

class NySurpriseMachineStates(object):
    MACHINE = b'Machine'
    BUTTONS = b'Buttons'


TOY_TO_CAMERA = {(ToyTypes.TOP): (InternalViewState.TREE_TOP), 
   (ToyTypes.GARLAND_FIR): (InternalViewState.TREE), 
   (ToyTypes.BALL): (InternalViewState.TREE), 
   (ToyTypes.FLOOR): (InternalViewState.TREE_DOWN)}

class TamagotchiState(Enum):
    SAD = b'sad'
    NORMAL = b'normal'
    FUN = b'fun'


class EnvironmentState(Enum):
    DAY = b'Day'
    AUTO = b'Auto'
    NIGHT = b'Night'
    RACCOON = b'Raccoon'
