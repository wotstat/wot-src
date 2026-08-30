from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.views.lobby.lootbox_system.box_info_model import BoxInfoModel
from gui.impl.gen.view_models.views.lobby.lootbox_system.submodels.statistics_model import StatisticsModel

class HomeViewModel(ViewModel):
    __slots__ = (b'onInfoOpen', b'onBoxesOpen', b'onBuyBoxes', b'onAnimationStateChanged', b'onOpeningOptionChanged', b'onBoxOptionChanged', b'onClose', b'onResetError')

    def __init__(self, properties=11, commands=8):
        super(HomeViewModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def statistics(self):
        return self._getViewModel(0)

    @staticmethod
    def getStatisticsType():
        return StatisticsModel

    def getEventName(self):
        return self._getString(1)

    def setEventName(self, value):
        self._setString(1, value)
        return

    def getBoxesInfo(self):
        return self._getArray(2)

    def setBoxesInfo(self, value):
        self._setArray(2, value)
        return

    @staticmethod
    def getBoxesInfoType():
        return BoxInfoModel

    def getOpeningOptions(self):
        return self._getArray(3)

    def setOpeningOptions(self, value):
        self._setArray(3, value)
        return

    @staticmethod
    def getOpeningOptionsType():
        return int

    def getSelectedBoxOption(self):
        return self._getString(4)

    def setSelectedBoxOption(self, value):
        self._setString(4, value)
        return

    def getSelectedOpeningOption(self):
        return self._getNumber(5)

    def setSelectedOpeningOption(self, value):
        self._setNumber(5, value)
        return

    def getIsAnimationActive(self):
        return self._getBool(6)

    def setIsAnimationActive(self, value):
        self._setBool(6, value)
        return

    def getIsError(self):
        return self._getBool(7)

    def setIsError(self, value):
        self._setBool(7, value)
        return

    def getUseStats(self):
        return self._getBool(8)

    def setUseStats(self, value):
        self._setBool(8, value)
        return

    def getIsShopVisible(self):
        return self._getBool(9)

    def setIsShopVisible(self, value):
        self._setBool(9, value)
        return

    def getEventExpireTime(self):
        return self._getNumber(10)

    def setEventExpireTime(self, value):
        self._setNumber(10, value)
        return

    def _initialize(self):
        super(HomeViewModel, self)._initialize()
        self._addViewModelProperty(b'statistics', StatisticsModel())
        self._addStringProperty(b'eventName', b'')
        self._addArrayProperty(b'boxesInfo', Array())
        self._addArrayProperty(b'openingOptions', Array())
        self._addStringProperty(b'selectedBoxOption', b'')
        self._addNumberProperty(b'selectedOpeningOption', 0)
        self._addBoolProperty(b'isAnimationActive', False)
        self._addBoolProperty(b'isError', False)
        self._addBoolProperty(b'useStats', True)
        self._addBoolProperty(b'isShopVisible', False)
        self._addNumberProperty(b'eventExpireTime', 0)
        self.onInfoOpen = self._addCommand(b'onInfoOpen')
        self.onBoxesOpen = self._addCommand(b'onBoxesOpen')
        self.onBuyBoxes = self._addCommand(b'onBuyBoxes')
        self.onAnimationStateChanged = self._addCommand(b'onAnimationStateChanged')
        self.onOpeningOptionChanged = self._addCommand(b'onOpeningOptionChanged')
        self.onBoxOptionChanged = self._addCommand(b'onBoxOptionChanged')
        self.onClose = self._addCommand(b'onClose')
        self.onResetError = self._addCommand(b'onResetError')
        return
