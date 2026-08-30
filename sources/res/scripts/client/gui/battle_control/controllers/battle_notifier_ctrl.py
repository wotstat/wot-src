from __future__ import absolute_import
import logging
from PlayerEvents import g_playerEvents
from gui.battle_control.battle_constants import BATTLE_CTRL_ID
from gui.battle_control.view_components import ViewComponentsController
from helpers import dependency
from messenger.proto.events import g_messengerEvents
from skeletons.gui.battle_session import IBattleSessionProvider
_logger = logging.getLogger(__name__)

class IBattleNotifierListener(object):

    def resultsNotificationReceived(self, results):
        return


class BattleNotifierController(ViewComponentsController):
    __slots__ = (b'__weakref__', b'__enabled')
    sessionProvider = dependency.descriptor(IBattleSessionProvider)

    def __init__(self, setup):
        super(BattleNotifierController, self).__init__()
        self.__enabled = False
        return

    def getControllerID(self):
        return BATTLE_CTRL_ID.BATTLE_NOTIFIER

    def startControl(self):
        _logger.debug(b'[BattleNotifierController PY] __startControl!')
        channel = g_messengerEvents.serviceChannel
        channel.onChatMessageReceived += self.__onChatMessage
        g_playerEvents.onRoundFinished += self.__onRoundFinished
        self.__enabled = True
        return

    def stopControl(self):
        channel = g_messengerEvents.serviceChannel
        channel.onChatMessageReceived -= self.__onChatMessage
        g_playerEvents.onRoundFinished -= self.__onRoundFinished
        return

    def __onRoundFinished(self, winningTeam, reason):
        self.__enabled = False
        return

    def __onChatMessage(self, clientID, message):
        if message.type == 2 and self.__enabled:
            for component in self._viewComponents:
                component.resultsNotificationReceived(message)

        return


def createBattleNotifierController(setup):
    return BattleNotifierController(setup)
