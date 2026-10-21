from frameworks.wulf import ViewModel

class BannerTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(BannerTooltipModel, self).__init__(properties=properties, commands=commands)
        return

    def getPerformance(self):
        return self._getNumber(0)

    def setPerformance(self, value):
        self._setNumber(0, value)
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
        super(BannerTooltipModel, self)._initialize()
        self._addNumberProperty(b'performance', 0)
        self._addNumberProperty(b'startDate', 0)
        self._addNumberProperty(b'endDate', 0)
        return
