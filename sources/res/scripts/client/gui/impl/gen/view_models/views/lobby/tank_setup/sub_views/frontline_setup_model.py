from frameworks.wulf import Array
from gui.impl.gen.view_models.views.lobby.tank_setup.sub_views.base_setup_model import BaseSetupModel
from gui.impl.gen.view_models.views.lobby.tank_setup.sub_views.battle_ability_details import BattleAbilityDetails
from gui.impl.gen.view_models.views.lobby.tank_setup.sub_views.battle_ability_slot_model import BattleAbilitySlotModel

class FrontlineSetupModel(BaseSetupModel):
    __slots__ = (b'showInfoPage', b'purchaseSelectedAbilities', b'setCurrentSlotDetailsLevel', b'onChangeApplyAbilitiesToTypeSettings')

    def __init__(self, properties=13, commands=11):
        super(FrontlineSetupModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def details(self):
        return self._getViewModel(5)

    @staticmethod
    def getDetailsType():
        return BattleAbilityDetails

    def getIsLocked(self):
        return self._getBool(6)

    def setIsLocked(self, value):
        self._setBool(6, value)
        return

    def getIsTypeSelected(self):
        return self._getBool(7)

    def setIsTypeSelected(self, value):
        self._setBool(7, value)
        return

    def getVehicleType(self):
        return self._getString(8)

    def setVehicleType(self, value):
        self._setString(8, value)
        return

    def getPointsAmount(self):
        return self._getNumber(9)

    def setPointsAmount(self, value):
        self._setNumber(9, value)
        return

    def getTotalPurchasePrice(self):
        return self._getNumber(10)

    def setTotalPurchasePrice(self, value):
        self._setNumber(10, value)
        return

    def getCategoriesOrder(self):
        return self._getArray(11)

    def setCategoriesOrder(self, value):
        self._setArray(11, value)
        return

    @staticmethod
    def getCategoriesOrderType():
        return unicode

    def getSlots(self):
        return self._getArray(12)

    def setSlots(self, value):
        self._setArray(12, value)
        return

    @staticmethod
    def getSlotsType():
        return BattleAbilitySlotModel

    def _initialize(self):
        super(FrontlineSetupModel, self)._initialize()
        self._addViewModelProperty(b'details', BattleAbilityDetails())
        self._addBoolProperty(b'isLocked', True)
        self._addBoolProperty(b'isTypeSelected', False)
        self._addStringProperty(b'vehicleType', b'')
        self._addNumberProperty(b'pointsAmount', 0)
        self._addNumberProperty(b'totalPurchasePrice', 0)
        self._addArrayProperty(b'categoriesOrder', Array())
        self._addArrayProperty(b'slots', Array())
        self.showInfoPage = self._addCommand(b'showInfoPage')
        self.purchaseSelectedAbilities = self._addCommand(b'purchaseSelectedAbilities')
        self.setCurrentSlotDetailsLevel = self._addCommand(b'setCurrentSlotDetailsLevel')
        self.onChangeApplyAbilitiesToTypeSettings = self._addCommand(b'onChangeApplyAbilitiesToTypeSettings')
        return
