from frameworks.wulf import ViewModel

class StrongholdEventBannerTooltipViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(StrongholdEventBannerTooltipViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getState(self):
        return self._getString(0)

    def setState(self, value):
        self._setString(0, value)
        return

    def getStartDate(self):
        return self._getNumber(1)

    def setStartDate(self, value):
        self._setNumber(1, value)
        return

    def getEndDate(self):
        return self._getNumber(2)

    def setEndDate(self, value):
        self._setNumber(2, value)
        return

    def _initialize(self):
        super(StrongholdEventBannerTooltipViewModel, self)._initialize()
        self._addStringProperty(b'state', b'')
        self._addNumberProperty(b'startDate', 0)
        self._addNumberProperty(b'endDate', 0)
        return
