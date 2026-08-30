import typing
from wotdecorators import singleton

def getCache():
    return GFNotificationsCache


class IGFNotificationsCache(object):
    __slots__ = (b'__data',)

    def setPayload(self, id, payload):
        raise NotImplementedError
        return

    def getPayload(self, id):
        raise NotImplementedError
        return

    def clear(self):
        raise NotImplementedError
        return


@singleton
class GFNotificationsCache(IGFNotificationsCache):

    def __init__(self):
        self.__data = {}
        return

    def setPayload(self, id, payload):
        self.__data[id] = payload
        return

    def getPayload(self, id):
        return self.__data.get(id, {})

    def clear(self):
        self.__data.clear()
        return
