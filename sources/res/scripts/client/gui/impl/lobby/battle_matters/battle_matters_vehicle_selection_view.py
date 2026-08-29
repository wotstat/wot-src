from collections import OrderedDict
from functools import partial
from frameworks.wulf import ViewFlags, ViewSettings, ViewStatus
from gui import GUI_NATIONS_ORDER_INDEX, GUI_NATIONS
from gui.Scaleform.locale.VEHICLE_PREVIEW import VEHICLE_PREVIEW
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.battle_matters.battle_matters_vehicle_selection_view_model import BattleMattersVehicleSelectionViewModel
from gui.impl.lobby.battle_matters.popovers.battle_matters_filter_popover_view import BattleMattersFilterPopoverView
from gui.impl.pub import ViewImpl
from gui.selectable_reward.common import BattleMattersSelectableRewardManager
from gui.server_events.events_dispatcher import showBattleMattersMainView
from gui.shared.event_dispatcher import showOfferGiftVehiclePreview, showDelayedReward, showBonusDelayedConfirmationDialog
from gui.impl.lobby.battle_matters.battle_matters_bonus_packer import BattleMattersVehiclesBonusUIPacker
from gui.shared.gui_items.Vehicle import VEHICLE_TYPES_ORDER
from helpers import dependency
from nations import NONE_INDEX
from shared_utils import first
from skeletons.gui.battle_matters import IBattleMattersController
from skeletons.gui.game_control import IVehicleComparisonBasket
from skeletons.gui.shared import IItemsCache
_NATIONS_KEY_NAME = b'Nations'
_TYPES_KEY_NAME = b'Types'
_TYPES_ORDER = (b'heavyTank', b'mediumTank', b'lightTank', b'AT-SPG', b'SPG')

def _sortByNation(vehicleTuple):
    _, vehicleDict = vehicleTuple
    nation = vehicleDict[b'vehicle'].displayedItem.nationName
    return GUI_NATIONS_ORDER_INDEX.get(nation, NONE_INDEX)


def _sortByType(vehicleTuple):
    _, vehicleDict = vehicleTuple
    vehicleType = vehicleDict[b'vehicle'].displayedItem.type
    return _TYPES_ORDER.index(vehicleType)


def _sortByName(firstVehicleTuple, secondVehicleTuple):
    _, firstVehicleDict = firstVehicleTuple
    _, secondVehicleDict = secondVehicleTuple
    firstUserName = firstVehicleDict[b'vehicle'].displayedItem.userName
    secondUserName = secondVehicleDict[b'vehicle'].displayedItem.userName
    return cmp(firstUserName, secondUserName)


def _sortVehicles(vehicles):
    vehicleSortedByNations = sorted(vehicles.iteritems(), key=_sortByNation)
    sortedVehicles = []
    for nation in GUI_NATIONS:
        sortedByType = sorted([(cd, veh) for cd, veh in vehicleSortedByNations if veh[b'vehicle'].displayedItem.nationName == nation], key=_sortByType)
        finallySortedByType = []
        for vehicleType in _TYPES_ORDER:
            sortedByName = sorted([(cd, veh) for cd, veh in sortedByType if veh[b'vehicle'].displayedItem.type == vehicleType], cmp=_sortByName)
            finallySortedByType += sortedByName

        sortedVehicles += finallySortedByType

    return sortedVehicles


class BattleMattersVehicleSelectionView(ViewImpl):
    __slots__ = (b'__selectableBonus', b'__vehicles', b'__savedCD', b'__filters', b'__filterPopover', b'__delayedRewardToken')
    _battleMattersController = dependency.descriptor(IBattleMattersController)
    _comparisonBasket = dependency.descriptor(IVehicleComparisonBasket)
    _itemsCache = dependency.descriptor(IItemsCache)
    _selectableBonusManager = BattleMattersSelectableRewardManager

    def __init__(self, delayedRewardToken=None):
        settings = ViewSettings(R.views.lobby.battle_matters.BattleMattersVehicleSelectionView())
        settings.flags = ViewFlags.VIEW
        settings.model = BattleMattersVehicleSelectionViewModel()

        def delayedRewardPredicate(token):
            if delayedRewardToken is not None:
                return token == delayedRewardToken
            else:
                return True

        self.__delayedRewardToken = delayedRewardToken
        self.__selectableBonus = first(self._selectableBonusManager.getAvailableSelectableBonuses(delayedRewardPredicate))
        bonuses = self._selectableBonusManager.getBonusOptions(self.__selectableBonus)
        vehicles = {v[b'option'].displayedItem.intCD: {b'vehicle': (v[b'option']), b'giftID': k} for k, v in bonuses.iteritems() if not v[b'option'].displayedItem.isUnlocked or v[b'option'].displayedItem.isCollectible}
        self.__vehicles = OrderedDict(_sortVehicles(vehicles))
        self.__filterPopover = None
        self.__filters = {}
        self.__resetFilters(True)
        self.__savedCD = -1
        super(BattleMattersVehicleSelectionView, self).__init__(settings)
        return

    @property
    def viewModel(self):
        return super(BattleMattersVehicleSelectionView, self).getViewModel()

    def createPopOverContent(self, event):
        if event.contentID == R.views.lobby.battle_matters.popovers.BattleMattersFilterPopoverView():
            self.__filterPopover = BattleMattersFilterPopoverView(self.__filters, self.onUpdateFilter)
            return self.__filterPopover
        return super(BattleMattersVehicleSelectionView, self).createPopOverContent(event)

    def onCompareVehicle(self, event):
        vehCD = int(event.get(BattleMattersVehicleSelectionViewModel.ARG_VEHICLE_ID))
        self._comparisonBasket.addVehicle(vehCD)
        return

    def onShowVehicle(self, event):
        vehCD = int(event.get(BattleMattersVehicleSelectionViewModel.ARG_VEHICLE_ID))
        self.__savedCD = vehCD
        giftID = self.__getIdByCD(vehCD)
        onConfirm = partial(showBonusDelayedConfirmationDialog, self.__vehicles[self.__savedCD][b'vehicle'].displayedItem, self.__delayedRewardToken, partial(_onDialogConfirm, bonus=self.__selectableBonus, giftID=giftID))
        showOfferGiftVehiclePreview(self._selectableBonusManager.getBonusOffer(self.__selectableBonus).id, giftID, onConfirm, VEHICLE_PREVIEW.HEADER_BACKBTN_DESCRLABEL_BATTLEMATTERS, customCallbacks={b'previewBackCb': (partial(showDelayedReward, self.__delayedRewardToken)), b'offerEndedCb': (lambda : None)})
        return

    def onResetFilter(self):
        self.__resetFilters()
        return

    def onUpdateFilter(self, filters=None):
        if filters:
            self.__filters = filters
        self._updateVehicles(self.viewModel.getVehicles())
        return

    def _onLoading(self):
        super(BattleMattersVehicleSelectionView, self)._onLoading()
        self.viewModel.getVehicles().reserve(len(self.__vehicles))
        self._update()
        return

    def _finalize(self):
        self.__filters = None
        self.__filterPopover = None
        self.__vehicles = None
        super(BattleMattersVehicleSelectionView, self)._finalize()
        return

    def _update(self):
        expires = self._battleMattersController.getDelayedRewardExpirationTime()
        with self.viewModel.transaction() as tx:
            if self._battleMattersController.isFinished():
                tx.setEndDate(expires)
            tx.setTotalVehiclesCount(len(self.__vehicles))
            level = self._battleMattersController.getDelayedRewardVehiclesLevel(self.__delayedRewardToken)
            tx.setLevel(level)
            vehiclesVM = tx.getVehicles()
            self._updateVehicles(vehiclesVM)
        return

    def _updateVehicles(self, vm):
        isNationsFilterEmpty = self.__isFilterEmpty(_NATIONS_KEY_NAME)
        isTypesFilterEmpty = self.__isFilterEmpty(_TYPES_KEY_NAME)
        vm.clear()
        for vehCD, vehicleDict in self.__vehicles.iteritems():
            if isNationsFilterEmpty and isTypesFilterEmpty or isTypesFilterEmpty and self.__nationFit(vehCD) or isNationsFilterEmpty and self.__typeFit(vehCD) or self.__nationFit(vehCD) and self.__typeFit(vehCD):
                vm.addViewModel(BattleMattersVehiclesBonusUIPacker.pack(vehicleDict[b'vehicle'])[0])

        vm.invalidate()
        return

    def _getEvents(self):
        return (
         (
          self._battleMattersController.onStateChanged, showBattleMattersMainView),
         (
          self.viewModel.onGoBack, showBattleMattersMainView),
         (
          self.viewModel.onCompareVehicle, self.onCompareVehicle),
         (
          self.viewModel.onShowVehicle, self.onShowVehicle),
         (
          self.viewModel.onResetFilter, self.onResetFilter))

    def __getIdByCD(self, vehCD):
        return self.__vehicles.get(vehCD, {}).get(b'giftID', -1)

    def __isFilterEmpty(self, key):
        return not any(value for value in self.__filters[key].itervalues())

    def __nationFit(self, vehCD):
        return self.__filters[_NATIONS_KEY_NAME][self.__vehicles[vehCD][b'vehicle'].displayedItem.nationName]

    def __typeFit(self, vehCD):
        return self.__filters[_TYPES_KEY_NAME][self.__vehicles[vehCD][b'vehicle'].displayedItem.type]

    def __resetFilters(self, init=False):
        self.__filters = {_NATIONS_KEY_NAME: (OrderedDict((nation, False) for nation in GUI_NATIONS)), 
           _TYPES_KEY_NAME: (OrderedDict((t, False) for t in VEHICLE_TYPES_ORDER))}
        if self.__filterPopover and self.__filterPopover.viewStatus == ViewStatus.LOADED:
            self.__filterPopover.updateFilterFromOutside(self.__filters)
        elif not init:
            self.onUpdateFilter()
        return


def _onDialogConfirm(result, bonus, giftID):
    if result:
        BattleMattersSelectableRewardManager.chooseReward(bonus, giftID=giftID, callback=_showAwardView)
    return


@dependency.replace_none_kwargs(bmController=IBattleMattersController)
def _showAwardView(result, bmController=None):
    if result and result.auxData:
        bmController.showAwardView(questsData=None, clientCtx=result.auxData)
    return
