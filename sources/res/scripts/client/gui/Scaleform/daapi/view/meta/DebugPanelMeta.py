from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class DebugPanelMeta(BaseDAAPIComponent):

    def as_initReplayS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_initReplay()
        return

    def as_updatePingS(self, ping):
        if self._isDAAPIInited():
            return self.flashObject.as_updatePing(ping)
        return

    def as_updateFpsS(self, fps):
        if self._isDAAPIInited():
            return self.flashObject.as_updateFps(fps)
        return

    def as_updatePingFPSS(self, ping, fps):
        if self._isDAAPIInited():
            return self.flashObject.as_updatePingFPS(ping, fps)
        return

    def as_updateAllS(self, ping, fps, isLagging):
        if self._isDAAPIInited():
            return self.flashObject.as_updateAll(ping, fps, isLagging)
        return

    def as_updateReplayS(self, ping, fps, isLagging, replayFps):
        if self._isDAAPIInited():
            return self.flashObject.as_updateReplay(ping, fps, isLagging, replayFps)
        return
