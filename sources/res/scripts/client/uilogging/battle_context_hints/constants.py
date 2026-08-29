from enum import Enum
FEATURE = b'battle_context_hints'

class BattleContextHintsLogActions(Enum):
    HINT_ACTIVATED = b'hint_activated'
    HINT_SHOWED = b'hint_showed'
    HINT_APPLIED = b'hint_applied'
    HINT_MAX_VIEWS_REACHED = b'hint_max_views_reached'
