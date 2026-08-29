from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.collection.item_model import ItemModel
from gui.impl.gen.view_models.views.lobby.collection.page_backgrounds_model import PageBackgroundsModel
from gui.impl.gen.view_models.views.lobby.collection.reward_info_model import RewardInfoModel
from gui.impl.gen.view_models.views.lobby.collection.tab_model import TabModel

class CollectionViewModel(ViewModel):
    __slots__ = (b'onViewLoaded', b'onSetItemReceived', b'onSetRewardReceived', b'onSetProgressItemsReceived', b'onOpenItemPreview', b'onFinishTutorial', b'onTabSelected', b'onPageChanged', b'onClose')

    def __init__(self, properties=14, commands=9):
        super(CollectionViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getBackButtonText(self):
        return self._getString(0)

    def setBackButtonText(self, value):
        self._setString(0, value)
        return

    def getCurrentCollection(self):
        return self._getString(1)

    def setCurrentCollection(self, value):
        self._setString(1, value)
        return

    def getIsCompleted(self):
        return self._getBool(2)

    def setIsCompleted(self, value):
        self._setBool(2, value)
        return

    def getIsTutorial(self):
        return self._getBool(3)

    def setIsTutorial(self, value):
        self._setBool(3, value)
        return

    def getIsError(self):
        return self._getBool(4)

    def setIsError(self, value):
        self._setBool(4, value)
        return

    def getPage(self):
        return self._getNumber(5)

    def setPage(self, value):
        self._setNumber(5, value)
        return

    def getTabs(self):
        return self._getArray(6)

    def setTabs(self, value):
        self._setArray(6, value)
        return

    @staticmethod
    def getTabsType():
        return TabModel

    def getItems(self):
        return self._getArray(7)

    def setItems(self, value):
        self._setArray(7, value)
        return

    @staticmethod
    def getItemsType():
        return ItemModel

    def getMaxItemsCount(self):
        return self._getNumber(8)

    def setMaxItemsCount(self, value):
        self._setNumber(8, value)
        return

    def getReceivedItemsCount(self):
        return self._getNumber(9)

    def setReceivedItemsCount(self, value):
        self._setNumber(9, value)
        return

    def getPrevReceivedItemsCount(self):
        return self._getNumber(10)

    def setPrevReceivedItemsCount(self, value):
        self._setNumber(10, value)
        return

    def getRewardsInfo(self):
        return self._getArray(11)

    def setRewardsInfo(self, value):
        self._setArray(11, value)
        return

    @staticmethod
    def getRewardsInfoType():
        return RewardInfoModel

    def getGeneralBackground(self):
        return self._getString(12)

    def setGeneralBackground(self, value):
        self._setString(12, value)
        return

    def getPagesBackgrounds(self):
        return self._getArray(13)

    def setPagesBackgrounds(self, value):
        self._setArray(13, value)
        return

    @staticmethod
    def getPagesBackgroundsType():
        return PageBackgroundsModel

    def _initialize(self):
        super(CollectionViewModel, self)._initialize()
        self._addStringProperty(b'backButtonText', b'')
        self._addStringProperty(b'currentCollection', b'defaultConfig')
        self._addBoolProperty(b'isCompleted', False)
        self._addBoolProperty(b'isTutorial', True)
        self._addBoolProperty(b'isError', False)
        self._addNumberProperty(b'page', -1)
        self._addArrayProperty(b'tabs', Array())
        self._addArrayProperty(b'items', Array())
        self._addNumberProperty(b'maxItemsCount', 0)
        self._addNumberProperty(b'receivedItemsCount', 0)
        self._addNumberProperty(b'prevReceivedItemsCount', 0)
        self._addArrayProperty(b'rewardsInfo', Array())
        self._addStringProperty(b'generalBackground', b'')
        self._addArrayProperty(b'pagesBackgrounds', Array())
        self.onViewLoaded = self._addCommand(b'onViewLoaded')
        self.onSetItemReceived = self._addCommand(b'onSetItemReceived')
        self.onSetRewardReceived = self._addCommand(b'onSetRewardReceived')
        self.onSetProgressItemsReceived = self._addCommand(b'onSetProgressItemsReceived')
        self.onOpenItemPreview = self._addCommand(b'onOpenItemPreview')
        self.onFinishTutorial = self._addCommand(b'onFinishTutorial')
        self.onTabSelected = self._addCommand(b'onTabSelected')
        self.onPageChanged = self._addCommand(b'onPageChanged')
        self.onClose = self._addCommand(b'onClose')
        return
