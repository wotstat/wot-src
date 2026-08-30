from functools import partial, wraps
from time import sleep, time
import BigWorld
from constants import IS_DEVELOPMENT
from debug_utils import LOG_DEBUG
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


def replaceImgPrefix(path):
    return path.replace(FLASH_IMG_PREFIX, b'')


def isDeveloperFunc(func):

    @wraps(func)
    def decorator(*args, **kwargs):
        if not IS_DEVELOPMENT:
            return
        return func(*args, **kwargs)

    return decorator
