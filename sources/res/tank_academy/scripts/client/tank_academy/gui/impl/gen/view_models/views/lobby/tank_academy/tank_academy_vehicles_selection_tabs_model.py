from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from tank_academy.gui.impl.gen.view_models.views.lobby.tank_academy.quest_view_model import QuestViewModel

class TankAcademyVehiclesSelectionTabsModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=7, commands=0):
        super(TankAcademyVehiclesSelectionTabsModel, self).__init__(properties=properties, commands=commands)
        return

    def getLevel(self):
        return self._getNumber(0)

    def setLevel(self, value):
        self._setNumber(0, value)
        return

    def getIsSelected(self):
        return self._getBool(1)

    def setIsSelected(self, value):
        self._setBool(1, value)
        return

    def getIsNew(self):
        return self._getBool(2)

    def setIsNew(self, value):
        self._setBool(2, value)
        return

    def getIsDone(self):
        return self._getBool(3)

    def setIsDone(self, value):
        self._setBool(3, value)
        return

    def getIsPremium(self):
        return self._getBool(4)

    def setIsPremium(self, value):
        self._setBool(4, value)
        return

    def getTokensCount(self):
        return self._getNumber(5)

    def setTokensCount(self, value):
        self._setNumber(5, value)
        return

    def getTasks(self):
        return self._getArray(6)

    def setTasks(self, value):
        self._setArray(6, value)
        return

    @staticmethod
    def getTasksType():
        return QuestViewModel

    def _initialize(self):
        super(TankAcademyVehiclesSelectionTabsModel, self)._initialize()
        self._addNumberProperty(b'level', 0)
        self._addBoolProperty(b'isSelected', False)
        self._addBoolProperty(b'isNew', False)
        self._addBoolProperty(b'isDone', False)
        self._addBoolProperty(b'isPremium', False)
        self._addNumberProperty(b'tokensCount', 0)
        self._addArrayProperty(b'tasks', Array())
        return
