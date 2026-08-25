from enum import Enum
from frameworks.wulf import ViewModel

class ProgressionState(Enum):
    INPROGRESS = b'inProgress'
    COMPLETED = b'completed'


class EntryPointModel(ViewModel):
    __slots__ = (b'onOpenProgression', b'onAnimationEnd', b'onEntryPointAnimationSeen')

    def __init__(self, properties=6, commands=3):
        super(EntryPointModel, self).__init__(properties=properties, commands=commands)
        return

    def getState(self):
        return ProgressionState(self._getString(0))

    def setState(self, value):
        self._setString(0, value.value)
        return

    def getCurProgressPoints(self):
        return self._getNumber(1)

    def setCurProgressPoints(self, value):
        self._setNumber(1, value)
        return

    def getPrevProgressPoints(self):
        return self._getNumber(2)

    def setPrevProgressPoints(self, value):
        self._setNumber(2, value)
        return

    def getPointsForLevel(self):
        return self._getNumber(3)

    def setPointsForLevel(self, value):
        self._setNumber(3, value)
        return

    def getCurrentStage(self):
        return self._getNumber(4)

    def setCurrentStage(self, value):
        self._setNumber(4, value)
        return

    def getIsEntryPointAnimationSeen(self):
        return self._getBool(5)

    def setIsEntryPointAnimationSeen(self, value):
        self._setBool(5, value)
        return

    def _initialize(self):
        super(EntryPointModel, self)._initialize()
        self._addStringProperty(b'state')
        self._addNumberProperty(b'curProgressPoints', 0)
        self._addNumberProperty(b'prevProgressPoints', 0)
        self._addNumberProperty(b'pointsForLevel', 0)
        self._addNumberProperty(b'currentStage', 0)
        self._addBoolProperty(b'isEntryPointAnimationSeen', False)
        self.onOpenProgression = self._addCommand(b'onOpenProgression')
        self.onAnimationEnd = self._addCommand(b'onAnimationEnd')
        self.onEntryPointAnimationSeen = self._addCommand(b'onEntryPointAnimationSeen')
        return
