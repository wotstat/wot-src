from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.common.price_model import PriceModel

class RentIconTooltipViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=5, commands=0):
        super(RentIconTooltipViewModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def price(self):
        return self._getViewModel(0)

    @staticmethod
    def getPriceType():
        return PriceModel

    def getRentDays(self):
        return self._getNumber(1)

    def setRentDays(self, value):
        self._setNumber(1, value)
        return

    def getDaysTotal(self):
        return self._getNumber(2)

    def setDaysTotal(self, value):
        self._setNumber(2, value)
        return

    def getTimeLeft(self):
        return self._getString(3)

    def setTimeLeft(self, value):
        self._setString(3, value)
        return

    def getIsTestDriveMode(self):
        return self._getBool(4)

    def setIsTestDriveMode(self, value):
        self._setBool(4, value)
        return

    def _initialize(self):
        super(RentIconTooltipViewModel, self)._initialize()
        self._addViewModelProperty(b'price', PriceModel())
        self._addNumberProperty(b'rentDays', 0)
        self._addNumberProperty(b'daysTotal', 0)
        self._addStringProperty(b'timeLeft', b'')
        self._addBoolProperty(b'isTestDriveMode', False)
        return
