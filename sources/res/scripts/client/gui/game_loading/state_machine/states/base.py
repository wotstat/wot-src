import time, typing, wg_async
from gui.game_loading import loggers
from helpers.CallbackDelayer import CallbackDelayer
from frameworks_common.state_machine import State, StateFlags, StateEvent
from gui.game_loading.state_machine.const import TickingMode
if typing.TYPE_CHECKING:
    from frameworks_common.state_machine import StateMachine
    from gui.game_loading.resources.base import BaseResources
    from gui.game_loading.resources.models import BaseResourceModel
_logger = loggers.getStatesLogger()

class _StateWaiting(object):
    __slots__ = (b'_states', b'_event', b'_resetOnStateEnter', b'_releaseOnStateExit', b'_destroyOnStateClear')

    def __init__(self, stateName, waiting=None, resetOnStateEnter=True, releaseOnStateExit=True):
        if waiting is None:
            self._event = wg_async.AsyncEvent()
            self._states = (stateName,)
            self._destroyOnStateClear = True
        else:
            self._event = waiting.getEvent()
            self._states = (waiting.getStateName(), stateName)
            self._destroyOnStateClear = False
        self._resetOnStateEnter = resetOnStateEnter
        self._releaseOnStateExit = releaseOnStateExit
        _logger.debug(b'[%s] Waiting initialized.', self._states)
        return

    def getStateName(self):
        return self._states[-1]

    def getEvent(self):
        return self._event

    def release(self):
        _logger.debug(b'[%s] Waiting released.', self._states)
        self._event.set()
        return

    def reset(self):
        _logger.debug(b'[%s] Waiting reset.', self._states)
        self._event.clear()
        return

    @wg_async.wg_async
    def wait(self):
        _logger.debug(b'[%s] Waiting started.', self._states)
        yield wg_async.wg_await(self._event.wait())
        _logger.debug(b'[%s] Waiting ends.', self._states)
        return

    def onStateEnter(self):
        if self._resetOnStateEnter:
            self.reset()
        return

    def onStateExit(self):
        if self._releaseOnStateExit:
            self.release()
        return

    def onStateClear(self):
        if self._destroyOnStateClear:
            self.release()
            self._event.destroy()
            _logger.debug(b'[%s] Waiting destroyed.', self._states)
        return


class BaseState(State):
    __slots__ = (b'_waiting',)

    def __init__(self, stateID, flags=StateFlags.UNDEFINED):
        super(BaseState, self).__init__(stateID=stateID, flags=flags)
        self._waiting = None
        return

    def clear(self):
        if self._waiting is not None:
            self._waiting.onStateClear()
            self._waiting = None
        super(BaseState, self).clear()
        _logger.debug(b'[%s] cleared.', self)
        return

    def initWaiting(self, waiting=None, releaseOnStateExit=True, resetOnStateEnter=True):
        if self._waiting is not None:
            _logger.warning(b'[%s] Waiting already initialized.', self)
            return
        else:
            self._waiting = _StateWaiting(stateName=repr(self), waiting=waiting, releaseOnStateExit=releaseOnStateExit, resetOnStateEnter=resetOnStateEnter)
            return

    @wg_async.wg_async
    def wait(self):
        if self._waiting is None:
            raise wg_async.AsyncReturn(None)
        yield wg_async.wg_await(self._waiting.wait())
        return

    def _releaseWaiting(self):
        if self._waiting is not None:
            self._waiting.release()
        return

    def _resetWaiting(self):
        if self._waiting is not None:
            self._waiting.reset()
        return

    def _onEntered(self, event):
        super(BaseState, self)._onEntered(event)
        if self._waiting is not None:
            self._waiting.onStateEnter()
        return

    def _onExited(self):
        if self._waiting is not None:
            self._waiting.onStateExit()
        super(BaseState, self)._onExited()
        return


class BaseTickingState(BaseState):
    __slots__ = (b'_tickingMode', b'_stopped', b'_ticker', b'_nextTickTime', b'_onCompleteEvent', b'_stepNumber', b'_isSelfTicking')

    def __init__(self, stateID, flags=StateFlags.UNDEFINED, tickingMode=TickingMode.MANUAL, onCompleteEvent=None):
        super(BaseTickingState, self).__init__(stateID, flags=flags)
        self._tickingMode = tickingMode
        self._nextTickTime = 0
        self._onCompleteEvent = onCompleteEvent or StateEvent()
        self._stopped = True
        self._ticker = None
        self._stepNumber = 0
        self._isSelfTicking = False
        return

    @property
    def timeLeft(self):
        return max(self._nextTickTime - time.time(), 0.0)

    def clear(self):
        self._stop()
        super(BaseTickingState, self).clear()
        return

    def manualTick(self, stepNumber=0):
        if self._stopped or not self.isEntered():
            return
        if self._tickingMode == TickingMode.SELF_TICKING:
            _logger.warning(b'[%s] Manual tick on self ticking state.', self)
            return
        self._stepNumber = stepNumber
        self._runTick()
        return

    def _start(self, *args, **kwargs):
        if not self.isEntered():
            _logger.debug(b'[%s] can not start not entered state.', self)
            return
        else:
            if not self._stopped:
                _logger.debug(b'[%s] already started.', self)
                return
            self._stopped = False
            nextTickDelay = self._runTick()
            _logger.debug(b'[%s] First tick delay <%s>.', self, nextTickDelay)
            if nextTickDelay is None:
                return
            self._startTicker(nextTickDelay)
            _logger.debug(b'[%s] started.', self)
            return

    def _stop(self, *args, **kwargs):
        self._stopTicker()
        self._isSelfTicking = False
        self._nextTickTime = 0
        self._stopped = True
        _logger.debug(b'[%s] stopped.', self)
        return

    def _runTick(self):
        if self._nextTickTime > 0:
            waitingTime = self.timeLeft
            if waitingTime > 0:
                return waitingTime
        nextTickDelay = self._task()
        isStateComplete = nextTickDelay is None or nextTickDelay < 0
        if isStateComplete:
            self._stop()
            machine = self.getMachine()
            if machine is not None:
                _logger.debug(b'[%s] complete, sending notification to state machine.', self)
                machine.post(self._onCompleteEvent)
            else:
                _logger.debug(b'[%s] not registered in state machine.', self)
            return
        self._nextTickTime = time.time() + nextTickDelay
        return nextTickDelay

    def _onEntered(self, event):
        super(BaseTickingState, self)._onEntered(event)
        self._start()
        return

    def _onExited(self):
        self._stop()
        super(BaseTickingState, self)._onExited()
        return

    def _runSelfTick(self):
        if not self._isSelfTicking:
            self._isSelfTicking = True
            _logger.debug(b'[%s] Became self ticking.', self)
        return self._runTick()

    def _startTicker(self, delay):
        if self._tickingMode != TickingMode.MANUAL and self._ticker is None and delay >= 0:
            self._ticker = CallbackDelayer()
            self._ticker.delayCallback(delay, self._runSelfTick)
            _logger.debug(b'[%s] ticker started.', self)
        return

    def _stopTicker(self):
        if self._ticker is not None:
            self._ticker.destroy()
            self._ticker = None
            _logger.debug(b'[%s] ticker stopped.', self)
        return

    def _task(self):
        raise NotImplementedError
        return


class BaseViewResourcesTickingState(BaseTickingState):
    __slots__ = (b'_resources', b'_overriddenViewTime', b'_minDurationEventTime')

    def __init__(self, stateID, resources, flags=StateFlags.UNDEFINED, tickingMode=TickingMode.MANUAL, minDurationEventTime=0, onCompleteEvent=None):
        super(BaseViewResourcesTickingState, self).__init__(stateID=stateID, flags=flags, tickingMode=tickingMode, onCompleteEvent=onCompleteEvent)
        self._resources = resources
        self._minDurationEventTime = minDurationEventTime
        self._overriddenViewTime = None
        return

    def _stop(self):
        self._overriddenViewTime = None
        self._resources.reset()
        super(BaseViewResourcesTickingState, self)._stop()
        return

    def _task(self):
        if self._overriddenViewTime is not None:
            viewTime = max(self._overriddenViewTime, 0)
            self._overriddenViewTime = None
            self._onMinDurationTimeReached()
            _logger.debug(b'[%s] Minimal time duration reached. Next view time <%s>', self, viewTime)
            return viewTime
        else:
            resource = self._selectResource()
            if not resource:
                return
            self._beforeView()
            self._view(resource)
            viewTime = resource.minShowTimeSec
            if self._minDurationEventTime > 0:
                self._overriddenViewTime = max(viewTime - self._minDurationEventTime, 0)
                viewTime = self._minDurationEventTime
                _logger.debug(b'[%s] Overridden view time <%s>', self, self._overriddenViewTime)
            _logger.debug(b'[%s] Next tick time <%s>', self, viewTime)
            return viewTime

    def _selectResource(self):
        return self._resources.get()

    def _beforeView(self):
        return

    def _onMinDurationTimeReached(self):
        return

    def _view(self, resource):
        raise NotImplementedError
        return


class BaseGroupTickingStates(BaseState):
    __slots__ = ()

    def manualTick(self, stepNumber=0):
        for state in self.getChildrenStates():
            if isinstance(state, (BaseTickingState, BaseGroupTickingStates)) and state.isEntered():
                state.manualTick(stepNumber)

        return
