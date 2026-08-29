from account_helpers.settings_core.ServerSettingsManager import UI_STORAGE_KEYS
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS
from gui.Scaleform.locale.TOOLTIPS import TOOLTIPS
from gui.shared.utils import EXTRA_MODULE_INFO
from gui.Scaleform.genConsts.FITTING_TYPES import FITTING_TYPES
from helpers import dependency
from items import ITEM_TYPES
from skeletons.account_helpers.settings_core import ISettingsCore

class _SlotVOConstants(object):
    UNRESOLVED_LIST_INDEX = -1
    MODULE_LABEL_EMPTY = b'empty'


class FittingSlotVO(dict):

    def __init__(self, modulesData, vehicle, moduleType, tooltipType=None, isDisabledTooltip=False):
        super(FittingSlotVO, self).__init__()
        if moduleType == FITTING_TYPES.VEHICLE_TURRET and not vehicle.hasTurrets:
            ttType = b''
        else:
            ttType = tooltipType or TOOLTIPS_CONSTANTS.PREVIEW_MODULE
        vehicleModule = self._prepareModule(modulesData, vehicle)
        if moduleType == FITTING_TYPES.VEHICLE_CHASSIS:
            if vehicleModule and vehicleModule.isWheeledChassis():
                moduleType = FITTING_TYPES.VEHICLE_WHEELED_CHASSIS
        self[b'tooltip'] = b''
        self[b'name'] = b''
        self[b'tooltipType'] = ttType
        self[b'slotType'] = moduleType
        self[b'removable'] = True
        if vehicleModule is None:
            self[b'id'] = _SlotVOConstants.UNRESOLVED_LIST_INDEX
            self[b'tooltipType'] = TOOLTIPS_CONSTANTS.COMPLEX
            if not isDisabledTooltip:
                self[b'tooltip'] = TOOLTIPS.HANGAR_AMMO_PANEL_EQUIPMENT_EMPTY
            else:
                self[b'tooltip'] = TOOLTIPS.HANGAR_AMMO_PANEL_EQUIPMENT_DISABLED
            self[b'moduleLabel'] = _SlotVOConstants.MODULE_LABEL_EMPTY
        else:
            self[b'id'] = vehicleModule.intCD
            self[b'removable'] = vehicleModule.isRemovable
            self[b'moduleLabel'] = vehicleModule.getGUIEmblemID()
            self[b'name'] = vehicleModule.userName
        self._setNewCounter(vehicleModule, vehicle)
        return

    def _prepareModule(self, modulesData, vehicle):
        vehicleModule = modulesData[0]
        self[b'slotIndex'] = 0
        self[b'level'] = vehicleModule.level
        self[EXTRA_MODULE_INFO] = vehicleModule.getExtraIconInfo(vehicle.descriptor)
        return vehicleModule

    def _setNewCounter(self, vehicleModule, vehicle):
        if vehicleModule is None:
            return
        else:
            if vehicleModule.itemTypeID == ITEM_TYPES.vehicleGun:
                if vehicleModule.isAutoReloadable(vehicle.descriptor):
                    uiStorage = dependency.instance(ISettingsCore).serverSettings.getUIStorage()
                    if not uiStorage.get(UI_STORAGE_KEYS.AUTO_RELOAD_MARK_IS_SHOWN):
                        self[b'counter'] = 1
                if vehicleModule.isDualGun(vehicle.descriptor):
                    uiStorage = dependency.instance(ISettingsCore).serverSettings.getUIStorage()
                    if not uiStorage.get(UI_STORAGE_KEYS.DUAL_GUN_MARK_IS_SHOWN):
                        if b'counter' in self:
                            self[b'counter'] += 3
                        else:
                            self[b'counter'] = 3
                if vehicleModule.hasDualAccuracy(vehicle.descriptor):
                    uiStorage = dependency.instance(ISettingsCore).serverSettings.getUIStorage2()
                    if not uiStorage.get(UI_STORAGE_KEYS.DUAL_ACCURACY_MARK_IS_SHOWN):
                        self[b'counter'] = self.get(b'counter', 0) + 1
                if vehicleModule.isAutoReloadableDualGun(vehicle.descriptor):
                    uiStorage = dependency.instance(ISettingsCore).serverSettings.getUIStorage2()
                    if not uiStorage.get(UI_STORAGE_KEYS.AUTO_RELOAD_DUAL_GUN_MARK_IS_SHOWN):
                        self[b'counter'] = self.get(b'counter', 0) + 1
                if vehicleModule.isClipDualGun(vehicle.descriptor):
                    uiStorage = dependency.instance(ISettingsCore).serverSettings.getUIStorage2()
                    if not uiStorage.get(UI_STORAGE_KEYS.CLIP_DUAL_GUN_MARK_IS_SHOWN):
                        self[b'counter'] = self.get(b'counter', 0) + 1
            if vehicleModule.itemTypeID == ITEM_TYPES.vehicleEngine:
                if vehicleModule.hasTurboshaftEngine():
                    uiStorage = dependency.instance(ISettingsCore).serverSettings.getUIStorage()
                    if not uiStorage.get(UI_STORAGE_KEYS.TURBOSHAFT_MARK_IS_SHOWN):
                        self[b'counter'] = self.get(b'counter', 0) + 1
                if vehicleModule.hasRocketAcceleration():
                    uiStorage = dependency.instance(ISettingsCore).serverSettings.getUIStorage2()
                    if not uiStorage.get(UI_STORAGE_KEYS.ROCKET_ACCELERATION_MARK_IS_SHOWN):
                        self[b'counter'] = self.get(b'counter', 0) + 1
            return
