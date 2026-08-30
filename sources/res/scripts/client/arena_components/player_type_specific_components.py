from arena_components.epic_battle_player_data_component import EpicBattlePlayerDataComponent
from player_data_component import PlayerDataComponent
from advanced_chat_component import AdvancedChatComponent
from arena_component_system.epic_sector_warning_component import EpicSectorWarningComponent
from arena_component_system.arena_equipment_component import ArenaEquipmentComponent
from arena_component_system.overtime_component import OvertimeComponent
from gui.shared.system_factory import collectAdvancedChatComponent

def getPlayerTypeSpecificComponentsForEpicRandom():
    return {b'playerDataComponent': PlayerDataComponent}


def getPlayerTypeSpecificComponentsForEpicBattle():
    return {b'playerDataComponent': EpicBattlePlayerDataComponent, 
       b'sectorWarningComponent': EpicSectorWarningComponent, 
       b'overtimeComponent': OvertimeComponent}


def getDefaultComponents(bonusType):
    return {b'arenaEquipmentComponent': ArenaEquipmentComponent, 
       b'advancedChatComponent': (collectAdvancedChatComponent(bonusType) or AdvancedChatComponent)}
