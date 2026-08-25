from __future__ import absolute_import
import typing
from frameworks.wulf import WindowStatus
from gui.Scaleform.framework.entities.sf_window import SFWindow
from gui.impl.pub.lobby_window import LobbyNotificationWindow
if typing.TYPE_CHECKING:
    from typing import Any

class NotificationEvent(object):
    __slots__ = (b'_args', b'_kwargs', b'_method')

    def __init__(self, method, *args, **kwargs):
        self._method = method
        self._args = args
        self._kwargs = kwargs
        return

    def __call__(self):
        self._method(*self._args, **self._kwargs)
        return

    def isEventSet(self):
        return self._method is not None and callable(self._method)


class NotificationCommand(object):
    __slots__ = ()
    __hash__ = None
    isPersistent = True

    def __eq__(self, other):
        return False

    def init(self):
        raise NotImplementedError
        return

    def fini(self):
        raise NotImplementedError
        return

    def execute(self):
        raise NotImplementedError
        return

    def getWindow(self):
        raise NotImplementedError
        return


class WindowNotificationCommand(NotificationCommand):
    __slots__ = (b'__window',)
    __hash__ = None

    def __init__(self, window):
        super(WindowNotificationCommand, self).__init__()
        self.__window = window
        return

    def __eq__(self, other):
        if not isinstance(other, WindowNotificationCommand):
            return False
        return self.__window == other.getWindow()

    def init(self):
        return

    def fini(self):
        self.__window.destroy()
        return

    def execute(self):
        self.__window.load()
        return

    def getWindow(self):
        return self.__window


class EventNotificationCommand(NotificationCommand):
    __slots__ = (b'__event',)
    __hash__ = None

    def __init__(self, event):
        super(EventNotificationCommand, self).__init__()
        self.__event = event
        return

    def __eq__(self, other):
        if not isinstance(other, EventNotificationCommand):
            return False
        return self.__event == other.getEvent()

    def init(self):
        return

    def fini(self):
        return

    def execute(self):
        self.__event()
        return

    def getWindow(self):
        return

    def getEvent(self):
        return self.__event


class NonPersistentEventNotificationCommand(EventNotificationCommand):
    __slots__ = ()
    isPersistent = False
