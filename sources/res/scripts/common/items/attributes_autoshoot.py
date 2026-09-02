from items.attributes_helpers import CommonFactorsHelper
AUTOSHOOT_DYNAMIC_ATTRS = [
 b'rate/multiplier',
 b'shotDispersionPerSecFactor',
 b'maxShotDispersionFactor']

class AutoshootFactorsHelper(CommonFactorsHelper):
    ALLOWED_ATTRS = AUTOSHOOT_DYNAMIC_ATTRS
    PREFIX = b'autoShootAttrs/'


attributes_autoshoot_factory = AutoshootFactorsHelper()
