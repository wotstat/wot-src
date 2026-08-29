from enum import Enum
from frameworks.wulf import ViewModel

class CardState(Enum):
    SWITCH = b'switch'
    NOTAVAILABLE = b'notAvailable'
    AVAILABLE = b'available'
    PAUSE = b'pause'
    INPROGRESS = b'inProgress'
    INPROGRESSHONOR = b'inProgressHonor'
    DONES = b'doneSwitch'
    DONE = b'done'
    DONEP = b'donePause'
    DONEH = b'doneHonor'


class AnimationCardState(Enum):
    COMPLETEBASIC = b'completeBasic'
    COMPLETE = b'complete'
    COMPLETEHONOR = b'completeHonor'
    INPROGRESS = b'inProgress'
    INPROGRESSHONOR = b'inProgressHonor'
    ONPAUSE = b'isOnPause'
    UNLOCK = b'unlock'
    UNLOCKINPROGRESS = b'unlockInProgress'
    SWITCHHONORPROGRESS = b'switchHonorProgress'
    SWITCHHONORPAUSE = b'switchHonorPause'
    SWITCHPAUSE = b'switchPause'
    SWITCHPROGRESS = b'switchProgress'
    LOCKED = b'locked'
    DEFAULT = b'default'
    SWITCHCOMPLETEINPROGRESS = b'switchCompleteInProgress'
    SWITCHINPROGRESSCOMPLETE = b'switchInProgressComplete'


class Pm3QuestsCardModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=7, commands=0):
        super(Pm3QuestsCardModel, self).__init__(properties=properties, commands=commands)
        return

    def getId(self):
        return self._getNumber(0)

    def setId(self, value):
        self._setNumber(0, value)
        return

    def getType(self):
        return CardState(self._getString(1))

    def setType(self, value):
        self._setString(1, value.value)
        return

    def getAnimationType(self):
        return AnimationCardState(self._getString(2))

    def setAnimationType(self, value):
        self._setString(2, value.value)
        return

    def getSelectionAvailable(self):
        return self._getBool(3)

    def setSelectionAvailable(self, value):
        self._setBool(3, value)
        return

    def getSelected(self):
        return self._getBool(4)

    def setSelected(self, value):
        self._setBool(4, value)
        return

    def getIsLast(self):
        return self._getBool(5)

    def setIsLast(self, value):
        self._setBool(5, value)
        return

    def getQuestName(self):
        return self._getString(6)

    def setQuestName(self, value):
        self._setString(6, value)
        return

    def _initialize(self):
        super(Pm3QuestsCardModel, self)._initialize()
        self._addNumberProperty(b'id', 0)
        self._addStringProperty(b'type')
        self._addStringProperty(b'animationType')
        self._addBoolProperty(b'selectionAvailable', False)
        self._addBoolProperty(b'selected', False)
        self._addBoolProperty(b'isLast', False)
        self._addStringProperty(b'questName', b'')
        return
