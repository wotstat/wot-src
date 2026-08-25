from enum import Enum
from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.views.lobby.prestige.prestige_emblem_model import PrestigeEmblemModel
from gui.impl.gen.view_models.views.lobby.vehicle_hub.views.sub_models.veh_skill_tree.rewards_slot_model import RewardsSlotModel

class PrestigeState(Enum):
    AVAILABLE = b'available'
    COMPLETED = b'completed'
    DISABLED = b'disabled'


class PrestigeViewModel(ViewModel):
    __slots__ = (b'onPreview',)

    def __init__(self, properties=3, commands=1):
        super(PrestigeViewModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def prestigeEmblem(self):
        return self._getViewModel(0)

    @staticmethod
    def getPrestigeEmblemType():
        return PrestigeEmblemModel

    def getRewards(self):
        return self._getArray(1)

    def setRewards(self, value):
        self._setArray(1, value)
        return

    @staticmethod
    def getRewardsType():
        return RewardsSlotModel

    def getPrestigeState(self):
        return PrestigeState(self._getString(2))

    def setPrestigeState(self, value):
        self._setString(2, value.value)
        return

    def _initialize(self):
        super(PrestigeViewModel, self)._initialize()
        self._addViewModelProperty(b'prestigeEmblem', PrestigeEmblemModel())
        self._addArrayProperty(b'rewards', Array())
        self._addStringProperty(b'prestigeState')
        self.onPreview = self._addCommand(b'onPreview')
        return
