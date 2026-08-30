from enum import Enum
from frameworks.wulf import Array
from gui.impl.gen.view_models.common.missions.bonuses.item_bonus_model import ItemBonusModel
from gui.impl.gen.view_models.views.dialogs.dialog_template_view_model import DialogTemplateViewModel
from gui.impl.gen.view_models.views.lobby.tank_setup.dialogs.equipment_price_model import EquipmentPriceModel
from gui.impl.gen.view_models.views.lobby.tank_setup.dialogs.sub_views.current_balance_model import CurrentBalanceModel

class ModuleType(Enum):
    IMPROVED = b'improved'
    TROPHY = b'trophy'
    STANDARD = b'standard'


class SellViewModel(DialogTemplateViewModel):
    __slots__ = (b'onSell', b'onClose')

    def __init__(self, properties=11, commands=4):
        super(SellViewModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def equipmentPrice(self):
        return self._getViewModel(6)

    @staticmethod
    def getEquipmentPriceType():
        return EquipmentPriceModel

    @property
    def equipment(self):
        return self._getViewModel(7)

    @staticmethod
    def getEquipmentType():
        return ItemBonusModel

    def getModuleType(self):
        return ModuleType(self._getString(8))

    def setModuleType(self, value):
        self._setString(8, value.value)
        return

    def getBalance(self):
        return self._getArray(9)

    def setBalance(self, value):
        self._setArray(9, value)
        return

    @staticmethod
    def getBalanceType():
        return CurrentBalanceModel

    def getIsOptDeviceRestored(self):
        return self._getBool(10)

    def setIsOptDeviceRestored(self, value):
        self._setBool(10, value)
        return

    def _initialize(self):
        super(SellViewModel, self)._initialize()
        self._addViewModelProperty(b'equipmentPrice', EquipmentPriceModel())
        self._addViewModelProperty(b'equipment', ItemBonusModel())
        self._addStringProperty(b'moduleType')
        self._addArrayProperty(b'balance', Array())
        self._addBoolProperty(b'isOptDeviceRestored', False)
        self.onSell = self._addCommand(b'onSell')
        self.onClose = self._addCommand(b'onClose')
        return
