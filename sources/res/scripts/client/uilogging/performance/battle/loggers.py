import BigWorld, logging, typing
from helpers import dependency
from skeletons.helpers.statistics import IStatisticsCollector
from uilogging.base.logger import _BaseLogger as Logger
from uilogging.constants import DEFAULT_LOGGER_NAME
from uilogging.performance.battle.constants import Features, Groups, LogActions
from uilogging.helpers import getClientSessionID
from wotdecorators import noexcept
if typing.TYPE_CHECKING:
    from uilogging.types import GroupType, PartnerIdType
_logger = logging.getLogger(DEFAULT_LOGGER_NAME)

class _BaseBattleMetricsLogger(Logger):
    __slots__ = ()

    def __init__(self, group):
        super(_BaseBattleMetricsLogger, self).__init__(Features.METRICS, group)
        return

    @noexcept
    def log(self, data, partnerID=None, sessionID=b''):
        if not isinstance(data, dict):
            _logger.error(b'Wrong metrics data type: [dict != %s].', type(data))
            return
        if data:
            super(_BaseBattleMetricsLogger, self)._log(LogActions.SPACE_DONE, partnerID=partnerID, session_id=sessionID, **data)
        else:
            _logger.error(b'%s stats are empty.', self._feature)
        return


class _ClientSessionLogger(_BaseBattleMetricsLogger):
    __slots__ = ()

    def __init__(self):
        super(_ClientSessionLogger, self).__init__(Groups.SESSION)
        return


class _ClientSystemLogger(_BaseBattleMetricsLogger):
    __slots__ = ()

    def __init__(self):
        super(_ClientSystemLogger, self).__init__(Groups.SYSTEM)
        return


class BattleMetricsLogger(object):
    __slots__ = (b'_loggers', b'_defaultLogger')
    statsCollector = dependency.descriptor(IStatisticsCollector)

    def __init__(self):
        self._loggers = {(Groups.SESSION.value): (_ClientSessionLogger()), 
           (Groups.SYSTEM.value): (_ClientSystemLogger())}
        self._defaultLogger = self._loggers[Groups.SYSTEM.value]
        return

    def initialize(self):
        self._defaultLogger.ensureSession()
        return

    @noexcept
    def log(self):
        _logger.debug(b'Battle metrics requested.')
        if not self._defaultLogger.disabled or BigWorld.wg_debugLogging():
            data = self.statsCollector.getStatistics()
        if self._defaultLogger.disabled:
            return
        if not data:
            _logger.error(b'Battle stats are empty.')
            return
        diff = set(data) ^ set(self._loggers)
        if diff:
            _logger.error(b'Difference in loggers and received metrics groups: %s.', diff)
            return
        clientSessionID = getClientSessionID()
        for group, stats in data.iteritems():
            if stats:
                self._loggers[group].log(stats, sessionID=clientSessionID)

        return
