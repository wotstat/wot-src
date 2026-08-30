from __future__ import absolute_import
import typing
from soft_exception import SoftException
if typing.TYPE_CHECKING:
    from persistent_data_cache_common.types import TPDCVersion

class BasePDCConfig(object):
    __slots__ = (b'version', b'cacheFilePath')

    def __init__(self, version, cacheFilePath):
        self.version = version
        if not cacheFilePath:
            raise SoftException(b'Cache file path cannot be empty.')
        self.cacheFilePath = cacheFilePath
        return

    def __repr__(self):
        return (b'<{}>(version={}, cacheFilePath={})').format(self.__class__.__name__, self.version, self.cacheFilePath)
