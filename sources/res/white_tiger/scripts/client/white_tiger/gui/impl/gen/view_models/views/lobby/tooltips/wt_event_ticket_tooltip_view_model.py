from frameworks.wulf import ViewModel

class WtEventTicketTooltipViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=1, commands=0):
        super(WtEventTicketTooltipViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getQuantity(self):
        return self._getNumber(0)

    def setQuantity(self, value):
        self._setNumber(0, value)
        return

    def _initialize(self):
        super(WtEventTicketTooltipViewModel, self)._initialize()
        self._addNumberProperty(b'quantity', 0)
        return
