from __future__ import absolute_import
from collections import defaultdict, namedtuple, OrderedDict
from future.utils import viewitems
BATTLE_REPO = 1
EQUIPMENT_ITEMS = 2
SCALEFORM_COMMON_PACKAGES = 3
SCALEFORM_LOBBY_PACKAGES = 4
SCALEFORM_BATTLE_PACKAGES = 5
LOBBY_TOOLTIP_BUILDERS = 6
BATTLE_TOOLTIP_BUILDERS = 7
GAME_CONTROLLERS = 8
QUEUE = 9
QUEUE_ENTRY_POINT = 10
UNIT_ENTITY = 11
UNIT_ENTRY_POINT = 12
UNIT_ENTITY_BY_TYPE = 13
UNIT_ENTRY_POINT_BY_TYPE = 14
PBR_STORAGE = 15
PRB_INVITE_HTML_FORMATTER = 16
NOTIFICATIONS_LISTENERS = 17
NOTIFICATIONS_ACTIONS_HANDLERS = 18
MESSENGER_CLIENT_FORMATTERS = 19
TOKEN_QUEST_SUBFORMATTERS = 20
MODE_SELECTOR_ITEM = 21
MODE_SELECTOR_TOOLTIP = 22
BANNER_ENTRY_POINT_VALIDATOR = 23
BATTLE_QUEUE_PROVIDER = 24
BATTLE_TIPS_CRITERIA = 25
ARENA_DESCRIPTION = 26
ARENA_SQUAD_FINDER = 27
INGAME_HELP_PAGES_BUILDERS = 28
QUEST_BUILDERS = 29
AWARD_CONTROLLER_HANDLERS = 30
CAN_SELECT_PRB_ENTITY = 31
BATTLE_RESULT_STATS_CONTROLLER = 32
SEASON_PROVIDER_HANDLER = 33
MESSENGER_SERVER_FORMATTERS = 34
CAROUSEL_EVENTS_ENTRIES = 35
BANNER_ENTRY_POINT_LUI_RULE = 36
LIMITED_UI_TOKENS = 37
PRB_MODE_NAME_KWARGS = 38
QUEUE_MODE_NAME_KWARGS = 39
BONUS_TYPE_MODE_NAME_KWARGS = 40
PRB_CONDITION_ICON = 41
HANGAR_PRESETS_READERS = 42
HANGAR_DYNAMIC_GUI_PROVIDERS = 43
AMMUNITION_PANEL_VIEW = 44
VEHICLE_VIEW_STATE = 45
DYN_OBJ_CACHE = 46
SHARED_REPO = 47
CONTEXT_MENU_COMMANDS = 48
CONTEXT_MENU_OPTION_BUILDER = 49
ADVANCED_CHAT_COMPONENT = 50
BATTLE_CHANEL_CONTROLLER = 51
HIT_DIRECTION_CONTROLLER = 52
CUSTOMIZATION_HANGAR_AVAILABLE = 53
OPTIMIZED_VIEWS = 54
REPLAY_MODE_TAG = 55
QUEST_FLAGS = 56
BATTLE_RESULTS_STATS_SORTING = 57
LOOTBOX_AUTOOPEN_SUBFORMATTERS = 58
EQUIPMENT_TRIGGERS = 59
LOW_PRIORITY_WULF_WINDOWS = 60
TRAINING_ROOM_EXTERNAL_HANDLERS = 61
LOBBY_HEADER_TAB = 62
GAMEFACE_NOTIFICATIONS = 63
GAME_MODE_ARENA_INFO_KEYS = 64
AMMUNITION_SETUP_VIEW = 65
GUI_ITEMS_CACHE_INVALIDATOR = 66
IGNORED_MODE_FOR_AUTO_SELECTED_VEHICLE = 67
HANGAR_MENU_ITEMS = 68
BONUS_TOKENS = 69
VIEWS_FOR_MONITORING = 70
LIFECYCLE_HANDLED_SUB_VIEWS = 71
BATTLE_BUTTON_MANUAL_CONTROL = 72
PREBATTLE_CONTROL_MODE = 73
CLASS_TAG_GETTER = 74
BATTLE_RESULT_PROGRESS_PRESENTER = 75
BATTLE_ENTRY = 76
DYNAMIC_VIEWS_FOR_MONITORING = 77
VEHICLE_READY_CHECKERS = 78
POSTBATTLE_SQUAD_FINDER = 79
POSTMORTEM_INFO_VIEW = 89
MODE_HIDDEN_VEHICLES_CRITERIA = 81
PBS_ENTRY_STATE = 82
UNIT_MEMBERS_ORDER_KEY = 83
TEAM_VOIP_SUPPORT = 84

class CollectEventsManager(object):

    def __init__(self):
        self.__handlers = defaultdict(list)
        return

    def addListener(self, eventID, callback):
        self.__handlers[eventID].append(callback)
        return

    def handleEvent(self, eventID, ctx):
        for callback in self.__handlers[eventID]:
            callback(ctx)

        return ctx

    @property
    def handlers(self):
        return self.__handlers


__collectEM = CollectEventsManager()

def registerScaleformBattlePackages(guiType, packages):

    def onCollect(ctx):
        ctx[b'packages'].extend(packages)
        return

    __collectEM.addListener((SCALEFORM_BATTLE_PACKAGES, guiType), onCollect)
    return


def collectScaleformBattlePackages(guiType):
    return __collectEM.handleEvent((SCALEFORM_BATTLE_PACKAGES, guiType), {b'packages': []})[b'packages']


def registerScaleformLobbyPackages(packages):

    def onCollect(ctx):
        ctx[b'packages'].extend(packages)
        return

    __collectEM.addListener(SCALEFORM_LOBBY_PACKAGES, onCollect)
    return


def collectScaleformLobbyPackages():
    return __collectEM.handleEvent(SCALEFORM_LOBBY_PACKAGES, {b'packages': []})[b'packages']


def registerBattleTooltipsBuilders(builders):

    def onCollect(ctx):
        ctx[b'builders'].extend(builders)
        return

    __collectEM.addListener(BATTLE_TOOLTIP_BUILDERS, onCollect)
    return


def collectBattleTooltipsBuilders():
    return __collectEM.handleEvent(BATTLE_TOOLTIP_BUILDERS, {b'builders': []})[b'builders']


def registerLobbyTooltipsBuilders(builders):

    def onCollect(ctx):
        ctx[b'builders'].extend(builders)
        return

    __collectEM.addListener(LOBBY_TOOLTIP_BUILDERS, onCollect)
    return


def collectLobbyTooltipsBuilders():
    return __collectEM.handleEvent(LOBBY_TOOLTIP_BUILDERS, {b'builders': []})[b'builders']


def registerEquipmentItem(equipmentName, itemCls, replayItemCls):

    def onCollect(ctx):
        descriptor, quantity, stage, timeRemaining, totalTime = ctx[b'args']
        cls = replayItemCls if ctx[b'isReplay'] else itemCls
        ctx[b'item'] = cls(descriptor, quantity, stage, timeRemaining, totalTime, descriptor.tags)
        return

    __collectEM.addListener((EQUIPMENT_ITEMS, equipmentName), onCollect)
    return


def collectEquipmentItem(equipmentName, isReplay, args):
    return __collectEM.handleEvent((EQUIPMENT_ITEMS, equipmentName), {b'args': args, b'isReplay': isReplay}).get(b'item', None)


def registerEquipmentTrigger(equipmentPrefix, itemCls, replayItemCls):

    def onCollect(ctx):
        if not ctx[b'equipmentName'].startswith(equipmentPrefix):
            return
        cls = replayItemCls if ctx[b'isReplay'] else itemCls
        ctx[b'item'] = cls
        return

    __collectEM.addListener(EQUIPMENT_TRIGGERS, onCollect)
    return


def collectEquipmentTrigger(equipmentName, isReplay):
    return __collectEM.handleEvent(EQUIPMENT_TRIGGERS, {b'equipmentName': equipmentName, b'isReplay': isReplay}).get(b'item', None)


def registerGameControllers(controllersList):

    def onCollect(ctx):
        configurator = ctx[b'configurator']
        for iface, controllerCls, replace in controllersList:
            configurator(iface, controllerCls(), replace)

        return

    __collectEM.addListener(GAME_CONTROLLERS, onCollect)
    return


def collectGameControllers(configurator):
    __collectEM.handleEvent(GAME_CONTROLLERS, ctx={b'configurator': configurator})
    return


def registerBattleControllerRepo(guiType, repoCls):

    def onCollect(ctx):
        ctx[b'repo'] = repoCls.create(ctx[b'setup']) if repoCls else None
        return

    __collectEM.addListener((BATTLE_REPO, guiType), onCollect)
    return


def collectBattleControllerRepo(guiType, setup):
    ctx = __collectEM.handleEvent((BATTLE_REPO, guiType), ctx={b'setup': setup})
    return (ctx.get(b'repo'), b'repo' in ctx)


def registerSharedControllerRepo(guiType, repoCls):

    def onCollect(ctx):
        ctx[b'repo'] = repoCls.create(ctx[b'setup']) if repoCls else None
        return

    __collectEM.addListener((SHARED_REPO, guiType), onCollect)
    return


def collectSharedControllerRepo(guiType, setup):
    ctx = __collectEM.handleEvent((SHARED_REPO, guiType), ctx={b'setup': setup})
    return (ctx.get(b'repo'), b'repo' in ctx)


def registerQueueEntity(queueType, queueCls):

    def onCollect(ctx):
        ctx[b'queue'] = queueCls()
        return

    __collectEM.addListener((QUEUE, queueType), onCollect)
    return


def collectQueueEntity(queueType):
    return __collectEM.handleEvent((QUEUE, queueType), ctx={}).get(b'queue')


def registerEntryPoint(actionName, entryPointCls):

    def onCollect(ctx):
        ctx[b'entry'] = entryPointCls()
        return

    __collectEM.addListener((QUEUE_ENTRY_POINT, actionName), onCollect)
    return


def collectEntryPoint(queueType):
    return __collectEM.handleEvent((QUEUE_ENTRY_POINT, queueType), ctx={}).get(b'entry')


def registerUnitEntity(pbrType, entityCls):

    def onCollect(ctx):
        ctx[b'entity'] = entityCls()
        return

    __collectEM.addListener((UNIT_ENTITY, pbrType), onCollect)
    return


def collectUnitEntity(pbrType):
    return __collectEM.handleEvent((UNIT_ENTITY, pbrType), ctx={}).get(b'entity')


def registerUnitEntryPoint(actionName, entryPointCls):

    def onCollect(ctx):
        ctx[b'entry'] = entryPointCls()
        return

    __collectEM.addListener((UNIT_ENTRY_POINT, actionName), onCollect)
    return


def collectUnitEntryPoint(queueType):
    return __collectEM.handleEvent((UNIT_ENTRY_POINT, queueType), ctx={}).get(b'entry')


def registerUnitEntryPointByType(pbrType, entryPointCls):

    def onCollect(ctx):
        ctx[b'entry'] = entryPointCls()
        return

    __collectEM.addListener((UNIT_ENTRY_POINT_BY_TYPE, pbrType), onCollect)
    return


def collectUnitEntryPointByType(pbrType):
    return __collectEM.handleEvent((UNIT_ENTRY_POINT_BY_TYPE, pbrType), ctx={}).get(b'entry')


def registerLegacyEntity(pbrType, entityCls):

    def onCollect(ctx):
        ctx[b'entity'] = entityCls
        return

    __collectEM.addListener((UNIT_ENTITY, pbrType), onCollect)
    return


def collectLegacyEntity(pbrType):
    return __collectEM.handleEvent((UNIT_ENTITY, pbrType), ctx={}).get(b'entity')


def registerLegacyEntryPoint(actionName, entryPointCls):

    def onCollect(ctx):
        ctx[b'entry'] = entryPointCls()
        return

    __collectEM.addListener((UNIT_ENTRY_POINT, actionName), onCollect)
    return


def collectLegacyEntryPoint(queueType):
    return __collectEM.handleEvent((UNIT_ENTRY_POINT, queueType), ctx={}).get(b'entry')


def registerLegacyEntryPointByType(pbrType, entryPointCls):

    def onCollect(ctx):
        ctx[b'entry'] = entryPointCls()
        return

    __collectEM.addListener((UNIT_ENTRY_POINT_BY_TYPE, pbrType), onCollect)
    return


def collectLegacyEntryPointByType(pbrType):
    return __collectEM.handleEvent((UNIT_ENTRY_POINT_BY_TYPE, pbrType), ctx={}).get(b'entry')


def registerPrbStorage(name, storage):

    def onCollect(ctx):
        ctx[b'storage'] = storage
        return

    __collectEM.addListener((PBR_STORAGE, name), onCollect)
    return


def collectPrbStorage(name):
    return __collectEM.handleEvent((PBR_STORAGE, name), ctx={}).get(b'storage')


def collectAllStorages():
    storages = []
    for eventID, handlers in viewitems(__collectEM.handlers):
        if isinstance(eventID, tuple) and eventID[0] == PBR_STORAGE:
            for handler in handlers:
                ctx = {}
                handler(ctx)
                storages.append(ctx[b'storage'])

    return storages


def registerArenaDescrs(guiType, arenaDescrClass):

    def onCollect(ctx):
        ctx[b'arena_descr_class'] = arenaDescrClass
        return

    __collectEM.addListener((ARENA_DESCRIPTION, guiType), onCollect)
    return


def collectArenaDescrs(guiType):
    return __collectEM.handleEvent((ARENA_DESCRIPTION, guiType), ctx={}).get(b'arena_descr_class')


def registerSquadFinder(guiType, squadFinderClass, rosterClass):

    def onCollect(ctx):
        ctx[b'squad_finder_data'] = (
         squadFinderClass, rosterClass)
        return

    __collectEM.addListener((ARENA_SQUAD_FINDER, guiType), onCollect)
    return


def collectSquadFinder(guiType):
    return __collectEM.handleEvent((ARENA_SQUAD_FINDER, guiType), ctx={}).get(b'squad_finder_data', (None, None))


def registerNotificationsListeners(listenerClasses):

    def onCollect(ctx):
        ctx[b'listeners'].extend(listenerCls() for listenerCls in listenerClasses)
        return

    __collectEM.addListener(NOTIFICATIONS_LISTENERS, onCollect)
    return


def collectAllNotificationsListeners():
    ctx = {b'listeners': []}
    for handler in __collectEM.handlers[NOTIFICATIONS_LISTENERS]:
        handler(ctx)

    return ctx[b'listeners']


def registerNotificationsActionsHandlers(handlersClasses):

    def onCollect(ctx):
        ctx[b'handlers'].extend(handlersClasses)
        return

    __collectEM.addListener(NOTIFICATIONS_ACTIONS_HANDLERS, onCollect)
    return


def collectAllNotificationsActionsHandlers():
    ctx = {b'handlers': []}
    for handler in __collectEM.handlers[NOTIFICATIONS_ACTIONS_HANDLERS]:
        handler(ctx)

    return ctx[b'handlers']


def registerMessengerClientFormatter(msgType, formatter):

    def onCollect(ctx):
        ctx[b'formatter'] = formatter
        return

    __collectEM.addListener((MESSENGER_CLIENT_FORMATTERS, msgType), onCollect)
    return


def collectMessengerClientFormatter(msgType):
    return __collectEM.handleEvent((MESSENGER_CLIENT_FORMATTERS, msgType), ctx={}).get(b'formatter')


def registerMessengerServerFormatter(msgType, formatter, replace=False):

    def onCollect(ctx):
        if not replace:
            pass
        ctx[b'formatter'] = formatter
        return

    __collectEM.addListener((MESSENGER_SERVER_FORMATTERS, msgType), onCollect)
    return


def collectMessengerServerFormatter(msgType):
    return __collectEM.handleEvent((MESSENGER_SERVER_FORMATTERS, msgType), ctx={}).get(b'formatter')


def registerTokenQuestsSubFormatter(formatter):

    def onCollect(ctx):
        ctx[b'formatters'].append(formatter)
        return

    __collectEM.addListener(TOKEN_QUEST_SUBFORMATTERS, onCollect)
    return


def registerTokenQuestsSubFormatters(formatters):

    def onCollect(ctx):
        ctx[b'formatters'].extend(formatters)
        return

    __collectEM.addListener(TOKEN_QUEST_SUBFORMATTERS, onCollect)
    return


def collectTokenQuestsSubFormatters():
    return __collectEM.handleEvent(TOKEN_QUEST_SUBFORMATTERS, ctx={b'formatters': []}).get(b'formatters')


def registerLootBoxAutoOpenSubFormatter(formatter):

    def onCollect(ctx):
        ctx[b'formatters'].append(formatter)
        return

    __collectEM.addListener(LOOTBOX_AUTOOPEN_SUBFORMATTERS, onCollect)
    return


def registerLootBoxAutoOpenSubFormatters(formatters):

    def onCollect(ctx):
        ctx[b'formatters'].extend(formatters)
        return

    __collectEM.addListener(LOOTBOX_AUTOOPEN_SUBFORMATTERS, onCollect)
    return


def collectLootBoxAutoOpenSubFormatters():
    return __collectEM.handleEvent(LOOTBOX_AUTOOPEN_SUBFORMATTERS, ctx={b'formatters': []}).get(b'formatters')


def registerPrbInviteHtmlFormatter(prbType, formatterCls):

    def onCollect(ctx):
        ctx[b'formatter'] = formatterCls()
        return

    __collectEM.addListener((PRB_INVITE_HTML_FORMATTER, prbType), onCollect)
    return


def registerPrbInvitesHtmlFormatter(prbTypes, formatterCls):
    for prbType in prbTypes:
        registerPrbInviteHtmlFormatter(prbType, formatterCls)

    return


def collectPrbInviteHtmlFormatter(prbType):
    return __collectEM.handleEvent((PRB_INVITE_HTML_FORMATTER, prbType), ctx={}).get(b'formatter')


def registerModeNameKwargsGetterByPrb(prbType, prbModeNameKwargsKwargsGetter):

    def onCollect(ctx):
        ctx[b'prbModeNameKwargsGetter'] = prbModeNameKwargsKwargsGetter
        return

    __collectEM.addListener((PRB_MODE_NAME_KWARGS, prbType), onCollect)
    return


def collectModeNameKwargsByPrbType(prbType):
    getter = __collectEM.handleEvent((PRB_MODE_NAME_KWARGS, prbType), ctx={}).get(b'prbModeNameKwargsGetter')
    if getter is not None:
        return getter()
    else:
        return {}


def registerModeNameKwargsGetterByQueue(queueType, queueModeNameKwargsKwargsGetter):

    def onCollect(ctx):
        ctx[b'queueModeNameKwargsGetter'] = queueModeNameKwargsKwargsGetter
        return

    __collectEM.addListener((QUEUE_MODE_NAME_KWARGS, queueType), onCollect)
    return


def collectModeNameKwargsByQueueType(queueType):
    getter = __collectEM.handleEvent((QUEUE_MODE_NAME_KWARGS, queueType), ctx={}).get(b'queueModeNameKwargsGetter')
    if getter is not None:
        return getter()
    else:
        return {}


def registerModeNameKwargsGetterByBonusType(bonusType, prbModeNameKwargsKwargsGetter):

    def onCollect(ctx):
        ctx[b'bonusModeNameKwargsGetter'] = prbModeNameKwargsKwargsGetter
        return

    __collectEM.addListener((BONUS_TYPE_MODE_NAME_KWARGS, bonusType), onCollect)
    return


def collectModeNameKwargsByBonusType(bonusType):
    getter = __collectEM.handleEvent((BONUS_TYPE_MODE_NAME_KWARGS, bonusType), ctx={}).get(b'bonusModeNameKwargsGetter')
    if getter is not None:
        return getter()
    else:
        return {}


def registerPrebattleConditionIconGetter(bonusType, prebattleConditionIconGetter):

    def onCollect(ctx):
        ctx[b'prbConditionIconGetter'] = prebattleConditionIconGetter
        return

    __collectEM.addListener((PRB_CONDITION_ICON, bonusType), onCollect)
    return


def collectPrebattleConditionIcon(bonusType):
    getter = __collectEM.handleEvent((PRB_CONDITION_ICON, bonusType), ctx={}).get(b'prbConditionIconGetter')
    if getter is not None:
        return getter()
    else:
        return


def registerModeSelectorItem(prbActionName, itemCls):

    def onCollect(ctx):
        ctx[b'item'] = itemCls
        return

    __collectEM.addListener((MODE_SELECTOR_ITEM, prbActionName), onCollect)
    return


def collectModeSelectorItem(prbActionName):
    return __collectEM.handleEvent((MODE_SELECTOR_ITEM, prbActionName), ctx={}).get(b'item')


def registerModeSelectorTooltips(simpleTooltipIds, contentTooltipsMap):

    def onCollect(ctx):
        ctx[b'modeSelectorTooltips'][b'simpleTooltipIds'].extend(simpleTooltipIds)
        ctx[b'modeSelectorTooltips'][b'contentTooltipsMap'].update(contentTooltipsMap)
        return

    __collectEM.addListener(MODE_SELECTOR_TOOLTIP, onCollect)
    return


def collectModeSelectorTooltips():
    return __collectEM.handleEvent(MODE_SELECTOR_TOOLTIP, ctx={b'modeSelectorTooltips': {b'simpleTooltipIds': [], b'contentTooltipsMap': {}}}).get(b'modeSelectorTooltips')


def registerBannerEntryPointValidator(alias, validator):

    def onCollect(ctx):
        ctx[b'validator'] = validator
        return

    __collectEM.addListener((BANNER_ENTRY_POINT_VALIDATOR, alias), onCollect)
    return


def collectBannerEntryPointValidator(alias):
    return __collectEM.handleEvent((BANNER_ENTRY_POINT_VALIDATOR, alias), ctx={}).get(b'validator')


def registerBannerEntryPointLUIRule(alias, ruleID):

    def onCollect(ctx):
        ctx[b'ruleID'] = ruleID
        return

    __collectEM.addListener((BANNER_ENTRY_POINT_LUI_RULE, alias), onCollect)
    return


def registerCarouselEventEntryPoint(viewID, viewClass):

    def onCollect(ctx):
        ctx[b'carouselEventEntries'][viewID] = viewClass
        return

    __collectEM.addListener(CAROUSEL_EVENTS_ENTRIES, onCollect)
    return


def collectCarouselEventEntryPoints():
    return __collectEM.handleEvent(CAROUSEL_EVENTS_ENTRIES, {b'carouselEventEntries': {}})[b'carouselEventEntries']


def registerBattleQueueProvider(queueType, providerCls):

    def onCollect(ctx):
        ctx[b'providerCls'] = providerCls
        return

    __collectEM.addListener((BATTLE_QUEUE_PROVIDER, queueType), onCollect)
    return


def collectBattleQueueProvider(queueType):
    return __collectEM.handleEvent((BATTLE_QUEUE_PROVIDER, queueType), ctx={}).get(b'providerCls')


def registerBattleTipCriteria(guiType, criteriaCls):

    def onCollect(ctx):
        ctx[b'criteriaCls'] = criteriaCls
        return

    __collectEM.addListener((BATTLE_TIPS_CRITERIA, guiType), onCollect)
    return


def registerBattleTipsCriteria(guiTypes, criteriaCls):
    for guiType in guiTypes:
        registerBattleTipCriteria(guiType, criteriaCls)

    return


def collectBattleTipsCriteria(guiType):
    return __collectEM.handleEvent((BATTLE_TIPS_CRITERIA, guiType), ctx={}).get(b'criteriaCls')


def registerIngameHelpPagesBuilder(builder):

    def onCollect(ctx):
        ctx[b'builders'].append(builder)
        return

    __collectEM.addListener(INGAME_HELP_PAGES_BUILDERS, onCollect)
    return


def registerIngameHelpPagesBuilders(builders):

    def onCollect(ctx):
        ctx[b'builders'].extend(builders)
        return

    __collectEM.addListener(INGAME_HELP_PAGES_BUILDERS, onCollect)
    return


def collectIngameHelpPagesBuilders():
    return __collectEM.handleEvent(INGAME_HELP_PAGES_BUILDERS, {b'builders': []})[b'builders']


def registerQuestBuilder(questBuilder):

    def onCollect(ctx):
        ctx[b'questBuilders'].append(questBuilder)
        return

    __collectEM.addListener(QUEST_BUILDERS, onCollect)
    return


def registerQuestBuilders(questBuilders):

    def onCollect(ctx):
        ctx[b'questBuilders'].extend(questBuilders)
        return

    __collectEM.addListener(QUEST_BUILDERS, onCollect)
    return


def collectQuestBuilders():
    return __collectEM.handleEvent(QUEST_BUILDERS, {b'questBuilders': []})[b'questBuilders']


def registerAwardControllerHandler(handler):

    def onCollect(ctx):
        ctx[b'handlers'].append(handler)
        return

    __collectEM.addListener(AWARD_CONTROLLER_HANDLERS, onCollect)
    return


def registerAwardControllerHandlers(handlers):

    def onCollect(ctx):
        ctx[b'handlers'].extend(handlers)
        return

    __collectEM.addListener(AWARD_CONTROLLER_HANDLERS, onCollect)
    return


def collectAwardControllerHandlers():
    return __collectEM.handleEvent(AWARD_CONTROLLER_HANDLERS, {b'handlers': []})[b'handlers']


def registerCanSelectPrbEntity(queueType, itemFun):

    def onCollect(ctx):
        ctx[b'itemFun'] = itemFun
        return

    __collectEM.addListener((CAN_SELECT_PRB_ENTITY, queueType), onCollect)
    return


def collectCanSelectPrbEntity(queueType):
    return __collectEM.handleEvent((
     CAN_SELECT_PRB_ENTITY, queueType), ctx={}).get(b'itemFun', (lambda *args, **kwargs: False))


def registerBattleResultStatsCtrl(bonusType, itemCls):

    def onCollect(ctx):
        ctx[b'item'] = itemCls
        return

    __collectEM.addListener((BATTLE_RESULT_STATS_CONTROLLER, bonusType), onCollect)
    return


def collectBattleResultStatsCtrl(bonusType):
    return __collectEM.handleEvent((BATTLE_RESULT_STATS_CONTROLLER, bonusType), ctx={}).get(b'item', None)


def registerBattleResultsEntryState(bonusType, pbsEntryCls):

    def onCollect(ctx):
        ctx[b'pbsEntryCls'] = pbsEntryCls
        return

    __collectEM.addListener((PBS_ENTRY_STATE, bonusType), onCollect)
    return


def collectBattleResultsEntryState(bonusType):
    return __collectEM.handleEvent((PBS_ENTRY_STATE, bonusType), ctx={}).get(b'pbsEntryCls', None)


def registerProgressionPresenter(questCategory, itemClsTuplesList):

    def onCollect(ctx):
        ctx[b'questCategory'][questCategory] = itemClsTuplesList
        return

    __collectEM.addListener(BATTLE_RESULT_PROGRESS_PRESENTER, onCollect)
    return


def collectProgressionPresenters():
    return __collectEM.handleEvent(BATTLE_RESULT_PROGRESS_PRESENTER, {b'questCategory': {}})[b'questCategory']


def registerSeasonProviderHandler(seasonType, seasonControllerHandler):

    def onCollect(ctx):
        ctx[seasonType] = seasonControllerHandler
        return

    __collectEM.addListener((SEASON_PROVIDER_HANDLER, seasonType), onCollect)
    return


def collectSeasonProviderHandler(seasonType):
    return __collectEM.handleEvent((SEASON_PROVIDER_HANDLER, seasonType), ctx={}).get(seasonType, None)


def registerLimitedUIToken(tokenInfo):

    def onCollect(ctx):
        ctx[b'tokens'].append(tokenInfo)
        return

    __collectEM.addListener(LIMITED_UI_TOKENS, onCollect)
    return


def registerLimitedUITokens(tokensInfos):

    def onCollect(ctx):
        ctx[b'tokens'].extend(tokensInfos)
        return

    __collectEM.addListener(LIMITED_UI_TOKENS, onCollect)
    return


def collectLimitedUITokens():
    return __collectEM.handleEvent(LIMITED_UI_TOKENS, ctx={b'tokens': []})[b'tokens']


def registerHangarDynamicGuiProvider(queueType, processor):

    def onCollect(ctx):
        ctx[b'dynamicGuiProviders'][queueType] = processor(ctx[b'config'])
        return

    __collectEM.addListener(HANGAR_DYNAMIC_GUI_PROVIDERS, onCollect)
    return


def collectHangarDynamicGuiProviders(config):
    return __collectEM.handleEvent(HANGAR_DYNAMIC_GUI_PROVIDERS, {b'dynamicGuiProviders': {}, b'config': config})[b'dynamicGuiProviders']


def registerHangarPresetsReader(reader):

    def onCollect(ctx):
        ctx[b'presetsReaders'].append(reader)
        return

    __collectEM.addListener(HANGAR_PRESETS_READERS, onCollect)
    return


def collectHangarPresetsReaders():
    return __collectEM.handleEvent(HANGAR_PRESETS_READERS, ctx={b'presetsReaders': []})[b'presetsReaders']


def registerAmmunitionPanelView(viewCls):

    def onCollect(ctx):
        ctx[viewCls.__name__] = viewCls
        return

    __collectEM.addListener((AMMUNITION_PANEL_VIEW, viewCls.__name__), onCollect)
    return


def collectAmmunitionPanelView(viewAlias):
    return __collectEM.handleEvent((AMMUNITION_PANEL_VIEW, viewAlias), ctx={}).get(viewAlias, None)


def registerAmmunitionSetupView(viewCls):

    def onCollect(ctx):
        ctx[viewCls.__name__] = viewCls
        return

    __collectEM.addListener((AMMUNITION_SETUP_VIEW, viewCls.__name__), onCollect)
    return


def collectAmmunitionSetupView(viewAlias):
    return __collectEM.handleEvent((AMMUNITION_SETUP_VIEW, viewAlias), ctx={}).get(viewAlias, None)


def registerVehicleViewState(viewState):

    def onCollect(ctx):
        ctx[b'viewStates'].append(viewState)
        return

    __collectEM.addListener(VEHICLE_VIEW_STATE, onCollect)
    return


def collectVehicleViewStates():
    return __collectEM.handleEvent(VEHICLE_VIEW_STATE, ctx={b'viewStates': []})[b'viewStates']


def registerDynObjCache(arenaGuiType, dynCache):

    def onCollect(ctx):
        ctx[b'dynCache'] = dynCache
        return

    __collectEM.addListener((DYN_OBJ_CACHE, arenaGuiType), onCollect)
    return


def collectDynObjCache(arenaGuiType):
    return __collectEM.handleEvent((DYN_OBJ_CACHE, arenaGuiType), ctx={}).get(b'dynCache')


def registerLobbyContexMenuHandler(optionID, commandHandler):

    def onCollect(ctx):
        ctx[optionID] = commandHandler
        return

    __collectEM.addListener((CONTEXT_MENU_COMMANDS, optionID), onCollect)
    return


def collectLobbyContexMenuHandler(optionID):
    return __collectEM.handleEvent((CONTEXT_MENU_COMMANDS, optionID), ctx={}).get(optionID, None)


def registerLobbyContexMenuOptionBuilder(optionBuilder):

    def onCollect(ctx):
        ctx[b'cmOptionBuilders'].append(optionBuilder)
        return

    __collectEM.addListener(CONTEXT_MENU_OPTION_BUILDER, onCollect)
    return


def collectLobbyContexMenuOptionBuilders():
    return __collectEM.handleEvent(CONTEXT_MENU_OPTION_BUILDER, {b'cmOptionBuilders': []})[b'cmOptionBuilders']


def registerAdvancedChatComponent(bonusType, component):

    def onCollect(ctx):
        ctx[bonusType] = component
        return

    __collectEM.addListener((ADVANCED_CHAT_COMPONENT, bonusType), onCollect)
    return


def collectAdvancedChatComponent(bonusType):
    return __collectEM.handleEvent((ADVANCED_CHAT_COMPONENT, bonusType), ctx={}).get(bonusType, None)


def registerBattleChanelController(guiType, battleChanelType, controller):

    def onCollect(ctx):
        ctx[guiType] = controller
        return

    __collectEM.addListener((BATTLE_CHANEL_CONTROLLER, battleChanelType), onCollect)
    return


def collectBattleChanelController(battleChanelType, guiType):
    return __collectEM.handleEvent((BATTLE_CHANEL_CONTROLLER, battleChanelType), ctx={}).get(guiType, None)


def registerHitDirectionController(guiType, hitDirectionType, hitDirectionPlayerType):

    def onCollect(ctx):
        ctx[guiType] = (
         hitDirectionType, hitDirectionPlayerType)
        return

    __collectEM.addListener((HIT_DIRECTION_CONTROLLER, guiType), onCollect)
    return


def collectHitDirectionController(guiType, defaultHitDirectionType, defaultHitDirectionPlayerType):
    defaultValue = (
     defaultHitDirectionType, defaultHitDirectionPlayerType)
    return __collectEM.handleEvent((HIT_DIRECTION_CONTROLLER, guiType), ctx={}).get(guiType, defaultValue)


def registerCustomizationHangarDecorator(handler):

    def onCollect(ctx):
        ctx[b'handlers'].append(handler)
        return

    __collectEM.addListener(CUSTOMIZATION_HANGAR_AVAILABLE, onCollect)
    return


def collectCustomizationHangarDecorator():
    return __collectEM.handleEvent(CUSTOMIZATION_HANGAR_AVAILABLE, {b'handlers': []})[b'handlers']


def registerOptimizedViews(optimizedViewsSettings):

    def onCollect(ctx):
        ctx[b'optimizedViewsSettings'].update(optimizedViewsSettings)
        return

    __collectEM.addListener(OPTIMIZED_VIEWS, onCollect)
    return


def collectOptimizedViews():
    return __collectEM.handleEvent(OPTIMIZED_VIEWS, ctx={b'optimizedViewsSettings': {}})[b'optimizedViewsSettings']


def registerReplayModeTag(guiType, replayModeTag):

    def onCollect(ctx):
        ctx[b'replayModeTag'] = replayModeTag
        return

    __collectEM.addListener((REPLAY_MODE_TAG, guiType), onCollect)
    return


def collectReplayModeTag(guiType):
    return __collectEM.handleEvent((REPLAY_MODE_TAG, guiType), ctx={}).get(b'replayModeTag', b'')


def registerQuestFlag(questFlagType, flagCls):

    def onCollect(ctx):
        ctx[b'questFlags'][questFlagType] = flagCls
        return

    __collectEM.addListener(QUEST_FLAGS, onCollect)
    return


def collectQuestFlags():
    return __collectEM.handleEvent(QUEST_FLAGS, {b'questFlags': {}})[b'questFlags']


def registerBattleResultsStatsSorting(bonusType, sortingKey):

    def onCollect(ctx):
        ctx[b'sortingKey'][bonusType] = sortingKey
        return

    __collectEM.addListener(BATTLE_RESULTS_STATS_SORTING, onCollect)
    return


def collectBattleResultsStatsSorting():
    return __collectEM.handleEvent(BATTLE_RESULTS_STATS_SORTING, {b'sortingKey': {}})[b'sortingKey']


def registerLowPriorityWulfWindows(layoutsID):

    def onCollect(ctx):
        ctx.extend(layoutsID)
        return

    __collectEM.addListener(LOW_PRIORITY_WULF_WINDOWS, onCollect)
    return


def collectLowPriorityWindows():
    return __collectEM.handleEvent(LOW_PRIORITY_WULF_WINDOWS, ctx=[])


def registerTrainingRoomExternalHandler(guiType, handler):

    def onCollect(ctx):
        ctx[b'trainingRoomHandlers'][guiType] = handler
        return

    __collectEM.addListener(TRAINING_ROOM_EXTERNAL_HANDLERS, onCollect)
    return


def collectTrainingRoomExternalHandlers():
    return __collectEM.handleEvent(TRAINING_ROOM_EXTERNAL_HANDLERS, {b'trainingRoomHandlers': {}})[b'trainingRoomHandlers']


def registerLobbyHeaderTab(alias, tabInfo):

    def onCollect(ctx):
        ctx[b'tabs'][alias] = tabInfo
        return

    __collectEM.addListener(LOBBY_HEADER_TAB, onCollect)
    return


def collectLobbyHeaderTabs():
    return __collectEM.handleEvent(LOBBY_HEADER_TAB, {b'tabs': {}})[b'tabs']


def registerMenuItems(hangarMode, menuItems):

    def onCollect(ctx):
        ctx[b'menuItems'][hangarMode].update(menuItems)
        return

    __collectEM.addListener(HANGAR_MENU_ITEMS, onCollect)
    return


def collectMenuItems(hangarMode):
    return __collectEM.handleEvent(HANGAR_MENU_ITEMS, {b'menuItems': (defaultdict(OrderedDict))})[b'menuItems'][hangarMode]


def registerGamefaceNotifications(gamefaceNotifications):

    def onCollect(ctx):
        ctx[b'gamefaceNotifications'].update(gamefaceNotifications)
        return

    __collectEM.addListener(GAMEFACE_NOTIFICATIONS, onCollect)
    return


def collectGamefaceNotifications():
    return __collectEM.handleEvent(GAMEFACE_NOTIFICATIONS, ctx={b'gamefaceNotifications': {}})[b'gamefaceNotifications']


def registerGameModeArenaInfoKeys(guiType, gameModeSpecificKeys):

    def onCollect(ctx):
        ctx[b'game_mode_specific_keys'] = gameModeSpecificKeys
        return

    __collectEM.addListener((GAME_MODE_ARENA_INFO_KEYS, guiType), onCollect)
    return


def collectGameModeArenaInfoKeys(guiType):
    return __collectEM.handleEvent((GAME_MODE_ARENA_INFO_KEYS, guiType), ctx={}).get(b'game_mode_specific_keys')


GuiItemsCacheInvalidatorParams = namedtuple(b'GuiItemsCacheInvalidatorParams', (b'inventory', b'invalidate', b'diff'))

def registerGuiItemsCacheInvalidators(invalidatorsList):

    def onCollect(ctx):
        ctx.extend(invalidatorsList)
        return

    __collectEM.addListener(GUI_ITEMS_CACHE_INVALIDATOR, onCollect)
    return


def collectGuiItemsCacheInvalidators():
    return __collectEM.handleEvent(GUI_ITEMS_CACHE_INVALIDATOR, ctx=[])


def registerIgnoredModeForAutoSelectVehicle(modeFlags):

    def onCollect(ctx):
        ctx.extend(modeFlags)
        return

    __collectEM.addListener(IGNORED_MODE_FOR_AUTO_SELECTED_VEHICLE, onCollect)
    return


def collectIgnoredModeForAutoSelectVehicle():
    return __collectEM.handleEvent(IGNORED_MODE_FOR_AUTO_SELECTED_VEHICLE, ctx=[])


def registerBonusTokens(bonusTokens):

    def onCollect(ctx):
        ctx[b'bonusTokens'].extend(bonusTokens)
        return

    __collectEM.addListener(BONUS_TOKENS, onCollect)
    return


def collectBonusTokens():
    return __collectEM.handleEvent(BONUS_TOKENS, ctx={b'bonusTokens': []})[b'bonusTokens']


def registerViewsForMonitoring(viewsForMonitoring):

    def onCollect(ctx):
        ctx[b'viewsForMonitoring'].extend(viewsForMonitoring)
        return

    __collectEM.addListener(VIEWS_FOR_MONITORING, onCollect)
    return


def collectViewsForMonitoring():
    return __collectEM.handleEvent(VIEWS_FOR_MONITORING, ctx={b'viewsForMonitoring': []})[b'viewsForMonitoring']


def registerDynamicViewsForMonitoring(dynamicViewsForMonitoring):

    def onCollect(ctx):
        ctx[b'dynamicViewsForMonitoring'].extend(dynamicViewsForMonitoring)
        return

    __collectEM.addListener(DYNAMIC_VIEWS_FOR_MONITORING, onCollect)
    return


def collectDynamicViewsForMonitoring():
    return __collectEM.handleEvent(DYNAMIC_VIEWS_FOR_MONITORING, ctx={b'dynamicViewsForMonitoring': []})[b'dynamicViewsForMonitoring']


def registerLifecycleHandledSubViews(subViews):

    def onCollect(ctx):
        ctx[b'subViews'].extend(subViews)
        return

    __collectEM.addListener(LIFECYCLE_HANDLED_SUB_VIEWS, onCollect)
    return


def collectLifecycleHandledSubViews():
    return __collectEM.handleEvent(LIFECYCLE_HANDLED_SUB_VIEWS, {b'subViews': []})[b'subViews']


def registerBattleButtonManualControl(queueType, handler):

    def onCollect(ctx):
        ctx[b'battleButtonManualControl'][queueType] = handler
        return

    __collectEM.addListener(BATTLE_BUTTON_MANUAL_CONTROL, onCollect)
    return


def collectBattleButtonManualControl():
    return __collectEM.handleEvent(BATTLE_BUTTON_MANUAL_CONTROL, ctx={b'battleButtonManualControl': {}})[b'battleButtonManualControl']


def registerPrebattleCtrlMode(bonusType, controlModes):

    def onCollect(ctx):
        ctx[b'prebattleCtrlMode'][bonusType] = controlModes
        return

    __collectEM.addListener(PREBATTLE_CONTROL_MODE, onCollect)
    return


def collectPrebattleCtrlMode():
    return __collectEM.handleEvent(PREBATTLE_CONTROL_MODE, ctx={b'prebattleCtrlMode': {}})[b'prebattleCtrlMode']


def registerDisplayedClassTagGetter(guiType, getterFunc):

    def onCollect(ctx):
        ctx[b'classTagGetter'] = getterFunc
        return

    __collectEM.addListener((CLASS_TAG_GETTER, guiType), onCollect)
    return


def collectDisplayedClassTagGetter(guiType):
    return __collectEM.handleEvent((CLASS_TAG_GETTER, guiType), ctx={}).get(b'classTagGetter')


def registerBattleEntry(arenaGuiType, resId):

    def onCollect(ctx):
        ctx[b'battleEntryResID'] = resId
        return

    __collectEM.addListener((BATTLE_ENTRY, arenaGuiType), onCollect)
    return


def collectBattleEntry(arenaGuiType):
    return __collectEM.handleEvent((BATTLE_ENTRY, arenaGuiType), ctx={}).get(b'battleEntryResID', 0)


def registerReadyVehicleChekers(queueType, listCheckerFunc):

    def onCollect(ctx):
        ctx[b'listCheckerFunc'] = listCheckerFunc
        return

    __collectEM.addListener((VEHICLE_READY_CHECKERS, queueType), onCollect)
    return


def collectReadyVehicleChekers(queueType):
    return __collectEM.handleEvent((VEHICLE_READY_CHECKERS, queueType), ctx={}).get(b'listCheckerFunc', [])


def registerUnitMembersOrderKey(queueType, unitMembersOrderKey):

    def onCollect(ctx):
        ctx[b'unitMembersOrderKey'] = unitMembersOrderKey
        return

    __collectEM.addListener((UNIT_MEMBERS_ORDER_KEY, queueType), onCollect)
    return


def collectUnitMembersOrderKey(queueType):
    return __collectEM.handleEvent((UNIT_MEMBERS_ORDER_KEY, queueType), ctx={}).get(b'unitMembersOrderKey', [])


def registerPostbattleSquadFinder(guiType, squadFinderClass):

    def onCollect(ctx):
        ctx[b'pbs_squad_finder_data'] = squadFinderClass
        return

    __collectEM.addListener((POSTBATTLE_SQUAD_FINDER, guiType), onCollect)
    return


def collectPostbattleSquadFinder(guiType):
    return __collectEM.handleEvent((POSTBATTLE_SQUAD_FINDER, guiType), ctx={}).get(b'pbs_squad_finder_data', None)


def registerPostmortemInfoView(guiType, viewCls):

    def onCollect(ctx):
        ctx[b'postmortem_info_view'] = viewCls
        return

    __collectEM.addListener((POSTMORTEM_INFO_VIEW, guiType), onCollect)
    return


def collectPostmortemInfoView(guiType):
    return __collectEM.handleEvent((POSTMORTEM_INFO_VIEW, guiType), ctx={}).get(b'postmortem_info_view', None)


def registerModeHiddenVehiclesCriteria(bonusType, criteria):

    def onCollect(ctx):
        ctx[b'modeHiddenCriteria'][bonusType] = criteria
        return

    __collectEM.addListener(MODE_HIDDEN_VEHICLES_CRITERIA, onCollect)
    return


def collectModeHiddenVehiclesCriteria():
    return __collectEM.handleEvent(MODE_HIDDEN_VEHICLES_CRITERIA, {b'modeHiddenCriteria': {}})[b'modeHiddenCriteria']


def registerTeamVoipSupport(guiType, status):

    def onCollect(ctx):
        ctx[b'teamVoipSupport'] = status
        return

    __collectEM.addListener((TEAM_VOIP_SUPPORT, guiType), onCollect)
    return


def collectTeamVoipSupport(guiType):
    return __collectEM.handleEvent((TEAM_VOIP_SUPPORT, guiType), ctx={}).get(b'teamVoipSupport', False)
