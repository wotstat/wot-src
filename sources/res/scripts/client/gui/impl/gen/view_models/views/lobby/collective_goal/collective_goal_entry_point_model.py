from enum import Enum
from frameworks.wulf import ViewModel

class EventState(Enum):
    ACTIVE = b'active'
    FORBIDDEN = b'forbidden'
    NOTSTARTED = b'notStarted'
    FINISHED = b'finished'


class CollectiveGoalEntryPointModel(ViewModel):
    __slots__ = (b'showProgression',)

    def __init__(self, properties=6, commands=1):
        super(CollectiveGoalEntryPointModel, self).__init__(properties=properties, commands=commands)
        return

    def getProgress(self):
        return self._getNumber(0)

    def setProgress(self, value):
        self._setNumber(0, value)
        return

    def getCurrentGoal(self):
        return self._getNumber(1)

    def setCurrentGoal(self, value):
        self._setNumber(1, value)
        return

    def getEventState(self):
        return EventState(self._getString(2))

    def setEventState(self, value):
        self._setString(2, value.value)
        return

    def getPrevProgress(self):
        return self._getNumber(3)

    def setPrevProgress(self, value):
        self._setNumber(3, value)
        return

    def getPrevEventState(self):
        return EventState(self._getString(4))

    def setPrevEventState(self, value):
        self._setString(4, value.value)
        return

    def getStartDate(self):
        return self._getNumber(5)

    def setStartDate(self, value):
        self._setNumber(5, value)
        return

    def _initialize(self):
        super(CollectiveGoalEntryPointModel, self)._initialize()
        self._addNumberProperty(b'progress', 0)
        self._addNumberProperty(b'currentGoal', 0)
        self._addStringProperty(b'eventState')
        self._addNumberProperty(b'prevProgress', 0)
        self._addStringProperty(b'prevEventState')
        self._addNumberProperty(b'startDate', 0)
        self.showProgression = self._addCommand(b'showProgression')
        return
