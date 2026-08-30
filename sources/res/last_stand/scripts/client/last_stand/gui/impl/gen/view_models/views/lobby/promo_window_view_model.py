from frameworks.wulf import ViewModel

class PromoWindowViewModel(ViewModel):
    __slots__ = (b'onClose',)

    def __init__(self, properties=3, commands=1):
        super(PromoWindowViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getStartDate(self):
        return self._getNumber(0)

    def setStartDate(self, value):
        self._setNumber(0, value)
        return

    def getEndDate(self):
        return self._getNumber(1)

    def setEndDate(self, value):
        self._setNumber(1, value)
        return

    def getRegularArtefactsLength(self):
        return self._getNumber(2)

    def setRegularArtefactsLength(self, value):
        self._setNumber(2, value)
        return

    def _initialize(self):
        super(PromoWindowViewModel, self)._initialize()
        self._addNumberProperty(b'startDate', 0)
        self._addNumberProperty(b'endDate', 0)
        self._addNumberProperty(b'regularArtefactsLength', 0)
        self.onClose = self._addCommand(b'onClose')
        return
