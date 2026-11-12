from frameworks.wulf import ViewSettings, WindowLayer
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.customization_resource.customization_resource_filter_popover_view_model import CustomizationResourceFilterPopoverViewModel
from gui.impl.pub import PopOverViewImpl, PopOverWindow
from helpers import dependency
from skeletons.gui.game_control import ICustomizationResourceController

class CustomizationResourceFilterPopoverView(PopOverViewImpl):
    __customizationResourceController = dependency.descriptor(ICustomizationResourceController)
    __slots__ = (b'__activeTabId', b'__filters', b'__dataProvider', b'__parent')

    def __init__(self, layoutID, activeTabId, filters, dataProvider, parent):
        settings = ViewSettings(layoutID)
        settings.model = CustomizationResourceFilterPopoverViewModel()
        super(CustomizationResourceFilterPopoverView, self).__init__(settings)
        self.__dataProvider = dataProvider
        self.__activeTabId = activeTabId
        self.__filters = filters
        self.__parent = parent
        return

    @property
    def viewModel(self):
        return super(CustomizationResourceFilterPopoverView, self).getViewModel()

    def _getEvents(self):
        return (
         (
          self.viewModel.changeFilter, self.__changeFilter),
         (
          self.viewModel.clearFilter, self.__clearFilter))

    def _onLoading(self, *args, **kwargs):
        super(CustomizationResourceFilterPopoverView, self)._onLoading(*args, **kwargs)
        self.__fillModel()
        return

    def __fillModel(self):
        activeItems = self.__dataProvider.getItems(self.__activeTabId)
        groups = self.__filters.getGroups(activeItems, self.__activeTabId)
        visibleItems = self.__filters.apply(activeItems, self.__activeTabId)
        with self.viewModel.transaction() as model:
            filterModel = model.filterModel
            filterData = self.__filters.getFilterData()
            filterModel.setAvailability(filterData[b'availability'])
            filterModel.setApplied(filterData[b'applied'])
            filterModel.setInventory(filterData[b'inventory'])
            filterModel.setFavorite(filterData[b'favorite'])
            filterModel.setHistoric(filterData[b'historic'])
            filterModel.setNonHistoric(filterData[b'nonHistoric'])
            filterModel.setFantastical(filterData[b'fantastical'])
            filterModel.setOnlyEditableStyles(filterData[b'onlyEditableStyles'])
            filterModel.setOnlyNonEditableStyles(filterData[b'onlyNonEditableStyles'])
            filterModel.setOnlyProgressionStyles(filterData[b'onlyProgressionStyles'])
            filterModel.setOnlyProgressionDecals(filterData[b'onlyProgressionDecals'])
            filterModel.setFormfactor_square(filterData[b'formfactor_square'])
            filterModel.setFormfactor_rect1x2(filterData[b'formfactor_rect1x2'])
            filterModel.setFormfactor_rect1x3(filterData[b'formfactor_rect1x3'])
            filterModel.setFormfactor_rect1x4(filterData[b'formfactor_rect1x4'])
            filterModel.setFormfactor_rect1x6(filterData[b'formfactor_rect1x6'])
            filterModel.setSelectedGroup(self.__filters.getSelectedGroup(self.__activeTabId, groups))
            filterModel.setIsFilteringActive(self.__filters.hasAppliedFilter(self.__activeTabId, groups))
            filterModel.setFilteredItemsCounter(len(visibleItems))
            filterModel.setAllItemsCounter(len(activeItems))
            groupsModel = filterModel.getGroups()
            groupsModel.clear()
            for group in groups:
                groupsModel.addString(group)

            groupsModel.invalidate()
            structureModel = filterModel.getStructure()
            structureModel.clear()
            for block in self.__filters.getStructure(activeItems, self.__activeTabId, groups):
                structureModel.addString(block)

            structureModel.invalidate()
        return

    def __changeFilter(self, args):
        items = self.__dataProvider.getItems(self.__activeTabId)
        groups = self.__filters.getGroups(items, self.__activeTabId)
        self.__filters.change(args.get(b'key'), args.get(b'value'), self.__activeTabId, groups)
        self.__fillModel()
        self.__parent.content.updateFilterState()
        return

    def __clearFilter(self):
        self.__filters.clear()
        self.__fillModel()
        self.__parent.content.updateFilterState()
        return


class CustomizationResourceFilterPopoverViewWindow(PopOverWindow):
    __slots__ = ()

    def __init__(self, event, activeTabId, filters, dataProvider, parent=None):
        super(CustomizationResourceFilterPopoverViewWindow, self).__init__(event=event, content=CustomizationResourceFilterPopoverView(R.views.lobby.customization_resource.CustomizationResourceFilterPopoverView(), activeTabId, filters, dataProvider, parent), parent=parent, layer=WindowLayer.TOP_WINDOW)
        return
