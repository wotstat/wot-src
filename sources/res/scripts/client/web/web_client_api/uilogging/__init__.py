from helpers import dependency
from skeletons.ui_logging import IUILoggingCore
from uilogging.constants import LogLevels
from web.web_client_api import w2c, w2capi, W2CSchema, Field

class _UILoggingLogSchema(W2CSchema):
    feature = Field(required=True, type=basestring)
    group = Field(required=True, type=basestring)
    log_action = Field(required=True, type=basestring)
    log_level = Field(required=False, type=int, default=LogLevels.INFO)
    params = Field(required=False, type=dict, default={})


@w2capi(name=b'ui_logging', key=b'action')
class UILoggingWebApi(object):
    _logger = dependency.descriptor(IUILoggingCore)

    @w2c(_UILoggingLogSchema, b'log')
    def log(self, cmd):
        self._logger.log(feature=cmd.feature, group=cmd.group, action=cmd.log_action, loglevel=cmd.log_level, **cmd.params)
        return
