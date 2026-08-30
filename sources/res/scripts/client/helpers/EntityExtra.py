from soft_exception import SoftException
from debug_utils import LOG_CURRENT_EXCEPTION

class EntityExtra(object):
    __slots__ = (b'name', b'index')

    def __init__(self, name, index, containerName, dataSection, **kwargs):
        self.name = name
        self.index = index
        self._readConfig(dataSection, containerName)
        return

    def prerequisites(self):
        return ()

    def startFor(self, entity, args=None):
        if entity.extras.has_key(self.index):
            raise SoftException(b"the extra '%s' is already started" % self.name)
        d = self._newData(entity)
        entity.extras[self.index] = d
        try:
            self._start(d, args)
        except Exception:
            if d[b'entity'] is not None:
                del entity.extras[self.index]
                try:
                    self._cleanup(d)
                except Exception:
                    LOG_CURRENT_EXCEPTION()

                d[b'entity'] = None
            raise

        return

    def stopFor(self, entity):
        data = entity.extras.pop(self.index, None)
        if data is None:
            return False
        else:
            try:
                self._cleanup(data)
            except Exception:
                LOG_CURRENT_EXCEPTION()

            data[b'entity'] = None
            return True

    def stop(self, data):
        if data[b'entity'] is None:
            return
        else:
            try:
                del data[b'entity'].extras[self.index]
                self._cleanup(data)
            except Exception:
                LOG_CURRENT_EXCEPTION()

            data[b'entity'] = None
            return

    def updateFor(self, entity, args):
        data = entity.extras.get(self.index)
        if data is None:
            return False
        else:
            self._update(data, args)
            return True

    def isRunningFor(self, entity):
        return self.index in entity.extras

    def _readConfig(self, dataSection, containerName):
        return

    def _start(self, data, args):
        self.stop(data)
        return

    def _update(self, data, args):
        return

    def _cleanup(self, data):
        return

    def _raiseWrongConfig(self, paramName, containerName):
        raise SoftException(b"missing or wrong parameter <%s> (entity extra '%s' in '%s')" % (
         paramName, self.name, containerName))
        return

    def _newData(self, entity):
        return {b'extra': self, 
           b'entity': entity}
