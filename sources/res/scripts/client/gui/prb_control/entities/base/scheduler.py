import weakref
from gui.shared.utils.scheduled_notifications import Notifiable

class BaseScheduler(Notifiable):

    def __init__(self, entity):
        super(BaseScheduler, self).__init__()
        self._entity = weakref.proxy(entity)
        return

    def init(self):
        return

    def fini(self):
        return
