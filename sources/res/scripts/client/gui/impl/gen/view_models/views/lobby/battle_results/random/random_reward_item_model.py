from enum import Enum
from gui.impl.gen.view_models.views.lobby.battle_results.reward_item_model import RewardItemModel

class RandomRewardTypes(Enum):
    CREDITS = b'credits'
    GOLD = b'gold'
    CRYSTALS = b'crystal'
    XP = b'xp'


class RandomRewardItemModel(RewardItemModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(RandomRewardItemModel, self).__init__(properties=properties, commands=commands)
        return

    def _initialize(self):
        super(RandomRewardItemModel, self)._initialize()
        return
