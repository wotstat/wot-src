import logging, operator
from . import states as _states
from . import validator
from . import visitor
from .events import StateEvent
from .exceptions import StateMachineError
from .observers import BaseStateObserver
from .observers import StateObserversContainer
from .transitions import BaseTransition
_logger = logging.getLogger(__name__)

class StateMachine(_states.State):
    __slots__ = (b'__isRunning', b'__entered', b'__history', b'__observers')

    def __init__(self, stateID=b''):
        super(StateMachine, self).__init__(stateID=stateID)
        self.__isRunning = False
        self.__entered = []
        self.__history = {}
        self.__observers = StateObserversContainer()
        return

    @staticmethod
    def isMachine():
        return True

    def start(self, doValidate=True):
        if doValidate:
            validator.validate(self)
        if self.__isRunning:
            _logger.debug(b'%r: Machine is already started', self)
            return
        else:
            self.__isRunning = True
            transition = _InitialTransition(target=self.getInitial())
            _logger.debug(b'%r: Machine is started by %r', self, transition)
            entered = self.__enter((transition,))
            transition.clear()
            self.__notify(entered, True, None)
            self.__tick()
            return

    def stop(self):
        if not self.__isRunning:
            _logger.debug(b'%r: Machine is not started', self)
            return
        self.__isRunning = False
        self.__observers.clear()
        self.__history.clear()
        del self.__entered[:]
        self.clear()
        _logger.debug(b'%r: Machine is stopped', self)
        return

    def isStateEntered(self, stateID):
        for state in self.__entered:
            if state.getStateID() == stateID:
                return True

        return False

    def isRunning(self):
        return self.__isRunning

    def addState(self, state):
        self.addChildState(state)
        return

    def removeState(self, state):
        self.removeChildState(state)
        return

    def post(self, event):
        _logger.debug(b'%r: %r is posted', self, event)
        if not isinstance(event, StateEvent):
            raise StateMachineError(b'Instance of StateEvent class is required')
        if not self.__isRunning:
            raise StateMachineError(b'State machine is not running')
        self.__tick(event=event)
        return

    def connect(self, observer):
        self.__observers.addObserver(observer)
        for state in self.__entered:
            observer.onStateChanged(state.getStateID(), True)

        return

    def disconnect(self, observer):
        self.__observers.removeObserver(observer)
        return

    def __tick(self, event=None):
        transitions = self.__select(event)
        if transitions:
            self.__process(transitions, event)
        return

    def __process(self, transitions, event):
        _logger.debug(b'%r: Start process, enabled transitions = %r', self, transitions)
        _logger.debug(b'%r: Snapshot before exiting states = %r', self, self.__entered)
        exited = self.__exit(transitions)
        _logger.debug(b'%r: Snapshot after exiting states = %r', self, self.__entered)
        entered = self.__enter(transitions)
        self.__notify(exited, False, event)
        self.__notify(entered, True, event)
        for state in self.__entered:
            if state.isFinal() and state.getParent() == self:
                self.stop()
                break

        _logger.debug(b'%r: Snapshot after entering states = %r', self, self.__entered)
        _logger.debug(b'%r: Stop process', self)
        return

    def __select(self, event):
        result = []
        filtered = [state for state in self.__entered if state.isAtomic()]
        for state in filtered:
            states = visitor.getAncestors(state, upper=self.getParent())
            states.insert(0, state)
            transition = self.__execute(states, event)
            if transition is not None and transition not in result:
                result.append(transition)

        return result

    def __execute(self, states, event):
        result = []
        for state in states:
            transitions = state.getTransitions()
            for transition in transitions:
                if transition.execute(event):
                    _logger.debug(b'%r: %r has execution result is True', self, transition)
                    result.append(transition)

            if result:
                result.sort(key=operator.methodcaller(b'getPriority'), reverse=True)
                transition = result[0]
                _logger.debug(b'%r: %r is selected', self, transition)
                return transition

        return

    def __exit(self, transitions):
        result = []
        for transition in transitions:
            domain = visitor.getTransitionDomain(transition, self.__history, upper=self.getParent())
            for state in self.__entered:
                if visitor.isDescendantOf(state, domain) and state not in result:
                    result.append(state)

        result.sort(key=_states.StateExitingSortKey)
        for state in result:
            for history in state.getHistoryStates():
                historyFlag = history.getFlags() & _states.StateFlags.HISTORY_TYPE_MASK
                if historyFlag == _states.StateFlags.DEEP_HISTORY:
                    snapshot = [entered for entered in self.__entered if entered.isAtomic() and visitor.isDescendantOf(entered, state)]
                else:
                    snapshot = [entered for entered in self.__entered if entered.getParent() == state]
                self.__history[history.getStateID()] = snapshot
                _logger.debug(b'%r: snapshot is recorded to history for %r -> %r', self, state, snapshot)

        for state in result:
            _logger.debug(b'%r: %r is exiting', self, state)
            state.exit()
            self.__entered.remove(state)

        return result

    def __enter(self, transitions):
        result = []
        for transition in transitions:
            self.__collect(transition, result)

        result.sort(key=_states.StateEnteringSortKey)
        for state in result:
            self.__entered.append(state)
            _logger.debug(b'%r: %r is entering', self, state)
            state.enter()

        return result

    def __collect(self, transition, accumulation):
        domain = visitor.getTransitionDomain(transition, self.__history, upper=self.getParent())
        for state in transition.getTargets():
            self.__dcollect(state, accumulation)

        for state in visitor.getEffectiveTargetStates(transition, self.__history):
            self.__acollect(state, domain, accumulation)

        return

    def __dcollect(self, state, accumulation):
        if state.isHistory():
            self.__restore(state, accumulation)
        else:
            accumulation.append(state)
            if state.isCompound():
                self.__dcollect(state.getInitial(), accumulation)
                self.__acollect(state.getInitial(), state, accumulation)
            elif state.isParallel():
                self.__pcollect(state, accumulation)
        return

    def __acollect(self, state, root, accumulation):
        ancestors = visitor.getAncestors(state, root)
        for ancestor in ancestors:
            if ancestor.getParent() is None:
                continue
            accumulation.append(ancestor)
            if ancestor.isParallel():
                self.__pcollect(state, accumulation)

        return

    def __pcollect(self, state, accumulation):
        for child in state.getChildrenStates():
            for item in accumulation:
                if visitor.isDescendantOf(item, child):
                    break
            else:
                self.__dcollect(child, accumulation)

        return

    def __restore(self, history, accumulation):
        stateID = history.getStateID()
        if stateID in self.__history:
            states = self.__history[stateID]
        else:
            transitions = history.getTransitions()
            if transitions:
                states = (
                 transitions[0].getTarget(),)
            else:
                states = ()
        for state in states:
            self.__dcollect(state, accumulation)
            parent = state.getParent()
            if parent is not None:
                self.__acollect(state, parent, accumulation)

        return

    def __notify(self, states, flag, event):
        for state in states:
            stateID = state.getStateID()
            if not stateID:
                _logger.warn(b'%r: %r has no ID, can not notify observers', self, state)
                continue
            self.__observers.onStateChanged(stateID, flag, event=event)

        return


class _InitialTransition(BaseTransition):
    __slots__ = ()

    def __init__(self, target):
        super(_InitialTransition, self).__init__()
        self.setTarget(target)
        return

    def getSource(self):
        return _states.State()

    def execute(self, event):
        return True
