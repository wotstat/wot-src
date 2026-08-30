from __future__ import absolute_import
import functools, inspect, logging
from frameworks.wulf import View, ViewStatus
from helpers.uniprof import regions
from py2to3.backport.inspect import getargspec
_REGION_FORMAT = b'view.{}.{}'
_logger = logging.getLogger(__name__)
_logger.addHandler(logging.NullHandler())

def args2params(*types):

    def _decorator(func):

        @functools.wraps(func)
        def _wrapper(*args):
            signature = getargspec(func).args
            if b'self' in signature:
                args, kwargs = (
                 args[0],), args[1]
                signature.remove(b'self')
            else:
                args, kwargs = tuple(), args[0]
            if types:
                for idx, name in enumerate(signature):
                    try:
                        kwargs[name] = types[idx](kwargs[name])
                    except (ValueError, TypeError) as e:
                        _logger.warning(b'There is an error while converting arg @%s[%s] to %s: %s', name, kwargs[name], str(types[idx]), str(e))

            return func(*args, **kwargs)

        return _wrapper

    return _decorator


def trackLifeCycle(uniqueName):
    return ViewLifeCycleToRegions(uniqueName)


class ViewLifeCycleToRegions(object):
    __slots__ = (b'__uniqueName', b'__viewStatus')

    def __init__(self, uniqueName):
        super(ViewLifeCycleToRegions, self).__init__()
        self.__uniqueName = uniqueName
        self.__viewStatus = ViewStatus.UNDEFINED
        return

    def __call__(self, clazz):
        if View not in inspect.getmro(clazz):
            raise UserWarning((b'The following argument {} is not subclass of View').format(clazz))

        def swap(func):

            @functools.wraps(func)
            def wrapper(view, oldStatus, newStatus, *args, **kwargs):
                func(view, oldStatus, newStatus, *args, **kwargs)
                self.__trigger(newStatus)
                return

            return wrapper

        if not getattr(clazz, b'__lifeCycleTracked__', False):
            setattr(clazz, b'_swapStates', swap(getattr(clazz, b'_swapStates')))
            setattr(clazz, b'__lifeCycleTracked__', True)
        else:
            _logger.warning(b'Class already wrapped: %r', clazz)
        return clazz

    def __enter(self):
        regions.enterToRegion(_REGION_FORMAT.format(self.__uniqueName, ViewStatus.getKeyByValue(self.__viewStatus).lower()))
        return

    def __exit(self):
        regions.exitFromRegion(_REGION_FORMAT.format(self.__uniqueName, ViewStatus.getKeyByValue(self.__viewStatus).lower()))
        return

    def __trigger(self, newState):
        if self.__viewStatus != ViewStatus.UNDEFINED:
            self.__exit()
        self.__viewStatus = newState
        if self.__viewStatus != ViewStatus.DESTROYED:
            self.__enter()
        return
