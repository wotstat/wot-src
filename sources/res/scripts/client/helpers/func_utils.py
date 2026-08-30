import logging
from collections import namedtuple
from functools import partial, wraps
from time import sleep, time
import typing, BigWorld
from BWUtil import AsyncReturn
from PlayerEvents import g_playerEvents
from helpers import dependency
from skeletons.gui.game_control import IParagonsController
from th_async import th_async, th_await, AsyncScope, AsyncEvent, BrokenPromiseError
from debug_utils import LOG_DEBUG
_logger = logging.getLogger(__name__)
FLASH_IMG_PREFIX = b'img://'

def callback(delay, obj, methodName, *args):
    return BigWorld.callback(delay, partial(callMethod, obj, methodName, *args))


def callMethod(obj, methodName, *args):
    if hasattr(obj, methodName):
        getattr(obj, methodName)(*args)
    return


def debugDelay(timeLag):

    def delayCallDecorator(func):

        def delayCall(*args, **kwargs):
            BigWorld.callback(timeLag, partial(func, *args, **kwargs))
            return

        return delayCall

    return delayCallDecorator


def logFunc(func):

    def wrapped(*args, **kwargs):
        LOG_DEBUG(b'|||||||||||||||||| %s(%s, %s) |||||||||||' % (func.func_name, args, kwargs))
        func(*args, **kwargs)
        return

    return wrapped


def freeze(seconds, nextFrame=True):
    if nextFrame:
        LOG_DEBUG(b'Freeze call at', BigWorld.time())
        BigWorld.callback(0, partial(freeze, seconds, False))
        return
    LOG_DEBUG(b'Actual Freezing at', BigWorld.time())
    sleep(seconds)
    return


def oncePerPeriod(period):
    timeHolder = {(intern(b'lastRequest')): 0.0}

    def wrapper(func):

        def caller(*args, **kwargs):
            currTime = time()
            if currTime - timeHolder[b'lastRequest'] > period:
                timeHolder[b'lastRequest'] = currTime
                func(*args, **kwargs)
            return

        return caller

    return wrapper


CallParams = namedtuple(b'CallParams', (b'args', b'kwargs'))
CallParams.__new__.__defaults__ = ((), {})

class CooldownCaller(object):
    __slots__ = (b'__call', b'__cooldown', b'__paramsMerger', b'__lock', b'__delayedCalls')

    class _Lock(object):
        __slots__ = (b'__locked',)

        def __init__(self):
            self.__locked = False
            return

        def __enter__(self):
            self.__locked = True
            return

        def __exit__(self, *_, **__):
            self.__locked = False
            return

        @property
        def locked(self):
            return self.__locked

    def __init__(self, func, cooldown, paramsMerger):
        self.__call = func
        self.__cooldown = cooldown
        self.__paramsMerger = paramsMerger
        self.__lock = self._Lock()
        self.__delayedCalls = []
        return

    def __call__(self, *args, **kwargs):
        if self.__lock.locked:
            self.__delayCall(*args, **kwargs)
        else:
            self.__doCall(*args, **kwargs)
        return

    def __delayCall(self, *args, **kwargs):
        callParams = CallParams(args=args, kwargs=kwargs)
        self.__delayedCalls.append(callParams)
        return

    @th_async
    def __doCall(self, *args, **kwargs):
        with self.__lock:
            self.__call(*args, **kwargs)
            result = yield th_await(self.__waitForCooldown())
            if not result:
                self.__delayedCalls = []
        if self.__delayedCalls:
            callParams = self.__mergeDelayedCalls()
            self(*callParams.args, **callParams.kwargs)
        return

    @th_async
    def __waitForCooldown(self):
        scope = AsyncScope()
        event = AsyncEvent(scope=scope)
        callbackId = BigWorld.callback(self.__cooldown, event.set)
        try:
            try:
                g_playerEvents.onDisconnected += scope.destroy
                yield th_await(event.wait())
                result = True
            except BrokenPromiseError:
                BigWorld.cancelCallback(callbackId)
                result = False

        finally:
            g_playerEvents.onDisconnected -= scope.destroy

        raise AsyncReturn(result)
        return

    def __mergeDelayedCalls(self):
        merged = CallParams()
        while self.__delayedCalls:
            callParams = self.__delayedCalls.pop(0)
            merged = self.__paramsMerger(merged, callParams)

        return merged


def cooldownCallerDecorator(cooldown, paramsMerger):

    def decorator(func):
        return CooldownCaller(func, cooldown, paramsMerger)

    return decorator


def replaceImgPrefix(path):
    return path.replace(FLASH_IMG_PREFIX, b'')


@th_async
def waitEventAndCall(event, func):
    try:
        yield th_await(event.wait())
        func()
    except BrokenPromiseError:
        _logger.debug(b'%s has not been called. AsyncEvent scope has been destroyed', func.__name__ if hasattr(func, __name__) else func)

    return


def checkParagonsEnabled(func):

    @wraps(func)
    def wrapped(*args, **kwargs):
        paragonsController = dependency.instance(IParagonsController)
        if paragonsController.isEnabled:
            return func(*args, **kwargs)
        return

    return wrapped
