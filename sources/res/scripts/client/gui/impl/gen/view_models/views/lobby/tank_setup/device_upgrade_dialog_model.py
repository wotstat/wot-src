from frameworks.wulf import Array
from gui.impl.gen.view_models.common.price_item_model import PriceItemModel
from gui.impl.gen.view_models.views.dialogs.dialog_template_view_model import DialogTemplateViewModel
from gui.impl.gen.view_models.views.lobby.tank_setup.dialogs.sub_views.current_balance_model import CurrentBalanceModel
from gui.impl.gen.view_models.views.lobby.tank_setup.kpi_equip_level_model import KpiEquipLevelModel

class DeviceUpgradeDialogModel(DialogTemplateViewModel):
    __slots__ = ()

    def __init__(self, properties=15, commands=2):
        super(DeviceUpgradeDialogModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def prices(self):
        return self._getViewModel(6)

    @staticmethod
    def getPricesType():
        return PriceItemModel

    def getDeviceName(self):
        return self._getString(7)

    def setDeviceName(self, value):
        self._setString(7, value)
        return

    def getDeviceImg(self):
        return self._getString(8)

    def setDeviceImg(self, value):
        self._setString(8, value)
        return

    def getKpiItems(self):
        return self._getArray(9)

    def setKpiItems(self, value):
        self._setArray(9, value)
        return

    @staticmethod
    def getKpiItemsType():
        return KpiEquipLevelModel

    def getCurrencyValue(self):
        return self._getNumber(10)

    def setCurrencyValue(self, value):
        self._setNumber(10, value)
        return

    def getCurrentModuleIdx(self):
        return self._getNumber(11)

    def setCurrentModuleIdx(self, value):
        self._setNumber(11, value)
        return

    def getCanGetMoreCurrency(self):
        return self._getBool(12)

    def setCanGetMoreCurrency(self, value):
        self._setBool(12, value)
        return

    def getOverlayType(self):
        return self._getString(13)

    def setOverlayType(self, value):
        self._setString(13, value)
        return

    def getBalance(self):
        return self._getArray(14)

    def setBalance(self, value):
        self._setArray(14, value)
        return

    @staticmethod
    def getBalanceType():
        return CurrentBalanceModel

    def _initialize(self):
        super(DeviceUpgradeDialogModel, self)._initialize()
        self._addViewModelProperty(b'prices', PriceItemModel())
        self._addStringProperty(b'deviceName', b'')
        self._addStringProperty(b'deviceImg', b'')
        self._addArrayProperty(b'kpiItems', Array())
        self._addNumberProperty(b'currencyValue', 0)
        self._addNumberProperty(b'currentModuleIdx', 0)
        self._addBoolProperty(b'canGetMoreCurrency', False)
        self._addStringProperty(b'overlayType', b'')
        self._addArrayProperty(b'balance', Array())
        return
