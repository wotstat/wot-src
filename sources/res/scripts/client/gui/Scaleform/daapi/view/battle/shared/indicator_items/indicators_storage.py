import logging, Event
_logger = logging.getLogger(__name__)

class IndicatorsStorage(object):
    __slots__ = (b'__storage', b'onNewItem')

    def __init__(self):
        super(IndicatorsStorage, self).__init__()
        self.__storage = dict()
        self.onNewItem = Event.Event()
        return

    def get(self, name):
        return self.__storage.get(name, None)

    def add(self, name, indicatorMeta):
        if name in self.__storage:
            _logger.error(b'trying to add indicator meta(%s) multiple times', name)
            return
        self.__storage[name] = indicatorMeta
        self.onNewItem(name, indicatorMeta)
        return

    def pop(self, name):
        self.__storage.pop(name, None)
        return


g_indicatorsStorage = IndicatorsStorage()
