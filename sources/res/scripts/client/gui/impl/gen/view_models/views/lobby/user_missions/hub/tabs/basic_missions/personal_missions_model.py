from enum import Enum
from frameworks.wulf import ViewModel

class State(Enum):
    CAMPAIGN_NOT_ACTIVATED = b'campaignNotActivated'
    IN_PROGRESS = b'inProgress'
    IN_PROGRESS_FOR_HONORS = b'inProgressForHonors'
    COMPLETED = b'completed'
    COMPLETED_WITH_HONORS = b'completedWithHonors'


class PersonalMissionsModel(ViewModel):
    __slots__ = (b'goToCampaigns', b'goToOperation')

    def __init__(self, properties=13, commands=2):
        super(PersonalMissionsModel, self).__init__(properties=properties, commands=commands)
        return

    def getState(self):
        return State(self._getString(0))

    def setState(self, value):
        self._setString(0, value.value)
        return

    def getAllOperationsCompleted(self):
        return self._getBool(1)

    def setAllOperationsCompleted(self, value):
        self._setBool(1, value)
        return

    def getCampaignName(self):
        return self._getString(2)

    def setCampaignName(self, value):
        self._setString(2, value)
        return

    def getCurrentOperationName(self):
        return self._getString(3)

    def setCurrentOperationName(self, value):
        self._setString(3, value)
        return

    def getCurrentOperationId(self):
        return self._getNumber(4)

    def setCurrentOperationId(self, value):
        self._setNumber(4, value)
        return

    def getNextOperationName(self):
        return self._getString(5)

    def setNextOperationName(self, value):
        self._setString(5, value)
        return

    def getNextOperationId(self):
        return self._getNumber(6)

    def setNextOperationId(self, value):
        self._setNumber(6, value)
        return

    def getStageNumber(self):
        return self._getNumber(7)

    def setStageNumber(self, value):
        self._setNumber(7, value)
        return

    def getDetailId(self):
        return self._getString(8)

    def setDetailId(self, value):
        self._setString(8, value)
        return

    def getVehicleName(self):
        return self._getString(9)

    def setVehicleName(self, value):
        self._setString(9, value)
        return

    def getPreviousProgress(self):
        return self._getNumber(10)

    def setPreviousProgress(self, value):
        self._setNumber(10, value)
        return

    def getCurrentProgress(self):
        return self._getNumber(11)

    def setCurrentProgress(self, value):
        self._setNumber(11, value)
        return

    def getTotalProgress(self):
        return self._getNumber(12)

    def setTotalProgress(self, value):
        self._setNumber(12, value)
        return

    def _initialize(self):
        super(PersonalMissionsModel, self)._initialize()
        self._addStringProperty(b'state')
        self._addBoolProperty(b'allOperationsCompleted', False)
        self._addStringProperty(b'campaignName', b'')
        self._addStringProperty(b'currentOperationName', b'')
        self._addNumberProperty(b'currentOperationId', 0)
        self._addStringProperty(b'nextOperationName', b'')
        self._addNumberProperty(b'nextOperationId', 0)
        self._addNumberProperty(b'stageNumber', 0)
        self._addStringProperty(b'detailId', b'')
        self._addStringProperty(b'vehicleName', b'')
        self._addNumberProperty(b'previousProgress', 0)
        self._addNumberProperty(b'currentProgress', 0)
        self._addNumberProperty(b'totalProgress', 0)
        self.goToCampaigns = self._addCommand(b'goToCampaigns')
        self.goToOperation = self._addCommand(b'goToOperation')
        return
