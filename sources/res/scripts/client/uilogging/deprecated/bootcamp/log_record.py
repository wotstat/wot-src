from uilogging.core.log import LogRecord

class BootcampLogRecord(LogRecord):
    __slots__ = ()

    def __init__(self, *args, **kwargs):
        super(BootcampLogRecord, self).__init__(*args, **kwargs)
        if self._properties:
            self._properties.setdefault(b'is_newbie', None)
            self._properties.setdefault(b'lesson_id', None)
            self._properties.setdefault(b'finishReason', None)
            self._properties.setdefault(b'item_id', None)
            self._properties.setdefault(b'skipped', None)
            self._properties.setdefault(b'page', None)
            self._properties.setdefault(b'tooltip', None)
            intProperties = (b'lesson_id', b'item_id', b'page')
            for propertyName in intProperties:
                if propertyName in self._properties and self._properties[propertyName] is not None:
                    self._properties[propertyName] = int(self._properties[propertyName])

        return
