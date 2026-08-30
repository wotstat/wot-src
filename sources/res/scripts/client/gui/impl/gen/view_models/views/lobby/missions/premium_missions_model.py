from frameworks.wulf import Array
from gui.impl.gen import R
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.common.missions.premium_mission_model import PremiumMissionModel
from gui.impl.gen.view_models.views.lobby.missions.missions_completed_visited_model import MissionsCompletedVisitedModel

class PremiumMissionsModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=6, commands=0):
        super(PremiumMissionsModel, self).__init__(properties=properties, commands=commands)
        return

    def getIsPremiumAccount(self):
        return self._getBool(0)

    def setIsPremiumAccount(self, value):
        self._setBool(0, value)
        return

    def getIsEnabled(self):
        return self._getBool(1)

    def setIsEnabled(self, value):
        self._setBool(1, value)
        return

    def getTitle(self):
        return self._getResource(2)

    def setTitle(self, value):
        self._setResource(2, value)
        return

    def getMissions(self):
        return self._getArray(3)

    def setMissions(self, value):
        self._setArray(3, value)
        return

    @staticmethod
    def getMissionsType():
        return PremiumMissionModel

    def getMissionsCompletedVisited(self):
        return self._getArray(4)

    def setMissionsCompletedVisited(self, value):
        self._setArray(4, value)
        return

    @staticmethod
    def getMissionsCompletedVisitedType():
        return MissionsCompletedVisitedModel

    def getSyncInitiator(self):
        return self._getNumber(5)

    def setSyncInitiator(self, value):
        self._setNumber(5, value)
        return

    def _initialize(self):
        super(PremiumMissionsModel, self)._initialize()
        self._addBoolProperty(b'isPremiumAccount', False)
        self._addBoolProperty(b'isEnabled', False)
        self._addResourceProperty(b'title', R.invalid())
        self._addArrayProperty(b'missions', Array())
        self._addArrayProperty(b'missionsCompletedVisited', Array())
        self._addNumberProperty(b'syncInitiator', 0)
        return
