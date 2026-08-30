from frameworks.wulf import ViewModel

class TooltipConstants(ViewModel):
    __slots__ = ()
    SKILL = b'crewPerkGf'
    COMMANDER_BONUS = b'commanderBonus'
    ACHIEVEMENT = b'achievement'
    SKIN = b'crewSkin'
    TANKMAN = b'tankman'
    TANKMAN_NOT_RECRUITED = b'tankmanNotRecruited'

    def __init__(self, properties=0, commands=0):
        super(TooltipConstants, self).__init__(properties=properties, commands=commands)
        return

    def _initialize(self):
        super(TooltipConstants, self)._initialize()
        return
