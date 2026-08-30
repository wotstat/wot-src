import logging
from adisp import adisp_process, adisp_async
from gui.shared.gui_items.items_actions import actions
_logger = logging.getLogger(__name__)
SELL_ITEM = b'sellItemAction'
SELL_MULTIPLE = b'sellMultipleItems'
BUY_VEHICLE = b'vehBuyAction'
BUY_MODULE = b'moduleBuyAction'
UNLOCK_ITEM = b'unlockAction'
BC_UNLOCK_ITEM = b'bcUnlockAction'
INSTALL_ITEM = b'installItemAction'
BUY_AND_INSTALL_ITEM = b'buyAndInstallItemAction'
BUY_AND_INSTALL_AND_SELL_ITEM = b'BuyAndInstallWithOptionalSellItemAction'
BC_BUY_AND_INSTALL_ITEM = b'bcBuyAndInstallItemAction'
VEHICLE_AUTO_FILL_LAYOUT = b'vehicleAutoFillLayoutAction'
BUY_BERTHS = b'buyBerths'
BUY_VEHICLE_SLOT = b'buyVehClot'
ACTIVATE_BOOSTER = b'activateBooster'
BUY_BOOSTER = b'buyBooster'
BUY_AND_ACTIVATE_BOOSTER = b'buyAndActivateBooster'
CONVERT_BLUEPRINT_FRAGMENT = b'convertFragment'
USE_CREW_BOOK = b'useCrewBook'
USE_FREE_XP_TO_TANKMAN = b'useFreeXpToTankman'
RETRAIN_TANKMAN = b'retrainTankman'
CHANGE_ROLE_TANKMAN = b'changeRoleTankman'
UNLOAD_TANKMAN = b'unloadTankman'
EQUIP_TANKMAN = b'equipTankman'
CHANGE_TANKMAN_PASSPORT = b'changeTankmanPassport'
DISMISS_TANKMAN = b'dismissTankman'
RESTORE_TANKMAN = b'restoreTankman'
RESTORE_TANKMANS = b'restoreTankmans'
CREW_SKIN_EQUIP = b'crewSkinEquip'
CREW_SKIN_UNEQUIP = b'crewSkinUnequip'
CHANGE_NATION = b'changeNation'
INSTALL_BATTLE_ABILITIES = b'installBattleAbilities'
BUY_BATTLE_ABILITIES = b'buyBattleAbilities'
BUY_AND_INSTALL_OPT_DEVICES = b'buyAndInstallOptDevices'
BUY_AND_INSTALL_CONSUMABLES = b'buyAndInstallConsumables'
BUY_AND_INSTALL_SHELLS = b'buyAndInstallShells'
BUY_AND_INSTALL_BATTLE_BOOSTERS = b'buyAndInstallBattleBoosters'
UPGRADE_OPT_DEVICE = b'upgradeOptDevice'
DECONSTRUCT_OPT_DEVICE = b'deconstructOptDevice'
DECONSTRUCT_MULT_OPT_DEVICE = b'deconstructMultOptDevice'
REMOVE_OPT_DEVICE = b'removeOptDevice'
CHANGE_SETUP_EQUIPMENTS_INDEX = b'changeSetupEquipmentsIndex'
SET_EQUIPMENT_SLOT_TYPE = b'setEquipmentSlotType'
DISCARD_POST_PROGRESSION_PAIRS = b'discardPostProgressionPairs'
PURCHASE_POST_PROGRESSION_PAIR = b'purchasePostProgressionPair'
PURCHASE_POST_PROGRESSION_STEPS = b'purchasePostProgressionSteps'
SWITCH_PREBATTLE_AMMO_PANEL_AVAILABILITY = b'switchPrebattleAmmoPanelAvailability'
_ACTION_MAP = {SELL_ITEM: (actions.SellItemAction), 
   SELL_MULTIPLE: (actions.SellMultipleItems), 
   UNLOCK_ITEM: (actions.UnlockItemAction), 
   BC_UNLOCK_ITEM: (actions.BCUnlockItemAction), 
   BUY_MODULE: (actions.ModuleBuyAction), 
   BUY_VEHICLE: (actions.VehicleBuyAction), 
   INSTALL_ITEM: (actions.InstallItemAction), 
   BUY_AND_INSTALL_AND_SELL_ITEM: (actions.BuyAndInstallWithOptionalSellItemAction), 
   BC_BUY_AND_INSTALL_ITEM: (actions.BCBuyAndInstallItemAction), 
   VEHICLE_AUTO_FILL_LAYOUT: (actions.VehicleAutoFillLayoutAction), 
   BUY_BERTHS: (actions.BuyBerthsAction), 
   BUY_VEHICLE_SLOT: (actions.BuyVehicleSlotAction), 
   ACTIVATE_BOOSTER: (actions.ActivateBoosterAction), 
   BUY_BOOSTER: (actions.BuyBoosterAction), 
   BUY_AND_ACTIVATE_BOOSTER: (actions.BuyAndActivateBooster), 
   CONVERT_BLUEPRINT_FRAGMENT: (actions.ConvertBlueprintFragmentAction), 
   USE_CREW_BOOK: (actions.UseCrewBookAction), 
   USE_FREE_XP_TO_TANKMAN: (actions.UseFreeXpToTankman), 
   RETRAIN_TANKMAN: (actions.TankmanRetrainingAction), 
   CHANGE_ROLE_TANKMAN: (actions.TankmanChangeRoleAction), 
   UNLOAD_TANKMAN: (actions.TankmanUnloadAction), 
   EQUIP_TANKMAN: (actions.TankmanEquipAction), 
   CHANGE_TANKMAN_PASSPORT: (actions.TankmanChangePassportAction), 
   DISMISS_TANKMAN: (actions.TankmanDismissAction), 
   RESTORE_TANKMAN: (actions.TankmanRestoreAction), 
   RESTORE_TANKMANS: (actions.TankmansRestoreAction), 
   CREW_SKIN_EQUIP: (actions.CrewSkinEquipAction), 
   CREW_SKIN_UNEQUIP: (actions.CrewSkinUnequipAction), 
   CHANGE_NATION: (actions.ChangeVehicleNationAction), 
   INSTALL_BATTLE_ABILITIES: (actions.InstallBattleAbilities), 
   BUY_BATTLE_ABILITIES: (actions.BuyBattleAbilities), 
   BUY_AND_INSTALL_OPT_DEVICES: (actions.BuyAndInstallOptDevices), 
   BUY_AND_INSTALL_CONSUMABLES: (actions.BuyAndInstallConsumables), 
   BUY_AND_INSTALL_SHELLS: (actions.BuyAndInstallShells), 
   BUY_AND_INSTALL_BATTLE_BOOSTERS: (actions.BuyAndInstallBattleBoosters), 
   UPGRADE_OPT_DEVICE: (actions.UpgradeOptDeviceAction), 
   DECONSTRUCT_OPT_DEVICE: (actions.DeconstructOptDevice), 
   DECONSTRUCT_MULT_OPT_DEVICE: (actions.DeconstructMultOptDevice), 
   REMOVE_OPT_DEVICE: (actions.RemoveOptionalDevice), 
   CHANGE_SETUP_EQUIPMENTS_INDEX: (actions.ChangeSetupEquipmentsIndex), 
   DISCARD_POST_PROGRESSION_PAIRS: (actions.DiscardPostProgressionPairs), 
   PURCHASE_POST_PROGRESSION_PAIR: (actions.PurchasePostProgressionPair), 
   PURCHASE_POST_PROGRESSION_STEPS: (actions.PurchasePostProgressionSteps), 
   SET_EQUIPMENT_SLOT_TYPE: (actions.SetEquipmentSlotType), 
   SWITCH_PREBATTLE_AMMO_PANEL_AVAILABILITY: (actions.SwitchPrebattleAmmoPanelAvailabilityAction)}

@adisp_process
def doAction(actionType, *args, **kwargs):
    action = getAction(actionType, *args, **kwargs)
    if action is not None:
        if action.isAsync():
            yield action.doAction()
        else:
            action.doAction()
    return


@adisp_async
@adisp_process
def asyncDoAction(action, callback):
    result = False
    if action is not None:
        if action.isAsync():
            result = yield action.doAction()
        else:
            action.doAction()
            result = True
    callback(result)
    return


def getAction(actionType, *args, **kwargs):
    if actionType in _ACTION_MAP:
        skipConfirm = kwargs.pop(b'skipConfirm', False)
        action = _ACTION_MAP[actionType](*args, **kwargs)
        action.skipConfirm = skipConfirm
        return action
    else:
        _logger.error(b'Action type is not found %s', actionType)
        return


def registerAction(actionType, action):
    _ACTION_MAP[actionType] = action
    return
