from gui.impl import backport
from gui.impl.gen.view_models.views.lobby.hangar.sub_views.vehicle_param_group_view_model import BuffIconType
from gui.shared.gui_items import KPI, kpiFormatValue
from gui.shared.items_parameters import MAX_RELATIVE_VALUE
from gui.shared.items_parameters.comparator import PARAM_STATE
from gui.shared.items_parameters.formatters import FORMAT_SETTINGS, KPI_FORMATTERS, KPIFormatter
from gui.shared.items_parameters.params_helper import hasPositiveEffect, hasNegativeEffect, hasGroupPenalties
from gui.shared.utils import DUAL_GUN_RATE_TIME, DUAL_GUN_CHARGE_TIME
_SMART_ROUND_PARAMS = (b'damage', b'piercingPower', b'bombDamage', b'shellsCount', b'shellReloadingTime',
 b'reloadMagazineTime', b'reloadTime', b'dispertionRadius', b'aimingTime', b'weight',
 DUAL_GUN_RATE_TIME, DUAL_GUN_CHARGE_TIME, b'crewRolesFactor')
_EQUAL_TO_ZERO_LITERAL = b'~0'
_NUMBER_DIGITS = 2

def getGroupIcon(parameter, comparator):
    states = {0: (BuffIconType.NONE), 
       1: (BuffIconType.INCREASE), 
       2: (BuffIconType.DECREASE), 
       3: (BuffIconType.MIXED)}
    state = 0
    if hasPositiveEffect(parameter.name, comparator):
        state |= 1
    if hasNegativeEffect(parameter.name, comparator):
        state |= 2
    if hasGroupPenalties(parameter.name, comparator):
        state |= 2
    return states[state]


def getMaxValue(value, delta):
    return max(MAX_RELATIVE_VALUE, value + delta)


def _applyFormat(value, state, settings, doSmartRound, isColorize, nDigits=_NUMBER_DIGITS):
    if doSmartRound:
        value = _cutDigits(value, nDigits)
    if isinstance(value, (str, unicode)):
        paramStr = value
    elif value is None:
        paramStr = b'--'
    else:
        paramStr = settings[b'rounder'](value)
    if state is not None:
        if paramStr == _EQUAL_TO_ZERO_LITERAL and isinstance(state, (tuple, list)):
            stateType, value = state
            if value > 0:
                paramStr = b'+&lt;0.01'
            elif value < 0:
                paramStr = b'-&lt;0.01'
            if stateType == PARAM_STATE.NORMAL:
                paramStr = b'0'
        if isColorize:
            paramStr = colorize(paramStr, state)
    return paramStr


def colorize(paramStr, state):
    if isinstance(state, (tuple, list)):
        stateType, _ = state
    else:
        stateType = state
    if stateType == PARAM_STATE.NOT_APPLICABLE:
        return paramStr
    if stateType == PARAM_STATE.WORSE:
        return (b'%(red_open)s{}%(red_close)s').format(paramStr)
    if stateType == PARAM_STATE.BETTER:
        return (b'%(green_open)s{}%(green_close)s').format(paramStr)
    return paramStr


def _cutDigits(value, nDigits=_NUMBER_DIGITS):
    if abs(value) > 99:
        return round(value)
    if abs(value) > 9:
        return round(value, 1)
    return round(value, nDigits)


def formatParameterValue(parameterName, paramValue, parameterState=None, formatSettings=None, allowSmartRound=True, showZeroDiff=False, isColorize=True, nDigits=_NUMBER_DIGITS):
    _listFormat = {b'rounder': (lambda v: backport.getIntegralFormat(int(v))), 
       b'separator': b'/'}
    _kpiFormatValue = KPIFormatter(formatter=kpiFormatValue, separator=None, addEnding=True)
    formatSettings = formatSettings or FORMAT_SETTINGS
    settings = formatSettings.get(parameterName, _listFormat)
    doSmartRound = allowSmartRound and parameterName in _SMART_ROUND_PARAMS
    preprocessor = settings.get(b'preprocessor')
    if KPI.Name.hasValue(parameterName):
        formatter, separator, addEnding = KPI_FORMATTERS.get(parameterName, _kpiFormatValue)
        values = formatter(parameterName, paramValue, addEnding)
    elif preprocessor:
        values, separator, parameterState = preprocessor(paramValue, parameterState)
    else:
        values = paramValue
        separator = None
    if values is None:
        return
    else:
        if isinstance(values, (tuple, list)):
            if parameterState is None:
                parameterState = [
                 None] * len(values)
            if doSmartRound and len(set(values)) == 1:
                if values[0] > 0:
                    return _applyFormat(values[0], parameterState[0], settings, doSmartRound, isColorize, nDigits)
                return
            separator = separator or settings.get(b'separator', b'')
            paramsList = [_applyFormat(val, state, settings, doSmartRound, isColorize, nDigits) for val, state in zip(values, parameterState)]
            return separator.join(paramsList)
        if not showZeroDiff and values == 0:
            return
        return _applyFormat(values, parameterState, settings, doSmartRound, isColorize, nDigits)


def formatAdditionalParameter(parameter, isApproximately=False):
    delta = int(parameter.state[1])
    if delta:
        sign = b'-' if delta < 0 else b'+'
        approximatelySymbol = b'*' if isApproximately else b''
        deltaStr = colorize(b'%s%s%s' % (sign, abs(delta), approximatelySymbol), parameter.state)
        return b'(%s)' % deltaStr
    return b''
