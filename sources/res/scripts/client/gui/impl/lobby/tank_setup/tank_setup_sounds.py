import SoundGroups, WWISE
from gui.impl.gen.view_models.views.lobby.tank_setup.sub_views.base_setup_model import BaseSetupModel
from gui.impl.gen.view_models.views.lobby.tank_setup.tank_setup_constants import TankSetupConstants
from helpers import dependency
from shared_utils import CONST_CONTAINER, first
from skeletons.gui.shared import IItemsCache

class TankSetupSoundEvents(CONST_CONTAINER):
    STATE_PLACE = b'STATE_hangar_place'
    STATE_PLACE_ENTER = b'STATE_hangar_place_consumables'
    STATE_PLACE_GARAGE = b'STATE_hangar_place_garage'
    VIEW_ENTER = b'cons_enter'
    VIEW_EXIT = b'cons_exit'
    SELECT_VIEW = b'cons_select_view'
    ACCEPT = b'cons_accept'
    EQUIPMENT_SLOT_PREFIX = b'cons_equipment_slot_'
    EQUIPMENT_MOUNT = b'cons_equipment_mount'
    EQUIPMENT_DEMOUNT = b'cons_equipment_demount'
    EQUIPMENT_DEMOUNT_KIT = b'cons_equipment_demount_kit'
    EQUIPMENT_DESTROY = b'cons_equipment_destroy'
    EQUIPMENT_SWAP = b'cons_equipment_swipe'
    EQUIPMENT_BONUS = b'cons_equipment_bonus'
    CONSUMABLES_MOUNT = b'cons_consumables_mount'
    CONSUMABLES_DEMOUNT = b'cons_consumables_demount'
    INSTRUCTIONS_MOUNT = b'cons_instructions_mount'
    INSTRUCTIONS_DEMOUNT = b'cons_instructions_demount'
    INSTRUCTIONS_EQUIP_NOT_SUITABLE = b'cons_instructions_equip_not_suitable'
    RTPC_SHELLS_PROGRESS_BAR = b'RTPC_ext_ammo_progress_bar'
    AMMO_SINGLE_PLUS = b'cons_ammo_single_plus'
    AMMO_SINGLE_MINUS = b'cons_ammo_single_minus'


def playEnterTankSetupView():
    WWISE.WW_setState(TankSetupSoundEvents.STATE_PLACE, TankSetupSoundEvents.STATE_PLACE_ENTER)
    playSound(TankSetupSoundEvents.VIEW_ENTER)
    return


def playExitTankSetupView():
    WWISE.WW_setState(TankSetupSoundEvents.STATE_PLACE, TankSetupSoundEvents.STATE_PLACE_GARAGE)
    playSound(TankSetupSoundEvents.VIEW_EXIT)
    return


def playOptDeviceSlotEnter(vehicle, slotID):
    category = first(vehicle.optDevices.slots[slotID].categories)
    if category is None:
        return
    else:
        soundName = TankSetupSoundEvents.EQUIPMENT_SLOT_PREFIX + category
        playSound(soundName)
        return


def playSound(eventName):
    if eventName:
        SoundGroups.g_instance.playSound2D(eventName)
    return


def playSectionSelectSound():
    playSound(TankSetupSoundEvents.SELECT_VIEW)
    return


def playSlotActionSound(setupName, *args, **kwargs):
    if setupName == TankSetupConstants.CONSUMABLES or setupName == TankSetupConstants.BATTLE_ABILITIES:
        ConsumableActionSoundHelper.playActionSound(*args, **kwargs)
    elif setupName == TankSetupConstants.BATTLE_BOOSTERS:
        BattleBoostersActionSoundHelper.playActionSound(*args, **kwargs)
    elif setupName == TankSetupConstants.OPT_DEVICES:
        return OptDeviceActionSound.playActionSound(*args, **kwargs)
    ActionSoundHelper.playActionSound(*args, **kwargs)
    return


class ActionSoundHelper(object):
    _itemsCache = dependency.descriptor(IItemsCache)

    @classmethod
    def playActionSound(cls, actionType, vehicle, intCD=-1, leftIntCD=-1, rightIntCD=-1):
        if actionType == BaseSetupModel.SELECT_SLOT_ACTION:
            cls.playSelectSound(vehicle, intCD)
        elif actionType == BaseSetupModel.REVERT_SLOT_ACTION:
            cls.playRevertSound(vehicle)
        elif actionType == BaseSetupModel.SWAP_SLOTS_ACTION:
            cls.playSwapSound(vehicle, leftIntCD, rightIntCD)
        elif actionType in (BaseSetupModel.DEMOUNT_SLOT_ACTION,
         BaseSetupModel.DEMOUNT_SLOT_FROM_SETUP_ACTION,
         BaseSetupModel.DEMOUNT_SLOT_FROM_SETUPS_ACTION):
            cls.playDemountSound(vehicle, intCD)
        elif actionType == BaseSetupModel.DRAG_AND_DROP_SLOT_ACTION:
            cls.playDragAndDropSound(vehicle, leftIntCD, rightIntCD)
        elif actionType == BaseSetupModel.DESTROY_SLOT_ACTION:
            cls.playDestroySound(vehicle, intCD)
        return

    @classmethod
    def playSelectSound(cls, vehicle, intCD):
        playSound(TankSetupSoundEvents.EQUIPMENT_MOUNT)
        return

    @classmethod
    def playRevertSound(cls, vehicle):
        playSound(TankSetupSoundEvents.EQUIPMENT_DEMOUNT)
        return

    @classmethod
    def playDemountSound(cls, vehicle, intCD):
        playSound(TankSetupSoundEvents.EQUIPMENT_DEMOUNT_KIT)
        return

    @classmethod
    def playDestroySound(cls, vehicle, intCD):
        playSound(TankSetupSoundEvents.EQUIPMENT_DESTROY)
        return

    @classmethod
    def playSwapSound(cls, vehicle, leftIntCD, rightIntCD):
        playSound(TankSetupSoundEvents.EQUIPMENT_SWAP)
        return

    @classmethod
    def playDragAndDropSound(cls, vehicle, leftIntCD, rightIntCD):
        return


class ConsumableActionSoundHelper(ActionSoundHelper):

    @classmethod
    def playSelectSound(cls, vehicle, intCD):
        playSound(TankSetupSoundEvents.CONSUMABLES_MOUNT)
        return

    @classmethod
    def playRevertSound(cls, vehicle):
        playSound(TankSetupSoundEvents.CONSUMABLES_DEMOUNT)
        return


class OptDeviceActionSound(ActionSoundHelper):

    @classmethod
    def playSelectSound(cls, vehicle, intCD):
        playSound(TankSetupSoundEvents.EQUIPMENT_MOUNT)
        if cls._isCategoryMatch(vehicle, intCD):
            playSound(TankSetupSoundEvents.EQUIPMENT_BONUS)
        return

    @classmethod
    def playSwapSound(cls, vehicle, leftIntCD, rightIntCD):
        playSound(TankSetupSoundEvents.EQUIPMENT_SWAP)
        if cls._isCategoryMatch(vehicle, leftIntCD) or cls._isCategoryMatch(vehicle, rightIntCD):
            playSound(TankSetupSoundEvents.EQUIPMENT_BONUS)
        return

    @classmethod
    def playDragAndDropSound(cls, vehicle, leftIntCD, rightIntCD):
        if cls._isCategoryMatch(vehicle, leftIntCD) or cls._isCategoryMatch(vehicle, rightIntCD):
            playSound(TankSetupSoundEvents.EQUIPMENT_BONUS)
        return

    @classmethod
    def _isCategoryMatch(cls, vehicle, intCD):
        intCDs = vehicle.optDevices.layout.getIntCDs(default=None)
        if intCD in intCDs:
            slotID = intCDs.index(intCD)
            vehCategories = vehicle.optDevices.getSlot(slotID).item.categories
            itemCategories = vehicle.optDevices.layout[slotID].descriptor.categories
            return bool(vehCategories & itemCategories)
        else:
            return False


class BattleBoostersActionSoundHelper(ActionSoundHelper):
    _CREW_BOOSTER_SOUND = {b'smoothTurretBattleBooster': b'cons_instructions_steady_hand', 
       b'virtuosoBattleBooster': b'cons_instructions_combat_course', 
       b'pedantBattleBooster': b'cons_instructions_shell_organizer', 
       b'smoothDrivingBattleBooster': b'cons_instructions_gearbox_intricacy', 
       b'fireFightingBattleBooster': b'cons_instructions_firefighters', 
       b'rancorousBattleBooster': b'cons_instructions_focus_target', 
       b'camouflageBattleBooster': b'cons_instructions_natural_cover', 
       b'enemyShotPredictorBattleBooster': b'cons_instructions_heightened_vigilance', 
       b'practicalityBattleBooster': b'cons_instructions_thorough_preparations'}

    @classmethod
    def playSelectSound(cls, vehicle, intCD):
        item = cls._itemsCache.items.getItemByCD(intCD)
        if item.isCrewBooster():
            cls._playCrewBoosterSelectSound(vehicle, item)
        else:
            cls._playOptDeviceBoosterSelectSound(vehicle, item)
        playSound(TankSetupSoundEvents.INSTRUCTIONS_MOUNT)
        return

    @classmethod
    def playRevertSound(cls, vehicle):
        playSound(TankSetupSoundEvents.INSTRUCTIONS_DEMOUNT)
        return

    @classmethod
    def _playCrewBoosterSelectSound(cls, vehicle, item):
        soundName = cls._CREW_BOOSTER_SOUND.get(item.name)
        if soundName:
            playSound(soundName)
        return

    @classmethod
    def _playOptDeviceBoosterSelectSound(cls, vehicle, item):
        if not item.isAffectsOnVehicle(vehicle):
            playSound(TankSetupSoundEvents.INSTRUCTIONS_EQUIP_NOT_SUITABLE)
        return
