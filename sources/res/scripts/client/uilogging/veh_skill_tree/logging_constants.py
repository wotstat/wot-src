from enum import Enum
FEATURE_VEH_SKILL_TREE = b'veh_skill_tree'
VEH_SKILL_TREE_SCREEN = b'tier_11_progression_screen'

class VehSkillTreeActions(str, Enum):
    CLICK = b'click'
    OPEN = b'open'
    CLOSE = b'close'


class VehSkillTreeItems(str, Enum):
    SKILL_TREE = b'skill_tree'
    RESEARCH_BUTTON = b'research_button'
