from gui.impl.gen import R
from frameworks.wulf import ViewModel

class WtCarouselTankStatusModel(ViewModel):
    __slots__ = (b'onOpenTasks', b'onBuyTicket')

    def __init__(self, properties=4, commands=2):
        super(WtCarouselTankStatusModel, self).__init__(properties=properties, commands=commands)
        return

    def getTitle(self):
        return self._getString(0)

    def setTitle(self, value):
        self._setString(0, value)
        return

    def getIcon(self):
        return self._getResource(1)

    def setIcon(self, value):
        self._setResource(1, value)
        return

    def getQuantity(self):
        return self._getNumber(2)

    def setQuantity(self, value):
        self._setNumber(2, value)
        return

    def getWtVehicleType(self):
        return self._getString(3)

    def setWtVehicleType(self, value):
        self._setString(3, value)
        return

    def _initialize(self):
        super(WtCarouselTankStatusModel, self)._initialize()
        self._addStringProperty(b'title', b'')
        self._addResourceProperty(b'icon', R.invalid())
        self._addNumberProperty(b'quantity', -1)
        self._addStringProperty(b'wtVehicleType', b'boss')
        self.onOpenTasks = self._addCommand(b'onOpenTasks')
        self.onBuyTicket = self._addCommand(b'onBuyTicket')
        return
