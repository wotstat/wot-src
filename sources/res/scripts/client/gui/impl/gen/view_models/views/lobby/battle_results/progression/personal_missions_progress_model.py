from enum import Enum
from gui.impl.gen.view_models.views.lobby.personal_missions_30.common.enums import MissionCategory
from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.common.missions.bonuses.icon_bonus_model import IconBonusModel
from gui.impl.gen.view_models.views.lobby.personal_missions_30.quest_model import QuestModel

class PM3Status(Enum):
    OPERATION_MISSION_PROGRESS = b'operation_mission_progress'
    OPERATION_MISSION_COMPLETE = b'operation_mission_complete'
    OPERATION_COMPLETED_WITH_HONOR = b'operation_completed_with_honor'
    CAMPAIGN_COMPLETED_WITH_HONOR = b'campaign_completed_with_honor'


class PersonalMissionsProgressModel(ViewModel):
    __slots__ = (b'onNavigate',)
    PATH = b'coui://gui/gameface/_dist/production/mono/plugins/personal_missions_30/post_battle/post_battle.js'

    def __init__(self, properties=9, commands=1):
        super(PersonalMissionsProgressModel, self).__init__(properties=properties, commands=commands)
        return

    def getMissionName(self):
        return self._getString(0)

    def setMissionName(self, value):
        self._setString(0, value)
        return

    def getMissionCategory(self):
        return MissionCategory(self._getString(1))

    def setMissionCategory(self, value):
        self._setString(1, value.value)
        return

    def getQuests(self):
        return self._getArray(2)

    def setQuests(self, value):
        self._setArray(2, value)
        return

    @staticmethod
    def getQuestsType():
        return QuestModel

    def getAllQuestsRequired(self):
        return self._getBool(3)

    def setAllQuestsRequired(self, value):
        self._setBool(3, value)
        return

    def getCurrentProgress(self):
        return self._getNumber(4)

    def setCurrentProgress(self, value):
        self._setNumber(4, value)
        return

    def getMaxProgress(self):
        return self._getNumber(5)

    def setMaxProgress(self, value):
        self._setNumber(5, value)
        return

    def getRewards(self):
        return self._getArray(6)

    def setRewards(self, value):
        self._setArray(6, value)
        return

    @staticmethod
    def getRewardsType():
        return IconBonusModel

    def getCurrentPM3Status(self):
        return PM3Status(self._getString(7))

    def setCurrentPM3Status(self, value):
        self._setString(7, value.value)
        return

    def getNavigationEnabled(self):
        return self._getBool(8)

    def setNavigationEnabled(self, value):
        self._setBool(8, value)
        return

    def _initialize(self):
        super(PersonalMissionsProgressModel, self)._initialize()
        self._addStringProperty(b'missionName', b'')
        self._addStringProperty(b'missionCategory')
        self._addArrayProperty(b'quests', Array())
        self._addBoolProperty(b'allQuestsRequired', False)
        self._addNumberProperty(b'currentProgress', 0)
        self._addNumberProperty(b'maxProgress', 0)
        self._addArrayProperty(b'rewards', Array())
        self._addStringProperty(b'currentPM3Status')
        self._addBoolProperty(b'navigationEnabled', False)
        self.onNavigate = self._addCommand(b'onNavigate')
        return
