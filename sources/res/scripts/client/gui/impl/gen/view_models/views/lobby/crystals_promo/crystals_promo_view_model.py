from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.crystals_promo.battle_type_model import BattleTypeModel

class CrystalsPromoViewModel(ViewModel):
    __slots__ = (b'goToShop',)
    TANKS_TAB = b'tanksTab'
    INSTRUCTIONS_TAB = b'instructionsTab'
    EQUIPMENT_TAB = b'equipmentTab'

    def __init__(self, properties=7, commands=1):
        super(CrystalsPromoViewModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def battleType(self):
        return self._getViewModel(0)

    @staticmethod
    def getBattleTypeType():
        return BattleTypeModel

    def getSelectedTab(self):
        return self._getNumber(1)

    def setSelectedTab(self, value):
        self._setNumber(1, value)
        return

    def getInstructionPrice(self):
        return self._getString(2)

    def setInstructionPrice(self, value):
        self._setString(2, value)
        return

    def getVehiclePrice(self):
        return self._getString(3)

    def setVehiclePrice(self, value):
        self._setString(3, value)
        return

    def getEquipmentPrice(self):
        return self._getString(4)

    def setEquipmentPrice(self, value):
        self._setString(4, value)
        return

    def getSyncInitiator(self):
        return self._getBool(5)

    def setSyncInitiator(self, value):
        self._setBool(5, value)
        return

    def getIsChina(self):
        return self._getBool(6)

    def setIsChina(self, value):
        self._setBool(6, value)
        return

    def _initialize(self):
        super(CrystalsPromoViewModel, self)._initialize()
        self._addViewModelProperty(b'battleType', BattleTypeModel())
        self._addNumberProperty(b'selectedTab', 0)
        self._addStringProperty(b'instructionPrice', b'')
        self._addStringProperty(b'vehiclePrice', b'')
        self._addStringProperty(b'equipmentPrice', b'')
        self._addBoolProperty(b'syncInitiator', False)
        self._addBoolProperty(b'isChina', False)
        self.goToShop = self._addCommand(b'goToShop')
        return
