from gui.shared.event_bus import EVENT_BUS_SCOPE
from items import _xml
from tutorial.control.sales import triggers
from tutorial.data import chapter, effects
from tutorial.doc_loader import sub_parsers
from tutorial.doc_loader.sub_parsers import readVarValue, parseID

def readLoadViewDataSection(xmlCtx, section, flags):
    settingID = parseID(xmlCtx, section, b'Specify a setting ID')
    alias = None
    if b'alias' in section.keys():
        alias = _xml.readString(xmlCtx, section, b'alias')
    else:
        _xml.raiseWrongXml(xmlCtx, section.name, b'Specify a setting name')
    scope = EVENT_BUS_SCOPE.DEFAULT
    if b'scope' in section.keys():
        scope = _xml.readInt(xmlCtx, section, b'scope')
    else:
        _xml.raiseWrongXml(xmlCtx, section.name, b'Specify a setting value')
    ctx = None
    if b'context' in section.keys():
        ctx = readVarValue(b'asDict', section[b'context'])
    return chapter.LoadViewData(settingID, alias, scope, ctx)


def readIsCollectibleVehicleTrigger(_, __, ___, triggerID):
    return triggers.IsCollectibleVehicleTrigger(triggerID)


def readTimerTriggerSection(xmlCtx, section, _, triggerID):
    return sub_parsers.readValidateVarTriggerSection(xmlCtx, section, triggerID, triggers.TimerTrigger)


def readCurrentVehicleChangedTriggerSection(xmlCtx, section, _, triggerID):
    unlockTargetIDs = _readUnlockTargetIDs(xmlCtx, section)
    return sub_parsers.readValidateVarTriggerSection(xmlCtx, section, triggerID, triggers.CurrentVehicleChangedTrigger, unlockTargetIDs=unlockTargetIDs)


def readItemsCacheSyncTriggerSection(xmlCtx, section, _, triggerID):
    unlockTargetIDs = _readUnlockTargetIDs(xmlCtx, section)
    return sub_parsers.readValidateVarTriggerSection(xmlCtx, section, triggerID, triggers.ItemsCacheSyncTrigger, unlockTargetIDs=unlockTargetIDs)


def readResearchGoToNextVehicleTriggerSection(xmlCtx, section, _, triggerID):
    unlockTargetIDs = _readUnlockTargetIDs(xmlCtx, section)
    return sub_parsers.readValidateVarTriggerSection(xmlCtx, section, triggerID, triggers.ResearchGoToNextVehicleTrigger, unlockTargetIDs=unlockTargetIDs)


def _readUnlockTargetIDs(xmlCtx, section):
    unlockTargetIDs = []
    if b'unlock-targets' in section.keys():
        for _, subSec in _xml.getChildren(xmlCtx, section, b'unlock-targets'):
            unlockTargetIDs.append(parseID(xmlCtx, subSec, b'Specify a target ID'))

    return unlockTargetIDs


def readHintSection(xmlCtx, section, flags):
    sectionInfo = sub_parsers.parseHint(xmlCtx, section)
    hint = chapter.ChainHint(sectionInfo[b'hintID'], sectionInfo[b'itemID'], sectionInfo[b'text'], sectionInfo[b'hasBox'], sectionInfo[b'arrow'], sectionInfo[b'padding'], sectionInfo[b'hideImmediately'], sectionInfo[b'updateRuntime'])
    hint.setActions(sub_parsers.parseActions(xmlCtx, _xml.getSubsection(xmlCtx, section, b'actions'), flags))
    return hint


def _reaLoadViewSection(xmlCtx, section, _, conditions):
    viewID = parseID(xmlCtx, section, b'Specify a view ID')
    return effects.HasTargetEffect(viewID, effects.EFFECT_TYPE.LOAD_VIEW, conditions=conditions)


def init():
    sub_parsers.setEntitiesParsers({b'hint': readHintSection, 
       b'view-data': readLoadViewDataSection})
    sub_parsers.setEffectsParsers({b'load-view': _reaLoadViewSection})
    sub_parsers.setTriggersParsers({b'timer': readTimerTriggerSection, 
       b'isCollectibleVehicle': readIsCollectibleVehicleTrigger, 
       b'current-vehicle-changed': readCurrentVehicleChangedTriggerSection, 
       b'items-cache-sync': readItemsCacheSyncTriggerSection, 
       b'research-go-to-next-vehicle': readResearchGoToNextVehicleTriggerSection})
    return
