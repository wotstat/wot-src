from enum import Enum
from items import ITEM_TYPE_NAMES, ITEM_TYPES
FEATURE = b'easy_tank_equip'

class EasyTankEquipLogActions(str, Enum):
    OPEN = b'open'
    CLOSE = b'close'
    CLICK = b'click'
    SWITCH_PRESET = b'switch_preset'
    SWAP_SLOTS = b'swap_slots'


class EasyTankEquipLogItems(str, Enum):
    MAIN_VIEW = b'easy_tank_equip_view'
    APPLY_BUTTON = b'apply_button'
    CANCEL_BUTTON = b'cancel_button'
    CREW = ITEM_TYPE_NAMES[ITEM_TYPES.tankman]
    OPT_DEVICES = ITEM_TYPE_NAMES[ITEM_TYPES.optionalDevice]
    SHELLS = ITEM_TYPE_NAMES[ITEM_TYPES.shell]
    CONSUMABLES = ITEM_TYPE_NAMES[ITEM_TYPES.equipment]
    STYLES = ITEM_TYPE_NAMES[ITEM_TYPES.customizationItem]


class EasyTankEquipSwapInitiators(str, Enum):
    DRAG_AND_DROP = b'drag_and_drop'
    SWAP_BUTTON = b'swap_button'
