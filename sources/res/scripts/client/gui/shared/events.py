import logging
from collections import namedtuple
import typing
from gui.shared.event_bus import SharedEvent
from shared_utils import CONST_CONTAINER
if typing.TYPE_CHECKING:
    from gui.Scaleform.framework.managers.loaders import GuiImplViewLoadParams
    from gui.Scaleform.framework.managers.loaders import SFViewLoadParams
__all__ = (b'ArgsEvent', b'ComponentEvent', b'LoadViewEvent', b'LoadGuiImplViewEvent', b'ShowDialogEvent', b'LoginEvent', b'LoginEventEx', b'LobbySimpleEvent', b'FightButtonDisablingEvent', b'FightButtonEvent', b'CloseWindowEvent', b'BrowserEvent', b'HangarVehicleEvent', b'HangarCustomizationEvent', b'GameEvent', b'BootcampEvent', b'ViewEventType', b'OpenLinkEvent', b'ChannelManagementEvent', b'PreBattleChannelEvent', b'AmmunitionSetupViewEvent', b'HasCtxEvent', b'DogTagsEvent', b'FullscreenModeSelectorEvent', b'MarkersManagerEvent', b'ModeSelectorPopoverEvent', b'ModeSubSelectorEvent', b'ArmoryYardEvent')
_logger = logging.getLogger(__name__)

class HasCtxEvent(SharedEvent):

    def __init__(self, eventType=None, ctx=None):
        super(HasCtxEvent, self).__init__(eventType)
        self.ctx = ctx if ctx is not None else {}
        return


class AppLifeCycleEvent(SharedEvent):
    CREATING = b'app/creating'
    INITIALIZING = b'app/initializing'
    INITIALIZED = b'app/initialized'
    DESTROYED = b'app/destroyed'

    def __init__(self, ns, eventType):
        super(AppLifeCycleEvent, self).__init__(eventType)
        self.__ns = ns
        return

    @property
    def ns(self):
        return self.__ns


class GameEvent(HasCtxEvent):
    SCREEN_SHOT_MADE = b'game/screenShotMade'
    SHOW_EXTENDED_INFO = b'game/showExtendedInfo'
    CHOICE_CONSUMABLE = b'game/choiceConsumable'
    MINIMAP_CMD = b'game/minimapCmd'
    RADIAL_MENU_CMD = b'game/radialMenuCmd'
    TOGGLE_GUI = b'game/toggleGUI'
    GUI_VISIBILITY = b'game/guiVisibility'
    MARKERS_2D_VISIBILITY = b'game/markers2DVisibility'
    CROSSHAIR_VISIBILITY = b'game/crosshairVisibility'
    GUN_MARKER_VISIBILITY = b'game/gunMarkerVisibility'
    CROSSHAIR_VIEW = b'game/crosshairView'
    FULL_STATS = b'game/fullStats'
    EVENT_STATS = b'game/eventStats'
    FULL_STATS_QUEST_PROGRESS = b'game/fullStats/questProgress'
    FULL_STATS_PERSONAL_RESERVES = b'game/fullStats/personalReserves'
    HIDE_VEHICLE_UPGRADE = b'game/battleRoyale/hideVehicleUpgrade'
    SHOW_CURSOR = b'game/showCursor'
    HIDE_CURSOR = b'game/hideCursor'
    NEXT_PLAYERS_PANEL_MODE = b'game/nextPlayersPanelMode'
    PLAYING_TIME_ON_ARENA = b'game/playingTimeOnArena'
    CHANGE_APP_RESOLUTION = b'game/changeAppResolution'
    SHOW_EXTERNAL_COMPONENTS = b'game/showExternalComponents'
    HIDE_EXTERNAL_COMPONENTS = b'game/hideExternalComponents'
    ON_BACKGROUND_ALPHA_CHANGE = b'game/onBackgroundAlphaChange'
    HIDE_LOBBY_SUB_CONTAINER_ITEMS = b'game/hideLobbySubContainerItems'
    REVEAL_LOBBY_SUB_CONTAINER_ITEMS = b'game/revealLobbySubContainerItems'
    BATTLE_LOADING = b'game/battleLoading'
    SHOW_BTN_HINT = b'game/showBtnHint'
    HIDE_BTN_HINT = b'game/hideBtnHint'
    DESTROY_TIMERS_PANEL = b'game/destroyTimersPanel'
    SHOW_LOOT_BOX_WINDOWS = b'game/showLootBoxWindows'
    HIDE_LOOT_BOX_WINDOWS = b'game/hideLootBoxWindows'
    CLOSE_LOOT_BOX_WINDOWS = b'game/closeLootBoxWindows'
    CHARGE_RELEASED = b'game/chargeReleased'
    PRE_CHARGE = b'game/preCharge'
    CONTROL_MODE_CHANGE = b'game/controlModeChange'
    SNIPER_CAMERA_TRANSITION = b'game/sniperCameraTransition'
    FADE_OUT_AND_IN = b'game/fadeOutIn'
    CALLOUT_DISPLAY_EVENT = b'game/calloutDisplayEvent'
    RESPOND_TO_CALLOUT = b'game/respondToCallout'
    ARENA_BORDER_TYPE_CHANGED = b'game/arenaBorderTypeChanged'
    TOGGLE_VOIP_CHANNEL_ENABLED = b'game/voip/toggleEnabled'
    ROLE_HINT_TOGGLE = b'roleHintToggle'
    COMMANDER_HINT = b'game/commanderHint'
    CHANGE_AMMUNITION_SETUP = b'game/changeAmmunitionSetup'
    TOGGLE_DEBUG_PIERCING_PANEL = b'game/toggleDebugPiercingPanel'
    ON_TARGET_VEHICLE_CHANGED = b'game/onTargetVehicleChanged'
    POINT_OF_INTEREST_ADDED = b'game/changeAmmunitionSetup'
    POINT_OF_INTEREST_REMOVED = b'game/changeAmmunitionSetup'
    PREBATTLE_INPUT_STATE_LOCKED = b'game/inputStateLocked'
    BATTLE_CONTEXT_HINT_ACTIVATED = b'game/battleContextHintActivated'


class GUICommonEvent(SharedEvent):
    LOBBY_VIEW_LOADED = b'lobbyViewLoaded'


class GUIEditorEvent(HasCtxEvent):
    HIDE_GUIEditor = b'hideGUIEditor'


class ArgsEvent(HasCtxEvent):
    UPDATE_ARGS = b'updateArguments'

    def __init__(self, eventType=None, alias=b'', ctx=None):
        super(ArgsEvent, self).__init__(eventType, ctx)
        self.alias = alias
        return


class FocusEvent(HasCtxEvent):
    COMPONENT_FOCUSED = b'onComponentFocused'


class ComponentEvent(SharedEvent):
    COMPONENT_REGISTERED = b'onComponentRegistered'
    COMPONENT_UNREGISTERED = b'onComponentUnRegistered'

    def __init__(self, eventType, owner, componentPy, alias):
        super(ComponentEvent, self).__init__(eventType)
        self.owner = owner
        self.componentPy = componentPy
        self.alias = alias
        return


class ViewEventType(CONST_CONTAINER):
    LOAD_VIEW = b'viewEventLoadView'
    LOAD_GUI_IMPL_VIEW = b'ubViewEventLoadView'
    LOAD_VIEWS_CHAIN = b'viewEventLoadViewChain'
    PRELOAD_VIEW = b'viewEventPreLoadView'
    DESTROY_VIEW = b'viewEventDestroyView'
    DESTROY_GUI_IMPL_VIEW = b'ubViewEventDestroyView'


class _ViewEvent(HasCtxEvent):

    def __init__(self, eventType, alias, name=None, ctx=None):
        super(_ViewEvent, self).__init__(eventType, ctx)
        self.alias = alias
        self.name = name
        return


class LoadViewEvent(_ViewEvent):

    def __init__(self, loadParams, *args, **kwargs):
        if isinstance(loadParams, str):
            _logger.error(b'Wrong loadParams type for "%s"! Replace it by SFViewLoadParams.', loadParams)
        super(LoadViewEvent, self).__init__(ViewEventType.LOAD_VIEW, loadParams.viewKey.alias, loadParams.viewKey.name, ctx=kwargs.get(b'ctx', None))
        self.loadParams = loadParams
        self.args = args
        self.kwargs = kwargs
        return

    def __repr__(self):
        return (b'LoadViewEvent[loadParams={}, ctx={}, args={}, kwargs={}]').format(repr(self.loadParams), self.ctx, self.args, self.kwargs)


class LoadViewsChainEvent(_ViewEvent):

    def __init__(self, viewLoadEvents):
        super(LoadViewsChainEvent, self).__init__(ViewEventType.LOAD_VIEWS_CHAIN, None, None)
        self.viewLoadEvents = viewLoadEvents
        return


class PreLoadViewEvent(_ViewEvent):

    def __init__(self, alias, name=None, ctx=None):
        super(PreLoadViewEvent, self).__init__(ViewEventType.PRELOAD_VIEW, alias, name, ctx)
        return


class DestroyViewEvent(_ViewEvent):

    def __init__(self, alias, name=None):
        super(DestroyViewEvent, self).__init__(ViewEventType.DESTROY_VIEW, alias, name)
        return


class LoadGuiImplViewEvent(_ViewEvent):

    def __init__(self, loadParams, *args, **kwargs):
        super(LoadGuiImplViewEvent, self).__init__(ViewEventType.LOAD_GUI_IMPL_VIEW, loadParams.viewKey.alias)
        self.loadParams = loadParams
        self.viewClass = loadParams.viewClass
        self.scope = loadParams.scope
        self.args = args
        self.kwargs = kwargs
        return


class DestroyGuiImplViewEvent(_ViewEvent):

    def __init__(self, layoutID):
        super(DestroyGuiImplViewEvent, self).__init__(ViewEventType.DESTROY_GUI_IMPL_VIEW, layoutID)
        return


class BrowserEvent(HasCtxEvent):
    BROWSER_CREATED = b'onBrowserCreated'


class ShowDialogEvent(SharedEvent):
    SHOW_SIMPLE_DLG = b'showSimpleDialog'
    SHOW_BUTTON_DLG = b'showButtonDialog'
    SHOW_ICON_DIALOG = b'showIconDialog'
    SHOW_ICON_PRICE_DIALOG = b'showIconPriceDialog'
    SHOW_PM_CONFIRMATION_DIALOG = b'showPMConfirmationDialog'
    SHOW_CONFIRM_MODULE = b'showConfirmModule'
    SHOW_CONFIRM_BOOSTER = b'showConfirmBooster'
    SHOW_SYSTEM_MESSAGE_DIALOG = b'showSystemMessageDialog'
    SHOW_CYBER_SPORT_DIALOG = b'showCyberSportDialog'
    SHOW_CONFIRM_ORDER_DIALOG = b'showConfirmOrderDialog'
    SHOW_PUNISHMENT_DIALOG = b'showPunishmentDialog'
    SHOW_COMP7_PUNISHMENT_DIALOG = b'showComp7PunishmentDialog'
    SHOW_EXCHANGE_DIALOG = b'showExchangeDialog'
    SHOW_EXCHANGE_BERTHS_DIALOG = b'showExchangeBerthsDialog'
    SHOW_EXCHANGE_DIALOG_MODAL = b'showExchangeDialogModal'
    SHOW_DETAILED_EXCHANGE_XP_DIALOG = b'showDetailedExchangeXPDialog'
    SHOW_CHECK_BOX_DIALOG = b'showCheckBoxDialog'
    SHOW_EXECUTION_CHOOSER_DIALOG = b'showExecutionChooserDialog'
    SHOW_USE_AWARD_SHEET_DIALOG = b'useAwardSheetDialog'
    SHOW_CONFIRM_C11N_BUY_DIALOG = b'showConfirmC11nBuyDialog'
    SHOW_CONFIRM_C11N_SELL_DIALOG = b'showConfirmC11nSellDialog'

    def __init__(self, meta, handler, parent=None):
        super(ShowDialogEvent, self).__init__(ViewEventType.LOAD_VIEW)
        self.alias = meta.getEventType()
        self.meta = meta
        self.handler = handler
        self.parent = parent
        return


class LoginEvent(SharedEvent):
    CANCEL_LGN_QUEUE = b'cancelLoginQueue'
    LOGIN_VIEW_READY = b'loginViewReady'
    DISCONNECTION_STARTED = b'disconnectionStarted'
    CONNECTION_FAILED = b'connectionFailed'

    def __init__(self, eventType, alias=b'', isSuccess=False, errorMsg=b''):
        super(LoginEvent, self).__init__(eventType=eventType)
        self.alias = alias
        self.isSuccess = isSuccess
        self.errorMsg = errorMsg
        return


class LoginEventEx(LoginEvent):
    ON_LOGIN_QUEUE_CLOSED = b'onLoginQueueClosed'
    SWITCH_LOGIN_QUEUE_TO_AUTO = b'switchLoginQueueToAuto'

    def __init__(self, eventType, alias, waitingOpen, msg, waitingClose, showAutoLoginBtn):
        super(LoginEventEx, self).__init__(eventType=eventType, alias=alias)
        self.waitingOpen = waitingOpen
        self.msg = msg
        self.waitingClose = waitingClose
        self.showAutoLoginBtn = showAutoLoginBtn
        return


class BCLoginEvent(SharedEvent):
    CLOSE_WINDOW = b'closeBCLoginQueue'
    CANCEL_WAITING = b'cancelWaitingBCLoginQueue'
    HIDE_GAME_LOADING = b'hideGameLoadingBCLoginQueue'

    def __init__(self, eventType, title=None, message=None, cancelLabel=None):
        super(BCLoginEvent, self).__init__(eventType=eventType)
        self.title = title
        self.message = message
        self.cancelLabel = cancelLabel
        return


class RenameWindowEvent(HasCtxEvent):
    RENAME_WINDOW = b'renameWindow'

    def __init__(self, eventType, ctx):
        super(RenameWindowEvent, self).__init__(eventType=eventType, ctx=ctx)
        return


class HideWindowEvent(HasCtxEvent):
    HIDE_BATTLE_RESULT_WINDOW = b'hideBattleResultsWindow'
    HIDE_BATTLE_SESSION_WINDOW = b'hideBattleSessionWindow'
    HIDE_UNIT_WINDOW = b'hideUnitWindow'
    HIDE_LEGAL_INFO_WINDOW = b'hideLegalInfoWindow'
    HIDE_VEHICLE_SELECTOR_WINDOW = b'hideVehicleSelectorWindow'
    HIDE_ROSTER_SLOT_SETTINGS_WINDOW = b'hideRosterSlotSettingsWindow'
    HIDE_MISSION_DETAILS_VIEW = b'hideMissionDetailsView'
    HIDE_PERSONAL_MISSION_DETAILS_VIEW = b'hidePersonalMissionDetailsView'
    HIDE_BROWSER_WINDOW = b'hideBrowserWindow'
    HIDE_VEHICLE_PREVIEW = b'hideVehiclePreview'
    HIDE_OVERLAY_BROWSER_VIEW = b'hideOverlayBrowserView'
    HIDE_MISSIONS_PAGE_VIEW = b'hideMissionsPageView'
    HIDE_SPECIAL_BATTLE_WINDOW = b'hideSpecialBattleWindow'


class HidePopoverEvent(HasCtxEvent):
    HIDE_POPOVER = b'hidePopover'
    POPOVER_DESTROYED = b'popoverDestroyed'


class LobbySimpleEvent(HasCtxEvent):
    UPDATE_TANK_PARAMS = b'updateTankParams'
    SHOW_HELPLAYOUT = b'showHelplayout'
    CLOSE_HELPLAYOUT = b'closeHelplayout'
    EVENTS_UPDATED = b'questUpdated'
    HIDE_HANGAR = b'hideHangar'
    NOTIFY_CURSOR_OVER_3DSCENE = b'notifyCursorOver3dScene'
    NOTIFY_CURSOR_DRAGGING = b'notifyCursorDragging'
    NOTIFY_SPACE_MOVED = b'notifySpaceMoved'
    PREMIUM_BOUGHT = b'premiumBought'
    PREMIUM_XP_BONUS_CHANGED = b'premiumXPBonusChanged'
    WAITING_SHOWN = b'waitingShown'
    WAITING_HIDDEN = b'waitingHidden'
    BATTLE_RESULTS_POSTED = b'battleResultsPosted'
    BATTLE_RESULTS_SHOW_QUEST = b'battleResultsWindowShowQuest'
    CHANGE_SOUND_ENVIRONMENT = b'changeSoundEnvironment'
    VEHICLE_PREVIEW_HIDDEN = b'vehiclePreviewHidden'
    ENTITY_TOOLTIP_SHOW = b'entityTooltipShow'
    ENTITY_TOOLTIP_HIDE = b'entityTooltipHide'
    HANGAR_STATUS_CHANGED = b'hangarStatusChanged'


class MissionsEvent(HasCtxEvent):
    ON_FILTER_CHANGED = b'onFilterChanged'
    ON_FILTER_CLOSED = b'onFilterClosed'
    ON_GROUPS_DATA_CHANGED = b'onGroupsDataChanged'
    ON_ACTIVATE = b'onActivate'
    ON_DEACTIVATE = b'onDeactivate'
    ON_TAB_CHANGED = b'onTabChanged'
    PAGE_INVALIDATE = b'pageInvalidate'


class PersonalMissionsEvent(HasCtxEvent):
    ON_DETAILS_VIEW_OPEN = b'onDetailsViewOpen'
    ON_DETAILS_VIEW_CLOSE = b'onDetailsViewClose'
    ON_AWARD_SCEEN_OPEN = b'onAwardScreenOpen'
    ON_AWARD_SCEEN_CLOSE = b'onAwardScreenClose'
    UPDATE_AWARD_SCREEN = b'updateAwardScreen'
    ON_AWARD_PM_SCREEN_CLOSE = b'onAwardPmScreenClose'
    ON_ALL_REWARDS_PM3_VIEW_CLOSE = b'onAllRewardsPm3ViewClose'


class TrainingSettingsEvent(HasCtxEvent):
    UPDATE_TRAINING_SETTINGS = b'updateTrainingSettings'
    UPDATE_EPIC_TRAINING_SETTINGS = b'updateEpicTrainingSettings'


class TechnicalMaintenanceEvent(HasCtxEvent):
    RESET_EQUIPMENT = b'resetEquipment'


class ContactsEvent(HasCtxEvent):
    EDIT_GROUP = b'editGroup'
    REMOVE_GROUP = b'removeGroup'
    CREATE_CONTACT_NOTE = b'createContactNote'
    EDIT_CONTACT_NOTE = b'editContactNote'


class FightButtonDisablingEvent(LobbySimpleEvent):
    FIGHT_BUTTON_DISABLE = b'fightButtonDisable'

    def __init__(self, eventType, isDisabled, toolTip):
        super(FightButtonDisablingEvent, self).__init__(eventType)
        self.isDisabled = isDisabled
        self.toolTip = toolTip
        return


class FightButtonEvent(LobbySimpleEvent):
    FIGHT_BUTTON_UPDATE = b'updateFightButton'


class LobbyHeaderEvent(LobbySimpleEvent):
    TOGGLE_VISIBILITY = b'toggleVisibilityHeader'


class LobbyHeaderMenuEvent(LobbySimpleEvent):
    TOGGLE_VISIBILITY = b'toggleVisibilityHeaderMenu'
    MENU_CLICK = b'headerMenuClick'


class ReferralViewEvent(HasCtxEvent):
    TOGGLE_BUTTON = b'toggleButton'


class CloseWindowEvent(SharedEvent):
    EULA_CLOSED = b'EULAClosed'
    GOLD_FISH_CLOSED = b'GoldFishClosed'
    ELITE_WINDOW_CLOSED = b'EliteWindowClosed'
    BUY_VEHICLE_VIEW_CLOSED = b'BuyVehicleViewClosed'

    def __init__(self, eventType=None, isAgree=False):
        super(CloseWindowEvent, self).__init__(eventType)
        self.isAgree = isAgree
        return


coolDownEventParams = namedtuple(b'coolDownEventParams', b'eventType, requestScope, actionId')

class CoolDownEvent(SharedEvent):
    GLOBAL = b'globalCoolDown'
    PREBATTLE = b'prebattleCoolDown'
    FORTIFICATION = b'fortificationCoolDown'
    BW_CHAT2 = b'bwChat2CoolDown'
    XMPP = b'xmppCoolDown'
    BATTLE = b'battleCoolDown'
    CLIENTGW = b'clientgw'
    STRONGHOLD = b'stronghold'
    BATTLE_ACTION = b'battleAction'
    WGNP = b'wgnp'

    def __init__(self, eventType=None, requestID=0, coolDown=5.0):
        super(CoolDownEvent, self).__init__(eventType)
        self.coolDown = coolDown
        self.requestID = requestID
        return


class HangarHeaderEvent(SharedEvent):
    UPDATE_VO_HEADER = b'updateVOHeader'


class TutorialEvent(SharedEvent):
    START_TRAINING = b'startTraining'
    STOP_TRAINING = b'stopTraining'
    ON_COMPONENT_FOUND = b'onComponentFound'
    ON_COMPONENT_LOST = b'onComponentLost'
    ON_TRIGGER_ACTIVATED = b'onTriggerActivated'
    ON_ANIMATION_COMPLETE = b'onAnimationComplete'
    SIMPLE_WINDOW_PROCESSED = b'simpleWindowProcessed'
    UPDATE_TUTORIAL_HINTS = b'updateTutorialHints'
    IMPORTANT_HINT_SHOWING = b'importantHintShowing'
    OVERRIDE_HANGAR_MENU_BUTTONS = b'overrideHangarMenuButtons'
    OVERRIDE_HEADER_MENU_BUTTONS = b'overrideHeaderMenuButtons'
    SET_HANGAR_HEADER_ENABLED = b'setHangarHeaderEnabled'
    OVERRIDE_BATTLE_SELECTOR_HINT = b'overrideBattleSelectorHint'

    def __init__(self, eventType, settingsID=b'', targetID=b'', reloadIfRun=False, initialChapter=None, restoreIfRun=False, isStopForced=False, isAfterBattle=False, state=False, arguments=b'', showWaiting=True):
        super(TutorialEvent, self).__init__(eventType)
        self.settingsID = settingsID
        self.targetID = targetID
        self.reloadIfRun = reloadIfRun
        self.initialChapter = initialChapter
        self.restoreIfRun = restoreIfRun
        self.isStopForced = isStopForced
        self.isAfterBattle = isAfterBattle
        self.componentState = state
        self.arguments = arguments
        self.showWaiting = showWaiting
        return

    def getState(self):
        return {b'reloadIfRun': (self.reloadIfRun), 
           b'initialChapter': (self.initialChapter), 
           b'restoreIfRun': (self.restoreIfRun), 
           b'isStopForced': (self.isStopForced), 
           b'isAfterBattle': (self.isAfterBattle)}


class BootcampEvent(SharedEvent):
    SHOW_SECONDARY_HINT = b'ShowSecondaryHint'
    HIDE_SECONDARY_HINT = b'HideSecondaryHint'

    def __init__(self, eventType, eventId=0, eventArg=0):
        super(BootcampEvent, self).__init__(eventType)
        self.eventId = eventId
        self.eventArg = eventArg
        return


class MessengerEvent(HasCtxEvent):
    PRB_CHANNEL_CTRL_INITED = b'prbChannelCtrlInited'
    PRB_CHANNEL_CTRL_DESTROYED = b'prbChannelCtrlDestroyed'
    LAZY_CHANNEL_CTRL_INITED = b'lazyChannelCtrlInited'
    LAZY_CHANNEL_CTRL_DESTROYED = b'lazyChannelCtrlDestroyed'
    LOBBY_CHANNEL_CTRL_INITED = b'lobbyChannelCtrlInited'
    LOBBY_CHANNEL_CTRL_DESTROYED = b'lobbyChannelCtrlDestroyed'
    BATTLE_CHANNEL_CTRL_INITED = b'battleChannelCtrlInited'
    BATTLE_CHANNEL_CTRL_DESTROY = b'battleChannelCtrlDestroyed'


class ChannelManagementEvent(HasCtxEvent):
    REQUEST_TO_ADD = b'requestToAdd'
    REQUEST_TO_REMOVE = b'requestToRemove'
    REQUEST_TO_CHANGE = b'requestToChange'
    REQUEST_TO_MULTI_CHANGE = b'requestMultiChange'
    REQUEST_TO_SHOW = b'requestToShow'
    REQUEST_TO_ACTIVATE = b'rqActivateChannel'
    REQUEST_TO_DEACTIVATE = b'rqDeactivateChannel'
    REQUEST_TO_EXIT = b'rqExitChannel'
    REGISTER_BATTLE = b'registerBattleComponent'
    UNREGISTER_BATTLE = b'unregisterBattleComponent'
    MESSAGE_FADING_ENABLED = b'messageFadingEnabled'

    def __init__(self, clientID, eventType=None, ctx=None):
        super(ChannelManagementEvent, self).__init__(eventType, ctx)
        self.clientID = clientID
        return


class PreBattleChannelEvent(ChannelManagementEvent):
    REQUEST_TO_ADD_PRE_BATTLE_CHANNEL = b'loadSquad'
    REQUEST_TO_REMOVE_PRE_BATTLE_CHANNEL = b'removeSquad'


class ChannelCarouselEvent(SharedEvent):
    CAROUSEL_INITED = b'carouselInited'
    CAROUSEL_DESTROYED = b'carouselDestroyed'
    OPEN_BUTTON_CLICK = b'openButtonClick'
    MINIMIZE_ALL_CHANNELS = b'minimizeAllChannels'
    CLOSE_ALL_EXCEPT_CURRENT = b'closeAllExceptCurrent'
    CLOSE_BUTTON_CLICK = b'closeButtonClick'
    ON_WINDOW_CHANGE_FOCUS = b'onWindowChangeFocus'
    ON_WINDOW_CHANGE_OPEN_STATE = b'onWindowChangeOpenState'

    def __init__(self, target, eventType=None, clientID=None, wndType=None, flag=False):
        super(ChannelCarouselEvent, self).__init__(eventType)
        self.target = target
        self.clientID = clientID
        self.wndType = wndType
        self.flag = flag
        return


class AutoInviteEvent(SharedEvent):
    INVITE_RECEIVED = b'inviteReceived'

    def __init__(self, invite, eventType=None):
        super(AutoInviteEvent, self).__init__(eventType)
        self.invite = invite
        return


class CSVehicleSelectEvent(HasCtxEvent):
    VEHICLE_SELECTED = b'CSVehicleSelectEvent/vehicleSelected'


class CSReserveSelectEvent(HasCtxEvent):
    RESERVE_SELECTED = b'reserveSelected'


class CSRosterSlotSettingsWindow(HasCtxEvent):
    APPLY_SLOT_SETTINGS = b'applySlotSettings'


class StrongholdEvent(HasCtxEvent):
    STRONGHOLD_ACTIVATED = b'strongholdActivated'
    STRONGHOLD_DEACTIVATED = b'strongholdDeactivated'
    STRONGHOLD_DATA_UNAVAILABLE = b'strongholdDataUnavailable'
    STRONGHOLD_ON_TIMER = b'strongholdOnTimer'
    STRONGHOLD_VEHICLES_SELECTED = b'strongholdVehicleSelected'
    STRONGHOLD_LOADED = b'strongholdLoaded'
    STRONGHOLD_UPDATED = b'strongholdUpdated'


class ShopEvent(HasCtxEvent):
    SHOP_ACTIVATED = b'shopActivated'
    SHOP_DEACTIVATED = b'shopDeactivated'
    SHOP_DATA_UNAVAILABLE = b'shopDataUnavailable'
    SHOP_ON_TIMER = b'shopOnTimer'
    CONFIRM_TRADE_IN = b'confirmTradeIn'
    SELECT_RENT_TERM = b'selectRentTerm'


class OpenLinkEvent(SharedEvent):
    SPECIFIED = b'openSpecifiedURL'
    PARSED = b'openParsedURL'
    REGISTRATION = b'openRegistrationURL'
    RECOVERY_PASSWORD = b'openRecoveryPasswordURL'
    PAYMENT = b'openPaymentURL'
    SECURITY_SETTINGS = b'openSecuritySettingsURL'
    CLAN_RULES = b'openClanRulesURL'
    SUPPORT = b'openSupportURL'
    MIGRATION = b'openMigrationURL'
    FORT_DESC = b'fortDescription'
    CLAN_SEARCH = b'clanSearch'
    CLAN_CREATE = b'clanCreate'
    INVIETES_MANAGEMENT = b'invitesManagementURL'
    GLOBAL_MAP_SUMMARY = b'globalMapSummary'
    GLOBAL_MAP_PROMO_SUMMARY = b'globalMapPromoSummary'
    GLOBAL_MAP_CAP = b'globalMapCap'
    GLOBAL_MAP_PROMO = b'globalMapPromo'
    PREM_SHOP = b'premShopURL'
    TOKEN_SHOP = b'tokenShopUrl'
    FRONTLINE_CHANGES = b'frontlineChangesURL'
    WOT_PLUS_STEAM_SHOP = b'wotPlusSteamURL'
    WOT_PLUS_SHOP = b'wotPlusShopURL'

    def __init__(self, eventType, url=b'', title=b'', params=None):
        super(OpenLinkEvent, self).__init__(eventType)
        self.url = url
        self.title = title
        self.params = params
        return


class CalendarEvent(SharedEvent):
    MONTH_CHANGED = b'monthChanged'
    DATE_SELECTED = b'dateSelected'

    def __init__(self, eventType=None, timestamp=None):
        super(CalendarEvent, self).__init__(eventType)
        self.__timestamp = timestamp
        return

    def getTimestamp(self):
        return self.__timestamp


class BubbleTooltipEvent(LobbySimpleEvent):
    SHOW = b'showBubble'

    def __init__(self, eventType, message=None, duration=5000):
        super(BubbleTooltipEvent, self).__init__(eventType)
        self.__message = message
        self.__duration = duration
        return

    def getMessage(self):
        return self.__message

    def getDuration(self):
        return self.__duration


class NotifyCenterShowItemEvent(SharedEvent):
    SHOW_BASIC_WINDOW = b'notifycenter/basicWindow/show'
    CLOSE_POLL_WINDOW = b'notifycenter/pollWindow/close'

    def __init__(self, notID, target, alias=None):
        super(NotifyCenterShowItemEvent, self).__init__(ViewEventType.LOAD_VIEW)
        self.alias = alias
        self.__notID = notID
        self.__target = target
        return

    def getNotID(self):
        return self.__notID

    def getTarget(self):
        return self.__target


class MarkersManagerEvent(SharedEvent):
    MARKERS_CREATED = b'markersCreated'

    def __init__(self, eventType=None, markersManager=None):
        super(MarkersManagerEvent, self).__init__(eventType)
        self.__markersManager = markersManager
        return

    def getMarkersManager(self):
        return self.__markersManager


class VehicleBuyEvent(HasCtxEvent):
    VEHICLE_SELECTED = b'vehicleBuyEvent/vehicleSelected'


class HangarVehicleEvent(HasCtxEvent):
    ON_HERO_TANK_LOADED = b'hangarVehicle/onHeroTankLoaded'
    ON_HERO_TANK_DESTROY = b'hangarVehicle/onHeroTankDestroy'
    ON_PLATOON_TANK_LOADED = b'hangarVehicle/onPlatoonTankLoaded'
    ON_PLATOON_TANK_DESTROY = b'hangarVehicle/onPlatoonTankDestroy'
    PLATOON_TANK_MARKER = b'hangarVehicle/platoonTankMarker'
    SELECT_VEHICLE_IN_HANGAR = b'hangarVehicle/selectVehicleInHangar'
    BOOTCAMP_SECOND_TANK_MARKER = b'hangarVehicle/bootcampSecondTankMarker'


class ManualEvent(HasCtxEvent):
    CHAPTER_OPENED = b'manual/chapterOpened'
    CHAPTER_CLOSED = b'manual/chapterClosed'


class StorageEvent(HasCtxEvent):
    SELECT_MODULE_FOR_SELL = b'storage/forSellView/selectModule'
    VEHICLE_SELECTED = b'storage/inventory/vehicleSelected'


class HangarCustomizationEvent(HasCtxEvent):
    CHANGE_VEHICLE_MODEL_TRANSFORM = b'hangarCustomization/changeVehicleModelTransform'
    RESET_VEHICLE_MODEL_TRANSFORM = b'hangarCustomization/resetVehicleModelTransform'


class SeniorityAwardsEvent(HasCtxEvent):
    ON_REWARD_VIEW_CLOSED = b'seniorityAwards/onRewardViewClosed'
    ON_ENTRY_VIEW_LOADED = b'seniorityAwards/onEntryViewLoaded'


class ReferralProgramEvent(HasCtxEvent):
    REFERRAL_PROGRAM_ACTIVATED = b'referralProgramActivated'
    REFERRAL_PROGRAM_DEACTIVATED = b'referralProgrammDeactivated'
    SHOW_REFERRAL_PROGRAM_WINDOW = b'showReferralProgramWindow'
    DISABLE_REFERRAL_PROGRAM = b'disableReferralProgram'


class AdventCalendarEvent(HasCtxEvent):
    ADVENT_CALENDAR = b'adventCalendar'
    HERO_ADVENT_ACTION_STATE_CHANGED = b'heroAdventActionStateChanged'


class ProgressiveRewardEvent(HasCtxEvent):
    WIDGET_WAS_SHOWN = b'progressiveWidgetWasShown'


class Comp7Event(SharedEvent):
    OPEN_META = b'openMeta'


class TechTreeEvent(HasCtxEvent):
    HIGHLIGHT_NODES = b'highlightNodes'


class AirDropEvent(HasCtxEvent):
    AIR_DROP_SPAWNED = b'onAirDropSpawned'
    AIR_DROP_LANDED = b'onAirDropLanded'
    AIR_DROP_LOOP_ENTERED = b'onAirDropLootEntered'
    AIR_DROP_LOOP_LEFT = b'onAirDropLootLeft'
    AIR_DROP_NXT_SPAWNED = b'onAirDropNxtSpawned'


class ProfilePageEvent(HasCtxEvent):
    SELECT_PROFILE_ALIAS = b'onProfileSelectAlias'


class ProfileStatisticEvent(HasCtxEvent):
    SELECT_BATTLE_TYPE = b'onProfileStatisticEventBattleTypeSelect'
    DISPOSE = b'onProfileStatisticEventDispose'


class ProfileTechniqueEvent(HasCtxEvent):
    SELECT_BATTLE_TYPE = b'onProfileTechniqueEventBattleTypeSelect'
    DISPOSE = b'onProfileTechniqueEventDispose'


class BattlePassEvent(HasCtxEvent):
    BUYING_THINGS = b'buyingThings'
    AWARD_VIEW_CLOSE = b'onAwardViewClose'
    ON_PURCHASE_LEVELS = b'onPurchaseLevels'
    ON_PREVIEW_PROGRESSION_STYLE_CLOSE = b'onPreviewProgressionStyleClose'
    VIDEO_SHOWN = b'videoShown'
    SHOW_BATTLE_PASS_AWARDS_VIDEO = b'showBattlePassAwardsVideo'


class ItemRemovalByDemountKitEvent(HasCtxEvent):
    DECLARED = b'item_removal_by_dk_declared'
    CANCELED = b'item_removal_by_dk_canceled'

    def __init__(self, eventType=None, slotIndex=None):
        self.slotIndex = slotIndex
        super(ItemRemovalByDemountKitEvent, self).__init__(eventType)
        return


class TrainingEvent(HasCtxEvent):
    RETURN_TO_TRAINING_ROOM = b'trainingEvent/returnToTrainingRoom'
    SHOW_TRAINING_LIST = b'trainingEvent/showTrainingList'
    SHOW_EPIC_TRAINING_LIST = b'trainingEvent/showEpicTrainingList'


class RallyWindowEvent(HasCtxEvent):
    ON_CLOSE = b'rallyWindowEvent/onClose'


class CustomizationEvent(HasCtxEvent):
    SHOW = b'customizationEvent/show'


class PrbInvitesEvent(HasCtxEvent):
    ACCEPT = b'prbInvitesEvent/accept'

    def __init__(self, eventType=None, inviteID=None, postActions=None):
        super(PrbInvitesEvent, self).__init__(eventType)
        self.inviteID = inviteID
        self.postActions = postActions
        return


class PrbActionEvent(HasCtxEvent):
    SELECT = b'prbActionEvent/select'
    LEAVE = b'prbActionEvent/leave'

    def __init__(self, action, eventType=None):
        super(PrbActionEvent, self).__init__(eventType)
        self.action = action
        return


class AmmunitionSetupViewEvent(HasCtxEvent):
    GF_RESIZED = b'ammunitionSetupViewEvent/gfResized'
    UPDATE_TTC = b'ammunitionSetupViewEvent/updateTTC'
    HINT_ZONE_ADD = b'ammunitionSetupViewEvent/hintZoneAdd'
    HINT_ZONE_HIDE = b'ammunitionSetupViewEvent/hintZoneHide'
    HINT_ZONE_CLICK = b'ammunitionSetupViewEvent/hintZoneClick'
    CLOSE_VIEW = b'ammunitionSetupViewEvent/closeView'


class AmmunitionPanelViewEvent(HasCtxEvent):
    SECTION_SELECTED = b'ammunitionPanelViewEvent/sectionSelected'
    CLOSE_VIEW = b'ammunitionPanelViewEvent/closeView'


class RadialMenuEvent(SharedEvent):
    RADIAL_MENU_ACTION = b'radialMenuAction'


class HangarSpacesSwitcherEvent(HasCtxEvent):
    SWITCH_TO_HANGAR_SPACE = b'hangarSpacesSwitcherEvent/SwitchToHangarSpace'


class DogTagsEvent(SharedEvent):
    COUNTERS_UPDATED = b'onCountersUpdated'


class PlatoonDropdownEvent(HasCtxEvent):
    NAME = b'DropdownEvent'


class FullscreenModeSelectorEvent(HasCtxEvent):
    NAME = b'FullscreenModeSelectorEvent'


class ModeSelectorPopoverEvent(HasCtxEvent):
    NAME = b'ModeSelectorPopoverEvent'


class ModeSubSelectorEvent(HasCtxEvent):
    CHANGE_VISIBILITY = b'subSelectorViewEvent/changeVisibility'
    CLICK_PROCESSING = b'subSelectorViewEvent/clickProcessing'


class GunMarkerEvent(HasCtxEvent):
    UPDATE_PIERCING_DATA = b'onPiercingDataUpdated'


class ResourceWellLoadingViewEvent(HasCtxEvent):
    LOAD = b'load'
    DESTROY = b'destroy'


class PointOfInterestEvent(HasCtxEvent):
    ADDED = b'poi/added'
    REMOVED = b'poi/removed'


class RoleSkillEvent(HasCtxEvent):
    STATE_CHANGED = b'roleSkill/stateChanged'
    COUNTER_CHANGED = b'roleSkill/counterChanged'


class CollectionsEvent(HasCtxEvent):
    NEW_ITEM_SHOWN = b'newItemShown'
    TAB_COUNTER_UPDATED = b'tabCounterUpdated'
    COLLECTION_VIEW_CLOSED = b'collectionViewClosed'
    COLLECTION_INTRO_CLOSED = b'collectionIntroClosed'


class ArmoryYardEvent(HasCtxEvent):
    STAGE_FINISHED = b'ayStageFinished'
    STAGE_MUTE_SOUND = b'ayStageMuteSound'
    STAGE_UNMUTE_SOUND = b'ayStageUnmuteSound'
    DESTROY_ARMORY_YARD_MAIN_VIEW = b'armoryYardEvents/destroyMainView'
    SHOW_ARMORY_YARD_BUY_VIEW = b'armoryYardEvents/showBuyView'
    SHOW_ARMORY_YARD_SHOP_BUY_VIEW = b'armoryYardEvents/shopBuyView'
    SHOW_ARMORY_YARD_REROLL_VIEW = b'armoryYardEvents/rerollView'
    POI_ACTIVATED = b'ayPoiActivated'
    STAGE_CLICKED = b'ayStageClicked'


class Achievements20Event(HasCtxEvent):
    LAYOUT_CHANGED = b'layoutChanged'
    CLOSE_SUMMARY_VIEW = b'closeSummaryView'
    CLOSE_EDIT_VIEW = b'closeEditView'


class PrebattleEvent(HasCtxEvent):
    SWITCHED = b'PrebattleEvent/SWITCHED'
    NOT_SWITCHED = b'PrebattleEvent/NOT_SWITCHED'


class HangarCrewWidgetViewEvent(HasCtxEvent):
    GF_RESIZED = b'hangarCrewWidgetViewEvent/gfResized'


class CosmicEvent(SharedEvent):
    OPEN_COSMIC = b'openCosmic'


class SurveyEvent(SharedEvent):
    SURVEY_FINISHED = b'onSurveyFinished'


class LobbyMarkersManagerEvent(HasCtxEvent):
    ON_MARKER_ADDED = b'lobbyMarkersManager/added'
    ON_MARKER_REMOVED = b'lobbyMarkersManager/removed'
    ON_MARKER_REQUEST = b'lobbyMarkersManager/request'
    ON_MARKER_RESPONSE = b'lobbyMarkersManager/response'


class RespawnViewEvent(SharedEvent):
    ON_RESPAWN_VIEW_SHOW = b'ON_RESPAWN_VIEW_SHOW'
    ON_RESPAWN_VIEW_HIDE = b'ON_RESPAWN_VIEW_HIDE'


class SummerSaleViewEvent(SharedEvent):
    ON_CLOSE_REWARD_VIEW = b'ON_CLOSE_REWARD_VIEW'
