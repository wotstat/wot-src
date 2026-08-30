from __future__ import absolute_import
import BigWorld
from PlayerEvents import g_playerEvents
from debug_utils import LOG_DEBUG

class PlayerLogin(BigWorld.Entity):

    def __init__(self):
        return

    def onBecomePlayer(self):
        return

    def onBecomeNonPlayer(self):
        return

    def onKickedFromServer(self, checkoutPeripheryID):
        LOG_DEBUG(b'onKickedFromServer', checkoutPeripheryID)
        g_playerEvents.onKickWhileLoginReceived(checkoutPeripheryID)
        return

    def receiveLoginQueueNumber(self, queueNumber):
        LOG_DEBUG(b'receiveLoginQueueNumber', queueNumber)
        g_playerEvents.onLoginQueueNumberReceived(queueNumber)
        return

    def handleKeyEvent(self, event):
        return False

    def setPeripheryRoutingGroup(self, peripheryRoutingGroup, availableHosts):
        g_playerEvents.onPeripheryRoutingGroupReceived(peripheryRoutingGroup, availableHosts)
        return


Login = PlayerLogin
