from frameworks.wulf import ViewModel
from gui.impl.wrappers.user_list_model import UserListModel
from gui.impl.gen.view_models.views.lobby.lootbox_system.bonus_model import BonusModel

class SingleBoxRewardsViewModel(ViewModel):
    __slots__ = (b'onOpen', b'onGoBack', b'onPreview', b'onBuyBoxes', b'onAnimationStateChanged', b'onVideoPlaying', b'onClose')

    def __init__(self, properties=11, commands=7):
        super(SingleBoxRewardsViewModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def bonuses(self):
        return self._getViewModel(0)

    @staticmethod
    def getBonusesType():
        return BonusModel

    @property
    def extraBonuses(self):
        return self._getViewModel(1)

    @staticmethod
    def getExtraBonusesType():
        return BonusModel

    def getEventName(self):
        return self._getString(2)

    def setEventName(self, value):
        self._setString(2, value)
        return

    def getBoxCategory(self):
        return self._getString(3)

    def setBoxCategory(self, value):
        self._setString(3, value)
        return

    def getIsReopen(self):
        return self._getBool(4)

    def setIsReopen(self, value):
        self._setBool(4, value)
        return

    def getBoxesCount(self):
        return self._getNumber(5)

    def setBoxesCount(self, value):
        self._setNumber(5, value)
        return

    def getBoxesCountToGuaranteed(self):
        return self._getNumber(6)

    def setBoxesCountToGuaranteed(self, value):
        self._setNumber(6, value)
        return

    def getIsAnimationActive(self):
        return self._getBool(7)

    def setIsAnimationActive(self, value):
        self._setBool(7, value)
        return

    def getIsAwaitingResponse(self):
        return self._getBool(8)

    def setIsAwaitingResponse(self, value):
        self._setBool(8, value)
        return

    def getIsWindowAccessible(self):
        return self._getBool(9)

    def setIsWindowAccessible(self, value):
        self._setBool(9, value)
        return

    def getIsShopVisible(self):
        return self._getBool(10)

    def setIsShopVisible(self, value):
        self._setBool(10, value)
        return

    def _initialize(self):
        super(SingleBoxRewardsViewModel, self)._initialize()
        self._addViewModelProperty(b'bonuses', UserListModel())
        self._addViewModelProperty(b'extraBonuses', UserListModel())
        self._addStringProperty(b'eventName', b'')
        self._addStringProperty(b'boxCategory', b'')
        self._addBoolProperty(b'isReopen', False)
        self._addNumberProperty(b'boxesCount', 0)
        self._addNumberProperty(b'boxesCountToGuaranteed', 0)
        self._addBoolProperty(b'isAnimationActive', False)
        self._addBoolProperty(b'isAwaitingResponse', False)
        self._addBoolProperty(b'isWindowAccessible', False)
        self._addBoolProperty(b'isShopVisible', False)
        self.onOpen = self._addCommand(b'onOpen')
        self.onGoBack = self._addCommand(b'onGoBack')
        self.onPreview = self._addCommand(b'onPreview')
        self.onBuyBoxes = self._addCommand(b'onBuyBoxes')
        self.onAnimationStateChanged = self._addCommand(b'onAnimationStateChanged')
        self.onVideoPlaying = self._addCommand(b'onVideoPlaying')
        self.onClose = self._addCommand(b'onClose')
        return
