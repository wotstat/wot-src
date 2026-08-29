from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class StatsBaseMeta(BaseDAAPIComponent):

    def acceptSquad(self, sessionID):
        self._printOverrideError(b'acceptSquad')
        return

    def addToSquad(self, sessionID):
        self._printOverrideError(b'addToSquad')
        return

    def as_setIsInteractiveS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setIsInteractive(value)
        return
