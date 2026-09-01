from enum import Enum
from gui.impl.gen.view_models.views.lobby.battle_results.reward_item_model import RewardItemModel

class WhiteTigerRewardTypes(Enum):
    CREDITS = b'credits'
    GOLD = b'gold'
    CRYSTALS = b'crystal'
    XP = b'xp'
    FREE_XP = b'freeXP'
    TANKMEN_XP = b'tankmenXP'
    ACHIEVEMENT = b'achievement'
    EQUIP_COIN = b'equipCoin'
    PROGRESSION_STAMPS = b'stamp'
    WT_TICKET = b'wtevent_Ticket'
    BATTLE_PASS_POINTS = b'battlepassPoints'
    LOOT_BOX = b'wtevent_lootBox'
    CUSTOMIZATIONS = b'customizations'


class WhiteTigerRewardItemModel(RewardItemModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(WhiteTigerRewardItemModel, self).__init__(properties=properties, commands=commands)
        return

    def _initialize(self):
        super(WhiteTigerRewardItemModel, self)._initialize()
        return
