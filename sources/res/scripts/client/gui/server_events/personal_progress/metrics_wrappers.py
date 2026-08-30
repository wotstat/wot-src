import typing
from constants import QUEST_PROGRESS_STATE
from gui.Scaleform.genConsts.QUESTSPROGRESS import QUESTSPROGRESS
from gui.Scaleform.genConsts.QUEST_PROGRESS_BASE import QUEST_PROGRESS_BASE
from gui.Scaleform.locale.QUESTS import QUESTS
from gui.impl import backport
from helpers.time_utils import ONE_MINUTE

class METRICS_TYPES(object):
    SIMPLE = QUEST_PROGRESS_BASE.QP_METRIC_TYPE_SIMPLE
    SIMPLE_VALUE = QUEST_PROGRESS_BASE.QP_METRIC_TYPE_SIMPLE_VALUE
    RANGE_VALUE = QUEST_PROGRESS_BASE.QP_METRIC_TYPE_RANGE
    VEHICLES_VALUE = QUEST_PROGRESS_BASE.QP_METRIC_TYPE_VEHICLES
    TIMER_VALUE = QUEST_PROGRESS_BASE.QP_METRIC_TYPE_TIMER


def wrapSimple(_):
    return {b'mType': (METRICS_TYPES.SIMPLE)}


def wrapRangeValue(progress):
    return {b'title': (QUESTS.METRICS_TITLE_PROGRESS), 
       b'value': (_formatValue(progress.getCurrent())), 
       b'goal': (_formatValue(progress.getGoal())), 
       b'mType': (METRICS_TYPES.RANGE_VALUE)}


def wrapCurrentValue(progress):
    return _wrapSimpleValue(QUESTS.METRICS_TITLE_PROGRESS, _formatValue(progress.getCurrent()))


def wrapVehiclesValue(progress):
    return _wrapVehiclesValue(QUESTS.METRICS_TITLE_DONE, progress.getCurrent(), progress.getDoneTargets())


def wrapLimiterValue(progress):
    limiterProgress = progress.getLimiter()
    return {b'mType': (QUEST_PROGRESS_BASE.QP_METRIC_TYPE_LIMITER), 
       b'value': (_formatValue(limiterProgress.getRest())), 
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
