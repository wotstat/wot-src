from __future__ import absolute_import
import inspect, logging, types
from .actions_base import ActionBase
from .transitions_base import TransitionBase
from constants import IS_DEVELOPMENT
__all__ = [
 b'StateActionsRegistrar', b'TransitionsRegistrar']
_logger = logging.getLogger(__name__)

def findClassesInModule(module, baseCls):
    return list(value for key, value in inspect.getmembers(module, inspect.isclass) if issubclass(value, baseCls) and value is not baseCls and inspect.getmodule(value) is module and (not value.isDevOnly() or IS_DEVELOPMENT))


class StateActionsRegistrar(object):

    def __init__(self):
        self._domainActions = set()
        return

    def regActionsFromModule(self, module):
        for action in findClassesInModule(module, ActionBase):
            if action in self._domainActions:
                _logger.error(b'Action already registered: %s', action.__name__)
            else:
                self._domainActions.add(action)

        return

    def getActions(self):
        return self._domainActions


class TransitionsRegistrar(object):

    def __init__(self):
        self._transitions = set()
        return

    def regTransitionsFromModule(self, module):
        for transition in findClassesInModule(module, TransitionBase):
            if transition in self._transitions:
                _logger.error(b'Transition already registered: %s', transition.__name__)
            else:
                self._transitions.add(transition)

        return

    def getTransitions(self):
        return self._transitions
