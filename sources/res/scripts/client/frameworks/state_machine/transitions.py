import weakref
from .events import StateEvent, StringEvent
from .node import Node

class BaseTransition(Node):
    __slots__ = (b'__targets', b'__priority')

    def __init__(self, priority=0):
        super(BaseTransition, self).__init__()
        self.__targets = []
        self.__priority = priority
        return

    def __repr__(self):
        return (b'{}({}->{}, priority={})').format(self.__class__.__name__, self.getSource(), self.getTargets(), self.__priority)

    def clear(self):
        del self.__targets[:]
        super(BaseTransition, self).clear()
        return

    def getPriority(self):
        return self.__priority

    def getSource(self):
        return self.getParent()

    def getTargets(self):
        return [target() for target in self.__targets if target() is not None]

    def setTarget(self, state):
        self.__targets.append(weakref.ref(state))
        return

    def execute(self, event):
        raise NotImplementedError
        return


class ConditionTransition(BaseTransition):
    __slots__ = (b'__condition', b'__invert')

    def __init__(self, condition, invert=False, priority=0):
        super(ConditionTransition, self).__init__(priority=priority)
        self.__condition = condition
        self.__invert = invert
        return

    def clear(self):
        super(ConditionTransition, self).clear()
        self.__condition = None
        return

    def execute(self, event):
        result = self.__condition(event)
        if self.__invert:
            result = not result
        return result


class StringEventTransition(BaseTransition):
    __slots__ = (b'__token',)

    def __init__(self, token=b'', priority=0):
        super(StringEventTransition, self).__init__(priority=priority)
        self.__token = token
        return

    def execute(self, event):
        if isinstance(event, StringEvent):
            return not self.__token or event.token == self.__token
        return False
