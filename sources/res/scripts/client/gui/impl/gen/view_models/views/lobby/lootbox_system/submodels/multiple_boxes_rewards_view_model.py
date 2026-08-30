from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.views.lobby.lootbox_system.bonus_model import BonusModel

class MultipleBoxesRewardsViewModel(ViewModel):
    __slots__ = (b'onOpen', b'onGoBack', b'onPreview', b'onBuyBoxes', b'onAnimationStateChanged', b'onVideoPlaying', b'onClose')

    def __init__(self, properties=11, commands=7):
        super(MultipleBoxesRewardsViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getEventName(self):
        return self._getString(0)

    def setEventName(self, value):
        self._setString(0, value)
        return

    def getBoxCategory(self):
        return self._getString(1)

    def setBoxCategory(self, value):
        self._setString(1, value)
        return

    def getIsReopen(self):
        return self._getBool(2)

    def setIsReopen(self, value):
        self._setBool(2, value)
        return

    def getBoxesCount(self):
        return self._getNumber(3)

    def setBoxesCount(self, value):
        self._setNumber(3, value)
        return

    def getBoxesCountToGuaranteed(self):
        return self._getNumber(4)

    def setBoxesCountToGuaranteed(self, value):
        self._setNumber(4, value)
        return

    def getOpeningCount(self):
        return self._getNumber(5)

    def setOpeningCount(self, value):
        self._setNumber(5, value)
        return

    def getIsAnimationActive(self):
        return self._getBool(6)

    def setIsAnimationActive(self, value):
        self._setBool(6, value)
        return

    def getIsAwaitingResponse(self):
        return self._getBool(7)

    def setIsAwaitingResponse(self, value):
        self._setBool(7, value)
        return

    def getIsWindowAccessible(self):
        return self._getBool(8)

    def setIsWindowAccessible(self, value):
        self._setBool(8, value)
        return

    def getIsShopVisible(self):
        return self._getBool(9)

    def setIsShopVisible(self, value):
        self._setBool(9, value)
        return

    def getBonuses(self):
        return self._getArray(10)

    def setBonuses(self, value):
        self._setArray(10, value)
        return

    @staticmethod
    def getBonusesType():
        return Array[BonusModel]

    def _initialize(self):
        super(MultipleBoxesRewardsViewModel, self)._initialize()
        self._addStringProperty(b'eventName', b'')
        self._addStringProperty(b'boxCategory', b'')
        self._addBoolProperty(b'isReopen', False)
        self._addNumberProperty(b'boxesCount', 0)
        self._addNumberProperty(b'boxesCountToGuaranteed', 0)
        self._addNumberProperty(b'openingCount', 0)
        self._addBoolProperty(b'isAnimationActive', False)
        self._addBoolProperty(b'isAwaitingResponse', False)
        self._addBoolProperty(b'isWindowAccessible', False)
        self._addBoolProperty(b'isShopVisible', False)
        self._addArrayProperty(b'bonuses', Array())
        self.onOpen = self._addCommand(b'onOpen')
        self.onGoBack = self._addCommand(b'onGoBack')
        self.onPreview = self._addCommand(b'onPreview')
        self.onBuyBoxes = self._addCommand(b'onBuyBoxes')
        self.onAnimationStateChanged = self._addCommand(b'onAnimationStateChanged')
        self.onVideoPlaying = self._addCommand(b'onVideoPlaying')
        self.onClose = self._addCommand(b'onClose')
        return
