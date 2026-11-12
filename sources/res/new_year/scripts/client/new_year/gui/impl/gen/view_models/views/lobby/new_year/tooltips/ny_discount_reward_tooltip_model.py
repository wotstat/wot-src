from frameworks.wulf import ViewModel

class NyDiscountRewardTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(NyDiscountRewardTooltipModel, self).__init__(properties=properties, commands=commands)
        return

    def getLevel(self):
        return self._getNumber(0)

    def setLevel(self, value):
        self._setNumber(0, value)
        return

    def getSelectedVehicle(self):
        return self._getString(1)

    def setSelectedVehicle(self, value):
        self._setString(1, value)
        return

    def getDiscount(self):
        return self._getNumber(2)

    def setDiscount(self, value):
        self._setNumber(2, value)
        return

    def _initialize(self):
        super(NyDiscountRewardTooltipModel, self)._initialize()
        self._addNumberProperty(b'level', 0)
        self._addStringProperty(b'selectedVehicle', b'')
        self._addNumberProperty(b'discount', 0)
        return
