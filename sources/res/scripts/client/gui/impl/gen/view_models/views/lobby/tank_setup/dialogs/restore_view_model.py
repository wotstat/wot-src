from enum import Enum
from frameworks.wulf import Array
from gui.impl.gen.view_models.common.missions.bonuses.item_bonus_model import ItemBonusModel
from gui.impl.gen.view_models.views.dialogs.dialog_template_view_model import DialogTemplateViewModel
from gui.impl.gen.view_models.views.lobby.tank_setup.dialogs.equipment_price_model import EquipmentPriceModel

class EquipmentType(Enum):
    IMPROVED = b'improved'
    TROPHY = b'trophy'
    MODERNIZED = b'modernized'


class RestoreViewModel(DialogTemplateViewModel):
    __slots__ = (b'onRestore', b'onClose', b'onAmountChange')

    def __init__(self, properties=11, commands=5):
        super(RestoreViewModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def equipmentBonus(self):
        return self._getViewModel(6)

    @staticmethod
    def getEquipmentBonusType():
        return ItemBonusModel

    def getEquipmentType(self):
        return EquipmentType(self._getString(7))

    def setEquipmentType(self, value):
        self._setString(7, value.value)
        return

    def getMinEquipCount(self):
        return self._getNumber(8)

    def setMinEquipCount(self, value):
        self._setNumber(8, value)
        return

    def getMaxEquipCount(self):
        return self._getNumber(9)

    def setMaxEquipCount(self, value):
        self._setNumber(9, value)
        return

    def getEquipmentPriceList(self):
        return self._getArray(10)

    def setEquipmentPriceList(self, value):
        self._setArray(10, value)
        return

    @staticmethod
    def getEquipmentPriceListType():
        return EquipmentPriceModel

    def _initialize(self):
        super(RestoreViewModel, self)._initialize()
        self._addViewModelProperty(b'equipmentBonus', ItemBonusModel())
        self._addStringProperty(b'equipmentType')
        self._addNumberProperty(b'minEquipCount', 0)
        self._addNumberProperty(b'maxEquipCount', 0)
        self._addArrayProperty(b'equipmentPriceList', Array())
        self.onRestore = self._addCommand(b'onRestore')
        self.onClose = self._addCommand(b'onClose')
        self.onAmountChange = self._addCommand(b'onAmountChange')
        return
