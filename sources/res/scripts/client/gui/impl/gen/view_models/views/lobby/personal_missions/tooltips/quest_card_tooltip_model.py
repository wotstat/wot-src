from enum import Enum
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.personal_missions.pm3_quest_model import Pm3QuestModel

class QuestState(Enum):
    NAPREVIOUS = b'previousProgress'
    NAPREVIOUSALL = b'previousProgressAll'
    NATECH = b'noTech'
    AVAILABLE = b'available'
    INPROGRESS = b'inProgress'
    INPROGRESSHONOR = b'inProgressHonor'
    DONE = b'done'
    DONEBASIC = b'doneBasic'
    DONEHONOR = b'doneHonor'
    DONEPAUSE = b'donePause'
    PAUSE = b'pause'


class DescriptionQuestStatus(Enum):
    NOTAVAILABLENOVEHICLE = b'notAvailableNoVehicle'
    NOTAVAILABLESWITCH = b'notAvailableSwitch'
    NOTAVAILABLEPREVQUESTNOTCOMPLETED = b'notAvailablePrevQuestNotCompleted'
    NOTAVAILABLEPREVOPERATIONNOTCOMPLETED = b'notAvailablePrevOperationNotCompleted'
    AVAILABLE = b'available'
    INPROGRESS = b'inProgress'
    DONE = b'done'
    DONEH = b'doneHonor'


class QuestCardTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=9, commands=0):
        super(QuestCardTooltipModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def questData(self):
        return self._getViewModel(0)

    @staticmethod
    def getQuestDataType():
        return Pm3QuestModel

    def getId(self):
        return self._getNumber(1)

    def setId(self, value):
        self._setNumber(1, value)
        return

    def getName(self):
        return self._getString(2)

    def setName(self, value):
        self._setString(2, value)
        return

    def getIsFinal(self):
        return self._getBool(3)

    def setIsFinal(self, value):
        self._setBool(3, value)
        return

    def getStatus(self):
        return QuestState(self._getString(4))

    def setStatus(self, value):
        self._setString(4, value.value)
        return

    def getDescriptionStatus(self):
        return DescriptionQuestStatus(self._getString(5))

    def setDescriptionStatus(self, value):
        self._setString(5, value.value)
        return

    def getMinVehicleLevel(self):
        return self._getNumber(6)

    def setMinVehicleLevel(self, value):
        self._setNumber(6, value)
        return

    def getMaxVehicleLevel(self):
        return self._getNumber(7)

    def setMaxVehicleLevel(self, value):
        self._setNumber(7, value)
        return

    def getPrevOperationName(self):
        return self._getString(8)

    def setPrevOperationName(self, value):
        self._setString(8, value)
        return

    def _initialize(self):
        super(QuestCardTooltipModel, self)._initialize()
        self._addViewModelProperty(b'questData', Pm3QuestModel())
        self._addNumberProperty(b'id', 0)
        self._addStringProperty(b'name', b'')
        self._addBoolProperty(b'isFinal', False)
        self._addStringProperty(b'status')
        self._addStringProperty(b'descriptionStatus')
        self._addNumberProperty(b'minVehicleLevel', 0)
        self._addNumberProperty(b'maxVehicleLevel', 0)
        self._addStringProperty(b'prevOperationName', b'')
        return
