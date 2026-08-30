from __future__ import absolute_import
import logging
from future.utils import iteritems
import BigWorld
from PlayerEvents import g_playerEvents
from shared_utils import nextTick
from vehicle_systems.stricted_loading import makeCallbackWeak
_logger = logging.getLogger(__name__)

class DynamicScriptComponent(BigWorld.DynamicScriptComponent):

    def __init__(self, *_, **__):
        BigWorld.DynamicScriptComponent.__init__(self)
        if self._isAvatarReady:
            nextTick(makeCallbackWeak(self.__onAvatarReady))()
        else:
            g_playerEvents.onAvatarReady += self.__onAvatarReady
        _logger.debug(b'%s.__init__. EntityID=%s', self.__class__.__name__, self.entity.id)
        return

    @property
    def _isAvatarReady(self):
        return BigWorld.player().userSeesWorld()

    def onDestroy(self):
        _logger.debug(b'%s.onDestroy. EntityID=%s', self.__class__.__name__, self.entity.id)
        g_playerEvents.onAvatarReady -= self.__onAvatarReady
        return

    def onLeaveWorld(self):
        self.onDestroy()
        return

    @property
    def spaceID(self):
        return self.entity.spaceID

    @property
    def keyName(self):
        return next(name for name, value in iteritems(self.entity.dynamicComponents) if value == self)

    def _onAvatarReady(self):
        return

    def __onAvatarReady(self):
        g_playerEvents.onAvatarReady -= self.__onAvatarReady
        if self._isValid:
            self._onAvatarReady()
        return

    @property
    def _isValid(self):
        return not self.entity.isDestroyed and self in self.entity.dynamicComponents.values()
