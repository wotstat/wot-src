import typing
from Event import SuspendedEventManager, SuspendedEvent
from fun_random.gui.shared import g_funEventBus
from fun_random.gui.shared.events import FunEventScope, FunEventType
from skeletons.gui.game_control import IFunRandomController
if typing.TYPE_CHECKING:
    from gui.shared.event_bus import SharedEvent

class FunSubscription(IFunRandomController.IFunSubscription):

    def __init__(self):
        super(FunSubscription, self).__init__()
        self.__em = SuspendedEventManager()
        self.__handleEvent = SuspendedEvent(self.__em)
        self.__handleEvent += g_funEventBus.handleEvent
        return

    def addListener(self, eventType, handler, scope=FunEventScope.DEFAULT):
        g_funEventBus.addListener(eventType, handler, scope)
        return

    def removeListener(self, eventType, handler, scope=FunEventScope.DEFAULT):
        g_funEventBus.removeListener(eventType, handler, scope)
        return

    def handleEvent(self, event, scope=FunEventScope.DEFAULT):
        self.__handleEvent(event, scope)
        return

    def fini(self):
        self.__handleEvent -= g_funEventBus.handleEvent
        self.__em.clear()
        return

    def clear(self):
        g_funEventBus.clear()
        return

    def addSubModesWatcher(self, method, desiredOnly=False, withTicks=False):
        scope = FunEventScope.DESIRABLE if desiredOnly else FunEventScope.DEFAULT
        self.addListener(FunEventType.SUB_SELECTION, method)
        self.addListener(FunEventType.SUB_SETTINGS, method, scope=scope)
        self.addListener(FunEventType.SUB_STATUS_UPDATE, method, scope=scope)
        if withTicks:
            self.addListener(FunEventType.SUB_STATUS_TICK, method, scope=scope)
        return

    def removeSubModesWatcher(self, method, desiredOnly=False, withTicks=False):
        scope = FunEventScope.DESIRABLE if desiredOnly else FunEventScope.DEFAULT
        if withTicks:
            self.removeListener(FunEventType.SUB_STATUS_TICK, method, scope=scope)
        self.removeListener(FunEventType.SUB_STATUS_UPDATE, method, scope=scope)
        self.removeListener(FunEventType.SUB_SETTINGS, method, scope=scope)
        self.removeListener(FunEventType.SUB_SELECTION, method)
        return

    def resume(self):
        self.__em.resume()
        return

    def suspend(self):
        self.__em.suspend()
        return
