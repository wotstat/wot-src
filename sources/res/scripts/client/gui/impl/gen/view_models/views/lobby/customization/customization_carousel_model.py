from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.customization.customization_carousel_arrow_model import CustomizationCarouselArrowModel
from gui.impl.gen.view_models.views.lobby.customization.customization_carousel_bookmark_model import CustomizationCarouselBookmarkModel
from gui.impl.gen.view_models.views.lobby.customization.customization_carousel_item_model import CustomizationCarouselItemModel

class CustomizationCarouselModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=11, commands=0):
        super(CustomizationCarouselModel, self).__init__(properties=properties, commands=commands)
        return

    def getIsProgressionDecalsBannerVisible(self):
        return self._getBool(0)

    def setIsProgressionDecalsBannerVisible(self, value):
        self._setBool(0, value)
        return

    def getIsLeftAvailable(self):
        return self._getBool(1)

    def setIsLeftAvailable(self, value):
        self._setBool(1, value)
        return

    def getIsCarouselArrowsHintVisible(self):
        return self._getBool(2)

    def setIsCarouselArrowsHintVisible(self, value):
        self._setBool(2, value)
        return

    def getIsRightAvailable(self):
        return self._getBool(3)

    def setIsRightAvailable(self, value):
        self._setBool(3, value)
        return

    def getTotalItemsCount(self):
        return self._getNumber(4)

    def setTotalItemsCount(self, value):
        self._setNumber(4, value)
        return

    def getFilteredItemsCount(self):
        return self._getNumber(5)

    def setFilteredItemsCount(self, value):
        self._setNumber(5, value)
        return

    def getShouldShowCounts(self):
        return self._getArray(6)

    def setShouldShowCounts(self, value):
        self._setArray(6, value)
        return

    @staticmethod
    def getShouldShowCountsType():
        return int

    def getCarouselItemsList(self):
        return self._getArray(7)

    def setCarouselItemsList(self, value):
        self._setArray(7, value)
        return

    @staticmethod
    def getCarouselItemsListType():
        return CustomizationCarouselItemModel

    def getBookmarksList(self):
        return self._getArray(8)

    def setBookmarksList(self, value):
        self._setArray(8, value)
        return

    @staticmethod
    def getBookmarksListType():
        return CustomizationCarouselBookmarkModel

    def getArrowsList(self):
        return self._getArray(9)

    def setArrowsList(self, value):
        self._setArray(9, value)
        return

    @staticmethod
    def getArrowsListType():
        return CustomizationCarouselArrowModel

    def getScrollStartItemId(self):
        return self._getNumber(10)

    def setScrollStartItemId(self, value):
        self._setNumber(10, value)
        return

    def _initialize(self):
        super(CustomizationCarouselModel, self)._initialize()
        self._addBoolProperty(b'isProgressionDecalsBannerVisible', False)
        self._addBoolProperty(b'isLeftAvailable', False)
        self._addBoolProperty(b'isCarouselArrowsHintVisible', False)
        self._addBoolProperty(b'isRightAvailable', False)
        self._addNumberProperty(b'totalItemsCount', 0)
        self._addNumberProperty(b'filteredItemsCount', 0)
        self._addArrayProperty(b'shouldShowCounts', Array())
        self._addArrayProperty(b'carouselItemsList', Array())
        self._addArrayProperty(b'bookmarksList', Array())
        self._addArrayProperty(b'arrowsList', Array())
        self._addNumberProperty(b'scrollStartItemId', 0)
        return
