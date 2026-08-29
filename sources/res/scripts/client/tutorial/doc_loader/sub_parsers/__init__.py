import importlib
from collections import namedtuple
from functools import partial
import nations, resource_helper
from gui.Scaleform.genConsts.LAYER_NAMES import LAYER_NAMES
from gui.impl.lobby.common.view_helpers import getLayoutIDByText
from items import _xml, vehicles
from helpers.html import translation
from tutorial.data import chapter as tutorial_chapter
from tutorial.data import effects
from tutorial.data import conditions as tut_conditions
from tutorial.data.events import GuiEventType
from tutorial.control.context import SOUND_EVENT
from tutorial.logger import LOG_ERROR
_EFFECT_TYPE = effects.EFFECT_TYPE
_COND_STATE = tut_conditions.CONDITION_STATE
_CheckedComponentState = namedtuple(b'CheckedComponentState', (b'state', b'value'))

def parseID(xmlCtx, section, msg):
    entityID = section.asString
    if not entityID:
        _xml.raiseWrongXml(xmlCtx, section.name, msg)
    return entityID


def _parseOneState(xml, section):
    checkedState = parseID(xml, section[b'state'], b'Specify ui state')
    neededValue = _xml.readBool(xml, section, b'value')
    return _CheckedComponentState(checkedState, neededValue)


def _parseNeededState(xmlCtx, section):
    stateSection = section[b'checked-ui-state']
    if not stateSection:
        return
    else:
        result = []
        for name, subSection in stateSection.items():
            if name == b'simple-state':
                result.append(_parseOneState(xmlCtx, subSection))
            else:
                _xml.raiseWrongXml(xmlCtx, section, b'Tag %s are not found' % name)

        if result:
            return result
        return


def _readFlagCondition(xmlCtx, section, state, flags):
    flagID = parseID(xmlCtx, section, b'Specify a flag ID')
    if flagID not in flags:
        flags.append(flagID)
    return tut_conditions.FlagCondition(flagID, state=state)


def _readGlobalFlagCondition(xmlCtx, section, state):
    flagID = parseID(xmlCtx, section, b'Specify a flag ID')
    return tut_conditions.GlobalFlagCondition(flagID, state=state)


def _readWindowOnSceneCondition(xmlCtx, section, state):
    windowID = parseID(xmlCtx, section, b'Specify a window ID')
    return tut_conditions.WindowOnSceneCondition(windowID, state=state)


def _readComponentOnSceneCondition(xmlCtx, section, state):
    componentID = parseID(xmlCtx, section, b'Specify a component ID')
    return tut_conditions.ComponentOnSceneCondition(componentID, state=state)


def _readCurrentSceneCondition(xmlCtx, section, state):
    sceneID = parseID(xmlCtx, section, b'Specify a scene ID')
    return tut_conditions.CurrentSceneCondition(sceneID, state=state)


def _readViewPresentCondition(xmlCtx, section, state):
    layer = LAYER_NAMES.LAYER_ORDER.index(_xml.readString(xmlCtx, section, b'type'))
    viewAlias = _xml.readString(xmlCtx, section, b'alias')
    dynamic = _xml.readBool(xmlCtx, section, b'dynamic', default=False)
    if dynamic:
        res = getLayoutIDByText(viewAlias)
        if res.exists():
            viewAlias = res()
        else:
            _xml.raiseWrongXml(xmlCtx, section.name, (b'view {} not exists').format(viewAlias))
    return tut_conditions.ViewPresentCondition(layer, viewAlias, state=state)


_GAME_ITEM_CONDITION_TAGS = {b'selected': (_COND_STATE.SELECTED), 
   b'not-selected': (~_COND_STATE.SELECTED), 
   b'premium': (_COND_STATE.PREMIUM), 
   b'not-premium': (~_COND_STATE.PREMIUM), 
   b'unlocked': (_COND_STATE.UNLOCKED), 
   b'not-unlocked': (~_COND_STATE.UNLOCKED), 
   b'in-inventory': (_COND_STATE.IN_INVENTORY), 
   b'not-in-inventory': (~_COND_STATE.IN_INVENTORY), 
   b'crew-has-any-skill': (_COND_STATE.CREW_HAS_ANY_SKILL), 
   b'crew-has-not-any-skill': (~_COND_STATE.CREW_HAS_ANY_SKILL), 
   b'xp-enough': (_COND_STATE.XP_ENOUGH), 
   b'xp-not-enough': (~_COND_STATE.XP_ENOUGH), 
   b'money-enough': (_COND_STATE.MONEY_ENOUGH), 
   b'money-not-enough': (~_COND_STATE.MONEY_ENOUGH), 
   b'level': (_COND_STATE.LEVEL), 
   b'not-level': (~_COND_STATE.LEVEL), 
   b'level-range': (_COND_STATE.LEVEL_RANGE), 
   b'not-level-range': (~_COND_STATE.LEVEL_RANGE), 
   b'may-install': (_COND_STATE.MAY_INSTALL), 
   b'may-not-install': (~_COND_STATE.MAY_INSTALL), 
   b'installed': (_COND_STATE.INSTALLED), 
   b'not-installed': (~_COND_STATE.INSTALLED), 
   b'has-regular-consumables': (_COND_STATE.HAS_REGULAR_CONSUMABLES), 
   b'has-no-regular-consumables': (~_COND_STATE.HAS_REGULAR_CONSUMABLES), 
   b'all-equipment-installed': (_COND_STATE.ALL_EQUIPMENT_INSTALLED), 
   b'not-all-equipment-installed': (~_COND_STATE.ALL_EQUIPMENT_INSTALLED), 
   b'has-optional-devices': (_COND_STATE.HAS_OPTIONAL_DEVICES), 
   b'has-no-optional-devices': (~_COND_STATE.HAS_OPTIONAL_DEVICES), 
   b'has-multiplied-xp': (_COND_STATE.HAS_MULTIPLIED_XP), 
   b'has-no-multiplied-xp': (~_COND_STATE.HAS_MULTIPLIED_XP)}
_GAME_ITEM_CONDITION_SET = set(_GAME_ITEM_CONDITION_TAGS.keys())

def _readGameItemCondition(xmlCtx, section, _):
    varID = parseID(xmlCtx, section, b'Specify a var ID')
    tags = set(section.keys()) & _GAME_ITEM_CONDITION_SET
    if tags:
        if len(tags) > 1:
            _xml.raiseWrongXml(xmlCtx, b'var', (b'One state of vehicle condition must be defined, found {0}').format(tags))
            return
        tag = tags.pop()
        state = _GAME_ITEM_CONDITION_TAGS[tag]
        if state.base in _COND_STATE.GAME_ITEM_RELATE_STATE:
            otherIDs = parseID(xmlCtx, section[tag], b'Specify a other ID').split()
            return tut_conditions.GameItemRelateStateCondition(varID, otherIDs, state)
        return tut_conditions.GameItemSimpleStateCondition(varID, state)
    else:
        _xml.raiseWrongXml(xmlCtx, b'var', (b'State of vehicle condition is not found: {0}').format(section.keys()))
        return


def _readVarCondition(xmlCtx, section, _):
    varID = parseID(xmlCtx, section, b'Specify a var ID')
    tags = section.keys()
    if b'is-none' in tags:
        return tut_conditions.VarDefinedCondition(varID, ~_COND_STATE.ACTIVE)
    else:
        if b'is-not-none' in tags:
            return tut_conditions.VarDefinedCondition(varID, _COND_STATE.ACTIVE)
        if b'equals' in tags:
            return tut_conditions.VarCompareCondition(varID, _xml.readString(xmlCtx, section, b'equals'), _COND_STATE.EQUALS)
        if b'not-equals' in tags:
            return tut_conditions.VarCompareCondition(varID, _xml.readString(xmlCtx, section, b'not-equals'), ~_COND_STATE.EQUALS)
        _xml.raiseWrongXml(xmlCtx, b'var', b'State of var condition is not found')
        return


def _readConnectedItemCondition(xmlCtx, section, _=None):
    hintID = parseID(xmlCtx, section[b'hint-id'], b'Specify a hint ID')
    status = _xml.readBool(xmlCtx, section, b'value')
    return tut_conditions.ConnectedItemCondition(hintID, status)


def _readComplexCondition(xmlCtx, section, flags):
    items = []
    for name, subSection in section.items():
        function = _conditions.tags.get(name)
        if function is None:
            LOG_ERROR(b'Condition is not supported: ', name)
            continue
        items.append(function(xmlCtx, subSection, flags))

    return items


def _readComplexConditionAnd(xmlCtx, section, flags):
    return tut_conditions.ComplexConditionAnd(_readComplexCondition(xmlCtx, section, flags))


def _readComplexConditionOr(xmlCtx, section, flags):
    return tut_conditions.ComplexConditionOr(_readComplexCondition(xmlCtx, section, flags))


def _parseEffectTriggeredCondition(xmlCtx, section, state):
    entityID = parseID(xmlCtx, section, b'Specify a entity ID')
    return tut_conditions.EffectTriggeredCondition(entityID, state)


def _readEffectTriggeredCondition(xmlCtx, section, _):
    return _parseEffectTriggeredCondition(xmlCtx, section, _COND_STATE.ACTIVE)


def _readEffectNotTriggeredCondition(xmlCtx, section, _):
    return _parseEffectTriggeredCondition(xmlCtx, section, ~_COND_STATE.ACTIVE)


def _readServiceCondition(xmlCtx, section, _):
    entityID = parseID(xmlCtx, section, b'Specify a entity ID')
    serviceClass = _getClass(entityID, xmlCtx, section)
    return tut_conditions.ServiceCondition(entityID, serviceClass)


def _readClassCondition(xmlCtx, section, _):
    entityID = parseID(xmlCtx, section, b'Specify a entity ID')
    conditionClass = _getClass(entityID, xmlCtx, section)
    tags = section.keys()
    arguments = parseID(xmlCtx, section[b'arguments'], b'') if b'arguments' in tags else b''
    return tut_conditions.ClassCondition(entityID, conditionClass, arguments)


def _getClass(entityID, xmlCtx, section):
    tags = section.keys()
    if b'path' in tags:
        path = parseID(xmlCtx, section[b'path'], b'Specify a path.')
    else:
        path = None
    try:
        if path is not None:
            resultClass = getattr(importlib.import_module(path), entityID)
        else:
            resultClass = importlib.import_module(entityID)
    except (ImportError, NameError):
        _xml.raiseWrongXml(xmlCtx, section.name, b'Class %s not found!' % entityID)
        return

    return resultClass


_BASE_CONDITION_TAGS = {b'active': (lambda xmlCtx, section, flags: _readFlagCondition(xmlCtx, section, _COND_STATE.ACTIVE, flags)), 
   b'inactive': (lambda xmlCtx, section, flags: _readFlagCondition(xmlCtx, section, ~_COND_STATE.ACTIVE, flags)), 
   b'global-active': (lambda xmlCtx, section, flags: _readGlobalFlagCondition(xmlCtx, section, _COND_STATE.ACTIVE)), 
   b'global-inactive': (lambda xmlCtx, section, flags: _readGlobalFlagCondition(xmlCtx, section, ~_COND_STATE.ACTIVE)), 
   b'is-widow-opened': (lambda xmlCtx, section, flags: _readWindowOnSceneCondition(xmlCtx, section, _COND_STATE.ACTIVE)), 
   b'is-widow-closed': (lambda xmlCtx, section, flags: _readWindowOnSceneCondition(xmlCtx, section, ~_COND_STATE.ACTIVE)), 
   b'game-item': _readGameItemCondition, 
   b'var': _readVarCondition, 
   b'effect-triggered': _readEffectTriggeredCondition, 
   b'effect-not-triggered': _readEffectNotTriggeredCondition, 
   b'service': _readServiceCondition, 
   b'class-condition': _readClassCondition, 
   b'component-on-scene': (lambda xmlCtx, section, flags: _readComponentOnSceneCondition(xmlCtx, section, _COND_STATE.ACTIVE)), 
   b'component-not-on-scene': (lambda xmlCtx, section, flags: _readComponentOnSceneCondition(xmlCtx, section, ~_COND_STATE.ACTIVE)), 
   b'on-scene': (lambda xmlCtx, section, flags: _readCurrentSceneCondition(xmlCtx, section, _COND_STATE.ACTIVE)), 
   b'not-on-scene': (lambda xmlCtx, section, flags: _readCurrentSceneCondition(xmlCtx, section, ~_COND_STATE.ACTIVE)), 
   b'view-present': (lambda xmlCtx, section, flags: _readViewPresentCondition(xmlCtx, section, _COND_STATE.ACTIVE)), 
   b'view-not-present': (lambda xmlCtx, section, flags: _readViewPresentCondition(xmlCtx, section, ~_COND_STATE.ACTIVE)), 
   b'condition-hint-showed': _readConnectedItemCondition, 
   b'condition-and': _readComplexConditionAnd, 
   b'condition-or': _readComplexConditionOr}

class ConditionTags(object):

    def __init__(self):
        self.tags = _BASE_CONDITION_TAGS.copy()
        return


_conditions = ConditionTags()

def setConditionsParsers(parsers):
    _conditions.tags.clear()
    _conditions.tags = _BASE_CONDITION_TAGS.copy()
    _conditions.tags.update(parsers)
    return


def readConditions(xmlCtx, section, flags):
    result = tut_conditions.Conditions()
    for name, subSec in section.items():
        if name == b'either':
            eitherCondition = readConditions(xmlCtx, subSec, flags)
            result.appendEitherBlock(eitherCondition)
        else:
            function = _conditions.tags.get(name)
            if function is None:
                LOG_ERROR(b'Condition is not supported: ', name)
                continue
            result.append(function(xmlCtx, subSec, flags))

    return result


def _parseConditions(xmlCtx, section, flags):
    condSec = section[b'condition']
    if condSec is not None:
        return readConditions(xmlCtx, condSec, flags)
    else:
        return


ACTION_TAGS = {b'click': (GuiEventType.CLICK), 
   b'click-outside': (GuiEventType.CLICK_OUTSIDE), 
   b'esc': (GuiEventType.ESC), 
   b'enable': (GuiEventType.ENABLE), 
   b'disable': (GuiEventType.DISABLE)}

def parseAction(xmlCtx, section, flags):
    name = section.name
    if name not in ACTION_TAGS:
        LOG_ERROR(b'Action is not supported: ', name)
        return
    else:
        targetID = parseID(xmlCtx, section, b'Specify a target ID')
        action = tutorial_chapter.Action(ACTION_TAGS[name], targetID)
        if b'effects' in section.keys():
            for _, effectSec in _xml.getChildren(xmlCtx, section, b'effects'):
                effect = _parseEffect(xmlCtx, effectSec, flags)
                if effect is not None:
                    action.addEffect(effect)

        return action


def parseActions(xmlCtx, section, flags):
    result = []
    for _, subSec in section.items():
        action = parseAction(xmlCtx, subSec, flags)
        if action is not None:
            result.append(action)

    return result


def _readEffectsGroupSection(xmlCtx, section, flags, conditions):
    _effects = (_parseEffect(xmlCtx, effectSec, flags) for _, effectSec in _xml.getChildren(xmlCtx, section, b'effects'))
    return effects.EffectsGroup(tuple(e for e in _effects if e is not None), conditions)


def _readActivateEffectSection(xmlCtx, section, flags, conditions):
    flagID = parseID(xmlCtx, section, b'Specify a flag ID')
    if flagID not in flags:
        flags.append(flagID)
    return effects.HasTargetEffect(flagID, _EFFECT_TYPE.ACTIVATE, conditions=conditions)


def _readDeactivateEffectSection(xmlCtx, section, flags, conditions):
    flagID = parseID(xmlCtx, section, b'Specify a flag ID')
    if flagID not in flags:
        flags.append(flagID)
    return effects.HasTargetEffect(flagID, _EFFECT_TYPE.DEACTIVATE, conditions=conditions)


def _readGlobalActivateEffectSection(xmlCtx, section, _, conditions):
    flagID = parseID(xmlCtx, section, b'Specify a flag ID')
    return effects.HasTargetEffect(flagID, _EFFECT_TYPE.GLOBAL_ACTIVATE, conditions=conditions)


def _readGlobalDeactivateEffectSection(xmlCtx, section, _, conditions):
    flagID = parseID(xmlCtx, section, b'Specify a flag ID')
    return effects.HasTargetEffect(flagID, _EFFECT_TYPE.GLOBAL_DEACTIVATE, conditions=conditions)


def _readRunTriggerEffectSection(xmlCtx, section, _, conditions):
    triggerID = parseID(xmlCtx, section, b'Specify a trigger ID')
    return effects.HasTargetEffect(triggerID, _EFFECT_TYPE.RUN_TRIGGER, conditions=conditions)


def _readShowHintSection(xmlCtx, section, _, conditions):
    hintID = parseID(xmlCtx, section, b'Specify a hint ID')
    return effects.HasTargetEffect(hintID, _EFFECT_TYPE.SHOW_HINT, conditions=conditions)


def _readCloseHintSection(xmlCtx, section, _, conditions):
    hintID = parseID(xmlCtx, section, b'Specify a hint ID')
    return effects.HasTargetEffect(hintID, _EFFECT_TYPE.CLOSE_HINT, conditions=conditions)


def _readShowDialogSection(xmlCtx, section, _, conditions):
    dialogID = parseID(xmlCtx, section, b'Specify a dialog ID')
    return effects.HasTargetEffect(dialogID, _EFFECT_TYPE.SHOW_DIALOG, conditions=conditions)


def _readShowWindowSection(xmlCtx, section, _, conditions):
    windowID = parseID(xmlCtx, section, b'Specify a window ID')
    return effects.HasTargetEffect(windowID, _EFFECT_TYPE.SHOW_WINDOW, conditions=conditions)


def _readSetGuiItemCriteria(xmlCtx, section, _, conditions):
    criteriaID = parseID(xmlCtx, section, b'Specify a criteria ID')
    return effects.HasTargetEffect(criteriaID, _EFFECT_TYPE.SET_GUI_ITEM_CRITERIA, conditions=conditions)


def _setReadGuiItemViewCriteria(xmlCtx, section, _, conditions):
    criteriaID = parseID(xmlCtx, section, b'Specify a criteria ID')
    return effects.HasTargetEffect(criteriaID, _EFFECT_TYPE.SET_GUI_ITEM_VIEW_CRITERIA, conditions=conditions)


def _readSetActionSection(xmlCtx, section, _, conditions):
    actionID = parseID(xmlCtx, section, b'Specify a action ID')
    return effects.HasTargetEffect(actionID, _EFFECT_TYPE.SET_ACTION, conditions=conditions)


def _readRemoveActionSection(xmlCtx, section, _, conditions):
    actionID = parseID(xmlCtx, section, b'Specify a action ID')
    return effects.HasTargetEffect(actionID, _EFFECT_TYPE.REMOVE_ACTION, conditions=conditions)


def _readSetVarSection(xmlCtx, section, _, conditions):
    varID = parseID(xmlCtx, section, b'Specify a var ID')
    return effects.HasTargetEffect(varID, _EFFECT_TYPE.SET_VAR, conditions=conditions)


def _readGuiItemPropertiesEffectSection(xmlCtx, section, _, conditions, fixedProp=None):
    itemID = parseID(xmlCtx, section, b'Specify a item ID')
    props = {}
    if fixedProp is None:
        for _, subSec in _xml.getChildren(xmlCtx, section, b'properties'):
            propType, propSec = subSec.items()[0]
            props[subSec.asString] = readVarValue(propType, propSec)

    else:
        propName, propType = fixedProp
        if propType is not None:
            props[propName] = readVarValue(propType, _xml.getSubsection(xmlCtx, section, b'val'))
        else:
            props[propName] = None
    return effects.SetGuiItemProperties(itemID, props, conditions=conditions)


def _readPlayAnimationEffectSection(xmlCtx, section, _, conditions):
    itemID = parseID(xmlCtx, section, b'Specify an item ID')
    animType = _xml.readString(xmlCtx, section, b'type')
    waitForFinish = _xml.readBool(xmlCtx, section, b'wait_for_finish')
    return effects.PlayAnimationEffect(itemID, animType, waitForFinish, conditions=conditions)


def _readInvokeGuiCmdSection(xmlCtx, section, _, conditions):
    commandID = parseID(xmlCtx, section, b'Specify a command ID')
    argOverrides = {}
    argsSection = _xml.getSubsection(xmlCtx, section, b'args', throwIfMissing=False)
    if argsSection is not None:
        for _, subSec in argsSection.items():
            arg = resource_helper.readItem(xmlCtx, subSec, b'arg')
            argOverrides[arg.name] = arg.value

    return effects.InvokeGuiCommand(commandID, argOverrides, conditions=conditions)


def _readGoSceneSection(xmlCtx, section, _, conditions):
    sceneID = parseID(xmlCtx, section, b'Specify a setting ID')
    return effects.HasTargetEffect(sceneID, _EFFECT_TYPE.GO_SCENE, conditions=conditions)


def _readSetAllowedToFightEffectSection(xmlCtx, section, _, conditions):
    value = _xml.readBool(xmlCtx, section, b'value')
    return effects.SetAllowedToFightEffect(value, conditions=conditions)


def _readSelectVehicleInHangarSection(xmlCtx, section, flags, conditions):
    targetID = section.asString
    return effects.HasTargetEffect(targetID, effects.EFFECT_TYPE.SELECT_VEHICLE_IN_HANGAR, conditions=conditions)


def _readPlaySoundEffectSection(xmlCtx, section, flags, conditions):
    soundID = section.asString
    soundEvent = _xml.readString(xmlCtx, section, b'event')
    soundEvent = getattr(SOUND_EVENT, soundEvent, None)
    return effects.PlaySoundEffect(soundID, soundEvent, conditions=conditions)


def _readCloseViewEffectSection(xmlCtx, section, flags, conditions):
    layer = LAYER_NAMES.LAYER_ORDER.index(_xml.readString(xmlCtx, section, b'type'))
    viewAlias = _xml.readString(xmlCtx, section, b'alias')
    return effects.HasTargetEffect((
     layer, viewAlias), effects.EFFECT_TYPE.CLOSE_VIEW, conditions=conditions)


def makeSimpleEffectReader(effectType):
    return (lambda xmlCtx, section, flags, conditions: effects.SimpleEffect(effectType=effectType, conditions=conditions))


_BASE_EFFECT_TAGS = {b'effects-group': _readEffectsGroupSection, 
   b'activate': _readActivateEffectSection, 
   b'inactivate': _readDeactivateEffectSection, 
   b'global-activate': _readGlobalActivateEffectSection, 
   b'global-inactivate': _readGlobalDeactivateEffectSection, 
   b'refuse-training': (makeSimpleEffectReader(_EFFECT_TYPE.REFUSE_TRAINING)), 
   b'run-trigger': _readRunTriggerEffectSection, 
   b'set-gui-item-props': _readGuiItemPropertiesEffectSection, 
   b'set-visible': (partial(_readGuiItemPropertiesEffectSection, fixedProp=(b'visible', b'asBool'))), 
   b'set-button-enabled': (partial(_readGuiItemPropertiesEffectSection, fixedProp=(b'enabled', b'asBool'))), 
   b'update-layout': (partial(_readGuiItemPropertiesEffectSection, fixedProp=(b'layout', None))), 
   b'play-animation': _readPlayAnimationEffectSection, 
   b'finish-training': (makeSimpleEffectReader(_EFFECT_TYPE.FINISH_TRAINING)), 
   b'go-scene': _readGoSceneSection, 
   b'invoke-gui-cmd': _readInvokeGuiCmdSection, 
   b'show-hint': _readShowHintSection, 
   b'close-hint': _readCloseHintSection, 
   b'show-dialog': _readShowDialogSection, 
   b'show-window': _readShowWindowSection, 
   b'set-gui-item-criteria': _readSetGuiItemCriteria, 
   b'set-gui-item-view-criteria': _setReadGuiItemViewCriteria, 
   b'set-action': _readSetActionSection, 
   b'remove-action': _readRemoveActionSection, 
   b'set-var': _readSetVarSection, 
   b'clear-scene': (makeSimpleEffectReader(_EFFECT_TYPE.CLEAR_SCENE)), 
   b'set-allowed-to-fight': _readSetAllowedToFightEffectSection, 
   b'select-in-hangar': _readSelectVehicleInHangarSection, 
   b'play-sound': _readPlaySoundEffectSection, 
   b'close-view': _readCloseViewEffectSection}
_EFFECT_TAGS = _BASE_EFFECT_TAGS.copy()

def setEffectsParsers(parsers):
    global _BASE_EFFECT_TAGS
    global _EFFECT_TAGS
    _EFFECT_TAGS.clear()
    _EFFECT_TAGS = _BASE_EFFECT_TAGS.copy()
    _EFFECT_TAGS.update(parsers)
    return


def _parseEffect(xmlCtx, section, flags):
    function = _EFFECT_TAGS.get(section.name)
    result = None
    if function is not None:
        result = function(xmlCtx, section, flags, _parseConditions(xmlCtx, section, flags))
    else:
        LOG_ERROR(b'Effect is not supported:', section.name)
    return result


_TRIGGER_SUB_PARSERS = {}

def readValidateVarTriggerSection(xmlCtx, section, triggerID, clazz, **kwargs):
    validateVarID = _xml.readString(xmlCtx, section, b'validate-var')
    setVarID = section.readString(b'set-var')
    if not setVarID:
        setVarID = None
    return clazz(triggerID, validateVarID, setVarID=setVarID, **kwargs)


def setTriggersParsers(parsers):
    global _TRIGGER_SUB_PARSERS
    _TRIGGER_SUB_PARSERS.clear()
    _TRIGGER_SUB_PARSERS = parsers.copy()
    return


def parseTrigger(xmlCtx, section, flags, chapter):
    triggerID = parseID(xmlCtx, section, b'Specify a trigger ID')
    trigger = None
    triggerType = _xml.readString(xmlCtx, section, b'type')
    parser = _TRIGGER_SUB_PARSERS.get(triggerType)
    if parser is not None:
        trigger = parser(xmlCtx, section, chapter, triggerID)
        if b'on-effects' in section.keys():
            for _, effectSec in _xml.getChildren(xmlCtx, section, b'on-effects'):
                effect = _parseEffect(xmlCtx, effectSec, flags)
                if effect is not None:
                    trigger.addOnEffect(effect)

        if b'off-effects' in section.keys():
            for _, effectSec in _xml.getChildren(xmlCtx, section, b'off-effects'):
                effect = _parseEffect(xmlCtx, effectSec, flags)
                if effect is not None:
                    trigger.addOffEffect(effect)

        if b'exclude-triggers' in section.keys():
            for _, triggerSec in _xml.getChildren(xmlCtx, section, b'exclude-triggers'):
                trigger.addExcludeTriggerID(triggerSec.asString)

    else:
        LOG_ERROR(b'Trigger is not supported:', triggerType)
    return trigger


def _parseGuiItem(xmlCtx, section, flags, itemFlags):
    itemID = parseID(xmlCtx, section, b'Specify a GUI item ID')
    tags = section.keys()
    item = tutorial_chapter.GuiItemRef(itemID, conditions=_parseConditions(xmlCtx, section, flags))
    if b'on-scene-effects' in tags:
        for _, effectSec in _xml.getChildren(xmlCtx, section, b'on-scene-effects'):
            effect = _parseEffect(xmlCtx, effectSec, itemFlags)
            if effect is not None:
                item.addOnSceneEffect(effect)

    if b'not-on-scene-effects' in tags:
        for _, effectSec in _xml.getChildren(xmlCtx, section, b'not-on-scene-effects'):
            effect = _parseEffect(xmlCtx, effectSec, itemFlags)
            if effect is not None:
                item.addNotOnSceneEffect(effect)

    return item


def _readAsStringSection(name, section):
    return translation(getattr(section, name))


def _readAsListSection(_, section):
    value = []
    for name, subSec in section.items():
        if name == b'condition':
            continue
        value.append(readVarValue(name, subSec))

    return value


def _readAsDictSection(_, section):
    value = {}
    for name, subSec in section.items():
        valueType, valueSec = subSec.items()[0]
        value[name] = readVarValue(valueType, valueSec)

    return value


def _readAsIntSequence(_, section):
    return [int(item) if item else None for item in section.asString.split(b' ')]


def _readAsVehTypeNameSection(_, section):
    return vehicles.makeIntCompactDescrByID(b'vehicle', *vehicles.g_list.getIDsByName(section.asString))


def _readAsVehItemNameSection(itemName, itemIDsMethod, section):
    nationName, chassisName = section.asString.split(b':')
    nationID = nations.INDICES[nationName]
    itemGetter = getattr(vehicles.g_cache, itemIDsMethod)
    return vehicles.makeIntCompactDescrByID(itemName, nationID, itemGetter(nationID)[chassisName])


def _readAsEquipmentSection(_, section):
    equipmentName = section.asString
    return vehicles.makeIntCompactDescrByID(b'equipment', nations.NONE_INDEX, vehicles.g_cache.equipmentIDs()[equipmentName])


def _readAsItemSection(_, section):
    return {(section.readInt(b'itemTypeCD')): (section.readInt(b'count'))}


def _readAsBoosterSection(_, section):
    return {(section.readInt(b'boosterID')): {b'count': (section.readInt(b'count'))}}


def _readAsItemsDict(_, section):
    value = {}
    for name, subSec in section.items():
        value.update(readVarValue(name, subSec))

    return value


CUSTOM_VARS_PARERS = {b'asString': _readAsStringSection, 
   b'asDict': _readAsDictSection, 
   b'asList': _readAsListSection, 
   b'asIntSequence': _readAsIntSequence, 
   b'asVehTypeName': _readAsVehTypeNameSection, 
   b'asVehChassisName': (lambda name, section: _readAsVehItemNameSection(b'vehicleChassis', b'chassisIDs', section)), 
   b'asVehGunName': (lambda name, section: _readAsVehItemNameSection(b'vehicleGun', b'gunIDs', section)), 
   b'asVehEngineName': (lambda name, section: _readAsVehItemNameSection(b'vehicleEngine', b'engineIDs', section)), 
   b'asVehRadioName': (lambda name, section: _readAsVehItemNameSection(b'vehicleRadio', b'radioIDs', section)), 
   b'asVehTurretName': (lambda name, section: _readAsVehItemNameSection(b'vehicleTurret', b'turretIDs', section)), 
   b'asEquipment': _readAsEquipmentSection, 
   b'asItem': _readAsItemSection, 
   b'asBooster': _readAsBoosterSection, 
   b'asItemsDict': _readAsItemsDict}

def readVarValue(name, section):
    if name in CUSTOM_VARS_PARERS:
        value = CUSTOM_VARS_PARERS[name](name, section)
    else:
        value = getattr(section, name)
    return value


def parseVarSet(xmlCtx, section, flags):
    varID = parseID(xmlCtx, section, b'Specify a var ID')
    varSet = []
    for name, subSec in section.items():
        value = readVarValue(name, subSec)
        varSet.append((value, _parseConditions(xmlCtx, subSec, flags)))

    return tutorial_chapter.VarSet(varID, varSet)


def parseBonus(xmlCtx, section):
    tags = section.keys()
    altBonusValues = None
    if b'altBonus' in tags:
        altBonusSec = section[b'altBonus']
        altBonusValues = readValues(altBonusSec)
    valueCondition = None
    if b'valueCondition' in tags:
        valueConditionSec = section[b'valueCondition']
        valueCondition = _parseConditions(xmlCtx, valueConditionSec, [])
    return tutorial_chapter.Bonus(section.readInt(b'id', -1), section.readString(b'message'), readValues(section), altBonusValues, valueCondition)


_DIALOG_SUB_PARERS = {}

def setDialogsParsers(parsers):
    global _DIALOG_SUB_PARERS
    _DIALOG_SUB_PARERS.clear()
    _DIALOG_SUB_PARERS = parsers.copy()
    return


def _parseDialog(xmlCtx, section, flags):
    dialogID = parseID(xmlCtx, section, b'Specify a dialog ID')
    dialogType = _xml.readString(xmlCtx, section, b'type')
    bSec = _xml.getSubsection(xmlCtx, section, b'buttons')
    submitID = bSec.readString(b'submit', b'')
    cancelID = bSec.readString(b'cancel', b'')
    customID = bSec.readString(b'custom', b'')
    content = {b'type': dialogType, 
       b'dialogID': dialogID, 
       b'submitID': submitID, 
       b'cancelID': cancelID, 
       b'customID': customID, 
       b'title': (translation(_xml.readStringOrNone(xmlCtx, section, b'title') or b'')), 
       b'message': (translation(_xml.readStringOrNone(xmlCtx, section, b'text') or b'')), 
       b'imageUrl': (_xml.readStringOrNone(xmlCtx, section, b'image') or b'')}
    parser = _DIALOG_SUB_PARERS.get(dialogType)
    if parser is not None:
        dialog = parser(xmlCtx, section, flags, dialogID, dialogType, content)
    else:
        dialog = tutorial_chapter.PopUp(dialogID, dialogType, content)
    dialog.setActions(parseActions(xmlCtx, _xml.getSubsection(xmlCtx, section, b'actions'), flags))
    return dialog


_WINDOW_SUB_PARERS = {}

def setWindowsParsers(parsers):
    global _WINDOW_SUB_PARERS
    _WINDOW_SUB_PARERS.clear()
    _WINDOW_SUB_PARERS = parsers.copy()
    return


def _parseWindow(xmlCtx, section, flags):
    windowID = parseID(xmlCtx, section, b'Specify a window ID')
    windowType = _xml.readString(xmlCtx, section, b'type')
    content = {}
    bSec = _xml.getSubsection(xmlCtx, section, b'buttons')
    content[b'closeID'] = _xml.readString(xmlCtx, bSec, b'close')
    content[b'type'] = windowType
    content[b'windowID'] = windowID
    parser = _WINDOW_SUB_PARERS.get(windowType)
    if parser is not None:
        window = parser(xmlCtx, section, flags, windowID, windowType, content)
        window.setActions(parseActions(xmlCtx, _xml.getSubsection(xmlCtx, section, b'actions'), flags))
    else:
        window = None
        LOG_ERROR(b'Type of window is not supported: ', windowType)
    return window


def _parseMessage(xmlCtx, section, _):
    messageID = parseID(xmlCtx, section, b'Specify a message ID')
    guiType = _xml.readString(xmlCtx, section, b'type')
    text = translation(_xml.readString(xmlCtx, section, b'text'))
    return tutorial_chapter.Message(messageID, guiType, text)


def _readGuiItemCriteria(xmlCtx, section, _):
    criteriaID = parseID(xmlCtx, section, b'Specify a criteria ID')
    itemID = None
    if b'item-id' in section.keys():
        itemID = parseID(xmlCtx, section[b'item-id'], b'Specify a item ID')
    else:
        _xml.raiseWrongXml(xmlCtx, section.name, b'Specify a item ID')
    return tutorial_chapter.GuiItemCriteria(criteriaID, itemID, _xml.readString(xmlCtx, section, b'value'))


def _readGuiItemViewCriteria(xmlCtx, section, _):
    criteriaID = parseID(xmlCtx, section, b'Specify a criteria ID')
    componentIDs = [parseID(xmlCtx, componentSec, b'Specify a component ID') for _, componentSec in _xml.getChildren(xmlCtx, section, b'components')]
    return tutorial_chapter.GuiItemViewCriteria(criteriaID, componentIDs, _xml.readString(xmlCtx, section, b'value'))


def _readAction(xmlCtx, section, eventType, flags):
    actionID = parseID(xmlCtx, section, b'Specify a action ID')
    itemID = None
    if b'item-id' in section.keys():
        itemID = parseID(xmlCtx, section[b'item-id'], b'Specify a item ID')
    else:
        _xml.raiseWrongXml(xmlCtx, section.name, b'Specify a item ID')
    action = tutorial_chapter.Action(eventType, itemID)
    action.setID(actionID)
    for _, effectSec in _xml.getChildren(xmlCtx, section, b'effects'):
        effect = _parseEffect(xmlCtx, effectSec, flags)
        if effect is not None:
            action.addEffect(effect)

    return action


def _readClickAction(xmlCtx, section, flags):
    return _readAction(xmlCtx, section, GuiEventType.CLICK, flags)


def _readClickOutsideAction(xmlCtx, section, flags):
    return _readAction(xmlCtx, section, GuiEventType.CLICK_OUTSIDE, flags)


def _readEscapeAction(xmlCtx, section, flags):
    return _readAction(xmlCtx, section, GuiEventType.ESC, flags)


def _readEnableAction(xmlCtx, section, flags):
    return _readAction(xmlCtx, section, GuiEventType.ENABLE, flags)


def _readDisableAction(xmlCtx, section, flags):
    return _readAction(xmlCtx, section, GuiEventType.DISABLE, flags)


def _readGameAttribute(xmlCtx, section, _):
    attributeID = parseID(xmlCtx, section, b'Specify a attribute ID')
    tags = section.keys()
    if b'name' in tags:
        name = parseID(xmlCtx, section[b'name'], b'Specify a name of game attribute')
    else:
        _xml.raiseWrongXml(xmlCtx, section.name, b'Specify a item ID')
        return
    if b'var-ref' in tags:
        varID = parseID(xmlCtx, section[b'var-ref'], b'Specify a var ID')
    else:
        _xml.raiseWrongXml(xmlCtx, section.name, b'Specify a item ID')
        return
    value = section.readString(b'args')
    if value:
        args = value.split()
    else:
        args = None
    return tutorial_chapter.GameAttribute(attributeID, name, varID, args)


_BASE_ENTITY_PARSERS = {b'dialog': _parseDialog, 
   b'window': _parseWindow, 
   b'message': _parseMessage, 
   b'gui-item-criteria': _readGuiItemCriteria, 
   b'gui-item-view-criteria': _readGuiItemViewCriteria, 
   b'click-action': _readClickAction, 
   b'click-outside-action': _readClickOutsideAction, 
   b'esc-action': _readEscapeAction, 
   b'enable-action': _readEnableAction, 
   b'disable-action': _readDisableAction, 
   b'game-attribute': _readGameAttribute}
_ENTITY_PARSERS = _BASE_ENTITY_PARSERS.copy()

def setEntitiesParsers(parsers):
    global _BASE_ENTITY_PARSERS
    global _ENTITY_PARSERS
    _ENTITY_PARSERS.clear()
    _ENTITY_PARSERS = _BASE_ENTITY_PARSERS.copy()
    _ENTITY_PARSERS.update(parsers)
    return


def parseEntity(xmlCtx, name, section, flags):
    parser = _ENTITY_PARSERS.get(name)
    item = None
    if parser is not None:
        item = parser(xmlCtx, section, flags)
    else:
        LOG_ERROR(b'Entity is not supported:', name)
    return item


def readValues(section):
    result = {}
    valuesSec = section[b'values']
    if valuesSec is not None:
        for name, valueSection in valuesSec.items():
            valueType, valueSec = valueSection.items()[0]
            result[name] = readVarValue(valueType, valueSec)

    return result


_AVAILABLE_DIRECTIONS = (b'L', b'T', b'R', b'B')
_ArrowProps = namedtuple(b'_ArrowProps', (b'direction', b'loop', b'positionValue', b'textPadding'))
_Padding = namedtuple(b'_Padding', (b'left', b'top', b'right', b'bottom'))

def parseHint(xmlCtx, section):
    sectionInfo = dict()
    sectionInfo[b'hintID'] = parseID(xmlCtx, section, b'Specify a hint ID')
    tags = section.keys()
    if b'item-id' in tags:
        sectionInfo[b'itemID'] = parseID(xmlCtx, section[b'item-id'], b'Specify a item ID')
    else:
        _xml.raiseWrongXml(xmlCtx, section.name, b'Specify a item ID')
        return
    if b'text' in tags:
        sectionInfo[b'text'] = translation(_xml.readString(xmlCtx, section, b'text'))
    else:
        sectionInfo[b'text'] = b''
    if b'arrow' in tags:
        subSec = section[b'arrow']
        direction = _xml.readString(xmlCtx, subSec, b'direction')
        if direction not in _AVAILABLE_DIRECTIONS:
            _xml.raiseWrongXml(xmlCtx, section, (b'Arrow direction {} is invalid.').format(direction))
        positionValue = _xml.readFloat(xmlCtx, subSec, b'position-value', 0.5)
        textPadding = _xml.readFloat(xmlCtx, subSec, b'text-padding', 0)
        sectionInfo[b'arrow'] = _ArrowProps(direction, _xml.readBool(xmlCtx, subSec, b'loop'), positionValue, textPadding)
    else:
        sectionInfo[b'arrow'] = None
    if b'padding' in tags:
        subSec = section[b'padding']
        sectionInfo[b'padding'] = _Padding(_xml.readFloat(xmlCtx, subSec, b'left'), _xml.readFloat(xmlCtx, subSec, b'top'), _xml.readFloat(xmlCtx, subSec, b'right'), _xml.readFloat(xmlCtx, subSec, b'bottom'))
    else:
        sectionInfo[b'padding'] = None
    sectionInfo[b'hasBox'] = section.readBool(b'has-box', True)
    sectionInfo[b'conditions'] = _parseConditions(xmlCtx, section, [])
    sectionInfo[b'checked-ui-state'] = _parseNeededState(xmlCtx, section)
    sectionInfo[b'equalActions'] = section.readBool(b'equal-actions', False)
    sectionInfo[b'ignoreOutsideClick'] = section.readBool(b'ignore-outside-click', False)
    sectionInfo[b'updateRuntime'] = section.readBool(b'update-runtime', False)
    sectionInfo[b'hideImmediately'] = section.readBool(b'hide-immediately', False)
    sectionInfo[b'checkViewArea'] = section.readBool(b'check-view-area', False)
    return sectionInfo
