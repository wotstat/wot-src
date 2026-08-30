from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.views.lobby.common.vehicle_model import VehicleModel
from gui.impl.gen.view_models.views.lobby.hangar.buy_vehicle_option_model import BuyVehicleOptionModel
from gui.impl.gen.view_models.views.lobby.hangar.buy_vehicle_price_model import BuyVehiclePriceModel
from gui.impl.gen.view_models.views.lobby.hangar.buy_vehicle_simple_tooltip_model import BuyVehicleSimpleTooltipModel

class BuyVehicleViewModel(ViewModel):
    __slots__ = (b'onCloseBtnClick', b'onBuyBtnClick', b'onBackClick', b'onOptionClick', b'onSelectTradeInVehicleToSell', b'onClearTradeInVehicleToSell', b'onDisclaimerClick')
    VEHICLE_NOT_SELECTED_CD = -1
    BUYING_RENT_IDX = -1
    RENT_NOT_SELECTED_IDX = -2
    ACTION_PRICE_TOOLTIP = b'actionPrice'
    TRADE_IN_INFO_NOT_AVAILABLE_TOOLTIP = b'tradeInInfoNotAvailable'
    TRADE_IN_INFO_TOOLTIP = b'tradeInInfo'
    TRADE_IN_STATE_NOT_AVAILABLE_TOOLTIP = b'tradeInStateNotAvailable'
    SELECTED_VEHICLE_TRADEOFF_TOOLTIP = b'selectedVehicleTradeOff'
    VEHICLE_SELL_CONFIRMATION_POPOVER = b'VehicleSellConfirmationPopover'
    RENTAL_TERM_SELECTION_POPOVER = b'RentalTermSelectionPopover'

    def __init__(self, properties=15, commands=7):
        super(BuyVehicleViewModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def vehicle(self):
        return self._getViewModel(0)

    @staticmethod
    def getVehicleType():
        return VehicleModel

    @property
    def tradeInVehicleToSell(self):
        return self._getViewModel(1)

    @staticmethod
    def getTradeInVehicleToSellType():
        return VehicleModel

    @property
    def totals(self):
        return self._getViewModel(2)

    @staticmethod
    def getTotalsType():
        return BuyVehiclePriceModel

    @property
    def buyButtonTooltip(self):
        return self._getViewModel(3)

    @staticmethod
    def getBuyButtonTooltipType():
        return BuyVehicleSimpleTooltipModel

    def getIsRestore(self):
        return self._getBool(4)

    def setIsRestore(self, value):
        self._setBool(4, value)
        return

    def getHasTradeInWidget(self):
        return self._getBool(5)

    def setHasTradeInWidget(self, value):
        self._setBool(5, value)
        return

    def getHasTradeInVehiclesToSelect(self):
        return self._getBool(6)

    def setHasTradeInVehiclesToSelect(self, value):
        self._setBool(6, value)
        return

    def getHasTradeInGoldConfirmation(self):
        return self._getBool(7)

    def setHasTradeInGoldConfirmation(self, value):
        self._setBool(7, value)
        return

    def getHasDisclaimer(self):
        return self._getBool(8)

    def setHasDisclaimer(self, value):
        self._setBool(8, value)
        return

    def getIsBuyButtonEnabled(self):
        return self._getBool(9)

    def setIsBuyButtonEnabled(self, value):
        self._setBool(9, value)
        return

    def getIsRentAvailable(self):
        return self._getBool(10)

    def setIsRentAvailable(self, value):
        self._setBool(10, value)
        return

    def getTitle(self):
        return self._getString(11)

    def setTitle(self, value):
        self._setString(11, value)
        return

    def getRentButtonLabel(self):
        return self._getString(12)

    def setRentButtonLabel(self, value):
        self._setString(12, value)
        return

    def getBuyButtonLabel(self):
        return self._getString(13)

    def setBuyButtonLabel(self, value):
        self._setString(13, value)
        return

    def getOptions(self):
        return self._getArray(14)

    def setOptions(self, value):
        self._setArray(14, value)
        return

    @staticmethod
    def getOptionsType():
        return BuyVehicleOptionModel

    def _initialize(self):
        super(BuyVehicleViewModel, self)._initialize()
        self._addViewModelProperty(b'vehicle', VehicleModel())
        self._addViewModelProperty(b'tradeInVehicleToSell', VehicleModel())
        self._addViewModelProperty(b'totals', BuyVehiclePriceModel())
        self._addViewModelProperty(b'buyButtonTooltip', BuyVehicleSimpleTooltipModel())
        self._addBoolProperty(b'isRestore', False)
        self._addBoolProperty(b'hasTradeInWidget', False)
        self._addBoolProperty(b'hasTradeInVehiclesToSelect', False)
        self._addBoolProperty(b'hasTradeInGoldConfirmation', False)
        self._addBoolProperty(b'hasDisclaimer', False)
        self._addBoolProperty(b'isBuyButtonEnabled', False)
        self._addBoolProperty(b'isRentAvailable', False)
        self._addStringProperty(b'title', b'')
        self._addStringProperty(b'rentButtonLabel', b'')
        self._addStringProperty(b'buyButtonLabel', b'')
        self._addArrayProperty(b'options', Array())
        self.onCloseBtnClick = self._addCommand(b'onCloseBtnClick')
        self.onBuyBtnClick = self._addCommand(b'onBuyBtnClick')
        self.onBackClick = self._addCommand(b'onBackClick')
        self.onOptionClick = self._addCommand(b'onOptionClick')
        self.onSelectTradeInVehicleToSell = self._addCommand(b'onSelectTradeInVehicleToSell')
        self.onClearTradeInVehicleToSell = self._addCommand(b'onClearTradeInVehicleToSell')
        self.onDisclaimerClick = self._addCommand(b'onDisclaimerClick')
        return
