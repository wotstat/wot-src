from __future__ import absolute_import
import copy, weakref

class Listenable:

    def __init__(self):
        self.listeners = _Listeners()
        return

    def addListener(self, eventName, fn):
        self.listeners.addListener(eventName, fn)
        return

    def removeListener(self, eventName, fn):
        self.listeners.removeListener(eventName, fn)
        return


class _Listeners(object):

    def __init__(self):
        self.listeners = {}
        return

    def addListener(self, eventName, fn):
        if eventName not in self.listeners:
            self.listeners[eventName] = set()
        self.listeners[eventName].add(fn)
        return

    def removeListener(self, eventName, fn):
        if eventName in self.listeners and fn in self.listeners[eventName]:
            self.listeners[eventName].remove(fn)
        if eventName in self.listeners and len(self.listeners[eventName]) == 0:
            del self.listeners[eventName]
        return

    def __getattribute__(self, name):
        try:
            return object.__getattribute__(self, name)
        except AttributeError:
            return _ListenerDispatch(self, name)

        return


class _ListenerDispatch:

    def __init__(self, dispatcher, eventName):
        self.dispatcher = dispatcher
        self.eventName = eventName
        return

    def __call__(self, *args, **kargs):
        if self.eventName not in self.dispatcher.listeners:
            return
        functions = self.dispatcher.listeners[self.eventName]
        for fn in copy.copy(functions):
            fn(*args, **kargs)

        return


class _ListenerFunc(object):

    def __init__(self, func):
        if hasattr(func, b'im_self'):
            self.isBoundMethod = True
            self.ref = weakref.ref(func.im_self)
            self.func = func.im_func
        else:
            self.isBoundMethod = False
            self.ref = weakref.ref(func)
        return

    def matches(self, func):
        if not self.alive():
            return False
        else:
            if self.isBoundMethod:
                return func == getattr(self.ref(), self.func.func_name)
            return func == self.ref()

        return

    def alive(self):
        return self.ref() is not None

    def get(self):
        obj = self.ref()
        if obj is not None:
            if self.isBoundMethod:
                return getattr(obj, self.func.func_name)
            else:
                return obj

        return

    def __call__(self, *args, **kwargs):
        fn = self.get()
        if fn is not None:
            return fn(*args, **kwargs)
        else:
            return


class FunctionListeners(object):

    def __init__(self):
        self.listeners = []
        return

    def append(self, func):
        self.listeners.append(_ListenerFunc(func))
        return

    def remove(self, func):
        for listener in self.listeners:
            if listener.matches(func):
                self.listeners.remove(listener)
                break

        return

    def reset(self):
        self.listeners = []
        return

    def __call__(self, *args, **kwargs):
        self.listeners = [item for item in self.listeners if item.alive()]
        for listener in self.listeners:
            listener(*args, **kwargs)

        return
