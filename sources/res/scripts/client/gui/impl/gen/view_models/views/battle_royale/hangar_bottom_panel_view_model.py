from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.ui_kit.list_model import ListModel

class HangarBottomPanelViewModel(ViewModel):
    __slots__ = (b'onRentBtnClicked', b'onRepairBtnClicked')

    def __init__(self, properties=12, commands=2):
        super(HangarBottomPanelViewModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def ammunition(self):
        return self._getViewModel(0)

    @staticmethod
    def getAmmunitionType():
        return ListModel

    @property
    def abilities(self):
        return self._getViewModel(1)

    @staticmethod
    def getAbilitiesType():
        return ListModel

    @property
    def specialAbilities(self):
        return self._getViewModel(2)

    @staticmethod
    def getSpecialAbilitiesType():
        return ListModel

    @property
    def rentPrice(self):
        return self._getViewModel(3)

    @staticmethod
    def getRentPriceType():
        return ListModel

    def getVehName(self):
        return self._getString(4)

    def setVehName(self, value):
        self._setString(4, value)
        return

    def getVehType(self):
        return self._getString(5)

    def setVehType(self, value):
        self._setString(5, value)
        return

    def getRentState(self):
        return self._getString(6)

    def setRentState(self, value):
        self._setString(6, value)
        return

    def getRentDays(self):
        return self._getNumber(7)

    def setRentDays(self, value):
        self._setNumber(7, value)
        return

    def getRentTime(self):
        return self._getString(8)

    def setRentTime(self, value):
        self._setString(8, value)
        return

    def getIsRepairBtnVisible(self):
        return self._getBool(9)

    def setIsRepairBtnVisible(self, value):
        self._setBool(9, value)
        return

    def getIsVehicleInBattle(self):
        return self._getBool(10)

    def setIsVehicleInBattle(self, value):
        self._setBool(10, value)
        return

    def getIsEnoughMoney(self):
        return self._getBool(11)

    def setIsEnoughMoney(self, value):
        self._setBool(11, value)
        return

    def _initialize(self):
        super(HangarBottomPanelViewModel, self)._initialize()
        self._addViewModelProperty(b'ammunition', ListModel())
        self._addViewModelProperty(b'abilities', ListModel())
        self._addViewModelProperty(b'specialAbilities', ListModel())
        self._addViewModelProperty(b'rentPrice', ListModel())
        self._addStringProperty(b'vehName', b'')
        self._addStringProperty(b'vehType', b'')
        self._addStringProperty(b'rentState', b'')
        self._addNumberProperty(b'rentDays', 0)
        self._addStringProperty(b'rentTime', b'')
        self._addBoolProperty(b'isRepairBtnVisible', False)
        self._addBoolProperty(b'isVehicleInBattle', False)
        self._addBoolProperty(b'isEnoughMoney', True)
        self.onRentBtnClicked = self._addCommand(b'onRentBtnClicked')
        self.onRepairBtnClicked = self._addCommand(b'onRepairBtnClicked')
        return
