import base64, cPickle as pickle, copy, logging, typing
from collections import namedtuple
from copy import deepcopy
import BigWorld, CommandMapping, Event, Keys, Settings, WWISE, constants, nations
from account_helpers import gameplay_ctx
from account_helpers.settings_core.settings_constants import AIM, BATTLE_EVENTS, CONTOUR, GAME, SOUND, ArmorFlashlight, BattleCommStorageKeys, GuiSettingsBehavior, PersonalMission3, ScorePanelStorageKeys, SPGAim, SITUATIONAL_PERKS, ArmorInspector
from aih_constants import CTRL_MODE_NAME
from constants import MAX_VEHICLE_LEVEL, VEHICLE_CLASSES
from debug_utils import LOG_CURRENT_EXCEPTION
from gui.Scaleform.genConsts.MISSIONS_CONSTANTS import MISSIONS_CONSTANTS
from gui.Scaleform.genConsts.PROFILE_CONSTANTS import PROFILE_CONSTANTS
from gui.Scaleform.genConsts.STORE_CONSTANTS import STORE_CONSTANTS
from gui.collection.collections_constants import COLLECTION_RENEW_SEEN, COLLECTION_START_SEEN, COLLECTIONS_UPDATED_ENTRY_SEEN
from gui.integrated_auction.constants import AUCTION_FINISH_STAGE_SEEN, AUCTION_STAGE_START_SEEN
from gui.prb_control.settings import SELECTOR_BATTLE_TYPES
from helpers import dependency, getClientVersion
from items.components.crew_books_constants import CREW_BOOK_RARITY
from skeletons.account_helpers.settings_core import ISettingsCore
from soft_exception import SoftException
if typing.TYPE_CHECKING:
    from ResMgr import DataSection
    from typing import List, Optional, Iterable
_logger = logging.getLogger(__name__)
KEY_FILTERS = b'filters'
KEY_SESSION_SETTINGS = b'session_settings'
KEY_SETTINGS = b'settings'
KEY_FAVORITES = b'favorites'
KEY_COUNTERS = b'counters'
KEY_NOTIFICATIONS = b'notifications'
KEY_UI_FLAGS = b'ui_flags'
KEY_MANUAL = b'manual'
KEY_BATTLE_HINTS = b'battle_hints'
KEY_NEWBIE_HINTS = b'newbie_hints'
CAROUSEL_FILTER_1 = b'CAROUSEL_FILTER_1'
CAROUSEL_FILTER_2 = b'CAROUSEL_FILTER_2'
CAROUSEL_FILTER_3 = b'CAROUSEL_FILTER_3'
CAROUSEL_FILTER_CLIENT_1 = b'CAROUSEL_FILTER_CLIENT_1'
MISSION_SELECTOR_FILTER = b'MISSION_SELECTOR_FILTER'
PM_SELECTOR_FILTER = b'PM_SELECTOR_FILTER'
RANKED_CAROUSEL_FILTER_1 = b'RANKED_CAROUSEL_FILTER_1'
RANKED_CAROUSEL_FILTER_2 = b'RANKED_CAROUSEL_FILTER_2'
RANKED_CAROUSEL_FILTER_3 = b'RANKED_CAROUSEL_FILTER_3'
RANKED_CAROUSEL_FILTER_CLIENT_1 = b'RANKED_CAROUSEL_FILTER_CLIENT_1'
EPICBATTLE_CAROUSEL_FILTER_1 = b'EPICBATTLE_CAROUSEL_FILTER_1'
EPICBATTLE_CAROUSEL_FILTER_2 = b'EPICBATTLE_CAROUSEL_FILTER_2'
EPICBATTLE_CAROUSEL_FILTER_3 = b'EPICBATTLE_CAROUSEL_FILTER_3'
EPICBATTLE_CAROUSEL_FILTER_CLIENT_1 = b'EPICBATTLE_CAROUSEL_FILTER_CLIENT_1'
EPICBATTLE_CAROUSEL_FILTER_CLIENT_2 = b'EPICBATTLE_CAROUSEL_FILTER_CLIENT_2'
STORAGE_VEHICLES_CAROUSEL_FILTER_1 = b'STORAGE_CAROUSEL_FILTER_1'
STORAGE_BLUEPRINTS_CAROUSEL_FILTER = b'STORAGE_BLUEPRINTS_CAROUSEL_FILTER'
BATTLEPASS_CAROUSEL_FILTER_1 = b'BATTLEPASS_CAROUSEL_FILTER_1'
BATTLEPASS_CAROUSEL_FILTER_CLIENT_1 = b'BATTLEPASS_CAROUSEL_FILTER_CLIENT_1'
SELECT_VEHICLES_CAROUSEL_FILTER_1 = b'SELECT_VEHICLES_CAROUSEL_FILTER_1'
ROYALE_CAROUSEL_FILTER_1 = b'ROYALE_CAROUSEL_FILTER_1'
ROYALE_CAROUSEL_FILTER_2 = b'ROYALE_CAROUSEL_FILTER_2'
ROYALE_CAROUSEL_FILTER_CLIENT_1 = b'ROYALE_CAROUSEL_FILTER_CLIENT_1'
ROYALE_INTRO_VIDEO_SHOWN = b'ROYALE_INTRO_VIDEO_SHOWN'
ROYALE_INTRO_VIDEO_SHOWN_FOR_SEASON = b'ROYALE_INTRO_VIDEO_SHOWN_FOR_SEASON'
ROYALE_SQUAD_TIP_SHOWN_FOR_SEASON = b'ROYALE_SQUAD_TIP_SHOWN_FOR_SEASON'
MAPBOX_CAROUSEL_FILTER_1 = b'MAPBOX_CAROUSEL_FILTER_1'
MAPBOX_CAROUSEL_FILTER_2 = b'MAPBOX_CAROUSEL_FILTER_2'
MAPBOX_CAROUSEL_FILTER_3 = b'MAPBOX_CAROUSEL_FILTER_3'
MAPBOX_CAROUSEL_FILTER_CLIENT_1 = b'MAPBOX_CAROUSEL_FILTER_CLIENT_1'
FUN_RANDOM_CAROUSEL_FILTER_1 = b'FUN_RANDOM_CAROUSEL_FILTER_1'
FUN_RANDOM_CAROUSEL_FILTER_2 = b'FUN_RANDOM_CAROUSEL_FILTER_2'
FUN_RANDOM_CAROUSEL_FILTER_3 = b'FUN_RANDOM_CAROUSEL_FILTER_3'
FUN_RANDOM_CAROUSEL_FILTER_CLIENT_1 = b'FUN_RANDOM_CAROUSEL_FILTER_CLIENT_1'
COMP7_CAROUSEL_FILTER_1 = b'COMP7_CAROUSEL_FILTER_1'
COMP7_CAROUSEL_FILTER_2 = b'COMP7_CAROUSEL_FILTER_2'
COMP7_CAROUSEL_FILTER_3 = b'COMP7_CAROUSEL_FILTER_3'
COMP7_CAROUSEL_FILTER_CLIENT_1 = b'COMP7_CAROUSEL_FILTER_CLIENT_1'
COMP7_PREBATTLE_CAROUSEL_ROW_VALUE = b'comp7PrebattleCarouselRowValue'
COMP7_IS_VOIP_IN_BATTLE_ACTIVATED = b'comp7IsVoipInBattleActivated'
COMP7_ENTITLEMENTS = b'comp7Entitlements'
COMP7_ENTITLEMENTS_TIMESTAMP = b'timestamp'
COMP7_ENTITLEMENTS_BALANCE = b'balance'
COMP7_LIGHT_CAROUSEL_FILTER_1 = b'COMP7_LIGHT_CAROUSEL_FILTER_1'
COMP7_LIGHT_CAROUSEL_FILTER_2 = b'COMP7_LIGHT_CAROUSEL_FILTER_2'
COMP7_LIGHT_CAROUSEL_FILTER_3 = b'COMP7_LIGHT_CAROUSEL_FILTER_3'
COMP7_LIGHT_CAROUSEL_FILTER_CLIENT_1 = b'COMP7_LIGHT_CAROUSEL_FILTER_CLIENT_1'
ORDERS_FILTER = b'ORDERS_FILTER'
CURRENT_VEHICLE = b'current'
ROYALE_VEHICLE = b'ROYALE_VEHICLE'
LOBBY_MENU_MANUAL_TRIGGER_SHOWN = b'lobby_menu_manual_trigger_shown'
MANUAL_NEW_CONTENT = b'manual_new_content'
GUI_START_BEHAVIOR = b'GUI_START_BEHAVIOR'
EULA_VERSION = b'EULA_VERSION'
FORT_MEMBER_TUTORIAL = b'FORT_MEMBER_TUTORIAL'
IGR_PROMO = b'IGR_PROMO'
PROMO = b'PROMO'
CONTACTS = b'CONTACTS'
FALLOUT_VEHICLES = b'FALLOUT_VEHICLES'
BOOSTERS_FILTER = b'boostersFilter'
LAST_PROMO_PATCH_VERSION = b'lastPromoPatchVersion'
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
RECRUITS_NOTIFICATIONS = b'recruitsNotifications'
SPEAKERS_DEVICE = b'speakersDevice'
SESSION_STATS_PREV_BATTLE_COUNT = b'sessionStatsPrevBattleCnt'
UNIT_FILTER = b'UNIT_FILTER'
BLUEPRINTS_CONVERT_SALE_STARTED_SEEN = b'bcsStartedSeen'
IS_SHOP_VISITED = b'isShopVisited'
LAST_SHOP_ACTION_COUNTER_MODIFICATION = b'lastShopActionCounterModification'
OVERRIDEN_HEADER_COUNTER_ACTION_ALIASES = b'overridenHeaderCounterActionAliases'
LIVE_OPS_WEB_EVENTS_COUNTERS = b'liveOpsWebEventsCounters'
LIVE_OPS_WEB_EVENTS_UI_FLAGS = b'liveOpsWebEventsUIFlags'
COMP7_BOND_EQUIPMENT_REMINDER_SHOWN_TIMESTAMP = b'comp7BondEquipmentReminderShown'
COMP7_LAST_SEASON_WITH_SEEN_REWARD = b'comp7LastSeasonWithSeenReward'
COMP7_LAST_MASKOT_WITH_SEEN_REWARD = b'comp7LastMaskotWithSeenReward'
VEHICLE_CAROUSEL_COUNTERS_SEEN = b'vehicleCarouselCountersSeen'
SELECT_VEHICLES_PLAYLIST = b'selectVehiclesPlaylist'
SELECT_VEHICLES_IS_ALL_VEHICLES = b'selectVehiclesIsAllVehicles'
STORE_TAB = b'store_tab'
STATS_REGULAR_SORTING = b'statsSorting'
STATS_SORTIE_SORTING = b'statsSortingSortie'
STATS_COMP7_SORTING = b'statsSortingComp7'
STATS_COMP7_LIGHT_SORTING = b'statsSortingComp7Light'
STATS_COMP7_SPECIAL_SORTING = b'statsSortingComp7Special'
STATS_FUN_RANDOM_SORTING = b'statsSortingFunRandom'
MISSIONS_PAGE = b'missions_page'
DEFAULT_VEHICLE_TYPES_FILTER = [
 False] * len(VEHICLE_CLASSES)
DEFAULT_LEVELS_FILTERS = [False] * MAX_VEHICLE_LEVEL
SHOW_OPT_DEVICE_HINT = b'showOptDeviceHint'
SHOW_OPT_DEVICE_HINT_TROPHY = b'showOptDeviceHintTrophy'
SHOW_OPT_MODERNIZED_DEVICE_HINT = b'showOptModernizedDeviceHint'
LAST_BADGES_VISIT = b'lastBadgesVisit'
LAST_SELECTED_SUFFIX_BADGE_ID = b'lastSelectedSuffixBadgeID'
ENABLE_RANKED_ANIMATIONS = b'enableRankedAnimations'
COLOR_SETTINGS_TAB_IDX = b'colorSettingsTabIdx'
COLOR_SETTINGS_SHOWS_COUNT = b'colorSettingsShowsCount'
APPLIED_COLOR_SETTINGS = b'appliedColorSettings'
SELECTED_QUEST_IN_REPLAY = b'SELECTED_QUEST_IN_REPLAY'
LAST_SELECTED_PM_BRANCH = b'lastSelectedPMBranch'
WHEELED_DEATH_DELAY_COUNT = b'wheeledDeathCounter'
FREE_CAM_USES_COUNT = b'killCamBattlesCount'
LAST_BATTLE_PASS_POINTS_SEEN = b'lastBattlePassPointsSeen'
LAST_BATTLE_PASS_CYCLES_SEEN = b'lastBattlePassCyclesSeen'
IS_BATTLE_PASS_EXTRA_START_NOTIFICATION_SEEN = b'isBattlePassExtraStarted'
IS_BATTLE_PASS_COLLECTION_SEEN = b'isCollectionSeen'
IS_BATTLE_PASS_START_NOTIFICATION_SEEN = b'isBattlePassStarted'
EXTRA_CHAPTERS_VIDEO_SHOWN = b'extraChaptersVideoShown'
BUY_ANIMATIONS_WAS_SHOWN = b'buyAnimationsWasShown'
IS_BATTLE_PASS_START_ANIMATION_SEEN = b'isBattlePassStartAnimationSeen'
LAST_BATTLE_PASS_EXTRA_CHAPTER_SEEN = b'lastBattlePassExtraChapterSeen'
UMG_BATTLE_PASS_EXTRA_CHAPTER_SEEN = b'umgBattlePassExtraChapterSeen'
LAST_BATTLE_PASS_HOLIDAY_CHAPTER_SEEN = b'lastBattlePassHolidayChapterSeen'
BR_UI_SECTION = b'battleRoyale'
BR_PROGRESSION_SEEN_QUESTS = b'battleRoyaleSeenQuests'
BR_PROGRESSION_POINTS_SEEN = b'brProgressionPointsSeen'
CRYSTALS_INFO_SHOWN = b'crystalsInfoShown'
IS_CUSTOMIZATION_INTRO_VIEWED = b'isCustomizationIntroViewed'
NPS_STORAGE = b'nps_storage'
CUSTOMIZATION_STYLE_ITEMS_VISITED = b'CustomizationStyleItemsVisited'
CUSTOMIZATION_TABS_VISITED = b'CustomizationTabsVisited'
OPT_DEVICE_TAB_VISITED = b'optDeviceTabVisited'
ANONYMIZER = GAME.ANONYMIZER
CUSTOMIZATION_SECTION = b'customization'
CAROUSEL_ARROWS_HINT_SHOWN_FIELD = b'isCarouselsArrowsHintShown'
PROJECTION_DECAL_HINT_SHOWN_FIELD = b'isProjectionDecalHintShown'
SESSION_STATS_SECTION = b'sessionStats'
BATTLE_EFFICIENCY_SECTION_EXPANDED_FIELD = b'battleEfficiencySectionExpanded'
SIEGE_HINT_SECTION = b'siegeModeHint'
WHEELED_MODE_HINT_SECTION = b'wheeledModeScreenHint'
TRAJECTORY_VIEW_HINT_SECTION = b'trajectoryViewHint'
TURBO_SHAFT_ENGINE_MODE_HINT_SECTION = b'turboShaftEngineModeHint'
ROCKET_ACCELERATION_MODE_HINT_SECTION = b'rocketAccelerationModeHint'
RECHARGEABLE_NITRO_MODE_HINT_SECTION = b'rechargeableNitroModeHint'
STAGED_JET_BOOSTERS_MODE_HINT_SECTION = b'stagedJetBoostersModeHint'
TARGET_DESIGNATOR_MODE_HINT_SECTION = b'targetDesignatorModeHint'
DYN_SQUAD_HINT_SECTION = b'dynSquadHint'
PILLBOX_HINT_SECTION = b'pillboxModeHint'
WHEELED_DASH_MODE_HINT_SECTION = b'wheeledDashModeHint'
RADAR_HINT_SECTION = b'radarHint'
PRE_BATTLE_HINT_SECTION = b'preBattleHintSection'
PRE_BATTLE_ROLE_HINT_SECTION = b'preBattleRoleHintSection'
FUN_RANDOM_HINT_SECTION = b'funRandomHintSection'
MAPBOX_HINT_SECTION = b'mapboxHintSection'
QUEST_PROGRESS_HINT_SECTION = b'questProgressHint'
HELP_SCREEN_HINT_SECTION = b'helpScreenHint'
IBC_HINT_SECTION = b'battleCommunicationHint'
RESERVES_HINT_SECTION = b'reservesHintSection'
TWIN_GUN_HINT_SECTION = b'twinGunHintSection'
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
IS_COMP7_BONS_BANNER_VISITED = b'isComp7BonsBannerVisited'
LAST_SHOP_TAB_COUNTER = b'lastShopTabCounter'
CUSTOM_SHOP_SETTINGS = b'customShopSettings'
QUESTS = b'quests'
QUEST_DELTAS = b'questDeltas'
QUEST_DELTAS_COMPLETION = b'questCompletion'
QUEST_DELTAS_PROGRESS = b'questProgress'
QUEST_DELTAS_TOKENS_PROGRESS = b'tokensProgress'
TOP_OF_TREE_CONFIG = b'topOfTree'
DOG_TAGS = b'dogTags'
DOG_TAGS_SELECTED_ANIMATED = b'selectedAnimated'
DOG_TAGS_SELECTED_CUSTOMIZABLE = b'selectedCustomizable'
WOT_PLUS = b'wotPlus'
TELECOM_RENTALS = b'telecomRentals'
COMMENDATIONS = b'commendations'
PERSONAL_RESERVES = b'personalReserves'
LAST_ARTY_CTRL_MODE = b'lastArtyCtrlMode'
ACTIVE_TEST_PARTICIPATION_CONFIRMED = b'activeTestParticipateConfirmed'
MAPBOX_PROGRESSION = b'mapbox_progression'
UNLOCK_VEHICLES_IN_BATTLE_HINTS = b'unlockVehiclesInBattleHints'
BECOME_ELITE_VEHICLES_WATCHED = b'becomeEliteWatched'
VPP_ENTRY_POINT_LAST_SEEN_STEP = b'vehiclePostProgressionLastSeenStep'
CLAN_PREBATTLE_SORTING_KEY = b'ClanPrebattleSortingKey'
SHOW_DEMO_ACC_REGISTRATION = b'showDemoAccRegistration'
MAPBOX_SURVEYS = b'mapbox_surveys'
CLAN_NEWS_SEEN = b'clanNewsSeen'
INTEGRATED_AUCTION_NOTIFICATIONS = b'integratedAuctionNotifications'
INTEGRATED_AUCTION_FIRST_APPEARANCE_TIMESTAMP = b'integratedAuctionBannerFirstAppearanceTimestamp'
INTEGRATED_AUCTION_INTRO_CLICK_TIMESTAMP = b'integratedAuctionBannerIntroClickTimestamp'
MINIMAP_SIZE = b'minimapSize'
COMP7_UI_SECTION = b'comp7'
COMP7_WEEKLY_QUESTS_PAGE_TOKENS_COUNT = b'comp7WeeklyQuestsPageTokensCount'
COMP7_SHOP_SEEN_PRODUCTS = b'comp7ShopSeenProducts'
COMP7_LAST_SEASON = b'comp7LastSeason'
COMP7_WEEKLY_WIDGET_SHOWN_QUEST = b'comp7WeeklyWidgetShownQuest'
COMP7_LAST_SEASON_WHERE_STATISTICS_SHOWN = b'comp7LastSeasonWhereStatisticsShown'
COMP7_UMG_PROGRESSION_POINTS_SEEN = b'comp7UMGProgressionPointsSeen'
COMP7_UMG_ENTRY_POINT_SEEN = b'comp7UmgEntryPointSeen'
COMP7_PROGRESSION_PAGE_C11N_PROGRESS = b'comp7ProgressionPageC11nProgress'
COMP7_LIGHT_UI_SECTION = b'comp7Light'
COMP7_LIGHT_LAST_SEASON = b'comp7LightLastSeason'
COMP7_LIGHT_PROGRESSION_POINTS_SEEN = b'comp7LightProgressionPointsSeen'
COMP7_LIGHT_UMG_PROGRESSION_POINTS_SEEN = b'comp7LightUMGProgressionPointsSeen'
COMP7_LIGHT_UMG_SEEN_QUESTS = b'comp7LightUmgSeenQuests'
COMP7_LIGHT_UMG_ENTRY_POINT_SEEN = b'comp7LightUmgEntryPointSeen'
INGAME_TOURNAMENT_SECTION = b'ingameTournament'
INGAME_TOURNAMENT_WCI_INTRO_SEEN = b'WCIIntroSeen'
INGAME_TOURNAMENT_OLS_INTRO_SEEN = b'OLSIntroSeen'
FUN_RANDOM_NOTIFICATIONS = b'funRandomNotifications'
FUN_RANDOM_NOTIFICATIONS_FROZEN = b'funRandomNotificationsFrozen'
FUN_RANDOM_NOTIFICATIONS_PROGRESSIONS = b'funRandomNotificationsProgressions'
FUN_RANDOM_NOTIFICATIONS_SUB_MODES = b'funRandomNotificationsSubModes'
LOOTBOX_SYSTEM = b'lootBoxSystem'
LOOT_BOXES_WAS_STARTED = b'lootBoxesWasStarted'
LOOT_BOXES_WAS_FINISHED = b'lootBoxesWasFinished'
LOOT_BOXES_OPEN_ANIMATION_ENABLED = b'lootBoxesOpenAnimationEnabled'
LOOT_BOXES_HAS_NEW = b'lootBoxesHasNew'
LOOT_BOXES_SELECTED_BOX = b'lootBoxesSelectedBox'
LOOT_BOXES_UNIQUE_ID = b'lootBoxesUniqueID'
LOOT_BOXES_INTRO_VIDEO_SHOWN = b'lootBoxesIntroVideoShown'
OPEN_BUNDLE_NOTIFICATIONS = b'openBundle'
OPEN_BUNDLE_START_SHOWN = b'openBundleStartShown'
OPEN_BUNDLE_REMINDER_SHOWN = b'openBundleEndSoonShown'
OPEN_BUNDLE_ENTRY_POINT_SHOWN = b'openBundleEntryIntroShown'
OPEN_BUNDLE_ENTRY_POINT_ANIMATION_SHOWN = b'openBundleEntryAnimationShown'
OPEN_BUNDLE_INTRO_SHOWN = b'openBundleIntroShown'
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
ADVANCED_ACHIEVEMENTS = b'AdvancedAchievements'
PREV_CATEGORY_LIST_DATA = b'prevCategoryListData'
PREV_ACHIEVEMENT_SCORE = b'prevAchievementScore'
PREV_PLAYER_COLLECTION_PROGRESS = b'prevPlayerCollectionProgress'
PREV_TROPHY_COUNT = b'prevTrophyCount'
IS_NEEDED_SHOW_HINT_ACHIEVEMENT_CATALOG = b'isNeededShowHintAchievementCatalog'
UNSEEN_ADVANCED_ACHIEVEMENTS = b'unseenAdvancedAchievements'
SEEN_TROPHIES_ADVANCED_ACHIEVEMENTS = b'seenTrophiesAdvancedAchievements'
MAIN_ADVANCED_ACHIEVEMENTS_PAGE_VISITED = b'mainAdvancedAchievementsPageVisited'
EXCHANGE_GOLD_RATE_DISCOUNT_ANIMATION_SHOWED = b'ExchangeGoldRateDiscountAnimationShowed'
EXCHANGE_XP_RATE_DISCOUNT_ANIMATION_SHOWED = b'ExchangeXpRateDiscountAnimationShowed'
VIEWED_MODULES_SECTION = b'mua'
LIMITED_UI_VERSIONED_RULES = b'luiVersioned'
TANKMEN_LIST = b'tankmenList'
NATIONS_VISITED = b'nationsVisited'
VEH_SKILL_TREE_HINT_SHOWN = b'vehSkillTreeHintShown'
VEH_SKILL_TREE_POPUP_SHOWN = b'vehSkillTreePopupShown'
VEH_SKILL_TREE_RECORDED_NOFITICATION_NODE = b'vehSkillTreeRecordedNotificationNode'
VEH_SKILL_TREE_PRESTIGE_GLARE_SHOWN = b'vehSkillTreePrestigeGlareShown'
VEH_SKILL_TREE_INTRO_SHOWN = b'vehSkillTreeIntroShown'
PERSONAL_MISSION_3 = b'PERSONAL_MISSION_3'
CHALLENGES_START_SEEN_NOTIFICATION = b'challengesStartSeenNotification'
CHALLENGES_REMINDER_SEEN_NOTIFICATION = b'challengesReminderSeenNotification'
HANGAR_VIEW_SETTINGS = b'hangarView'
HANGAR_KEY_BINDINGS = b'hangarKeyBindings'

class BattleMatters(object):
    BATTLE_MATTERS_SETTINGS = b'battleMattersSettings'
    BATTLES_COUNT_WITHOUT_PROGRESS = b'battlesCountWithoutProgress'
    QUEST_IDX_FOR_LAST_UPDATED_PROGRESS = b'progressForQuest'
    LAST_QUEST_PROGRESS = b'lastQuestProgress'
    REMINDER_LAST_DISPLAY_TIME = b'reminderLastDisplayTime'
    LAST_BATTLE_TIME = b'lastBattleTime'


class Winback(object):
    WINBACK_SETTINGS = b'winbackSettings'
    COMPLETED_STARTING_QUEST_COUNT = b'completedStartingQuestCount'
    INTRO_SHOWN = b'introShown'
    BATTLE_SELECTOR_SETTINGS_BULLET_SHOWN = b'battleSelectorSettingsBulletShown'


class EasyTankEquip(object):
    EASY_TANK_EQUIP_SETTINGS = b'easyTankEquipSettings'
    SHELLS_CARD_SELECTED_PRESET_INDEX = b'shellsCardSelectedPresetIndex'
    CONSUMABLES_CARD_SELECTED_PRESET_INDEX = b'consumablesCardSelectedPresetIndex'
    CONSUMABLES_CARD_PRESET_SLOTS_ORDER = b'consumablesCardPresetSlotsOrder'


class AdventCalendar(object):
    SETTINGS = b'adventCalendarSettings'
    INTRO_SHOWN = b'adventCalendarIntroShown'
    LAST_HIGHLIGHTED_DOOR = b'adventCalendarLastHighlightedDoor'
    FIRST_ENTRY_NOTIFICATION_SHOWING_DAY = b'adventCalendarFirstEntryNotificationShowingDay'
    LAST_DAY_POPUP_SEEN = b'adventCalendarLastDayPopupSeen'


class StrongholdEvent(object):
    SETTINGS = b'strongholdEventSettings'
    IS_BANNER_FIRST_APPEARANCE_SEEN = b'isBannerFirstAppearanceSeen'
    FIRST_BANNER_ENTERING_MADE = b'firstBannerEnteringMade'


class ResourceWell(object):
    SETTINGS = b'resourceWellSettings'
    START_SHOWN = b'resourceWellStartShown'
    END_SHOWN = b'resourceWellEndShown'
    NOTIFICATIONS = b'resourceWellNotifications'
    IS_BANNER_FIRST_APPEARANCE_SEEN = b'isBannerFirstAppearanceSeen'
    FIRST_BANNER_ENTERING_MADE = b'firstBannerEnteringMade'


class OptionalDevicesAssistant(object):
    SELECTED_PRESET = b'optionalDevicesAssistantSelectedPreset'


class PetSystem(object):
    SETTINGS = b'petSystemSettings'
    SEEN_PET_NAME_IDS = b'petSystemSeenPetNameIDs'
    SEEN_PET_LEVELS = b'petSystemSeenPetLevels'
    SEEN_IN_STORAGE_PET_IDS = b'petSystemSeenInStoragePetIDs'
    SEEN_PROMO_PET_IDS = b'petSystemSeenPromoPetIDs'


class ChallengesMissions(object):
    SETTINGS = b'challengesSettings'
    CHALLENGES_BUNDLE_SHOWN = b'challengesBundleIntroShown'
    CHALLENGES_BUNDLE_ANIMATION_SHOWN = b'challengesBundleAnimationShown'
    VISITED_CHALLENGES = b'visitedChallenges'
    CHALLENGES_INFO_SHOWN = b'challengesInfoShown'


AttackerVehicleConfiguration = namedtuple(b'AttackerVehicleConfiguration', [b'compactDescr', b'gunCompactDescr', b'activeGunShotIndex'])
KNOWN_SELECTOR_BATTLES = b'knownSelectorBattles'
MODE_SELECTOR_BATTLE_PASS_SHOWN = b'modeSelectorBattlePassShown'
RANKED_LAST_CYCLE_ID = b'rankedLastCycleID'
EPIC_LAST_CYCLE_ID = b'epicLastCycleID'
FRONTLINE_BANNER_FIRST_APPEARANCE_TIMESTAMP = b'frontlineBannerFirstAppearanceTimestamp'
FRONTLINE_BANNER_INTRO_CLICK_TIMESTAMP = b'frontlineBannerIntroClickTimestamp'
COMP7_BANNER_FIRST_APPEARANCE_TIMESTAMP = b'comp7BannerFirstAppearanceTimestamp'
COMP7_LIGHT_BANNER_FIRST_APPEARANCE_TIMESTAMP = b'comp7LightBannerFirstAppearanceTimestamp'
BATTLE_ROYALE_BANNER_FIRST_APPEARANCE_TIMESTAMP = b'battleRoyaleBannerFirstAppearanceTimestamp'
FUN_RANDOM_BANNER_INTRO_CLICK_TIMESTAMP = b'funRandomBannerIntroClickTimestamp'
FUN_RANDOM_BANNER_LAST_VISIBLE_PROGRESSION_NAME = b'funRandomBannerLastVisibleProgressionName'
FUN_RANDOM_LAST_PRESET = b'funRandomLastPreset'
FUN_RANDOM_PROGRESSION_OPENED = b'funRandomProgressionOpened'
FUN_RANDOM_INF_PROGRESSION_OPENED = b'funRandomInfProgressionOpened'
FUN_RANDOM_PROGRESSION = b'funRandomProgression'
FUN_RANDOM_PROGR_PREV_COUNTER = b'funRandomProgressionPrevCounter'
FUN_RANDOM_INF_PROGR_PREV_COUNTER = b'funRandomInfProgressionPrevCounter'
FUN_RANDOM_INF_PROGR_PREV_COMPLETE_COUNT = b'funRandomInfProgressionPrevCompleteCount'
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
                                     b'role_SPG': False}, 
                 CAROUSEL_FILTER_3: {b'own3DStyle': False, 
                                     b'canInstallAttachments': False}, 
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
                                            b'role_SPG': False}, 
                 RANKED_CAROUSEL_FILTER_3: {b'own3DStyle': False, 
                                            b'canInstallAttachments': False}, 
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
                                                b'event': False, 
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
                                                b'role_SPG': False}, 
                 EPICBATTLE_CAROUSEL_FILTER_3: {b'own3DStyle': False, 
                                                b'canInstallAttachments': False}, 
                 EPICBATTLE_CAROUSEL_FILTER_CLIENT_1: {b'level_8': True, 
                                                       b'level_9': True, 
                                                       b'searchNameVehicle': b'', 
                                                       b'clanRented': False}, 
                 EPICBATTLE_CAROUSEL_FILTER_CLIENT_2: {b'level_8': True, 
                                                       b'level_9': False, 
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
                                            b'level_11': False}, 
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
                                            b'role_SPG': False}, 
                 MAPBOX_CAROUSEL_FILTER_3: {b'own3DStyle': False, 
                                            b'canInstallAttachments': False}, 
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
                                                b'role_SPG': False}, 
                 FUN_RANDOM_CAROUSEL_FILTER_3: {b'own3DStyle': False, 
                                                b'canInstallAttachments': False}, 
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
                                           b'role_SPG': False}, 
                 COMP7_CAROUSEL_FILTER_3: {b'own3DStyle': False, 
                                           b'canInstallAttachments': False}, 
                 COMP7_CAROUSEL_FILTER_CLIENT_1: {b'searchNameVehicle': b'', 
                                                  b'clanRented': False}, 
                 COMP7_LIGHT_CAROUSEL_FILTER_1: {b'ussr': False, 
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
                 COMP7_LIGHT_CAROUSEL_FILTER_2: {b'premium': False, 
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
                                                 b'role_SPG': False}, 
                 COMP7_LIGHT_CAROUSEL_FILTER_3: {b'own3DStyle': False, 
                                                 b'canInstallAttachments': False}, 
                 COMP7_LIGHT_CAROUSEL_FILTER_CLIENT_1: {b'searchNameVehicle': b'', 
                                                        b'clanRented': False}, 
                 MISSION_SELECTOR_FILTER: {b'inventory': False}, 
                 PM_SELECTOR_FILTER: {b'inventory': False}, 
                 ORDERS_FILTER: {b'isSelected': False}, GUI_START_BEHAVIOR: {b'isFreeXPInfoDialogShowed': False, 
                                      b'isRankedWelcomeViewShowed': False, 
                                      b'isRankedWelcomeViewStarted': False, 
                                      b'isDisplayPlatoonMembersClicked': False, 
                                      (GuiSettingsBehavior.VEH_POST_PROGRESSION_UNLOCK_MSG_NEED_SHOW): True, 
                                      (GuiSettingsBehavior.IS_PRESTIGE_ONBOARDING_VIEWED): False, 
                                      (GuiSettingsBehavior.PRESTIGE_FIRST_ENTRY_NOTIFICATION_SHOWN): False, 
                                      b'birthdayCalendarIntroShowed': False, 
                                      (GuiSettingsBehavior.COMP7_YEARLY_ANIMATION_SEEN): False, 
                                      (GuiSettingsBehavior.CLAN_SUPPLY_INTRO_SHOWN): False, 
                                      (GuiSettingsBehavior.CREW_PE_WELCOME_SHOWN): False, 
                                      (GuiSettingsBehavior.CREW_MENTORING_LICENSE_AWARDS_SHOWN): False, 
                                      (GuiSettingsBehavior.W2GT_APPLIED): False}, 
                 EULA_VERSION: {b'version': 0}, FORT_MEMBER_TUTORIAL: {b'wasShown': False}, IGR_PROMO: {b'wasShown': False}, CONTACTS: {b'showOfflineUsers': True, b'showOthersCategory': True}, BOOSTERS_FILTER: 0, 
                 b'cs_intro_view_vehicle': {b'nation': (-1), b'vehicleType': b'none', b'isMain': False, b'level': (-1), b'compatibleOnly': True}, 
                 b'cs_list_view_vehicle': {b'nation': (-1), b'vehicleType': b'none', b'isMain': False, b'level': (-1), b'compatibleOnly': True}, 
                 b'cs_unit_view_vehicle': {b'nation': (-1), b'vehicleType': b'none', b'isMain': False, b'level': (-1), b'compatibleOnly': True}, 
                 b'cs_unit_view_settings': {b'nation': (-1), b'vehicleType': b'none', b'isMain': False, b'level': (-1), b'compatibleOnly': True}, 
                 b'epic_rent_view_vehicle': {b'nation': (-1), b'vehicleType': b'none', b'isMain': False, b'level': (-1), b'compatibleOnly': True}, 
                 PROMO: {}, PROFILE_TECHNIQUE: {b'selectedColumn': 4, b'selectedColumnSorting': b'descending', b'isInHangarSelected': False}, PROFILE_TECHNIQUE_MEMBER: {b'selectedColumn': 4, b'selectedColumnSorting': b'descending'}, SPEAKERS_DEVICE: 0, 
                 UNIT_FILTER: {(GAME.UNIT_FILTER): 4095}, TANKMEN_LIST: {}}, 
   KEY_FAVORITES: {CURRENT_VEHICLE: 0, 
                   ROYALE_VEHICLE: 0, 
                   FALLOUT_VEHICLES: {}}, 
   KEY_MANUAL: {LOBBY_MENU_MANUAL_TRIGGER_SHOWN: False, 
                MANUAL_NEW_CONTENT: {}}, 
   KEY_SETTINGS: {b'unitWindow': {SELECTED_INTRO_VEHICLES_FIELD: []}, b'vehicleSellDialog': {b'isOpened': False}, 
                  KNOWN_SELECTOR_BATTLES: (set()), 
                  b'tankmanDropSkillIdx': 0, 
                  b'cursor': False, 
                  b'arcade': {b'mixing': {b'alpha': 100, b'type': 3}, b'gunTag': {b'alpha': 100, b'type': 9}, b'centralTag': {b'alpha': 100, b'type': 8}, b'net': {b'alpha': 100, b'type': 0}, b'reloader': {b'alpha': 100, b'type': 0}, b'condition': {b'alpha': 100, b'type': 0}, b'cassette': {b'alpha': 100, b'type': 0}, b'reloaderTimer': {b'alpha': 100, b'type': 0}, b'zoomIndicator': {b'alpha': 100, b'type': 0}}, b'sniper': {b'mixing': {b'alpha': 90, b'type': 0}, b'gunTag': {b'alpha': 90, b'type': 0}, b'centralTag': {b'alpha': 90, b'type': 0}, b'net': {b'alpha': 90, b'type': 0}, b'reloader': {b'alpha': 90, b'type': 0}, b'condition': {b'alpha': 90, b'type': 0}, b'cassette': {b'alpha': 90, b'type': 0}, b'reloaderTimer': {b'alpha': 100, b'type': 0}, b'zoomIndicator': {b'alpha': 100, b'type': 0}}, b'spgAim': {(SPGAim.SHOTS_RESULT_INDICATOR): True, 
                              (SPGAim.SPG_SCALE_WIDGET): True, 
                              (SPGAim.AUTO_CHANGE_AIM_MODE): True, 
                              (SPGAim.AIM_ENTRANCE_MODE): 0}, 
                  b'contour': {(CONTOUR.ENHANCED_CONTOUR): False, 
                               (CONTOUR.CONTOUR_PENETRABLE_ZONE): 0, 
                               (CONTOUR.CONTOUR_IMPENETRABLE_ZONE): 0}, 
                  (ArmorFlashlight.ENABLED): False, 
                  (ArmorFlashlight.COLOR_SCHEMA): 0, 
                  (ArmorFlashlight.FILL): 0, 
                  (ArmorFlashlight.OPACITY): 1, 
                  (ArmorFlashlight.RESOLUTION): None, 
                  LAST_ARTY_CTRL_MODE: (CTRL_MODE_NAME.STRATEGIC), 
                  b'markers': {b'ally': {b'markerBaseIcon': False, 
                                         b'markerBaseLevel': False, 
                                         b'markerBaseHpIndicator': True, 
                                         b'markerBaseDamage': True, 
                                         b'markerBaseHp': 2, 
                                         b'markerBaseVehicleName': True, 
                                         b'markerBasePlayerName': False, 
                                         b'markerBaseAimMarker2D': False, 
                                         b'markerAltIcon': False, 
                                         b'markerAltLevel': True, 
                                         b'markerAltHpIndicator': True, 
                                         b'markerAltDamage': True, 
                                         b'markerAltHp': 1, 
                                         b'markerAltVehicleName': False, 
                                         b'markerAltPlayerName': True, 
                                         b'markerAltAimMarker2D': False}, 
                               b'enemy': {b'markerBaseIcon': False, 
                                          b'markerBaseLevel': False, 
                                          b'markerBaseHpIndicator': True, 
                                          b'markerBaseDamage': True, 
                                          b'markerBaseHp': 2, 
                                          b'markerBaseVehicleName': True, 
                                          b'markerBasePlayerName': False, 
                                          b'markerBaseAimMarker2D': True, 
                                          b'markerAltIcon': False, 
                                          b'markerAltLevel': True, 
                                          b'markerAltHpIndicator': True, 
                                          b'markerAltDamage': True, 
                                          b'markerAltHp': 1, 
                                          b'markerAltVehicleName': False, 
                                          b'markerAltPlayerName': True, 
                                          b'markerAltAimMarker2D': True}, 
                               b'dead': {b'markerBaseIcon': False, 
                                         b'markerBaseLevel': False, 
                                         b'markerBaseHpIndicator': False, 
                                         b'markerBaseDamage': True, 
                                         b'markerBaseHp': 3, 
                                         b'markerBaseVehicleName': True, 
                                         b'markerBasePlayerName': False, 
                                         b'markerBaseAimMarker2D': False, 
                                         b'markerAltIcon': False, 
                                         b'markerAltLevel': True, 
                                         b'markerAltHpIndicator': True, 
                                         b'markerAltDamage': True, 
                                         b'markerAltHp': 1, 
                                         b'markerAltVehicleName': False, 
                                         b'markerAltPlayerName': True, 
                                         b'markerAltAimMarker2D': False}}, 
                  COMP7_PREBATTLE_CAROUSEL_ROW_VALUE: (-1), 
                  (GAME.COMP7_MINIMAP_SIZE): (-1), 
                  COMP7_IS_VOIP_IN_BATTLE_ACTIVATED: False, 
                  COMP7_ENTITLEMENTS: {COMP7_ENTITLEMENTS_TIMESTAMP: 0, 
                                       COMP7_ENTITLEMENTS_BALANCE: {}}, 
                  b'showVehicleIcon': False, 
                  b'showVehicleLevel': False, 
                  b'showExInf4Destroyed': False, 
                  b'ingameHelpVersion': (-1), 
                  b'isColorBlind': False, 
                  b'useServerAim': False, 
                  b'showDamageIcon': True, 
                  b'showVehiclesCounter': True, 
                  b'minimapAlpha': 0, 
                  (GAME.MINIMAP_SIZE): None, 
                  (GAME.SHOW_VEHICLE_HP_IN_PLAYERS_PANEL): 1, 
                  (GAME.SHOW_VEHICLE_HP_IN_MINIMAP): 1, 
                  b'minimapRespawnSize': 0, 
                  b'minimapViewRange': True, 
                  b'minimapMaxViewRange': True, 
                  b'minimapDrawRange': True, 
                  b'minimapAlphaEnabled': False, 
                  b'epicMinimapZoom': 1.5, 
                  (GAME.TRAINING_MINIMAP_SIZE): None, 
                  b'increasedZoom': True, 
                  b'sniperModeByShift': True, 
                  b'nationalVoices': False, 
                  b'enableVoIP': True, 
                  b'replayEnabled': 1, 
                  b'sniperZoom': 0, 
                  (GAME.SWITCH_SETUPS_IN_LOADING): None, 
                  (GAME.HULLLOCK_ENABLED): True, 
                  (GAME.PRE_COMMANDER_CAM): True, 
                  (GAME.COMMANDER_CAM): True, 
                  (GAME.SCROLL_SMOOTHING): True, 
                  (GAME.W2GT_ENABLE): False, 
                  b'hangarCamPeriod': 1, 
                  b'hangarCamParallaxEnabled': True, 
                  b'players_panel': {b'state': None, 
                                     b'showLevels': True, 
                                     b'showTypes': True}, 
                  b'epic_random_players_panel': {b'state': 5}, 
                  b'gameplayMask': (gameplay_ctx.getDefaultMask()), 
                  b'statsSorting': {b'iconType': b'tank', 
                                    b'sortDirection': b'descending'}, 
                  b'statsSortingSortie': {b'iconType': b'tank', 
                                          b'sortDirection': b'descending'}, 
                  STATS_COMP7_SORTING: {b'iconType': b'rank', 
                                        b'sortDirection': b'descending'}, 
                  STATS_COMP7_LIGHT_SORTING: {b'iconType': b'prestigePoints', 
                                              b'sortDirection': b'descending'}, 
                  STATS_COMP7_SPECIAL_SORTING: {b'iconType': b'tank', 
                                                b'sortDirection': b'descending'}, 
                  STATS_FUN_RANDOM_SORTING: {b'iconType': b'xp', 
                                             b'sortDirection': b'descending'}, 
                  b'backDraftInvert': False, 
                  QUESTS: {b'lastVisitTime': (-1), 
                           b'visited': [], b'naVisited': [], b'personalMissions': {b'introShown': False, 
                                                 b'operationsVisited': (set()), 
                                                 b'headerAlert': False}, 
                           b'dailyQuests': {b'lastVisitedDQTabIdx': None, 
                                            b'seenCompleted': False, 
                                            b'visitedBonus': False, 
                                            b'premMissionsTabDiscovered': False}, 
                           QUEST_DELTAS: {QUEST_DELTAS_COMPLETION: (dict()), 
                                          QUEST_DELTAS_PROGRESS: (dict()), 
                                          QUEST_DELTAS_TOKENS_PROGRESS: (dict())}}, 
                  b'checkBoxConfirmator': {b'questsConfirmDialogShow': True, 
                                           b'questsConfirmDialogShowPM2': True}, 
                  DOG_TAGS: {b'lastVisitedDogTagsTabIdx': None, 
                             b'onboardingEnabled': True, 
                             b'seenComps': (set()), 
                             b'animatedDogTagsVisited': False, 
                             b'customizableDogTagsVisited': False, 
                             DOG_TAGS_SELECTED_ANIMATED: [], DOG_TAGS_SELECTED_CUSTOMIZABLE: []}, 
                  WOT_PLUS: {b'isFirstTime': True, 
                             b'isWotPlusEnabled': False, 
                             b'isGoldReserveEnabled': False, 
                             b'isPassiveXpEnabled': False, 
                             b'isFreeDemountingEnabled': False, 
                             b'isExcludedMapEnabled': False, 
                             b'isDailyAttendancesEnabled': False, 
                             b'amountOfDailyAttendance': 0, 
                             b'isBattleBonusesEnabled': False, 
                             b'isBadgesEnabled': False, 
                             b'isAdditionalXPEnabled': False, 
                             b'isOptionalDevicesAssistantEnabled': False, 
                             b'isCrewAssistantEnabled': False, 
                             b'isServiceRecordCustomizationEnabled': False, 
                             b'isProBoostEnabled': False, 
                             b'isBattlePassEnabled': False}, 
                  TELECOM_RENTALS: {b'isTelecomRentalsEnabled': True, 
                                    b'isTelecomRentalsBlocked': True}, 
                  COMMENDATIONS: {b'isMessagesEnable': True, 
                                  b'isLiveTagsEnable': True}, 
                  PERSONAL_RESERVES: {b'isFirstTimeNotificationShown': False, 
                                      b'isIntroPageShown': False, 
                                      b'boosterCardHintsSeen': (set())}, 
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
                  b'interfaceScale': 0, 
                  b'medKitInstalled': False, 
                  b'repairKitInstalled': False, 
                  b'fireExtinguisherInstalled': False, 
                  b'PveTriggerShown': False, 
                  b'isEpicPerformanceWarningClicked': False, 
                  LAST_PROMO_PATCH_VERSION: b'', 
                  LAST_RESTORE_NOTIFICATION: None, 
                  b'dynamicRange': 0, 
                  b'soundDevice': 0, 
                  b'bassBoost': False, 
                  (SOUND.LOW_QUALITY): (WWISE.WG_isMSR()), 
                  b'nightMode': False, 
                  (SOUND.DETECTION_ALERT_SOUND): b'lightbulb', 
                  (SOUND.ARTY_SHOT_ALERT_SOUND): b'artillery_lightbulb', 
                  (SOUND.PHYSICS_QUALITY): b'disabled', 
                  PREVIEW_INFO_PANEL_IDX: 0, 
                  b'carouselType': 0, 
                  b'doubleCarouselType': 0, 
                  b'contentType': 0, 
                  b'vehicleCarouselStats': True, 
                  WHEELED_DEATH_DELAY_COUNT: 10, 
                  FREE_CAM_USES_COUNT: 0, 
                  NEW_SETTINGS_COUNTER: {b'GameSettings': {(BattleCommStorageKeys.SHOW_LOCATION_MARKERS): True, 
                                                           (BattleCommStorageKeys.ENABLE_COMMENDATIONS_FEEDBACK): True, 
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
                                                           (GAME.SHOW_ARTY_HIT_ON_MAP): True, 
                                                           (GAME.SWITCH_SETUPS_IN_LOADING): True, 
                                                           (GAME.SCROLL_SMOOTHING): True, 
                                                           (GAME.LIMITED_UI_ACTIVE): True, 
                                                           (GAME.GAMEPLAY_DEV_MAPS): True, 
                                                           (GAME.POSTMORTEM_MODE): True}, 
                                         b'GraphicSettings': {b'ScreenSettings': {b'gammaSetting': True, 
                                                                                  b'colorFilter': True}, 
                                                              b'AdvancedGraphicSettings': {b'HAVOK_ENABLED': True, 
                                                                                           b'TERRAIN_TESSELLATION_ENABLED': True, 
                                                                                           b'SNIPER_MODE_TERRAIN_TESSELLATION_ENABLED': True, 
                                                                                           b'TRACK_PHYSICS_QUALITY': True, 
                                                                                           b'VISIBILITY_TUNNEL_ENABLED': True}}, 
                                         b'FeedbackSettings': {b'feedbackBattleBorderMap': {b'battleBorderMapType': True, 
                                                                                            b'battleBorderMapMode': True}, 
                                                               b'feedbackQuestsProgress': {(ScorePanelStorageKeys.SHOW_HP_VALUES): True, 
                                                                                           (ScorePanelStorageKeys.SHOW_HP_DIFFERENCE): True, 
                                                                                           (ScorePanelStorageKeys.ENABLE_TIER_GROUPING): True, 
                                                                                           (ScorePanelStorageKeys.SHOW_HP_BAR): True, 
                                                                                           b'progressViewType': True, 
                                                                                           b'progressViewConditions': True}, 
                                                               b'feedbackDamageIndicator': {b'damageIndicatorAllies': True}, 
                                                               b'feedbackBattleEvents': {(BATTLE_EVENTS.CREW_PERKS): True, 
                                                                                         (SITUATIONAL_PERKS.ARMOR_PATCHING): True, 
                                                                                         (SITUATIONAL_PERKS.COMMANDER_EAGLE_EYE): True, 
                                                                                         (SITUATIONAL_PERKS.COMMANDER_EMERGENCY): True, 
                                                                                         (SITUATIONAL_PERKS.COMMANDER_TUTOR): True, 
                                                                                         (SITUATIONAL_PERKS.COMMANDER_COORDINATION): True, 
                                                                                         (SITUATIONAL_PERKS.COMMANDER_HOLD_LINE): True, 
                                                                                         (SITUATIONAL_PERKS.COMMANDER_STAY_SHARP): True, 
                                                                                         (SITUATIONAL_PERKS.GUNNER_FOCUS): True, 
                                                                                         (SITUATIONAL_PERKS.GUNNER_LONE_WOLF): True, 
                                                                                         (SITUATIONAL_PERKS.DRIVER_MOTOR_EXPERT): True, 
                                                                                         (SITUATIONAL_PERKS.DRIVER_SUSPENSION_REPAIR): True, 
                                                                                         (SITUATIONAL_PERKS.DRIVER_BULLETPROOF): True, 
                                                                                         (SITUATIONAL_PERKS.LOADER_DESPERADO): True, 
                                                                                         (SITUATIONAL_PERKS.LOADER_INTUITION): True, 
                                                                                         (SITUATIONAL_PERKS.LOADER_MELEE): True, 
                                                                                         (SITUATIONAL_PERKS.LOADER_SECOND_CHANCE): True, 
                                                                                         (SITUATIONAL_PERKS.RADIOMAN_SIDE_BY_SIDE): True, 
                                                                                         (SITUATIONAL_PERKS.RADIOMAN_EXPERT): True, 
                                                                                         (SITUATIONAL_PERKS.RADIOMAN_THREAT_SEARCH): True}}, 
                                         b'ControlsSettings': {b'highlightLocation': True, 
                                                               b'showQuestProgress': True, 
                                                               b'chargeFire': True, 
                                                               b'affirmative': True, 
                                                               b'negative': True, 
                                                               b'showPersonalReserves': True, 
                                                               b'toggleFlashlight': True, 
                                                               b'specialAbility': True}, 
                                         b'AimSettings': {(AIM.SPG): {(SPGAim.AUTO_CHANGE_AIM_MODE): True, 
                                                                      (SPGAim.SPG_SCALE_WIDGET): True, 
                                                                      (SPGAim.SPG_STRATEGIC_CAM_MODE): True, 
                                                                      (SPGAim.SHOTS_RESULT_INDICATOR): True, 
                                                                      (SPGAim.AIM_ENTRANCE_MODE): True}, 
                                                          (AIM.CONTOUR): {(CONTOUR.ENHANCED_CONTOUR): True, 
                                                                          (CONTOUR.CONTOUR_PENETRABLE_ZONE): True, 
                                                                          (CONTOUR.CONTOUR_IMPENETRABLE_ZONE): True}, 
                                                          (AIM.ARMOR_FLASHLIGHT): {(ArmorFlashlight.ENABLED): True, 
                                                                                   (ArmorFlashlight.COLOR_SCHEMA): True, 
                                                                                   (ArmorFlashlight.OPACITY): True, 
                                                                                   (ArmorFlashlight.FILL): True, 
                                                                                   (ArmorFlashlight.RESOLUTION): True}}, 
                                         b'SoundSettings': {b'artyBulbVoices': True, 
                                                            b'physicsQuality': True}}, 
                  CLAN_PREBATTLE_SORTING_KEY: 0, 
                  SHOW_OPT_DEVICE_HINT: True, 
                  SHOW_OPT_DEVICE_HINT_TROPHY: True, 
                  SHOW_OPT_MODERNIZED_DEVICE_HINT: True, 
                  LAST_BADGES_VISIT: 0, 
                  LAST_SELECTED_SUFFIX_BADGE_ID: 0, 
                  ENABLE_RANKED_ANIMATIONS: True, 
                  COLOR_SETTINGS_TAB_IDX: 0, 
                  COLOR_SETTINGS_SHOWS_COUNT: 0, 
                  SELECTED_QUEST_IN_REPLAY: None, 
                  APPLIED_COLOR_SETTINGS: {}, LAST_SELECTED_PM_BRANCH: 0, 
                  CRYSTALS_INFO_SHOWN: False, 
                  NPS_STORAGE: {}, TRAJECTORY_VIEW_HINT_SECTION: {HINTS_LEFT: 3, 
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
                  TWIN_GUN_HINT_SECTION: {HINTS_LEFT: 3, 
                                          LAST_DISPLAY_DAY: 0, 
                                          NUM_BATTLES: 0}, 
                  ROCKET_ACCELERATION_MODE_HINT_SECTION: {HINTS_LEFT: 3, 
                                                          LAST_DISPLAY_DAY: 0, 
                                                          NUM_BATTLES: 0}, 
                  RECHARGEABLE_NITRO_MODE_HINT_SECTION: {HINTS_LEFT: 3, 
                                                         LAST_DISPLAY_DAY: 0, 
                                                         NUM_BATTLES: 0}, 
                  STAGED_JET_BOOSTERS_MODE_HINT_SECTION: {HINTS_LEFT: 3, 
                                                          LAST_DISPLAY_DAY: 0, 
                                                          NUM_BATTLES: 0}, 
                  WHEELED_DASH_MODE_HINT_SECTION: {HINTS_LEFT: 3, 
                                                   LAST_DISPLAY_DAY: 0, 
                                                   NUM_BATTLES: 0}, 
                  TARGET_DESIGNATOR_MODE_HINT_SECTION: {HINTS_LEFT: 3, 
                                                        LAST_DISPLAY_DAY: 0, 
                                                        NUM_BATTLES: 0}, 
                  RADAR_HINT_SECTION: {HINTS_LEFT: 3, 
                                       LAST_DISPLAY_DAY: 0, 
                                       NUM_BATTLES: 0}, 
                  PILLBOX_HINT_SECTION: {HINTS_LEFT: 3, 
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
                  LAST_BATTLE_PASS_POINTS_SEEN: {}, LAST_BATTLE_PASS_CYCLES_SEEN: 0, 
                  IS_BATTLE_PASS_EXTRA_START_NOTIFICATION_SEEN: (set()), 
                  LAST_BATTLE_PASS_EXTRA_CHAPTER_SEEN: 0, 
                  UMG_BATTLE_PASS_EXTRA_CHAPTER_SEEN: 0, 
                  LAST_BATTLE_PASS_HOLIDAY_CHAPTER_SEEN: 0, 
                  IS_BATTLE_PASS_COLLECTION_SEEN: False, 
                  IS_BATTLE_PASS_START_NOTIFICATION_SEEN: False, 
                  EXTRA_CHAPTERS_VIDEO_SHOWN: (set()), 
                  BUY_ANIMATIONS_WAS_SHOWN: (set()), 
                  IS_BATTLE_PASS_START_ANIMATION_SEEN: False, 
                  MODULES_ANIMATION_SHOWN: False, 
                  SUBTITLES: True, 
                  RANKED_YEAR_POSITION: None, 
                  TOP_OF_TREE_CONFIG: {}, BECOME_ELITE_VEHICLES_WATCHED: (set()), 
                  (GAME.GAMEPLAY_DEV_MAPS): True, 
                  MAPBOX_PROGRESSION: {b'previous_battles_played': 0, 
                                       b'visited_maps': [], b'stored_rewards': {}, b'lastCycleId': None}, 
                  MAPBOX_SURVEYS: {}, UNLOCK_VEHICLES_IN_BATTLE_HINTS: 5, 
                  MODE_SELECTOR_BATTLE_PASS_SHOWN: {}, RANKED_LAST_CYCLE_ID: None, 
                  EPIC_LAST_CYCLE_ID: None, 
                  INTEGRATED_AUCTION_FIRST_APPEARANCE_TIMESTAMP: 0, 
                  INTEGRATED_AUCTION_INTRO_CLICK_TIMESTAMP: 0, 
                  FRONTLINE_BANNER_FIRST_APPEARANCE_TIMESTAMP: 0, 
                  FRONTLINE_BANNER_INTRO_CLICK_TIMESTAMP: 0, 
                  COMP7_BANNER_FIRST_APPEARANCE_TIMESTAMP: 0, 
                  COMP7_LIGHT_BANNER_FIRST_APPEARANCE_TIMESTAMP: 0, 
                  BATTLE_ROYALE_BANNER_FIRST_APPEARANCE_TIMESTAMP: 0, 
                  FUN_RANDOM_BANNER_INTRO_CLICK_TIMESTAMP: 0, 
                  FUN_RANDOM_BANNER_LAST_VISIBLE_PROGRESSION_NAME: b'', 
                  FUN_RANDOM_LAST_PRESET: b'undefined', 
                  FUN_RANDOM_PROGRESSION_OPENED: False, 
                  FUN_RANDOM_INF_PROGRESSION_OPENED: False, 
                  FUN_RANDOM_PROGRESSION: {}, SHOW_DEMO_ACC_REGISTRATION: False, 
                  IS_CUSTOMIZATION_INTRO_VIEWED: False, 
                  CUSTOMIZATION_STYLE_ITEMS_VISITED: (set()), 
                  CUSTOMIZATION_TABS_VISITED: (set([526, 531, 508, 495, 576, 694, 695])), 
                  (OptionalDevicesAssistant.SELECTED_PRESET): 0, 
                  OPT_DEVICE_TAB_VISITED: {}, (BattleMatters.BATTLE_MATTERS_SETTINGS): {(BattleMatters.BATTLES_COUNT_WITHOUT_PROGRESS): 0, 
                                                            (BattleMatters.QUEST_IDX_FOR_LAST_UPDATED_PROGRESS): 0, 
                                                            (BattleMatters.LAST_QUEST_PROGRESS): 0, 
                                                            (BattleMatters.REMINDER_LAST_DISPLAY_TIME): 0, 
                                                            (BattleMatters.LAST_BATTLE_TIME): 0}, 
                  ROYALE_INTRO_VIDEO_SHOWN_FOR_SEASON: 0, 
                  ROYALE_SQUAD_TIP_SHOWN_FOR_SEASON: 0, 
                  LOOTBOX_SYSTEM: {}, CUSTOM_SHOP_SETTINGS: {}, (Winback.WINBACK_SETTINGS): {(Winback.COMPLETED_STARTING_QUEST_COUNT): 0, 
                                               (Winback.INTRO_SHOWN): False, 
                                               (Winback.BATTLE_SELECTOR_SETTINGS_BULLET_SHOWN): False}, 
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
                  ADVANCED_ACHIEVEMENTS: {PREV_ACHIEVEMENT_SCORE: 0, 
                                          PREV_TROPHY_COUNT: 0, 
                                          PREV_PLAYER_COLLECTION_PROGRESS: 0, 
                                          PREV_CATEGORY_LIST_DATA: [
                                                                  (0, 0), (0, 0), (0, 0)], 
                                          IS_NEEDED_SHOW_HINT_ACHIEVEMENT_CATALOG: True, 
                                          UNSEEN_ADVANCED_ACHIEVEMENTS: {}, SEEN_TROPHIES_ADVANCED_ACHIEVEMENTS: {}, MAIN_ADVANCED_ACHIEVEMENTS_PAGE_VISITED: False}, 
                  (EasyTankEquip.EASY_TANK_EQUIP_SETTINGS): {(EasyTankEquip.SHELLS_CARD_SELECTED_PRESET_INDEX): 0, 
                                                             (EasyTankEquip.CONSUMABLES_CARD_SELECTED_PRESET_INDEX): 0, 
                                                             (EasyTankEquip.CONSUMABLES_CARD_PRESET_SLOTS_ORDER): [
                                                                                                                 0, 1, 2]}, 
                  (AdventCalendar.SETTINGS): {(AdventCalendar.INTRO_SHOWN): False, 
                                              (AdventCalendar.LAST_HIGHLIGHTED_DOOR): (-1), 
                                              (AdventCalendar.FIRST_ENTRY_NOTIFICATION_SHOWING_DAY): (-1), 
                                              (AdventCalendar.LAST_DAY_POPUP_SEEN): 0}, 
                  (ResourceWell.SETTINGS): {(ResourceWell.FIRST_BANNER_ENTERING_MADE): (set()), 
                                            (ResourceWell.IS_BANNER_FIRST_APPEARANCE_SEEN): (set())}, 
                  PERSONAL_MISSION_3: {(PersonalMission3.INTRO): False, 
                                       (PersonalMission3.INTRO_OP_8): False, 
                                       (PersonalMission3.INTRO_OP_9): False, 
                                       (PersonalMission3.INTRO_OP_10): False, 
                                       (PersonalMission3.PM_BANNER_ANIMATION_KEY): False, 
                                       (PersonalMission3.CHECKED_PM3_POINTS): 0, 
                                       (PersonalMission3.PART_NO): 0}, 
                  NATIONS_VISITED: (set()), 
                  OPEN_BUNDLE_ENTRY_POINT_SHOWN: (set()), 
                  OPEN_BUNDLE_ENTRY_POINT_ANIMATION_SHOWN: (set()), 
                  OPEN_BUNDLE_INTRO_SHOWN: (set()), 
                  (StrongholdEvent.SETTINGS): {}, (PetSystem.SETTINGS): {(PetSystem.SEEN_PET_NAME_IDS): (set()), 
                                         (PetSystem.SEEN_PET_LEVELS): {}, (PetSystem.SEEN_IN_STORAGE_PET_IDS): (set()), 
                                         (PetSystem.SEEN_PROMO_PET_IDS): (set())}, 
                  (ChallengesMissions.SETTINGS): {(ChallengesMissions.CHALLENGES_BUNDLE_SHOWN): False, 
                                                  (ChallengesMissions.CHALLENGES_BUNDLE_ANIMATION_SHOWN): False, 
                                                  (ChallengesMissions.CHALLENGES_INFO_SHOWN): False, 
                                                  (ChallengesMissions.VISITED_CHALLENGES): (set())}, 
                  HANGAR_VIEW_SETTINGS: {b'allVehicles': {b'crewEnabled': True, 
                                                          b'ttcEnabled': True}}, 
                  HANGAR_KEY_BINDINGS: {b'vehicleMenu': {}}, (ArmorInspector.SETTINGS): {(ArmorInspector.SELECTED_MODE): b'nominal'}}, 
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
                  NEW_SHOP_TABS: {IS_COMP7_BONS_BANNER_VISITED: False}, 
                  VPP_ENTRY_POINT_LAST_SEEN_STEP: {}, LIVE_OPS_WEB_EVENTS_COUNTERS: {}, VEHICLE_CAROUSEL_COUNTERS_SEEN: {}}, 
   KEY_NOTIFICATIONS: {ELEN_NOTIFICATIONS: {(MISSIONS_CONSTANTS.ELEN_EVENT_STARTED_NOTIFICATION): (set()), 
                                            (MISSIONS_CONSTANTS.ELEN_EVENT_FINISHED_NOTIFICATION): (set()), 
                                            (MISSIONS_CONSTANTS.ELEN_EVENT_TAB_VISITED): (set())}, 
                       RECRUITS_NOTIFICATIONS: {}, PROGRESSIVE_REWARD_VISITED: False, 
                       VIEWED_OFFERS: (set()), 
                       OFFERS_DISABLED_MSG_SEEN: False, 
                       BLUEPRINTS_CONVERT_SALE_STARTED_SEEN: False, 
                       CLAN_NEWS_SEEN: False, 
                       SENIORITY_AWARDS_COINS_REMINDER_SHOWN_TIMESTAMP: None, 
                       ACHIEVEMENTS_VISITED: False, 
                       INTEGRATED_AUCTION_NOTIFICATIONS: {AUCTION_STAGE_START_SEEN: (set()), 
                                                          AUCTION_FINISH_STAGE_SEEN: (set())}, 
                       FUN_RANDOM_NOTIFICATIONS: {FUN_RANDOM_NOTIFICATIONS_FROZEN: (set()), 
                                                  FUN_RANDOM_NOTIFICATIONS_PROGRESSIONS: (set()), 
                                                  FUN_RANDOM_NOTIFICATIONS_SUB_MODES: (set())}, 
                       (ResourceWell.NOTIFICATIONS): {(ResourceWell.START_SHOWN): (set()), 
                                                      (ResourceWell.END_SHOWN): (set())}, 
                       COLLECTIONS_NOTIFICATIONS: {COLLECTION_START_SEEN: [], COLLECTION_RENEW_SEEN: {}, COLLECTIONS_UPDATED_ENTRY_SEEN: False}, 
                       COMP7_BOND_EQUIPMENT_REMINDER_SHOWN_TIMESTAMP: None, 
                       COMP7_LAST_SEASON_WITH_SEEN_REWARD: None, 
                       COMP7_LAST_MASKOT_WITH_SEEN_REWARD: None, 
                       OPEN_BUNDLE_NOTIFICATIONS: {OPEN_BUNDLE_START_SHOWN: (set()), 
                                                   OPEN_BUNDLE_REMINDER_SHOWN: (set())}, 
                       CHALLENGES_START_SEEN_NOTIFICATION: (set()), 
                       CHALLENGES_REMINDER_SEEN_NOTIFICATION: (set())}, 
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
                          OVERRIDEN_HEADER_COUNTER_ACTION_ALIASES: (set()), 
                          SELECT_VEHICLES_CAROUSEL_FILTER_1: {b'ussr': False, 
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
                                                              b'favorite': False, 
                                                              b'searchNameVehicle': b''}, 
                          SELECT_VEHICLES_PLAYLIST: b'', 
                          SELECT_VEHICLES_IS_ALL_VEHICLES: True, 
                          (ArmorInspector.SESSION_ATTACKING_VEHICLES): {}}, 
   KEY_UI_FLAGS: {COMP7_UI_SECTION: {COMP7_WEEKLY_QUESTS_PAGE_TOKENS_COUNT: 0, 
                                     COMP7_SHOP_SEEN_PRODUCTS: (set()), 
                                     COMP7_LAST_SEASON: None, 
                                     COMP7_WEEKLY_WIDGET_SHOWN_QUEST: {}, COMP7_LAST_SEASON_WHERE_STATISTICS_SHOWN: None, 
                                     COMP7_UMG_PROGRESSION_POINTS_SEEN: 0, 
                                     COMP7_UMG_ENTRY_POINT_SEEN: False, 
                                     COMP7_PROGRESSION_PAGE_C11N_PROGRESS: {}}, 
                  COMP7_LIGHT_UI_SECTION: {COMP7_LIGHT_LAST_SEASON: None, 
                                           COMP7_LIGHT_PROGRESSION_POINTS_SEEN: 0, 
                                           COMP7_LIGHT_UMG_PROGRESSION_POINTS_SEEN: 0, 
                                           COMP7_LIGHT_UMG_SEEN_QUESTS: {}, COMP7_LIGHT_UMG_ENTRY_POINT_SEEN: False}, 
                  INGAME_TOURNAMENT_SECTION: {INGAME_TOURNAMENT_WCI_INTRO_SEEN: False, 
                                              INGAME_TOURNAMENT_OLS_INTRO_SEEN: False}, 
                  BR_UI_SECTION: {BR_PROGRESSION_SEEN_QUESTS: {}, BR_PROGRESSION_POINTS_SEEN: 0}, 
                  COLLECTIONS_SECTION: {COLLECTION_SHOWN_NEW_REWARDS: {}, COLLECTION_SHOWN_NEW_ITEMS: {}, COLLECTION_SHOWN_NEW_ITEMS_COUNT: {}, COLLECTION_TUTORIAL_COMPLETED: (set()), 
                                        COLLECTION_WAS_ENABLED: True, 
                                        COLLECTIONS_INTRO_SHOWN: False, 
                                        COLLECTIONS_TAB_SHOWN_IDS: (set()), 
                                        COLLECTIONS_TAB_SHOWN_NEW_ITEMS: {}, SHOWN_COMPLETED_COLLECTIONS: (set()), 
                                        LAST_SHOWN_NEW_COLLECTION: 0, 
                                        LAST_SHOWN_COLLECTION_BALANCE: {}}, 
                  LIVE_OPS_WEB_EVENTS_UI_FLAGS: {}, b'uiSpamVisited_store': False, 
                  b'uiSpamVisited_profile': False, 
                  b'uiSpamVisited_profileHof': False, 
                  b'uiSpamVisited_profileTechniquePage': False, 
                  b'uiSpamVisited_sessionStats': False, 
                  b'uiSpamVisited_blueprintsButton': False, 
                  b'uiSpamVisited_missions': False, 
                  b'uiSpamVisited_MissionsMarathonView': False, 
                  b'uiSpamVisited_PersonalMissionOperations': False, 
                  b'uiSpamVisited_referralButtonCounter': False, 
                  b'uiSpamVisited_AmmunitionPanelHintZoneHint': False, 
                  b'uiSpamVisited_CustomizationProgressionViewHint': False, 
                  b'uiSpamVisited_TechTreeEvent': False, 
                  b'uiSpamVisited_DogTagHangarHint': False, 
                  b'uiSpamVisited_ModeSelectorWidgetsBtnHint': False, 
                  b'uiSpamVisited_PersonalReservesHangarHint': False, 
                  b'uiSpamVisited_ModernizedSetupTabHint': False, 
                  b'uiSpamVisited_OfferBannerWindow': False, 
                  b'uiSpamVisited_StrongholdView': False, 
                  EXCHANGE_GOLD_RATE_DISCOUNT_ANIMATION_SHOWED: (set()), 
                  EXCHANGE_XP_RATE_DISCOUNT_ANIMATION_SHOWED: (set()), 
                  VEH_SKILL_TREE_HINT_SHOWN: {}, VEH_SKILL_TREE_POPUP_SHOWN: (set()), 
                  VEH_SKILL_TREE_RECORDED_NOFITICATION_NODE: {}, VEH_SKILL_TREE_PRESTIGE_GLARE_SHOWN: (set()), 
                  VEH_SKILL_TREE_INTRO_SHOWN: False}, 
   KEY_BATTLE_HINTS: {}, KEY_NEWBIE_HINTS: {}}

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
    version = 101
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
                            if presentMode in legacyToNewMode:
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
                        if b'potapov' in quests:
                            newVersion = quests.pop(b'potapov')
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
                from gui.impl.lobby.common.main_menu_utils import TABS
                for key, section in _filterAccountSection(ads):
                    accSettings = AccountSettings._readSection(section, KEY_COUNTERS)
                    if NEW_LOBBY_TAB_COUNTER in accSettings.keys():
                        counters = _unpack(accSettings[NEW_LOBBY_TAB_COUNTER].asString)
                        if TABS.PERSONAL_MISSIONS in counters:
                            counters[TABS.PERSONAL_MISSIONS] = True
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
                    if IS_BATTLE_PASS_EXTRA_START_NOTIFICATION_SEEN in keySettings.keys():
                        keySettings.write(IS_BATTLE_PASS_EXTRA_START_NOTIFICATION_SEEN, _pack(False))

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
                     ResourceWell.START_SHOWN, ResourceWell.END_SHOWN)
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
                obsoleteKeys = [b'isEntryPointsEnabled', b'isTankRentalEnabled', b'isFreeDirectivesEnabled', b'rentPendingVehCD']
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
                    if CREW_SKINS_VIEWED in accSettings.keys():
                        accSettings.deleteSection(CREW_SKINS_VIEWED)

            if currVersion < 68:
                for key, section in _filterAccountSection(ads):
                    keySettings = AccountSettings._readSection(section, KEY_NOTIFICATIONS)
                    if SENIORITY_AWARDS_COINS_REMINDER_SHOWN_TIMESTAMP in keySettings.keys():
                        keySettings.write(SENIORITY_AWARDS_COINS_REMINDER_SHOWN_TIMESTAMP, _pack(None))

            if currVersion < 69:
                pass
            if currVersion < 70:
                pass
            if currVersion < 71:
                isZeroVersion = currVersion is 0
                for key, section in _filterAccountSection(ads):
                    accSettings = AccountSettings._readSection(section, KEY_SETTINGS)
                    panelSettingsExist = b'players_panel' in accSettings.keys()
                    if not isZeroVersion:
                        panelSettings = _unpack(accSettings[b'players_panel'].asString) if panelSettingsExist else DEFAULT_VALUES[KEY_SETTINGS][b'players_panel']
                        panelSettings[b'state'] = panelSettings.get(b'state')
                        if panelSettings[b'state'] is None:
                            panelSettings[b'state'] = 2
                        accSettings.write(b'players_panel', _pack(panelSettings))

            if currVersion < 72:
                for key, section in _filterAccountSection(ads):
                    accFilters = AccountSettings._readSection(section, KEY_FILTERS)
                    obsoleteKey = b'barracks_filter'
                    if obsoleteKey in accFilters.keys():
                        accFilters.deleteSection(obsoleteKey)

            if currVersion < 73:
                oldShowPersonalReservesKey = b'shownPersonalReserves'
                for _, section in _filterAccountSection(ads):
                    accSettings = AccountSettings._readSection(section, KEY_SETTINGS)
                    if oldShowPersonalReservesKey in accSettings.keys():
                        accSettings.deleteSection(oldShowPersonalReservesKey)

            if currVersion < 74:
                for key, section in _filterAccountSection(ads):
                    counterSettings = AccountSettings._readSection(section, KEY_COUNTERS)
                    if counterSettings.has_key(CLAN_NOTIFICATION_COUNTERS):
                        clanNotificationCounters = _unpack(counterSettings[CLAN_NOTIFICATION_COUNTERS].asString)
                        if b'wgcq_hangar_bubble' in clanNotificationCounters:
                            clanNotificationCounters.pop(b'wgcq_hangar_bubble')
                            counterSettings.write(CLAN_NOTIFICATION_COUNTERS, _pack(clanNotificationCounters))

            if currVersion < 75:
                for _, section in _filterAccountSection(ads):
                    accSettings = AccountSettings._readSection(section, KEY_SETTINGS)
                    if WOT_PLUS in accSettings.keys():
                        wotPlusSettings = _unpack(accSettings[WOT_PLUS].asString)
                        wotPlusSettings[b'isOnboardingShown'] = False
                        accSettings.write(WOT_PLUS, _pack(wotPlusSettings))
                    if b'shownWotPlusIntro' in accSettings.keys():
                        accSettings.write(b'shownWotPlusIntro', _pack(False))

            if currVersion < 76:
                pass
            if currVersion < 77:
                for key, section in _filterAccountSection(ads):
                    accSettings = AccountSettings._readSection(section, KEY_SETTINGS)
                    defaultSorting = DEFAULT_VALUES[KEY_SETTINGS][b'statsSortingFunRandom'].copy()
                    accSettings.write(b'statsSortingFunRandom', _pack(defaultSorting))

            if currVersion < 78:
                for _, section in _filterAccountSection(ads):
                    accSettings = AccountSettings._readSection(section, KEY_SETTINGS)
                    if ROYALE_INTRO_VIDEO_SHOWN in accSettings.keys():
                        accSettings.deleteSection(ROYALE_INTRO_VIDEO_SHOWN)

            if currVersion < 79:
                for key, section in _filterAccountSection(ads):
                    keySettings = AccountSettings._readSection(section, KEY_SETTINGS)
                    if MAPBOX_HINT_SECTION in keySettings.keys():
                        keySettings.write(MAPBOX_HINT_SECTION, _pack({}))

            if currVersion < 80:
                for key, section in _filterAccountSection(ads):
                    hintsSection = AccountSettings._readSection(section, KEY_BATTLE_HINTS)
                    if b'lastDisplayTime' in hintsSection.keys():
                        displayHistory = {b'lastDisplayTime': {}, b'totalDisplayCount': {}}
                        hintsDisplayTime = _unpack(hintsSection[b'lastDisplayTime'].asString)
                        for hintID, lastDisplayTime in hintsDisplayTime.iteritems():
                            displayHistory[b'lastDisplayTime'][hintID] = lastDisplayTime

                        hintsSection.write(b'displayHistory', _pack(displayHistory))

            if currVersion < 81:
                pass
            if currVersion < 82:
                for key, section in _filterAccountSection(ads):
                    accSettings = AccountSettings._readSection(section, KEY_COUNTERS)
                    if accSettings.has_key(NEW_SHOP_TABS):
                        counters = _unpack(accSettings[NEW_SHOP_TABS].asString)
                        if IS_COMP7_BONS_BANNER_VISITED not in counters:
                            counters[IS_COMP7_BONS_BANNER_VISITED] = False
                        if b'isCollectibleVehiclesVisited' in counters:
                            del counters[b'isCollectibleVehiclesVisited']
                        accSettings.write(NEW_SHOP_TABS, _pack(counters))

            if currVersion < 83:
                for key, section in _filterAccountSection(ads):
                    keySettings = AccountSettings._readSection(section, KEY_SETTINGS)
                    if b'shownOptionalDevicesAssistantHint' in keySettings.keys():
                        keySettings.deleteSection(b'shownOptionalDevicesAssistantHint')

            if currVersion < 84:
                for key, section in _filterAccountSection(ads):
                    accSettings = AccountSettings._readSection(section, KEY_SETTINGS)
                    easyTankEquipKey = EasyTankEquip.EASY_TANK_EQUIP_SETTINGS
                    easyTankEquipSettings = DEFAULT_VALUES[KEY_SETTINGS][easyTankEquipKey].copy()
                    accSettings.write(easyTankEquipKey, _pack(easyTankEquipSettings))

            if currVersion < 85:
                for key, section in _filterAccountSection(ads):
                    keySettings = AccountSettings._readSection(section, KEY_SETTINGS)
                    if LOOTBOX_SYSTEM in keySettings.keys():
                        keySettings.write(LOOTBOX_SYSTEM, _pack({}))

            if currVersion < 86:
                for key, section in _filterAccountSection(ads):
                    notifications = AccountSettings._readSection(section, KEY_NOTIFICATIONS)
                    if b'story_mode_dday' in notifications.keys():
                        notifications.deleteSection(b'story_mode_dday')

            if currVersion < 87:
                for key, section in _filterAccountSection(ads):
                    notifications = AccountSettings._readSection(section, KEY_NOTIFICATIONS)
                    if b'recruitNotifications' in notifications.keys():
                        notifications.deleteSection(b'recruitNotifications')

            if currVersion < 88:
                for key, section in _filterAccountSection(ads):
                    keySettings = AccountSettings._readSection(section, KEY_SETTINGS)
                    if IS_BATTLE_PASS_EXTRA_START_NOTIFICATION_SEEN in keySettings.keys():
                        keySettings.write(IS_BATTLE_PASS_EXTRA_START_NOTIFICATION_SEEN, _pack(set()))
                    keySettings.write(BUY_ANIMATIONS_WAS_SHOWN, _pack(set()))
                    keySettings.write(EXTRA_CHAPTERS_VIDEO_SHOWN, _pack(set()))

            if currVersion < 89:
                instance = CommandMapping.g_instance
                commandName = instance.getName(CommandMapping.CMD_TOGGLE_ARMOR_FLASHLIGHT)
                defaultKeyCode = instance.getDefaults().get(CommandMapping.CMD_TOGGLE_ARMOR_FLASHLIGHT, Keys.KEY_NONE)
                if defaultKeyCode != Keys.KEY_NONE:
                    keyValues = Keys.__dict__.values()
                    if defaultKeyCode in keyValues:
                        defaultKeyName = Keys.__dict__.keys()[keyValues.index(defaultKeyCode)]
                        AccountSettings.rebindKey(defaultKeyName, commandName)
                        instance.restoreUserConfig()
                for _, section in _filterAccountSection(ads):
                    accSettings = AccountSettings._readSection(section, KEY_SETTINGS)
                    if WOT_PLUS in accSettings.keys():
                        wotPlusSettings = _unpack(accSettings[WOT_PLUS].asString)
                        wotPlusSettings.pop(b'isOnboardingShown', None)
                        accSettings.write(WOT_PLUS, _pack(wotPlusSettings))
                    if b'shownWotPlusIntro' in accSettings.keys():
                        accSettings.deleteSection(b'shownWotPlusIntro')
                        accSettings.deleteSection(b'optionalDevicesAssistantHintShown')

            if currVersion < 90:
                for key, section in _filterAccountSection(ads):
                    UISettings = AccountSettings._readSection(section, KEY_UI_FLAGS)
                    obsoleteKeys = (b'comp7WeeklyQuestWidgetProgress', b'comp7WeeklyQuestInWidgetID', b'comp7WeeklyQuestInWidgetState')
                    if COMP7_UI_SECTION in UISettings.keys():
                        for sectionName in obsoleteKeys:
                            if sectionName in UISettings.keys():
                                UISettings.deleteSection(sectionName)

            if currVersion < 91:
                for key, section in _filterAccountSection(ads):
                    accSettings = AccountSettings._readSection(section, KEY_SETTINGS)
                    obsoleteKeys = (b'comp7LightIntroShown', b'comp7LightProgressionPointsSeen')
                    for sectionName in obsoleteKeys:
                        if sectionName in accSettings.keys():
                            accSettings.deleteSection(sectionName)

            if currVersion < 92:
                for key, section in _filterAccountSection(ads):
                    keySettings = AccountSettings._readSection(section, KEY_UI_FLAGS)
                    if COMP7_UI_SECTION in keySettings.keys():
                        keySettings.write(COMP7_WEEKLY_WIDGET_SHOWN_QUEST, _pack(None))

            if currVersion < 93:
                for key, section in _filterAccountSection(ads):
                    UiSettings = AccountSettings._readSection(section, KEY_UI_FLAGS)
                    if UiSettings.has_key(COMP7_UI_SECTION):
                        comp7UiSection = _unpack(UiSettings[COMP7_UI_SECTION].asString)
                        comp7UiSection[COMP7_LAST_SEASON] = comp7UiSection.get(COMP7_LAST_SEASON)
                        comp7UiSection[COMP7_LAST_SEASON_WHERE_STATISTICS_SHOWN] = comp7UiSection.get(COMP7_LAST_SEASON_WHERE_STATISTICS_SHOWN)
                        comp7UiSection[COMP7_SHOP_SEEN_PRODUCTS] = set(comp7UiSection.get(COMP7_SHOP_SEEN_PRODUCTS, ()))
                        UiSettings.write(COMP7_UI_SECTION, _pack(comp7UiSection))

            if currVersion < 94:
                for key, section in _filterAccountSection(ads):
                    UiSettings = AccountSettings._readSection(section, KEY_UI_FLAGS)
                    if UiSettings.has_key(COMP7_LIGHT_UI_SECTION):
                        comp7LightUiSection = _unpack(UiSettings[COMP7_LIGHT_UI_SECTION].asString)
                        comp7LightUiSection[COMP7_LIGHT_UMG_PROGRESSION_POINTS_SEEN] = comp7LightUiSection.get(COMP7_LIGHT_UMG_PROGRESSION_POINTS_SEEN)
                        comp7LightUiSection[COMP7_LIGHT_UMG_SEEN_QUESTS] = comp7LightUiSection.get(COMP7_LIGHT_UMG_SEEN_QUESTS, {})
                        UiSettings.write(COMP7_LIGHT_UI_SECTION, _pack(comp7LightUiSection))
                    if COMP7_UI_SECTION in UiSettings.keys():
                        UiSettings.write(COMP7_UMG_PROGRESSION_POINTS_SEEN, 0)

            if currVersion < 95:
                flFilters = (EPICBATTLE_CAROUSEL_FILTER_CLIENT_2, EPICBATTLE_CAROUSEL_FILTER_CLIENT_1)
                for key, section in _filterAccountSection(ads):
                    filtersSection = AccountSettings._readSection(section, KEY_FILTERS)
                    for filterKey in filtersSection.keys():
                        if filterKey in flFilters:
                            data = _unpack(filtersSection[filterKey].asString)
                            if b'epicBattleSeason' in data:
                                data.pop(b'epicBattleSeason', None)
                                filtersSection.write(filterKey, _pack(data))

                for _, section in _filterAccountSection(ads):
                    accSettings = AccountSettings._readSection(section, KEY_SETTINGS)
                    if NEW_SETTINGS_COUNTER in accSettings.keys():
                        newSettingsCounters = _unpack(accSettings[NEW_SETTINGS_COUNTER].asString)
                        newSettingsCounters[b'ControlsSettings'].update({b'specialAbility': True})
                        accSettings.write(NEW_SETTINGS_COUNTER, _pack(newSettingsCounters))
                    AccountSettings.clearKeyAndSetNewCommand(b'CMD_CM_SPECIAL_ABILITY', b'KEY_E')
                    CommandMapping.g_instance.restoreUserConfig()
                    bmKey = BattleMatters.BATTLE_MATTERS_SETTINGS
                    if bmKey in accSettings.keys():
                        bmAccSettings = _unpack(accSettings[bmKey].asString)
                        bmAccSettings.update({(BattleMatters.BATTLES_COUNT_WITHOUT_PROGRESS): 0, 
                           (BattleMatters.QUEST_IDX_FOR_LAST_UPDATED_PROGRESS): 0, 
                           (BattleMatters.LAST_QUEST_PROGRESS): 0, 
                           (BattleMatters.REMINDER_LAST_DISPLAY_TIME): 0, 
                           (BattleMatters.LAST_BATTLE_TIME): 0})
                        accSettings.write(bmKey, _pack(bmAccSettings))

            if currVersion < 96:
                for key, section in _filterAccountSection(ads):
                    keySettings = AccountSettings._readSection(section, KEY_SETTINGS)
                    adventCalendarDefaultSection = DEFAULT_VALUES[KEY_SETTINGS][AdventCalendar.SETTINGS].copy()
                    keySettings.write(AdventCalendar.SETTINGS, _pack(adventCalendarDefaultSection))

            if currVersion < 97:
                for key, section in _filterAccountSection(ads):
                    uiSettings = AccountSettings._readSection(section, KEY_UI_FLAGS)
                    ingameTournamentFlags = {INGAME_TOURNAMENT_WCI_INTRO_SEEN: False, 
                       INGAME_TOURNAMENT_OLS_INTRO_SEEN: False}
                    uiSettings.write(INGAME_TOURNAMENT_SECTION, _pack(ingameTournamentFlags))

            if currVersion < 97:
                for key, section in _filterAccountSection(ads):
                    accSettings = AccountSettings._readSection(section, KEY_SETTINGS)
                    obsoleteKey = b'lowQualitySound'
                    if obsoleteKey in accSettings.keys():
                        accSettings.deleteSection(obsoleteKey)

            if currVersion < 98:
                pass
            if currVersion < 99:
                pass
            if currVersion < 100:
                for key, section in _filterAccountSection(ads):
                    notifications = AccountSettings._readSection(section, KEY_NOTIFICATIONS)
                    notifications.deleteSection(b'story_mode_vday')
                    notifications.deleteSection(b'story_mode_scc')

                for _, section in _filterAccountSection(ads):
                    keyUIFlagsSettings = AccountSettings._readSection(section, KEY_UI_FLAGS)
                    if keyUIFlagsSettings.has_key(b'grinch_progression_keys'):
                        keyUIFlagsSettings.deleteSection(b'grinch_progression_keys')
                    accSettings = AccountSettings._readSection(section, KEY_SETTINGS)
                    if accSettings.has_key(b'grinch_keys'):
                        accSettings.deleteSection(b'grinch_keys')
                    if accSettings.has_key(b'grinch_progression_key'):
                        accSettings.deleteSection(b'grinch_progression_key')

            if currVersion < 101:
                for key, section in _filterAccountSection(ads):
                    uiSettings = AccountSettings._readSection(section, KEY_UI_FLAGS)
                    if uiSettings.has_key(COMP7_LIGHT_UI_SECTION):
                        uiSettings.deleteSection(COMP7_LIGHT_UI_SECTION)

            ads.writeInt(b'version', AccountSettings.version)
        return

    @staticmethod
    def getFilterDefault(name):
        return DEFAULT_VALUES[KEY_FILTERS].get(name, None)

    @staticmethod
    def getNotificationDefault(name):
        return DEFAULT_VALUES[KEY_NOTIFICATIONS].get(name, None)

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
    def rebindKey(key, newCommand):
        cmSection = AccountSettings._readSection(Settings.g_instance.userPrefs, Settings.KEY_COMMAND_MAPPING)
        for command, section in cmSection.items()[:]:
            fireKey = AccountSettings._readSection(section, b'fireKey').asString
            if command == newCommand:
                cmSection.deleteSection(command)
                newSection = cmSection.createSection(command)
                newSection.writeString(b'fireKey', key)
            elif fireKey == key:
                cmSection.deleteSection(command)
                newSection = cmSection.createSection(command)
                newSection.writeString(b'fireKey', b'KEY_NONE')

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
    def clearKeyAndSetNewCommand(newCommand, commandKey):
        cmSection = AccountSettings._readSection(Settings.g_instance.userPrefs, Settings.KEY_COMMAND_MAPPING)
        for command, section in cmSection.items()[:]:
            fireKey = AccountSettings._readSection(section, b'fireKey').asString
            if fireKey == commandKey:
                if command != newCommand:
                    cmSection.deleteSection(command)
                    newSection = cmSection.createSection(command)
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
    def getNotifications(name, default=None):
        return AccountSettings._getValue(name, KEY_NOTIFICATIONS, default=default)

    @staticmethod
    def setNotifications(name, value, force=False):
        AccountSettings._setValue(name, value, KEY_NOTIFICATIONS, force=force)
        return

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

    @classmethod
    def getNewbieHints(cls, name, default=None):
        return cls._getValue(name, KEY_NEWBIE_HINTS, force=True, default=default)

    @classmethod
    def setNewbieHints(cls, name, value, default=None):
        return cls._setValue(name, value, KEY_NEWBIE_HINTS, force=True, default=default)

    @classmethod
    def getBattleHints(cls, name, default=None):
        return cls._getValue(name, KEY_BATTLE_HINTS, force=True, default=default)

    @classmethod
    def setBattleHints(cls, name, value, default=None):
        return cls._setValue(name, value, KEY_BATTLE_HINTS, force=True, default=default)

    @classmethod
    def getVehicleViewedModules(cls, vehIntCD):
        viewedModules = cls.getUIFlag(VIEWED_MODULES_SECTION)
        if viewedModules:
            return viewedModules.get(vehIntCD, None)
        else:
            return

    @classmethod
    def setVehicleViewedModules(cls, vehIntCD, modules):
        viewedModules = cls.getUIFlag(VIEWED_MODULES_SECTION)
        if viewedModules is None:
            viewedModules = {}
        viewedModules.update({vehIntCD: modules})
        cls.setUIFlag(VIEWED_MODULES_SECTION, viewedModules)
        return

    @classmethod
    def clearVehicleViewedModules(cls, vehIntCD):
        viewedModules = cls.getUIFlag(VIEWED_MODULES_SECTION)
        if viewedModules is not None and vehIntCD in viewedModules:
            del viewedModules[vehIntCD]
        cls.setUIFlag(VIEWED_MODULES_SECTION, viewedModules)
        return

    @classmethod
    def isVersionedRuleCompleted(cls, ruleID):
        versionedRules = cls.getUIFlag(LIMITED_UI_VERSIONED_RULES)
        if versionedRules:
            return ruleID in versionedRules
        return False

    @classmethod
    def getCompletedVersionedRules(cls):
        return cls.getUIFlag(LIMITED_UI_VERSIONED_RULES)

    @classmethod
    def completeVersionedRules(cls, ruleIDs):
        versionedRules = cls.getUIFlag(LIMITED_UI_VERSIONED_RULES)
        if versionedRules is None:
            versionedRules = []
        versionedRules = list(set(ruleIDs + versionedRules))
        cls.setUIFlag(LIMITED_UI_VERSIONED_RULES, versionedRules)
        return

    @classmethod
    def clearVersionedRules(cls, ruleIDs):
        versionedRules = cls.getUIFlag(LIMITED_UI_VERSIONED_RULES)
        if versionedRules is None:
            return
        else:
            for ruleID in ruleIDs:
                if ruleID in versionedRules:
                    versionedRules.remove(ruleID)

            cls.setUIFlag(LIMITED_UI_VERSIONED_RULES, versionedRules)
            return

    @staticmethod
    def _getValue(name, setting, force=False, default=None):
        fds = AccountSettings._readSection(AccountSettings._readUserSection(), setting)
        try:
            if fds.has_key(name):
                return pickle.loads(base64.b64decode(fds.readString(name)))
        except Exception:
            if constants.IS_DEVELOPMENT:
                LOG_CURRENT_EXCEPTION()

        if name in DEFAULT_VALUES[setting]:
            return copy.deepcopy(DEFAULT_VALUES[setting][name])
        return default

    @staticmethod
    def _setValue(name, value, setting, force=False, default=None):
        if name not in DEFAULT_VALUES[setting] and not force:
            raise SoftException((b'Default value "{}" is not found in "{}"').format(name, type))
        if AccountSettings._getValue(name, setting, force, default=default) != value:
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
