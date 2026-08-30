from __future__ import absolute_import
from builtins import map
from collections import namedtuple
from future.utils import lfilter, lmap
import BigWorld, Event
from PlayerEvents import g_playerEvents
from helpers import getLocalizedData
from skeletons.gui.game_control import IEventsNotificationsController

class EventsNotificationsController(IEventsNotificationsController):

    def __init__(self):
        super(EventsNotificationsController, self).__init__()
        self.__eventMgr = Event.EventManager()
        self.onEventNotificationsChanged = Event.Event(self.__eventMgr)
        return

    def fini(self):
        self.__stop()
        self.__eventMgr = None
        super(EventsNotificationsController, self).fini()
        return

    def onLobbyInited(self, event):
        g_playerEvents.onEventNotificationsChanged += self.__onEventNotification
        return

    def onAvatarBecomePlayer(self):
        self.__stop()
        return

    def onDisconnected(self):
        self.__stop()
        return

    def getEventsNotifications(self, filterFunc=None):
        player = BigWorld.player()
        if player:
            return lfilter(filterFunc or (lambda a: True), map(EventNotification.make, player.eventNotifications))
        return ()

    def __stop(self):
        self.__eventMgr.clear()
        g_playerEvents.onEventNotificationsChanged -= self.__onEventNotification
        return

    def __onEventNotification(self, diff):
        added = lmap(EventNotification.make, diff.get(b'added', ()))
        removed = lmap(EventNotification.make, diff.get(b'removed', ()))
        self.onEventNotificationsChanged(added, removed)
        return


class EventNotification(namedtuple(b'EventNotification', b'eventType data text')):

    @classmethod
    def default(cls):
        return cls.__new__(cls, None, None, None)

    @classmethod
    def make(cls, data):
        text = getLocalizedData(data, b'text')
        return cls.__new__(cls, data[b'type'], data.get(b'data'), text)
