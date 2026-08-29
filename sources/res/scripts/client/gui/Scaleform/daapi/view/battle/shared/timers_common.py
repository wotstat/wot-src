import BigWorld
from gui.shared.utils.TimeInterval import TimeInterval

class TimerComponent(object):
    __slots__ = (b'_viewObject', b'_typeID', b'_viewID', b'_totalTime', b'_startTime', b'_finishTime', b'_secondInRow')

    def __init__(self, viewObject, typeID, viewID, totalTime, finishTime, startTime=None, secondInRow=False, **kwargs):
        super(TimerComponent, self).__init__(**kwargs)
        self._viewObject = viewObject
        self._typeID = typeID
        self._viewID = viewID
        self._totalTime = totalTime
        self._secondInRow = secondInRow
        if finishTime:
            self._startTime = finishTime - totalTime
            self._finishTime = finishTime
        else:
            self._startTime = BigWorld.serverTime()
            self._finishTime = self._startTime + totalTime if totalTime > 0 else self._startTime
        return

    def __repr__(self):
        return (b'TimerComponent(typeID = {}, viewID = {}, totalTime = {})').format(self._typeID, self._viewID, self._totalTime)

    def clear(self):
        self._viewObject = None
        return

    def show(self, isBubble=True):
        self._showView(isBubble)
        self._startTick()
        return

    def hide(self):
        self._stopTick()
        self._hideView()
        return

    @property
    def typeID(self):
        return self._typeID

    @property
    def viewID(self):
        return self._viewID

    @property
    def finishTime(self):
        return self._finishTime

    @property
    def totalTime(self):
        return self._totalTime

    def _startTick(self):
        raise NotImplementedError
        return

    def _stopTick(self):
        raise NotImplementedError
        return

    def _hideView(self):
        raise NotImplementedError
        return

    def _showView(self, isBubble):
        raise NotImplementedError
        return


class PythonTimer(TimerComponent):
    __slots__ = (b'_timeInterval', b'__weakref__')

    def __init__(self, viewObject, typeID, viewID, totalTime, finishTime, startTime=None, interval=1.0, secondInRow=False, **kwargs):
        super(PythonTimer, self).__init__(viewObject, typeID, viewID, totalTime, finishTime, startTime, secondInRow=secondInRow, **kwargs)
        self._timeInterval = TimeInterval(interval, self, b'_tick')
        return

    def clear(self):
        self._timeInterval.stop()
        super(PythonTimer, self).clear()
        return

    def _startTick(self):
        if self._totalTime:
            timeLeft = max(0, self._finishTime - BigWorld.serverTime())
            if timeLeft:
                self._setViewSnapshot(timeLeft)
                self._timeInterval.restart()
        return

    def _stopTick(self):
        self._timeInterval.stop()
        return

    def _tick(self):
        timeLeft = self._finishTime - BigWorld.serverTime()
        if timeLeft >= 0:
            self._setViewSnapshot(timeLeft)
        else:
            self.hide()
        return

    def _setViewSnapshot(self, timeLeft):
        raise NotImplementedError
        return


class PrecisePythonTimer(PythonTimer):
    __slots__ = (b'__short1stPeriodCbId', b'__interval', b'_timeInterval', b'_startTime')

    def __init__(self, viewObject, typeID, viewID, totalTime, finishTime, startTime=None, interval=1.0, secondInRow=False, **kwargs):
        super(PrecisePythonTimer, self).__init__(viewObject, typeID, viewID, totalTime, finishTime, startTime, interval, secondInRow, **kwargs)
        if startTime is not None:
            self._startTime = startTime
        self.__interval = interval
        self.__short1stPeriodCbId = None
        return

    def _startTick(self):
        if self._totalTime:
            timeLeft = max(0, self._finishTime - BigWorld.serverTime())
            if timeLeft:
                self._setViewSnapshot(timeLeft)
                self._timeInterval = TimeInterval(self.__interval, self, b'_tick')
                firstShortPeriod = float(self._totalTime) % self.__interval
                if round(firstShortPeriod, 4) > 0.0:
                    self.__short1stPeriodCbId = BigWorld.callback(firstShortPeriod, self.__onShort1stPeriodFinished)
                else:
                    self._timeInterval.restart()
        return

    def clear(self):
        self.__clearShort1stPeriodCb()
        super(PrecisePythonTimer, self).clear()
        return

    def _stopTick(self):
        self.__clearShort1stPeriodCb()
        super(PrecisePythonTimer, self)._stopTick()
        return

    def _setViewSnapshot(self, timeLeft):
        raise NotImplementedError
        return

    def __clearShort1stPeriodCb(self):
        if self.__short1stPeriodCbId is not None:
            BigWorld.cancelCallback(self.__short1stPeriodCbId)
        self.__short1stPeriodCbId = None
        return

    def __onShort1stPeriodFinished(self):
        self.__short1stPeriodCbId = None
        self._tick()
        timeLeft = self._finishTime - BigWorld.serverTime()
        if timeLeft > 0:
            self._timeInterval.restart()
        else:
            self.hide()
        return
