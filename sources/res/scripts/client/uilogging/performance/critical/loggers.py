import BigWorld, logging
from uilogging.base.logger import _BaseLogger as Logger
from uilogging.constants import DEFAULT_LOGGER_NAME
from uilogging.performance.critical.constants import Features, Groups, LogActions
from uilogging.helpers import getClientSessionID
from wotdecorators import noexcept
_logger = logging.getLogger(DEFAULT_LOGGER_NAME)

class MemoryCriticalLogger(Logger):
    __slots__ = ()

    def __init__(self):
        super(MemoryCriticalLogger, self).__init__(Features.MEMORY_CRITICAL, Groups.EVENT)
        return

    def initialize(self):
        self.ensureSession()
        return

    @noexcept
    def log(self, sessionStartedAt=0):
        _logger.debug(b'Critical memory metrics requested.')
        if not self.disabled or BigWorld.wg_debugLogging():
            data = BigWorld.collectLastMemoryCriticalEvent()
        if self.disabled:
            return
        self.ensureSession()
        sessionID = getClientSessionID()
        if data:
            self._logImmediately(LogActions.MEMORY_CRITICAL_EVENT, session_id=sessionID, started_at=sessionStartedAt, **data)
        else:
            _logger.error(b'Memory critical metrics are empty')
        return
