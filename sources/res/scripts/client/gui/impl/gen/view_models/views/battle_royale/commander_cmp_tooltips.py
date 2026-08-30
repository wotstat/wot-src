from frameworks.wulf import ViewModel

class CommanderCmpTooltips(ViewModel):
    __slots__ = ()
    TOOLTIP_SIXTH_SENSE_SKILL = b'commander_sixthSense'
    TOOLTIP_TANKMAN = b'battleRoyaleTankman'

    def __init__(self, properties=0, commands=0):
        super(CommanderCmpTooltips, self).__init__(properties=properties, commands=commands)
        return

    def _initialize(self):
        super(CommanderCmpTooltips, self)._initialize()
        return
