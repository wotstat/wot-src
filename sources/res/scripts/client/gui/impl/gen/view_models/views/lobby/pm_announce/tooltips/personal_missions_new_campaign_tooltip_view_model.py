from enum import Enum
from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.pm_announce.tooltips.personal_missions_old_campaign_tooltip_operations_model import PersonalMissionsOldCampaignTooltipOperationsModel
from gui.impl.gen.view_models.views.lobby.pm_announce.tooltips.personal_missions_old_campaign_tooltip_rewards_model import PersonalMissionsOldCampaignTooltipRewardsModel

class MissionStatus(Enum):
    ACTIVE = b'active'
    COMPLETED = b'completed'
    COMPLETEDPERFECT = b'completedPerfect'
    DISABLED = b'disabled'


class PersonalMissionsNewCampaignTooltipViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(PersonalMissionsNewCampaignTooltipViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getMissionStatus(self):
        return MissionStatus(self._getString(0))

    def setMissionStatus(self, value):
        self._setString(0, value.value)
        return

    def getOperations(self):
        return self._getArray(1)

    def setOperations(self, value):
        self._setArray(1, value)
        return

    @staticmethod
    def getOperationsType():
        return PersonalMissionsOldCampaignTooltipOperationsModel

    def getRewards(self):
        return self._getArray(2)

    def setRewards(self, value):
        self._setArray(2, value)
        return

    @staticmethod
    def getRewardsType():
        return PersonalMissionsOldCampaignTooltipRewardsModel

    def _initialize(self):
        super(PersonalMissionsNewCampaignTooltipViewModel, self)._initialize()
        self._addStringProperty(b'missionStatus')
        self._addArrayProperty(b'operations', Array())
        self._addArrayProperty(b'rewards', Array())
        return
