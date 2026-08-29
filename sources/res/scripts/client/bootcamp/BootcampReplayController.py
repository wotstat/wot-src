from debug_utils_bootcamp import LOG_DEBUG_DEV_BOOTCAMP
import BattleReplay
BOOTCAMP_REPLAY_EVENTS = (b'bootcampMarkers_onTriggerActivated', b'bootcampMarkers_onTriggerDeactivated', b'bootcampMarkers_showMarker', b'bootcampMarkers_hideMarker', b'bootcampHint_show', b'bootcampHint_hide', b'bootcampHint_complete', b'bootcampHint_close', b'bootcampHint_onHided')

class BootcampReplayControllerQueue:

    def __init__(self, name):
        self.__name = name
        self.__data = []
        self.__callback = None
        return

    def init(self):
        BattleReplay.g_replayCtrl.setDataCallback(self.__name, self.replayCallbackeMethod)
        return

    def fini(self):
        BattleReplay.g_replayCtrl.delDataCallback(self.__name, self.replayCallbackeMethod)
        self.__callback = None
        return

    def replayCallbackeMethod(self, binData):
        if self.__callback is not None:
            return self.__callback(binData)
        else:
            self.__data.append(binData)
            return

    def setDataCallback(self, callback):
        self.__callback = callback
        for binData in self.__data:
            callback(binData)

        self.__data = []
        return

    def delDataCallback(self, callback):
        if callback is not self.__callback:
            LOG_DEBUG_DEV_BOOTCAMP(b'Multiple callback unsubscribe:', self.__name)
            return
        else:
            self.__callback = None
            return


class BootcampReplayController:

    def __init__(self):
        self.__queues = {}
        for name in BOOTCAMP_REPLAY_EVENTS:
            self.__queues[name] = BootcampReplayControllerQueue(name)

        return

    def init(self):
        for quque in self.__queues.itervalues():
            quque.init()

        return

    def fini(self):
        for quque in self.__queues.itervalues():
            quque.fini()

        return

    def setDataCallback(self, eventName, callback):
        if eventName not in self.__queues:
            LOG_DEBUG_DEV_BOOTCAMP(b'Failed to set replay data callback:', eventName)
            return
        queue = self.__queues[eventName]
        queue.setDataCallback(callback)
        return

    def delDataCallback(self, eventName, callback):
        if eventName not in self.__queues:
            LOG_DEBUG_DEV_BOOTCAMP(b'Failed to del replay data callback:', eventName)
            return
        queue = self.__queues[eventName]
        queue.delDataCallback(callback)
        return
