from __future__ import absolute_import
import json, logging
from typing import TYPE_CHECKING, NamedTuple, Tuple
from uilogging.base.logger import MetricsLogger
from uilogging.prebattle_highlights.constants import FEATURE, PrebattleHighlightsLogAction, PrebattleHighlightsLogKeys
if TYPE_CHECKING:
    from typing import Dict, Any, Optional
_logger = logging.getLogger(__name__)
PBHViewingLogInfo = NamedTuple(b'PBHViewingLogInfo', [
 (
  b'sequence_layer', Tuple[str, int]),
 (
  b'historical_level', int),
 (
  b'was_historical_compliance', bool)])

class PrebattleHighlightsEventLogger(MetricsLogger):

    def __init__(self):
        super(PrebattleHighlightsEventLogger, self).__init__(FEATURE)
        self.__viewingLogInfo = None
        return

    def reset(self):
        self.__viewingLogInfo = None
        super(PrebattleHighlightsEventLogger, self).reset()
        return

    def logStartViewingAction(self, info):
        if self.__viewingLogInfo is not None:
            _logger.debug(b'Log info is already stored and will be rewrote. Current: %s; New: %s', self.__viewingLogInfo, info)
        self.__viewingLogInfo = info
        self.startAction(PrebattleHighlightsLogAction.VIEWED)
        return

    def logStopViewingAction(self, viewStatus):
        if self.__viewingLogInfo is None:
            _logger.debug(b'Log info not found.')
            return
        else:
            layerName, layerDuration = self.__viewingLogInfo.sequence_layer
            infoStr = json.dumps({b'view_status': (viewStatus.value), 
               b'sequence_type': layerName, 
               b'sequence_duration': (int(layerDuration)), 
               b'historical_level': (self.__viewingLogInfo.historical_level), 
               b'was_historical_warning_shown': (self.__viewingLogInfo.was_historical_compliance)})
            self.__viewingLogInfo = None
            self.stopAction(PrebattleHighlightsLogAction.VIEWED, PrebattleHighlightsLogKeys.PBH, info=infoStr)
            return

    def logSkipViewingEvent(self, info):
        infoStr = json.dumps(info)
        self._log(PrebattleHighlightsLogAction.VIEWED, item=PrebattleHighlightsLogKeys.PBH, parent_screen=None, item_state=None, additional_info=infoStr, partnerID=None, timeSpent=0.0)
        return

    def logUnfocusClientEvent(self):
        self.logOnce(PrebattleHighlightsLogAction.COLLAPSE, PrebattleHighlightsLogKeys.PBH_OUT_OF_FOCUS)
        return
