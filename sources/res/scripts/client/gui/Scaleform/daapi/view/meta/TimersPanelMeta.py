from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class TimersPanelMeta(BaseDAAPIComponent):

    def as_setInitDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setInitData(data)
        return

    def as_showS(self, timerTypeID, timerViewTypeID, isBubble):
        if self._isDAAPIInited():
            return self.flashObject.as_show(timerTypeID, timerViewTypeID, isBubble)
        return

    def as_hideS(self, timerTypeID):
        if self._isDAAPIInited():
            return self.flashObject.as_hide(timerTypeID)
        return

    def as_setVerticalOffsetS(self, offsetY):
        if self._isDAAPIInited():
            return self.flashObject.as_setVerticalOffset(offsetY)
        return

    def as_setTimeInSecondsS(self, timerTypeID, totalSeconds, currentTime):
        if self._isDAAPIInited():
            return self.flashObject.as_setTimeInSeconds(timerTypeID, totalSeconds, currentTime)
        return

    def as_setTimeSnapshotS(self, timerTypeID, totalSeconds, timeLeft):
        if self._isDAAPIInited():
            return self.flashObject.as_setTimeSnapshot(timerTypeID, totalSeconds, timeLeft)
        return

    def as_setSpeedS(self, speed):
        if self._isDAAPIInited():
            return self.flashObject.as_setSpeed(speed)
        return

    def as_turnOnStackViewS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_turnOnStackView(value)
        return

    def as_setTimerTextS(self, timerID, title, description=b''):
        if self._isDAAPIInited():
            return self.flashObject.as_setTimerText(timerID, title, description)
        return

    def as_showSecondaryTimerS(self, secTimerID, totalSeconds, currentTime, secondInRow):
        if self._isDAAPIInited():
            return self.flashObject.as_showSecondaryTimer(secTimerID, totalSeconds, currentTime, secondInRow)
        return

    def as_hideSecondaryTimerS(self, secTimerID):
        if self._isDAAPIInited():
            return self.flashObject.as_hideSecondaryTimer(secTimerID)
        return

    def as_setSecondaryTimeSnapshotS(self, secTimerID, totalSeconds, currentTime):
        if self._isDAAPIInited():
            return self.flashObject.as_setSecondaryTimeSnapshot(secTimerID, totalSeconds, currentTime)
        return

    def as_setSecondaryTimerTextS(self, secTimerID, title, description=b''):
        if self._isDAAPIInited():
            return self.flashObject.as_setSecondaryTimerText(secTimerID, title, description)
        return
