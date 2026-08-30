from functools import partial
import resource_helper
from tutorial.doc_loader import sub_parsers
from tutorial.data import chapter, effects
from tutorial.data.conditions import Conditions, ComponentOnSceneCondition, CONDITION_STATE as _COND_STATE
from tutorial.data.bootcamp.checkpoint import Checkpoint
from tutorial.data.bootcamp import effects as bc_effects
from tutorial.control.bootcamp.lobby import triggers as bc_triggers, conditions as bc_conditions
from tutorial.control import triggers
from items import _xml
from tutorial.data.effects import EFFECT_TYPE as _EFFECT_TYPE

def _fillValue(targetDict, xmlCtx, section, key, readFunc, default=None, **kwargs):
    val = readFunc(xmlCtx, section, key, **kwargs)
    if val is None:
        val = default
    targetDict[key] = val
    return val


def _readBootcampMessageDialogSection(xmlCtx, section, _, dialogID, dialogType, content):
    content[b'sequence'] = [_readMessageDialogSequenceItem(xmlCtx, messageSec) for _, messageSec in _xml.getChildren(xmlCtx, section, b'sequence')]
    return chapter.PopUp(dialogID, dialogType, content, varRef=None, forcedQuery=True)


def _readMessageDialogSequenceItem(xmlCtx, section):
    messageContent = {}
    nations = _xml.getChildren(xmlCtx, section, b'nations', False)
    if nations:
        nationsDataDict = messageContent[b'nations_data'] = {}
        for _, subSec in nations:
            nationID, data = _readMessageDialogData(xmlCtx, subSec, True)
            nationsDataDict[nationID] = data

    else:
        subSec = _xml.getSubsection(xmlCtx, section, b'data')
        _, messageContent[b'data'] = _readMessageDialogData(xmlCtx, subSec, False)
    return messageContent


def _readSequenceItem(ctx, sec, fields):
    messageContent = {b'data': {}}
    if fields:
        subSec = _xml.getSubsection(ctx, sec, b'data')
        for field in fields:
            _fillValue(messageContent[b'data'], ctx, subSec, field, _xml.readStringOrNone, default=b'')

    return messageContent


def _readSubtitleWindowSection(xmlCtx, section, _, windowID, windowType, content):
    fields = (b'subtitle', b'voiceover')
    content[b'sequence'] = [_readSequenceItem(xmlCtx, messageSec, fields) for _, messageSec in _xml.getChildren(xmlCtx, section, b'sequence')]
    return chapter.PopUp(windowID, windowType, content, varRef=None, forcedQuery=True)


def _readVideoWindowSection(xmlCtx, section, _, windowID, windowType, content):
    fields = (b'subtitle', b'video-path', b'event-start', b'event-stop', b'event-pause', b'event-resume', b'event-loop', b'video-fit-to-screen')
    content[b'sequence'] = [_readSequenceItem(xmlCtx, messageSec, fields) for _, messageSec in _xml.getChildren(xmlCtx, section, b'sequence')]
    return chapter.PopUp(windowID, windowType, content, varRef=None, forcedQuery=True)


def _readMessageDialogData(xmlCtx, section, isNation):
    nationID = _xml.readString(xmlCtx, section, b'nation_id') if isNation else None
    data = {}
    _fillValue(data, xmlCtx, section, b'preset', _xml.readString)
    _fillValue(data, xmlCtx, section, b'icon', _xml.readStringOrNone, default=b'')
    _fillValue(data, xmlCtx, section, b'label', _xml.readStringOrNone, default=b'')
    _fillValue(data, xmlCtx, section, b'label_first_bootcamp', partial(_xml.readStringOrNone))
    _fillValue(data, xmlCtx, section, b'text', _xml.readStringOrNone, default=b'')
    _fillValue(data, xmlCtx, section, b'subtitle', _xml.readStringOrNone, default=b'')
    _fillValue(data, xmlCtx, section, b'voiceover', _xml.readStringOrNone, default=b'')
    _fillValue(data, xmlCtx, section, b'description', _xml.readStringOrNone, default=b'')
    _fillValue(data, xmlCtx, section, b'background', _xml.readStringOrNone, default=b'')
    _fillValue(data, xmlCtx, section, b'only_first_bootcamp_bottom', partial(_xml.readBool, default=False))
    bottomRenderer = _fillValue(data, xmlCtx, section, b'bottom_renderer', _xml.readStringOrNone, default=b'')
    bottomDataList = data[b'bottom'] = []
    if bottomRenderer:
        for name, dataSection in _xml.getChildren(xmlCtx, section, b'bottom'):
            if name == b'data':
                bottomData = {}
                _fillValue(bottomData, xmlCtx, dataSection, b'icon', _xml.readStringOrNone, default=b'')
                _fillValue(bottomData, xmlCtx, dataSection, b'label', _xml.readStringOrNone, default=b'')
                _fillValue(bottomData, xmlCtx, dataSection, b'label_format', _xml.readStringOrNone, default=b'')
                _fillValue(bottomData, xmlCtx, dataSection, b'description', _xml.readStringOrNone, default=b'')
                _fillValue(bottomData, xmlCtx, dataSection, b'iconTooltip', _xml.readStringOrNone, default=b'')
                _fillValue(bottomData, xmlCtx, dataSection, b'labelTooltip', _xml.readStringOrNone, default=b'')
                _fillValue(bottomData, xmlCtx, dataSection, b'animationTarget', _xml.readStringOrNone, default=b'')
                _fillValue(bottomData, xmlCtx, dataSection, b'animationType', _xml.readStringOrNone, default=b'')
                bottomDataList.append(bottomData)

    return (
     nationID, data)


def _readBootcampSelectNationDialogSection(xmlCtx, section, _, dialogID, dialogType, content):
    content[b'resultVarID'] = _xml.readString(xmlCtx, section, b'result-var')
    return chapter.PopUp(dialogID, dialogType, content, varRef=None, forcedQuery=False)


def _readCheckpointSection(xmlCtx, section, flags):
    checkpointID = sub_parsers.parseID(xmlCtx, section, b'missing checkpoint ID')
    checkpointConditions = sub_parsers.readConditions(xmlCtx, _xml.getSubsection(xmlCtx, section, b'condition'), flags)
    checkpointEffects = [effect for effect in (sub_parsers._parseEffect(xmlCtx, effectSec, flags) for _, effectSec in _xml.getChildren(xmlCtx, section, b'effects')) if effect is not None]
    return Checkpoint(checkpointID, checkpointConditions, checkpointEffects)


def _readLinearCheckpointControllerTriggerSection(xmlCtx, section, _, triggerID):
    checkpointsSequence = [sub_parsers.parseID(xmlCtx, subSec, b'missing checkpoint ID in sequence') for _, subSec in _xml.getChildren(xmlCtx, section, b'sequence')]
    return sub_parsers.readValidateVarTriggerSection(xmlCtx, section, triggerID, bc_triggers.LinearCheckpointControllerTrigger, checkpointsSequence=checkpointsSequence)


def _makeSimpleValidateVarTriggerReader(clazz):
    return (lambda xmlCtx, section, _, triggerID: sub_parsers.readValidateVarTriggerSection(xmlCtx, section, triggerID, clazz))


def _readCheckpointReachedCondition(xmlCtx, section, state):
    checkpointID = sub_parsers.parseID(xmlCtx, section, b'missing checkpoint ID in condition')
    return bc_conditions.CheckpointReachedCondition(checkpointID, state=state)


def _readRequestExclusiveHintEffectSection(xmlCtx, section, _, conditions):
    componentID = sub_parsers.parseID(xmlCtx, section, b'missing hint target component ID')
    soundID = _xml.readStringOrNone(xmlCtx, section, b'sound')
    if soundID is None:
        soundID = b'bc_new_ui_element_button'
    if conditions is None:
        conditions = Conditions()
    conditions.insert(0, ComponentOnSceneCondition(componentID))
    return bc_effects.RequestExclusiveHintEffect(componentID, soundID, conditions=conditions)


def _readStartPlanSection(xmlCtx, section, _, conditions):
    item = resource_helper.readStringItem(resource_helper.ResourceCtx(xmlCtx[1]), _xml.getSubsection(xmlCtx, section, b'plan'))
    planName = item.value
    return bc_effects.StartVSEPlanEffect(planName, conditions=conditions)


def _readSetBootcampNationEffectSection(xmlCtx, section, _, conditions):
    varID = sub_parsers.parseID(xmlCtx, section, b'missing selected nation variable ID')
    return effects.HasTargetEffect(varID, _EFFECT_TYPE.SET_BOOTCAMP_NATION, conditions=conditions)


def init():
    sub_parsers.setEffectsParsers({b'request-exclusive-hint': _readRequestExclusiveHintEffectSection, 
       b'update-exclusive-hints': (sub_parsers.makeSimpleEffectReader(_EFFECT_TYPE.UPDATE_EXCLUSIVE_HINTS)), 
       b'start-vse-plan': _readStartPlanSection, 
       b'restore-checkpoint': (sub_parsers.makeSimpleEffectReader(_EFFECT_TYPE.RESTORE_CHECKPOINT)), 
       b'save-checkpoint': (sub_parsers.makeSimpleEffectReader(_EFFECT_TYPE.SAVE_CHECKPOINT)), 
       b'set-bootcamp-nation': _readSetBootcampNationEffectSection, 
       b'play-final-video': (sub_parsers.makeSimpleEffectReader(_EFFECT_TYPE.PLAY_VIDEO)), 
       b'show-demo-acc-renaming': (sub_parsers.makeSimpleEffectReader(_EFFECT_TYPE.SHOW_DEMO_ACCOUNT_RENAMING))})
    sub_parsers.setEntitiesParsers({b'checkpoint': _readCheckpointSection})
    sub_parsers.setTriggersParsers({b'linear-checkpoint-controller': _readLinearCheckpointControllerTriggerSection, 
       b'current-vehicle-changed': (_makeSimpleValidateVarTriggerReader(triggers.CurrentVehicleChangedTrigger)), 
       b'items-cache-sync': (_makeSimpleValidateVarTriggerReader(triggers.ItemsCacheSyncTrigger))})
    sub_parsers.setDialogsParsers({b'bootcampMessage': _readBootcampMessageDialogSection, 
       b'bootcampSelectNation': _readBootcampSelectNationDialogSection, 
       b'bootcampVideo': _readVideoWindowSection})
    sub_parsers.setConditionsParsers({b'checkpoint-reached': (lambda xmlCtx, section, flags: _readCheckpointReachedCondition(xmlCtx, section, _COND_STATE.ACTIVE)), 
       b'checkpoint-not-reached': (lambda xmlCtx, section, flags: _readCheckpointReachedCondition(xmlCtx, section, ~_COND_STATE.ACTIVE))})
    sub_parsers.setWindowsParsers({b'bootcampSubtitle': _readSubtitleWindowSection})
    return
