from frameworks.wulf import ViewModel

class SelectableRewardCategoryModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=5, commands=0):
        super(SelectableRewardCategoryModel, self).__init__(properties=properties, commands=commands)
        return

    def getIsDiscount(self):
        return self._getBool(0)

    def setIsDiscount(self, value):
        self._setBool(0, value)
        return

    def getIsSelected(self):
        return self._getBool(1)

    def setIsSelected(self, value):
        self._setBool(1, value)
        return

    def getIsCompensation(self):
        return self._getBool(2)

    def setIsCompensation(self, value):
        self._setBool(2, value)
        return

    def getVehicleLevel(self):
        return self._getNumber(3)

    def setVehicleLevel(self, value):
        self._setNumber(3, value)
        return

    def getRewardsSelected(self):
        return self._getNumber(4)

    def setRewardsSelected(self, value):
        self._setNumber(4, value)
        return

    def _initialize(self):
        super(SelectableRewardCategoryModel, self)._initialize()
        self._addBoolProperty(b'isDiscount', False)
        self._addBoolProperty(b'isSelected', False)
        self._addBoolProperty(b'isCompensation', False)
        self._addNumberProperty(b'vehicleLevel', 0)
        self._addNumberProperty(b'rewardsSelected', 0)
        return
