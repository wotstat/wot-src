from frameworks.wulf import ViewModel

class ModeSelectorTooltipsConstants(ViewModel):
    __slots__ = ()
    WHITE_TIGER_BATTLES_CALENDAR_TOOLTIP = b'whiteTigerCalendarTooltip'
    WHITE_TIGER_PROGRESSION_VIEW = b'whiteTigerProgressionView'

    def __init__(self, properties=0, commands=0):
        super(ModeSelectorTooltipsConstants, self).__init__(properties=properties, commands=commands)
        return

    def _initialize(self):
        super(ModeSelectorTooltipsConstants, self)._initialize()
        return
