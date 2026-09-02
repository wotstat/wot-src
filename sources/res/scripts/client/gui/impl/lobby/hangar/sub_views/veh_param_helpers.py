from __future__ import absolute_import
import json
from builtins import round
from past.builtins import basestring
from gui.impl import backport
from gui.impl.gen.view_models.views.lobby.hangar.sub_views.vehicle_param_base_view_model import HighlightType
from gui.impl.gen.view_models.views.lobby.hangar.sub_views.vehicle_param_group_view_model import BuffIconType
from gui.shared.gui_items import KPI, kpiFormatValue
from gui.shared.items_parameters import MAX_RELATIVE_VALUE
from gui.shared.items_parameters.comparator import PARAM_STATE
from gui.shared.items_parameters.formatters import FORMAT_SETTINGS, KPI_FORMATTERS, SMART_ROUND_PARAMS
from gui.shared.items_parameters.params_helper import hasPositiveEffect, hasNegativeEffect, hasGroupPenalties
_EQUAL_TO_ZERO_LITERAL = b'~0'
_NUMBER_DIGITS = 2
_STATE_COLOR_MAP = {(PARAM_STATE.BETTER): b'%(green_open)s{}%(green_close)s', 
   (PARAM_STATE.WORSE): b'%(red_open)s{}%(red_close)s', 
   (PARAM_STATE.SITUATIONAL): b'%(yellow_open)s{}%(yellow_close)s'}

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
    if isinstance(value, basestring):
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
    color = _STATE_COLOR_MAP.get(stateType, b'')
    if color:
        return color.format(paramStr)
    return paramStr


def _cutDigits(value, nDigits=_NUMBER_DIGITS):
    if abs(value) > 99:
        return round(value)
    if abs(value) > 9:
        return round(value, 1)
    return round(value, nDigits)


def _mapStateToHighlight(state):
    mapping = {b'better': (HighlightType.INCREASE), 
       b'worse': (HighlightType.DECREASE), 
       b'normal': (HighlightType.NONE)}
    return mapping.get(state, HighlightType.SITUATIONAL)


def formatParameterValue(parameterName, paramValue, applyFormatting=True, parameterState=None, formatSettings=None, allowSmartRound=True, showZeroDiff=False, isColorize=True, nDigits=_NUMBER_DIGITS):
    if KPI.Name.hasValue(parameterName) and isinstance(paramValue, float):
        paramValue = round(paramValue, 3)
    if applyFormatting:
        _listFormat = {b'rounder': (lambda v: backport.getIntegralFormat(int(v))), 
           b'separator': b'/'}
        formatSettings = formatSettings or FORMAT_SETTINGS
        settings = formatSettings.get(parameterName, _listFormat)
        doSmartRound = allowSmartRound and parameterName in SMART_ROUND_PARAMS
        preprocessor = settings.get(b'preprocessor')
        if KPI.Name.hasValue(parameterName):
            formatter = KPI_FORMATTERS.get(parameterName, kpiFormatValue)
            values, separator = formatter(parameterName, paramValue), None
        elif preprocessor:
            values, separator, parameterState = preprocessor(paramValue, parameterState)
        else:
            values = paramValue
            separator = None
        if values is None:
            return
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
    else:
        if not isinstance(paramValue, (list, tuple)):
            paramValue = [
             paramValue]
        if isinstance(parameterState, tuple) and len(parameterState) == 1 and isinstance(parameterState[0], tuple):
            parameterState = parameterState[0]
        extractedStates = (state[0] if isinstance(state, tuple) else state for state in parameterState)
        return json.dumps([{b'value': v, b'state': (_mapStateToHighlight(s).value)} for v, s in zip(paramValue, extractedStates)])


def formatAdditionalParameter(parameter, isApproximately=False):
    delta = int(parameter.state[1])
    if delta:
        sign = b'-' if delta < 0 else b'+'
        approximatelySymbol = b'*' if isApproximately else b''
        deltaStr = colorize(b'%s%s%s' % (sign, abs(delta), approximatelySymbol), parameter.state)
        return b'(%s)' % deltaStr
    return b''
