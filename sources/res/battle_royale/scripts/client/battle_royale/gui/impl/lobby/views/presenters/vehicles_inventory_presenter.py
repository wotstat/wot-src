from __future__ import absolute_import
import json, typing
from future.utils import viewvalues
from CurrentVehicle import g_currentVehicle
from battle_royale.gui.impl.gen.view_models.views.lobby.views.vehicles_inventory_model import VehiclesInventoryModel
from battle_royale.gui.impl.lobby.tooltips.vehicle_tooltip_view import VehicleTooltipView
from gui.impl.gen import R
from gui.impl.pub.view_component import ViewComponent
from gui.prb_control.ctrl_events import g_prbCtrlEvents
from gui.shared.items_cache import CACHE_SYNC_REASON
from helpers import dependency
from skeletons.gui.customization import ICustomizationService
from skeletons.gui.game_control import IRentalsController
from skeletons.gui.shared import IItemsCache
from battle_royale.gui.impl.gen.view_models.views.lobby.enums import CoinType
from skeletons.gui.game_control import IBattleRoyaleController
if typing.TYPE_CHECKING:
    from gui.impl.lobby.hangar.base.hangar_interfaces import IVehicleFilter
    from gui.shared.gui_items.Vehicle import Vehicle
    from gui.shared.utils.requesters import RequestCriteria

class BattleRoyaleVehiclesInventoryPresenter(ViewComponent[VehiclesInventoryModel]):
    __itemsCache = dependency.descriptor(IItemsCache)
    __rentalsCtrl = dependency.descriptor(IRentalsController)
    __customizationService = dependency.descriptor(ICustomizationService)
    __brController = dependency.descriptor(IBattleRoyaleController)

    def __init__(self, vehiclesComponent, vehiclesCriteria):
        super(BattleRoyaleVehiclesInventoryPresenter, self).__init__(model=VehiclesInventoryModel)
        self.__vehiclesComponent = vehiclesComponent
        self.__vehiclesCriteria = vehiclesCriteria
        return

    @property
    def viewModel(self):
        return super(BattleRoyaleVehiclesInventoryPresenter, self).getViewModel()

    def createToolTipContent(self, event, contentID):
        if contentID == R.views.battle_royale.mono.lobby.tooltips.vehicle():
            return VehicleTooltipView(int(event.getArgument(b'intCD')))
        return super(BattleRoyaleVehiclesInventoryPresenter, self).createToolTipContent(event=event, contentID=contentID)

    def _getEvents(self):
        return (
         (
          g_currentVehicle.onChanged, self.__onVehicleChanged),
         (
          self.__itemsCache.onSyncCompleted, self.__onCacheResync),
         (
          self.__vehiclesComponent.onDiff, self.__onUpdateVehicles),
         (
          self.__rentalsCtrl.onRentChangeNotify, self.__onUpdateVehicles),
         (
          g_prbCtrlEvents.onVehicleClientStateChanged, self.__onVehicleClientStateChanged),
         (
          self.viewModel.onSelect, self.__onSelectVehicle))

    def _onLoading(self, *args, **kwargs):
        super(BattleRoyaleVehiclesInventoryPresenter, self)._onLoading(*args, **kwargs)
        self.__updateModel()
        return

    def _toModelItem(self, vehicle):
        vState = self.__getVehicleStatus(vehicle)
        modeSettings = self.__brController.getModeSettings()
        coinType = CoinType.STPCOIN if self.__brController.isStPatrick() else CoinType.BRCOIN
        return {b'id': (str(vehicle.intCD)), 
           b'vehicleId': (vehicle.intCD), 
           b'inventoryId': (vehicle.invID), 
           b'nationId': (vehicle.nationID), 
           b'type': (vehicle.type), 
           b'name': (vehicle.name), 
           b'shortName': (vehicle.shortUserName), 
           b'fullName': (vehicle.typeDescr.userString), 
           b'status': vState, 
           b'hasDailyBonus': (self.__brController.hasDailyBonus(vehicle)), 
           b'dailyBonusFactor': (modeSettings.dailyBonus.get(b'bonusFactor', 0)), 
           b'coinType': (coinType.value)}

    @staticmethod
    def __getVehicleStatus(vehicle):
        vState, _ = vehicle.getState()
        if vehicle.isRotationApplied():
            if vState in (Vehicle.VEHICLE_STATE.AMMO_NOT_FULL,
             Vehicle.VEHICLE_STATE.LOCKED):
                vState = Vehicle.VEHICLE_STATE.ROTATION_GROUP_UNLOCKED
        if not vehicle.activeInNationGroup:
            vState = Vehicle.VEHICLE_STATE.NOT_PRESENT
        return vState

    def __onVehicleClientStateChanged(self, vehicles=None):
        if vehicles:
            self.__onUpdateVehicles(vehicles)
        return

    def __onCacheResync(self, reason, diff):
        if reason == CACHE_SYNC_REASON.CLIENT_UPDATE:
            with self.viewModel.transaction() as model:
                self.__setupCurrentVehicle(model)
        return

    def __onVehicleChanged(self):
        if g_currentVehicle.intCD in self.__itemsCache.items.getVehicles(self.__vehiclesCriteria):
            with self.viewModel.transaction() as model:
                self.__setupCurrentVehicle(model)
        return

    def __setItem(self, model, vehicle):
        item = self._toModelItem(vehicle)
        model.getVehicles().set(str(item[b'id']), json.dumps(item))
        return

    def __setupVehicles(self, model, vehicles):
        for vehicle in viewvalues(vehicles):
            self.__setItem(model, vehicle)

        return

    def __onUpdateVehicles(self, diff):
        with self.viewModel.transaction() as model:
            for intCD in diff:
                if intCD in self.__vehiclesComponent.vehicles:
                    self.__setItem(model, self.__vehiclesComponent.vehicles[intCD])
                else:
                    model.getVehicles().remove(str(intCD))

        return

    def __onSelectVehicle(self, vehId):
        inventoryId = int(vehId[b'id'])
        g_currentVehicle.selectVehicle(inventoryId)
        return

    def __updateModel(self):
        with self.viewModel.transaction() as model:
            self.__setupVehicles(model, self.__vehiclesComponent.vehicles)
            self.__setupCurrentVehicle(model)
        return

    def __setupCurrentVehicle(self, model):
        if not g_currentVehicle.isPresent():
            g_currentVehicle.selectVehicle()
        if g_currentVehicle.isPresent():
            model.setCurrentVehicleInventoryId(g_currentVehicle.invID)
            model.setCurrentVehicleIntCD(g_currentVehicle.intCD)
        else:
            model.setCurrentVehicleInventoryId(VehiclesInventoryModel.NO_VEHICLE_ID)
            model.setCurrentVehicleIntCD(VehiclesInventoryModel.NO_VEHICLE_ID)
        return
