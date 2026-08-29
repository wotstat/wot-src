import typing
from constants import QUEST_PROGRESS_STATE, VEHICLE_CLASSES
from gui.Scaleform.genConsts.QUESTSPROGRESS import QUESTSPROGRESS
from gui.Scaleform.genConsts.QUEST_PROGRESS_BASE import QUEST_PROGRESS_BASE
from gui.Scaleform.locale.QUESTS import QUESTS
from gui.shared.gui_items.Vehicle import VEHICLE_TYPES_ORDER
from gui.impl import backport
from helpers.time_utils import ONE_MINUTE
from personal_missions_constants import PROGRESS_TEMPLATE

class METRICS_TYPES(object):
    SIMPLE = QUEST_PROGRESS_BASE.QP_METRIC_TYPE_SIMPLE
    SIMPLE_VALUE = QUEST_PROGRESS_BASE.QP_METRIC_TYPE_SIMPLE_VALUE
    RANGE_VALUE = QUEST_PROGRESS_BASE.QP_METRIC_TYPE_RANGE
    VEHICLES_VALUE = QUEST_PROGRESS_BASE.QP_METRIC_TYPE_VEHICLES
    TIMER_VALUE = QUEST_PROGRESS_BASE.QP_METRIC_TYPE_TIMER
    VEHICLES_RANGE_VALUE = QUEST_PROGRESS_BASE.QP_VEHICLES_METRIC_TYPE_RANGE


def wrapSimple(_):
    return {b'mType': (METRICS_TYPES.SIMPLE)}


def wrapRangeValue(progress):
    if progress.getProgressID() == b'killsDiversity' and progress.isCumulative():
        return None
    else:
        return {b'title': (QUESTS.METRICS_TITLE_PROGRESS), 
           b'value': (_formatValue(progress.getCurrent())), 
           b'goal': (_formatValue(progress.getGoal())), 
           b'mType': (METRICS_TYPES.RANGE_VALUE)}


def wrapCurrentValue(progress):
    return _wrapSimpleValue(QUESTS.METRICS_TITLE_PROGRESS, _formatValue(progress.getCurrent()))


def wrapVehiclesValue(progress):
    vehTypesCount = progress.getUniqueGoal()
    totalTypesCount = len(VEHICLE_CLASSES)
    totalGoal = progress.getTotalGoal()
    doneTargets = progress.getDoneTargets()
    if (progress.isCumulative() or vehTypesCount == totalTypesCount) and totalGoal % 5 == 0:
        goal = totalGoal / vehTypesCount
        return _wrapRangeVehiclesValue(totalGoal, progress.getCounter(), goal)
    return _wrapVehiclesValue(QUESTS.METRICS_TITLE_DONE, progress.getCurrent(), doneTargets)


def wrapLimiterValue(progress):
    limiterProgress = progress.getLimiter()
    if limiterProgress.getTemplateID() == PROGRESS_TEMPLATE.BINARY:
        value = b''
    else:
        value = _formatValue(limiterProgress.getRest())
    return {b'mType': (QUEST_PROGRESS_BASE.QP_METRIC_TYPE_LIMITER), b'value': value, 
       b'isActive': (limiterProgress.getState() not in QUEST_PROGRESS_STATE.COMPLETED_STATES)}


def wrapTimerValue(progress):
    timeLeft = progress.getCountDown()
    if progress.getTimeLeft() is not None:
        timeLeft = progress.getTimeLeft()
    return _wrapTimerValue(timeLeft)


def _formatValue(value):
    return backport.getNiceNumberFormat(value)


def _wrapSimpleValue(title, value):
    return {b'title': title, 
       b'value': value, 
       b'mType': (METRICS_TYPES.SIMPLE_VALUE)}


def _wrapRangeVehiclesValue(goal, counter, currentGoal):
    vehTypes = [
     QUESTSPROGRESS.QP_DOT]
    doneTargets = []
    totalValue = 0
    for vType, vCount in counter.iteritems():
        if vCount:
            totalValue += min(vCount, currentGoal)
            doneTargets.append(vType)

    if doneTargets:
        vehTypes = [QUESTSPROGRESS.getQPOrangeVehicleType(vehType) for vehType in doneTargets]
    all = []
    for vehType in VEHICLE_TYPES_ORDER:
        all.append({b'mType': (METRICS_TYPES.VEHICLES_RANGE_VALUE), 
           b'value': (_formatValue(totalValue)), 
           b'goal': (_formatValue(goal)), 
           b'vehicleTypes': vehTypes, 
           b'vehType': (QUESTSPROGRESS.getQPOrangeVehicleType(vehType)), 
           b'currentGoal': (_formatValue(currentGoal)), 
           b'currentValue': (_formatValue(min(counter.get(vehType, 0), currentGoal)))})

    return all


def _wrapVehiclesValue(title, current, targets):
    vehTypes = [
     QUESTSPROGRESS.QP_DOT]
    if targets:
        vehTypes = [QUESTSPROGRESS.getQPOrangeVehicleType(vehType) for vehType in targets]
    return {b'title': title, 
       b'value': (_formatValue(current)), 
       b'vehicleTypes': vehTypes, 
       b'mType': (METRICS_TYPES.VEHICLES_VALUE)}


def _wrapTimerValue(timeLeft):
    if timeLeft <= 1:
        status = QUEST_PROGRESS_BASE.QP_TIMER_STATE_WAS_COMPLETED
    elif timeLeft < ONE_MINUTE / 2:
        status = QUEST_PROGRESS_BASE.QP_TIMER_STATE_CRITICAL
    elif timeLeft < ONE_MINUTE:
        status = QUEST_PROGRESS_BASE.QP_TIMER_STATE_WARNING
    else:
        status = QUEST_PROGRESS_BASE.QP_TIMER_STATE_NORMAL
    minutes, seconds = divmod(int(timeLeft), 60)
    return {b'mType': (QUEST_PROGRESS_BASE.QP_METRIC_TYPE_TIMER), 
       b'time': ((b'{:02d}:{:02d}').format(minutes, seconds)), 
       b'title': (QUESTS.METRICS_TITLE_LEFT), 
       b'status': status}
