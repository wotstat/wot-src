from gui import GUI_NATIONS_ORDER_INDEX
from gui.Scaleform.daapi.view.lobby.hangar.carousels.basic.carousel_data_provider import HangarCarouselDataProvider
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS
from gui.impl import backport
from gui.impl.gen import R
from gui.impl.gen.view_models.views.battle_royale.equipment_panel_cmp_rent_states import EquipmentPanelCmpRentStates
from gui.shared.gui_items.Vehicle import Vehicle, VEHICLE_TYPES_ORDER_INDICES
from gui.shared.utils.functions import makeTooltip
from gui.shared.utils.requesters import REQ_CRITERIA
from helpers import dependency
from skeletons.gui.game_control import IBattleRoyaleRentVehiclesController
_UNDEFINED_VEHICLE_TYPE = b'undefined'

class RoyaleCarouselDataProvider(HangarCarouselDataProvider):
    __rentVehiclesController = dependency.descriptor(IBattleRoyaleRentVehiclesController)

    def getVehiclesIntCDs(self):
        vehicledIntCDs = []
        for vehicle in self._vehicles:
            vehicledIntCDs.append(vehicle.intCD)

        return vehicledIntCDs

    def _getAdditionalItemsIndexes(self):
        return []

    def _setBaseCriteria(self):
        self._baseCriteria = REQ_CRITERIA.INVENTORY | REQ_CRITERIA.VEHICLE.BATTLE_ROYALE
        return

    @classmethod
    def _vehicleComparisonKey(cls, vehicle):
        return (
         vehicle.getCustomState() == Vehicle.VEHICLE_STATE.UNSUITABLE_TO_QUEUE,
         vehicle.isRented,
         not vehicle.isInInventory,
         not vehicle.isEvent,
         not vehicle.isOnlyForBattleRoyaleBattles,
         not vehicle.isFavorite,
         GUI_NATIONS_ORDER_INDEX[vehicle.nationName],
         VEHICLE_TYPES_ORDER_INDICES[vehicle.type],
         vehicle.level,
         tuple(vehicle.buyPrices.itemPrice.price.iterallitems(byWeight=True)),
         vehicle.userName)

    def _isTelecomRentalsEnabled(self):
        return False

    def _buildVehicle(self, vehicle):
        result = super(RoyaleCarouselDataProvider, self)._buildVehicle(vehicle)
        state, _ = vehicle.getState()
        if vehicle.isOnlyForBattleRoyaleBattles:
            rentState = self.__rentVehiclesController.getRentState(vehicle.intCD)
            isTestDriveEnabled = rentState == EquipmentPanelCmpRentStates.STATE_TEST_DRIVE_AVAILABLE
            rentLeft = self.__rentVehiclesController.getFormatedRentTimeLeft(vehicle.intCD)
            isRentActive = rentState in (EquipmentPanelCmpRentStates.STATE_TEST_DRIVE_ACTIVE,
             EquipmentPanelCmpRentStates.STATE_RENT_ACTIVE)
            isBgLocked = result.get(b'lockBackground', False)
            isRentAvailable = rentState in (EquipmentPanelCmpRentStates.STATE_TEST_DRIVE_AVAILABLE,
             EquipmentPanelCmpRentStates.STATE_RENT_AVAILABLE)
            vState, _ = vehicle.getState()
            result.update({b'label': (vehicle.shortUserName), 
               b'tooltip': (TOOLTIPS_CONSTANTS.BATTLE_ROYALE_VEHICLE), 
               b'level': 0, 
               b'tankType': (vehicle.type), 
               b'xpImgSource': b'', 
               b'debutBoxesImgSource': b'', 
               b'isUseRightBtn': True, 
               b'isTestDriveEnabled': isTestDriveEnabled, 
               b'lockBackground': (isBgLocked or isRentAvailable), 
               b'rentLeft': (rentLeft if isRentActive else b'')})
            if vState not in (Vehicle.VEHICLE_STATE.IN_PREBATTLE,
             Vehicle.VEHICLE_STATE.DAMAGED,
             Vehicle.VEHICLE_STATE.DESTROYED,
             Vehicle.VEHICLE_STATE.EXPLODED,
             Vehicle.VEHICLE_STATE.BATTLE):
                result.update({b'infoText': b'', 
                   b'smallInfoText': b'', 
                   b'infoImgSrc': b''})
        elif state == Vehicle.VEHICLE_STATE.UNSUITABLE_TO_QUEUE:
            result[b'lockedTooltip'] = makeTooltip(backport.text(R.strings.battle_royale.battleRoyaleCarousel.lockedToolTip.header()), backport.text(R.strings.battle_royale.battleRoyaleCarousel.lockedToolTip.body()))
            result[b'clickEnabled'] = True
        return result
