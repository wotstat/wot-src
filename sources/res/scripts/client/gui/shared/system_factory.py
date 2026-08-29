import typing
from collections import defaultdict
if typing.TYPE_CHECKING:
    from typing import Iterable, List
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
BATTLE_RESULTS_COMPOSER = 32
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
HANGAR_PRESETS_PROCESSORS = 43
AMMUNITION_PANEL_VIEW = 44
VEHICLE_VIEW_STATE = 45
DYN_OBJ_CACHE = 46
SHARED_REPO = 47
CONVERTERS_EXT_DATA_FORMATTERS = 48
BONUS_MERGERS = 49
SERVICE_CHANNEL_SUBFORMATTERS = 50
QUESTS_FROM_EXTENSIONS_SOURCE = 51
SETTINGS_PROVIDERS_SERIALIZABLES = 52
BATTLE_MODIFIERS_PANELS = 53
BONUS_PACKERS = 54
WULF_TOOLTIP_CONTENT_FACTORY = 55

class _CollectEventsManager(object):

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


__collectEM = _CollectEventsManager()

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
    return __collectEM.handleEvent((EQUIPMENT_ITEMS, equipmentName), {b'args': args, b'isReplay': isReplay}).get(b'item')


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
    for eventID, handlers in __collectEM.handlers.iteritems():
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


def registerSquadFinder(guiType, squadFinderClass):

    def onCollect(ctx):
        ctx[b'squad_finder_class'] = squadFinderClass
        return

    __collectEM.addListener((ARENA_SQUAD_FINDER, guiType), onCollect)
    return


def collectSquadFinder(guiType):
    return __collectEM.handleEvent((ARENA_SQUAD_FINDER, guiType), ctx={}).get(b'squad_finder_class')


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


def registerMessengerServerFormatter(msgType, formatter):

    def onCollect(ctx):
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


def registerConvertersSubFormatter(dataKey, formatter):

    def onCollect(ctx):
        ctx[b'formatter'] = formatter
        return

    __collectEM.addListener((CONVERTERS_EXT_DATA_FORMATTERS, dataKey), onCollect)
    return


def collectConvertersSubFormatter(dataKey):
    return __collectEM.handleEvent((CONVERTERS_EXT_DATA_FORMATTERS, dataKey), ctx={}).get(b'formatter')


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


def collectBannerEntryPointLUIRule(alias):
    return __collectEM.handleEvent((BANNER_ENTRY_POINT_LUI_RULE, alias), ctx={}).get(b'ruleID')


def registerCarouselEventEntryPoint(viewID, viewClass):

    def onCollect(ctx):
        ctx[b'carouselEventEntries'][viewID] = viewClass
        return

    __collectEM.addListener(CAROUSEL_EVENTS_ENTRIES, onCollect)
    return


def collectCarouselEventEntryPoints():
    return __collectEM.handleEvent(CAROUSEL_EVENTS_ENTRIES, {b'carouselEventEntries': {}})[b'carouselEventEntries']


def registerBattleModifiersPanel(viewID, viewClass):

    def onCollect(ctx):
        ctx[b'battleModifiersPanels'][viewID] = viewClass
        return

    __collectEM.addListener(BATTLE_MODIFIERS_PANELS, onCollect)
    return


def collectBattleModifiersPanel():
    return __collectEM.handleEvent(BATTLE_MODIFIERS_PANELS, {b'battleModifiersPanels': {}})[b'battleModifiersPanels']


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


def registerQuestBuilder(questBuilder, index=None):

    def onCollect(ctx):
        if index is None:
            ctx[b'questBuilders'].append(questBuilder)
        else:
            ctx[b'questBuilders'].insert(index, questBuilder)
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


def registerBattleResultsComposer(bonusType, itemCls):

    def onCollect(ctx):
        ctx[b'item'] = itemCls
        return

    __collectEM.addListener((BATTLE_RESULTS_COMPOSER, bonusType), onCollect)
    return


def collectBattleResultsComposer(bonusType):
    return __collectEM.handleEvent((BATTLE_RESULTS_COMPOSER, bonusType), ctx={}).get(b'item', None)


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


def registerHangarPresetGetter(queueType, processor):

    def onCollect(ctx):
        ctx[b'presetsGetters'][queueType] = processor(ctx[b'config'])
        return

    __collectEM.addListener(HANGAR_PRESETS_PROCESSORS, onCollect)
    return


def collectHangarPresetsGetters(config):
    return __collectEM.handleEvent(HANGAR_PRESETS_PROCESSORS, {b'presetsGetters': {}, b'config': config})[b'presetsGetters']


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


def registerVehicleViewState(viewState):

    def onCollect(ctx):
        ctx[b'viewStates'].append(viewState)
        return

    __collectEM.addListener(VEHICLE_VIEW_STATE, onCollect)
    return


def collectVehicleViewStates():
    return __collectEM.handleEvent(VEHICLE_VIEW_STATE, ctx={b'viewStates': []})[b'viewStates']


def registerDynObjCache(queueType, dynCache):

    def onCollect(ctx):
        ctx[b'dynCache'] = dynCache
        return

    __collectEM.addListener((DYN_OBJ_CACHE, queueType), onCollect)
    return


def collectDynObjCache(queueType):
    return __collectEM.handleEvent((DYN_OBJ_CACHE, queueType), ctx={}).get(b'dynCache')


def registerClientBonusMergers(predicate, mergeFunction):

    def onCollect(ctx):
        ctx[b'mergers'].append((predicate, mergeFunction))
        return

    __collectEM.addListener(BONUS_MERGERS, onCollect)
    return


def collectClientBonusMergers():
    return __collectEM.handleEvent(BONUS_MERGERS, ctx={b'mergers': []})[b'mergers']


def registerServiceChannelSubformatter(callContext, subformatter):

    def onCollect(ctx):
        ctx[b'formatters'].append(subformatter)
        return

    __collectEM.addListener((SERVICE_CHANNEL_SUBFORMATTERS, callContext), onCollect)
    return


def collectServiceChannelSubformatter(callContext):
    return __collectEM.handleEvent((SERVICE_CHANNEL_SUBFORMATTERS, callContext), ctx={b'formatters': []}).get(b'formatters', [])


def registerExtensionQuestsSources(sources):

    def onCollect(ctx):
        ctx[b'sources'].extend(sources)
        return

    __collectEM.addListener(QUESTS_FROM_EXTENSIONS_SOURCE, onCollect)
    return


def collectExtensionQuestsSources():
    return __collectEM.handleEvent(QUESTS_FROM_EXTENSIONS_SOURCE, {b'sources': []})[b'sources']


def registerExtensionSettingsProvidersSerializable(settingsProvidersSerializable):

    def onCollect(ctx):
        ctx[b'settingsProvidersSerializable'].update(settingsProvidersSerializable)
        return

    __collectEM.addListener(SETTINGS_PROVIDERS_SERIALIZABLES, onCollect)
    return


def collectExtensionSettingsProvidersSerializable():
    return __collectEM.handleEvent(SETTINGS_PROVIDERS_SERIALIZABLES, ctx={b'settingsProvidersSerializable': {}}).get(b'settingsProvidersSerializable')


def registerCurrencyBonusPacker(bonusType, packer):

    def onCollect(ctx):
        ctx[b'currencyBonusPackers'][bonusType] = packer
        return

    __collectEM.addListener(BONUS_PACKERS, onCollect)
    return


def collectCurrencyBonusPacker(bonusType):
    return __collectEM.handleEvent(BONUS_PACKERS, ctx={b'currencyBonusPackers': {}})[b'currencyBonusPackers'].get(bonusType, None)


def registerWulfTooltipContentFactory(contentID, factory):

    def onCollect(ctx):
        ctx[b'factory'] = factory
        return

    __collectEM.addListener((WULF_TOOLTIP_CONTENT_FACTORY, contentID), onCollect)
    return


def collectWulfTooltipContentFactory(contentID):
    return __collectEM.handleEvent((WULF_TOOLTIP_CONTENT_FACTORY, contentID), ctx={}).get(b'factory')
