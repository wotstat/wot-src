import BigWorld
from debug_utils_bootcamp import LOG_DEBUG_DEV_BOOTCAMP

class AbstractState(object):

    def __init__(self, stateId):
        super(AbstractState, self).__init__()
        self.__id = stateId
        self.__isActive = False
        return

    def id(self):
        return self.__id

    def handleKeyEvent(self, event):
        return

    def activate(self):
        if self.__isActive:
            LOG_DEBUG_DEV_BOOTCAMP(b'State.activate: state is already active')
            return
        self.__isActive = True
        self._doActivate()
        return

    def deactivate(self):
        if not self.__isActive:
            LOG_DEBUG_DEV_BOOTCAMP(b'State.deactivate: state is already not active')
            return
        self._doDeactivate()
        self.__isActive = False
        return

    def onSpaceLoadCompleted(self):
        BigWorld.player().onSpaceLoaded()
        return

    def onAvatarBecomeNonPlayer(self):
        return

    def onArenaLoadCompleted(self):
        return

    def getIntroVideoData(self):
        return {}

    def _doActivate(self):
        raise NotImplementedError(b'Should be implemented in subclass')
        return

    def _doDeactivate(self):
        raise NotImplementedError(b'Should be implemented in subclass')
        return
