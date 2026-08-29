from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.personal_missions.pm3_quest_item_part_progress_model import Pm3QuestItemPartProgressModel

class Pm3QuestItemPartModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=11, commands=0):
        super(Pm3QuestItemPartModel, self).__init__(properties=properties, commands=commands)
        return

    def getIdName(self):
        return self._getString(0)

    def setIdName(self, value):
        self._setString(0, value)
        return

    def getName(self):
        return self._getString(1)

    def setName(self, value):
        self._setString(1, value)
        return

    def getDescription(self):
        return self._getString(2)

    def setDescription(self, value):
        self._setString(2, value)
        return

    def getIcon(self):
        return self._getString(3)

    def setIcon(self, value):
        self._setString(3, value)
        return

    def getHeaderDescription(self):
        return self._getString(4)

    def setHeaderDescription(self, value):
        self._setString(4, value)
        return

    def getType(self):
        return self._getString(5)

    def setType(self, value):
        self._setString(5, value)
        return

    def getIsCycle(self):
        return self._getBool(6)

    def setIsCycle(self, value):
        self._setBool(6, value)
        return

    def getIsCumulative(self):
        return self._getBool(7)

    def setIsCumulative(self, value):
        self._setBool(7, value)
        return

    def getBiathlonGoal(self):
        return self._getNumber(8)

    def setBiathlonGoal(self, value):
        self._setNumber(8, value)
        return

    def getProgression(self):
        return self._getArray(9)

    def setProgression(self, value):
        self._setArray(9, value)
        return

    @staticmethod
    def getProgressionType():
        return Pm3QuestItemPartProgressModel

    def getQuestTooltipID(self):
        return self._getNumber(10)

    def setQuestTooltipID(self, value):
        self._setNumber(10, value)
        return

    def _initialize(self):
        super(Pm3QuestItemPartModel, self)._initialize()
        self._addStringProperty(b'idName', b'')
        self._addStringProperty(b'name', b'')
        self._addStringProperty(b'description', b'')
        self._addStringProperty(b'icon', b'')
        self._addStringProperty(b'headerDescription', b'')
        self._addStringProperty(b'type', b'')
        self._addBoolProperty(b'isCycle', False)
        self._addBoolProperty(b'isCumulative', False)
        self._addNumberProperty(b'biathlonGoal', 0)
        self._addArrayProperty(b'progression', Array())
        self._addNumberProperty(b'questTooltipID', 0)
        return
