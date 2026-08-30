from enum import Enum
from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.personal_missions.tooltips.pm3_operations_tooltip_branches_model import Pm3OperationsTooltipBranchesModel
from gui.impl.gen.view_models.views.lobby.personal_missions.tooltips.pm3_operations_tooltip_rewards_model import Pm3OperationsTooltipRewardsModel

class MissionStatus(Enum):
    AVAILABLE = b'available'
    ACTIVE = b'active'
    DISABLED = b'disabled'
    COMPLETED = b'completed'
    COMPLETEDPERFECTLY = b'completedPerfectly'
    DISABLEDLEVEL = b'disabledLevel'


class PersonalMissionsOperationsTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=8, commands=0):
        super(PersonalMissionsOperationsTooltipModel, self).__init__(properties=properties, commands=commands)
        return

    def getMissionStatus(self):
        return MissionStatus(self._getString(0))

    def setMissionStatus(self, value):
        self._setString(0, value.value)
        return

    def getOperationID(self):
        return self._getNumber(1)

    def setOperationID(self, value):
        self._setNumber(1, value)
        return

    def getName(self):
        return self._getString(2)

    def setName(self, value):
        self._setString(2, value)
        return

    def getFrom(self):
        return self._getString(3)

    def setFrom(self, value):
        self._setString(3, value)
        return

    def getPrevOperationName(self):
        return self._getString(4)

    def setPrevOperationName(self, value):
        self._setString(4, value)
        return

    def getTo(self):
        return self._getString(5)

    def setTo(self, value):
        self._setString(5, value)
        return

    def getBranches(self):
        return self._getArray(6)

    def setBranches(self, value):
        self._setArray(6, value)
        return

    @staticmethod
    def getBranchesType():
        return Pm3OperationsTooltipBranchesModel

    def getRewards(self):
        return self._getArray(7)

    def setRewards(self, value):
        self._setArray(7, value)
        return

    @staticmethod
    def getRewardsType():
        return Pm3OperationsTooltipRewardsModel

    def _initialize(self):
        super(PersonalMissionsOperationsTooltipModel, self)._initialize()
        self._addStringProperty(b'missionStatus')
        self._addNumberProperty(b'operationID', 0)
        self._addStringProperty(b'name', b'')
        self._addStringProperty(b'from', b'')
        self._addStringProperty(b'prevOperationName', b'')
        self._addStringProperty(b'to', b'')
        self._addArrayProperty(b'branches', Array())
        self._addArrayProperty(b'rewards', Array())
        return
