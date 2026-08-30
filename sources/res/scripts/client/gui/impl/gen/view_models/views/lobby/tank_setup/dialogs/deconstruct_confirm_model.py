from enum import Enum
from frameworks.wulf import Array
from gui.impl.gen.view_models.views.dialogs.dialog_template_view_model import DialogTemplateViewModel
from gui.impl.gen.view_models.views.lobby.tank_setup.dialogs.main_content.deconstruct_confirm_item_model import DeconstructConfirmItemModel
from gui.impl.gen.view_models.views.lobby.tank_setup.dialogs.sub_views.current_balance_model import CurrentBalanceModel

class DialogType(Enum):
    DECONSTRUCT = b'deconstruct'
    UPGRADE = b'upgrade'


class DeconstructConfirmModel(DialogTemplateViewModel):
    __slots__ = (b'onClose',)

    def __init__(self, properties=14, commands=3):
        super(DeconstructConfirmModel, self).__init__(properties=properties, commands=commands)
        return

    def getIsLastVehicleEquipment(self):
        return self._getBool(6)

    def setIsLastVehicleEquipment(self, value):
        self._setBool(6, value)
        return

    def getDeconstructingEquipCoinsAmount(self):
        return self._getNumber(7)

    def setDeconstructingEquipCoinsAmount(self, value):
        self._setNumber(7, value)
        return

    def getEquipUpgradeCost(self):
        return self._getNumber(8)

    def setEquipUpgradeCost(self, value):
        self._setNumber(8, value)
        return

    def getDeviceName(self):
        return self._getString(9)

    def setDeviceName(self, value):
        self._setString(9, value)
        return

    def getDialogType(self):
        return DialogType(self._getString(10))

    def setDialogType(self, value):
        self._setString(10, value.value)
        return

    def getBalance(self):
        return self._getArray(11)

    def setBalance(self, value):
        self._setArray(11, value)
        return

    @staticmethod
    def getBalanceType():
        return CurrentBalanceModel

    def getVehicleEquipment(self):
        return self._getArray(12)

    def setVehicleEquipment(self, value):
        self._setArray(12, value)
        return

    @staticmethod
    def getVehicleEquipmentType():
        return DeconstructConfirmItemModel

    def getInventoryEquipment(self):
        return self._getArray(13)

    def setInventoryEquipment(self, value):
        self._setArray(13, value)
        return

    @staticmethod
    def getInventoryEquipmentType():
        return DeconstructConfirmItemModel

    def _initialize(self):
        super(DeconstructConfirmModel, self)._initialize()
        self._addBoolProperty(b'isLastVehicleEquipment', False)
        self._addNumberProperty(b'deconstructingEquipCoinsAmount', 0)
        self._addNumberProperty(b'equipUpgradeCost', 0)
        self._addStringProperty(b'deviceName', b'')
        self._addStringProperty(b'dialogType')
        self._addArrayProperty(b'balance', Array())
        self._addArrayProperty(b'vehicleEquipment', Array())
        self._addArrayProperty(b'inventoryEquipment', Array())
        self.onClose = self._addCommand(b'onClose')
        return
