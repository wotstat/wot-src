from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.battle_pass.collection_entry_point_view_model import CollectionEntryPointViewModel

class AwardsWidgetModel(ViewModel):
    __slots__ = (b'onBpcoinClick', b'onTakeRewardsClick', b'showTankmen', b'showTickets', b'showTalers')

    def __init__(self, properties=10, commands=5):
        super(AwardsWidgetModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def collectionEntryPoint(self):
        return self._getViewModel(0)

    @staticmethod
    def getCollectionEntryPointType():
        return CollectionEntryPointViewModel

    def getTalerCount(self):
        return self._getNumber(1)

    def setTalerCount(self, value):
        self._setNumber(1, value)
        return

    def getNotChosenRewardCount(self):
        return self._getNumber(2)

    def setNotChosenRewardCount(self, value):
        self._setNumber(2, value)
        return

    def getBpcoinCount(self):
        return self._getNumber(3)

    def setBpcoinCount(self, value):
        self._setNumber(3, value)
        return

    def getTicketsCount(self):
        return self._getNumber(4)

    def setTicketsCount(self, value):
        self._setNumber(4, value)
        return

    def getIsChooseRewardsEnabled(self):
        return self._getBool(5)

    def setIsChooseRewardsEnabled(self, value):
        self._setBool(5, value)
        return

    def getTankmenScreenID(self):
        return self._getNumber(6)

    def setTankmenScreenID(self, value):
        self._setNumber(6, value)
        return

    def getIsTalerEnabled(self):
        return self._getBool(7)

    def setIsTalerEnabled(self, value):
        self._setBool(7, value)
        return

    def getIsBpCoinEnabled(self):
        return self._getBool(8)

    def setIsBpCoinEnabled(self, value):
        self._setBool(8, value)
        return

    def getIsTicketsEnabled(self):
        return self._getBool(9)

    def setIsTicketsEnabled(self, value):
        self._setBool(9, value)
        return

    def _initialize(self):
        super(AwardsWidgetModel, self)._initialize()
        self._addViewModelProperty(b'collectionEntryPoint', CollectionEntryPointViewModel())
        self._addNumberProperty(b'talerCount', 0)
        self._addNumberProperty(b'notChosenRewardCount', 0)
        self._addNumberProperty(b'bpcoinCount', 0)
        self._addNumberProperty(b'ticketsCount', 0)
        self._addBoolProperty(b'isChooseRewardsEnabled', True)
        self._addNumberProperty(b'tankmenScreenID', 0)
        self._addBoolProperty(b'isTalerEnabled', False)
        self._addBoolProperty(b'isBpCoinEnabled', False)
        self._addBoolProperty(b'isTicketsEnabled', False)
        self.onBpcoinClick = self._addCommand(b'onBpcoinClick')
        self.onTakeRewardsClick = self._addCommand(b'onTakeRewardsClick')
        self.showTankmen = self._addCommand(b'showTankmen')
        self.showTickets = self._addCommand(b'showTickets')
        self.showTalers = self._addCommand(b'showTalers')
        return
