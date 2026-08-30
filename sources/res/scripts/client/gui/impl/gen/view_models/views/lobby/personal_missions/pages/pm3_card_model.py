from enum import Enum
from frameworks.wulf import ViewModel

class SmallCardState(Enum):
    SWITCH = b'switch'
    NOTAVAILABLE = b'notAvailable'
    AVAILABLE = b'available'
    PAUSE = b'pause'
    INPROGRESS = b'inProgress'
    DONES = b'doneSwitch'
    DONE = b'done'
    DONEP = b'donePause'
    DONEH = b'doneHonor'


class Pm3CardModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=5, commands=0):
        super(Pm3CardModel, self).__init__(properties=properties, commands=commands)
        return

    def getQuestId(self):
        return self._getNumber(0)

    def setQuestId(self, value):
        self._setNumber(0, value)
        return

    def getState(self):
        return SmallCardState(self._getString(1))

    def setState(self, value):
        self._setString(1, value.value)
        return

    def getIsSelected(self):
        return self._getBool(2)

    def setIsSelected(self, value):
        self._setBool(2, value)
        return

    def getIsLast(self):
        return self._getBool(3)

    def setIsLast(self, value):
        self._setBool(3, value)
        return

    def getQuestName(self):
        return self._getString(4)

    def setQuestName(self, value):
        self._setString(4, value)
        return

    def _initialize(self):
        super(Pm3CardModel, self)._initialize()
        self._addNumberProperty(b'questId', 0)
        self._addStringProperty(b'state')
        self._addBoolProperty(b'isSelected', False)
        self._addBoolProperty(b'isLast', False)
        self._addStringProperty(b'questName', b'')
        return
