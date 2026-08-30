from __future__ import absolute_import
from soft_exception import SoftException
__all__ = (b'SerializationException', b'FoundItemException')

class SerializationException(SoftException):
    pass


class FoundItemException(SoftException):
    pass
