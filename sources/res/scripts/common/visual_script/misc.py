from __future__ import absolute_import
import typing
from debug_utils import LOG_ERROR, LOG_WARNING
if typing.TYPE_CHECKING:
    from typing import Dict, Union
    from ResMgr import DataSection
    from visual_script.block import Block
VisualScriptTag = b'visualScript'

class DeferredQueue(object):
    COMMON = 0
    SINGLE = 1


class ASPECT(object):
    SERVER = b'SERVER'
    CLIENT = b'CLIENT'
    HANGAR = b'HANGAR'
    ALL = [
     CLIENT, SERVER, HANGAR]


class EDITOR_TYPE(object):
    NONE = 0
    STR_KEY_SELECTOR = 1
    ENUM_SELECTOR = 2
    COMPLEX_KEY_SELECTOR = 3
    VEHICLE_NAME_SELECTOR = 4
    VEHICLE_PRESET_SELECTOR = 5


class EDITOR_CUSTOM_ICON(object):
    EVENT_DELAYED = 1


class BLOCK_MODE(object):
    NONE = 0
    UNIQUE = 32
    DEV = 64
    HIDE_FROM_LIB = 256
    DEPRECATED = 512
    CAN_BE_CONST_EXPR = 2048


def makePlanPath(planName):
    return (b'vscript/plans/{}.xml').format(planName)


def errorVScript(owner, msg):
    LOG_ERROR(b'[VScript]', str(owner.planName()), str(owner.blockId()), msg)
    owner._writeLog(b'%s:%s : %s' % (owner.planName(), owner.blockId(), msg))
    return


def warningVScript(owner, msg):
    LOG_WARNING(b'[VScript]', str(owner.planName()), str(owner.blockId()), msg)
    owner._writeLog(b'%s:%s : %s' % (owner.planName(), owner.blockId(), msg))
    return


def readVisualScriptPlanParams(section, commonParams={}):
    PARAM_READERS = {b'string': (lambda val: val.asString), 
       b'int': (lambda val: val.asInt), 
       b'float': (lambda val: val.asFloat), 
       b'bool': (lambda val: val.asBool)}
    DEFAULT_PARAM_READER = PARAM_READERS[b'string']
    params = dict(commonParams.items())
    if section.has_key(b'params'):
        for name, subsection in section[b'params'].items():
            if subsection.has_key(b'type'):
                paramReader = PARAM_READERS.get(subsection[b'type'].asString, DEFAULT_PARAM_READER)
            else:
                paramReader = DEFAULT_PARAM_READER
            if subsection.has_key(b'item'):
                params[name] = [paramReader(value) for value in subsection.values()]
            else:
                params[name] = paramReader(subsection)

    return params


def readVisualScriptPlan(section, commonParams={}):
    planDef = {}
    if section.has_key(b'name'):
        planDef[b'name'] = section[b'name'].asString
        planDef[b'params'] = readVisualScriptPlanParams(section, commonParams)
        planDef[b'plan_id'] = section[b'plan_id'].asString if section.has_key(b'plan_id') else b''
    else:
        planDef[b'name'] = section.asString
        planDef[b'params'] = dict(commonParams)
        planDef[b'plan_id'] = b''
    return planDef


def readVisualScriptPlans(section, commonParams={}):
    plans = []
    for name, subsection in section.items():
        if name == b'plan':
            plans.append(readVisualScriptPlan(subsection, commonParams))

    return plans


def readVisualScriptSection(section, aspects=None):
    if aspects is None:
        aspects = ASPECT.ALL
    if not aspects:
        return {}
    else:
        if section.has_key(VisualScriptTag):
            vseSection = section[VisualScriptTag]
            commonParams = {}
            if vseSection.has_key(b'common'):
                commonParams = readVisualScriptPlanParams(vseSection[b'common'])
            return {aspect: _readVisualScriptAspect(vseSection, aspect.lower(), commonParams) for aspect in aspects}
        return {aspect: [] for aspect in aspects}


def _readVisualScriptAspect(section, aspect, commonParams):
    plans = []
    if section.has_key(aspect):
        plans = readVisualScriptPlans(section[aspect], commonParams)
    return plans
