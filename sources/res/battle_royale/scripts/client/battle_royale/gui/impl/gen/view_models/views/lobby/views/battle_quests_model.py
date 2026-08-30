from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.common.missions.quest_model import QuestModel

class BattleQuestsModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=5, commands=0):
        super(BattleQuestsModel, self).__init__(properties=properties, commands=commands)
        return

    def getTasksBattle(self):
        return self._getArray(0)

    def setTasksBattle(self, value):
        self._setArray(0, value)
        return

    @staticmethod
    def getTasksBattleType():
        return QuestModel

    def getCurrentTimerDate(self):
        return self._getNumber(1)

    def setCurrentTimerDate(self, value):
        self._setNumber(1, value)
        return

    def getShowPrimeTime(self):
        return self._getBool(2)

    def setShowPrimeTime(self, value):
        self._setBool(2, value)
        return

    def getShowEventEnded(self):
        return self._getBool(3)

    def setShowEventEnded(self, value):
        self._setBool(3, value)
        return

    def getMissionsCompletedVisited(self):
        return self._getArray(4)

    def setMissionsCompletedVisited(self, value):
        self._setArray(4, value)
        return

    def _initialize(self):
        super(BattleQuestsModel, self)._initialize()
        self._addArrayProperty(b'tasksBattle', Array())
        self._addNumberProperty(b'currentTimerDate', 0)
        self._addBoolProperty(b'showPrimeTime', False)
        self._addBoolProperty(b'showEventEnded', False)
        self._addArrayProperty(b'missionsCompletedVisited', Array())
        return
