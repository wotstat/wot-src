from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.common.missions.bonuses.bonus_model import BonusModel
from gui.impl.gen.view_models.views.lobby.common.vehicle_model import VehicleModel

class SeniorityRewardAwardViewModel(ViewModel):
    __slots__ = (b'onOpenBtnClick',)

    def __init__(self, properties=5, commands=1):
        super(SeniorityRewardAwardViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getCategory(self):
        return self._getString(0)

    def setCategory(self, value):
        self._setString(0, value)
        return

    def getBonuses(self):
        return self._getArray(1)

    def setBonuses(self, value):
        self._setArray(1, value)
        return

    @staticmethod
    def getBonusesType():
        return BonusModel

    def getVehicles(self):
        return self._getArray(2)

    def setVehicles(self, value):
        self._setArray(2, value)
        return

    @staticmethod
    def getVehiclesType():
        return VehicleModel

    def getSpecialCurrencyCount(self):
        return self._getNumber(3)

    def setSpecialCurrencyCount(self, value):
        self._setNumber(3, value)
        return

    def getIsShopOnOpenLocked(self):
        return self._getBool(4)

    def setIsShopOnOpenLocked(self, value):
        self._setBool(4, value)
        return

    def _initialize(self):
        super(SeniorityRewardAwardViewModel, self)._initialize()
        self._addStringProperty(b'category', b'')
        self._addArrayProperty(b'bonuses', Array())
        self._addArrayProperty(b'vehicles', Array())
        self._addNumberProperty(b'specialCurrencyCount', -1)
        self._addBoolProperty(b'isShopOnOpenLocked', False)
        self.onOpenBtnClick = self._addCommand(b'onOpenBtnClick')
        return
