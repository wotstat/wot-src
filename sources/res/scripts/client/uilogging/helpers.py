import typing
if typing.TYPE_CHECKING:
    from uilogging.base.logger import LOGGERS_TYPING

class _LazyLoggerDescriptor(object):
    __slots__ = (b'__class', b'__args', b'__kwargs', b'__instance')

    def __init__(self, class_, *args, **kwargs):
        self.__class = class_
        self.__args = args
        self.__kwargs = kwargs
        self.__instance = None
        return

    def __set__(self, *_, **__):
        raise AttributeError(b'% is readonly' % self.__class__.__name__)
        return

    def __get__(self, *_, **__):
        if not self.__instance:
            self.__instance = self.__class(*self.__args, **self.__kwargs)
        return self.__instance


def lazyUILogger(class_, *args, **kwargs):
    return _LazyLoggerDescriptor(class_, *args, **kwargs)
