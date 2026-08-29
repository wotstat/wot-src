from gui.impl.gen import R
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.ui_kit.button_icon_text_model import ButtonIconTextModel
from gui.impl.gen.view_models.ui_kit.list_model import ListModel
from gui.impl.gen.view_models.ui_kit.vehicle_btn_model import VehicleBtnModel
from gui.impl.gen.view_models.views.buy_vehicle_view.additional_equipment_slot_model import AdditionalEquipmentSlotModel

class EquipmentBlockModel(ViewModel):
    __slots__ = (b'onSelectTradeOffVehicle', b'onCancelTradeOffVehicle')

    def __init__(self, properties=23, commands=2):
        super(EquipmentBlockModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def totalPrice(self):
        return self._getViewModel(0)

    @staticmethod
    def getTotalPriceType():
        return ListModel

    @property
    def ammo(self):
        return self._getViewModel(1)

    @staticmethod
    def getAmmoType():
        return AdditionalEquipmentSlotModel

    @property
    def slot(self):
        return self._getViewModel(2)

    @staticmethod
    def getSlotType():
        return AdditionalEquipmentSlotModel

    @property
    def vehicleBtn(self):
        return self._getViewModel(3)

    @staticmethod
    def getVehicleBtnType():
        return VehicleBtnModel

    @property
    def vehicleRentBtn(self):
        return self._getViewModel(4)

    @staticmethod
    def getVehicleRentBtnType():
        return ButtonIconTextModel

    @property
    def vehicleTradeInBtn(self):
        return self._getViewModel(5)

    @staticmethod
    def getVehicleTradeInBtnType():
        return ButtonIconTextModel

    def getBuyBtnIsEnabled(self):
        return self._getBool(6)

    def setBuyBtnIsEnabled(self, value):
        self._setBool(6, value)
        return

    def getTradeInIsEnabled(self):
        return self._getBool(7)

    def setTradeInIsEnabled(self, value):
        self._setBool(7, value)
        return

    def getTradeOffVehicleIntCD(self):
        return self._getNumber(8)

    def setTradeOffVehicleIntCD(self, value):
        self._setNumber(8, value)
        return

    def getTradeOffWidgetEnabled(self):
        return self._getBool(9)

    def setTradeOffWidgetEnabled(self, value):
        self._setBool(9, value)
        return

    def getBuyVehicleIntCD(self):
        return self._getNumber(10)

    def setBuyVehicleIntCD(self, value):
        self._setNumber(10, value)
        return

    def getSelectedRentID(self):
        return self._getNumber(11)

    def setSelectedRentID(self, value):
        self._setNumber(11, value)
        return

    def getSelectedRentDays(self):
        return self._getNumber(12)

    def setSelectedRentDays(self, value):
        self._setNumber(12, value)
        return

    def getSelectedRentType(self):
        return self._getNumber(13)

    def setSelectedRentType(self, value):
        self._setNumber(13, value)
        return

    def getSelectedRentSeason(self):
        return self._getNumber(14)

    def setSelectedRentSeason(self, value):
        self._setNumber(14, value)
        return

    def getEmtySlotAvailable(self):
        return self._getBool(15)

    def setEmtySlotAvailable(self, value):
        self._setBool(15, value)
        return

    def getIsRestore(self):
        return self._getBool(16)

    def setIsRestore(self, value):
        self._setBool(16, value)
        return

    def getIsSlotAnimPlaying(self):
        return self._getBool(17)

    def setIsSlotAnimPlaying(self, value):
        self._setBool(17, value)
        return

    def getBuyBtnLabel(self):
        return self._getResource(18)

    def setBuyBtnLabel(self, value):
        self._setResource(18, value)
        return

    def getConfirmGoldPrice(self):
        return self._getNumber(19)

    def setConfirmGoldPrice(self, value):
        self._setNumber(19, value)
        return

    def getPopoverIsAvailable(self):
        return self._getBool(20)

    def setPopoverIsAvailable(self, value):
        self._setBool(20, value)
        return

    def getIsRentVisible(self):
        return self._getBool(21)

    def setIsRentVisible(self, value):
        self._setBool(21, value)
        return

    def getTradeInTooltip(self):
        return self._getString(22)

    def setTradeInTooltip(self, value):
        self._setString(22, value)
        return

    def _initialize(self):
        super(EquipmentBlockModel, self)._initialize()
        self._addViewModelProperty(b'totalPrice', ListModel())
        self._addViewModelProperty(b'ammo', AdditionalEquipmentSlotModel())
        self._addViewModelProperty(b'slot', AdditionalEquipmentSlotModel())
        self._addViewModelProperty(b'vehicleBtn', VehicleBtnModel())
        self._addViewModelProperty(b'vehicleRentBtn', ButtonIconTextModel())
        self._addViewModelProperty(b'vehicleTradeInBtn', ButtonIconTextModel())
        self._addBoolProperty(b'buyBtnIsEnabled', False)
        self._addBoolProperty(b'tradeInIsEnabled', False)
        self._addNumberProperty(b'tradeOffVehicleIntCD', -1)
        self._addBoolProperty(b'tradeOffWidgetEnabled', True)
        self._addNumberProperty(b'buyVehicleIntCD', 0)
        self._addNumberProperty(b'selectedRentID', 0)
        self._addNumberProperty(b'selectedRentDays', 0)
        self._addNumberProperty(b'selectedRentType', 0)
        self._addNumberProperty(b'selectedRentSeason', 0)
        self._addBoolProperty(b'emtySlotAvailable', False)
        self._addBoolProperty(b'isRestore', False)
        self._addBoolProperty(b'isSlotAnimPlaying', False)
        self._addResourceProperty(b'buyBtnLabel', R.invalid())
        self._addNumberProperty(b'confirmGoldPrice', 0)
        self._addBoolProperty(b'popoverIsAvailable', False)
        self._addBoolProperty(b'isRentVisible', False)
        self._addStringProperty(b'tradeInTooltip', b'')
        self.onSelectTradeOffVehicle = self._addCommand(b'onSelectTradeOffVehicle')
        self.onCancelTradeOffVehicle = self._addCommand(b'onCancelTradeOffVehicle')
        return
