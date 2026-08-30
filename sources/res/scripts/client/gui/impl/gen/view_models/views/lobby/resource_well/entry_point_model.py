from enum import IntEnum
from frameworks.wulf import ViewModel

class EventState(IntEnum):
    ACTIVE = 0
    FORBIDDEN = 1
    PAUSED = 2
    COMPLETED = 3
    NOTSTARTED = 4
    SOLDOUT = 5


class EntryPointModel(ViewModel):
    __slots__ = (b'showProgression',)

    def __init__(self, properties=4, commands=1):
        super(EntryPointModel, self).__init__(properties=properties, commands=commands)
        return

    def getProgress(self):
        return self._getNumber(0)

    def setProgress(self, value):
        self._setNumber(0, value)
        return

    def getEventState(self):
        return EventState(self._getNumber(1))

    def setEventState(self, value):
        self._setNumber(1, value.value)
        return

    def getPrevProgress(self):
        return self._getNumber(2)

    def setPrevProgress(self, value):
        self._setNumber(2, value)
        return

    def getPrevEventState(self):
        return EventState(self._getNumber(3))

    def setPrevEventState(self, value):
        self._setNumber(3, value.value)
        return

    def _initialize(self):
        super(EntryPointModel, self)._initialize()
        self._addNumberProperty(b'progress', 0)
        self._addNumberProperty(b'eventState')
        self._addNumberProperty(b'prevProgress', 0)
        self._addNumberProperty(b'prevEventState')
        self.showProgression = self._addCommand(b'showProgression')
        return
