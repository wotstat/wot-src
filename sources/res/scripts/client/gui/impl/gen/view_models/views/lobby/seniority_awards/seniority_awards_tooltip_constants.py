from frameworks.wulf import ViewModel

class SeniorityAwardsTooltipConstants(ViewModel):
    __slots__ = ()
    TOOLTIP_VEHICLE_REWARD = b'TOOLTIP_VEHICLE_REWARD'

    def __init__(self, properties=0, commands=0):
        super(SeniorityAwardsTooltipConstants, self).__init__(properties=properties, commands=commands)
        return

    def _initialize(self):
        super(SeniorityAwardsTooltipConstants, self)._initialize()
        return
