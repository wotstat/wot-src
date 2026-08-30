from __future__ import absolute_import
import typing, time, logging
from contextlib import contextmanager
LOGGER_NAME = b'PersistentDataCache'
DEFAULT_SAVING_TIMEOUT = 120.0

def getLogger(*names):
    return logging.getLogger((b'{}').format((b'.').join((LOGGER_NAME,) + names)))


_logger = getLogger(b'Metrics')

class MeasureExecutionTime(object):
    __slots__ = (b'_logger', b'_metricName', b'_totalTime')

    def __init__(self, metricName, logger=None):
        self._logger = logger or _logger
        self._metricName = metricName
        self._totalTime = 0.0
        return

    def printTotalTime(self, reset=True):
        self._logger.debug(b'%s total time: %s', self._createMetricName(), self._totalTime)
        if reset:
            self._totalTime = 0.0
        return

    @contextmanager
    def start(self, section=b''):
        startTime = time.time()
        try:
            yield
        finally:
            endTime = time.time() - startTime
            self._totalTime += endTime
            self._logger.debug(b'%s executed in %s seconds.', self._createMetricName(section), endTime)

        return

    def _createMetricName(self, section=b''):
        if section:
            return (self._metricName, section)
        return (self._metricName,)

    def __call__(self, func, section=b''):

        def wrapper(*args, **kwargs):
            startTime = time.time()
            result = func(*args, **kwargs)
            endTime = time.time() - startTime
            self._totalTime += endTime
            self._logger.debug(b'%s executed in %s seconds.', self._createMetricName(section), endTime)
            return result

        return wrapper
