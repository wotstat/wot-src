from __future__ import absolute_import
import json, math, typing
from future.utils import itervalues
from gui.game_control.veh_comparison_basket import isValidVehicleForComparing
from gui.impl.gen.view_models.views.lobby.hangar.sub_views.vehicles_info_model import VehiclesInfoModel
from gui.impl.pub.view_component import ViewComponent
from helpers import dependency
from skeletons.gui.customization import ICustomizationService
from skeletons.gui.game_control import IRentalsController
if typing.TYPE_CHECKING:
    from gui.shared.gui_items import Vehicle
    from gui.impl.lobby.hangar.base.hangar_interfaces import IVehicleFilter

class VehiclesInfoPresenter(ViewComponent[VehiclesInfoModel]):
    __rentalsCtrl = dependency.descriptor(IRentalsController)
    __customizationService = dependency.descriptor(ICustomizationService)

    def __init__(self, vehiclesComponent):
        super(VehiclesInfoPresenter, self).__init__(model=VehiclesInfoModel)
        self._vehiclesComponent = vehiclesComponent
        return

    @property
    def viewModel(self):
        return super(VehiclesInfoPresenter, self).getViewModel()

    def _getEvents(self):
        return (
         (
          self._vehiclesComponent.onDiff, self.__onUpdateVehicles),
         (
          self.__rentalsCtrl.onRentChangeNotify, self.__onUpdateVehicles))

    def _onLoading(self, *args, **kwargs):
        super(VehiclesInfoPresenter, self)._onLoading(*args, **kwargs)
        self.__vehiclesWithAttachments = set(self.__customizationService.getVehiclesWithAttachmentSlot())
        self.__fillVehicles()
        return

    def __fillVehicles(self):
        self.__setupVehicles(self._vehiclesComponent.vehicles)
        return

    def _toModelItem(self, vehicle):
        return {b'id': (str(vehicle.intCD)), 
           b'vehicleId': (vehicle.intCD), 
           b'inventoryId': (vehicle.invID), 
           b'level': (vehicle.level), 
           b'type': (vehicle.type), 
           b'premium': (vehicle.isPremium), 
           b'name': (vehicle.name), 
           b'fullName': (vehicle.typeDescr.userString), 
           b'shortName': (vehicle.shortUserName), 
           b'nationId': (vehicle.nationID), 
           b'role': (vehicle.role), 
           b'nationChangeAvailable': (vehicle.isNationChangeAvailable), 
           b'favorite': (vehicle.isFavorite), 
           b'crystalEarning': (vehicle.isEarnCrystals), 
           b'comparable': (isValidVehicleForComparing(vehicle)), 
           b'canInstallAttachments': (vehicle in self.__vehiclesWithAttachments and not vehicle.isOutfitLocked and not vehicle.isProgressionDecalsOnly), 
           b'rent': {b'isRented': (vehicle.isRented), 
                     b'leftTime': ((math.isinf(vehicle.rentLeftTime) or vehicle).rentLeftTime if 1 else -1), 
                     b'leftBattles': (vehicle.rentLeftBattles or 0), 
                     b'leftWins': (vehicle.rentLeftWins or 0)}}

    def __setItem(self, model, vehicle):
        item = self._toModelItem(vehicle)
        model.getVehicles().set(str(item[b'id']), json.dumps(item))
        return

    def __setupVehicles(self, vehicles):
        with self.viewModel.transaction() as model:
            for vehicle in itervalues(vehicles):
                self.__setItem(model, vehicle)

        return

    def __onUpdateVehicles(self, diff):
        with self.viewModel.transaction() as model:
            for intCD in diff:
                if intCD in self._vehiclesComponent.vehicles:
                    self.__setItem(model, self._vehiclesComponent.vehicles[intCD])
                else:
                    model.getVehicles().remove(str(intCD))

        return
