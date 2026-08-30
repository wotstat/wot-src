from enum import Enum
from gui.impl.gen.view_models.views.lobby.personal_missions_30.common.enums import MissionCategory
from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.common.missions.bonuses.icon_bonus_model import IconBonusModel
from gui.impl.gen.view_models.views.lobby.personal_missions_30.quest_model import QuestModel

class MissionStatus(Enum):
    ACTIVE = b'active'
    DISABLED = b'disabled'
    COMPLETED = b'completed'
    LOCKED = b'locked'


class MissionModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=10, commands=0):
        super(MissionModel, self).__init__(properties=properties, commands=commands)
        return

    def getRewards(self):
        return self._getArray(0)

    def setRewards(self, value):
        self._setArray(0, value)
        return

    @staticmethod
    def getRewardsType():
        return IconBonusModel

    def getQuests(self):
        return self._getArray(1)

    def setQuests(self, value):
        self._setArray(1, value)
        return

    @staticmethod
    def getQuestsType():
        return QuestModel

    def getCurrentMissionNumber(self):
        return self._getNumber(2)

    def setCurrentMissionNumber(self, value):
        self._setNumber(2, value)
        return

    def getOperationId(self):
        return self._getNumber(3)

    def setOperationId(self, value):
        self._setNumber(3, value)
        return

    def getMaxMissions(self):
        return self._getNumber(4)

    def setMaxMissions(self, value):
        self._setNumber(4, value)
        return

    def getMissionStatus(self):
        return MissionStatus(self._getString(5))

    def setMissionStatus(self, value):
        self._setString(5, value.value)
        return

    def getMissionCategory(self):
        return MissionCategory(self._getString(6))

    def setMissionCategory(self, value):
        self._setString(6, value.value)
        return

    def getCurrentProgressValue(self):
        return self._getNumber(7)

    def setCurrentProgressValue(self, value):
        self._setNumber(7, value)
        return

    def getMaxProgressValue(self):
        return self._getNumber(8)

    def setMaxProgressValue(self, value):
        self._setNumber(8, value)
        return

    def getAllQuestsRequired(self):
        return self._getBool(9)

    def setAllQuestsRequired(self, value):
        self._setBool(9, value)
        return

    def _initialize(self):
        super(MissionModel, self)._initialize()
        self._addArrayProperty(b'rewards', Array())
        self._addArrayProperty(b'quests', Array())
        self._addNumberProperty(b'currentMissionNumber', 0)
        self._addNumberProperty(b'operationId', 0)
        self._addNumberProperty(b'maxMissions', 0)
        self._addStringProperty(b'missionStatus')
        self._addStringProperty(b'missionCategory')
        self._addNumberProperty(b'currentProgressValue', 0)
        self._addNumberProperty(b'maxProgressValue', 0)
        self._addBoolProperty(b'allQuestsRequired', False)
        return
