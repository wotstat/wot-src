from frameworks.wulf import ViewModel

class ItemHighlightTypes(ViewModel):
    __slots__ = ()
    OPTIONAL_DEVICE = b'optionalDevice'
    TROPHY = b'equipmentTrophy'
    TROPHY_BASIC = b'equipmentTrophyBasic'
    TROPHY_UPGRADED = b'equipmentTrophyUpgraded'
    BATTLE_BOOSTER_REPLACE = b'battleBoosterReplace'
    BATTLE_BOOSTER = b'battleBooster'
    EQUIPMENT_PLUS = b'equipmentPlus'
    BUILT_IN_EQUIPMENT = b'builtInEquipment'
    BATTLE_ABILITY = b'battleAbility'
    INCOMPATIBLE_EQUIPMENT = b'incompatibleEquipment'
    MODERNIZED = b'equipmentModernized'
    MODERNIZED1 = b'equipmentModernized_1'
    MODERNIZED2 = b'equipmentModernized_2'
    MODERNIZED3 = b'equipmentModernized_3'
    PROGRESSION_STYLE_UPGRADED = b'progressionStyleUpgraded_'
    POST_PROGRESSION_MODIFICATION = b'postProgressionModification'
    EMPTY = b''

    def __init__(self, properties=0, commands=0):
        super(ItemHighlightTypes, self).__init__(properties=properties, commands=commands)
        return

    def _initialize(self):
        super(ItemHighlightTypes, self)._initialize()
        return
