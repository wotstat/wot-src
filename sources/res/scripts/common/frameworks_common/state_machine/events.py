from __future__ import absolute_import
import typing

class StateEvent(object):
    __slots__ = (b'__arguments',)

    def __init__(self, *args, **kwargs):
        super(StateEvent, self).__init__()
        self.__arguments = kwargs
        return

    def __repr__(self):
        return (b'{}({})').format(self.__class__.__name__, id(self))

    def getArgument(self, name, default=None):
        return self.__arguments.get(name, default)


class StringEvent(StateEvent):
    __slots__ = (b'__token',)

    def __init__(self, token, **kwargs):
        super(StringEvent, self).__init__(**kwargs)
        self.__token = token
        return

    def __repr__(self):
        return (b'{}({})').format(self.__class__.__name__, self.__token)

    @property
    def token(self):
        return self.__token
