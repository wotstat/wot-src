import base64, cPickle as pickle, copy, logging
from copy import deepcopy
import BigWorld, WWISE, CommandMapping, Event, Settings, constants, nations
from account_helpers import gameplay_ctx
from account_helpers.settings_core.settings_constants import AIM, BattleCommStorageKeys, CONTOUR, GAME, GuiSettingsBehavior, SOUND, SPGAim, ScorePanelStorageKeys, SETTINGS_GROUP, MARKERS, MARKER_SETTINGS, CONTROLS, GRAPHICS
from aih_constants import CTRL_MODE_NAME
from constants import MAX_VEHICLE_LEVEL, VEHICLE_CLASSES
from debug_utils import LOG_CURRENT_EXCEPTION
from gui.Scaleform.genConsts.MISSIONS_CONSTANTS import MISSIONS_CONSTANTS
from gui.Scaleform.genConsts.PROFILE_CONSTANTS import PROFILE_CONSTANTS
from gui.Scaleform.genConsts.STORE_CONSTANTS import STORE_CONSTANTS
from gui.collection.collections_constants import COLLECTIONS_UPDATED_ENTRY_SEEN, COLLECTION_RENEW_SEEN, COLLECTION_START_SEEN
from gui.integrated_auction.constants import AUCTION_FINISH_STAGE_SEEN, AUCTION_STAGE_START_SEEN
from gui.black_market.constants import BLACK_MARKET_VEHICLE_STAGE_START_SEEN, BLACK_MARKET_VEHICLE_FINISH_STAGE_SEEN, BLACK_MARKET_STAGE_START_SEEN, BLACK_MARKET_FINISH_STAGE_SEEN
from gui.prb_control.settings import SELECTOR_BATTLE_TYPES
from gui.shop_sales_event.constants import TRADING_CARAVAN_REFILL_SEEN
from gui.custom_notifications.constants import CUSTOM_NOTIFICATIONS_SEEN
from helpers import dependency, getClientVersion
from items.components.crew_books_constants import CREW_BOOK_RARITY
from skeletons.account_helpers.settings_core import ISettingsCore
from soft_exception import SoftException
from uilogging.settings.constants import SettingsLogActions
_logger = logging.getLogger(__name__)
KEY_FILTERS = b'filters'
KEY_SESSION_SETTINGS = b'session_settings'
KEY_SETTINGS = b'settings'
KEY_FAVORITES = b'favorites'
KEY_COUNTERS = b'counters'
KEY_NOTIFICATIONS = b'notifications'
KEY_UI_FLAGS = b'ui_flags'
KEY_MANUAL = b'manual'
CAROUSEL_FILTER_1 = b'CAROUSEL_FILTER_1'
CAROUSEL_FILTER_2 = b'CAROUSEL_FILTER_2'
CAROUSEL_FILTER_CLIENT_1 = b'CAROUSEL_FILTER_CLIENT_1'
MISSION_SELECTOR_FILTER = b'MISSION_SELECTOR_FILTER'
PM_SELECTOR_FILTER = b'PM_SELECTOR_FILTER'
RANKED_CAROUSEL_FILTER_1 = b'RANKED_CAROUSEL_FILTER_1'
RANKED_CAROUSEL_FILTER_2 = b'RANKED_CAROUSEL_FILTER_2'
RANKED_CAROUSEL_FILTER_CLIENT_1 = b'RANKED_CAROUSEL_FILTER_CLIENT_1'
RANKED_IS_VOIP_IN_BATTLE_ACTIVATED = b'rankedIsVoipInBattleActivated'
EPICBATTLE_CAROUSEL_FILTER_1 = b'EPICBATTLE_CAROUSEL_FILTER_1'
EPICBATTLE_CAROUSEL_FILTER_2 = b'EPICBATTLE_CAROUSEL_FILTER_2'
EPICBATTLE_CAROUSEL_FILTER_CLIENT_1 = b'EPICBATTLE_CAROUSEL_FILTER_CLIENT_1'
EPICBATTLE_CAROUSEL_FILTER_CLIENT_2 = b'EPICBATTLE_CAROUSEL_FILTER_CLIENT_2'
STORAGE_VEHICLES_CAROUSEL_FILTER_1 = b'STORAGE_CAROUSEL_FILTER_1'
STORAGE_BLUEPRINTS_CAROUSEL_FILTER = b'STORAGE_BLUEPRINTS_CAROUSEL_FILTER'
BATTLEPASS_CAROUSEL_FILTER_1 = b'BATTLEPASS_CAROUSEL_FILTER_1'
BATTLEPASS_CAROUSEL_FILTER_CLIENT_1 = b'BATTLEPASS_CAROUSEL_FILTER_CLIENT_1'
ROYALE_CAROUSEL_FILTER_1 = b'ROYALE_CAROUSEL_FILTER_1'
ROYALE_CAROUSEL_FILTER_2 = b'ROYALE_CAROUSEL_FILTER_2'
ROYALE_CAROUSEL_FILTER_CLIENT_1 = b'ROYALE_CAROUSEL_FILTER_CLIENT_1'
ROYALE_INTRO_VIDEO_SHOWN = b'ROYALE_INTRO_VIDEO_SHOWN'
MAPBOX_CAROUSEL_FILTER_1 = b'MAPBOX_CAROUSEL_FILTER_1'
MAPBOX_CAROUSEL_FILTER_2 = b'MAPBOX_CAROUSEL_FILTER_2'
MAPBOX_CAROUSEL_FILTER_CLIENT_1 = b'MAPBOX_CAROUSEL_FILTER_CLIENT_1'
FUN_RANDOM_CAROUSEL_FILTER_1 = b'FUN_RANDOM_CAROUSEL_FILTER_1'
FUN_RANDOM_CAROUSEL_FILTER_2 = b'FUN_RANDOM_CAROUSEL_FILTER_2'
FUN_RANDOM_CAROUSEL_FILTER_CLIENT_1 = b'FUN_RANDOM_CAROUSEL_FILTER_CLIENT_1'
COMP7_CAROUSEL_FILTER_1 = b'COMP7_CAROUSEL_FILTER_1'
COMP7_CAROUSEL_FILTER_2 = b'COMP7_CAROUSEL_FILTER_2'
COMP7_CAROUSEL_FILTER_CLIENT_1 = b'COMP7_CAROUSEL_FILTER_CLIENT_1'
COMP7_PREBATTLE_CAROUSEL_ROW_VALUE = b'comp7PrebattleCarouselRowValue'
COMP7_PREBATTLE_MINIMAP_SIZE = b'comp7PrebattleMinimapSize'
COMP7_IS_VOIP_IN_BATTLE_ACTIVATED = b'comp7IsVoipInBattleActivated'
VERSUS_AI_CAROUSEL_FILTER_1 = b'VERSUS_AI_CAROUSEL_FILTER_1'
VERSUS_AI_CAROUSEL_FILTER_2 = b'VERSUS_AI_CAROUSEL_FILTER_2'
VERSUS_AI_CAROUSEL_FILTER_CLIENT_1 = b'VERSUS_AI_CAROUSEL_FILTER_CLIENT_1'
BARRACKS_FILTER = b'barracks_filter'
ORDERS_FILTER = b'ORDERS_FILTER'
CURRENT_VEHICLE = b'current'
ROYALE_VEHICLE = b'ROYALE_VEHICLE'
BOOTCAMP_VEHICLE = b'BOOTCAMP_VEHICLE'
LOBBY_MENU_MANUAL_TRIGGER_SHOWN = b'lobby_menu_manual_trigger_shown'
LOBBY_MENU_BOOTCAMP_TRIGGER_SHOWN = b'lobby_menu_bootcamp_trigger_shown'
MANUAL_NEW_CONTENT = b'manual_new_content'
GUI_START_BEHAVIOR = b'GUI_START_BEHAVIOR'
EULA_VERSION = b'EULA_VERSION'
FORT_MEMBER_TUTORIAL = b'FORT_MEMBER_TUTORIAL'
IGR_PROMO = b'IGR_PROMO'
PROMO = b'PROMO'
CONTACTS = b'CONTACTS'
FALLOUT_VEHICLES = b'FALLOUT_VEHICLES'
GOLD_FISH_LAST_SHOW_TIME = b'goldFishWindowShowCooldown'
BOOSTERS_FILTER = b'boostersFilter'
LAST_PROMO_PATCH_VERSION = b'lastPromoPatchVersion'
LAST_CALENDAR_SHOW_TIMESTAMP = b'lastCalendarShowTimestamp'
LAST_STORAGE_VISITED_TIMESTAMP = b'lastStorageVisitedTimestamp'
LAST_RESTORE_NOTIFICATION = b'lastRestoreNotification'
PREVIEW_INFO_PANEL_IDX = b'previewInfoPanelIdx'
NEW_SETTINGS_COUNTER = b'newSettingsCounter'
NEW_HOF_COUNTER = b'newHofCounter'
NEW_LOBBY_TAB_COUNTER = b'newLobbyTabCounter'
REFERRAL_COUNTER = b'referralButtonCounter'
CLAN_NOTIFICATION_COUNTERS = b'ClanButtonNewsCounters'
PROGRESSIVE_REWARD_VISITED = b'progressiveRewardVisited'
RANKED_AWARDS_COUNTER = b'rankedAwardsCounter'
RANKED_INFO_COUNTER = b'rankedInfoCounter'
RANKED_YEAR_RATING_COUNTER = b'rankedYearRatingCounter'
RANKED_SHOP_COUNTER = b'rankedShopCounter'
BOOSTERS_FOR_CREDITS_SLOT_COUNTER = b'boostersForCreditsSlotCounter'
SENIORITY_AWARDS_COUNTER = b'seniorityAwardsCounter'
SENIORITY_AWARDS_COINS_REMINDER_SHOWN_TIMESTAMP = b'saReminderShown'
DEMOUNT_KIT_SEEN = b'demountKitSeen'
RECERTIFICATION_FORM_SEEN = b'recertificationFormSeen'
VIEWED_OFFERS = b'viewedOffers'
OFFERS_DISABLED_MSG_SEEN = b'offersDisabledMsgSeen'
PROFILE_TECHNIQUE = b'profileTechnique'
PROFILE_TECHNIQUE_MEMBER = b'profileTechniqueMember'
SHOW_CRYSTAL_HEADER_BAND = b'showCrystalHeaderBand'
ELEN_NOTIFICATIONS = b'elenNotifications'
RECRUIT_NOTIFICATIONS = b'recruitNotifications'
SPEAKERS_DEVICE = b'speakersDevice'
SESSION_STATS_PREV_BATTLE_COUNT = b'sessionStatsPrevBattleCnt'
UNIT_FILTER = b'UNIT_FILTER'
BLUEPRINTS_CONVERT_SALE_STARTED_SEEN = b'bcsStartedSeen'
IS_SHOP_VISITED = b'isShopVisited'
LAST_SHOP_ACTION_COUNTER_MODIFICATION = b'lastShopActionCounterModification'
OVERRIDEN_HEADER_COUNTER_ACTION_ALIASES = b'overridenHeaderCounterActionAliases'
STORE_TAB = b'store_tab'
STATS_REGULAR_SORTING = b'statsSorting'
STATS_SORTIE_SORTING = b'statsSortingSortie'
STATS_COMP7_SORTING = b'statsSortingComp7'
MISSIONS_PAGE = b'missions_page'
DEFAULT_VEHICLE_TYPES_FILTER = [
 False] * len(VEHICLE_CLASSES)
DEFAULT_LEVELS_FILTERS = [False] * MAX_VEHICLE_LEVEL
SHOW_OPT_DEVICE_HINT = b'showOptDeviceHint'
SHOW_OPT_DEVICE_HINT_TROPHY = b'showOptDeviceHintTrophy'
SHOW_OPT_MODERNIZED_DEVICE_HINT = b'showOptModernizedDeviceHint'
SHOW_ECONOMIC_DIRECTIVES_HINT = b'showOEconomicDirectivesHint'
LAST_BADGES_VISIT = b'lastBadgesVisit'
LAST_SELECTED_SUFFIX_BADGE_ID = b'lastSelectedSuffixBadgeID'
ENABLE_RANKED_ANIMATIONS = b'enableRankedAnimations'
COLOR_SETTINGS_TAB_IDX = b'colorSettingsTabIdx'
COLOR_SETTINGS_SHOWS_COUNT = b'colorSettingsShowsCount'
APPLIED_COLOR_SETTINGS = b'appliedColorSettings'
SELECTED_QUEST_IN_REPLAY = b'SELECTED_QUEST_IN_REPLAY'
LAST_SELECTED_PM_BRANCH = b'lastSelectedPMBranch'
WHEELED_DEATH_DELAY_COUNT = b'wheeledDeathCounter'
LAST_BATTLE_PASS_POINTS_SEEN = b'lastBattlePassPointsSeen'
BR_PROGRESSION_POINTS_SEEN = b'brProgressionPointsSeen'
IS_BATTLE_PASS_MARATHON_STARTED = b'isBattlePassMarathonStarted'
IS_BATTLE_PASS_COLLECTION_SEEN = b'isCollectionSeen'
WIDGET_HINT_TRIGGER = b'widgetHintTrigger'
CRYSTALS_INFO_SHOWN = b'crystalsInfoShown'
IS_CUSTOMIZATION_INTRO_VIEWED = b'isCustomizationIntroViewed'
CUSTOMIZATION_STYLE_ITEMS_VISITED = b'CustomizationStyleItemsVisited'
OPT_DEVICE_TAB_VISITED = b'optDeviceTabVisited'
ANONYMIZER = GAME.ANONYMIZER
CUSTOMIZATION_SECTION = b'customization'
CAROUSEL_ARROWS_HINT_SHOWN_FIELD = b'isCarouselsArrowsHintShown'
PROJECTION_DECAL_HINT_SHOWN_FIELD = b'isProjectionDecalHintShown'
APPLY_TO_ALL_SEASONS_ENABLED = b'applyToAllSeasonsEnabled'
SESSION_STATS_SECTION = b'sessionStats'
BATTLE_EFFICIENCY_SECTION_EXPANDED_FIELD = b'battleEfficiencySectionExpanded'
SIEGE_HINT_SECTION = b'siegeModeHint'
WHEELED_MODE_HINT_SECTION = b'wheeledModeScreenHint'
TRAJECTORY_VIEW_HINT_SECTION = b'trajectoryViewHint'
ASSAULT_CAMERA_HINT_SECTION = b'assaultCameraHint'
TURBO_SHAFT_ENGINE_MODE_HINT_SECTION = b'turboShaftEngineModeHint'
ROCKET_ACCELERATION_MODE_HINT_SECTION = b'rocketAccelerationModeHint'
DYN_SQUAD_HINT_SECTION = b'dynSquadHint'
RADAR_HINT_SECTION = b'radarHint'
PRE_BATTLE_HINT_SECTION = b'preBattleHintSection'
PRE_BATTLE_ROLE_HINT_SECTION = b'preBattleRoleHintSection'
FUN_RANDOM_HINT_SECTION = b'funRandomHintSection'
MAPBOX_HINT_SECTION = b'mapboxHintSection'
QUEST_PROGRESS_HINT_SECTION = b'questProgressHint'
HELP_SCREEN_HINT_SECTION = b'helpScreenHint'
IBC_HINT_SECTION = b'battleCommunicationHint'
RESERVES_HINT_SECTION = b'reservesHintSection'
COMMANDER_CAM_HINT_SECTION = b'commanderCamHintSection'
MINIMAP_IBC_HINT_SECTION = b'minimapHintSection'
DEV_MAPS_HINT_SECTION = b'devMapsHintSection'
WATCHED_PRE_BATTLE_TIPS_SECTION = b'watchedPreBattleTipsSection'
LAST_DISPLAY_DAY = b'lastDisplayDay'
HINTS_LEFT = b'hintsLeft'
NUM_BATTLES = b'numBattles'
SELECTED_INTRO_VEHICLES_FIELD = b'selectedIntroVehicles'
NATION_CHANGE_VIEWED = b'nation_change_viewed'
CREW_SKINS_VIEWED = b'crew_skins_viewed'
CREW_BOOKS_VIEWED = b'crew_books_viewed'
CREW_SKINS_HISTORICAL_VISIBLE = b'crew_skins_historical_visible'
VEHICLES_WITH_BLUEPRINT_CONFIRM = b'showedBlueprintConfirm'
IS_FIRST_ENTRY_BY_DIVISION_ID = b'isFirstEntryByDivisionId'
RANKED_STYLED_VEHICLES_POOL = b'rankedStyledVehiclesPool'
STYLE_PREVIEW_VEHICLES_POOL = b'stylePreviewVehiclesPool'
RANKED_WEB_INFO = b'rankedWebLeague'
RANKED_WEB_INFO_UPDATE = b'rankedWebLeagueUpdate'
RANKED_AWARDS_BUBBLE_YEAR_REACHED = b'rankedAwardsBubbleYearReached'
RANKED_CURRENT_AWARDS_BUBBLE_YEAR_REACHED = b'rankedCurrentAwardsBubbleYearReached'
RANKED_ENTITLEMENT_EVENTS_AMOUNT = b'rankedEntitlementEventsAmount'
RANKED_YEAR_POSITION = b'rankedYearPosition'
MARATHON_REWARD_WAS_SHOWN_PREFIX = b'marathonRewardScreenWasShown'
MARATHON_VIDEO_WAS_SHOWN_PREFIX = b'marathonRewardVideoWasShown'
SUBTITLES = b'subtitles'
MODULES_ANIMATION_SHOWN = b'collectibleVehiclesAnimWasShown'
NEW_SHOP_TABS = b'newShopTabs'
IS_COLLECTIBLE_VEHICLES_VISITED = b'isCollectibleVehiclesVisited'
LAST_SHOP_TAB_COUNTER = b'lastShopTabCounter'
QUESTS = b'quests'
DAILY_QUESTS = b'dailyQuests'
DAILY_QUESTS_INTRO_SEEN = b'dailyQuestsIntroSeen'
QUEST_DELTAS = b'questDeltas'
QUEST_DELTAS_COMPLETION = b'questCompletion'
QUEST_DELTAS_PROGRESS = b'questProgress'
QUEST_DELTAS_TOKENS_PROGRESS = b'tokensProgress'
TOP_OF_TREE_CONFIG = b'topOfTree'
DOG_TAGS = b'dogTags'
WOT_PLUS = b'wotPlus'
TELECOM_RENTALS = b'telecomRentals'
LAST_ARTY_CTRL_MODE = b'lastArtyCtrlMode'
ACTIVE_TEST_PARTICIPATION_CONFIRMED = b'activeTestParticipateConfirmed'
MAPBOX_PROGRESSION = b'mapbox_progression'
UNLOCK_VEHICLES_IN_BATTLE_HINTS = b'unlockVehiclesInBattleHints'
BECOME_ELITE_VEHICLES_WATCHED = b'becomeEliteWatched'
VPP_ENTRY_POINT_LAST_SEEN_STEP = b'vehiclePostProgressionLastSeenStep'
CLAN_PREBATTLE_SORTING_KEY = b'ClanPrebattleSortingKey'
SHOW_ABILITY_ADVANCE_ANIM = b'showAbilityAdvanceAnim'
SHOW_DEMO_ACC_REGISTRATION = b'showDemoAccRegistration'
RESOURCE_WELL_START_SHOWN = b'resourceWellStartShown'
RESOURCE_WELL_END_SHOWN = b'resourceWellEndShown'
RESOURCE_WELL_NOTIFICATIONS = b'resourceWellNotifications'
MAPBOX_SURVEYS = b'mapbox_surveys'
CLAN_NEWS_SEEN = b'clanNewsSeen'
INTEGRATED_AUCTION_NOTIFICATIONS = b'integratedAuctionNotifications'
BLACK_MARKET_AUCTION_NOTIFICATIONS = b'blackMarketAuctionNotifications'
TRADING_CARAVAN_NOTIFICATIONS = b'tradingCaravanNotifications'
CUSTOM_NOTIFICATIONS = b'customNotifications'
SHOWN_PERSONAL_RESERVES_INTRO = b'shownPersonalReserves'
SHOWN_WOT_PLUS_INTRO = b'shownWotPlusIntro'
SHOWN_WOT_PLUS_COUNTER = b'shownWotPlusCounter'
SUBSCRIPTION_DAILY_QUESTS_INTRO_SHOWN = b'subscriptionDailyQuestsIntroShown'
SUBSCRIPTION_DAILY_QUESTS_SHINE_SHOWN = b'subscriptionDailyQuestsShineShown'
SUBSCRIPTION_LAST_EXPIRATION_NOTIFICATION = b'subscriptionLastExpirationNotification'
HAS_LEFT_VERSUS_AI = b'hasLeftVersusAI'
MINIMAP_SIZE = b'minimapSize'
COMP7_UI_SECTION = b'comp7'
COMP7_WEEKLY_QUESTS_PAGE_TOKENS_COUNT = b'comp7WeeklyQuestsPageTokensCount'
COMP7_FLAGS_VERSION = b'comp7FlagsVersion'
FUN_RANDOM_NOTIFICATIONS = b'funRandomNotifications'
FUN_RANDOM_NOTIFICATIONS_FROZEN = b'funRandomNotificationsFrozen'
FUN_RANDOM_NOTIFICATIONS_PROGRESSIONS = b'funRandomNotificationsProgressions'
FUN_RANDOM_NOTIFICATIONS_SUB_MODES = b'funRandomNotificationsSubModes'
GUI_LOOT_BOXES = b'guiLootBoxes'
LOOT_BOXES_INTRO_SHOWN = b'lootBoxesIntroShown'
LOOT_BOXES_OPEN_ANIMATION_ENABLED = b'lootBoxesOpenAnimationEnabled'
LOOT_BOXES_VIEWED_COUNT = b'lootBoxesViewedCount'
LOOT_BOXES_KEY_VIEWED_COUNT = b'lootBoxesKeyViewedCount'
LOOT_BOXES_VIEWED_HAS_INFINITE = b'lootBoxesViewedHasInfinite'
LOOT_BOXES_COUNT = b'lootBoxesCount'
LOOT_BOXES_LAST_ADDED_ID = b'lootBoxesLastAdded'
LOOT_BOXES_SHORT_STAT_STATE = b'lootBoxesShortStatState'
LOOT_BOXES_STATS_HINT_STATE = b'lootBoxesStatsHintState'
LOOT_BOXES_STATS_NO_BOX_HINT_STATE = b'lootBoxesStatsNoBoxHintState'
KEY_LOOTBOX_TRIGGER_HINT_SHOWN = b'keyLootboxTriggerHintShown'
COLLECTIONS_SECTION = b'collections'
COLLECTIONS_INTRO_SHOWN = b'collectionsIntroShown'
COLLECTION_SHOWN_NEW_REWARDS = b'collectionsNewRewards'
COLLECTION_SHOWN_NEW_ITEMS = b'collectionNewItems'
COLLECTION_SHOWN_NEW_ITEMS_COUNT = b'collectionNewItemsCount'
COLLECTION_TUTORIAL_COMPLETED = b'collectionTutorialCompleted'
COLLECTION_WAS_ENABLED = b'collectionsWasEnabled'
COLLECTIONS_TAB_SHOWN_IDS = b'collectionsTabShownIds'
COLLECTIONS_TAB_SHOWN_NEW_ITEMS = b'collectionsTabShownNewItems'
SHOWN_COMPLETED_COLLECTIONS = b'shownCompletedCollections'
LAST_SHOWN_NEW_COLLECTION = b'lastShownNewColLection'
LAST_SHOWN_COLLECTION_BALANCE = b'lastShownCollectionBalance'
COLLECTIONS_NOTIFICATIONS = b'collectionsNotifications'
REFERRAL_PROGRAM_PGB_FULL = b'referralProgramPgbFull'
ACHIEVEMENTS_INFO = b'achievements20_info'
ACHIEVEMENTS_INITIAL_BATTLE_COUNT = b'achievements20InitialBattleCount'
ACHIEVEMENTS_MAX_WTR_POINTS = b'achievements20MaxWtrPoints'
ACHIEVEMENTS_WTR_RANKS = b'achievementsWtrRanks'
ACHIEVEMENTS_WTR_PREV_POINTS_NOTIFICATION = b'achievementWtrPointsNotification'
ACHIEVEMENTS_WTR_INFO = b'achievementWtr'
ACHIEVEMENTS_WTR_PREV_POINTS = b'achievementWtrPoints'
ACHIEVEMENTS_WTR_PREV_RANK = b'achievementWtrPrevRank'
ACHIEVEMENTS_WTR_PREV_SUB_RANK = b'achievementWtrPrevSubRank'
PREV_ACHIEVEMENTS_NAME_LIST = b'prevAchievementNameList'
ACHIEVEMENTS_VISITED = b'achievementsVisited'
ACHIEVEMENTS_FIRST_ENTRY_STATUS = b'achievementsFirstEntryStatus'
ACHIEVEMENTS_RATING_CALCULATED_STATUS = b'achievementsRatingCalculatedStatus'
ACHIEVEMENTS_EDITING_ENABLED_STATUS = b'achievementsEditingEnabledStatus'
ACHIEVEMENTS_MEDAL_ADDED_STATUS = b'achievementsMedalAddedStatus'
ACHIEVEMENTS_RATING_CHANGED_STATUS = b'achievementsRatingChangedStatus'
ACHIEVEMENTS_MEDAL_COUNT_INFO = b'achievementsMedalCountInfo'
NEW_YEAR = b'newYear'
NY_DAILY_QUESTS_VISITED = b'NYDailyQuestsVisited'
NY_BONUS_DAILY_QUEST_VISITED = b'NYBonusDailyQuestVisited'
NY_OLD_COLLECTIONS_BY_YEAR_VISITED = b'NYOldCollectionsByYearVisited'
NY_OLD_REWARDS_BY_YEAR_VISITED = b'NYOldRewardsByYearVisited'
NY_LAST_SEEN_LEVEL_INFO = b'NYLastSeenLevelInfo'
NY_LAST_SEEN_TOTAL_BONUS = b'NYLastSeenTotalBonus'
NY_INTRO_SEEN = b'NYIntroSeen'
NY_DAILY_QUESTS_HOVERED = b'NYDailyQuestsHovered'
NY_WEEKLY_QUESTS_HOVERED = b'NYWeeklyQuestsHovered'
NY_DAILY_MEDIA = b'NYDailyMedia'
NY_GENERATION_TIME = b'NYGenerationTime'
NY_DAILY_VIDEO_DAY_VISITED = b'NYFirstVideoDayVisited'
NY_DAILY_VIDEO_VISITED_AT = b'NYFirstVideoVisitedAt'
NY_FIRST_VIDEO_SHUFFLE = b'NYFirstVideoShuffle'
NY_ACTIVE_WIDGET_TRANSITION_SHOWN = b'NyActiveWidgetTransitionShown'
NY_PET_SLOT_VISITED = b'NyPetSlotVisited'
NY_GREETINGS_SEEN = b'NYGreetingsSeen'
PREMIUM_QUESTS_NOTIFICATION = b'PremiumPurchased'
DEFERRED_LOG_PLAYER_SETTINGS_ACTIONS = b'DeferredLogPlayerSettingsActions'
DYNAMIC_SETTINGS_REPOSITORY = b'dynamicSettingsRepository'
SHOWN_SUMMER_SALE_INTRO = b'shownSummerSaleIntro'

class BattleMatters(object):
    BATTLE_MATTERS_SETTINGS = b'battleMattersSettings'
    BATTLES_COUNT_WITHOUT_PROGRESS = b'battlesCountWithoutProgress'
    QUEST_IDX_FOR_LAST_UPDATED_PROGRESS = b'progressForQuest'
    LAST_QUEST_PROGRESS = b'lastQuestProgress'
    REMINDER_LAST_DISPLAY_TIME = b'reminderLastDisplayTime'


class Winback(object):
    WINBACK_SETTINGS = b'winbackSettings'
    NEED_SHOW_INTRO = b'needShowIntro'
    INTRO_LAST_TIME_SHOWN = b'introLastTimeShown'
    HAS_LEFT_VERSUS_AI_FROM_WINBACK = b'hasLeftVersusAIFromWinback'
    WINBACK_PROGRESSION_POINTS_SEEN = b'winbackProgressionsPointsSeen'
    WINBACK_BATTLES_COUNT = b'winbackBattlesCount'


class ArmoryYard(object):
    ARMORY_YARD_SETTINGS = b'armoryYardSettings'
    ARMORY_YARD_LAST_INTRO_VIEWED = b'armoryYardLastIntroViewed'
    ARMORY_YARD_REROLL_INTRO_VIEWED = b'armoryYardRerollIntroViewed'
    ARMORY_YARD_REROLL_BUTTON_HINT_VIEWED = b'armoryYardRerollButtonHintViewed'
    ARMORY_YARD_REROLL_LAST_CURRENCY = b'armoryYardRerollLastCurrency'
    ARMORY_YARD_PREV_COMPLETED_QUESTS = b'armoryYardPrevCompletedQuests'
    ARMORY_SHOP_INTRO_VIEWED = b'armoryShopIntroViewed'
    EVENT_ANNOUNCEMENT = b'announcement'
    ANNOUNCEMENT_CHAPTER_PREFIX = b'announcement_chapter'
    CHAPTER_PREFIX = b'chapter'
    FINISH_CHAPTER_PREFIX = b'finish_chapter'
    START_CHAPTER_PREFIX = b'start_chapter'
    STYLE_QUEST_ENDS = b'style_quest_ends'
    ARMORY_YARD_CURRENT_SEASON = b'armoryYardCurrSeason'
    AY_SECTION_LAST_LISTENED_MESSAGE = b'lastListenedMessage'


class EarlyAccess(object):
    EARLY_ACCESS_SETTINGS = b'earlyAccessSettings'
    EARLY_ACCESS_CURRENT_SEASON = b'earlyAccessCurrentSeason'
    INTRO_SEEN = b'earlyAccessIntroSeen'
    TREE_SEEN = b'earlyAccessTreeSeen'
    EVENT_FINISHED = b'earlyAccessEventFinished'
    EVENT_ANNOUNCEMENT = b'eventAnnouncement'
    EVENT_PAUSED = b'eventPaused'
    STARTED_CHAPTER_PREFIX = b'startedChapter'
    FINISHED_PROGRESSION = b'finishedProgression'
    FINISHED_POSTRPOGRESSION = b'finishedPostprogression'
    COMPLETED_PROGRESSION_PREFIX = b'completedProgression'
    COMPLETED_POSTPROGRESSION = b'completedPostprogression'
    ALL_TOKENS_RECEIVED = b'allTokensReceived'
    PREV_COMPLETED_QUESTS = b'prevCompletedQuests'


class PersonalMissions(object):
    PERSONAL_MISSIONS_SETTINGS = b'personalMissionsSettings'
    INTRO_SEEN = b'personalMissionsIntroSeen'
    PREV_COMPLETED_QUESTS = b'prevCompletedQuests'
    CURR_QUESTS_STATEMENT = b'currentQuestStatement'
    OPERATIONS_VIDEO_REWARDS_STATUS = b'operationsVideoRewardsStatus'


class FunRandomMaps(object):
    FUN_RANDOM_MAPS_SETTINGS = b'funRandomMapsSettings'
    FUN_RANDOM_LAST_SELECTED_MAP = b'funRandomLastSelectedMap'
    FUN_RANDOM_WIDGET_VISITED_SUBMODES = b'funRandomWidgetVisitedSubModes'
    FUN_RANDOM_MODE_SELECTOR_CARD_SEEN_FEP_TYPES = b'funRandomModeSelectorCardSeenFepTypes'


class Paragons(object):
    PARAGONS_SETTINGS = b'paragonsSettings'
    INTRO_SEEN = b'introSeen'
    NEED_TO_SHOW_ANIMATION_FOR_PARAGONS_UNLOCK_IDS = b'needToShowAnimationForParagonsUnlockIDs'
    NEED_TO_SHOW_ANIMATION_FOR_PARAGONS_RESET_BRANCH = b'needToShowAnimationForParagonsResetBranch'
    PROJECT_IS_ENABLED_NOTIFICATION_WAS_SHOWN = b'ParagonsProjectEnabledNotificationWasShown'
    PROJECT_IS_DISABLED_NOTIFICATION_WAS_SHOWN = b'ParagonsProjectDisabledNotificationWasShown'
    PROJECT_IS_CONTINUING_NOTIFICATION_WAS_SHOWN = b'ParagonsProjectPaused'
    BRANCH_RESET_AVAILABILITY_NOTIFICATION_WAS_SHOWN = b'ParagonsResettableBranchAvailableNotificationWasShown'
    CHAPTER_COUNTER = b'ParagonsChapterCounter'


class BlackMarket(object):
    BLACK_MARKET_SETTINGS = b'BlackMarketSettings'
    BLACK_MARKET_ENTRY_CLICKED = b'BlackMarketEntryClicked'
    BLACK_MARKET_LAST_PHASE_SEEN = b'BlackMarketLastPhaseSeen'


class CustomizationFilter(object):
    CUSTOMIZATION_FILTER = b'customizationFilter'
    CAMOUFLAGE_GROUP = b'camouflageGroup'
    PAINTS_GROUP = b'paintsGroup'
    PROJECTION_DECALS_GROUP = b'projectionDecalsGroup'
    EMBLEMS_GROUP = b'emblemsGroup'
    INSCRIPTIONS_GROUP = b'inscriptionsGroup'
    STYLES_2D_GROUP = b'styles2dGroup'
    STYLES_3D_GROUP = b'styles3dGroup'
    DISPLAY_GROUP = b'displayGroup'
    FORMFACTOR_SQUARE = b'formfactor_square'
    FORMFACTOR_RECT1X2 = b'formfactor_rect1x2'
    FORMFACTOR_RECT1X3 = b'formfactor_rect1x3'
    FORMFACTOR_RECT1X4 = b'formfactor_rect1x4'
    FORMFACTOR_RECT1X6 = b'formfactor_rect1x6'
    HISTORIC = b'historic'
    NON_HISTORIC = b'nonHistoric'
    FANTASTICAL = b'fantastical'
    INVENTORY = b'inventory'
    SALE = b'sale'
    APPLIED = b'applied'
    FAVORITE = b'favorite'
    ON_ANOTHER_VEH = b'onAnotherVeh'
    ONLY_PROGRESSION_DECALS = b'onlyProgressionDecals'
    ONLY_EDITABLE_STYLES = b'onlyEditableStyles'
    ONLY_NON_EDITABLE_STYLES = b'onlyNonEditableStyles'
    ONLY_PROGRESSION_STYLES = b'onlyProgressionStyles'


class Epic(object):
    EPIC_SETTINGS = b'epicSettings'
    SUPPLY_PILLBOX_HINT_VIEWED = b'supplyPillboxHintViewed'
    SUPPLY_MORTAR_HINT_VIEWED = b'supplyMortarHintViewed'
    SUPPLY_FLAMER_HINT_VIEWED = b'supplyFlamerHintViewed'
    SUPPLY_AIRSHIP_HINT_VIEWED = b'supplyAirshipHintViewed'


KNOWN_SELECTOR_BATTLES = b'knownSelectorBattles'
MODE_SELECTOR_BATTLE_PASS_SHOWN = b'modeSelectorBattlePassShown'
RANKED_LAST_CYCLE_ID = b'rankedLastCycleID'
EPIC_LAST_CYCLE_ID = b'epicLastCycleID'
FUN_RANDOM_LAST_PRESET = b'funRandomLastPreset'
DEFAULT_VALUES = {KEY_FILTERS: {STORE_TAB: 0, 
                 b'shop_current': (
                                 -1, STORE_CONSTANTS.VEHICLE, False), 
                 b'scroll_to_item': None, 
                 b'shop_restoreVehicle': {b'obtainingType': (STORE_CONSTANTS.RESTORE_VEHICLE), 
                                          b'selectedTypes': DEFAULT_VEHICLE_TYPES_FILTER, 
                                          b'selectedLevels': DEFAULT_LEVELS_FILTERS}, 
                 b'shop_tradeInVehicle': {b'obtainingType': (STORE_CONSTANTS.TRADE_IN_VEHICLE), 
                                          b'selectedTypes': DEFAULT_VEHICLE_TYPES_FILTER, 
                                          b'selectedLevels': DEFAULT_LEVELS_FILTERS}, 
                 b'shop_module': {b'fitsType': (STORE_CONSTANTS.MY_VEHICLES_ARTEFACT_FIT), 
                                  b'vehicleCD': (-1), 
                                  b'extra': [
                                           STORE_CONSTANTS.LOCKED_EXTRA_NAME, STORE_CONSTANTS.IN_HANGAR_EXTRA_NAME], 
                                  b'itemTypes': [
                                               STORE_CONSTANTS.GUN_MODULE_NAME,
                                               STORE_CONSTANTS.TURRET_MODULE_NAME,
                                               STORE_CONSTANTS.ENGINE_MODULE_NAME,
                                               STORE_CONSTANTS.CHASSIS_MODULE_NAME,
                                               STORE_CONSTANTS.RADIO_MODULE_NAME]}, 
                 b'shop_shell': {b'fitsType': (STORE_CONSTANTS.CURRENT_VEHICLE_SHELL_FIT), 
                                 b'vehicleCD': (-1), 
                                 b'itemTypes': [
                                              STORE_CONSTANTS.ARMOR_PIERCING_SHELL,
                                              STORE_CONSTANTS.ARMOR_PIERCING_CR_SHELL,
                                              STORE_CONSTANTS.HOLLOW_CHARGE_SHELL,
                                              STORE_CONSTANTS.HIGH_EXPLOSIVE_SHELL]}, 
                 b'shop_battleBooster': {b'targetType': (STORE_CONSTANTS.ALL_KIND_FIT)}, 
                 b'inventory_current': (
                                      -1, STORE_CONSTANTS.VEHICLE, False), 
                 b'inventory_vehicle': {b'selectedTypes': DEFAULT_VEHICLE_TYPES_FILTER, 
                                        b'selectedLevels': DEFAULT_LEVELS_FILTERS, 
                                        b'extra': [
                                                 STORE_CONSTANTS.BROCKEN_EXTRA_NAME, STORE_CONSTANTS.LOCKED_EXTRA_NAME]}, 
                 b'inventory_module': {b'fitsType': (STORE_CONSTANTS.MY_VEHICLES_ARTEFACT_FIT), 
                                       b'vehicleCD': (-1), 
                                       b'extra': [], b'itemTypes': [
                                                    STORE_CONSTANTS.GUN_MODULE_NAME,
                                                    STORE_CONSTANTS.TURRET_MODULE_NAME,
                                                    STORE_CONSTANTS.ENGINE_MODULE_NAME,
                                                    STORE_CONSTANTS.CHASSIS_MODULE_NAME,
                                                    STORE_CONSTANTS.RADIO_MODULE_NAME]}, 
                 b'inventory_shell': {b'fitsType': (STORE_CONSTANTS.CURRENT_VEHICLE_SHELL_FIT), 
                                      b'vehicleCD': (-1), 
                                      b'itemTypes': [
                                                   STORE_CONSTANTS.ARMOR_PIERCING_SHELL,
                                                   STORE_CONSTANTS.ARMOR_PIERCING_CR_SHELL,
                                                   STORE_CONSTANTS.HOLLOW_CHARGE_SHELL,
                                                   STORE_CONSTANTS.HIGH_EXPLOSIVE_SHELL]}, 
                 b'inventory_optionalDevice': {b'fitsType': (STORE_CONSTANTS.CURRENT_VEHICLE_ARTEFACT_FIT), 
                                               b'vehicleCD': (-1), 
                                               b'extra': [
                                                        STORE_CONSTANTS.ON_VEHICLE_EXTRA_NAME]}, 
                 b'inventory_equipment': {b'fitsType': (STORE_CONSTANTS.CURRENT_VEHICLE_ARTEFACT_FIT), 
                                          b'vehicleCD': (-1), 
                                          b'extra': [
                                                   STORE_CONSTANTS.ON_VEHICLE_EXTRA_NAME]}, 
                 b'inventory_battleBooster': {b'targetType': (STORE_CONSTANTS.ALL_KIND_FIT)}, 
                 b'inventory_crewBooks': {b'targetType': (STORE_CONSTANTS.ALL_KIND_FIT)}, 
                 MISSIONS_PAGE: {b'hideDone': False, 
                                 b'hideUnavailable': False}, 
                 CAROUSEL_FILTER_1: {b'ussr': False, 
                                     b'germany': False, 
                                     b'usa': False, 
                                     b'china': False, 
                                     b'france': False, 
                                     b'uk': False, 
                                     b'japan': False, 
                                     b'czech': False, 
                                     b'sweden': False, 
                                     b'poland': False, 
                                     b'italy': False, 
                                     b'intunion': False, 
                                     b'lightTank': False, 
                                     b'mediumTank': False, 
                                     b'heavyTank': False, 
                                     b'SPG': False, 
                                     b'AT-SPG': False, 
                                     b'level_1': False, 
                                     b'level_2': False, 
                                     b'level_3': False, 
                                     b'level_4': False, 
                                     b'level_5': False, 
                                     b'level_6': False, 
                                     b'level_7': False, 
                                     b'level_8': False, 
                                     b'level_9': False, 
                                     b'level_10': False, 
                                     b'level_11': False}, 
                 CAROUSEL_FILTER_2: {b'premium': False, 
                                     b'elite': False, 
                                     b'igr': False, 
                                     b'rented': True, 
                                     b'event': True, 
                                     b'favorite': False, 
                                     b'bonus': False, 
                                     b'crystals': False, 
                                     b'early_access': False, 
                                     b'paragons': False, 
                                     b'debut_boxes': False, 
                                     b'role_HT_assault': False, 
                                     b'role_HT_break': False, 
                                     b'role_HT_support': False, 
                                     b'role_HT_universal': False, 
                                     b'role_MT_universal': False, 
                                     b'role_MT_sniper': False, 
                                     b'role_MT_assault': False, 
                                     b'role_MT_support': False, 
                                     b'role_ATSPG_assault': False, 
                                     b'role_ATSPG_universal': False, 
                                     b'role_ATSPG_sniper': False, 
                                     b'role_ATSPG_support': False, 
                                     b'role_LT_universal': False, 
                                     b'role_LT_wheeled': False, 
                                     b'role_SPG': False, 
                                     b'role_SPG_flame': False, 
                                     b'role_SPG_assault': False}, 
                 CAROUSEL_FILTER_CLIENT_1: {b'searchNameVehicle': b'', 
                                            b'clanRented': False}, 
                 BATTLEPASS_CAROUSEL_FILTER_CLIENT_1: {b'battlePassSeason': 0}, RANKED_CAROUSEL_FILTER_1: {b'ussr': False, 
                                            b'germany': False, 
                                            b'usa': False, 
                                            b'china': False, 
                                            b'france': False, 
                                            b'uk': False, 
                                            b'japan': False, 
                                            b'czech': False, 
                                            b'sweden': False, 
                                            b'poland': False, 
                                            b'italy': False, 
                                            b'intunion': False, 
                                            b'lightTank': False, 
                                            b'mediumTank': False, 
                                            b'heavyTank': False, 
                                            b'SPG': False, 
                                            b'AT-SPG': False, 
                                            b'level_1': False, 
                                            b'level_2': False, 
                                            b'level_3': False, 
                                            b'level_4': False, 
                                            b'level_5': False, 
                                            b'level_6': False, 
                                            b'level_7': False, 
                                            b'level_8': False, 
                                            b'level_9': False, 
                                            b'level_10': False, 
                                            b'level_11': False}, 
                 RANKED_CAROUSEL_FILTER_2: {b'premium': False, 
                                            b'elite': False, 
                                            b'igr': False, 
                                            b'rented': True, 
                                            b'event': True, 
                                            b'gameMode': False, 
                                            b'favorite': False, 
                                            b'bonus': False, 
                                            b'crystals': False, 
                                            b'ranked': True, 
                                            b'paragons': False, 
                                            b'debut_boxes': False, 
                                            b'role_HT_assault': False, 
                                            b'role_HT_break': False, 
                                            b'role_HT_universal': False, 
                                            b'role_HT_support': False, 
                                            b'role_MT_assault': False, 
                                            b'role_MT_universal': False, 
                                            b'role_MT_sniper': False, 
                                            b'role_MT_support': False, 
                                            b'role_ATSPG_assault': False, 
                                            b'role_ATSPG_universal': False, 
                                            b'role_ATSPG_sniper': False, 
                                            b'role_ATSPG_support': False, 
                                            b'role_LT_universal': False, 
                                            b'role_LT_wheeled': False, 
                                            b'role_SPG': False, 
                                            b'role_SPG_flame': False, 
                                            b'role_SPG_assault': False}, 
                 RANKED_CAROUSEL_FILTER_CLIENT_1: {b'searchNameVehicle': b'', 
                                                   b'clanRented': False}, 
                 ROYALE_CAROUSEL_FILTER_1: {b'ussr': False, 
                                            b'germany': False, 
                                            b'usa': False, 
                                            b'china': False, 
                                            b'france': False, 
                                            b'uk': False, 
                                            b'japan': False, 
                                            b'czech': False, 
                                            b'sweden': False, 
                                            b'poland': False, 
                                            b'italy': False, 
                                            b'intunion': False, 
                                            b'lightTank': True, 
                                            b'mediumTank': True, 
                                            b'heavyTank': True, 
                                            b'SPG': False, 
                                            b'AT-SPG': False, 
                                            b'level_1': False, 
                                            b'level_2': False, 
                                            b'level_3': False, 
                                            b'level_4': False, 
                                            b'level_5': False, 
                                            b'level_6': False, 
                                            b'level_7': False, 
                                            b'level_8': False, 
                                            b'level_9': False, 
                                            b'level_10': False, 
                                            b'level_11': False}, 
                 ROYALE_CAROUSEL_FILTER_2: {b'premium': False, 
                                            b'elite': False, 
                                            b'igr': False, 
                                            b'rented': True, 
                                            b'event': True, 
                                            b'gameMode': False, 
                                            b'favorite': False, 
                                            b'bonus': False, 
                                            b'crystals': False, 
                                            b'battleRoyale': True}, 
                 ROYALE_CAROUSEL_FILTER_CLIENT_1: {b'searchNameVehicle': b'', 
                                                   b'clanRented': False}, 
                 EPICBATTLE_CAROUSEL_FILTER_1: {b'ussr': False, 
                                                b'germany': False, 
                                                b'usa': False, 
                                                b'china': False, 
                                                b'france': False, 
                                                b'uk': False, 
                                                b'japan': False, 
                                                b'czech': False, 
                                                b'sweden': False, 
                                                b'poland': False, 
                                                b'italy': False, 
                                                b'intunion': False, 
                                                b'lightTank': False, 
                                                b'mediumTank': False, 
                                                b'heavyTank': False, 
                                                b'SPG': False, 
                                                b'AT-SPG': False, 
                                                b'level_1': False, 
                                                b'level_2': False, 
                                                b'level_3': False, 
                                                b'level_4': False, 
                                                b'level_5': False, 
                                                b'level_6': False, 
                                                b'level_7': False, 
                                                b'level_8': True, 
                                                b'level_9': False, 
                                                b'level_10': False, 
                                                b'level_11': False}, 
                 EPICBATTLE_CAROUSEL_FILTER_2: {b'premium': False, 
                                                b'elite': False, 
                                                b'igr': False, 
                                                b'rented': True, 
                                                b'event': True, 
                                                b'gameMode': False, 
                                                b'favorite': False, 
                                                b'bonus': False, 
                                                b'crystals': False, 
                                                b'paragons': False, 
                                                b'role_HT_assault': False, 
                                                b'role_HT_break': False, 
                                                b'role_HT_support': False, 
                                                b'role_HT_universal': False, 
                                                b'role_MT_universal': False, 
                                                b'role_MT_sniper': False, 
                                                b'role_MT_assault': False, 
                                                b'role_MT_support': False, 
                                                b'role_ATSPG_assault': False, 
                                                b'role_ATSPG_universal': False, 
                                                b'role_ATSPG_sniper': False, 
                                                b'role_ATSPG_support': False, 
                                                b'role_LT_universal': False, 
                                                b'role_LT_wheeled': False, 
                                                b'role_SPG': False, 
                                                b'role_SPG_flame': False, 
                                                b'role_SPG_assault': False}, 
                 EPICBATTLE_CAROUSEL_FILTER_CLIENT_1: {b'epicBattleSeason': 0, 
                                                       b'level_8': True, 
                                                       b'searchNameVehicle': b'', 
                                                       b'clanRented': False}, 
                 EPICBATTLE_CAROUSEL_FILTER_CLIENT_2: {b'epicBattleSeason': 0, 
                                                       b'level_8': True, 
                                                       b'searchNameVehicle': b'', 
                                                       b'clanRented': False}, 
                 BATTLEPASS_CAROUSEL_FILTER_1: {b'isCommonProgression': False}, 
                 MAPBOX_CAROUSEL_FILTER_1: {b'ussr': False, 
                                            b'germany': False, 
                                            b'usa': False, 
                                            b'china': False, 
                                            b'france': False, 
                                            b'uk': False, 
                                            b'japan': False, 
                                            b'czech': False, 
                                            b'sweden': False, 
                                            b'poland': False, 
                                            b'italy': False, 
                                            b'intunion': False, 
                                            b'lightTank': False, 
                                            b'mediumTank': False, 
                                            b'heavyTank': False, 
                                            b'SPG': False, 
                                            b'AT-SPG': False, 
                                            b'level_1': False, 
                                            b'level_2': False, 
                                            b'level_3': False, 
                                            b'level_4': False, 
                                            b'level_5': False, 
                                            b'level_6': False, 
                                            b'level_7': False, 
                                            b'level_8': True, 
                                            b'level_9': True, 
                                            b'level_10': True, 
                                            b'level_11': True}, 
                 MAPBOX_CAROUSEL_FILTER_2: {b'premium': False, 
                                            b'elite': False, 
                                            b'igr': False, 
                                            b'rented': True, 
                                            b'event': True, 
                                            b'gameMode': False, 
                                            b'favorite': False, 
                                            b'bonus': False, 
                                            b'crystals': False, 
                                            b'role_HT_assault': False, 
                                            b'role_HT_break': False, 
                                            b'role_HT_support': False, 
                                            b'role_HT_universal': False, 
                                            b'role_MT_universal': False, 
                                            b'role_MT_sniper': False, 
                                            b'role_MT_assault': False, 
                                            b'role_MT_support': False, 
                                            b'role_ATSPG_assault': False, 
                                            b'role_ATSPG_universal': False, 
                                            b'role_ATSPG_sniper': False, 
                                            b'role_ATSPG_support': False, 
                                            b'role_LT_universal': False, 
                                            b'role_LT_wheeled': False, 
                                            b'role_SPG': False, 
                                            b'role_SPG_flame': False, 
                                            b'role_SPG_assault': False}, 
                 MAPBOX_CAROUSEL_FILTER_CLIENT_1: {b'searchNameVehicle': b'', 
                                                   b'clanRented': False}, 
                 FUN_RANDOM_CAROUSEL_FILTER_1: {b'ussr': False, 
                                                b'germany': False, 
                                                b'usa': False, 
                                                b'china': False, 
                                                b'france': False, 
                                                b'uk': False, 
                                                b'japan': False, 
                                                b'czech': False, 
                                                b'sweden': False, 
                                                b'poland': False, 
                                                b'italy': False, 
                                                b'intunion': False, 
                                                b'lightTank': False, 
                                                b'mediumTank': False, 
                                                b'heavyTank': False, 
                                                b'SPG': False, 
                                                b'AT-SPG': False, 
                                                b'level_1': False, 
                                                b'level_2': False, 
                                                b'level_3': False, 
                                                b'level_4': False, 
                                                b'level_5': False, 
                                                b'level_6': False, 
                                                b'level_7': False, 
                                                b'level_8': False, 
                                                b'level_9': False, 
                                                b'level_10': False, 
                                                b'level_11': False}, 
                 FUN_RANDOM_CAROUSEL_FILTER_2: {b'premium': False, 
                                                b'elite': False, 
                                                b'igr': False, 
                                                b'rented': True, 
                                                b'event': False, 
                                                b'gameMode': False, 
                                                b'favorite': False, 
                                                b'bonus': False, 
                                                b'crystals': False, 
                                                b'funRandom': True, 
                                                b'paragons': False, 
                                                b'role_HT_assault': False, 
                                                b'role_HT_break': False, 
                                                b'role_HT_support': False, 
                                                b'role_HT_universal': False, 
                                                b'role_MT_universal': False, 
                                                b'role_MT_sniper': False, 
                                                b'role_MT_assault': False, 
                                                b'role_MT_support': False, 
                                                b'role_ATSPG_assault': False, 
                                                b'role_ATSPG_universal': False, 
                                                b'role_ATSPG_sniper': False, 
                                                b'role_ATSPG_support': False, 
                                                b'role_LT_universal': False, 
                                                b'role_LT_wheeled': False, 
                                                b'role_SPG': False, 
                                                b'role_SPG_flame': False, 
                                                b'role_SPG_assault': False}, 
                 FUN_RANDOM_CAROUSEL_FILTER_CLIENT_1: {b'searchNameVehicle': b'', 
                                                       b'clanRented': False}, 
                 COMP7_CAROUSEL_FILTER_1: {b'ussr': False, 
                                           b'germany': False, 
                                           b'usa': False, 
                                           b'china': False, 
                                           b'france': False, 
                                           b'uk': False, 
                                           b'japan': False, 
                                           b'czech': False, 
                                           b'sweden': False, 
                                           b'poland': False, 
                                           b'italy': False, 
                                           b'intunion': False, 
                                           b'lightTank': False, 
                                           b'mediumTank': False, 
                                           b'heavyTank': False, 
                                           b'SPG': False, 
                                           b'AT-SPG': False, 
                                           b'level_1': False, 
                                           b'level_2': False, 
                                           b'level_3': False, 
                                           b'level_4': False, 
                                           b'level_5': False, 
                                           b'level_6': False, 
                                           b'level_7': False, 
                                           b'level_8': False, 
                                           b'level_9': False, 
                                           b'level_10': False, 
                                           b'level_11': False}, 
                 COMP7_CAROUSEL_FILTER_2: {b'premium': False, 
                                           b'elite': False, 
                                           b'igr': False, 
                                           b'rented': True, 
                                           b'event': True, 
                                           b'gameMode': False, 
                                           b'favorite': False, 
                                           b'bonus': False, 
                                           b'crystals': False, 
                                           b'comp7': True, 
                                           b'paragons': False, 
                                           b'debut_boxes': False, 
                                           b'role_HT_assault': False, 
                                           b'role_HT_break': False, 
                                           b'role_HT_support': False, 
                                           b'role_HT_universal': False, 
                                           b'role_MT_universal': False, 
                                           b'role_MT_sniper': False, 
                                           b'role_MT_assault': False, 
                                           b'role_MT_support': False, 
                                           b'role_ATSPG_assault': False, 
                                           b'role_ATSPG_universal': False, 
                                           b'role_ATSPG_sniper': False, 
                                           b'role_ATSPG_support': False, 
                                           b'role_LT_universal': False, 
                                           b'role_LT_wheeled': False, 
                                           b'role_SPG': False, 
                                           b'role_SPG_flame': False, 
                                           b'role_SPG_assault': False}, 
                 COMP7_CAROUSEL_FILTER_CLIENT_1: {b'searchNameVehicle': b'', 
                                                  b'clanRented': False}, 
                 VERSUS_AI_CAROUSEL_FILTER_1: {b'ussr': False, 
                                               b'germany': False, 
                                               b'usa': False, 
                                               b'china': False, 
                                               b'france': False, 
                                               b'uk': False, 
                                               b'japan': False, 
                                               b'czech': False, 
                                               b'sweden': False, 
                                               b'poland': False, 
                                               b'italy': False, 
                                               b'intunion': False, 
                                               b'lightTank': False, 
                                               b'mediumTank': False, 
                                               b'heavyTank': False, 
                                               b'SPG': False, 
                                               b'AT-SPG': False, 
                                               b'level_1': False, 
                                               b'level_2': False, 
                                               b'level_3': False, 
                                               b'level_4': False, 
                                               b'level_5': False, 
                                               b'level_6': False, 
                                               b'level_7': False, 
                                               b'level_8': False, 
                                               b'level_9': False, 
                                               b'level_10': False, 
                                               b'level_11': False}, 
                 VERSUS_AI_CAROUSEL_FILTER_2: {b'premium': False, 
                                               b'elite': False, 
                                               b'igr': False, 
                                               b'rented': True, 
                                               b'event': True, 
                                               b'gameMode': False, 
                                               b'favorite': False, 
                                               b'bonus': False, 
                                               b'crystals': False, 
                                               b'paragons': False, 
                                               b'role_HT_assault': False, 
                                               b'role_HT_break': False, 
                                               b'role_HT_support': False, 
                                               b'role_HT_universal': False, 
                                               b'role_MT_universal': False, 
                                               b'role_MT_sniper': False, 
                                               b'role_MT_assault': False, 
                                               b'role_MT_support': False, 
                                               b'role_ATSPG_assault': False, 
                                               b'role_ATSPG_universal': False, 
                                               b'role_ATSPG_sniper': False, 
                                               b'role_ATSPG_support': False, 
                                               b'role_LT_universal': False, 
                                               b'role_LT_wheeled': False, 
                                               b'role_SPG': False, 
                                               b'role_SPG_flame': False, 
                                               b'role_SPG_assault': False}, 
                 VERSUS_AI_CAROUSEL_FILTER_CLIENT_1: {b'searchNameVehicle': b'', 
                                                      b'clanRented': False}, 
                 MISSION_SELECTOR_FILTER: {b'inventory': False}, 
                 PM_SELECTOR_FILTER: {b'inventory': False}, 
                 BARRACKS_FILTER: {b'nation': (-1), b'role': b'None', b'tankType': b'None', b'location': 3, b'nationID': None}, ORDERS_FILTER: {b'isSelected': False}, GUI_START_BEHAVIOR: {b'isFreeXPInfoDialogShowed': False, b'isRankedWelcomeViewShowed': False, 
                                      b'isRankedWelcomeViewStarted': False, 
                                      b'isEpicRandomCheckboxClicked': False, 
                                      b'isDisplayPlatoonMembersClicked': False, 
                                      (GuiSettingsBehavior.VEH_POST_PROGRESSION_UNLOCK_MSG_NEED_SHOW): True, 
                                      (GuiSettingsBehavior.RESOURCE_WELL_INTRO_SHOWN): False, 
                                      b'birthdayCalendarIntroShowed': False, 
                                      b'isComp7IntroShown': False, 
                                      (GuiSettingsBehavior.COMP7_VERSION_FLAG): 0, 
                                      b'isWinbackIntroShown': False}, 
                 EULA_VERSION: {b'version': 0}, FORT_MEMBER_TUTORIAL: {b'wasShown': False}, IGR_PROMO: {b'wasShown': False}, CONTACTS: {b'showOfflineUsers': True, b'showOthersCategory': True}, GOLD_FISH_LAST_SHOW_TIME: 0, 
                 BOOSTERS_FILTER: 0, 
                 b'cs_intro_view_vehicle': {b'nation': (-1), b'vehicleType': b'none', b'isMain': False, b'level': (-1), b'compatibleOnly': True}, 
                 b'cs_list_view_vehicle': {b'nation': (-1), b'vehicleType': b'none', b'isMain': False, b'level': (-1), b'compatibleOnly': True}, 
                 b'cs_unit_view_vehicle': {b'nation': (-1), b'vehicleType': b'none', b'isMain': False, b'level': (-1), b'compatibleOnly': True}, 
                 b'cs_unit_view_settings': {b'nation': (-1), b'vehicleType': b'none', b'isMain': False, b'level': (-1), b'compatibleOnly': True}, 
                 b'epic_rent_view_vehicle': {b'nation': (-1), b'vehicleType': b'none', b'isMain': False, b'level': (-1), b'compatibleOnly': True}, 
                 PROMO: {}, PROFILE_TECHNIQUE: {b'selectedColumn': 4, b'selectedColumnSorting': b'descending', b'isInHangarSelected': False}, PROFILE_TECHNIQUE_MEMBER: {b'selectedColumn': 4, b'selectedColumnSorting': b'descending'}, SPEAKERS_DEVICE: 0, 
                 UNIT_FILTER: {(GAME.UNIT_FILTER): 4095}, (CustomizationFilter.CUSTOMIZATION_FILTER): {(CustomizationFilter.CAMOUFLAGE_GROUP): (-1), 
                                                              (CustomizationFilter.PAINTS_GROUP): (-1), 
                                                              (CustomizationFilter.PROJECTION_DECALS_GROUP): (-1), 
                                                              (CustomizationFilter.EMBLEMS_GROUP): (-1), 
                                                              (CustomizationFilter.INSCRIPTIONS_GROUP): (-1), 
                                                              (CustomizationFilter.STYLES_2D_GROUP): (-1), 
                                                              (CustomizationFilter.STYLES_3D_GROUP): (-1), 
                                                              (CustomizationFilter.DISPLAY_GROUP): 0, 
                                                              (CustomizationFilter.FORMFACTOR_SQUARE): False, 
                                                              (CustomizationFilter.FORMFACTOR_RECT1X2): False, 
                                                              (CustomizationFilter.FORMFACTOR_RECT1X3): False, 
                                                              (CustomizationFilter.FORMFACTOR_RECT1X4): False, 
                                                              (CustomizationFilter.FORMFACTOR_RECT1X6): False, 
                                                              (CustomizationFilter.HISTORIC): False, 
                                                              (CustomizationFilter.NON_HISTORIC): False, 
                                                              (CustomizationFilter.FANTASTICAL): False, 
                                                              (CustomizationFilter.INVENTORY): False, 
                                                              (CustomizationFilter.APPLIED): False, 
                                                              (CustomizationFilter.SALE): False, 
                                                              (CustomizationFilter.FAVORITE): False, 
                                                              (CustomizationFilter.ON_ANOTHER_VEH): False, 
                                                              (CustomizationFilter.ONLY_PROGRESSION_DECALS): False, 
                                                              (CustomizationFilter.ONLY_EDITABLE_STYLES): False, 
                                                              (CustomizationFilter.ONLY_NON_EDITABLE_STYLES): False, 
                                                              (CustomizationFilter.ONLY_PROGRESSION_STYLES): False}}, 
   KEY_FAVORITES: {BOOTCAMP_VEHICLE: 0, 
                   CURRENT_VEHICLE: 0, 
                   ROYALE_VEHICLE: 0, 
                   FALLOUT_VEHICLES: {}}, 
   KEY_MANUAL: {LOBBY_MENU_MANUAL_TRIGGER_SHOWN: False, 
                LOBBY_MENU_BOOTCAMP_TRIGGER_SHOWN: False, 
                MANUAL_NEW_CONTENT: {}}, 
   KEY_SETTINGS: {b'unitWindow': {SELECTED_INTRO_VEHICLES_FIELD: []}, b'vehicleSellDialog': {b'isOpened': False}, 
                  KNOWN_SELECTOR_BATTLES: (set()), 
                  b'tankmanDropSkillIdx': 0, 
                  b'cursor': False, 
                  b'arcade': {b'mixing': {b'alpha': 100, b'type': 3}, b'gunTag': {b'alpha': 100, b'type': 9}, b'centralTag': {b'alpha': 100, b'type': 4}, b'net': {b'alpha': 100, b'type': 0}, b'reloader': {b'alpha': 100, b'type': 0}, b'condition': {b'alpha': 100, b'type': 0}, b'cassette': {b'alpha': 100, b'type': 0}, b'reloaderTimer': {b'alpha': 100, b'type': 0}, b'zoomIndicator': {b'alpha': 100, b'type': 0}}, b'sniper': {b'mixing': {b'alpha': 90, b'type': 3}, b'gunTag': {b'alpha': 90, b'type': 9}, b'centralTag': {b'alpha': 90, b'type': 4}, b'net': {b'alpha': 90, b'type': 0}, b'reloader': {b'alpha': 90, b'type': 0}, b'condition': {b'alpha': 90, b'type': 0}, b'cassette': {b'alpha': 90, b'type': 0}, b'reloaderTimer': {b'alpha': 100, b'type': 0}, b'zoomIndicator': {b'alpha': 100, b'type': 0}}, b'spgAim': {(SPGAim.SHOTS_RESULT_INDICATOR): True, 
                              (SPGAim.SPG_SCALE_WIDGET): True, 
                              (SPGAim.AUTO_CHANGE_AIM_MODE): True, 
                              (SPGAim.AIM_ENTRANCE_MODE): 0}, 
                  b'contour': {(CONTOUR.ENHANCED_CONTOUR): True, 
                               (CONTOUR.CONTOUR_PENETRABLE_ZONE): 0, 
                               (CONTOUR.CONTOUR_IMPENETRABLE_ZONE): 0}, 
                  LAST_ARTY_CTRL_MODE: (CTRL_MODE_NAME.STRATEGIC), 
                  b'markers': {b'ally': {b'markerBaseIcon': False, 
                                         b'markerBaseLevel': True, 
                                         b'markerBaseHpIndicator': True, 
                                         b'markerBaseDamage': True, 
                                         b'markerBaseHp': 1, 
                                         b'markerBaseVehicleName': True, 
                                         b'markerBasePlayerName': False, 
                                         b'markerBaseAimMarker2D': False, 
                                         b'markerBaseVehicleDist': False, 
                                         b'markerAltIcon': True, 
                                         b'markerAltLevel': True, 
                                         b'markerAltHpIndicator': True, 
                                         b'markerAltDamage': True, 
                                         b'markerAltHp': 1, 
                                         b'markerAltVehicleName': True, 
                                         b'markerAltPlayerName': True, 
                                         b'markerAltAimMarker2D': False, 
                                         b'markerAltVehicleDist': True}, 
                               b'enemy': {b'markerBaseIcon': False, 
                                          b'markerBaseLevel': True, 
                                          b'markerBaseHpIndicator': True, 
                                          b'markerBaseDamage': True, 
                                          b'markerBaseHp': 1, 
                                          b'markerBaseVehicleName': True, 
                                          b'markerBasePlayerName': False, 
                                          b'markerBaseAimMarker2D': True, 
                                          b'markerBaseVehicleDist': False, 
                                          b'markerAltIcon': True, 
                                          b'markerAltLevel': True, 
                                          b'markerAltHpIndicator': True, 
                                          b'markerAltDamage': True, 
                                          b'markerAltHp': 1, 
                                          b'markerAltVehicleName': True, 
                                          b'markerAltPlayerName': True, 
                                          b'markerAltAimMarker2D': True, 
                                          b'markerAltVehicleDist': True}, 
                               b'dead': {b'markerBaseIcon': False, 
                                         b'markerBaseLevel': False, 
                                         b'markerBaseHpIndicator': False, 
                                         b'markerBaseDamage': True, 
                                         b'markerBaseHp': 3, 
                                         b'markerBaseVehicleName': True, 
                                         b'markerBasePlayerName': False, 
                                         b'markerBaseAimMarker2D': False, 
                                         b'markerBaseVehicleDist': False, 
                                         b'markerAltIcon': True, 
                                         b'markerAltLevel': True, 
                                         b'markerAltHpIndicator': True, 
                                         b'markerAltDamage': True, 
                                         b'markerAltHp': 1, 
                                         b'markerAltVehicleName': True, 
                                         b'markerAltPlayerName': True, 
                                         b'markerAltAimMarker2D': False, 
                                         b'markerAltVehicleDist': True}}, 
                  COMP7_PREBATTLE_CAROUSEL_ROW_VALUE: (-1), 
                  COMP7_PREBATTLE_MINIMAP_SIZE: (-1), 
                  COMP7_IS_VOIP_IN_BATTLE_ACTIVATED: False, 
                  RANKED_IS_VOIP_IN_BATTLE_ACTIVATED: False, 
                  b'showVehicleIcon': False, 
                  b'showVehicleLevel': False, 
                  b'showExInf4Destroyed': False, 
                  b'ingameHelpVersion': (-1), 
                  b'isColorBlind': False, 
                  b'useServerAim': False, 
                  b'showDamageIcon': True, 
                  b'showVehiclesCounter': True, 
                  b'minimapAlpha': 0, 
                  MINIMAP_SIZE: 1, 
                  (GAME.SHOW_VEHICLE_HP_IN_PLAYERS_PANEL): 1, 
                  (GAME.SHOW_VEHICLE_HP_IN_MINIMAP): 1, 
                  b'minimapRespawnSize': 0, 
                  b'minimapViewRange': True, 
                  b'minimapMaxViewRange': True, 
                  b'minimapDrawRange': True, 
                  b'minimapAlphaEnabled': False, 
                  (GAME.MINIMAP_MIN_SPOTTING_RANGE): True, 
                  b'epicMinimapZoom': 1.5, 
                  b'mapsTrainingMinimapSize': 3, 
                  b'increasedZoom': True, 
                  b'sniperModeByShift': True, 
                  b'nationalVoices': False, 
                  b'enableVoIP': True, 
                  b'replayEnabled': 2, 
                  b'sniperZoom': 0, 
                  (GAME.SNIPER_MODE_STABILIZATION): True, 
                  (GAME.SWITCH_SETUPS_IN_LOADING): None, 
                  (GAME.HULLLOCK_ENABLED): True, 
                  (GAME.PRE_COMMANDER_CAM): True, 
                  (GAME.COMMANDER_CAM): True, 
                  (GAME.SCROLL_SMOOTHING): True, 
                  (GAME.SHOW_THERMAL_VISION_SECTOR_ON_MAP): True, 
                  (GAME.ENABLE_THERMAL_VISION_EFFECT): True, 
                  (GAME.ENABLE_THERMAL_VISION_SECTOR_EFFECT): True, 
                  b'hangarCamPeriod': 1, 
                  b'hangarCamParallaxEnabled': True, 
                  b'players_panel': {b'state': 3, 
                                     b'showLevels': True, 
                                     b'showTypes': True}, 
                  b'epic_random_players_panel': {b'state': 5}, 
                  b'gameplayMask': (gameplay_ctx.getDefaultMask()), 
                  b'statsSorting': {b'iconType': b'tank', 
                                    b'sortDirection': b'descending'}, 
                  b'statsSortingSortie': {b'iconType': b'tank', 
                                          b'sortDirection': b'descending'}, 
                  b'statsSortingComp7': {b'iconType': b'prestigePoints', 
                                         b'sortDirection': b'descending'}, 
                  b'backDraftInvert': False, 
                  QUESTS: {b'lastVisitTime': (-1), 
                           b'visited': [], b'naVisited': [], b'personalMissions': {b'introShown': False, 
                                                 b'operationsVisited': (set()), 
                                                 b'headerAlert': False}, 
                           DAILY_QUESTS: {b'lastVisitedDQTabIdx': None, 
                                          b'premMissionsTabDiscovered': False, 
                                          b'lastBonusMissionVisited': b'', 
                                          DAILY_QUESTS_INTRO_SEEN: False}, 
                           QUEST_DELTAS: {QUEST_DELTAS_COMPLETION: (dict()), 
                                          QUEST_DELTAS_PROGRESS: (dict()), 
                                          QUEST_DELTAS_TOKENS_PROGRESS: (dict())}}, 
                  b'checkBoxConfirmator': {b'questsConfirmDialogShow': True, 
                                           b'questsConfirmDialogShowPM2': True, 
                                           b'questsConfirmDialogShowPM3': True}, 
                  DOG_TAGS: {b'lastVisitedDogTagsTabIdx': None, 
                             b'onboardingEnabled': True, 
                             b'seenComps': (set())}, 
                  WOT_PLUS: {b'isFirstTime': True, 
                             b'isWotPlusEnabled': True, 
                             b'isGoldReserveEnabled': True, 
                             b'isPassiveXpEnabled': True, 
                             b'isFreeDemountingEnabled': True, 
                             b'isExcludedMapEnabled': False, 
                             b'isSubscrbExcludedMapSlotsEnabled': False, 
                             b'isExcludedMapsKillSwitchInitialized': False, 
                             b'isExclusiveVehicleEnabled': True, 
                             b'isDailyQuestsExtraRewardsEnabled': True, 
                             b'isTeamCreditsBonusEnabled': True, 
                             b'amountOfDailyAttendance': 0}, 
                  TELECOM_RENTALS: {b'isTelecomRentalsEnabled': True, 
                                    b'isTelecomRentalsBlocked': True}, 
                  CUSTOMIZATION_SECTION: {CAROUSEL_ARROWS_HINT_SHOWN_FIELD: False, 
                                          PROJECTION_DECAL_HINT_SHOWN_FIELD: False}, 
                  SESSION_STATS_SECTION: {BATTLE_EFFICIENCY_SECTION_EXPANDED_FIELD: False}, b'showVehModelsOnMap': 0, 
                  b'battleLoadingInfo': 1, 
                  b'battleLoadingRankedInfo': 1, 
                  b'relativePower': False, 
                  b'relativeArmor': False, 
                  b'relativeMobility': False, 
                  b'relativeVisibility': False, 
                  b'relativeCamouflage': False, 
                  b'relativeAbility': False, 
                  b'interfaceScale': 0.0, 
                  b'medKitInstalled': False, 
                  b'repairKitInstalled': False, 
                  b'fireExtinguisherInstalled': False, 
                  b'PveTriggerShown': False, 
                  b'isEpicPerformanceWarningClicked': False, 
                  LAST_PROMO_PATCH_VERSION: b'', 
                  LAST_CALENDAR_SHOW_TIMESTAMP: b'', 
                  LAST_RESTORE_NOTIFICATION: None, 
                  b'dynamicRange': 0, 
                  b'soundDevice': 0, 
                  b'bassBoost': False, 
                  b'lowQualitySound': (WWISE.isMSR()), 
                  b'nightMode': False, 
                  (SOUND.DETECTION_ALERT_SOUND): b'lightbulb', 
                  (SOUND.ARTY_SHOT_ALERT_SOUND): b'artillery_lightbulb', 
                  PREVIEW_INFO_PANEL_IDX: 0, 
                  (GAME.HANGAR_CREW_WIDGET): 0, 
                  b'carouselType': 0, 
                  b'doubleCarouselType': 0, 
                  b'contentType': 0, 
                  b'vehicleCarouselStats': True, 
                  WHEELED_DEATH_DELAY_COUNT: 10, 
                  NEW_SETTINGS_COUNTER: {b'GameSettings': {b'gameplay_epicStandard': True, 
                                                           (BattleCommStorageKeys.SHOW_LOCATION_MARKERS): True, 
                                                           (GAME.DISPLAY_PLATOON_MEMBERS): True, 
                                                           b'hangarCamParallaxEnabled': True, 
                                                           b'hangarCamPeriod': True, 
                                                           (GAME.HULLLOCK_ENABLED): True, 
                                                           (GAME.SHOW_VEHICLE_HP_IN_MINIMAP): True, 
                                                           (GAME.SHOW_VEHICLE_HP_IN_PLAYERS_PANEL): True, 
                                                           (GAME.PRE_COMMANDER_CAM): True, 
                                                           (GAME.COMMANDER_CAM): True, 
                                                           (GAME.SHOW_DAMAGE_ICON): True, 
                                                           ANONYMIZER: True, 
                                                           (GAME.SHOW_VICTIMS_DOGTAG): True, 
                                                           (GAME.GAMEPLAY_ONLY_10_MODE): True, 
                                                           (GAME.SHOW_ARTY_HIT_ON_MAP): True, 
                                                           (GAME.SWITCH_SETUPS_IN_LOADING): True, 
                                                           (GAME.SCROLL_SMOOTHING): True, 
                                                           (GAME.LIMITED_UI_ACTIVE): True, 
                                                           (GAME.GAMEPLAY_DEV_MAPS): True, 
                                                           (GAME.SHOW_THERMAL_VISION_SECTOR_ON_MAP): True, 
                                                           (GAME.ENABLE_THERMAL_VISION_EFFECT): True, 
                                                           (GAME.ENABLE_THERMAL_VISION_SECTOR_EFFECT): True}, 
                                         b'GraphicSettings': {b'ScreenSettings': {b'gammaSetting': True, 
                                                                                  b'colorFilter': True, 
                                                                                  (GRAPHICS.INTERFACE_SCALE): True}, 
                                                              b'AdvancedGraphicSettings': {b'HAVOK_ENABLED': True, 
                                                                                           b'TERRAIN_TESSELLATION_ENABLED': True, 
                                                                                           b'SNIPER_MODE_TERRAIN_TESSELLATION_ENABLED': True, 
                                                                                           b'TRACK_PHYSICS_QUALITY': True}}, 
                                         b'FeedbackSettings': {b'feedbackBattleBorderMap': {b'battleBorderMapType': True, 
                                                                                            b'battleBorderMapMode': True}, 
                                                               b'feedbackQuestsProgress': {(ScorePanelStorageKeys.SHOW_HP_VALUES): True, 
                                                                                           (ScorePanelStorageKeys.SHOW_HP_DIFFERENCE): True, 
                                                                                           (ScorePanelStorageKeys.ENABLE_TIER_GROUPING): True, 
                                                                                           (ScorePanelStorageKeys.SHOW_HP_BAR): True, 
                                                                                           b'progressViewType': True, 
                                                                                           b'progressViewConditions': True}, 
                                                               b'feedbackDamageIndicator': {b'damageIndicatorAllies': True}, 
                                                               b'feedbackSixthSense': {b'indicatorSize': 0, 
                                                                                       b'indicatorAlpha': 100}}, 
                                         b'ControlsSettings': {b'highlightLocation': True, 
                                                               b'showQuestProgress': True, 
                                                               b'chargeFire': True, 
                                                               b'affirmative': True, 
                                                               b'negative': True, 
                                                               b'showPersonalReserves': True, 
                                                               (CONTROLS.MOUSE_ASSAULT_SENS): True}, 
                                         b'AimSettings': {(AIM.SPG): {(SPGAim.AUTO_CHANGE_AIM_MODE): True, 
                                                                      (SPGAim.SPG_SCALE_WIDGET): True, 
                                                                      (SPGAim.SPG_STRATEGIC_CAM_MODE): True, 
                                                                      (SPGAim.SHOTS_RESULT_INDICATOR): True, 
                                                                      (SPGAim.AIM_ENTRANCE_MODE): True}, 
                                                          (AIM.CONTOUR): {(CONTOUR.ENHANCED_CONTOUR): True, 
                                                                          (CONTOUR.CONTOUR_PENETRABLE_ZONE): True, 
                                                                          (CONTOUR.CONTOUR_IMPENETRABLE_ZONE): True}}, 
                                         (SETTINGS_GROUP.MARKERS_SETTINGS): {(MARKERS.ENEMY): {(MARKER_SETTINGS.MARKER_BASE_VEHICLE_DIST): True, 
                                                                                               (MARKER_SETTINGS.MARKER_ALT_VEHICLE_DIST): True}, 
                                                                             (MARKERS.ALLY): {(MARKER_SETTINGS.MARKER_BASE_VEHICLE_DIST): True, 
                                                                                              (MARKER_SETTINGS.MARKER_ALT_VEHICLE_DIST): True}}, 
                                         b'SoundSettings': {b'artyBulbVoices': True}}, 
                  CLAN_PREBATTLE_SORTING_KEY: 0, 
                  SHOW_OPT_DEVICE_HINT: True, 
                  SHOW_OPT_DEVICE_HINT_TROPHY: True, 
                  SHOW_OPT_MODERNIZED_DEVICE_HINT: True, 
                  SHOW_ECONOMIC_DIRECTIVES_HINT: True, 
                  LAST_BADGES_VISIT: 0, 
                  LAST_SELECTED_SUFFIX_BADGE_ID: 0, 
                  ENABLE_RANKED_ANIMATIONS: True, 
                  COLOR_SETTINGS_TAB_IDX: 0, 
                  COLOR_SETTINGS_SHOWS_COUNT: 0, 
                  SELECTED_QUEST_IN_REPLAY: None, 
                  APPLIED_COLOR_SETTINGS: {}, LAST_SELECTED_PM_BRANCH: 0, 
                  CRYSTALS_INFO_SHOWN: False, 
                  TRAJECTORY_VIEW_HINT_SECTION: {HINTS_LEFT: 3, 
                                                 LAST_DISPLAY_DAY: 0, 
                                                 NUM_BATTLES: 0}, 
                  ASSAULT_CAMERA_HINT_SECTION: {HINTS_LEFT: 5, 
                                                LAST_DISPLAY_DAY: 0, 
                                                NUM_BATTLES: 0}, 
                  DYN_SQUAD_HINT_SECTION: {HINTS_LEFT: 3, 
                                           LAST_DISPLAY_DAY: 0, 
                                           NUM_BATTLES: 0}, 
                  PRE_BATTLE_HINT_SECTION: {QUEST_PROGRESS_HINT_SECTION: {HINTS_LEFT: 3, 
                                                                          LAST_DISPLAY_DAY: 0, 
                                                                          NUM_BATTLES: 0}, 
                                            HELP_SCREEN_HINT_SECTION: {}, IBC_HINT_SECTION: {HINTS_LEFT: 10}, 
                                            RESERVES_HINT_SECTION: {HINTS_LEFT: 10}}, 
                  PRE_BATTLE_ROLE_HINT_SECTION: {}, FUN_RANDOM_HINT_SECTION: {}, MAPBOX_HINT_SECTION: {}, DEV_MAPS_HINT_SECTION: {}, COMMANDER_CAM_HINT_SECTION: {HINTS_LEFT: 5}, 
                  MINIMAP_IBC_HINT_SECTION: {HINTS_LEFT: 10}, 
                  WATCHED_PRE_BATTLE_TIPS_SECTION: {}, SIEGE_HINT_SECTION: {HINTS_LEFT: 3, 
                                       LAST_DISPLAY_DAY: 0, 
                                       NUM_BATTLES: 0}, 
                  WHEELED_MODE_HINT_SECTION: {HINTS_LEFT: 3, 
                                              LAST_DISPLAY_DAY: 0, 
                                              NUM_BATTLES: 0}, 
                  TURBO_SHAFT_ENGINE_MODE_HINT_SECTION: {HINTS_LEFT: 3, 
                                                         LAST_DISPLAY_DAY: 0, 
                                                         NUM_BATTLES: 0}, 
                  ROCKET_ACCELERATION_MODE_HINT_SECTION: {HINTS_LEFT: 3, 
                                                          LAST_DISPLAY_DAY: 0, 
                                                          NUM_BATTLES: 0}, 
                  RADAR_HINT_SECTION: {HINTS_LEFT: 3, 
                                       LAST_DISPLAY_DAY: 0, 
                                       NUM_BATTLES: 0}, 
                  CREW_SKINS_VIEWED: {}, CREW_BOOKS_VIEWED: {(CREW_BOOK_RARITY.CREW_COMMON): {}, (CREW_BOOK_RARITY.CREW_EPIC): {}, (CREW_BOOK_RARITY.CREW_RARE): {}, (CREW_BOOK_RARITY.PERSONAL): 0, 
                                      (CREW_BOOK_RARITY.UNIVERSAL): 0}, 
                  CREW_SKINS_HISTORICAL_VISIBLE: (
                                                True, True), 
                  VEHICLES_WITH_BLUEPRINT_CONFIRM: {}, IS_FIRST_ENTRY_BY_DIVISION_ID: {}, STYLE_PREVIEW_VEHICLES_POOL: [], RANKED_STYLED_VEHICLES_POOL: [], RANKED_WEB_INFO: None, 
                  RANKED_WEB_INFO_UPDATE: None, 
                  RANKED_AWARDS_BUBBLE_YEAR_REACHED: False, 
                  RANKED_CURRENT_AWARDS_BUBBLE_YEAR_REACHED: False, 
                  NATION_CHANGE_VIEWED: False, 
                  LAST_BATTLE_PASS_POINTS_SEEN: {}, IS_BATTLE_PASS_MARATHON_STARTED: False, 
                  IS_BATTLE_PASS_COLLECTION_SEEN: False, 
                  WIDGET_HINT_TRIGGER: 0, 
                  MODULES_ANIMATION_SHOWN: False, 
                  SUBTITLES: True, 
                  RANKED_YEAR_POSITION: None, 
                  TOP_OF_TREE_CONFIG: {}, BECOME_ELITE_VEHICLES_WATCHED: (set()), 
                  (GAME.GAMEPLAY_ONLY_10_MODE): False, 
                  (GAME.GAMEPLAY_DEV_MAPS): True, 
                  MAPBOX_PROGRESSION: {b'previous_battles_played': 0, 
                                       b'visited_maps': [], b'stored_rewards': {}, b'lastCycleId': None}, 
                  MAPBOX_SURVEYS: {}, UNLOCK_VEHICLES_IN_BATTLE_HINTS: 5, 
                  MODE_SELECTOR_BATTLE_PASS_SHOWN: {}, RANKED_LAST_CYCLE_ID: None, 
                  EPIC_LAST_CYCLE_ID: None, 
                  FUN_RANDOM_LAST_PRESET: b'undefined', 
                  SHOW_ABILITY_ADVANCE_ANIM: True, 
                  SHOW_DEMO_ACC_REGISTRATION: False, 
                  IS_CUSTOMIZATION_INTRO_VIEWED: False, 
                  CUSTOMIZATION_STYLE_ITEMS_VISITED: (set()), 
                  SHOWN_PERSONAL_RESERVES_INTRO: False, 
                  SHOWN_WOT_PLUS_INTRO: True, 
                  SHOWN_WOT_PLUS_COUNTER: False, 
                  PREMIUM_QUESTS_NOTIFICATION: True, 
                  SUBSCRIPTION_DAILY_QUESTS_INTRO_SHOWN: False, 
                  SUBSCRIPTION_DAILY_QUESTS_SHINE_SHOWN: False, 
                  SUBSCRIPTION_LAST_EXPIRATION_NOTIFICATION: 0, 
                  HAS_LEFT_VERSUS_AI: False, 
                  OPT_DEVICE_TAB_VISITED: {}, (BattleMatters.BATTLE_MATTERS_SETTINGS): {(BattleMatters.BATTLES_COUNT_WITHOUT_PROGRESS): 0, 
                                                            (BattleMatters.QUEST_IDX_FOR_LAST_UPDATED_PROGRESS): 0, 
                                                            (BattleMatters.LAST_QUEST_PROGRESS): 0, 
                                                            (BattleMatters.REMINDER_LAST_DISPLAY_TIME): 0}, 
                  BR_PROGRESSION_POINTS_SEEN: 0, 
                  ROYALE_INTRO_VIDEO_SHOWN: False, 
                  (Winback.WINBACK_SETTINGS): {(Winback.INTRO_LAST_TIME_SHOWN): 0, 
                                               (Winback.NEED_SHOW_INTRO): True, 
                                               (Winback.HAS_LEFT_VERSUS_AI_FROM_WINBACK): False, 
                                               (Winback.WINBACK_BATTLES_COUNT): 0, 
                                               (Winback.WINBACK_PROGRESSION_POINTS_SEEN): {}}, 
                  ACHIEVEMENTS_INFO: {ACHIEVEMENTS_WTR_RANKS: {}, ACHIEVEMENTS_INITIAL_BATTLE_COUNT: (-1), 
                                      ACHIEVEMENTS_MAX_WTR_POINTS: 0, 
                                      ACHIEVEMENTS_FIRST_ENTRY_STATUS: 0, 
                                      ACHIEVEMENTS_RATING_CALCULATED_STATUS: 0, 
                                      ACHIEVEMENTS_EDITING_ENABLED_STATUS: 0, 
                                      ACHIEVEMENTS_MEDAL_ADDED_STATUS: 0, 
                                      ACHIEVEMENTS_RATING_CHANGED_STATUS: 0, 
                                      ACHIEVEMENTS_MEDAL_COUNT_INFO: 0, 
                                      ACHIEVEMENTS_WTR_PREV_POINTS_NOTIFICATION: 0, 
                                      ACHIEVEMENTS_WTR_INFO: {ACHIEVEMENTS_WTR_PREV_POINTS: 0, 
                                                              ACHIEVEMENTS_WTR_PREV_RANK: 0, 
                                                              ACHIEVEMENTS_WTR_PREV_SUB_RANK: 0}, 
                                      PREV_ACHIEVEMENTS_NAME_LIST: []}, 
                  GUI_LOOT_BOXES: {LOOT_BOXES_INTRO_SHOWN: (set()), 
                                   LOOT_BOXES_OPEN_ANIMATION_ENABLED: True, 
                                   LOOT_BOXES_VIEWED_COUNT: 0, 
                                   LOOT_BOXES_KEY_VIEWED_COUNT: 0, 
                                   LOOT_BOXES_VIEWED_HAS_INFINITE: False, 
                                   LOOT_BOXES_COUNT: {}, LOOT_BOXES_LAST_ADDED_ID: 0, 
                                   LOOT_BOXES_SHORT_STAT_STATE: 0, 
                                   LOOT_BOXES_STATS_HINT_STATE: 0, 
                                   LOOT_BOXES_STATS_NO_BOX_HINT_STATE: 0, 
                                   KEY_LOOTBOX_TRIGGER_HINT_SHOWN: False}, 
                  NEW_YEAR: {NY_DAILY_QUESTS_VISITED: False, 
                             NY_BONUS_DAILY_QUEST_VISITED: False, 
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
                             NY_INTRO_SEEN: False, 
                             NY_LAST_SEEN_TOTAL_BONUS: 0, 
                             NY_DAILY_QUESTS_HOVERED: {}, NY_WEEKLY_QUESTS_HOVERED: {}, NY_DAILY_MEDIA: [], NY_GENERATION_TIME: 0, 
                             NY_DAILY_VIDEO_VISITED_AT: 0, 
                             NY_DAILY_VIDEO_DAY_VISITED: False, 
                             NY_FIRST_VIDEO_SHUFFLE: False, 
                             NY_ACTIVE_WIDGET_TRANSITION_SHOWN: False, 
                             NY_PET_SLOT_VISITED: False, 
                             NY_GREETINGS_SEEN: False}, 
                  DEFERRED_LOG_PLAYER_SETTINGS_ACTIONS: {
                                                       SettingsLogActions.SETTINGS_INITED}, 
                  SHOWN_SUMMER_SALE_INTRO: False}, 
   KEY_COUNTERS: {NEW_HOF_COUNTER: {(PROFILE_CONSTANTS.HOF_ACHIEVEMENTS_BUTTON): True, 
                                    (PROFILE_CONSTANTS.HOF_VEHICLES_BUTTON): True, 
                                    (PROFILE_CONSTANTS.HOF_VIEW_RATING_BUTTON): True}, 
                  NEW_LOBBY_TAB_COUNTER: {}, REFERRAL_COUNTER: 1, 
                  CLAN_NOTIFICATION_COUNTERS: {}, RANKED_AWARDS_COUNTER: 1, 
                  RANKED_INFO_COUNTER: 1, 
                  RANKED_YEAR_RATING_COUNTER: 1, 
                  RANKED_SHOP_COUNTER: 1, 
                  RANKED_ENTITLEMENT_EVENTS_AMOUNT: 0, 
                  BOOSTERS_FOR_CREDITS_SLOT_COUNTER: 1, 
                  SENIORITY_AWARDS_COUNTER: 1, 
                  DEMOUNT_KIT_SEEN: False, 
                  RECERTIFICATION_FORM_SEEN: False, 
                  NEW_SHOP_TABS: {IS_COLLECTIBLE_VEHICLES_VISITED: False}, 
                  VPP_ENTRY_POINT_LAST_SEEN_STEP: {}}, 
   KEY_NOTIFICATIONS: {ELEN_NOTIFICATIONS: {(MISSIONS_CONSTANTS.ELEN_EVENT_STARTED_NOTIFICATION): (set()), 
                                            (MISSIONS_CONSTANTS.ELEN_EVENT_FINISHED_NOTIFICATION): (set()), 
                                            (MISSIONS_CONSTANTS.ELEN_EVENT_TAB_VISITED): (set())}, 
                       RECRUIT_NOTIFICATIONS: (set()), 
                       PROGRESSIVE_REWARD_VISITED: False, 
                       VIEWED_OFFERS: (set()), 
                       OFFERS_DISABLED_MSG_SEEN: False, 
                       BLUEPRINTS_CONVERT_SALE_STARTED_SEEN: False, 
                       CLAN_NEWS_SEEN: False, 
                       SENIORITY_AWARDS_COINS_REMINDER_SHOWN_TIMESTAMP: None, 
                       ACHIEVEMENTS_VISITED: False, 
                       INTEGRATED_AUCTION_NOTIFICATIONS: {AUCTION_STAGE_START_SEEN: (set()), 
                                                          AUCTION_FINISH_STAGE_SEEN: (set())}, 
                       BLACK_MARKET_AUCTION_NOTIFICATIONS: {BLACK_MARKET_VEHICLE_STAGE_START_SEEN: (set()), 
                                                            BLACK_MARKET_VEHICLE_FINISH_STAGE_SEEN: (set()), 
                                                            BLACK_MARKET_STAGE_START_SEEN: (set()), 
                                                            BLACK_MARKET_FINISH_STAGE_SEEN: (set())}, 
                       TRADING_CARAVAN_NOTIFICATIONS: {TRADING_CARAVAN_REFILL_SEEN: (set())}, 
                       CUSTOM_NOTIFICATIONS: {CUSTOM_NOTIFICATIONS_SEEN: (set())}, 
                       FUN_RANDOM_NOTIFICATIONS: {FUN_RANDOM_NOTIFICATIONS_FROZEN: (set()), 
                                                  FUN_RANDOM_NOTIFICATIONS_PROGRESSIONS: (set()), 
                                                  FUN_RANDOM_NOTIFICATIONS_SUB_MODES: (set())}, 
                       RESOURCE_WELL_NOTIFICATIONS: {RESOURCE_WELL_START_SHOWN: (set()), 
                                                     RESOURCE_WELL_END_SHOWN: (set())}, 
                       COLLECTIONS_NOTIFICATIONS: {COLLECTION_START_SEEN: [], COLLECTION_RENEW_SEEN: {}, COLLECTIONS_UPDATED_ENTRY_SEEN: False}, 
                       REFERRAL_PROGRAM_PGB_FULL: False}, 
   KEY_SESSION_SETTINGS: {STORAGE_VEHICLES_CAROUSEL_FILTER_1: {b'ussr': False, 
                                                               b'germany': False, 
                                                               b'usa': False, 
                                                               b'china': False, 
                                                               b'france': False, 
                                                               b'uk': False, 
                                                               b'japan': False, 
                                                               b'czech': False, 
                                                               b'sweden': False, 
                                                               b'poland': False, 
                                                               b'italy': False, 
                                                               b'intunion': False, 
                                                               b'lightTank': False, 
                                                               b'mediumTank': False, 
                                                               b'heavyTank': False, 
                                                               b'SPG': False, 
                                                               b'AT-SPG': False, 
                                                               b'level_1': False, 
                                                               b'level_2': False, 
                                                               b'level_3': False, 
                                                               b'level_4': False, 
                                                               b'level_5': False, 
                                                               b'level_6': False, 
                                                               b'level_7': False, 
                                                               b'level_8': False, 
                                                               b'level_9': False, 
                                                               b'level_10': False, 
                                                               b'level_11': False, 
                                                               b'premium': False, 
                                                               b'elite': False, 
                                                               b'igr': False, 
                                                               b'rented': True, 
                                                               b'event': True, 
                                                               b'gameMode': False, 
                                                               b'favorite': False, 
                                                               b'bonus': False, 
                                                               b'battleRoyale': False, 
                                                               b'clanRented': False, 
                                                               b'searchNameVehicle': b''}, 
                          b'storage_shells': {b'filterMask': 0, 
                                              b'vehicleCD': None}, 
                          b'storage_crew_books': {b'filterMask': 0, 
                                                  b'nationID': (nations.NONE_INDEX)}, 
                          b'storage_consumables_tab': {b'filterMask': 0}, 
                          b'storage_modules': {b'filterMask': 0, 
                                               b'vehicleCD': None}, 
                          b'storage_reserves': {b'filterMask': 0}, 
                          b'storage_customization': {b'filterMask': 0}, 
                          b'storage_opt_devices': {b'filterMask': 0, 
                                                   b'vehicleCD': None}, 
                          STORAGE_BLUEPRINTS_CAROUSEL_FILTER: {b'ussr': False, 
                                                               b'germany': False, 
                                                               b'usa': False, 
                                                               b'china': False, 
                                                               b'france': False, 
                                                               b'uk': False, 
                                                               b'japan': False, 
                                                               b'czech': False, 
                                                               b'sweden': False, 
                                                               b'poland': False, 
                                                               b'italy': False, 
                                                               b'intunion': False, 
                                                               b'lightTank': False, 
                                                               b'mediumTank': False, 
                                                               b'heavyTank': False, 
                                                               b'SPG': False, 
                                                               b'AT-SPG': False, 
                                                               b'level_1': False, 
                                                               b'level_2': False, 
                                                               b'level_3': False, 
                                                               b'level_4': False, 
                                                               b'level_5': False, 
                                                               b'level_6': False, 
                                                               b'level_7': False, 
                                                               b'level_8': False, 
                                                               b'level_9': False, 
                                                               b'level_10': False, 
                                                               b'level_11': False, 
                                                               b'premium': False, 
                                                               b'elite': False, 
                                                               b'igr': False, 
                                                               b'rented': True, 
                                                               b'event': True, 
                                                               b'gameMode': False, 
                                                               b'favorite': False, 
                                                               b'crystals': False, 
                                                               b'bonus': False, 
                                                               b'battleRoyale': False, 
                                                               b'clanRented': False, 
                                                               b'searchNameVehicle': b'', 
                                                               b'unlock_available': False, 
                                                               b'can_convert': False, 
                                                               b'scroll_to': None}, 
                          LAST_STORAGE_VISITED_TIMESTAMP: (-1), 
                          SESSION_STATS_PREV_BATTLE_COUNT: 0, 
                          ACTIVE_TEST_PARTICIPATION_CONFIRMED: False, 
                          IS_SHOP_VISITED: False, 
                          LAST_SHOP_ACTION_COUNTER_MODIFICATION: None, 
                          OVERRIDEN_HEADER_COUNTER_ACTION_ALIASES: (set())}, 
   KEY_UI_FLAGS: {COMP7_UI_SECTION: {COMP7_WEEKLY_QUESTS_PAGE_TOKENS_COUNT: 0, 
                                     COMP7_FLAGS_VERSION: 0}, 
                  COLLECTIONS_SECTION: {COLLECTION_SHOWN_NEW_REWARDS: {}, COLLECTION_SHOWN_NEW_ITEMS: {}, COLLECTION_SHOWN_NEW_ITEMS_COUNT: {}, COLLECTION_TUTORIAL_COMPLETED: (set()), 
                                        COLLECTION_WAS_ENABLED: True, 
                                        COLLECTIONS_INTRO_SHOWN: False, 
                                        COLLECTIONS_TAB_SHOWN_IDS: (set()), 
                                        COLLECTIONS_TAB_SHOWN_NEW_ITEMS: {}, SHOWN_COMPLETED_COLLECTIONS: (set()), 
                                        LAST_SHOWN_NEW_COLLECTION: 0, 
                                        LAST_SHOWN_COLLECTION_BALANCE: {}}, 
                  b'uiSpamVisited_store': False, 
                  b'uiSpamVisited_profile': False, 
                  b'uiSpamVisited_profileHof': False, 
                  b'uiSpamVisited_profileTechniquePage': False, 
                  b'uiSpamVisited_sessionStats': False, 
                  b'uiSpamVisited_blueprintsButton': False, 
                  b'uiSpamVisited_missions': False, 
                  b'uiSpamVisited_MissionsMarathonView': False, 
                  b'uiSpamVisited_PersonalMissionOperations': False, 
                  b'uiSpamVisited_AmmunitionPanelHintZoneHint': False, 
                  b'uiSpamVisited_AmmunitionPanelBattleAbilitiesHint': False, 
                  b'uiSpamVisited_CustomizationProgressionViewHint': False, 
                  b'uiSpamVisited_TechTreeEvent': False, 
                  b'uiSpamVisited_DogTagHangarHint': False, 
                  b'uiSpamVisited_ModeSelectorWidgetsBtnHint': False, 
                  b'uiSpamVisited_PersonalReservesHangarHint': False, 
                  b'uiSpamVisited_ModernizedSetupTabHint': False, 
                  b'uiSpamVisited_OfferBannerWindow': False, 
                  b'uiSpamVisited_StrongholdView': False}, 
   (ArmoryYard.ARMORY_YARD_SETTINGS): {(ArmoryYard.ARMORY_YARD_LAST_INTRO_VIEWED): None, 
                                       (ArmoryYard.ARMORY_YARD_PREV_COMPLETED_QUESTS): {}, (ArmoryYard.EVENT_ANNOUNCEMENT): False, 
                                       (ArmoryYard.ANNOUNCEMENT_CHAPTER_PREFIX): False, 
                                       (ArmoryYard.CHAPTER_PREFIX): False, 
                                       (ArmoryYard.FINISH_CHAPTER_PREFIX): False, 
                                       (ArmoryYard.STYLE_QUEST_ENDS): False, 
                                       (ArmoryYard.ARMORY_YARD_CURRENT_SEASON): None, 
                                       (ArmoryYard.AY_SECTION_LAST_LISTENED_MESSAGE): 0, 
                                       (ArmoryYard.ARMORY_SHOP_INTRO_VIEWED): False, 
                                       (ArmoryYard.ARMORY_YARD_REROLL_INTRO_VIEWED): False, 
                                       (ArmoryYard.ARMORY_YARD_REROLL_BUTTON_HINT_VIEWED): False, 
                                       (ArmoryYard.ARMORY_YARD_REROLL_LAST_CURRENCY): None}, 
   (EarlyAccess.EARLY_ACCESS_SETTINGS): {(EarlyAccess.EARLY_ACCESS_CURRENT_SEASON): None, 
                                         (EarlyAccess.EVENT_ANNOUNCEMENT): False, 
                                         (EarlyAccess.EVENT_PAUSED): False, 
                                         (EarlyAccess.INTRO_SEEN): False, 
                                         (EarlyAccess.TREE_SEEN): False, 
                                         (EarlyAccess.EVENT_FINISHED): False, 
                                         (EarlyAccess.STARTED_CHAPTER_PREFIX): False, 
                                         (EarlyAccess.FINISHED_PROGRESSION): False, 
                                         (EarlyAccess.FINISHED_POSTRPOGRESSION): False, 
                                         (EarlyAccess.COMPLETED_PROGRESSION_PREFIX): False, 
                                         (EarlyAccess.COMPLETED_POSTPROGRESSION): False, 
                                         (EarlyAccess.ALL_TOKENS_RECEIVED): False, 
                                         (EarlyAccess.PREV_COMPLETED_QUESTS): {}}, 
   (PersonalMissions.PERSONAL_MISSIONS_SETTINGS): {(PersonalMissions.INTRO_SEEN): False, 
                                                   (PersonalMissions.PREV_COMPLETED_QUESTS): {}, (PersonalMissions.CURR_QUESTS_STATEMENT): {}, (PersonalMissions.OPERATIONS_VIDEO_REWARDS_STATUS): {}}, 
   (Paragons.PARAGONS_SETTINGS): {(Paragons.INTRO_SEEN): False, 
                                  (Paragons.NEED_TO_SHOW_ANIMATION_FOR_PARAGONS_UNLOCK_IDS): (set()), 
                                  (Paragons.NEED_TO_SHOW_ANIMATION_FOR_PARAGONS_RESET_BRANCH): False, 
                                  (Paragons.PROJECT_IS_ENABLED_NOTIFICATION_WAS_SHOWN): False, 
                                  (Paragons.PROJECT_IS_CONTINUING_NOTIFICATION_WAS_SHOWN): False, 
                                  (Paragons.CHAPTER_COUNTER): 1}, 
   (FunRandomMaps.FUN_RANDOM_MAPS_SETTINGS): {(FunRandomMaps.FUN_RANDOM_LAST_SELECTED_MAP): None, 
                                              (FunRandomMaps.FUN_RANDOM_WIDGET_VISITED_SUBMODES): (set()), 
                                              (FunRandomMaps.FUN_RANDOM_MODE_SELECTOR_CARD_SEEN_FEP_TYPES): (set())}, 
   (BlackMarket.BLACK_MARKET_SETTINGS): {(BlackMarket.BLACK_MARKET_ENTRY_CLICKED): False, 
                                         (BlackMarket.BLACK_MARKET_LAST_PHASE_SEEN): None}, 
   (Epic.EPIC_SETTINGS): {(Epic.SUPPLY_AIRSHIP_HINT_VIEWED): False, 
                          (Epic.SUPPLY_FLAMER_HINT_VIEWED): False, 
                          (Epic.SUPPLY_PILLBOX_HINT_VIEWED): False, 
                          (Epic.SUPPLY_MORTAR_HINT_VIEWED): False}, 
   DYNAMIC_SETTINGS_REPOSITORY: {}}

def _filterAccountSection(dataSec):
    for key, section in dataSec.items()[:]:
        if key == b'account':
            yield (
             key, section)

    return


def _pack(value):
    return base64.b64encode(pickle.dumps(value))


def _unpack(value):
    if value:
        return pickle.loads(base64.b64decode(value))
    else:
        return


def _recursiveStep(defaultDict, savedDict, finalDict):
    for key in defaultDict:
        defaultElement = defaultDict[key]
        savedElement = savedDict.get(key, None)
        if type(defaultElement) == dict:
            if savedElement is not None and type(savedElement) == dict:
                finalDict[key] = dict()
                _recursiveStep(defaultElement, savedElement, finalDict[key])
            else:
                finalDict[key] = deepcopy(defaultElement)
        elif savedElement is not None:
            finalDict[key] = savedElement
        else:
            finalDict[key] = defaultElement

    return


class AccountSettings(object):
    onSettingsChanging = Event.Event()
    version = 80
    settingsCore = dependency.descriptor(ISettingsCore)
    __cache = {b'login': None, b'section': None}
    __sessionSettings = {b'login': None, b'section': None}
    __isFirstRun = True
    __isCleanPC = False

    @staticmethod
    def clearCache():
        AccountSettings.__cache[b'login'] = None
        AccountSettings.__cache[b'section'] = None
        AccountSettings.__sessionSettings[b'login'] = None
        AccountSettings.__sessionSettings[b'section'] = None
        return

    @staticmethod
    def _readSection(ds, name):
        if not ds.has_key(name):
            ds.write(name, b'')
        return ds[name]

    @staticmethod
    def _readUserSection():
        if AccountSettings.__isFirstRun:
            AccountSettings.convert()
            AccountSettings.invalidateNewSettingsCounter()
            AccountSettings.__isFirstRun = False
        userLogin = AccountSettings.__getPlayerName()
        if AccountSettings.__cache[b'login'] != userLogin:
            ads = AccountSettings._readSection(Settings.g_instance.userPrefs, Settings.KEY_ACCOUNT_SETTINGS)
            for key, section in ads.items():
                if key == b'account' and section.readString(b'login') == userLogin:
                    AccountSettings.__cache[b'login'] = userLogin
                    AccountSettings.__cache[b'section'] = section
                    break
            else:
                newSection = ads.createSection(b'account')
                newSection.writeString(b'login', userLogin)
                AccountSettings.__cache[b'login'] = userLogin
                AccountSettings.__cache[b'section'] = newSection

        return AccountSettings.__cache[b'section']

    @staticmethod
    def isCleanPC():
        return AccountSettings.__isCleanPC

    @staticmethod
    def overrideDefaultSettings(name, value):
        if name not in DEFAULT_VALUES:
            return
        DEFAULT_VALUES[name].update(value)
        return

    @staticmethod
    def convert():
        ads = AccountSettings._readSection(Settings.g_instance.userPrefs, Settings.KEY_ACCOUNT_SETTINGS)
        currVersion = ads.readInt(b'version', 0)
        if currVersion != AccountSettings.version:
            if currVersion < 1:
                AccountSettings.__isCleanPC = True
                for key, section in ads.items()[:]:
                    newSection = ads.createSection(b'account')
                    newSection.copy(section)
                    newSection.writeString(b'login', key)
                    ads.deleteSection(key)

            else:
                AccountSettings.__isCleanPC = False
            if currVersion < 2:
                MARKER_SETTINGS_MAP = {b'showVehicleIcon': b'markerBaseIcon', b'showVehicleLevel': b'markerBaseLevel', 
                   b'showExInf4Destroyed': b'markerBaseDead'}
                for key, section in ads.items()[:]:
                    if key == b'account':
                        accSettings = AccountSettings._readSection(section, KEY_SETTINGS)
                        defaultMarker = DEFAULT_VALUES[KEY_SETTINGS][b'markers'].copy()
                        needUpdate = False
                        for key1, section1 in accSettings.items()[:]:
                            if key1 in MARKER_SETTINGS_MAP:
                                defaultMarker[MARKER_SETTINGS_MAP[key1]] = pickle.loads(base64.b64decode(accSettings.readString(key1)))
                                accSettings.deleteSection(key1)
                                needUpdate = True

                        if needUpdate:
                            accSettings.write(b'markers', base64.b64encode(pickle.dumps(defaultMarker)))

            if currVersion < 3:
                for key, section in ads.items()[:]:
                    if key == b'account':
                        accSettings = AccountSettings._readSection(section, KEY_SETTINGS)
                        defaultCursor = DEFAULT_VALUES[KEY_SETTINGS][b'arcade'].copy()
                        cassetteDefValues = DEFAULT_VALUES[KEY_SETTINGS][b'arcade'].copy()[b'cassette']
                        for key1, section1 in accSettings.items()[:]:
                            if key1 == b'cursors':
                                defaultCursor = pickle.loads(base64.b64decode(section1.asString))
                                defaultCursor[b'cassette'] = cassetteDefValues
                                accSettings.deleteSection(key1)
                                break

                        accSettings.write(b'cursors', base64.b64encode(pickle.dumps(defaultCursor)))

            if currVersion < 4:
                for key, section in ads.items()[:]:
                    if key == b'account':
                        accSettings = AccountSettings._readSection(section, KEY_SETTINGS)
                        defaultCursor = DEFAULT_VALUES[KEY_SETTINGS][b'arcade'].copy()
                        for key1, section1 in accSettings.items()[:]:
                            if key1 == b'cursors':
                                defaultCursor = pickle.loads(base64.b64decode(section1.asString))
                                accSettings.deleteSection(key1)
                                break

                        accSettings.write(b'arcade', base64.b64encode(pickle.dumps(defaultCursor)))

            if currVersion < 5:
                for key, section in ads.items()[:]:
                    if key == b'account':
                        accSettings = AccountSettings._readSection(section, KEY_SETTINGS)
                        for key1, section1 in accSettings.items()[:]:
                            if key1 == b'markers':
                                accSettings.deleteSection(key1)

            if currVersion < 6:
                for key, section in ads.items()[:]:
                    if key == b'account':
                        accSettings = AccountSettings._readSection(section, KEY_SETTINGS)
                        defaultSorting = DEFAULT_VALUES[KEY_SETTINGS][b'statsSorting'].copy()
                        accSettings.write(b'statsSorting', base64.b64encode(pickle.dumps(defaultSorting)))

            if currVersion < 7:
                for key, section in ads.items()[:]:
                    if key == b'account':
                        accSettings = AccountSettings._readSection(section, KEY_SETTINGS)
                        result = DEFAULT_VALUES[KEY_SETTINGS][b'sniper'].copy()
                        for settingName, settingPickle in accSettings.items()[:]:
                            if settingName == b'sniper':
                                settingValues = pickle.loads(base64.b64decode(settingPickle.asString))
                                accSettings.deleteSection(settingName)
                                try:
                                    for k, v in settingValues.iteritems():
                                        newName = k[3].lower() + k[4:]
                                        result[newName] = v

                                except Exception:
                                    pass

                            break

                        accSettings.write(b'sniper', base64.b64encode(pickle.dumps(result)))

            if currVersion < 8:
                for key, section in ads.items()[:]:
                    if key == b'account':
                        accFilters = AccountSettings._readSection(section, KEY_FILTERS)
                        for filterName, filterPickle in accFilters.items()[:]:
                            if filterName in (b'cs_intro_view_vehicle', b'cs_list_view_vehicle', b'cs_unit_view_vehicle', b'cs_unit_view_settings'):
                                result = DEFAULT_VALUES[KEY_FILTERS][filterName].copy()
                                value = pickle.loads(base64.b64decode(filterPickle.asString))
                                result.update(value)
                                accFilters.write(filterName, base64.b64encode(pickle.dumps(result)))

            if currVersion < 9:
                for key, section in ads.items()[:]:
                    if key == b'account':
                        accFilters = AccountSettings._readSection(section, KEY_FILTERS)
                        for filterName, filterPickle in accFilters.items()[:]:
                            if filterName in (b'cs_intro_view_vehicle', b'cs_list_view_vehicle', b'cs_unit_view_vehicle', b'cs_unit_view_settings'):
                                defaults = DEFAULT_VALUES[KEY_FILTERS][filterName].copy()
                                userValue = pickle.loads(base64.b64decode(filterPickle.asString))
                                userValue[b'compatibleOnly'] = defaults[b'compatibleOnly']
                                accFilters.write(filterName, base64.b64encode(pickle.dumps(userValue)))

            if currVersion < 10:
                for key, section in ads.items()[:]:
                    if key == b'account':
                        accSettings = AccountSettings._readSection(section, KEY_SETTINGS)
                        result = set(DEFAULT_VALUES[KEY_SETTINGS][KNOWN_SELECTOR_BATTLES]).copy()
                        for key1, section1 in accSettings.items()[:]:
                            if key1 == b'unitWindow':
                                unitWindowVal = pickle.loads(base64.b64decode(section1.asString))
                                if b'isOpened' in unitWindowVal:
                                    if unitWindowVal[b'isOpened']:
                                        result.add(SELECTOR_BATTLE_TYPES.UNIT)
                                        accSettings.write(KNOWN_SELECTOR_BATTLES, base64.b64encode(pickle.dumps(result)))
                                    section1.deleteSection(b'isOpened')
                                    break

            if currVersion < 11:
                for key, section in ads.items()[:]:
                    if key == b'account':
                        accSettings = AccountSettings._readSection(section, KEY_SETTINGS)
                        defaultSorting = DEFAULT_VALUES[KEY_SETTINGS][b'statsSortingSortie'].copy()
                        accSettings.write(b'statsSortingSortie', base64.b64encode(pickle.dumps(defaultSorting)))

            if currVersion < 12:
                for key, section in _filterAccountSection(ads):
                    accSettings = AccountSettings._readSection(section, KEY_SETTINGS)
                    if KNOWN_SELECTOR_BATTLES in accSettings.keys():
                        known = _unpack(accSettings[KNOWN_SELECTOR_BATTLES].asString)
                        if SELECTOR_BATTLE_TYPES.UNIT in known:
                            known.remove(SELECTOR_BATTLE_TYPES.UNIT)
                            accSettings.write(KNOWN_SELECTOR_BATTLES, _pack(known))
                    if b'unitWindow' in accSettings.keys():
                        accSettings.deleteSection(b'unitWindow')

            if currVersion < 13:
                enableVoIPVal = False
                if Settings.g_instance.userPrefs.has_key(b'enableVoIP'):
                    enableVoIPVal = Settings.g_instance.userPrefs.readBool(b'enableVoIP')
                for key, section in _filterAccountSection(ads):
                    AccountSettings._readSection(section, KEY_SETTINGS).write(b'enableVoIP', _pack(enableVoIPVal))

                Settings.g_instance.userPrefs.deleteSection(b'enableVoIP')
            if currVersion < 17:
                for key, section in ads.items()[:]:
                    if key == b'account':
                        accSettings = AccountSettings._readSection(section, KEY_FAVORITES)
                        for key1, section1 in accSettings.items()[:]:
                            if key1 == FALLOUT_VEHICLES:
                                accSettings.deleteSection(key1)

            if currVersion < 18:
                cmSection = AccountSettings._readSection(Settings.g_instance.userPrefs, Settings.KEY_COMMAND_MAPPING)
                for command, section in cmSection.items()[:]:
                    newSection = None
                    satelliteKeys = b''
                    fireKey = AccountSettings._readSection(section, b'fireKey').asString
                    if fireKey == b'KEY_SPACE':
                        if command == b'CMD_BLOCK_TRACKS':
                            pass
                        elif command == b'CMD_STOP_UNTIL_FIRE':
                            satelliteKeys = AccountSettings._readSection(section, b'satelliteKeys').asString
                            cmSection.deleteSection(b'CMD_STOP_UNTIL_FIRE')
                            newSection = cmSection.createSection(b'CMD_STOP_UNTIL_FIRE')
                        else:
                            newSection = cmSection.createSection(b'CMD_BLOCK_TRACKS')
                    if newSection is not None:
                        newSection.writeString(b'fireKey', b'KEY_NONE')
                        newSection.writeString(b'satelliteKeys', satelliteKeys)

                CommandMapping.g_instance.restoreUserConfig()
            if currVersion < 19:
                pass
            if currVersion < 20:
                for key, section in _filterAccountSection(ads):
                    accSettings = AccountSettings._readSection(section, KEY_SETTINGS)
                    accSettings.write(b'battleLoadingInfo', base64.b64encode(pickle.dumps(0)))
                    AccountSettings._readSection(section, KEY_FILTERS).deleteSection(b'joinCommandPressed')

            if currVersion < 21:
                import SoundGroups
                SoundGroups.g_instance.setMasterVolume(1.0)
                SoundGroups.g_instance.setVolume(b'music', 1.0)
                SoundGroups.g_instance.setVolume(b'vehicles', 1.0)
                SoundGroups.g_instance.setVolume(b'effects', 1.0)
                SoundGroups.g_instance.setVolume(b'gui', 1.0)
                SoundGroups.g_instance.setVolume(b'ambient', 1.0)
                SoundGroups.g_instance.savePreferences()
            if currVersion < 22:
                pass
            if currVersion < 23:
                for key, section in _filterAccountSection(ads):
                    AccountSettings._readSection(section, KEY_SETTINGS).deleteSection(b'FootballVehSelectedOnce')

            if currVersion < 24:
                for key, section in _filterAccountSection(ads):
                    AccountSettings._readSection(section, KEY_SETTINGS).deleteSection(b'FootballCustTriggerShown')
                    AccountSettings._readSection(section, KEY_SETTINGS).deleteSection(b'FootballVehSelectedOnce')

            if currVersion < 24:
                import SoundGroups
                SoundGroups.g_instance.setVolume(b'music_hangar', 1.0)
                SoundGroups.g_instance.setVolume(b'voice', 1.0)
                SoundGroups.g_instance.setVolume(b'ev_ambient', 0.8)
                SoundGroups.g_instance.setVolume(b'ev_effects', 0.8)
                SoundGroups.g_instance.setVolume(b'ev_gui', 0.8)
                SoundGroups.g_instance.setVolume(b'ev_music', 0.8)
                SoundGroups.g_instance.setVolume(b'ev_vehicles', 0.8)
                SoundGroups.g_instance.setVolume(b'ev_voice', 0.8)
                SoundGroups.g_instance.savePreferences()
            if currVersion < 25:
                for key, section in _filterAccountSection(ads):
                    accFilters = AccountSettings._readSection(section, KEY_FILTERS)
                    for filterName, filterPickle in accFilters.items():
                        if filterName in (b'shop_module', b'shop_shell', b'inventory_vehicle', b'inventory_module', b'inventory_shell', b'inventory_optionalDevice', b'inventory_equipment'):
                            defaults = DEFAULT_VALUES[KEY_FILTERS][filterName].copy()
                            accFilters.write(filterName, base64.b64encode(pickle.dumps(defaults)))

            if currVersion < 26:
                for key, section in _filterAccountSection(ads):
                    AccountSettings._readSection(section, KEY_SETTINGS).deleteSection(b'new_customization_items')
                    AccountSettings._readSection(section, KEY_SETTINGS).deleteSection(b'statsSortingEvent')

            if currVersion < 27:
                legacyToNewMode = {b'hidden': 0, 
                   b'short': 1, 
                   b'medium': 2, 
                   b'medium2': 3, 
                   b'large': 4}
                for key, section in _filterAccountSection(ads):
                    settingsSection = AccountSettings._readSection(section, KEY_SETTINGS)
                    if b'players_panel' in settingsSection.keys():
                        panelSettings = _unpack(settingsSection[b'players_panel'].asString)
                        if b'state' in panelSettings:
                            presentMode = panelSettings[b'state']
                            if presentMode in legacyToNewMode.keys():
                                panelSettings[b'state'] = legacyToNewMode[presentMode]
                                settingsSection.write(b'players_panel', _pack(panelSettings))

            if currVersion < 28:
                for key, section in _filterAccountSection(ads):
                    filters = AccountSettings._readSection(section, KEY_FILTERS)
                    filters.deleteSection(b'lastClubOpenedForApps')
                    filters.deleteSection(b'showInviteCommandBtnAnimation')

            if currVersion < 29:
                getSection = AccountSettings._readSection
                cmSection = getSection(Settings.g_instance.userPrefs, Settings.KEY_COMMAND_MAPPING)
                cmdItems = cmSection.items()[:]
                if cmdItems:
                    checkUserKeyBinding = AccountSettings.__checkUserKeyBinding
                    hasKeyG, hasCmdVoice, bindedG = checkUserKeyBinding(b'KEY_G', b'CMD_VOICECHAT_ENABLE', cmdItems)
                    hasKeyH, hasCmdHorn, bindedH = checkUserKeyBinding(b'KEY_H', b'CMD_USE_HORN', cmdItems)
                    if hasCmdHorn:
                        cmSection.deleteSection(b'CMD_USE_HORN')
                    isKeyGDefault = not hasKeyG or bindedG
                    keyForCmdTraject = b'KEY_G' if isKeyGDefault else b'KEY_NONE'
                    getSection(cmSection, b'CMD_CM_TRAJECTORY_VIEW').writeString(b'fireKey', keyForCmdTraject)
                    if not hasCmdVoice or bindedG:
                        isKeyHDefault = not hasKeyH or bindedH
                        keyForCmdVoice = b'KEY_H' if isKeyHDefault else b'KEY_NONE'
                        getSection(cmSection, b'CMD_VOICECHAT_ENABLE').writeString(b'fireKey', keyForCmdVoice)
                    CommandMapping.g_instance.restoreUserConfig()
            if currVersion < 29:
                for key, section in _filterAccountSection(ads):
                    filtersSection = AccountSettings._readSection(section, KEY_FILTERS)
                    if b'searchNameVehicle' in filtersSection.keys():
                        searchName = _unpack(filtersSection[b'searchNameVehicle'].asString)
                        filtersSection.write(CAROUSEL_FILTER_CLIENT_1, _pack({b'searchNameVehicle': searchName}))
                        filtersSection.deleteSection(b'searchNameVehicle')

            if currVersion < 30:
                for key, section in _filterAccountSection(ads):
                    accFilters = AccountSettings._readSection(section, KEY_FILTERS)
                    for filterName, filterPickle in accFilters.items():
                        if filterName in (b'inventory_vehicle', b'shop_current', b'inventory_current', b'shop_tradeInVehicle', b'shop_restoreVehicle'):
                            defaults = DEFAULT_VALUES[KEY_FILTERS][filterName]
                            accFilters.write(filterName, base64.b64encode(pickle.dumps(defaults)))

            if currVersion < 32:
                for _, section in _filterAccountSection(ads):
                    accSettings = AccountSettings._readSection(section, KEY_SETTINGS)
                    accSettings.deleteSection(NEW_SETTINGS_COUNTER)

            if currVersion < 32:
                for _, section in _filterAccountSection(ads):
                    accSettings = AccountSettings._readSection(section, KEY_SETTINGS)
                    accSettings.deleteSection(SHOW_CRYSTAL_HEADER_BAND)

            if currVersion < 33:
                for _, section in _filterAccountSection(ads):
                    accSettings = AccountSettings._readSection(section, KEY_SETTINGS)
                    if QUESTS in accSettings.keys():
                        quests = _unpack(accSettings[QUESTS].asString)
                        if b'personalMissions' in quests:
                            newVersion = quests.pop(b'personalMissions')
                            newVersion[b'operationsVisited'] = newVersion.pop(b'tilesVisited')
                            accSettings.write(QUESTS, _pack(quests))

            if currVersion < 34:
                import SoundGroups
                maxVolume = max(SoundGroups.g_instance.getVolume(category) for category in (b'vehicles', b'ambient', b'voice', b'gui', b'effects', b'music', b'music_hangar'))
                SoundGroups.g_instance.setVolume(b'music', maxVolume)
                SoundGroups.g_instance.setVolume(b'music_hangar', maxVolume)
                SoundGroups.g_instance.savePreferences()
            if currVersion < 35:
                AccountSettings.settingsCore.applySetting(b'loginServerSelection', False)
            if currVersion < 36:
                from gui.Scaleform.daapi.view.lobby.header.LobbyHeader import LobbyHeader
                for key, section in _filterAccountSection(ads):
                    accSettings = AccountSettings._readSection(section, KEY_COUNTERS)
                    if NEW_LOBBY_TAB_COUNTER in accSettings.keys():
                        counters = _unpack(accSettings[NEW_LOBBY_TAB_COUNTER].asString)
                        if LobbyHeader.TABS.PERSONAL_MISSIONS in counters:
                            counters[LobbyHeader.TABS.PERSONAL_MISSIONS] = True
                            accSettings.write(NEW_LOBBY_TAB_COUNTER, _pack(counters))

            if currVersion < 37:
                AccountSettings.checkAndResetFireKeyIfInUse(b'CMD_QUEST_PROGRESS_SHOW', b'KEY_N')
                CommandMapping.g_instance.restoreUserConfig()
            if currVersion < 38:
                for key, section in _filterAccountSection(ads):
                    accSettings = AccountSettings._readSection(section, KEY_SETTINGS)
                    if CUSTOMIZATION_SECTION in accSettings.keys():
                        accSettings.write(CUSTOMIZATION_SECTION, _pack({}))
                    obsoleteKeys = (b'questProgressShowsCount', b'trajectoryViewHintCounter', b'siegeModeHintCounter')
                    for sectionName in obsoleteKeys:
                        if sectionName in accSettings.keys():
                            accSettings.deleteSection(sectionName)

            if currVersion < 39:
                for key, section in _filterAccountSection(ads):
                    accSettings = AccountSettings._readSection(section, KEY_SETTINGS)
                    if CUSTOMIZATION_SECTION in accSettings.keys():
                        custSett = _unpack(accSettings[CUSTOMIZATION_SECTION].asString)
                        if CAROUSEL_ARROWS_HINT_SHOWN_FIELD in custSett:
                            del custSett[CAROUSEL_ARROWS_HINT_SHOWN_FIELD]
                        accSettings.write(CUSTOMIZATION_SECTION, _pack(custSett))

            if currVersion < 40:
                for key, section in _filterAccountSection(ads):
                    accSettings = AccountSettings._readSection(section, KEY_SETTINGS)
                    obsoleteKeys = (b'questProgressHint', b'helpScreenHint')
                    for sectionName in obsoleteKeys:
                        if sectionName in accSettings.keys():
                            accSettings.deleteSection(sectionName)

            if currVersion < 41:
                for key, section in _filterAccountSection(ads):
                    keyFlush = (
                     RANKED_AWARDS_BUBBLE_YEAR_REACHED, RANKED_WEB_INFO, RANKED_WEB_INFO_UPDATE)
                    keySettings = AccountSettings._readSection(section, KEY_SETTINGS)
                    for flushName in keyFlush:
                        if flushName in keySettings.keys():
                            keySettings.write(flushName, _pack(None))

                    countersFlush = (
                     RANKED_AWARDS_COUNTER, RANKED_INFO_COUNTER)
                    counterSettings = AccountSettings._readSection(section, KEY_COUNTERS)
                    for flushName in countersFlush:
                        if flushName in counterSettings.keys():
                            counterSettings.write(flushName, _pack(1))

            if currVersion < 42:
                for key, section in _filterAccountSection(ads):
                    accSettings = AccountSettings._readSection(section, KEY_SETTINGS)
                    if PRE_BATTLE_HINT_SECTION in accSettings.keys():
                        preBattleSection = DEFAULT_VALUES[KEY_SETTINGS][PRE_BATTLE_HINT_SECTION].copy()
                        defPre = DEFAULT_VALUES[KEY_SETTINGS][PRE_BATTLE_HINT_SECTION].copy()[IBC_HINT_SECTION]
                        for key1, section1 in accSettings.items()[:]:
                            if key1 == PRE_BATTLE_HINT_SECTION:
                                preBattleSection = _unpack(section1.asString)
                                preBattleSection[IBC_HINT_SECTION] = defPre
                                accSettings.deleteSection(key1)
                                break

                        accSettings.write(b'preBattleHintSection', _pack(preBattleSection))

            if currVersion < 43:
                AccountSettings.checkAndResetFireKeyIfInUse(expectedCommand=b'CMD_CHAT_SHORTCUT_THANKYOU', expectedKey=b'KEY_F3')
                AccountSettings.checkAndResetFireKeyIfInUse(expectedCommand=b'CMD_CHAT_SHORTCUT_CONTEXT_COMMIT', expectedKey=b'KEY_F2')
                AccountSettings.removeOldCommandAndReuseFireKey(oldCommand=b'CMD_CHAT_SHORTCUT_ATTACK_MY_TARGET', newCommand=b'CMD_CHAT_SHORTCUT_CONTEXT_COMMAND')
                CommandMapping.g_instance.restoreUserConfig()
            if currVersion < 44:
                AccountSettings.checkAndResetFireKeyIfInUse(expectedCommand=b'CMD_CHAT_SHORTCUT_AFFIRMATIVE', expectedKey=b'KEY_F5')
                AccountSettings.checkAndResetFireKeyIfInUse(expectedCommand=b'CMD_CHAT_SHORTCUT_NEGATIVE', expectedKey=b'KEY_F6')
                AccountSettings.removeOldCommandAndReuseFireKey(oldCommand=b'CMD_CHAT_SHORTCUT_POSITIVE', newCommand=b'CMD_CHAT_SHORTCUT_AFFIRMATIVE')
                CommandMapping.g_instance.restoreUserConfig()
            if currVersion < 45:
                pass
            if currVersion < 46:
                for key, section in _filterAccountSection(ads):
                    accFilters = AccountSettings._readSection(section, KEY_FILTERS)
                    if GUI_START_BEHAVIOR in accFilters.keys():
                        guiSettings = _unpack(accFilters[GUI_START_BEHAVIOR].asString)
                        obsoleteKeys = (b'lastShownEpicWelcomeScreen', b'isEpicWelcomeViewShowed')
                        for sectionName in obsoleteKeys:
                            if sectionName in guiSettings:
                                del guiSettings[sectionName]

                        accFilters.write(GUI_START_BEHAVIOR, _pack(guiSettings))

            if currVersion < 47:
                for key, section in _filterAccountSection(ads):
                    filtersSection = AccountSettings._readSection(section, KEY_FILTERS)
                    existingSections = set(filtersSection.keys()).intersection((
                     CAROUSEL_FILTER_CLIENT_1, BATTLEPASS_CAROUSEL_FILTER_CLIENT_1, RANKED_CAROUSEL_FILTER_CLIENT_1,
                     MAPBOX_CAROUSEL_FILTER_CLIENT_1, EPICBATTLE_CAROUSEL_FILTER_CLIENT_1,
                     ROYALE_CAROUSEL_FILTER_CLIENT_1, STORAGE_BLUEPRINTS_CAROUSEL_FILTER,
                     STORAGE_VEHICLES_CAROUSEL_FILTER_1))
                    for filterSection in existingSections:
                        savedFilters = _unpack(filtersSection[filterSection].asString)
                        defaults = AccountSettings.getFilterDefault(filterSection)
                        updatedFilters = {key: savedFilters.get(key, defaults[key]) for key in defaults}
                        filtersSection.write(filterSection, _pack(updatedFilters))

            if currVersion < 48:
                pass
            if currVersion < 49:
                for key, section in _filterAccountSection(ads):
                    filtersSection = AccountSettings._readSection(section, KEY_FILTERS)
                    existingSections = set(filtersSection.keys()).intersection((
                     CAROUSEL_FILTER_CLIENT_1,
                     RANKED_CAROUSEL_FILTER_CLIENT_1,
                     ROYALE_CAROUSEL_FILTER_CLIENT_1,
                     EPICBATTLE_CAROUSEL_FILTER_CLIENT_1,
                     EPICBATTLE_CAROUSEL_FILTER_CLIENT_2,
                     MAPBOX_CAROUSEL_FILTER_CLIENT_1,
                     STORAGE_VEHICLES_CAROUSEL_FILTER_1,
                     STORAGE_BLUEPRINTS_CAROUSEL_FILTER))
                    for filterSection in existingSections:
                        savedFilters = _unpack(filtersSection[filterSection].asString)
                        if b'clanRented' in savedFilters:
                            savedFilters[b'clanRented'] = False
                        filtersSection.write(filterSection, _pack(savedFilters))

            if currVersion < 50:
                for key, section in _filterAccountSection(ads):
                    accFilters = AccountSettings._readSection(section, KEY_FILTERS)
                    if GUI_START_BEHAVIOR in accFilters.keys():
                        guiSettings = _unpack(accFilters[GUI_START_BEHAVIOR].asString)
                        obsoleteKeys = (b'techTreeIntroBlueprintsReceived', b'techTreeIntroShowed')
                        for sectionName in obsoleteKeys:
                            if sectionName in guiSettings:
                                del guiSettings[sectionName]

                        accFilters.write(GUI_START_BEHAVIOR, _pack(guiSettings))

            if currVersion < 51:
                for key, section in _filterAccountSection(ads):
                    keyFlush = (
                     RANKED_AWARDS_BUBBLE_YEAR_REACHED, RANKED_CURRENT_AWARDS_BUBBLE_YEAR_REACHED)
                    keySettings = AccountSettings._readSection(section, KEY_SETTINGS)
                    for flushName in keyFlush:
                        if flushName in keySettings.keys():
                            keySettings.write(flushName, _pack(False))

            if currVersion < 52:
                pass
            if currVersion < 53:
                for key, section in _filterAccountSection(ads):
                    keySettings = AccountSettings._readSection(section, KEY_SETTINGS)
                    if LAST_BATTLE_PASS_POINTS_SEEN in keySettings.keys():
                        keySettings.write(LAST_BATTLE_PASS_POINTS_SEEN, _pack({}))
                    if b'isBattlePassExtraStarted' in keySettings.keys():
                        keySettings.write(b'isBattlePassExtraStarted', _pack(False))

            if currVersion < 54:
                for key, section in _filterAccountSection(ads):
                    keySettings = AccountSettings._readSection(section, KEY_SETTINGS)
                    obsoleteKey = b'battleRoyaleHangarBottomPanelViewed'
                    if obsoleteKey in keySettings.keys():
                        keySettings.deleteSection(obsoleteKey)

            if currVersion < 55:
                for key, section in _filterAccountSection(ads):
                    accSettings = AccountSettings._readSection(section, KEY_SETTINGS)
                    if PRE_BATTLE_HINT_SECTION in accSettings.keys():
                        preBattleSection = DEFAULT_VALUES[KEY_SETTINGS][PRE_BATTLE_HINT_SECTION].copy()
                        defPre = preBattleSection[RESERVES_HINT_SECTION].copy()
                        for key1, section1 in accSettings.items()[:]:
                            if key1 == PRE_BATTLE_HINT_SECTION:
                                preBattleSection = _unpack(section1.asString)
                                preBattleSection[RESERVES_HINT_SECTION] = defPre
                                accSettings.deleteSection(key1)
                                break

                        accSettings.write(PRE_BATTLE_HINT_SECTION, _pack(preBattleSection))

            if currVersion < 56:
                for key, section in _filterAccountSection(ads):
                    keySettings = AccountSettings._readSection(section, KEY_SETTINGS)
                    if FUN_RANDOM_HINT_SECTION in keySettings.keys():
                        keySettings.write(FUN_RANDOM_HINT_SECTION, _pack({}))

            if currVersion < 57:
                for key, section in _filterAccountSection(ads):
                    obsoleteKeys = (
                     RESOURCE_WELL_START_SHOWN, RESOURCE_WELL_END_SHOWN)
                    settings = AccountSettings._readSection(section, KEY_NOTIFICATIONS)
                    for sectionName in obsoleteKeys:
                        if sectionName in settings.keys():
                            settings.deleteSection(sectionName)

            if currVersion < 58:
                for key, section in _filterAccountSection(ads):
                    accSessionSettings = AccountSettings._readSection(section, KEY_SESSION_SETTINGS)
                    obsoleteKey = b'seniorityAwardsWindowShown'
                    if obsoleteKey in accSessionSettings.keys():
                        accSessionSettings.deleteSection(obsoleteKey)

            if currVersion < 59:
                for key, section in _filterAccountSection(ads):
                    keySettings = AccountSettings._readSection(section, KEY_SETTINGS)
                    if IS_BATTLE_PASS_COLLECTION_SEEN in keySettings.keys():
                        keySettings.write(IS_BATTLE_PASS_COLLECTION_SEEN, _pack(False))

            if currVersion < 60:
                if Settings.g_instance.userPrefs.has_key(b'loginPage'):
                    Settings.g_instance.userPrefs.deleteSection(b'loginPage')
            if currVersion < 61:
                for key, section in _filterAccountSection(ads):
                    accSessionSettings = AccountSettings._readSection(section, KEY_FILTERS)
                    obsoleteKey = b'awards'
                    if obsoleteKey in accSessionSettings.keys():
                        accSessionSettings.deleteSection(obsoleteKey)

            if currVersion < 62:
                pass
            if currVersion < 63:
                pass
            if currVersion < 64:
                obsoleteKeys = [b'isEntryPointsEnabled', b'isTankRentalEnabled', b'isFreeDirectivesEnabled']
                for _, section in _filterAccountSection(ads):
                    accSettings = AccountSettings._readSection(section, KEY_SETTINGS)
                    if WOT_PLUS in accSettings.keys():
                        wotPlusSettings = _unpack(accSettings[WOT_PLUS].asString)
                        for key in obsoleteKeys:
                            wotPlusSettings.pop(key, None)

                        accSettings.write(WOT_PLUS, _pack(wotPlusSettings))

            if currVersion < 65:
                for key, section in _filterAccountSection(ads):
                    accSessionSettings = AccountSettings._readSection(section, KEY_COUNTERS)
                    obsoleteKey = b'battleMattersSeen'
                    if obsoleteKey in accSessionSettings.keys():
                        accSessionSettings.deleteSection(obsoleteKey)

            if currVersion < 66:
                for key, section in _filterAccountSection(ads):
                    accSettings = AccountSettings._readSection(section, KEY_SETTINGS)
                    bmKey = BattleMatters.BATTLE_MATTERS_SETTINGS
                    if bmKey in accSettings.keys():
                        bmSettings = DEFAULT_VALUES[KEY_SETTINGS][bmKey].copy()
                        bmAccSettings = _unpack(accSettings[bmKey].asString)
                        bmSettings.update(bmAccSettings)
                        accSettings.write(bmKey, _pack(bmSettings))

            if currVersion < 67:
                for key, section in _filterAccountSection(ads):
                    accSettings = AccountSettings._readSection(section, KEY_SETTINGS)
                    if NEW_YEAR in accSettings.keys():
                        accSettings.deleteSection(NEW_YEAR)
                    accUiFlags = AccountSettings._readSection(section, KEY_UI_FLAGS)
                    for uiKey in {NY_DAILY_QUESTS_VISITED, 
                     NY_BONUS_DAILY_QUEST_VISITED, 
                     NY_OLD_COLLECTIONS_BY_YEAR_VISITED, 
                     NY_OLD_REWARDS_BY_YEAR_VISITED, 
                     NY_LAST_SEEN_LEVEL_INFO, 
                     188, 
                     189, 
                     190}.intersection(accUiFlags.keys()):
                        accUiFlags.deleteSection(uiKey)

                    if GUI_LOOT_BOXES in accSettings.keys():
                        lootBoxesSettings = _unpack(accSettings[GUI_LOOT_BOXES].asString)
                        lootBoxesSettings[LOOT_BOXES_INTRO_SHOWN] = False
                        accSettings.write(GUI_LOOT_BOXES, _pack(lootBoxesSettings))

            if currVersion < 68:
                for key, section in _filterAccountSection(ads):
                    keySettings = AccountSettings._readSection(section, KEY_SETTINGS)
                    if b'isBattlePassExtraStarted' in keySettings.keys():
                        extraStarted = _unpack(keySettings[b'isBattlePassExtraStarted'].asString)
                        keySettings.deleteSection(b'isBattlePassExtraStarted')
                        keySettings.write(IS_BATTLE_PASS_MARATHON_STARTED, _pack(extraStarted))

            if currVersion < 69:
                for key, section in _filterAccountSection(ads):
                    keySettings = AccountSettings._readSection(section, KEY_SETTINGS)
                    if SOUND.DETECTION_ALERT_SOUND in keySettings.keys():
                        keySettings.write(SOUND.DETECTION_ALERT_SOUND, _pack(b'lightbulb'))

            if currVersion < 70:
                for key, section in _filterAccountSection(ads):
                    keySettings = AccountSettings._readSection(section, KEY_SETTINGS)
                    if SHOWN_WOT_PLUS_INTRO in keySettings.keys():
                        keySettings.write(SHOWN_WOT_PLUS_INTRO, _pack(True))

            if currVersion < 71:
                for key, section in _filterAccountSection(ads):
                    keySettings = AccountSettings._readSection(section, KEY_SETTINGS)
                    if WOT_PLUS in keySettings.keys():
                        keySettings.deleteSection(WOT_PLUS)

            if currVersion < 72:
                for key, section in _filterAccountSection(ads):
                    accSettings = AccountSettings._readSection(section, KEY_SETTINGS)
                    if GUI_LOOT_BOXES in accSettings.keys():
                        lootBoxesSettings = _unpack(accSettings[GUI_LOOT_BOXES].asString)
                        lootBoxesSettings[LOOT_BOXES_INTRO_SHOWN] = False
                        accSettings.write(GUI_LOOT_BOXES, _pack(lootBoxesSettings))

            if currVersion < 73:
                for key, section in _filterAccountSection(ads):
                    keySettings = AccountSettings._readSection(section, KEY_UI_FLAGS)
                    if COMP7_UI_SECTION in keySettings.keys():
                        comp7UiSection = _unpack(keySettings[COMP7_UI_SECTION].asString)
                        comp7UiSection[COMP7_WEEKLY_QUESTS_PAGE_TOKENS_COUNT] = 0
                        keySettings.write(COMP7_UI_SECTION, _pack(comp7UiSection))

            if currVersion < 74:
                for key, section in _filterAccountSection(ads):
                    accSettings = AccountSettings._readSection(section, KEY_SETTINGS)
                    if GUI_LOOT_BOXES in accSettings.keys():
                        lootBoxesSettings = _unpack(accSettings[GUI_LOOT_BOXES].asString)
                        lootBoxesSettings[LOOT_BOXES_INTRO_SHOWN] = set()
                        accSettings.write(GUI_LOOT_BOXES, _pack(lootBoxesSettings))

            if currVersion < 75:
                for _, section in _filterAccountSection(ads):
                    accSettings = AccountSettings._readSection(section, KEY_SETTINGS)
                    if QUESTS in accSettings.keys():
                        quests = _unpack(accSettings[QUESTS].asString)
                        if DAILY_QUESTS in quests:
                            quests[DAILY_QUESTS] = {b'lastVisitedDQTabIdx': None, b'premMissionsTabDiscovered': False, 
                               DAILY_QUESTS_INTRO_SEEN: False}
                        if b'visited' in quests:
                            newVisited = [q for q in quests[b'visited'] if not q.startswith(b'dq:')]
                            quests[b'visited'] = newVisited
                        if b'naVisited' in quests:
                            newNaVisited = [q for q in quests[b'naVisited'] if not q.startswith(b'dq:')]
                            quests[b'naVisited'] = newNaVisited
                        accSettings.write(QUESTS, _pack(quests))

            if currVersion < 76:
                for key, section in _filterAccountSection(ads):
                    accSettings = AccountSettings._readSection(section, KEY_SETTINGS)
                    if GUI_LOOT_BOXES in accSettings.keys():
                        lootBoxesSettings = _unpack(accSettings[GUI_LOOT_BOXES].asString)
                        lootBoxesSettings[LOOT_BOXES_SHORT_STAT_STATE] = 0
                        lootBoxesSettings[LOOT_BOXES_STATS_HINT_STATE] = 0
                        lootBoxesSettings[LOOT_BOXES_STATS_NO_BOX_HINT_STATE] = 0
                        accSettings.write(GUI_LOOT_BOXES, _pack(lootBoxesSettings))

            if currVersion < 77:
                if currVersion > 0:
                    from gui.Scaleform.daapi.view.lobby.header.LobbyHeader import LobbyHeader
                    for key, section in _filterAccountSection(ads):
                        accSettings = AccountSettings._readSection(section, KEY_COUNTERS)
                        counters = {}
                        if NEW_LOBBY_TAB_COUNTER in accSettings.keys():
                            counters = _unpack(accSettings[NEW_LOBBY_TAB_COUNTER].asString)
                        counters[LobbyHeader.TABS.TOURNAMENTS] = False
                        accSettings.write(NEW_LOBBY_TAB_COUNTER, _pack(counters))

            if currVersion < 78:
                for key, section in _filterAccountSection(ads):
                    accSettings = AccountSettings._readSection(section, KEY_SETTINGS)
                    customizationKey = CustomizationFilter.CUSTOMIZATION_FILTER
                    if customizationKey in accSettings.keys():
                        accSettings.deleteSection(customizationKey)

            if currVersion < 79:
                AccountSettings.__addDeferredLogPlayerSettingsInitAction(ads)
            if currVersion < 80:
                mtBirthdayKey = b'MT_BIRTHDAY'
                for key, section in _filterAccountSection(ads):
                    accSettings = AccountSettings._readSection(section, KEY_SETTINGS)
                    if mtBirthdayKey in accSettings.keys():
                        mtBirthdaySettings = _unpack(accSettings[mtBirthdayKey].asString)
                        mtBirthdaySettings[b'BirthdayWelcomeNotification'] = False
                        mtBirthdaySettings[b'GIFT_RECEIVED'] = False
                        mtBirthdaySettings[b'BONUS_RECEIVED'] = False
                        accSettings.write(mtBirthdayKey, _pack(mtBirthdaySettings))

            ads.writeInt(b'version', AccountSettings.version)
        return

    @staticmethod
    def getFilterDefault(name):
        return DEFAULT_VALUES[KEY_FILTERS].get(name, None)

    @staticmethod
    def invalidateNewSettingsCounter():
        ads = AccountSettings._readSection(Settings.g_instance.userPrefs, Settings.KEY_ACCOUNT_SETTINGS)
        currentDefaults = AccountSettings.getSettingsDefault(NEW_SETTINGS_COUNTER)
        filtered = _filterAccountSection(ads)
        for _, section in filtered:
            accSettings = AccountSettings._readSection(section, KEY_SETTINGS)
            if NEW_SETTINGS_COUNTER in accSettings.keys():
                savedNewSettingsCounters = _unpack(accSettings[NEW_SETTINGS_COUNTER].asString)
                if savedNewSettingsCounters is not None:
                    newSettingsCounters = AccountSettings.updateNewSettingsCounter(currentDefaults, savedNewSettingsCounters)
                    accSettings.write(NEW_SETTINGS_COUNTER, _pack(newSettingsCounters))

        return

    @staticmethod
    def checkAndResetFireKeyIfInUse(expectedCommand, expectedKey):
        cmSection = AccountSettings._readSection(Settings.g_instance.userPrefs, Settings.KEY_COMMAND_MAPPING)
        for command, section in cmSection.items()[:]:
            fireKey = AccountSettings._readSection(section, b'fireKey').asString
            if fireKey == expectedKey:
                if command == expectedCommand:
                    break
                else:
                    cmSection.deleteSection(expectedCommand)
                    newSection = cmSection.createSection(expectedCommand)
                    newSection.writeString(b'fireKey', b'KEY_NONE')
                    break

        return

    @staticmethod
    def removeOldCommandAndReuseFireKey(oldCommand, newCommand):
        cmSection = AccountSettings._readSection(Settings.g_instance.userPrefs, Settings.KEY_COMMAND_MAPPING)
        for command, section in cmSection.items()[:]:
            if command == oldCommand:
                fireKey = AccountSettings._readSection(section, b'fireKey').asString
                cmSection.deleteSection(newCommand)
                newSection = cmSection.createSection(newCommand)
                newSection.writeString(b'fireKey', fireKey)
                cmSection.deleteSection(command)
                break

        return

    @staticmethod
    def getFilterDefaults(names):
        result = {}
        for name in names:
            result.update(AccountSettings.getFilterDefault(name))

        return result

    @staticmethod
    def getFilter(name):
        return AccountSettings._getValue(name, KEY_FILTERS)

    @staticmethod
    def setFilter(name, value):
        AccountSettings._setValue(name, value, KEY_FILTERS)
        return

    @staticmethod
    def getSettingsDefault(name):
        return DEFAULT_VALUES[KEY_SETTINGS].get(name, None)

    @classmethod
    def getSettings(cls, name):
        return cls._getValue(name, KEY_SETTINGS)

    @classmethod
    def setSettings(cls, name, value):
        cls._setValue(name, value, KEY_SETTINGS)
        return

    @staticmethod
    def getManualData(name):
        return AccountSettings._getValue(name, KEY_MANUAL)

    @staticmethod
    def setManualData(name, value):
        AccountSettings._setValue(name, value, KEY_MANUAL)
        return

    @staticmethod
    def setManualUnreadPages(content):
        ver = getClientVersion()
        return AccountSettings.setManualData(MANUAL_NEW_CONTENT, {ver: content})

    @staticmethod
    def getManualUnreadPages():
        ver = getClientVersion()
        data = AccountSettings.getManualData(MANUAL_NEW_CONTENT)
        return data.get(ver, None)

    @staticmethod
    def getFavorites(name):
        return AccountSettings._getValue(name, KEY_FAVORITES)

    @staticmethod
    def setFavorites(name, value):
        AccountSettings._setValue(name, value, KEY_FAVORITES)
        return

    @staticmethod
    def getCounters(name):
        return AccountSettings._getValue(name, KEY_COUNTERS)

    @staticmethod
    def setCounters(name, value):
        AccountSettings._setValue(name, value, KEY_COUNTERS)
        return

    @staticmethod
    def getNotifications(name):
        return AccountSettings._getValue(name, KEY_NOTIFICATIONS)

    @staticmethod
    def setNotifications(name, value):
        AccountSettings._setValue(name, value, KEY_NOTIFICATIONS)
        return

    @staticmethod
    def getNotificationsDefault(name):
        return DEFAULT_VALUES[KEY_NOTIFICATIONS].get(name)

    @staticmethod
    def getSessionSettings(name):
        return AccountSettings.__getSessionSettings(name)

    @staticmethod
    def setSessionSettings(name, value):
        AccountSettings.__setSessionSettings(name, value)
        return

    @staticmethod
    def getSessionSettingsDefault(name):
        return DEFAULT_VALUES[KEY_SESSION_SETTINGS].get(name, None)

    @staticmethod
    def updateNewSettingsCounter(defaultDict, savedDict):
        finalDict = {}
        _recursiveStep(defaultDict, savedDict, finalDict)
        return finalDict

    @classmethod
    def getUIFlag(cls, name):
        return cls._getValue(name, KEY_UI_FLAGS, force=True)

    @classmethod
    def setUIFlag(cls, name, value):
        return cls._setValue(name, value, KEY_UI_FLAGS, force=True)

    @classmethod
    def getBattleMattersSetting(cls, name):
        return cls.getSettings(BattleMatters.BATTLE_MATTERS_SETTINGS).get(name)

    @classmethod
    def setBattleMattersSetting(cls, name, value):
        bmSection = cls.getSettings(BattleMatters.BATTLE_MATTERS_SETTINGS)
        if name in bmSection:
            bmSection[name] = value
            cls._setValue(BattleMatters.BATTLE_MATTERS_SETTINGS, bmSection, KEY_SETTINGS)
        else:
            _logger.error(b"Cann't set value in %s section for %s.", BattleMatters.BATTLE_MATTERS_SETTINGS, name)
        return

    @staticmethod
    def getArmoryYard(name):
        return AccountSettings._getValue(name, ArmoryYard.ARMORY_YARD_SETTINGS, True)

    @staticmethod
    def setArmoryYard(name, value):
        AccountSettings._setValue(name, value, ArmoryYard.ARMORY_YARD_SETTINGS, True)
        return

    @staticmethod
    def clearArmoryYard():
        fds = AccountSettings._readSection(AccountSettings._readUserSection(), ArmoryYard.ARMORY_YARD_SETTINGS)
        for name in fds.keys():
            fds.deleteSection(name)

        return

    @staticmethod
    def getEarlyAccess(name):
        return AccountSettings._getValue(name, EarlyAccess.EARLY_ACCESS_SETTINGS, True)

    @staticmethod
    def setEarlyAccess(name, value):
        AccountSettings._setValue(name, value, EarlyAccess.EARLY_ACCESS_SETTINGS, True)
        return

    @staticmethod
    def clearEarlyAccess():
        fds = AccountSettings._readSection(AccountSettings._readUserSection(), EarlyAccess.EARLY_ACCESS_SETTINGS)
        for name in fds.keys():
            fds.deleteSection(name)

        return

    @staticmethod
    def getPersonalMissions(name):
        return AccountSettings._getValue(name, PersonalMissions.PERSONAL_MISSIONS_SETTINGS, True)

    @staticmethod
    def setPersonalMissions(name, value):
        AccountSettings._setValue(name, value, PersonalMissions.PERSONAL_MISSIONS_SETTINGS, True)
        return

    @staticmethod
    def getFunRandom(name):
        return AccountSettings._getValue(name, FunRandomMaps.FUN_RANDOM_MAPS_SETTINGS, True)

    @staticmethod
    def setFunRandom(name, value):
        AccountSettings._setValue(name, value, FunRandomMaps.FUN_RANDOM_MAPS_SETTINGS, True)
        return

    @staticmethod
    def clearPersonalMissions():
        fds = AccountSettings._readSection(AccountSettings._readUserSection(), PersonalMissions.PERSONAL_MISSIONS_SETTINGS)
        for name in fds.keys():
            fds.deleteSection(name)

        return

    @staticmethod
    def getParagons(name):
        return AccountSettings._getValue(name, Paragons.PARAGONS_SETTINGS, True)

    @staticmethod
    def setParagons(name, value):
        AccountSettings._setValue(name, value, Paragons.PARAGONS_SETTINGS, True)
        return

    @staticmethod
    def clearParagons():
        fds = AccountSettings._readSection(AccountSettings._readUserSection(), Paragons.PARAGONS_SETTINGS)
        for name in fds.keys():
            fds.deleteSection(name)

        return

    @staticmethod
    def delUnusedSetting(settingSection, name):
        if name in DEFAULT_VALUES.get(settingSection, []):
            raise SoftException((b'The setting "{}" is still being used in DEFAULT_VALUES["{}"]').format(name, settingSection))
        settings = AccountSettings._readSection(AccountSettings._readUserSection(), settingSection)
        if name in settings.keys():
            settings.deleteSection(name)
            return True
        if settingSection not in DEFAULT_VALUES:
            raise SoftException((b'"{}" does not exist in DEFAULT_VALUES').format(settingSection))
        return False

    @staticmethod
    def getBlackMarket(name):
        return AccountSettings._getValue(name, BlackMarket.BLACK_MARKET_SETTINGS)

    @staticmethod
    def setBlackMarket(name, value):
        AccountSettings._setValue(name, value, BlackMarket.BLACK_MARKET_SETTINGS)
        return

    @staticmethod
    def getEpic(name):
        return AccountSettings._getValue(name, Epic.EPIC_SETTINGS, True)

    @staticmethod
    def setEpic(name, value):
        AccountSettings._setValue(name, value, Epic.EPIC_SETTINGS, True)
        return

    @staticmethod
    def _getValue(name, setting, force=False):
        fds = AccountSettings._readSection(AccountSettings._readUserSection(), setting)
        try:
            if fds.has_key(name):
                return pickle.loads(base64.b64decode(fds.readString(name)))
        except Exception:
            if constants.IS_DEVELOPMENT:
                LOG_CURRENT_EXCEPTION()

        if name in DEFAULT_VALUES[setting]:
            return copy.deepcopy(DEFAULT_VALUES[setting][name])
        else:
            return

    @staticmethod
    def _setValue(name, value, setting, force=False):
        if name not in DEFAULT_VALUES[setting] and not force:
            raise SoftException((b'Default value "{}" is not found in "{}"').format(name, type))
        if AccountSettings._getValue(name, setting, force) != value:
            fds = AccountSettings._readSection(AccountSettings._readUserSection(), setting)
            if name in DEFAULT_VALUES[setting] and DEFAULT_VALUES[setting][name] == value:
                fds.deleteSection(name)
            else:
                fds.write(name, base64.b64encode(pickle.dumps(value)))
            AccountSettings.onSettingsChanging(name, value)
        return

    @staticmethod
    def __getSessionSettings(name):
        if name in DEFAULT_VALUES[KEY_SESSION_SETTINGS]:
            sessionSettings = AccountSettings.__getUserSessionSettings()
            if isinstance(sessionSettings, dict) and name in sessionSettings.keys():
                return copy.deepcopy(sessionSettings.get(name))
            return copy.deepcopy(DEFAULT_VALUES[KEY_SESSION_SETTINGS][name])
        else:
            return

    @staticmethod
    def __setSessionSettings(name, value):
        if name not in DEFAULT_VALUES[KEY_SESSION_SETTINGS]:
            raise SoftException((b'Default value "{}" is not found in "{}"').format(name, type))
        if AccountSettings.__getSessionSettings(name) != value:
            sessionSettings = AccountSettings.__getUserSessionSettings()
            if isinstance(sessionSettings, dict):
                if DEFAULT_VALUES[KEY_SESSION_SETTINGS][name] != value:
                    sessionSettings.update({name: value})
                elif name in sessionSettings.keys():
                    sessionSettings.pop(name)
        return

    @staticmethod
    def __getUserSessionSettings():
        userLogin = AccountSettings.__getPlayerName()
        if AccountSettings.__sessionSettings[b'section'] is None:
            AccountSettings.__sessionSettings[b'section'] = dict()
        if AccountSettings.__sessionSettings[b'login'] != userLogin and userLogin != b'':
            AccountSettings.__sessionSettings[b'section'] = dict()
            AccountSettings.__sessionSettings[b'login'] = userLogin
        return AccountSettings.__sessionSettings[b'section']

    @staticmethod
    def __checkUserKeyBinding(key=None, command=None, commandSectionItems=None):
        if commandSectionItems is None:
            commandSection = AccountSettings._readSection(Settings.g_instance.userPrefs, Settings.KEY_COMMAND_MAPPING)
            commandSectionItems = commandSection.items()[:]
        hasKey, hasCommand, binded = False, False, False
        for cmd, section in commandSectionItems:
            fireKey = AccountSettings._readSection(section, b'fireKey').asString
            if key is not None and fireKey == key:
                if cmd == command:
                    return (True, True, True)
                hasKey = True
            if command is not None and cmd == command:
                hasCommand = True

        return (
         hasKey, hasCommand, binded)

    @classmethod
    def __getPlayerName(cls):
        playerName = getattr(BigWorld.player(), b'name', b'')
        if not playerName:
            return Settings.g_instance.userPrefs[Settings.KEY_LOGIN_INFO].readString(b'user', playerName)
        return playerName

    @staticmethod
    def __addDeferredLogPlayerSettingsInitAction(accountsSettings):
        for _, section in _filterAccountSection(accountsSettings):
            accSettings = AccountSettings._readSection(section, KEY_SETTINGS)
            actions = deepcopy(AccountSettings.getSettingsDefault(DEFERRED_LOG_PLAYER_SETTINGS_ACTIONS))
            actions.add(SettingsLogActions.SETTINGS_INITED)
            accSettings.write(DEFERRED_LOG_PLAYER_SETTINGS_ACTIONS, _pack(actions))

        return
