from frameworks.wulf import ViewModel

class InfoPageScrollToSection(ViewModel):
    __slots__ = ()
    BATTLE_SCENARIOS = b'battle_scenarios'

    def __init__(self, properties=0, commands=0):
        super(InfoPageScrollToSection, self).__init__(properties=properties, commands=commands)
        return

    def _initialize(self):
        super(InfoPageScrollToSection, self)._initialize()
        return
