from frameworks.wulf import ViewModel

class EarlyAccessIntroViewModel(ViewModel):
    __slots__ = (b'onClose', b'onContinue')

    def __init__(self, properties=2, commands=2):
        super(EarlyAccessIntroViewModel, self).__init__(properties=properties, commands=commands)
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

    def _initialize(self):
        super(EarlyAccessIntroViewModel, self)._initialize()
        self._addNumberProperty(b'startDate', 0)
        self._addNumberProperty(b'endDate', 0)
        self.onClose = self._addCommand(b'onClose')
        self.onContinue = self._addCommand(b'onContinue')
        return
