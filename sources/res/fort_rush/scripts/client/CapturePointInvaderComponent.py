from __future__ import absolute_import
import logging
from gui.shared import g_eventBus, EVENT_BUS_SCOPE
from fort_rush.gui.shared.events import CaptureInvaderEvent
from script_component.DynamicScriptComponent import DynamicScriptComponent
_logger = logging.getLogger(__name__)

class CapturePointInvaderComponent(DynamicScriptComponent):

    def _onAvatarReady(self):
        vehicleID = self.entity.id
        baseName = (self.capturablePointName or b'').upper()
        _logger.debug(b'[FORT_RUSH][INVADER] added vehicleID=%s base=%s', vehicleID, baseName)
        g_eventBus.handleEvent(CaptureInvaderEvent(CaptureInvaderEvent.INVADER_ADDED, vehicleID, baseName), EVENT_BUS_SCOPE.BATTLE)
        return

    def onDestroy(self):
        vehicleID = self.entity.id
        baseName = (self.capturablePointName or b'').upper()
        _logger.debug(b'[FORT_RUSH][INVADER] removed vehicleID=%s base=%s', vehicleID, baseName)
        g_eventBus.handleEvent(CaptureInvaderEvent(CaptureInvaderEvent.INVADER_REMOVED, vehicleID, baseName), EVENT_BUS_SCOPE.BATTLE)
        super(CapturePointInvaderComponent, self).onDestroy()
        return
