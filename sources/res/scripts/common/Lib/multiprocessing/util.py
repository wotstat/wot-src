import os, itertools, weakref, atexit, threading
from subprocess import _args_from_interpreter_flags
from multiprocessing.process import current_process, active_children
__all__ = [
 4, 5, 6, 7, 8, 
 9, 10, 11, 
 12, 13, 14, 15, 
 16, 17]
NOTSET = 0
SUBDEBUG = 5
DEBUG = 10
INFO = 20
SUBWARNING = 25
LOGGER_NAME = b'multiprocessing'
DEFAULT_LOGGING_FORMAT = b'[%(levelname)s/%(processName)s] %(message)s'
_logger = None
_log_to_stderr = False

def sub_debug(msg, *args):
    global _logger
    if _logger:
        _logger.log(SUBDEBUG, msg, *args)
    return


def debug(msg, *args):
    if _logger:
        _logger.log(DEBUG, msg, *args)
    return


def info(msg, *args):
    if _logger:
        _logger.log(INFO, msg, *args)
    return


def sub_warning(msg, *args):
    if _logger:
        _logger.log(SUBWARNING, msg, *args)
    return


def get_logger():
    global _logger
    import logging, atexit
    logging._acquireLock()
    try:
        if not _logger:
            _logger = logging.getLogger(LOGGER_NAME)
            _logger.propagate = 0
            logging.addLevelName(SUBDEBUG, b'SUBDEBUG')
            logging.addLevelName(SUBWARNING, b'SUBWARNING')
            if hasattr(atexit, b'unregister'):
                atexit.unregister(_exit_function)
                atexit.register(_exit_function)
            else:
                atexit._exithandlers.remove((_exit_function, (), {}))
                atexit._exithandlers.append((_exit_function, (), {}))
    finally:
        logging._releaseLock()

    return _logger


def log_to_stderr(level=None):
    global _log_to_stderr
    import logging
    logger = get_logger()
    formatter = logging.Formatter(DEFAULT_LOGGING_FORMAT)
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    if level:
        logger.setLevel(level)
    _log_to_stderr = True
    return _logger


def get_temp_dir():
    if current_process()._tempdir is None:
        import shutil, tempfile
        tempdir = tempfile.mkdtemp(prefix=b'pymp-')
        info(b'created temp directory %s', tempdir)
        Finalize(None, shutil.rmtree, args=[tempdir], exitpriority=-100)
        current_process()._tempdir = tempdir
    return current_process()._tempdir


_afterfork_registry = weakref.WeakValueDictionary()
_afterfork_counter = itertools.count()

def _run_after_forkers():
    items = list(_afterfork_registry.items())
    items.sort()
    for (index, ident, func), obj in items:
        try:
            func(obj)
        except Exception as e:
            info(b'after forker raised exception %s', e)

    return


def register_after_fork(obj, func):
    _afterfork_registry[(_afterfork_counter.next(), id(obj), func)] = obj
    return


_finalizer_registry = {}
_finalizer_counter = itertools.count()

class Finalize(object):

    def __init__(self, obj, callback, args=(), kwargs=None, exitpriority=None):
        if obj is not None:
            self._weakref = weakref.ref(obj, self)
        self._callback = callback
        self._args = args
        self._kwargs = kwargs or {}
        self._key = (exitpriority, _finalizer_counter.next())
        self._pid = os.getpid()
        _finalizer_registry[self._key] = self
        return

    def __call__(self, wr=None):
        try:
            del _finalizer_registry[self._key]
        except KeyError:
            sub_debug(b'finalizer no longer registered')
        else:
            if self._pid != os.getpid():
                sub_debug(b'finalizer ignored because different process')
                res = None
            else:
                sub_debug(b'finalizer calling %s with args %s and kwargs %s', self._callback, self._args, self._kwargs)
                res = self._callback(*self._args, **self._kwargs)
            self._weakref = self._callback = self._args = self._kwargs = self._key = None
            return res

        return

    def cancel(self):
        try:
            del _finalizer_registry[self._key]
        except KeyError:
            pass
        else:
            self._weakref = self._callback = self._args = self._kwargs = self._key = None

        return

    def still_active(self):
        return self._key in _finalizer_registry

    def __repr__(self):
        try:
            obj = self._weakref()
        except (AttributeError, TypeError):
            obj = None

        if obj is None:
            return b'<Finalize object, dead>'
        else:
            x = b'<Finalize object, callback=%s' % getattr(self._callback, b'__name__', self._callback)
            if self._args:
                x += b', args=' + str(self._args)
            if self._kwargs:
                x += b', kwargs=' + str(self._kwargs)
            if self._key[0] is not None:
                x += b', exitprority=' + str(self._key[0])
            return x + b'>'


def _run_finalizers(minpriority=None):
    if _finalizer_registry is None:
        return
    else:
        if minpriority is None:
            f = lambda p: p[0][0] is not None
        else:
            f = lambda p: p[0][0] is not None and p[0][0] >= minpriority
        items = [x for x in _finalizer_registry.items() if f(x)]
        items.sort(reverse=True)
        for key, finalizer in items:
            sub_debug(b'calling %s', finalizer)
            try:
                finalizer()
            except Exception:
                import traceback
                traceback.print_exc()

        if minpriority is None:
            _finalizer_registry.clear()
        return


def is_exiting():
    global _exiting
    return _exiting or _exiting is None


_exiting = False

def _exit_function(info=info, debug=debug, _run_finalizers=_run_finalizers, active_children=active_children, current_process=current_process):
    info(b'process shutting down')
    debug(b'running all "atexit" finalizers with priority >= 0')
    _run_finalizers(0)
    if current_process() is not None:
        for p in active_children():
            if p._daemonic:
                info(b'calling terminate() for daemon %s', p.name)
                p._popen.terminate()

        for p in active_children():
            info(b'calling join() for process %s', p.name)
            p.join()

    debug(b'running the remaining "atexit" finalizers')
    _run_finalizers()
    return


atexit.register(_exit_function)

class ForkAwareThreadLock(object):

    def __init__(self):
        self._reset()
        register_after_fork(self, ForkAwareThreadLock._reset)
        return

    def _reset(self):
        self._lock = threading.Lock()
        self.acquire = self._lock.acquire
        self.release = self._lock.release
        return


class ForkAwareLocal(threading.local):

    def __init__(self):
        register_after_fork(self, (lambda obj: obj.__dict__.clear()))
        return

    def __reduce__(self):
        return (
         type(self), ())
