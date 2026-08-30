from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.battle_pass.chapter_model import ChapterModel
from gui.impl.gen.view_models.views.lobby.battle_pass.collection_entry_point_view_model import CollectionEntryPointViewModel

class ChapterChoiceViewModel(ViewModel):
    __slots__ = (b'onPreviewClick', b'onChapterSelect', b'onAboutClick', b'onPointsInfoClick', b'onBuyClick', b'onBpbitClick', b'onBpcoinClick', b'onTakeRewardsClick', b'onViewLoaded', b'onClose', b'onActivateChapter')

    def __init__(self, properties=12, commands=11):
        super(ChapterChoiceViewModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def collectionEntryPoint(self):
        return self._getViewModel(0)

    @staticmethod
    def getCollectionEntryPointType():
        return CollectionEntryPointViewModel

    def getChapters(self):
        return self._getArray(1)

    def setChapters(self, value):
        self._setArray(1, value)
        return

    @staticmethod
    def getChaptersType():
        return ChapterModel

    def getBpbitCount(self):
        return self._getNumber(2)

    def setBpbitCount(self, value):
        self._setNumber(2, value)
        return

    def getNotChosenRewardCount(self):
        return self._getNumber(3)

    def setNotChosenRewardCount(self, value):
        self._setNumber(3, value)
        return

    def getBpcoinCount(self):
        return self._getNumber(4)

    def setBpcoinCount(self, value):
        self._setNumber(4, value)
        return

    def getIsBattlePassCompleted(self):
        return self._getBool(5)

    def setIsBattlePassCompleted(self, value):
        self._setBool(5, value)
        return

    def getIsChooseRewardsEnabled(self):
        return self._getBool(6)

    def setIsChooseRewardsEnabled(self, value):
        self._setBool(6, value)
        return

    def getFreePoints(self):
        return self._getNumber(7)

    def setFreePoints(self, value):
        self._setNumber(7, value)
        return

    def getShowHint(self):
        return self._getBool(8)

    def setShowHint(self, value):
        self._setBool(8, value)
        return

    def getIsBpCoinShopEntryPointActive(self):
        return self._getBool(9)

    def setIsBpCoinShopEntryPointActive(self, value):
        self._setBool(9, value)
        return

    def getIsBpPointsShopEntryPointActive(self):
        return self._getBool(10)

    def setIsBpPointsShopEntryPointActive(self, value):
        self._setBool(10, value)
        return

    def getIsSingleChapter(self):
        return self._getBool(11)

    def setIsSingleChapter(self, value):
        self._setBool(11, value)
        return

    def _initialize(self):
        super(ChapterChoiceViewModel, self)._initialize()
        self._addViewModelProperty(b'collectionEntryPoint', CollectionEntryPointViewModel())
        self._addArrayProperty(b'chapters', Array())
        self._addNumberProperty(b'bpbitCount', 0)
        self._addNumberProperty(b'notChosenRewardCount', 0)
        self._addNumberProperty(b'bpcoinCount', 0)
        self._addBoolProperty(b'isBattlePassCompleted', False)
        self._addBoolProperty(b'isChooseRewardsEnabled', True)
        self._addNumberProperty(b'freePoints', 0)
        self._addBoolProperty(b'showHint', False)
        self._addBoolProperty(b'isBpCoinShopEntryPointActive', False)
        self._addBoolProperty(b'isBpPointsShopEntryPointActive', False)
        self._addBoolProperty(b'isSingleChapter', False)
        self.onPreviewClick = self._addCommand(b'onPreviewClick')
        self.onChapterSelect = self._addCommand(b'onChapterSelect')
        self.onAboutClick = self._addCommand(b'onAboutClick')
        self.onPointsInfoClick = self._addCommand(b'onPointsInfoClick')
        self.onBuyClick = self._addCommand(b'onBuyClick')
        self.onBpbitClick = self._addCommand(b'onBpbitClick')
        self.onBpcoinClick = self._addCommand(b'onBpcoinClick')
        self.onTakeRewardsClick = self._addCommand(b'onTakeRewardsClick')
        self.onViewLoaded = self._addCommand(b'onViewLoaded')
        self.onClose = self._addCommand(b'onClose')
        self.onActivateChapter = self._addCommand(b'onActivateChapter')
        return
