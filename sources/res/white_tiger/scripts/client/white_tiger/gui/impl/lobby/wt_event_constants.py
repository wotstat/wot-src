from enum import Enum
from gui.server_events.bonuses import VehiclesBonus, CustomizationsBonus
from shared_utils import CONST_CONTAINER

class VehicleCharacteristics(Enum):
    PROS = b'pros'
    CONS = b'cons'


class BonusGroup(object):
    STYLE_3D = b'style3d'
    LOOTBOX = b'lootbox'
    OTHER = b'other'
    GUARANTEED_ITEMS = b'guaranteed_items'
    CUSTOMIZATION = b'customization'
    VEHICLES = b'vehicles'


class WhiteTigerLootBoxes(CONST_CONTAINER):
    WT_HUNTER = b'wt_hunter'
    WT_BOSS = b'wt_boss'
    WT_TANK = b'wt_tank'


class ReRollButton(CONST_CONTAINER):
    CLAIM_AND_RELAUNCH = b'claimAndRelaunch'
    REROLL = b'reroll'


def getBonusGroup(bonuses):
    customizationCount = sum(1 for bonus in bonuses if isinstance(bonus, CustomizationsBonus))
    if customizationCount > 0:
        return BonusGroup.CUSTOMIZATION
    vehicleCount = sum(1 for bonus in bonuses if isinstance(bonus, VehiclesBonus))
    if vehicleCount > 1:
        return BonusGroup.VEHICLES
    return BonusGroup.GUARANTEED_ITEMS
