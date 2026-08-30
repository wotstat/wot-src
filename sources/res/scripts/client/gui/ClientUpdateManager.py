import inspect
from gui.shared.money import Currency

class _ClientUpdateManager(object):
    EVENT_TYPE_DELIMITER = b'.'

    def __init__(self):
        self.__handlers = dict()
        self.__removedHandlers = set()
        return

    def update(self, diff):
        self.__clearRemoved()
        for handler, diffpaths in self.__handlers.items():
            if handler in self.__removedHandlers:
                continue
            for diffpath in list(diffpaths):
                isFire, args = self.__processPath(diffpath, diff)
                if isFire:
                    handler(args)
                    break

        return

    def addCallback(self, diffpath, handler):
        self.__subscribeHandler(handler, diffpath)
        return

    def addCallbacks(self, map_of_handlers):
        for diffpath, handler in map_of_handlers.iteritems():
            self.__subscribeHandler(handler, diffpath)

        return

    def addCurrencyCallback(self, currency, handler):
        self.__subscribeHandler(handler, (b'stats.{}').format(currency))
        return

    def addMoneyCallback(self, handler):
        for c in Currency.ALL:
            self.addCurrencyCallback(c, handler)

        return

    def removeCallback(self, diffpath, handler):
        self.__unsubscribeHandler(handler, diffpath)
        return

    def removeCurrencyCallback(self, currency, handler):
        self.__unsubscribeHandler(handler, (b'stats.{}').format(currency))
        return

    def removeObjectCallbacks(self, obj_instance, force=False):
        removed = set(key for key in self.__handlers.iterkeys() if inspect.ismethod(key) and key.__self__ is obj_instance)
        if force:
            for item in removed:
                del self.__handlers[item]

            self.__removedHandlers -= removed
        else:
            self.__removedHandlers |= removed
        return

    def __subscribeHandler(self, handler, diffpath):
        self.__clearRemoved()
        if handler not in self.__handlers:
            self.__handlers[handler] = []
        if diffpath not in self.__handlers[handler]:
            self.__handlers[handler].append(diffpath)
        return

    def __unsubscribeHandler(self, handler, diffpath):
        if handler in self.__handlers:
            if diffpath in self.__handlers[handler]:
                self.__handlers[handler].remove(diffpath)
            if not self.__handlers[handler]:
                del self.__handlers[handler]
        return

    def __processPath(self, diffpath, diff):
        diff_ptr = diff
        if diffpath == b'':
            return (True, diff_ptr)
        else:
            for key in diffpath.split(self.EVENT_TYPE_DELIMITER):
                key = (key[:-2], b'_r') if key.endswith(b'_r') else key if not key.isdigit() else int(key)
                if not isinstance(diff_ptr, dict) or key not in diff_ptr:
                    return (False, None)
                diff_ptr = diff_ptr[key]

            return (
             True, diff_ptr)

    def __clearRemoved(self):
        if not self.__removedHandlers:
            return
        for item in self.__removedHandlers:
            del self.__handlers[item]

        self.__removedHandlers = set()
        return


g_clientUpdateManager = _ClientUpdateManager()
