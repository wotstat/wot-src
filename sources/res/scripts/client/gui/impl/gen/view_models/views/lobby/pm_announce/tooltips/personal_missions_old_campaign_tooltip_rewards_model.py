from enum import Enum
from frameworks.wulf import ViewModel

class RewardStatus(Enum):
    COMPLETED = b'completed'
    AVAILABLE = b'available'
    LOCKED = b'locked'


class PersonalMissionsOldCampaignTooltipRewardsModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(PersonalMissionsOldCampaignTooltipRewardsModel, self).__init__(properties=properties, commands=commands)
        return

    def getName(self):
        return self._getString(0)

    def setName(self, value):
        self._setString(0, value)
        return

    def getIcon(self):
        return self._getString(1)

    def setIcon(self, value):
        self._setString(1, value)
        return

    def getStatus(self):
        return RewardStatus(self._getString(2))

    def setStatus(self, value):
        self._setString(2, value.value)
        return

    def _initialize(self):
        super(PersonalMissionsOldCampaignTooltipRewardsModel, self)._initialize()
        self._addStringProperty(b'name', b'')
        self._addStringProperty(b'icon', b'')
        self._addStringProperty(b'status')
        return
