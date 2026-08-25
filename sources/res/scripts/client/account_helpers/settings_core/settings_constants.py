from shared_utils import CONST_CONTAINER
VERSION = b'VERSION'
POST_PROCESSING_QUALITY = b'POST_PROCESSING_QUALITY'

class GRAPHICS(CONST_CONTAINER):
    MONITOR = b'monitor'
    VIDEO_MODE = b'screenMode'
    WINDOW_MODE = b'windowMode'
    WINDOW_SIZE = b'windowSize'
    RESOLUTION = b'resolution'
    BORDERLESS_SIZE = b'borderlessSize'
    REFRESH_RATE = b'refreshRate'
    GAMMA_SETTING = b'gammaSetting'
    NATIVE_RESOLUTION = b'nativeResolution'
    VERTICAL_SYNC = b'vertSync'
    TRIPLE_BUFFERED = b'tripleBuffered'
    IGB_HARDWARE_ACCELERATION = b'igbHardwareAcceleration'
    COLOR_BLIND = b'isColorBlind'
    GRAPHICS_QUALITY_HD_SD = b'graphicsQualityHDSD'
    GRAPHICS_QUALITY_HD_SD_HIGH = b'graphicsQualityHDSDHigh'
    IS_SD_QUALITY = b'isSDQuality'
    GRAPHICS_SETTINGS_LIST = b'qualityOrder'
    PRESETS = b'presets'
    QUALITY_PRESET = b'graphicsQuality'
    DYNAMIC_RENDERER = b'dynamicRenderer'
    COLOR_FILTER_INTENSITY = b'colorFilterIntensity'
    BRIGHTNESS_CORRECTION = b'brightnessCorrection'
    CONTRAST_CORRECTION = b'contrastCorrection'
    SATURATION_CORRECTON = b'saturationCorrection'
    COLOR_FILTER_SETTING = b'colorFilter'
    COLOR_FILTER_IMAGES = b'colorFilterImages'
    FOV = b'fov'
    DYNAMIC_FOV_ENABLED = b'dynamicFov'
    INTERFACE_SCALE = b'interfaceScale'
    DRR_AUTOSCALER_ENABLED = b'DRR_AUTOSCALER_ENABLED'
    RENDER_PIPELINE = b'RENDER_PIPELINE'
    RENDER_PIPELINE_QUALITY = b'RENDER_PIPELINE_QUALITY'
    TESSELLATION_SUPPORTED = b'tessellationSupported'
    COLOR_GRADING_TECHNIQUE = b'COLOR_GRADING_TECHNIQUE'

    @classmethod
    def getScreenConstants(cls):
        return (
         cls.MONITOR,
         cls.VIDEO_MODE,
         cls.WINDOW_SIZE,
         cls.RESOLUTION,
         cls.BORDERLESS_SIZE,
         cls.REFRESH_RATE,
         cls.DYNAMIC_RENDERER,
         cls.INTERFACE_SCALE)

    @classmethod
    def getColorSettings(cls):
        return (
         cls.COLOR_FILTER_INTENSITY,
         cls.BRIGHTNESS_CORRECTION,
         cls.CONTRAST_CORRECTION,
         cls.COLOR_GRADING_TECHNIQUE,
         cls.SATURATION_CORRECTON)

    @classmethod
    def getCustomColorSettings(cls):
        return (
         cls.BRIGHTNESS_CORRECTION,
         cls.CONTRAST_CORRECTION,
         cls.SATURATION_CORRECTON)


class GAME(CONST_CONTAINER):
    ENABLE_OL_FILTER = b'enableOlFilter'
    ENABLE_SPAM_FILTER = b'enableSpamFilter'
    DATE_TIME_MESSAGE_INDEX = b'datetimeIdx'
    SHOW_DATE_MESSAGE = b'showDateMessage'
    SHOW_TIME_MESSAGE = b'showTimeMessage'
    INVITES_FROM_FRIENDS = b'invitesFromFriendsOnly'
    RECEIVE_CLAN_INVITES_NOTIFICATIONS = b'receiveClanInvitesNotifications'
    RECEIVE_INVITES_IN_BATTLE = b'receiveInvitesInBattle'
    BATTLE_LOADING_INFO = b'battleLoadingInfo'
    BATTLE_LOADING_RANKED_INFO = b'battleLoadingRankedInfo'
    RECEIVE_FRIENDSHIP_REQUEST = b'receiveFriendshipRequest'
    STORE_RECEIVER_IN_BATTLE = b'storeReceiverInBattle'
    DISABLE_BATTLE_CHAT = b'disableBattleChat'
    CHAT_CONTACTS_LIST_ONLY = b'chatContactsListOnly'
    LENS_EFFECT = b'enableOpticalSnpEffect'
    MINIMAP_ALPHA = b'minimapAlpha'
    POSTMORTEM_MODE = b'postmortemMode'
    REPLAY_ENABLED = b'replayEnabled'
    SNIPER_ZOOM = b'sniperZoom'
    PRE_COMMANDER_CAM = b'preCommanderCam'
    COMMANDER_CAM = b'commanderCam'
    HULLLOCK_ENABLED = b'hullLockEnabled'
    SHOW_VEHICLE_HP_IN_PLAYERS_PANEL = b'showVehicleHPinPlayersPanel'
    SHOW_VEHICLE_HP_IN_MINIMAP = b'showVehicleHPinMinimap'
    ENABLE_SERVER_AIM = b'useServerAim'
    SHOW_DAMAGE_ICON = b'showDamageIcon'
    SHOW_VEHICLES_COUNTER = b'showVehiclesCounter'
    SHOW_MARKS_ON_GUN = b'showMarksOnGun'
    ANONYMIZER = b'anonymizer'
    SHOW_VICTIMS_DOGTAG = b'showVictimsDogTag'
    SHOW_DOGTAG_TO_KILLER = b'showDogTagToKiller'
    SHOW_KILLERS_DOGTAG = b'showKillersDogTag'
    SHOW_PERSONAL_ANIMATED_DOGTAG = b'showPersonalAnimatedDogTag'
    DYNAMIC_CAMERA = b'dynamicCamera'
    SNIPER_MODE_STABILIZATION = b'horStabilizationSnp'
    INCREASED_ZOOM = b'increasedZoom'
    SNIPER_MODE_BY_SHIFT = b'sniperModeByShift'
    ENABLE_SPEEDOMETER = b'enableSpeedometer'
    ENABLE_REPAIR_TIMER = b'enableRepairTimer'
    ENABLE_BATTLE_NOTIFIER = b'enableBattleNotifier'
    HANGAR_CAM_PERIOD = b'hangarCamPeriod'
    HANGAR_CAM_PARALLAX_ENABLED = b'hangarCamParallaxEnabled'
    PLAYERS_PANELS_SHOW_LEVELS = b'ppShowLevels'
    PLAYERS_PANELS_SHOW_TYPES = b'ppShowTypes'
    PLAYERS_PANELS_STATE = b'ppState'
    EPIC_RANDOM_PLAYERS_PANELS_STATE = b'epicppState'
    GAMEPLAY_MASK = b'gameplayMask'
    GAMEPLAY_CTF = b'gameplay_ctf'
    GAMEPLAY_DEV_MAPS = b'gameplay_devMaps'
    SHOW_VECTOR_ON_MAP = b'showVectorOnMap'
    SHOW_SECTOR_ON_MAP = b'showSectorOnMap'
    SHOW_VEH_MODELS_ON_MAP = b'showVehModelsOnMap'
    SHOW_ARTY_HIT_ON_MAP = b'showArtyHitOnMap'
    MINIMAP_SIZE = b'minimapSize'
    TRAINING_MINIMAP_SIZE = b'mapsTrainingMinimapSize'
    COMP7_MINIMAP_SIZE = b'comp7PrebattleMinimapSize'
    MINIMAP_VIEW_RANGE = b'minimapViewRange'
    MINIMAP_MAX_VIEW_RANGE = b'minimapMaxViewRange'
    MINIMAP_DRAW_RANGE = b'minimapDrawRange'
    MINIMAP_MIN_SPOTTING_RANGE = b'minimapMinSpottingRange'
    SNIPER_MODE_SWINGING_ENABLED = b'SNIPER_MODE_SWINGING_ENABLED'
    CAROUSEL_TYPE = b'carouselType'
    CUSTOMIZATION_DISPLAY_TYPE = b'customizationDisplayType'
    DOUBLE_CAROUSEL_TYPE = b'doubleCarouselType'
    VEHICLE_CAROUSEL_STATS = b'vehicleCarouselStats'
    MINIMAP_ALPHA_ENABLED = b'minimapAlphaEnabled'
    DISPLAY_PLATOON_MEMBERS = b'displayPlatoonMembers'
    LOGIN_SERVER_SELECTION = b'loginServerSelection'
    UNIT_FILTER = b'unitFilter'
    SWITCH_SETUPS_IN_LOADING = b'switchEquipment'
    SCROLL_SMOOTHING = b'scrollSmoothing'
    LIMITED_UI_ACTIVE = b'limitedUIActive'
    NEWBIE_PREBATTLE_HINTS = b'newbiePrebattleHints'
    NEWBIE_BATTLE_HINTS = b'newbieBattleHints'
    W2GT_ENABLE = b'w2gtEnable'


class SOUND(CONST_CONTAINER):
    GAME_EVENT_AMBIENT = b'specialAmbientVolume'
    GAME_EVENT_EFFECTS = b'specialEffectsVolume'
    GAME_EVENT_GUI = b'specialGuiVolume'
    GAME_EVENT_MUSIC = b'specialMusicVolume'
    GAME_EVENT_VEHICLES = b'specialVehiclesVolume'
    GAME_EVENT_VOICE = b'specialVoiceNotificationVolume'
    MASTER_TOGGLE = b'masterVolumeToggle'
    SOUND_QUALITY = b'soundQuality'
    SOUND_QUALITY_VISIBLE = b'soundQualityVisible'
    SUBTITLES = b'subtitles'
    MASTER = b'masterVolume'
    MUSIC = b'musicVolume'
    MUSIC_HANGAR = b'musicHangar'
    VEHICLES = b'vehiclesVolume'
    EFFECTS = b'effectsVolume'
    GUI = b'guiVolume'
    AMBIENT = b'ambientVolume'
    NATIONS_VOICES = b'nationalVoices'
    ALT_VOICES = b'alternativeVoices'
    SOUND_DEVICE = b'soundDevice'
    SOUND_SPEAKERS = b'soundSpeakers'
    VOICE_NOTIFICATION = b'voiceNotificationVolume'
    DETECTION_ALERT_SOUND = b'bulbVoices'
    ARTY_SHOT_ALERT_SOUND = b'artyBulbVoices'
    CAPTURE_DEVICES = b'captureDevice'
    VOIP_ENABLE = b'enableVoIP'
    VOIP_ENABLE_CHANNEL = b'enableVoIPChannel'
    VOIP_MASTER = b'masterVivoxVolume'
    VOIP_MIC = b'micVivoxVolume'
    VOIP_MASTER_FADE = b'masterFadeVivoxVolume'
    VOIP_SUPPORTED = b'voiceChatSupported'
    BASS_BOOST = b'bassBoost'
    NIGHT_MODE = b'nightMode'
    LOW_QUALITY = b'lowQualitySound'
    PHYSICS_QUALITY = b'physicsQuality'


class SoundPhysicsQuality(CONST_CONTAINER):
    DISABLE = b'disabled'
    LOW = b'low'
    MEDIUM = b'medium'
    HIGH = b'high'
    ORDER = (
     HIGH, MEDIUM, LOW, DISABLE)


class CONTROLS(CONST_CONTAINER):
    MOUSE_ARCADE_SENS = b'mouseArcadeSens'
    MOUSE_SNIPER_SENS = b'mouseSniperSens'
    MOUSE_STRATEGIC_SENS = b'mouseStrategicSens'
    MOUSE_ASSIST_AIM_SENS = b'mouseAssistAimSens'
    MOUSE_FREECAM_SENS = b'mouseDeathFreecamSens'
    MOUSE_HORZ_INVERSION = b'mouseHorzInvert'
    MOUSE_VERT_INVERSION = b'mouseVertInvert'
    BACK_DRAFT_INVERSION = b'backDraftInvert'
    KEYBOARD = b'keyboard'
    KEYBOARD_IMPORTANT_BINDS = b'keyboardImportantBinds'


class AIM(CONST_CONTAINER):
    ARCADE = b'arcade'
    SNIPER = b'sniper'
    SPG = b'spg'
    CONTOUR = b'contour'
    ARMOR_FLASHLIGHT = b'armorFlashlight'


class SPGAim(CONST_CONTAINER):
    SHOTS_RESULT_INDICATOR = b'shotsResultIndicator'
    SPG_SCALE_WIDGET = b'spgScaleWidget'
    SPG_STRATEGIC_CAM_MODE = b'spgStrategicCamMode'
    AUTO_CHANGE_AIM_MODE = b'autoChangeAimMode'
    AIM_ENTRANCE_MODE = b'aimEntranceMode'


class CONTOUR(CONST_CONTAINER):
    ENHANCED_CONTOUR = b'contour'
    CONTOUR_PENETRABLE_ZONE = b'contourPenetrableZone'
    CONTOUR_IMPENETRABLE_ZONE = b'contourImpenetrableZone'


class ArmorFlashlight(CONST_CONTAINER):
    ENABLED = b'armorFlashlightEnabled'
    COLOR_SCHEMA = b'armorFlashlightColorSchema'
    FILL = b'armorFlashlightFill'
    OPACITY = b'armorFlashlightOpacity'
    RESOLUTION = b'armorFlashlightResolutionScaling'


class SPGAimEntranceModeOptions(CONST_CONTAINER):
    LAST = b'last'
    STRATEGIC = b'strategic'
    TRAJECTORY = b'trajectory'
    SETTINGS_OPTIONS = [
     LAST,
     STRATEGIC,
     TRAJECTORY]


class MARKERS(CONST_CONTAINER):
    ALLY = b'ally'
    ENEMY = b'enemy'
    DEAD = b'dead'


class FEEDBACK(CONST_CONTAINER):
    DAMAGE_INDICATOR = b'feedbackDamageIndicator'
    DAMAGE_LOG = b'feedbackDamageLog'
    BATTLE_EVENTS = b'feedbackBattleEvents'
    BATTLE_BORDER_MAP = b'feedbackBattleBorderMap'
    QUESTS_PROGRESS = b'feedbackQuestsProgress'


class DAMAGE_INDICATOR(CONST_CONTAINER):
    TYPE = b'damageIndicatorType'
    PRESET_CRITS = b'damageIndicatorCrits'
    PRESET_ALLIES = b'damageIndicatorAllies'
    DAMAGE_VALUE = b'damageIndicatorDamageValue'
    VEHICLE_INFO = b'damageIndicatorVehicleInfo'
    ANIMATION = b'damageIndicatorAnimation'
    DYNAMIC_INDICATOR = b'damageIndicatorDynamicIndicator'


class DAMAGE_LOG(CONST_CONTAINER):
    TOTAL_DAMAGE = b'damageLogTotalDamage'
    BLOCKED_DAMAGE = b'damageLogBlockedDamage'
    ASSIST_DAMAGE = b'damageLogAssistDamage'
    ASSIST_STUN = b'damageLogAssistStun'
    SHOW_DETAILS = b'damageLogShowDetails'
    SHOW_EVENT_TYPES = b'damageLogShowEventTypes'
    EVENT_POSITIONS = b'damageLogEventsPosition'


class BATTLE_EVENTS(CONST_CONTAINER):
    SHOW_IN_BATTLE = b'battleEventsShowInBattle'
    ENEMY_HP_DAMAGE = b'battleEventsEnemyHpDamage'
    ENEMY_BURNING = b'battleEventsEnemyBurning'
    ENEMY_RAM_ATTACK = b'battleEventsEnemyRamAttack'
    BLOCKED_DAMAGE = b'battleEventsBlockedDamage'
    ENEMY_DETECTION_DAMAGE = b'battleEventsEnemyDetectionDamage'
    ENEMY_TRACK_DAMAGE = b'battleEventsEnemyTrackDamage'
    ENEMY_DETECTION = b'battleEventsEnemyDetection'
    ENEMY_KILL = b'battleEventsEnemyKill'
    BASE_CAPTURE_DROP = b'battleEventsBaseCaptureDrop'
    BASE_CAPTURE = b'battleEventsBaseCapture'
    ENEMY_CRITICAL_HIT = b'battleEventsEnemyCriticalHit'
    EVENT_NAME = b'battleEventsEventName'
    VEHICLE_INFO = b'battleEventsVehicleInfo'
    ENEMY_WORLD_COLLISION = b'battleEventsEnemyWorldCollision'
    RECEIVED_DAMAGE = b'battleEventsReceivedDamage'
    RECEIVED_CRITS = b'battleEventsReceivedCrits'
    ENEMY_ASSIST_STUN = b'battleEventsEnemyAssistStun'
    ENEMIES_STUN = b'battleEventsEnemyStun'
    CREW_PERKS = b'battleEventsCrewPerks'


class BATTLE_BORDER_MAP(CONST_CONTAINER):
    MODE_SHOW_BORDER = b'battleBorderMapMode'
    TYPE_BORDER = b'battleBorderMapType'


class QUESTS_PROGRESS(CONST_CONTAINER):
    VIEW_TYPE = b'progressViewType'
    DISPLAY_TYPE = b'progressViewConditions'


class SITUATIONAL_PERKS(CONST_CONTAINER):
    ARMOR_PATCHING = b'armorPatching'
    COMMANDER_EAGLE_EYE = b'commander_eagleEye'
    COMMANDER_EMERGENCY = b'commander_emergency'
    COMMANDER_TUTOR = b'commander_tutor'
    COMMANDER_COORDINATION = b'commander_coordination'
    COMMANDER_HOLD_LINE = b'commander_holdLine'
    COMMANDER_STAY_SHARP = b'commander_staySharp'
    GUNNER_FOCUS = b'gunner_focus'
    GUNNER_LONE_WOLF = b'gunner_loneWolf'
    DRIVER_MOTOR_EXPERT = b'driver_motorExpert'
    DRIVER_SUSPENSION_REPAIR = b'driver_suspensionRepair'
    DRIVER_BULLETPROOF = b'driver_bulletproof'
    LOADER_DESPERADO = b'loader_desperado'
    LOADER_INTUITION = b'loader_intuition'
    LOADER_SECOND_CHANCE = b'loader_secondChance'
    LOADER_MELEE = b'loader_melee'
    RADIOMAN_SIDE_BY_SIDE = b'radioman_sideBySide'
    RADIOMAN_EXPERT = b'radioman_expert'
    RADIOMAN_THREAT_SEARCH = b'radioman_threatSearch'


GROUPS_NOVELTY_SETTINGS = {b'crewPerks': (SITUATIONAL_PERKS.ALL() + (BATTLE_EVENTS.CREW_PERKS,)), 
   b'battleEfficiency': (
                       BATTLE_EVENTS.BASE_CAPTURE_DROP,
                       BATTLE_EVENTS.BASE_CAPTURE,
                       BATTLE_EVENTS.ENEMY_DETECTION,
                       BATTLE_EVENTS.ENEMY_RAM_ATTACK,
                       BATTLE_EVENTS.ENEMY_KILL,
                       BATTLE_EVENTS.ENEMY_TRACK_DAMAGE,
                       BATTLE_EVENTS.ENEMY_CRITICAL_HIT,
                       BATTLE_EVENTS.ENEMY_HP_DAMAGE,
                       BATTLE_EVENTS.ENEMY_WORLD_COLLISION,
                       BATTLE_EVENTS.ENEMY_DETECTION_DAMAGE,
                       BATTLE_EVENTS.ENEMY_ASSIST_STUN,
                       BATTLE_EVENTS.ENEMY_BURNING), 
   b'damage': (
             BATTLE_EVENTS.BLOCKED_DAMAGE,
             BATTLE_EVENTS.RECEIVED_DAMAGE,
             BATTLE_EVENTS.RECEIVED_CRITS)}

class CONTACTS(CONST_CONTAINER):
    SHOW_OFFLINE_USERS = b'showOfflineUsers'
    SHOW_OTHERS_CATEGORY = b'showOthersCategory'
    ANTISPAM_MESSAGES_COUNTER = b'antispamMessagesCounter'


class SETTINGS_GROUP(CONST_CONTAINER):
    GAME_SETTINGS = b'GameSettings'
    GRAPHICS_SETTINGS = b'GraphicSettings'
    SOUND_SETTINGS = b'SoundSettings'
    CONTROLS_SETTINGS = b'ControlsSettings'
    AIM_SETTINGS = b'AimSettings'
    MARKERS_SETTINGS = b'MarkerSettings'
    FEEDBACK_SETTINGS = b'FeedbackSettings'


class GuiSettingsBehavior(CONST_CONTAINER):
    FREE_XP_INFO_DIALOG_SHOWED = b'isFreeXPInfoDialogShowed'
    RANKED_WELCOME_VIEW_SHOWED = b'isRankedWelcomeViewShowed'
    RANKED_WELCOME_VIEW_STARTED = b'isRankedWelcomeViewStarted'
    DISPLAY_PLATOON_MEMBER_CLICKED = b'isDisplayPlatoonMembersClicked'
    VEH_POST_PROGRESSION_UNLOCK_MSG_NEED_SHOW = b'vehPostProgressionUnlockMsgNeedShow'
    BIRTHDAY_CALENDAR_INTRO_SHOWED = b'birthdayCalendarIntroShowed'
    COMP7_YEARLY_ANIMATION_SEEN = b'isComp7YearlyAnimationSeen'
    CREW_PE_WELCOME_SHOWN = b'crewPEWelcomeShown'
    IS_PRESTIGE_ONBOARDING_VIEWED = b'isPrestigeOnboardingViewed'
    PRESTIGE_FIRST_ENTRY_NOTIFICATION_SHOWN = b'prestigeFirstEntryNotificationShown'
    CLAN_SUPPLY_INTRO_SHOWN = b'clanSupplyIntroShown'
    CREW_MENTORING_LICENSE_AWARDS_SHOWN = b'crewMentoringLicenseAwardsShown'
    W2GT_APPLIED = b'w2gtApplied'


class OnceOnlyHints(CONST_CONTAINER):
    FALLOUT_QUESTS_TAB = b'FalloutQuestsTab'
    CUSTOMIZATION_SLOTS_HINT = b'CustomizationSlotsHint'
    SHOP_TRADE_IN_HINT = b'ShopTradeInHint'
    VEH_COMPARE_CONFIG_HINT = b'VehCompareConfigHint'
    HOLD_SHEET_HINT = b'HoldSheetHint'
    HAVE_NEW_BADGE_HINT = b'HaveNewBadgeHint'
    HANGAR_HAVE_NEW_BADGE_HINT = b'HangarHaveNewBadgeHint'
    EPIC_RESERVES_SLOT_HINT = b'EpicReservesSlotHint'
    PAUSE_HINT = b'PauseHint'
    HAVE_NEW_SUFFIX_BADGE_HINT = b'HaveNewSuffixBadgeHint'
    HANGAR_HAVE_NEW_SUFFIX_BADGE_HINT = b'HangarHaveNewSuffixBadgeHint'
    BADGE_PAGE_NEW_SUFFIX_BADGE_HINT = b'BadgePageNewSuffixBadgeHint'
    C11N_AUTOPROLONGATION_HINT = b'CustomizationAutoprolongationHint'
    C11N_EDITABLE_STYLE_SLOT_HINT = b'C11nEditableStyleSlotHint'
    C11N_EDITABLE_STYLE_SLOT_BUTTON_HINT = b'C11nEditableStyleSlotButtonHint'
    C11N_PROGRESSION_REQUIRED_STYLE_SLOT_HINT = b'C11nProgressionRequiredStyleSlotHint'
    C11N_PROGRESSION_REQUIRED_STYLE_SLOT_BUTTON_HINT = b'C11nProgressionRequiredStyleSlotButtonHint'
    BLUEPRINTS_SWITCHBUTTON_HINT = b'BlueprintsSwitchButtonHint'
    BLUEPRINTS_RESEARCH_BUTTON_HINT = b'BlueprintsResearchButtonHint'
    BLUEPRINTS_TECHTREE_CONVERT_BUTTON_HINT = b'BlueprintsTechtreeConvertButtonHint'
    BLUEPRINTS_RESEARCH_CONVERT_BUTTON_HINT = b'BlueprintsResearchConvertButtonHint'
    BLUEPRINT_SCREEN_CONVERT_FRAGMENT_HINT = b'BlueprintScreenConvertFragmentHint'
    ACCOUNT_BUTTON_HINT = b'AccountButtonHint'
    SESSION_STATS_OPEN_BTN_HINT = b'SessionStatsOpenBtnHint'
    SESSION_STATS_SETTINGS_BTN_HINT = b'SessionStatsSettingsBtnHint'
    BATTLE_SESSION_UP_BUTTON_TOURNAMENT_HINT = b'BattleSessionUpButtonTournamentHint'
    CREW_OPERATION_BTN_HINT = b'CrewOperationBtnHint'
    SOUND_BUTTONEX_HINT = b'SoundButtonExHint'
    VEHICLE_PREVIEW_MODULES_BUTTON_HINT = b'VehiclePreviewModulesButtonHint'
    PLATOON_BTN_HINT = b'PlatoonBtnHint'
    AMMUNITION_FILTER_HINT = b'FilterHintZoneHint'
    MODERNIZED_SETUP_TAB_HINT = b'ModernizedSetupTabHint'
    OPT_DEV_DRAG_AND_DROP_HINT = b'OptDevDragAndDropHint'
    HANGAR_MANUAL_HINT = b'HangarManualHint'
    DOGTAG_HANGAR_HINT = b'DogTagHangarHint'
    DOGTAG_PROFILE_HINT = b'DogTagProfileHint'
    ANIMATED_DOGTAG_HANGAR_HINT = b'AnimatedDogTagHangarHint'
    ANIMATED_DOGTAG_PROFILE_HINT = b'AnimatedDogTagProfileHint'
    WOTPLUS_HANGAR_HINT = b'WotPlusHangarHint'
    WOTPLUS_PROFILE_HINT = b'WotPlusProfileHint'
    MODE_SELECTOR_WIDGETS_BTN_HINT = b'ModeSelectorWidgetsBtnHint'
    MAPS_TRAINING_NEWBIE_HINT = b'MapsTrainingNewbieHint'
    VEHICLE_PREVIEW_POST_PROGRESSION_BUTTON_HINT = b'VehiclePreviewPostProgressionButtonHint'
    VEHICLE_POST_PROGRESSION_ENTRY_POINT_HINT = b'VehiclePostProgressionEntryPointHint'
    RESEARCH_POST_PROGRESSION_ENTRY_POINT_HINT = b'ResearchPostProgressionEntryPointHint'
    HERO_VEHICLE_POST_PROGRESSION_ENTRY_POINT_HINT = b'HeroVehiclePreviewPostProgressionButtonHint'
    SWITCH_EQUIPMENT_AUXILIARY_LOADOUT_HINT = b'SwitchEquipmentAuxiliaryLoadoutHint'
    SWITCH_EQUIPMENT_ESSENTIALS_LOADOUT_HINT = b'SwitchEquipmentEssentialsLoadoutHint'
    COMPARE_MODIFICATIONS_PANEL_HINT = b'CompareModificationsPanelHint'
    COMPARE_SPECIALIZATION_BUTTON_HINT = b'CompareSpecializationButtonHint'
    TRADE_IN_VEHICLE_POST_PROGRESSION_ENTRY_POINT_HINT = b'TradeInVehiclePreviewPostProgressionButtonHint'
    PERSONAL_TRADE_IN_VEHICLE_POST_PROGRESSION_ENTRY_POINT_HINT = b'PersonalTradeInVehiclePreviewPostProgressionButtonHint'
    BATTLE_MATTERS_FIGHT_BUTTON_HINT = b'BattleMattersFightButtonHint'
    BATTLE_MATTERS_ENTRY_POINT_BUTTON_HINT = b'BattleMattersEntryPointHint'
    SUMMARY_CUSTOMIZATION_BUTTON_HINT = b'SummaryCustomizationButtonHint'
    FL_SCENARIO_HINT = b'FrontlineScenariosHint'
    FL_SCENARIO_HINT_SMALL = b'FrontlineScenariosHintSmallSizes'
    BATTLE_ROYALE_DYNAMIC_PLATOON_SUB_MODE_HINT = b'BattleRoyaleDynamicPlatoonSubModeHint'
    CREW_BOOKS_POST_PROGRESSION_HINT = b'CrewBooksPostProgressionHint'
    CREW_BOOKS_MENTORING_LICENSE_HINT = b'CrewBooksMentoringLicenseHint'
    ACHIEVEMENTS_HANGAR_HINT = b'AchievementsHangarHint'
    ACHIEVEMENTS_PROFILE_HINT = b'AchievementsProfileHint'
    ACHIEVEMENTS_PROFILE_HINT_SMALL = b'AchievementsProfileHintSmallSize'
    NEW_C11N_SECTION_HINT = b'NewC11nSectionHint'
    C11N_VEHICLE_LIST_HINT = b'C11nVehicleListHint'
    VEHICLE_C11N_FILTER_HINT = b'VehicleC11nFilterHint'
    VDAY_DIFFICULTY_HINT = b'VDayDifficultyHint'


class SESSION_STATS(CONST_CONTAINER):
    IS_NOT_NEEDED_RESET_STATS_EVERY_DAY = b'IsNotNeededResetStatsEveryDay'
    IS_NEEDED_SAVE_CURRENT_TAB = b'IsNeededSaveCurrentTab'
    CURRENT_TAB = b'CurrentTab'
    ECONOMIC_BLOCK_VIEW = b'EconomicBlockView'
    SHOW_WTR = b'ShowWtr'
    SHOW_RATIO_DAMAGE = b'ShowRatioDamage'
    SHOW_RATIO_KILL = b'ShowRatioKill'
    SHOW_WINS = b'ShowWins'
    SHOW_AVERAGE_DAMAGE = b'ShowAverageDamage'
    SHOW_HELP_DAMAGE = b'ShowHelpDamage'
    SHOW_BLOCKED_DAMAGE = b'ShowBlockedDamage'
    SHOW_AVERAGE_XP = b'ShowAverageXp'
    SHOW_WIN_RATE = b'ShowWinRate'
    SHOW_AVERAGE_VEHICLE_LEVEL = b'ShowAverageVehicleLevel'
    SHOW_AVERAGE_FRAGS = b'ShowAverageFrags'
    SHOW_SURVIVED_RATE = b'ShowSurvivedRate'
    SHOW_SPOTTED = b'ShowSpotted'
    ONLY_ONCE_HINT_SHOWN_FIELD = b'OnlyOnceHintShownField'
    ECONOMIC_BLOCK_VIEW_WITH_SPENDING = 0
    ECONOMIC_BLOCK_VIEW_WITHOUT_SPENDING = 1
    BATTLES_TAB = 0
    VEHICLES_TAB = 1

    @classmethod
    def getEfficiencyBlock(cls):
        return (cls.SHOW_WTR,
         cls.SHOW_WINS,
         cls.SHOW_WIN_RATE,
         cls.SHOW_AVERAGE_FRAGS,
         cls.SHOW_RATIO_KILL,
         cls.SHOW_AVERAGE_DAMAGE,
         cls.SHOW_RATIO_DAMAGE,
         cls.SHOW_HELP_DAMAGE,
         cls.SHOW_BLOCKED_DAMAGE,
         cls.SHOW_SPOTTED,
         cls.SHOW_AVERAGE_VEHICLE_LEVEL,
         cls.SHOW_SURVIVED_RATE,
         cls.SHOW_AVERAGE_XP)

    @classmethod
    def getAccountEfficiencyBlock(cls):
        return (cls.SHOW_WTR,
         cls.SHOW_WINS,
         cls.SHOW_WIN_RATE,
         cls.SHOW_AVERAGE_FRAGS,
         cls.SHOW_RATIO_KILL,
         cls.SHOW_AVERAGE_DAMAGE,
         cls.SHOW_RATIO_DAMAGE,
         cls.SHOW_HELP_DAMAGE,
         cls.SHOW_BLOCKED_DAMAGE,
         cls.SHOW_SPOTTED,
         cls.SHOW_AVERAGE_VEHICLE_LEVEL,
         cls.SHOW_SURVIVED_RATE,
         cls.SHOW_AVERAGE_XP)

    @classmethod
    def getVehiclesEfficiencyBlock(cls):
        return (cls.SHOW_WTR,
         cls.SHOW_WINS,
         cls.SHOW_WIN_RATE,
         cls.SHOW_AVERAGE_FRAGS,
         cls.SHOW_RATIO_KILL,
         cls.SHOW_AVERAGE_DAMAGE,
         cls.SHOW_RATIO_DAMAGE,
         cls.SHOW_HELP_DAMAGE,
         cls.SHOW_BLOCKED_DAMAGE,
         cls.SHOW_SPOTTED,
         cls.SHOW_SURVIVED_RATE,
         cls.SHOW_AVERAGE_XP)

    @classmethod
    def getImmutableEfficiencyBlockParameters(cls):
        return (cls.SHOW_WTR,)

    @classmethod
    def getCommonBlock(cls):
        return (cls.IS_NOT_NEEDED_RESET_STATS_EVERY_DAY,
         cls.IS_NEEDED_SAVE_CURRENT_TAB)

    @classmethod
    def getEconomicBlockView(cls):
        return (cls.ECONOMIC_BLOCK_VIEW_WITHOUT_SPENDING,
         cls.ECONOMIC_BLOCK_VIEW_WITH_SPENDING)


class BattlePassStorageKeys(CONST_CONTAINER):
    INTRO_SHOWN = b'introShown'
    INTRO_VIDEO_SHOWN = b'introVideoShown'
    FLAGS_VERSION = b'flagsVersion'
    DAILY_QUESTS_INTRO_SHOWN = b'dailyQuestsIntroShown'
    FLAGS_VERSION_HOLIDAY = b'flagsVersionHoliday'


class BattleCommStorageKeys(CONST_CONTAINER):
    ENABLE_BATTLE_COMMUNICATION = b'enableBattleComm'
    SHOW_COM_IN_PLAYER_LIST = b'showCommInPlayerlist'
    SHOW_STICKY_MARKERS = b'showStickyMarkers'
    SHOW_CALLOUT_MESSAGES = b'showCalloutMessages'
    SHOW_LOCATION_MARKERS = b'showLocationMarkers'
    SHOW_BASE_MARKERS = b'showMarkers'
    ENABLE_COMMENDATIONS_FEEDBACK = b'enableCommendations'


class ScorePanelStorageKeys(CONST_CONTAINER):
    SHOW_HP_BAR = b'showHPBar'
    SHOW_HP_VALUES = b'showHPValues'
    SHOW_HP_DIFFERENCE = b'showHPDifference'
    ENABLE_TIER_GROUPING = b'enableTierGrouping'


class SeniorityAwardsStorageKeys(CONST_CONTAINER):
    SENIORITY_AWARDS_ON_PAUSE_NOTIFICATION_SHOWED = b'seniorityAwardsOnPauseShowed'


class ReferralProgram(CONST_CONTAINER):
    VIEWED_REFERRAL_PROGRAM_SEASON = b'viewedReferralProgramSeason'


class PersonalMission3(CONST_CONTAINER):
    INTRO = b'INTRO'
    INTRO_OP_8 = b'INTRO_OP_8'
    INTRO_OP_9 = b'INTRO_OP_9'
    INTRO_OP_10 = b'INTRO_OP_10'
    CHECKED_PM3_POINTS = b'DELTA_PM3_POINTS'
    PM_BANNER_ANIMATION_KEY = b'PM_BANNER_ANIMATION'
    LAST_FULL_COMPLETED_OP = b'LAST_FULL_COMPLETED_OP'
    PART_NO = b'PART_NO'


class ArmorInspector(object):
    SETTINGS = b'armorInspector'
    SELECTED_MODE = b'selectedMode'
    SESSION_ATTACKING_VEHICLES = b'sessionAttackingVehicles'


COLOR_GRADING_TECHNIQUE_DEFAULT = 0
