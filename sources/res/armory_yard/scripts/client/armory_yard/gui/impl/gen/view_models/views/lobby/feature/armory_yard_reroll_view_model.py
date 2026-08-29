from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.common.price_model import PriceModel
from armory_yard.gui.impl.gen.view_models.views.lobby.feature.armory_yard_quest_sub_model import ArmoryYardQuestSubModel
from gui.impl.gen.view_models.views.dialogs.sub_views.money_balance_view_model import MoneyBalanceViewModel

class ArmoryYardRerollViewModel(ViewModel):
    __slots__ = (b'onReroll', b'onConfirm', b'onClose')

    def __init__(self, properties=14, commands=3):
        super(ArmoryYardRerollViewModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def currentQuest(self):
        return self._getViewModel(0)

    @staticmethod
    def getCurrentQuestType():
        return ArmoryYardQuestSubModel

    @property
    def price(self):
        return self._getViewModel(1)

    @staticmethod
    def getPriceType():
        return PriceModel

    @property
    def moneyBalance(self):
        return self._getViewModel(2)

    @staticmethod
    def getMoneyBalanceType():
        return MoneyBalanceViewModel

    def getFromTimestamp(self):
        return self._getNumber(3)

    def setFromTimestamp(self, value):
        self._setNumber(3, value)
        return

    def getToTimestamp(self):
        return self._getNumber(4)

    def setToTimestamp(self, value):
        self._setNumber(4, value)
        return

    def getFreeRerollCount(self):
        return self._getNumber(5)

    def setFreeRerollCount(self, value):
        self._setNumber(5, value)
        return

    def getRerollCountdown(self):
        return self._getNumber(6)

    def setRerollCountdown(self, value):
        self._setNumber(6, value)
        return

    def getIsPostProgression(self):
        return self._getBool(7)

    def setIsPostProgression(self, value):
        self._setBool(7, value)
        return

    def getIsPostProgressionQuest(self):
        return self._getBool(8)

    def setIsPostProgressionQuest(self, value):
        self._setBool(8, value)
        return

    def getIsPostProgressionFinished(self):
        return self._getBool(9)

    def setIsPostProgressionFinished(self, value):
        self._setBool(9, value)
        return

    def getCanCloseWindow(self):
        return self._getBool(10)

    def setCanCloseWindow(self, value):
        self._setBool(10, value)
        return

    def getIsPaymentError(self):
        return self._getBool(11)

    def setIsPaymentError(self, value):
        self._setBool(11, value)
        return

    def getIsIntroScreenVisited(self):
        return self._getBool(12)

    def setIsIntroScreenVisited(self, value):
        self._setBool(12, value)
        return

    def getSuggestedQuests(self):
        return self._getArray(13)

    def setSuggestedQuests(self, value):
        self._setArray(13, value)
        return

    @staticmethod
    def getSuggestedQuestsType():
        return ArmoryYardQuestSubModel

    def _initialize(self):
        super(ArmoryYardRerollViewModel, self)._initialize()
        self._addViewModelProperty(b'currentQuest', ArmoryYardQuestSubModel())
        self._addViewModelProperty(b'price', PriceModel())
        self._addViewModelProperty(b'moneyBalance', MoneyBalanceViewModel())
        self._addNumberProperty(b'fromTimestamp', 0)
        self._addNumberProperty(b'toTimestamp', 0)
        self._addNumberProperty(b'freeRerollCount', 0)
        self._addNumberProperty(b'rerollCountdown', 0)
        self._addBoolProperty(b'isPostProgression', False)
        self._addBoolProperty(b'isPostProgressionQuest', False)
        self._addBoolProperty(b'isPostProgressionFinished', False)
        self._addBoolProperty(b'canCloseWindow', True)
        self._addBoolProperty(b'isPaymentError', False)
        self._addBoolProperty(b'isIntroScreenVisited', True)
        self._addArrayProperty(b'suggestedQuests', Array())
        self.onReroll = self._addCommand(b'onReroll')
        self.onConfirm = self._addCommand(b'onConfirm')
        self.onClose = self._addCommand(b'onClose')
        return
