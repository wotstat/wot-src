from enum import Enum
from gui.impl.gen.view_models.views.lobby.battle_results.reward_item_model import RewardItemModel

class FunRewardTypes(Enum):
    CREDITS = b'credits'
    GOLD = b'gold'
    CRYSTALS = b'crystal'
    XP = b'xp'
    FREE_XP = b'freeXP'
    TANKMEN_XP = b'tankmenXP'


class FunRandomRewardItemModel(RewardItemModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(FunRandomRewardItemModel, self).__init__(properties=properties, commands=commands)
        return

    def _initialize(self):
        super(FunRandomRewardItemModel, self)._initialize()
        return
