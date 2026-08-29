from frameworks.wulf import Array
from gui.impl.gen.view_models.views.lobby.tank_setup.sub_views.base_setup_model import BaseSetupModel
from gui.impl.gen.view_models.views.lobby.tank_setup.sub_views.opt_device_filter_model import OptDeviceFilterModel
from gui.impl.gen.view_models.views.lobby.tank_setup.sub_views.opt_device_slot_model import OptDeviceSlotModel
from gui.impl.gen.view_models.views.lobby.tank_setup.sub_views.special_currency_model import SpecialCurrencyModel

class OptDevicesSetupModel(BaseSetupModel):
    __slots__ = (b'onIntroPassed',)

    def __init__(self, properties=12, commands=8):
        super(OptDevicesSetupModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def filter(self):
        return self._getViewModel(5)

    @staticmethod
    def getFilterType():
        return OptDeviceFilterModel

    @property
    def specialCurrency(self):
        return self._getViewModel(6)

    @staticmethod
    def getSpecialCurrencyType():
        return SpecialCurrencyModel

    def getHasUnfitItems(self):
        return self._getBool(7)

    def setHasUnfitItems(self, value):
        self._setBool(7, value)
        return

    def getSlots(self):
        return self._getArray(8)

    def setSlots(self, value):
        self._setArray(8, value)
        return

    @staticmethod
    def getSlotsType():
        return OptDeviceSlotModel

    def getWithIntroduction(self):
        return self._getBool(9)

    def setWithIntroduction(self, value):
        self._setBool(9, value)
        return

    def getIntroductionType(self):
        return self._getString(10)

    def setIntroductionType(self, value):
        self._setString(10, value)
        return

    def getIsOptDeviceRestored(self):
        return self._getBool(11)

    def setIsOptDeviceRestored(self, value):
        self._setBool(11, value)
        return

    def _initialize(self):
        super(OptDevicesSetupModel, self)._initialize()
        self._addViewModelProperty(b'filter', OptDeviceFilterModel())
        self._addViewModelProperty(b'specialCurrency', SpecialCurrencyModel())
        self._addBoolProperty(b'hasUnfitItems', False)
        self._addArrayProperty(b'slots', Array())
        self._addBoolProperty(b'withIntroduction', False)
        self._addStringProperty(b'introductionType', b'')
        self._addBoolProperty(b'isOptDeviceRestored', True)
        self.onIntroPassed = self._addCommand(b'onIntroPassed')
        return
