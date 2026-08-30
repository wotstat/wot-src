import BigWorld, typing
from account_helpers import AccountSettings
from account_helpers.AccountSettings import COMP7_PREBATTLE_CAROUSEL_ROW_VALUE
from Event import Event, EventManager
from constants import REQUEST_COOLDOWN
from frameworks.wulf import ViewFlags, ViewSettings
from gui.Scaleform.daapi.view.common.vehicle_carousel.carousel_environment import ICarouselEnvironment, formatCountString
from gui.Scaleform.daapi.view.common.vehicle_carousel.carousel_filter import FILTER_KEYS
from gui.Scaleform.genConsts.BATTLE_VIEW_ALIASES import BATTLE_VIEW_ALIASES
from gui.app_loader import sf_battle
from gui.battle_pass.battle_pass_decorators import createBackportTooltipDecorator
from gui.impl.backport.backport_pop_over import createPopOverData, BackportPopOverContent
from gui.impl.battle.battle_page.carousel.prebattle_carousel_data import PrebattleCarouselDataProvider, PrebattleCarouselFilter
from gui.impl.gen import R
from gui.impl.gen.view_models.views.battle.battle_page.prebattle_carousel_view_model import PrebattleCarouselViewModel
from gui.impl.gen.view_models.views.battle.battle_page.prebattle_vehicle_model import PrebattleVehicleModel
from gui.impl.pub import ViewImpl
from gui.impl.lobby.common.vehicle_model_helpers import fillVehicleModel
from gui.impl.wrappers.function_helpers import replaceNoneKwargsModel
from gui.shared import g_eventBus
from gui.shared.events import HidePopoverEvent
from helpers import dependency
from skeletons.gui.battle_session import IBattleSessionProvider
from skeletons.gui.shared import IItemsCache
if typing.TYPE_CHECKING:
    from gui.battle_control.arena_info.interfaces import IComp7PrebattleSetupController

class PrebattleCarouselView(ViewImpl, ICarouselEnvironment):
    __slots__ = (b'onViewLoaded', b'_dataProvider', b'__eventManager', b'__filterPopoverRemoveCallback', b'__cooldownCallback')
    __sessionProvider = dependency.descriptor(IBattleSessionProvider)
    __itemsCache = dependency.descriptor(IItemsCache)

    def __init__(self, *args):
        settings = ViewSettings(layoutID=R.views.battle.battle_page.PrebattleCarouselView(), flags=ViewFlags.VIEW, model=PrebattleCarouselViewModel(), args=args)
        super(PrebattleCarouselView, self).__init__(settings)
        self._dataProvider = PrebattleCarouselDataProvider(PrebattleCarouselFilter(), None)
        self.__filterPopoverRemoveCallback = None
        self.__cooldownCallback = None
        self.__eventManager = EventManager()
        self.onViewLoaded = Event(self.__eventManager)
        return

    @property
    def viewModel(self):
        return super(PrebattleCarouselView, self).getViewModel()

    @createBackportTooltipDecorator()
    def createToolTip(self, event):
        return super(PrebattleCarouselView, self).createToolTip(event)

    def createPopOverContent(self, event):
        if event.contentID == R.views.common.pop_over_window.backport_pop_over.BackportPopOverContent():
            return BackportPopOverContent(popOverData=createPopOverData(BATTLE_VIEW_ALIASES.COMP7_TANK_CAROUSEL_FILTER_POPOVER, {b'parentWindow': (self.getParentWindow())}))
        return super(PrebattleCarouselView, self).createPopOverContent(event)

    def createContextMenu(self, event):
        return

    def updateViewActive(self, isActive):
        return

    @property
    def filter(self):
        return self._dataProvider.filter

    def applyFilter(self):
        self._dataProvider.applyFilter()
        self.updateVehicles()
        return

    def blinkCounter(self):
        return

    def formatCountVehicles(self):
        return formatCountString(self._dataProvider.getCurrentVehiclesCount(), self._dataProvider.getTotalVehiclesCount())

    def hasRentedVehicles(self):
        return self._dataProvider.hasRentedVehicles()

    def hasEventVehicles(self):
        return self._dataProvider.hasEventVehicles()

    def setPopoverCallback(self, callback=None):
        self.__filterPopoverRemoveCallback = callback
        return

    @replaceNoneKwargsModel
    def setRowCount(self, value, model=None):
        model.setIsDualRow(value > 1)
        return

    def hasRoles(self):
        return True

    def getCustomParams(self):
        return dict()

    @replaceNoneKwargsModel
    def updateHotFilters(self, model=None):
        filters = self._dataProvider.filter
        model.setRentedFilter(filters.get(FILTER_KEYS.RENTED))
        model.setFavoritesFilter(filters.get(FILTER_KEYS.FAVORITE))
        return

    def _initialize(self, *args, **kwargs):
        super(PrebattleCarouselView, self)._initialize()
        self.__addListeners()
        return

    def _finalize(self):
        if self.__cooldownCallback is not None:
            BigWorld.cancelCallback(self.__cooldownCallback)
            self.__cooldownCallback = None
        self.__removeListeners()
        self.__callPopoverCallback()
        super(PrebattleCarouselView, self)._finalize()
        return

    def _onLoading(self, *args, **kwargs):
        super(PrebattleCarouselView, self)._onLoading(*args, **kwargs)
        with self.viewModel.transaction() as model:
            self.__setDataProviderInfo()
            self.updateHotFilters(model=model)
            self.__setModelData(model=model)
        return

    def _onLoaded(self, *args, **kwargs):
        super(PrebattleCarouselView, self)._onLoaded(*args, **kwargs)
        self.onViewLoaded()
        return

    @sf_battle
    def _app(self):
        return

    def __addListeners(self):
        prbSwitch = self.__prbVehicleSwitch
        if prbSwitch:
            prbSwitch.onVehiclesListUpdated += self.__onListUpdated
            prbSwitch.onVehicleChanged += self.__onVehicleChanged
        viewModel = self.viewModel
        viewModel.onVehicleClick += self.__onVehicleClicked
        viewModel.onVehicleSelect += self.__onVehicleConfirmed
        viewModel.onApplyFavoritesFilter += self.__onFavoritesFilter
        viewModel.onApplyRentedFilter += self.__onRentedFilter
        viewModel.onClearFilters += self.__onClearFilters
        viewModel.onSetDualRow += self.__onSetDualRow
        self._app.loaderManager.onViewLoaded += self.__onViewLoaded
        g_eventBus.addListener(HidePopoverEvent.POPOVER_DESTROYED, self.__onPopOverDestroy)
        return

    def __removeListeners(self):
        prbSwitch = self.__prbVehicleSwitch
        if prbSwitch:
            prbSwitch.onVehiclesListUpdated -= self.__onListUpdated
            prbSwitch.onVehicleChanged -= self.__onVehicleChanged
        viewModel = self.viewModel
        viewModel.onVehicleClick -= self.__onVehicleClicked
        viewModel.onVehicleSelect -= self.__onVehicleConfirmed
        viewModel.onApplyFavoritesFilter -= self.__onFavoritesFilter
        viewModel.onApplyRentedFilter -= self.__onRentedFilter
        viewModel.onClearFilters -= self.__onClearFilters
        viewModel.onSetDualRow -= self.__onSetDualRow
        self._app.loaderManager.onViewLoaded -= self.__onViewLoaded
        g_eventBus.removeListener(HidePopoverEvent.POPOVER_DESTROYED, self.__onPopOverDestroy)
        self.__eventManager.clear()
        return

    @property
    def __prbVehicleSwitch(self):
        return self.__sessionProvider.dynamic.comp7PrebattleSetup

    def __onListUpdated(self):
        self.__setDataProviderInfo()
        self.__setModelData()
        return

    def __setDataProviderInfo(self):
        prbVehicleSwitchCtrl = self.__prbVehicleSwitch
        currentVehicle = prbVehicleSwitchCtrl.getCurrentGUIVehicle()
        vehicles = prbVehicleSwitchCtrl.getVehiclesList()
        self._dataProvider.setVehicles(vehicles)
        self._dataProvider.setCurrentVehicle(currentVehicle.intCD)
        return

    @replaceNoneKwargsModel
    def __setModelData(self, model=None):
        vehiclesModel = model.vehicles
        vehiclesModel.clearItems()
        vehicles = self._dataProvider.getSortedVehicles()
        currentCD = self._dataProvider.getSelectedCD()
        filteredVehicleCDs = self._dataProvider.getGetFilteredVehiclesCDs()
        for vehicleItem in vehicles:
            vehicleModel = PrebattleVehicleModel()
            fillVehicleModel(vehicleModel, vehicleItem)
            vehicleModel.setIsFavorite(vehicleItem.isFavorite)
            vehicleModel.setIsSelected(currentCD == vehicleModel.getVehicleCD())
            vehicleModel.setIsVisible(vehicleModel.getVehicleCD() in filteredVehicleCDs)
            vehiclesModel.addViewModel(vehicleModel)

        vehiclesModel.invalidate()
        return

    @replaceNoneKwargsModel
    def __updateVisibility(self, model=None):
        vehiclesModel = model.vehicles
        currentCD = self._dataProvider.getSelectedCD()
        filteredVehicleCDs = self._dataProvider.getGetFilteredVehiclesCDs()
        for vehicle in vehiclesModel.getItems():
            vehicle.setIsSelected(currentCD == vehicle.getVehicleCD())
            vehicle.setIsVisible(vehicle.getVehicleCD() in filteredVehicleCDs)

        vehiclesModel.invalidate()
        return

    def __onVehicleChanged(self, vehicle):
        self._dataProvider.setCurrentVehicle(vehicle.intCD)
        self.__updateVisibility()
        return

    def updateVehicles(self):
        self.__updateVisibility()
        return

    @replaceNoneKwargsModel
    def __onVehicleClicked(self, event, model=None):
        intCD = event.get(b'intCD')
        if intCD is None:
            return
        else:
            self.__cooldownCallback = BigWorld.callback(REQUEST_COOLDOWN.VEHICLE_IN_BATTLE_SWITCH, self.__onCooldownExpired)
            model.setIsLoading(True)
            self.__prbVehicleSwitch.chooseVehicle(intCD)
            return

    def __onVehicleConfirmed(self, *_):
        self.__prbVehicleSwitch.confirmVehicleSelection()
        return

    def __onViewLoaded(self, view, *args, **kwargs):
        if view.alias == BATTLE_VIEW_ALIASES.COMP7_TANK_CAROUSEL_FILTER_POPOVER:
            view.setTankCarousel(self)
            self.__setPopoverState(True)
        return

    @replaceNoneKwargsModel
    def __setPopoverState(self, hasPopover, model=None):
        model.setIsPopoverOpen(hasPopover)
        return

    def __onPopOverDestroy(self, *_):
        self.__setPopoverState(False)
        return

    def __onFavoritesFilter(self, *_):
        self._dataProvider.filter.switch(FILTER_KEYS.FAVORITE)
        self.updateHotFilters()
        self.applyFilter()
        return

    def __onRentedFilter(self, *_):
        self._dataProvider.filter.switch(FILTER_KEYS.RENTED)
        self.updateHotFilters()
        self.applyFilter()
        return

    def __callPopoverCallback(self):
        if callable(self.__filterPopoverRemoveCallback):
            callback = self.__filterPopoverRemoveCallback
            self.__filterPopoverRemoveCallback = None
            callback()
        return

    def __onClearFilters(self, *_):
        self._dataProvider.filter.reset()
        self.updateHotFilters()
        self.applyFilter()
        return

    @replaceNoneKwargsModel
    def __onCooldownExpired(self, model=None):
        model.setIsLoading(False)
        if self.__cooldownCallback is not None:
            BigWorld.cancelCallback(self.__cooldownCallback)
            self.__cooldownCallback = None
        return

    @replaceNoneKwargsModel
    def __onSetDualRow(self, model=None):
        AccountSettings.setSettings(COMP7_PREBATTLE_CAROUSEL_ROW_VALUE, 1)
        model.setIsDualRow(True)
        return
