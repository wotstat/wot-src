import logging, typing, constants
from helpers import time_utils
from uilogging.core.common import getClientBuildVersion, convertEnum
from uilogging.constants import LogLevels, DEFAULT_LOGGER_NAME
if typing.TYPE_CHECKING:
    from uilogging.types import FeatureType, GroupType, ActionType, LogLevelType
_logger = logging.getLogger(DEFAULT_LOGGER_NAME)

class LogRecord(object):
    __slots__ = (b'_properties',)

    def __init__(self, feature, group, action, level, params):
        params = {k: convertEnum(v) for k, v in dict(params).iteritems()}
        _time = time_utils.getServerUTCTime()
        properties = {b'client_version': (getClientBuildVersion()), 
           b'key': (convertEnum(group)), 
           b'loglevel': (int(convertEnum(level))), 
           b'time_spent': (params.pop(b'timeSpent', 0)), 
           b'action': (convertEnum(action)), 
           b'realm': (constants.CURRENT_REALM), 
           b'feature': (convertEnum(feature)), 
           b'time': (int(_time) if params.pop(b'__intTime__', False) else _time), 
           b'partner_id': (params.pop(b'partnerID', None))}
        duplicates = set(properties) & set(params)
        if duplicates:
            _logger.error(b'Reserved keys: %s in additional log params.', duplicates)
            self._properties = {}
        else:
            properties.update(params)
            self._properties = properties
        return

    @property
    def feature(self):
        return self._properties.get(b'feature', b'')

    @property
    def group(self):
        return self._properties.get(b'key', b'')

    @property
    def action(self):
        return self._properties.get(b'action', b'')

    @property
    def level(self):
        return self._properties.get(b'loglevel', LogLevels.NOTSET)

    @property
    def time(self):
        return self._properties.get(b'time', 0)

    @property
    def partnerID(self):
        return self._properties.get(b'partner_id', None)

    @property
    def broken(self):
        if self.feature and self.group and self.action:
            return False
        return True

    def toDict(self):
        return dict(self._properties)

    def __str__(self):
        return (b'<Log: {}, {}, {}, {}, {}>').format(self.feature, self.group, self.action, self.level, self.time)

    def __repr__(self):
        return self.__str__()

    def __len__(self):
        return len(self._properties)
