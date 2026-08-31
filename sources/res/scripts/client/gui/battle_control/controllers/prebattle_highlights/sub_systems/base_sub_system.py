from __future__ import absolute_import

class BasePbhSubSystem(object):

    def __init__(self, readyCallback):
        self._readyCallback = readyCallback
        return

    def subscribe(self):
        raise NotImplementedError
        return

    def unsubscribe(self):
        raise NotImplementedError
        return

    def isReady(self):
        raise NotImplementedError
        return

    def startFlow(self):
        raise NotImplementedError
        return

    def stopFlow(self):
        raise NotImplementedError
        return

    def clear(self):
        self._readyCallback = None
        return
