from frameworks.wulf import Array
from frontline.gui.impl.gen.view_models.views.lobby.components.loadout.battle_ability_details import BattleAbilityDetails
from frontline.gui.impl.gen.view_models.views.lobby.components.loadout.battle_ability_slot_model import BattleAbilitySlotModel
from gui.impl.gen.view_models.views.lobby.loadout.base_loadout_model import BaseLoadoutModel

class BattleAbilitiesSetupModel(BaseLoadoutModel):
    __slots__ = (b'onCurrentAbilityLevelChanged', b'onApplyToTypeChanged')

    def __init__(self, properties=10, commands=3):
        super(BattleAbilitiesSetupModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def details(self):
        return self._getViewModel(1)

    @staticmethod
    def getDetailsType():
        return BattleAbilityDetails

    def getIsTypeSelected(self):
        return self._getBool(2)

    def setIsTypeSelected(self, value):
        self._setBool(2, value)
        return

    def getModeState(self):
        return self._getString(3)

    def setModeState(self, value):
        self._setString(3, value)
        return

    def getVehicleType(self):
        return self._getString(4)

    def setVehicleType(self, value):
        self._setString(4, value)
        return

    def getPointsAmount(self):
        return self._getNumber(5)

    def setPointsAmount(self, value):
        self._setNumber(5, value)
        return

    def getTotalPurchasePrice(self):
        return self._getNumber(6)

    def setTotalPurchasePrice(self, value):
        self._setNumber(6, value)
        return

    def getCategoriesOrder(self):
        return self._getArray(7)

    def setCategoriesOrder(self, value):
        self._setArray(7, value)
        return

    @staticmethod
    def getCategoriesOrderType():
        return unicode

    def getKeyNames(self):
        return self._getArray(8)

    def setKeyNames(self, value):
        self._setArray(8, value)
        return

    @staticmethod
    def getKeyNamesType():
        return unicode

    def getSlots(self):
        return self._getArray(9)

    def setSlots(self, value):
        self._setArray(9, value)
        return

    @staticmethod
    def getSlotsType():
        return BattleAbilitySlotModel

    def _initialize(self):
        super(BattleAbilitiesSetupModel, self)._initialize()
        self._addViewModelProperty(b'details', BattleAbilityDetails())
        self._addBoolProperty(b'isTypeSelected', False)
        self._addStringProperty(b'modeState', b'')
        self._addStringProperty(b'vehicleType', b'')
        self._addNumberProperty(b'pointsAmount', 0)
        self._addNumberProperty(b'totalPurchasePrice', 0)
        self._addArrayProperty(b'categoriesOrder', Array())
        self._addArrayProperty(b'keyNames', Array())
        self._addArrayProperty(b'slots', Array())
        self.onCurrentAbilityLevelChanged = self._addCommand(b'onCurrentAbilityLevelChanged')
        self.onApplyToTypeChanged = self._addCommand(b'onApplyToTypeChanged')
        return
