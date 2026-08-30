from collections import defaultdict
import BigWorld
from bootcamp.Bootcamp import g_bootcamp
from helpers import dependency
from skeletons.gui.game_control import IBootcampController
from uilogging.base.logger import ifUILoggingEnabled
from uilogging.constants import LogLevels
from uilogging.deprecated.base.loggers import CommonLogger
from uilogging.deprecated.bootcamp.validators import TimeValidator
from uilogging.deprecated.logging_constants import FEATURES
from uilogging.deprecated.base.loggers import BaseLogger
from uilogging.deprecated.bootcamp.constants import ACTIONS_HINTS_TO_LOG_ONCE, ACTION_SEQUENCES
from wotdecorators import noexcept
__all__ = (b'BootcampUILogger', b'BootcampLogger')

class LoggingCacheMeta(type):
    _instance = None

    def __call__(cls):
        if cls._instance is None:
            cls._instance = super(LoggingCacheMeta, cls).__call__()
        return cls._instance


class LoggingCache(object):
    __metaclass__ = LoggingCacheMeta

    def __init__(self):
        self._data = defaultdict(set)
        return

    def __contains__(self, key):
        return key in self.data

    def add(self, key):
        self.data.add(key)
        return

    @property
    def data(self):
        return self._data[g_bootcamp.getLessonNum()]


class BootcampUILogger(BaseLogger):
    _validator = TimeValidator
    _feature = FEATURES.BOOTCAMP

    def __init__(self, *args, **kwargs):
        super(BootcampUILogger, self).__init__(*args, **kwargs)
        self._populateTime = None
        self._loggingCache = None
        return

    def _updateFromContext(self, data):
        contextKeyMapping = {b'is_newbie': b'isNewbie', 
           b'lesson_id': b'lessonNum'}
        context = g_bootcamp.getContext()
        for key, contextKey in contextKeyMapping.items():
            data[key] = context.get(contextKey, None)

        return

    def initLogger(self):
        super(BootcampUILogger, self).initLogger()
        self._populateTime = int(BigWorld.time())
        self._loggingCache = LoggingCache()
        return

    def getActionFromSequence(self, action):
        actionToLog, finalAction = ACTION_SEQUENCES[action]
        if actionToLog in self._loggingCache:
            actionToLog = finalAction
        if actionToLog in self._loggingCache:
            return None
        else:
            return actionToLog

    def logStatistic(self, resetTime=True, action=None, logOnce=False, restrictions=None, validate=True, **kwargs):
        if not self.ready:
            return
        else:
            if (logOnce or action in ACTIONS_HINTS_TO_LOG_ONCE) and action in self._loggingCache:
                return
            currentTimestamp = int(BigWorld.time())
            timeDelta = currentTimestamp - self._populateTime
            if self._validator and not self._validator.isValid(self._logKey, timeDelta, validate):
                return
            if action in ACTION_SEQUENCES:
                action = self.getActionFromSequence(action)
                if not action:
                    return
            data = {b'timeSpent': timeDelta, b'is_newbie': (self._isNewbie), 
               b'lesson_id': None}
            self._updateFromContext(data)
            if restrictions:
                for targetField, targetValue in restrictions.iteritems():
                    if callable(targetValue):
                        if not targetValue(data.get(targetField)):
                            return
                    elif data.get(targetField) != targetValue:
                        return

            self.sendLogData(action, **data)
            self._loggingCache.add(action)
            self._resetTime(resetTime)
            return


class BootcampLogger(CommonLogger):
    __slots__ = ()
    __bootcamp = dependency.descriptor(IBootcampController)

    def __init__(self, group):
        super(BootcampLogger, self).__init__(FEATURES.BOOTCAMP, group)
        return

    @noexcept
    @ifUILoggingEnabled()
    def log(self, action, loglevel=LogLevels.INFO, **params):
        if b'timeSpent' in params:
            params[b'timeSpent'] = int(params[b'timeSpent'])
        params[b'lesson_id'] = g_bootcamp.getLessonNum()
        params[b'is_newbie'] = g_bootcamp.isNewbie()
        return super(BootcampLogger, self).log(action=action, loglevel=loglevel, **params)

    def logOnlyFromBootcamp(self, action, loglevel=LogLevels.INFO, **params):
        if not self.__bootcamp.isInBootcamp():
            return
        self.log(action=action, loglevel=loglevel, **params)
        return
