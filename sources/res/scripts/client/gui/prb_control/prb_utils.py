import logging
from gui.Scaleform.daapi.view.lobby.header.battle_selector_items import BATTLES_SELECTOR_ITEMS, BATTLES_SELECTOR_SQUAD_ITEMS
from gui.impl.lobby.mode_selector.items.items_constants import DEFAULT_COLUMN_SETTINGS, modeNamesByArenaBonusType, arenaBonusTypeByModeName
from gui.prb_control.factories.PreQueueFactory import DEFAULT_QUEUE_TYPE_PRIORITIES
from gui.prb_control.prb_getters import _ARENA_GUI_TYPE_BY_QUEUE_TYPE
from gui.prb_control.settings import FUNCTIONAL_FLAG, _FUNCTIONAL_FLAG_NAMES, QUEUE_TYPE_TO_PREBATTLE_TYPE, PREBATTLE_TYPE_TO_QUEUE_TYPE, REQUEST_TYPE, REQUEST_TYPE_NAMES
from messenger.ext.channel_num_gen import PRB_CLIENT_COMBINED_IDS, initPrbTypeToClientID
from gui.shared.system_factory import registerQueueEntity, registerUnitEntryPoint, registerUnitEntity, registerUnitEntryPointByType, registerModeSelectorItem, registerBannerEntryPointValidator, registerSquadFinder, registerArenaDescrs, registerCanSelectPrbEntity, registerBattleQueueProvider, registerBannerEntryPointLUIRule, registerBattleModifiersPanel
from gui.shared.system_factory import registerEntryPoint
from soft_exception import SoftException
_logger = logging.getLogger(__name__)
_logger.addHandler(logging.NullHandler())

def addArenaGUITypeByQueueType(queueType, arenaGuiType, personality):
    if queueType in _ARENA_GUI_TYPE_BY_QUEUE_TYPE:
        raise SoftException((b'_ARENA_GUI_TYPE_BY_QUEUE_TYPE already has QUEUE_TYPE:{queueType}. Personality: {personality}').format(queueType=queueType, personality=personality))
    _ARENA_GUI_TYPE_BY_QUEUE_TYPE.update({queueType: arenaGuiType})
    msg = (b'QUEUE_TYPE:{queueType}->{arenaGuiType} was added to _ARENA_GUI_TYPE_BY_QUEUE_TYPE. Personality: {p}').format(queueType=queueType, arenaGuiType=arenaGuiType, p=personality)
    logging.debug(msg)
    return


def addFunctionalFlags(extFunctionalFlag, personality):
    extraAttrs = extFunctionalFlag.getExtraAttrs()
    extFunctionalFlag.inject(personality)
    for value in extraAttrs.itervalues():
        FUNCTIONAL_FLAG.MODES_BITMASK |= value
        FUNCTIONAL_FLAG.RANGE += (value,)

    _FUNCTIONAL_FLAG_NAMES.update(extraAttrs)
    return


def addSupportedQueues(queueType, prbEntity, canSelectPrbEntityFun, personality):
    registerQueueEntity(queueType, prbEntity)
    registerCanSelectPrbEntity(queueType, canSelectPrbEntityFun)
    msg = (b'QUEUE_TYPE:{queueType} was registered for entity. Personality: {personality}').format(queueType=queueType, personality=personality)
    logging.debug(msg)
    return


def addSupportedEntryByAction(prbActionName, prbEntryPoint, personality):
    registerEntryPoint(prbActionName, prbEntryPoint)
    msg = (b'prbActionName:{prb} was registered for entry point. Personality: {p}').format(prb=prbActionName, p=personality)
    logging.debug(msg)
    return


def addSupportedUnitEntryByAction(prbActionName, prbEntryPoint, personality):
    registerUnitEntryPoint(prbActionName, prbEntryPoint)
    msg = (b'prbActionName:{prb} was registered for entry point (squad). Personality: {p}').format(prb=prbActionName, p=personality)
    logging.debug(msg)
    return


def addSupportedUnitEntryByType(prbType, prbEntryPoint, personality):
    registerUnitEntryPointByType(prbType, prbEntryPoint)
    msg = (b'prebType:{prb} was registered for entry point (squad). Personality: {p}').format(prb=prbType, p=personality)
    logging.debug(msg)
    return


def addSupportedUnitByType(prbType, prbEntity, personality):
    registerUnitEntity(prbType, prbEntity)
    msg = (b'prebType:{prb} was registered for entity (squad). Personality: {p}').format(prb=prbType, p=personality)
    logging.debug(msg)
    return


def addBattleItemToColumnSelector(prbActionName, selectorColumn, personality):
    if prbActionName in DEFAULT_COLUMN_SETTINGS:
        raise SoftException((b'COLUMN_SETTINGS already has prbActionName:{prbActionName}. Personality: {p}').format(prbActionName=prbActionName, p=personality))
    DEFAULT_COLUMN_SETTINGS.update({prbActionName: selectorColumn})
    msg = (b'prbActionName:{prbActionName} was added to COLUMN_SETTINGS. Personality: {p}').format(prbActionName=prbActionName, p=personality)
    logging.debug(msg)
    return


def addDynamicModeSelectorPriorityAbility(prbActionName, bonusTypeName, personality):
    if bonusTypeName in modeNamesByArenaBonusType:
        raise SoftException((b'modeNamesByArenaBonusType already has bonusTypeName:{bonusTypeName}. Personality: {p}').format(bonusTypeName=bonusTypeName, p=personality))
    modeNamesByArenaBonusType.update({bonusTypeName: prbActionName})
    arenaBonusTypeByModeName.update({prbActionName: bonusTypeName})
    msg = (b'bonusTypeName:{bonusTypeName} was added to modeNamesByArenaBonusType. Personality: {p}').format(bonusTypeName=bonusTypeName, p=personality)
    logging.debug(msg)
    return


def addBattleSelectorItem(prbActionName, prbActionConstructor, personality):
    if prbActionConstructor in BATTLES_SELECTOR_ITEMS:
        raise SoftException((b'BATTLES_SELECTOR_ITEMS already has prbActionName:{prbActionName}. Personality: {p}').format(prbActionName=prbActionName, p=personality))
    BATTLES_SELECTOR_ITEMS.update({prbActionName: prbActionConstructor})
    msg = (b'prbActionName:{prbActionName} was added to BATTLES_SELECTOR_ITEMS. Personality: {p}').format(prbActionName=prbActionName, p=personality)
    logging.debug(msg)
    return


def addModeSelectorItem(prbActionName, modeSelectorItem, personality):
    registerModeSelectorItem(prbActionName, modeSelectorItem)
    msg = (b'prbActionName:{prbActionName} was registered for ModeSelectorDataProvider. Personality: {p}').format(prbActionName=prbActionName, p=personality)
    logging.debug(msg)
    return


def addBannerEntryPointValidatorMethod(alias, validator, personality):
    registerBannerEntryPointValidator(alias, validator)
    msg = (b'alias:{alias} was registered for banner entry point validator. Personality: {p}').format(alias=alias, p=personality)
    logging.debug(msg)
    return


def addBannerEntryPointLUIRule(alias, ruleID, personality):
    registerBannerEntryPointLUIRule(alias, ruleID)
    msg = (b'alias:{alias} was registered for Limited UI with ruleID:{ruleID}. Personality: {p}').format(alias=alias, p=personality, ruleID=ruleID)
    logging.debug(msg)
    return


def addBattleModifiersPanel(views, personality):
    alias, viewClass = views
    registerBattleModifiersPanel(alias, viewClass)
    msg = (b'BattleModifiersPanel alias:{alias} was registered. Personality: {p}').format(alias=alias, p=personality)
    logging.debug(msg)
    return


def addProviderBattleQueueCls(queueType, providerCls, personality):
    registerBattleQueueProvider(queueType, providerCls)
    msg = (b'queueType:{queueType} was registered for QueueProvider. Personality: {p}').format(queueType=queueType, p=personality)
    logging.debug(msg)
    return


def addBattleSelectorSquadItem(prbActionName, prbActionConstructor, personality):
    if prbActionConstructor in BATTLES_SELECTOR_SQUAD_ITEMS:
        raise SoftException((b'BATTLES_SELECTOR_SQUAD_ITEMS already has prbActionName:{prbActionName}. Personality: {p}').format(prbActionName=prbActionName, p=personality))
    BATTLES_SELECTOR_SQUAD_ITEMS.update({prbActionName: prbActionConstructor})
    msg = (b'prbActionName:{prbActionName} was added to BATTLES_SELECTOR_SQUAD_ITEMS. Personality: {p}').format(prbActionName=prbActionName, p=personality)
    logging.debug(msg)
    return


def addSquadFinder(arenaGuiType, squadFinderClass, personality):
    registerSquadFinder(arenaGuiType, squadFinderClass)
    msg = (b'arenaGuiType:{arenaGuiType} was added for squad finder. Personality: {p}').format(arenaGuiType=arenaGuiType, p=personality)
    logging.debug(msg)
    return


def addPrbClientCombinedIds(prbType, value, personality):
    if prbType in PRB_CLIENT_COMBINED_IDS:
        raise SoftException((b'PRB_CLIENT_COMBINED_IDS already has prbActionName:{prbType}. Personality: {p}').format(prbType=prbType, p=personality))
    PRB_CLIENT_COMBINED_IDS.update({prbType: value})
    msg = (b'prbActionName:{prbType} was added to PRB_CLIENT_COMBINED_IDS. Personality: {p}').format(prbType=prbType, p=personality)
    initPrbTypeToClientID()
    logging.debug(msg)
    return


def addQueueTypeToPrbType(queueType, prbType, personality):
    if queueType in QUEUE_TYPE_TO_PREBATTLE_TYPE:
        raise SoftException((b'QUEUE_TYPE_TO_PREBATTLE_TYPE already has queue type:{qType}. Personality: {p}').format(qType=queueType, p=personality))
    QUEUE_TYPE_TO_PREBATTLE_TYPE.update({queueType: prbType})
    msg = (b'queueType:{qtype} was added to QUEUE_TYPE_TO_PREBATTLE_TYPE. Personality: {p}').format(qtype=queueType, p=personality)
    logging.debug(msg)
    return


def addPrbTypeToQueueType(queueType, prbType, personality):
    if queueType in PREBATTLE_TYPE_TO_QUEUE_TYPE:
        raise SoftException((b'PREBATTLE_TYPE_TO_QUEUE_TYPE already has pre battle type:{prbType}. Personality: {p}').format(prbType=prbType, p=personality))
    PREBATTLE_TYPE_TO_QUEUE_TYPE.update({prbType: queueType})
    msg = (b'prbType:{prbType} was added to PREBATTLE_TYPE_TO_QUEUE_TYPE. Personality: {p}').format(prbType=prbType, p=personality)
    logging.debug(msg)
    return


def addDefaultQueueTypePriority(queueType, priority, personality):
    if queueType in DEFAULT_QUEUE_TYPE_PRIORITIES:
        raise SoftException((b'DEFAULT_QUEUE_TYPE_PRIORITIES already has queueType:{queueType}. Personality: {p}').format(queueType=queueType, p=personality))
    DEFAULT_QUEUE_TYPE_PRIORITIES.update({queueType: priority})
    msg = (b'queueType:{queueType} was added to DEFAULT_QUEUE_TYPE_PRIORITIES. Personality: {p}').format(queueType=queueType, p=personality)
    logging.debug(msg)
    return


def addArenaDescrs(arenaGuiType, arenaDescrClass, personality):
    registerArenaDescrs(arenaGuiType, arenaDescrClass)
    msg = (b'arenaGuiType:{arenaGuiType} was added for arena descrs class. Personality: {p}').format(arenaGuiType=arenaGuiType, p=personality)
    logging.debug(msg)
    return


def initGuiTypes(guiConstants, personality):
    guiConstants.PREBATTLE_ACTION_NAME.inject(personality)
    addFunctionalFlags(guiConstants.FUNCTIONAL_FLAG, personality)
    guiConstants.SELECTOR_BATTLE_TYPES.inject(personality)
    return


def initRequestType(guiConstants, personality):
    guiConstants.REQUEST_TYPE.inject(personality)
    REQUEST_TYPE_NAMES.update(dict([(v, k) for k, v in REQUEST_TYPE.__dict__.iteritems()]))
    return


def initScaleformGuiTypes(guiConstants, personality):
    guiConstants.VIEW_ALIAS.inject(personality)
    return
