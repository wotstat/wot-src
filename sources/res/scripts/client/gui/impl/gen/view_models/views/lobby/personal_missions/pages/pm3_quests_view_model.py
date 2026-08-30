from enum import Enum
from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.personal_missions.pages.pm3_quests_line_model import Pm3QuestsLineModel
from gui.impl.gen.view_models.views.lobby.personal_missions.pages.pm3_quests_page_tab_model import Pm3QuestsPageTabModel

class OperationState(Enum):
    LOCKED = b'locked'
    LOCKEDNOVEHICLE = b'lockedNoVehicle'
    ACTIVE = b'active'
    ALERT = b'alert'
    COMPLETEWITHHONOR = b'completeWithHonor'
    COMPLETE = b'complete'


class CardState(Enum):
    SWITCH = b'switch'
    NOTAVAILABLE = b'notAvailable'
    AVAILABLE = b'available'
    PAUSE = b'pause'
    INPROGRESS = b'inProgress'
    DONES = b'doneSwitch'
    DONE = b'done'
    DONEP = b'donePause'
    DONEH = b'doneHonor'


class Pm3QuestsViewModel(ViewModel):
    __slots__ = (b'switchTab', b'backToOperation', b'openVehicleViewWindow')

    def __init__(self, properties=9, commands=3):
        super(Pm3QuestsViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getQuestsLines(self):
        return self._getArray(0)

    def setQuestsLines(self, value):
        self._setArray(0, value)
        return

    @staticmethod
    def getQuestsLinesType():
        return Pm3QuestsLineModel

    def getState(self):
        return OperationState(self._getString(1))

    def setState(self, value):
        self._setString(1, value.value)
        return

    def getOperationName(self):
        return self._getString(2)

    def setOperationName(self, value):
        self._setString(2, value)
        return

    def getOperationId(self):
        return self._getNumber(3)

    def setOperationId(self, value):
        self._setNumber(3, value)
        return

    def getMinVehicleLevel(self):
        return self._getNumber(4)

    def setMinVehicleLevel(self, value):
        self._setNumber(4, value)
        return

    def getMaxVehicleLevel(self):
        return self._getNumber(5)

    def setMaxVehicleLevel(self, value):
        self._setNumber(5, value)
        return

    def getPrevOperationName(self):
        return self._getString(6)

    def setPrevOperationName(self, value):
        self._setString(6, value)
        return

    def getIsSwitched(self):
        return self._getBool(7)

    def setIsSwitched(self, value):
        self._setBool(7, value)
        return

    def getTabs(self):
        return self._getArray(8)

    def setTabs(self, value):
        self._setArray(8, value)
        return

    @staticmethod
    def getTabsType():
        return Pm3QuestsPageTabModel

    def _initialize(self):
        super(Pm3QuestsViewModel, self)._initialize()
        self._addArrayProperty(b'questsLines', Array())
        self._addStringProperty(b'state')
        self._addStringProperty(b'operationName', b'')
        self._addNumberProperty(b'operationId', 0)
        self._addNumberProperty(b'minVehicleLevel', 0)
        self._addNumberProperty(b'maxVehicleLevel', 0)
        self._addStringProperty(b'prevOperationName', b'')
        self._addBoolProperty(b'isSwitched', False)
        self._addArrayProperty(b'tabs', Array())
        self.switchTab = self._addCommand(b'switchTab')
        self.backToOperation = self._addCommand(b'backToOperation')
        self.openVehicleViewWindow = self._addCommand(b'openVehicleViewWindow')
        return
