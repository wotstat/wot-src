from enum import Enum

class AchievementType(Enum):
    REGULAR = b'regular'
    STEPPED = b'stepped'
    CUMULATIVE = b'cumulative'
    SUBCATEGORY = b'subcategory'


NEAREST_REQUIRED_COUNT = 3
TROPHIES_ACHIEVEMENT_ID = -1
BONUS_PRIORITY_MAP = {b'dogTagComponents': 1, 
   b'customizations': 2}
