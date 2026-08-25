from Event import EventManager, Event
from skeletons.helpers.platform import IPublishPlatform

class BasePublishPlatform(IPublishPlatform):
    __slots__ = (b'__eventMgr', b'onPayment', b'onOverlay')

    def __init__(self):
        super(BasePublishPlatform, self).__init__()
        self.__eventMgr = EventManager()
        self.onPayment = Event(self.__eventMgr)
        self.onOverlay = Event(self.__eventMgr)
        return

    def init(self):
        return

    def fini(self):
        self.__eventMgr.clear()
        return

    def isInited(self):
        return False

    def isConnected(self):
        return False
