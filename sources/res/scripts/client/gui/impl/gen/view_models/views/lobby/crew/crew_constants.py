from enum import Enum
from frameworks.wulf import ViewModel

class Color(Enum):
    BLACKREAL = b'blackReal'
    WHITEREAL = b'whiteReal'
    WHITE = b'white'
    WHITEORANGE = b'whiteOrange'
    WHITESPANISH = b'whiteSpanish'
    PAR = b'par'
    PARSECONDARY = b'parSecondary'
    PARTERTIARY = b'parTertiary'
    RED = b'red'
    REDDARK = b'redDark'
    YELLOW = b'yellow'
    ORANGE = b'orange'
    CREAM = b'cream'
    BROWN = b'brown'
    GREENBRIGHT = b'greenBright'
    GREEN = b'green'
    GREENDARK = b'greenDark'
    BLUEBOOSTER = b'blueBooster'
    BLUETEAMKILLER = b'blueTeamkiller'
    CRED = b'cred'
    GOLD = b'gold'
    BOND = b'bond'
    PROM = b'prom'


class CrewConstants(ViewModel):
    __slots__ = ()
    DONT_SHOW_LEVEL = -1
    SKILL_EFFICIENCY_UNTRAINED = -1
    SKILL_EFFICIENCY_MAX_LEVEL = 1
    SKILL_MAX_LEVEL = 100
    SKILL_MIN_LEVEL = 0
    NEW_SKILL = b'new_skill'
    MAX_FULL_SKILLS_FOR_DISCOUNT = 1
    MAX_BONUS_SKILLS_AMOUNT = 9
    MAX_MAJOR_SKILLS_AMOUNT = 6
    NO_TANKMAN = -1

    def __init__(self, properties=0, commands=0):
        super(CrewConstants, self).__init__(properties=properties, commands=commands)
        return

    def _initialize(self):
        super(CrewConstants, self)._initialize()
        return
