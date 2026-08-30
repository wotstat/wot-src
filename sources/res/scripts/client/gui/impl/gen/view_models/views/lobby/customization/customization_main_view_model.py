from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.customization.customization_bill_data_model import CustomizationBillDataModel
from gui.impl.gen.view_models.views.lobby.customization.customization_carousel_model import CustomizationCarouselModel
from gui.impl.gen.view_models.views.lobby.customization.customization_filter_model import CustomizationFilterModel
from gui.impl.gen.view_models.views.lobby.customization.customization_header_vehicle_info_model import CustomizationHeaderVehicleInfoModel
from gui.impl.gen.view_models.views.lobby.customization.customization_magnetic_tool_model import CustomizationMagneticToolModel
from gui.impl.gen.view_models.views.lobby.customization.customization_markers_model import CustomizationMarkersModel
from gui.impl.gen.view_models.views.lobby.customization.customization_seasons_model import CustomizationSeasonsModel
from gui.impl.gen.view_models.views.lobby.customization.customization_tabs_model import CustomizationTabsModel
from gui.impl.gen.view_models.views.lobby.customization.customization_toolbar_model import CustomizationToolbarModel
from gui.impl.gen.view_models.views.lobby.customization.progression_styles.stage_switcher_widget_model import StageSwitcherWidgetModel

class CustomizationMainViewModel(ViewModel):
    __slots__ = (b'onClose', b'onCloseCarouselView', b'onCloseBinEsc', b'onCloseStyleInfoEsc', b'onExpandCarousel', b'onMoveSpace', b'onSelectItem', b'onUnselectItem', b'onSelectTab', b'onSelectSeason', b'onApplyToAllSeasonsChange', b'changeFilter', b'clearFilter', b'onHoverItem', b'onHoverTab', b'onClickDecalsBanner', b'onEditItem', b'onCloseEditItem', b'onSceneOverChange', b'onSceneDraggingChange', b'onSceneClick', b'onBuyItems', b'onProgressiveInfoButtonClick', b'onPressSelectNextItem', b'onRequestItems')

    def __init__(self, properties=20, commands=25):
        super(CustomizationMainViewModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def carouselModel(self):
        return self._getViewModel(0)

    @staticmethod
    def getCarouselModelType():
        return CustomizationCarouselModel

    @property
    def tabsModel(self):
        return self._getViewModel(1)

    @staticmethod
    def getTabsModelType():
        return CustomizationTabsModel

    @property
    def filterModel(self):
        return self._getViewModel(2)

    @staticmethod
    def getFilterModelType():
        return CustomizationFilterModel

    @property
    def billModel(self):
        return self._getViewModel(3)

    @staticmethod
    def getBillModelType():
        return CustomizationBillDataModel

    @property
    def seasonsModel(self):
        return self._getViewModel(4)

    @staticmethod
    def getSeasonsModelType():
        return CustomizationSeasonsModel

    @property
    def headerVehicleInfoModel(self):
        return self._getViewModel(5)

    @staticmethod
    def getHeaderVehicleInfoModelType():
        return CustomizationHeaderVehicleInfoModel

    @property
    def markersModel(self):
        return self._getViewModel(6)

    @staticmethod
    def getMarkersModelType():
        return CustomizationMarkersModel

    @property
    def toolbarModel(self):
        return self._getViewModel(7)

    @staticmethod
    def getToolbarModelType():
        return CustomizationToolbarModel

    @property
    def stageSwitcherWidgetModel(self):
        return self._getViewModel(8)

    @staticmethod
    def getStageSwitcherWidgetModelType():
        return StageSwitcherWidgetModel

    @property
    def magneticToolModel(self):
        return self._getViewModel(9)

    @staticmethod
    def getMagneticToolModelType():
        return CustomizationMagneticToolModel

    def getIsEditable(self):
        return self._getBool(10)

    def setIsEditable(self, value):
        self._setBool(10, value)
        return

    def getIsApplyToAllSeasonsAvailable(self):
        return self._getBool(11)

    def setIsApplyToAllSeasonsAvailable(self, value):
        self._setBool(11, value)
        return

    def getIsApplyToAllSeasonsSelected(self):
        return self._getBool(12)

    def setIsApplyToAllSeasonsSelected(self, value):
        self._setBool(12, value)
        return

    def getIsBuyViewActive(self):
        return self._getBool(13)

    def setIsBuyViewActive(self, value):
        self._setBool(13, value)
        return

    def getIsShowProgressionInfoButton(self):
        return self._getBool(14)

    def setIsShowProgressionInfoButton(self, value):
        self._setBool(14, value)
        return

    def getIsStyleInfoViewActive(self):
        return self._getBool(15)

    def setIsStyleInfoViewActive(self, value):
        self._setBool(15, value)
        return

    def getIsHoverVehicleSlot(self):
        return self._getBool(16)

    def setIsHoverVehicleSlot(self, value):
        self._setBool(16, value)
        return

    def getIsProgressiveItemsViewVisible(self):
        return self._getBool(17)

    def setIsProgressiveItemsViewVisible(self, value):
        self._setBool(17, value)
        return

    def getIsFilterPopoverOpened(self):
        return self._getBool(18)

    def setIsFilterPopoverOpened(self, value):
        self._setBool(18, value)
        return

    def getIsOnboardingViewOpened(self):
        return self._getBool(19)

    def setIsOnboardingViewOpened(self, value):
        self._setBool(19, value)
        return

    def _initialize(self):
        super(CustomizationMainViewModel, self)._initialize()
        self._addViewModelProperty(b'carouselModel', CustomizationCarouselModel())
        self._addViewModelProperty(b'tabsModel', CustomizationTabsModel())
        self._addViewModelProperty(b'filterModel', CustomizationFilterModel())
        self._addViewModelProperty(b'billModel', CustomizationBillDataModel())
        self._addViewModelProperty(b'seasonsModel', CustomizationSeasonsModel())
        self._addViewModelProperty(b'headerVehicleInfoModel', CustomizationHeaderVehicleInfoModel())
        self._addViewModelProperty(b'markersModel', CustomizationMarkersModel())
        self._addViewModelProperty(b'toolbarModel', CustomizationToolbarModel())
        self._addViewModelProperty(b'stageSwitcherWidgetModel', StageSwitcherWidgetModel())
        self._addViewModelProperty(b'magneticToolModel', CustomizationMagneticToolModel())
        self._addBoolProperty(b'isEditable', False)
        self._addBoolProperty(b'isApplyToAllSeasonsAvailable', False)
        self._addBoolProperty(b'isApplyToAllSeasonsSelected', False)
        self._addBoolProperty(b'isBuyViewActive', False)
        self._addBoolProperty(b'isShowProgressionInfoButton', False)
        self._addBoolProperty(b'isStyleInfoViewActive', False)
        self._addBoolProperty(b'isHoverVehicleSlot', False)
        self._addBoolProperty(b'isProgressiveItemsViewVisible', False)
        self._addBoolProperty(b'isFilterPopoverOpened', False)
        self._addBoolProperty(b'isOnboardingViewOpened', False)
        self.onClose = self._addCommand(b'onClose')
        self.onCloseCarouselView = self._addCommand(b'onCloseCarouselView')
        self.onCloseBinEsc = self._addCommand(b'onCloseBinEsc')
        self.onCloseStyleInfoEsc = self._addCommand(b'onCloseStyleInfoEsc')
        self.onExpandCarousel = self._addCommand(b'onExpandCarousel')
        self.onMoveSpace = self._addCommand(b'onMoveSpace')
        self.onSelectItem = self._addCommand(b'onSelectItem')
        self.onUnselectItem = self._addCommand(b'onUnselectItem')
        self.onSelectTab = self._addCommand(b'onSelectTab')
        self.onSelectSeason = self._addCommand(b'onSelectSeason')
        self.onApplyToAllSeasonsChange = self._addCommand(b'onApplyToAllSeasonsChange')
        self.changeFilter = self._addCommand(b'changeFilter')
        self.clearFilter = self._addCommand(b'clearFilter')
        self.onHoverItem = self._addCommand(b'onHoverItem')
        self.onHoverTab = self._addCommand(b'onHoverTab')
        self.onClickDecalsBanner = self._addCommand(b'onClickDecalsBanner')
        self.onEditItem = self._addCommand(b'onEditItem')
        self.onCloseEditItem = self._addCommand(b'onCloseEditItem')
        self.onSceneOverChange = self._addCommand(b'onSceneOverChange')
        self.onSceneDraggingChange = self._addCommand(b'onSceneDraggingChange')
        self.onSceneClick = self._addCommand(b'onSceneClick')
        self.onBuyItems = self._addCommand(b'onBuyItems')
        self.onProgressiveInfoButtonClick = self._addCommand(b'onProgressiveInfoButtonClick')
        self.onPressSelectNextItem = self._addCommand(b'onPressSelectNextItem')
        self.onRequestItems = self._addCommand(b'onRequestItems')
        return
