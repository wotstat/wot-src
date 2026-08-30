from constants import IS_CLIENT, IS_CELLAPP, IS_BASEAPP
from soft_exception import SoftException
_IS_LEGACY_STUFF_SUPPORTED = not IS_CLIENT and not IS_CELLAPP and not IS_BASEAPP

class SupportedLegacyStuff(object):
    __slots__ = ()

    def __getitem__(self, item):
        return getattr(self, item)

    def __setitem__(self, key, value):
        setattr(self, key, value)
        return

    def __contains__(self, item):
        return hasattr(self, item)

    def __iter__(self):
        raise NotImplementedError
        return

    def keys(self):
        raise NotImplementedError
        return

    def values(self):
        raise NotImplementedError
        return

    def items(self):
        raise NotImplementedError
        return

    def get(self, k, d=None):
        return getattr(self, k, d)

    def copy(self):
        raise NotImplementedError
        return

    def clear(self):
        raise NotImplementedError
        return

    def has_key(self, k):
        raise NotImplementedError
        return

    def update(self, *args, **kwargs):
        raise NotImplementedError
        return

    def pop(self, *args):
        raise NotImplementedError
        return


class NoLegacyStuff(object):
    __slots__ = ()

    def __getitem__(self, item):
        raise SoftException(b'Operation is not allowed')
        return

    def __setitem__(self, key, value):
        raise SoftException(b'Operation is not allowed')
        return

    def __contains__(self, item):
        raise SoftException(b'Operation is not allowed')
        return

    def __iter__(self):
        raise SoftException(b'Operation is not allowed')
        return

    def keys(self):
        raise SoftException(b'Operation is not supported')
        return

    def values(self):
        raise SoftException(b'Operation is not supported')
        return

    def items(self):
        raise SoftException(b'Operation is not supported')
        return

    def get(self, k, d=None):
        raise SoftException(b'Operation is not allowed')
        return

    def copy(self):
        raise NotImplementedError
        return

    def clear(self):
        raise SoftException(b'Operation is not allowed')
        return

    def has_key(self, k):
        raise SoftException(b'Operation is not allowed')
        return

    def update(self, *args, **kwargs):
        raise SoftException(b'Operation is not allowed')
        return

    def pop(self, *args):
        raise SoftException(b'Operation is not allowed')
        return


if _IS_LEGACY_STUFF_SUPPORTED:
    LegacyStuff = SupportedLegacyStuff
else:
    LegacyStuff = NoLegacyStuff
