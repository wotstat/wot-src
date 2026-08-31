from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.views.lobby.lootbox_system.box_info_model import BoxInfoModel
from gui.impl.gen.view_models.views.lobby.lootbox_system.submodels.statistics_model import StatisticsModel

class NoBoxesViewModel(ViewModel):
    __slots__ = (b'onInfoOpen', b'onBuyBoxes', b'onClose')

    def __init__(self, properties=5, commands=3):
        super(NoBoxesViewModel, self).__init__(properties=properties, commands=commands)
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

    def getUseStats(self):
        return self._getBool(3)

    def setUseStats(self, value):
        self._setBool(3, value)
        return

    def getIsShopVisible(self):
        return self._getBool(4)

    def setIsShopVisible(self, value):
        self._setBool(4, value)
        return

    def _initialize(self):
        super(NoBoxesViewModel, self)._initialize()
        self._addViewModelProperty(b'statistics', StatisticsModel())
        self._addStringProperty(b'eventName', b'')
        self._addArrayProperty(b'boxesInfo', Array())
        self._addBoolProperty(b'useStats', True)
        self._addBoolProperty(b'isShopVisible', False)
        self.onInfoOpen = self._addCommand(b'onInfoOpen')
        self.onBuyBoxes = self._addCommand(b'onBuyBoxes')
        self.onClose = self._addCommand(b'onClose')
        return
