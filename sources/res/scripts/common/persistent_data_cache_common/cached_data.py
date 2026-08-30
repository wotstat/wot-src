from __future__ import absolute_import
import typing
from collections import OrderedDict
from future.utils import iteritems, listitems
import wg_pickle
from persistent_data_cache_common.common import getLogger, MeasureExecutionTime
if typing.TYPE_CHECKING:
    from persistent_data_cache_common.types import TData, TPDCVersion
    from persistent_data_cache_common.serializers import ISerializer
    from persistent_data_cache_common.data_providers import PDProvider

class LoadedData(object):
    __slots__ = (b'_logger', b'_version', b'_data')

    def __init__(self, version, data):
        self._logger = getLogger(self.__class__.__name__)
        self._version = version
        self._data = data
        return

    @property
    def version(self):
        return self._version

    def deserialize(self, onDataDeserialized=None):
        appliedSerializers = OrderedDict()
        deserialized, timing = {}, MeasureExecutionTime(b'cache.part.unpacked')
        try:
            for name, (serialized, serializerClass) in self._data:
                with timing.start(name):
                    serializer = serializerClass()
                    appliedSerializers[name] = serializer
                    deserialized[name] = serializer.deserialize(serialized)
                    if callable(onDataDeserialized):
                        onDataDeserialized(name)
                self._logger.debug(b'Data <%s> has been loaded with <%s>.', name, serializer)

        except Exception:
            for name, appliedSerializer in iteritems(appliedSerializers):
                appliedSerializer.rollbackSideEffects()
                self._logger.debug(b'Deserialized data <%s|%s> side effects rollback.', name, appliedSerializer)

            raise

        timing.printTotalTime()
        return deserialized


class CreatedData(object):
    __slots__ = (b'_logger', b'_version', b'_data')

    def __init__(self, version):
        self._logger = getLogger(self.__class__.__name__)
        self._version = version
        self._data = OrderedDict()
        return

    def isEmpty(self):
        return len(self._data) == 0

    def add(self, provider, data):
        name = provider.name
        if name in self._data:
            self._logger.error(b'Data for <%s> already exist.', name)
            return
        serializerClass = provider.getSerializerClass()
        self._data[name] = (data, serializerClass)
        self._logger.debug(b'Data <%s|%s> added.', name, serializerClass)
        return

    def toDict(self):
        return {b'version': (self._version), b'data': (listitems(self._data))}


def dumps(cachedData):
    return wg_pickle.dumps(cachedData.toDict())


def loads(string):
    return LoadedData(**wg_pickle.loads(string))
