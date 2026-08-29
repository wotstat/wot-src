from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.common.missions.daily_quest_model import DailyQuestModel
from gui.impl.gen.view_models.views.lobby.missions.missions_completed_visited_model import MissionsCompletedVisitedModel

class DailyQuestsRegularModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=7, commands=0):
        super(DailyQuestsRegularModel, self).__init__(properties=properties, commands=commands)
        return

    def getIsEnabled(self):
        return self._getBool(0)

    def setIsEnabled(self, value):
        self._setBool(0, value)
        return

    def getQuests(self):
        return self._getArray(1)

    def setQuests(self, value):
        self._setArray(1, value)
        return

    @staticmethod
    def getQuestsType():
        return DailyQuestModel

    def getCountDown(self):
        return self._getNumber(2)

    def setCountDown(self, value):
        self._setNumber(2, value)
        return

    def getRerollEnabled(self):
        return self._getBool(3)

    def setRerollEnabled(self, value):
        self._setBool(3, value)
        return

    def getRerollCountDown(self):
        return self._getNumber(4)

    def setRerollCountDown(self, value):
        self._setNumber(4, value)
        return

    def getFirstSeenNewBonusMissions(self):
        return self._getBool(5)

    def setFirstSeenNewBonusMissions(self, value):
        self._setBool(5, value)
        return

    def getMissionsCompletedVisited(self):
        return self._getArray(6)

    def setMissionsCompletedVisited(self, value):
        self._setArray(6, value)
        return

    @staticmethod
    def getMissionsCompletedVisitedType():
        return MissionsCompletedVisitedModel

    def _initialize(self):
        super(DailyQuestsRegularModel, self)._initialize()
        self._addBoolProperty(b'isEnabled', False)
        self._addArrayProperty(b'quests', Array())
        self._addNumberProperty(b'countDown', 0)
        self._addBoolProperty(b'rerollEnabled', False)
        self._addNumberProperty(b'rerollCountDown', 0)
        self._addBoolProperty(b'firstSeenNewBonusMissions', False)
        self._addArrayProperty(b'missionsCompletedVisited', Array())
        return
