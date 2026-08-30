import typing
from enum import Enum
from gui.impl.gen.view_models.views.lobby.mode_selector.mode_selector_columns import ModeSelectorColumns
from gui.prb_control.settings import PREBATTLE_ACTION_NAME
DEFAULT_COLUMN = ModeSelectorColumns.COLUMN_2
DEFAULT_PRIORITY = -1
DEFAULT_MODE_SETTING = b'default'
COLUMN_SETTINGS = {(PREBATTLE_ACTION_NAME.RANDOM): (
                                  ModeSelectorColumns.COLUMN_0, -1), 
   (PREBATTLE_ACTION_NAME.WINBACK): (
                                   ModeSelectorColumns.COLUMN_0, -1), 
   (PREBATTLE_ACTION_NAME.EPIC): (
                                ModeSelectorColumns.COLUMN_1, 10), 
   (PREBATTLE_ACTION_NAME.BATTLE_ROYALE): (
                                         ModeSelectorColumns.COLUMN_1, 10), 
   (PREBATTLE_ACTION_NAME.MAPBOX): (
                                  ModeSelectorColumns.COLUMN_2, 30), 
   (PREBATTLE_ACTION_NAME.RANKED): (
                                  ModeSelectorColumns.COLUMN_2, 10), 
   (PREBATTLE_ACTION_NAME.EVENT_BATTLE): (
                                        ModeSelectorColumns.COLUMN_2, 40), 
   (PREBATTLE_ACTION_NAME.STRONGHOLDS_BATTLES_LIST): (
                                                    ModeSelectorColumns.COLUMN_3, 10), 
   (PREBATTLE_ACTION_NAME.SPEC_BATTLES_LIST): (
                                             ModeSelectorColumns.COLUMN_3, 20), 
   (PREBATTLE_ACTION_NAME.TRAININGS_LIST): (
                                          ModeSelectorColumns.COLUMN_3, 30), 
   (PREBATTLE_ACTION_NAME.MAPS_TRAINING): (
                                         ModeSelectorColumns.COLUMN_3, 40), 
   DEFAULT_MODE_SETTING: (
                        ModeSelectorColumns.COLUMN_2, 50)}

class ModeSelectorRewardID(Enum):
    BONES = b'bones'
    BOUNTY_EQUIPMENT = b'bountyEquipment'
    CREDITS = b'credits'
    CREW = b'crew'
    EXPERIENCE = b'experience'
    IMPROVED_EQUIPMENT = b'improvedEquipment'
    OTHER = b'other'
    RANDOM = b'random'
    STYLE = b'style'
    PROGRESSION_STYLE = b'progressionStyle'
    VEHICLE = b'vehicle'
    LOOT_BOXES = b'lootBoxes'
    ATTACHMENT = b'attachment'
    EXPERIMENTAL_EQUIPMENT = b'experimentalEquipment'
