import BigWorld
from constants import IS_CLIENT, IS_BOT
from debug_utils import LOG_ERROR
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


class BLOCK_MODE(object):
    NONE = 0
    UNIQUE = 32
    DEV = 64
    HIDE_FROM_LIB = 256


def makePlanPath(planName):
    return (b'vscript/plans/{}.xml').format(planName)


def errorVScript(owner, msg):
    LOG_ERROR(b'[VScript]', owner.__class__.__name__, msg)
    owner._writeLog(b'%s : %s' % (owner.__class__.__name__, msg))
    return


def readVisualScriptPlanParams(section, commonParams={}):
    params = dict(commonParams.items())
    if section.has_key(b'params'):
        for name, subsection in section[b'params'].items():
            if subsection.has_key(b'item'):
                params[name] = [value.asString for idx, value in subsection.items()]
            else:
                params[name] = subsection.asString

    return params


def readVisualScriptPlans(section, commonParams={}):
    plans = []
    for name, subsection in section.items():
        if name == b'plan':
            planDef = {}
            if subsection.has_key(b'name'):
                planDef[b'name'] = subsection[b'name'].asString
                planDef[b'params'] = readVisualScriptPlanParams(subsection, commonParams)
                planDef[b'plan_id'] = subsection[b'plan_id'].asString if subsection.has_key(b'plan_id') else b''
            else:
                planDef[b'name'] = subsection.asString
                planDef[b'params'] = dict(commonParams)
                planDef[b'plan_id'] = b''
            plans.append(planDef)

    return plans
