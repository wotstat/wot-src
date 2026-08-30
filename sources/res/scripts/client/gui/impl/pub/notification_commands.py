import typing
from frameworks.wulf import WindowStatus
from gui.Scaleform.Waiting import Waiting
from gui.Scaleform.framework.entities.sf_window import SFWindow
from gui.impl.pub.lobby_window import LobbyNotificationWindow
from shared_utils import CONST_CONTAINER
from th_async import th_await, th_async

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


class Priority(CONST_CONTAINER):
    MEDIUM = b'medium'
    HIGH = b'high'


class NotificationCommand(object):
    __slots__ = ()

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

    def getPriority(self):
        raise NotImplementedError
        return


class WindowNotificationCommand(NotificationCommand):
    __slots__ = (b'__window', b'__priority')

    def __init__(self, window, priority=Priority.MEDIUM):
        super(WindowNotificationCommand, self).__init__()
        self.__window = window
        self.__priority = priority
        return

    def __eq__(self, other):
        return self.__window == other

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

    def getPriority(self):
        return self.__priority


class WindowNotificationWithWaitingCommand(NotificationCommand):
    __slots__ = (b'__window', b'__waitingMessage', b'__timeout')

    def __init__(self, window, waitingMessage, timeout):
        super(WindowNotificationWithWaitingCommand, self).__init__()
        self.__window = window
        self.__waitingMessage = waitingMessage
        self.__timeout = timeout
        return

    def __eq__(self, other):
        return self.__window == other

    def init(self):
        return

    def fini(self):
        self.__window.destroy()
        return

    @th_async
    def execute(self):
        Waiting.show(self.__waitingMessage)
        try:
            show = yield th_await(self.__window.waitData(self.__timeout))
        finally:
            Waiting.hide(self.__waitingMessage)

        if show:
            self.__window.load()
        return

    def getWindow(self):
        return self.__window

    def getPriority(self):
        return Priority.MEDIUM


class EventNotificationCommand(NotificationCommand):
    __slots__ = (b'__event',)

    def __init__(self, event):
        super(EventNotificationCommand, self).__init__()
        self.__event = event
        return

    def __eq__(self, other):
        return self.__event == other

    def init(self):
        return

    def fini(self):
        return

    def execute(self):
        self.__event()
        return

    def getWindow(self):
        return

    def getPriority(self):
        return Priority.MEDIUM
