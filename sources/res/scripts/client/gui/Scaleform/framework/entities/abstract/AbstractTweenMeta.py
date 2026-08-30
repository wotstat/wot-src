from gui.Scaleform.framework.entities.BaseDAAPIModule import BaseDAAPIModule

class AbstractTweenMeta(BaseDAAPIModule):

    def initialiaze(self, props):
        self._printOverrideError(b'initialiaze')
        return

    def creatTweenPY(self, tween):
        self._printOverrideError(b'creatTweenPY')
        return

    def getPaused(self):
        self._printOverrideError(b'getPaused')
        return

    def setPaused(self, paused):
        self._printOverrideError(b'setPaused')
        return

    def getLoop(self):
        self._printOverrideError(b'getLoop')
        return

    def setLoop(self, loop):
        self._printOverrideError(b'setLoop')
        return

    def getDuration(self):
        self._printOverrideError(b'getDuration')
        return

    def setDuration(self, duration):
        self._printOverrideError(b'setDuration')
        return

    def getPosition(self):
        self._printOverrideError(b'getPosition')
        return

    def setPosition(self, position):
        self._printOverrideError(b'setPosition')
        return

    def getDelay(self):
        self._printOverrideError(b'getDelay')
        return

    def setDelay(self, delay):
        self._printOverrideError(b'setDelay')
        return

    def resetAnim(self):
        self._printOverrideError(b'resetAnim')
        return

    def getTweenIdx(self):
        self._printOverrideError(b'getTweenIdx')
        return

    def getIsComplete(self):
        self._printOverrideError(b'getIsComplete')
        return

    def postponedCheckState(self):
        self._printOverrideError(b'postponedCheckState')
        return

    def getTargetDisplayObjectS(self):
        if self._isDAAPIInited():
            return self.flashObject.getTargetDisplayObject()
        return

    def onAnimCompleteS(self):
        if self._isDAAPIInited():
            return self.flashObject.onAnimComplete()
        return

    def onAnimStartS(self):
        if self._isDAAPIInited():
            return self.flashObject.onAnimStart()
        return
