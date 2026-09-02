from frameworks.wulf import ViewModel

class WtEventStampTooltipViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=1, commands=0):
        super(WtEventStampTooltipViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getStampsPerProgressionStage(self):
        return self._getNumber(0)

    def setStampsPerProgressionStage(self, value):
        self._setNumber(0, value)
        return

    def _initialize(self):
        super(WtEventStampTooltipViewModel, self)._initialize()
        self._addNumberProperty(b'stampsPerProgressionStage', 0)
        return
