__all__ = [
 0, 1, 2, 3, 
 4, 5, 6, 7, 8, 
 9, 10, 11, 12, 13, 14]
import threading, sys, weakref, array, itertools
from multiprocessing import TimeoutError, cpu_count
from multiprocessing.dummy.connection import Pipe
from threading import Lock, RLock, Semaphore, BoundedSemaphore
from threading import Event
from Queue import Queue

class DummyProcess(threading.Thread):

    def __init__(self, group=None, target=None, name=None, args=(), kwargs={}):
        threading.Thread.__init__(self, group, target, name, args, kwargs)
        self._pid = None
        self._children = weakref.WeakKeyDictionary()
        self._start_called = False
        self._parent = current_process()
        return

    def start(self):
        self._start_called = True
        if hasattr(self._parent, b'_children'):
            self._parent._children[self] = None
        threading.Thread.start(self)
        return

    @property
    def exitcode(self):
        if self._start_called and not self.is_alive():
            return 0
        else:
            return
            return


class Condition(threading._Condition):
    notify_all = threading._Condition.notify_all.im_func


Process = DummyProcess
current_process = threading.current_thread
current_process()._children = weakref.WeakKeyDictionary()

def active_children():
    children = current_process()._children
    for p in list(children):
        if not p.is_alive():
            children.pop(p, None)

    return list(children)


def freeze_support():
    return


class Namespace(object):

    def __init__(self, **kwds):
        self.__dict__.update(kwds)
        return

    def __repr__(self):
        items = self.__dict__.items()
        temp = []
        for name, value in items:
            if not name.startswith(b'_'):
                temp.append(b'%s=%r' % (name, value))

        temp.sort()
        return b'Namespace(%s)' % str.join(b', ', temp)


dict = dict
list = list

def Array(typecode, sequence, lock=True):
    return array.array(typecode, sequence)


class Value(object):

    def __init__(self, typecode, value, lock=True):
        self._typecode = typecode
        self._value = value
        return

    def _get(self):
        return self._value

    def _set(self, value):
        self._value = value
        return

    value = property(_get, _set)

    def __repr__(self):
        return b'<%s(%r, %r)>' % (type(self).__name__, self._typecode, self._value)


def Manager():
    return sys.modules[__name__]


def shutdown():
    return


def Pool(processes=None, initializer=None, initargs=()):
    from multiprocessing.pool import ThreadPool
    return ThreadPool(processes, initializer, initargs)


JoinableQueue = Queue
