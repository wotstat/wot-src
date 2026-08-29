from frameworks.wulf import Array
from gui.impl.gen import R
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.common.missions.daily_quest_model import DailyQuestModel
from gui.impl.gen.view_models.views.lobby.missions.missions_completed_visited_model import MissionsCompletedVisitedModel

class DailyQuestsModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=10, commands=0):
        super(DailyQuestsModel, self).__init__(properties=properties, commands=commands)
        return

    def getTitle(self):
        return self._getResource(0)

    def setTitle(self, value):
        self._setResource(0, value)
        return

    def getQuests(self):
        return self._getArray(1)

    def setQuests(self, value):
        self._setArray(1, value)
        return

    @staticmethod
    def getQuestsType():
        return DailyQuestModel

    def getIsEnabled(self):
        return self._getBool(2)

    def setIsEnabled(self, value):
        self._setBool(2, value)
        return

    def getHasPremium(self):
        return self._getBool(3)

    def setHasPremium(self, value):
        self._setBool(3, value)
        return

    def getRerollEnabled(self):
        return self._getBool(4)

    def setRerollEnabled(self, value):
        self._setBool(4, value)
        return

    def getRerollCountDown(self):
        return self._getNumber(5)

    def setRerollCountDown(self, value):
        self._setNumber(5, value)
        return

    def getRerollTimeout(self):
        return self._getNumber(6)

    def setRerollTimeout(self, value):
        self._setNumber(6, value)
        return

    def getBonusMissionVisited(self):
        return self._getBool(7)

    def setBonusMissionVisited(self, value):
        self._setBool(7, value)
        return

    def getMissionsCompletedVisited(self):
        return self._getArray(8)

    def setMissionsCompletedVisited(self, value):
        self._setArray(8, value)
        return

    @staticmethod
    def getMissionsCompletedVisitedType():
        return MissionsCompletedVisitedModel

    def getSyncInitiator(self):
        return self._getNumber(9)

    def setSyncInitiator(self, value):
        self._setNumber(9, value)
        return

    def _initialize(self):
        super(DailyQuestsModel, self)._initialize()
        self._addResourceProperty(b'title', R.invalid())
        self._addArrayProperty(b'quests', Array())
        self._addBoolProperty(b'isEnabled', False)
        self._addBoolProperty(b'hasPremium', False)
        self._addBoolProperty(b'rerollEnabled', False)
        self._addNumberProperty(b'rerollCountDown', 0)
        self._addNumberProperty(b'rerollTimeout', 0)
        self._addBoolProperty(b'bonusMissionVisited', False)
        self._addArrayProperty(b'missionsCompletedVisited', Array())
        self._addNumberProperty(b'syncInitiator', 0)
        return
