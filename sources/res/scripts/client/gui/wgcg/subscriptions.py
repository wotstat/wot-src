from gui.clans.interfaces import IClanListener
from gui.shared.utils.listeners_collection import ListenersCollection

class WebListeners(ListenersCollection):

    def __init__(self):
        super(WebListeners, self).__init__()
        self._setListenerClass(IClanListener)
        return

    def notify(self, eventType, *args):
        self._invokeListeners(eventType, *args)
        return

    def addListener(self, listener):
        if not self.hasListener(listener):
            super(WebListeners, self).addListener(listener)
        return

    def getListenersIterator(self):
        return list(super(WebListeners, self).getListenersIterator())
