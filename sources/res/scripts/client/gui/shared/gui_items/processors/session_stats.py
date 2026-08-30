from __future__ import absolute_import
import logging, BigWorld
from gui.shared.gui_items.processors import Processor, makeI18nError
_logger = logging.getLogger(__name__)

class ResetSessionStatsProcessor(Processor):

    def _errorHandler(self, code, errStr=b'', ctx=None):
        defaultKey = b'session_stats/reset/server_error'
        return makeI18nError((b'/').join((defaultKey, errStr)), defaultKey)

    def _request(self, callback):
        _logger.debug(b'Make server request to reset session stats')
        BigWorld.player().sessionStats.resetStats((lambda code, errStr, ext: self._response(code, callback, ctx=ext, errStr=errStr)))
        return
