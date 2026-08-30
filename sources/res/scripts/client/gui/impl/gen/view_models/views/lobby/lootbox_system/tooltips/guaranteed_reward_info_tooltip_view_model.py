from frameworks.wulf import ViewModel

class GuaranteedRewardInfoTooltipViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(GuaranteedRewardInfoTooltipViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getEventName(self):
        return self._getString(0)

    def setEventName(self, value):
        self._setString(0, value)
        return

    def getGuaranteedFrequency(self):
        return self._getNumber(1)

    def setGuaranteedFrequency(self, value):
        self._setNumber(1, value)
        return

    def _initialize(self):
        super(GuaranteedRewardInfoTooltipViewModel, self)._initialize()
        self._addStringProperty(b'eventName', b'')
        self._addNumberProperty(b'guaranteedFrequency', 0)
        return
