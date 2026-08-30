from __future__ import absolute_import
import logging, BigWorld, Avatar
from PlayerEvents import g_playerEvents
from helpers import dependency, isPlayerAvatar
from shared_utils import nextTick
from skeletons.gui.battle_session import IBattleSessionProvider
_logger = logging.getLogger(__name__)

class ScriptComponent(BigWorld.StaticScriptComponent):
    __sessionProvider = dependency.descriptor(IBattleSessionProvider)
    REQUIRED_BONUS_CAP = None

    def __init__(self):
        BigWorld.StaticScriptComponent.__init__(self)
        if not self.__checkBonusCaps():
            return
        if self._isAvatarReady:
            nextTick(self._onAvatarReady)()
        else:
            g_playerEvents.onAvatarReady += self.__onAvatarReady
        return

    @property
    def _isAvatarReady(self):
        return isPlayerAvatar() and BigWorld.player().userSeesWorld()

    def onEnterWorld(self, _):
        _logger.debug(b'%s.onEnterWorld. EntityID=%s', self.__class__.__name__, self.entity.id)
        return

    def onLeaveWorld(self):
        _logger.debug(b'%s.onLeaveWorld. EntityID=%s', self.__class__.__name__, self.entity.id)
        return

    def _onAvatarReady(self):
        return

    def __onAvatarReady(self):
        g_playerEvents.onAvatarReady -= self.__onAvatarReady
        self._onAvatarReady()
        return

    def __checkBonusCaps(self):
        if self.REQUIRED_BONUS_CAP is None:
            return True
        else:
            if isinstance(self.entity, Avatar.PlayerAvatar):
                capsChecker = self.entity.hasBonusCap
            else:
                capsChecker = self.__sessionProvider.arenaVisitor.bonus.hasBonusCap
            return capsChecker(self.REQUIRED_BONUS_CAP)
