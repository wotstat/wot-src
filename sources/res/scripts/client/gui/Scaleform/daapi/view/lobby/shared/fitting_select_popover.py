from __future__ import absolute_import
import logging, typing
from CurrentVehicle import g_currentVehicle, g_currentPreviewVehicle
from gui.Scaleform.daapi.view.lobby.shared.fitting_select.module_extenders import fittingSelectModuleExtenders
from gui.Scaleform.daapi.view.meta.FittingSelectPopoverMeta import FittingSelectPopoverMeta
from gui.Scaleform.genConsts.FITTING_TYPES import FITTING_TYPES
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS
from gui.Scaleform.locale.MENU import MENU
from gui.shared import event_dispatcher as shared_events
from gui.shared.formatters import text_styles, getItemPricesVOWithReason
from gui.shared.formatters.text_styles import builder as str_builder
from gui.shared.gui_items import GUI_ITEM_TYPE_INDICES, GUI_ITEM_TYPE, GUI_ITEM_ECONOMY_CODE, GUI_ITEM_TYPE_NAMES
from gui.shared.gui_items.fitting_item import FittingItem
from gui.shared.gui_items.items_actions import factory as ItemsActionsFactory
from gui.shared.items_parameters import params_helper
from gui.shared.items_parameters.formatters import formatModuleParamName, formatParameter
from gui.shared.utils import EXTRA_MODULE_INFO
from gui.shared.utils.requesters.ItemsRequester import REQ_CRITERIA
from helpers import dependency, i18n
from helpers.i18n import makeString as _ms
from items import getTypeInfoByName
from items.utils import getVehicleDescriptorWithoutMechanics
from items.vehicles import VehicleDescriptor
from skeletons.account_helpers.settings_core import ISettingsCore
from skeletons.gui.shared import IItemsCache
from vehicles.mechanics.mechanic_constants import VehicleMechanic
if typing.TYPE_CHECKING:
    from gui.shared.gui_items.vehicle_modules import VehicleGun, VehicleRadio, VehicleEngine, VehicleTurret, VehicleChassis
    from gui.Scaleform.daapi.view.lobby.shared.fitting_select.module_extenders import ModuleParamsExtender
_logger = logging.getLogger(__name__)
FITTING_MODULES = (
 GUI_ITEM_TYPE_NAMES[GUI_ITEM_TYPE.CHASSIS],
 GUI_ITEM_TYPE_NAMES[GUI_ITEM_TYPE.TURRET],
 GUI_ITEM_TYPE_NAMES[GUI_ITEM_TYPE.GUN],
 GUI_ITEM_TYPE_NAMES[GUI_ITEM_TYPE.ENGINE],
 GUI_ITEM_TYPE_NAMES[GUI_ITEM_TYPE.RADIO])
_PARAMS_LISTS = {(GUI_ITEM_TYPE.RADIO): (b'radioDistance',), 
   (GUI_ITEM_TYPE.CHASSIS): (b'rotationSpeed', b'maxSteeringLockAngle', b'chassisRepairTime'), 
   (GUI_ITEM_TYPE.ENGINE): (b'enginePower', b'fireStartingChance'), 
   (GUI_ITEM_TYPE.TURRET): (b'armor', b'rotationSpeed', b'circularVisionRadius'), 
   (GUI_ITEM_TYPE.GUN): (b'avgDamageList', b'avgPiercingPower', b'reloadTime')}
_POPOVER_FIRST_TAB_IDX = 0
_POPOVER_SECOND_TAB_IDX = 1
_TAB_IDS = (_POPOVER_FIRST_TAB_IDX, _POPOVER_SECOND_TAB_IDX)

def _extendByModuleData(targetData, vehicleModule, vehDescr, extenders):
    moduleType = vehicleModule.itemTypeID
    paramsList = _PARAMS_LISTS[moduleType]
    if moduleType == GUI_ITEM_TYPE.GUN:
        if vehicleModule.isDamageMutable():
            paramsList = (b'maxAvgMutableDamageList', b'minAvgMutableDamageList', b'avgPiercingPower', b'reloadTime')
        if vehicleModule.isLowChargeShotGun():
            vehDescr = getVehicleDescriptorWithoutMechanics(vehDescr, VehicleMechanic.LOW_CHARGE_SHOT.value)
    values, names = [], []
    paramsData = params_helper.getParameters(vehicleModule, vehDescr)
    serverSettings = dependency.instance(ISettingsCore).serverSettings
    for ext in extenders:
        if ext.check(vehicleModule, vehDescr):
            paramsList, indexes = ext.extendParamList(paramsList)
            if ext.highlightCheck(serverSettings) and indexes:
                targetData[b'highlightedParameterIdx'] = indexes[0]
                ext.updatedHighlightSettings(serverSettings)

    for paramName in paramsList:
        value = paramsData.get(paramName)
        if value is not None:
            values.append(_formatValuesString(formatParameter(paramName, value)))
            names.append(formatModuleParamName(paramName, vehDescr))

    targetData[b'level'] = vehicleModule.level
    targetData[b'paramValues'] = (b'\n').join(values)
    targetData[b'paramNames'] = (b'\n').join(names)
    targetData[b'name'] = text_styles.middleTitle(vehicleModule.userName)
    targetData[EXTRA_MODULE_INFO] = vehicleModule.getExtraIconInfo(vehDescr)
    return


def _getInstallReason(module, vehicle, reason, slotIdx=None):
    _, installReason = module.mayInstall(vehicle, slotIdx)
    if GUI_ITEM_ECONOMY_CODE.isCurrencyError(reason):
        return installReason or reason
    return installReason


def _getStatus(reason):
    if reason is not None and reason not in (GUI_ITEM_ECONOMY_CODE.ITEM_IS_HIDDEN,
     GUI_ITEM_ECONOMY_CODE.ITEM_IS_DUPLICATED):
        return text_styles.error(b'#menu:moduleFits/' + reason.replace(b' ', b'_'))
    else:
        return b''


def _formatValuesString(valuesStr):
    if valuesStr is None:
        return b''
    else:
        valuesBuilder = str_builder()
        values = valuesStr.split(b'/')
        length = len(values)
        for idx, value in enumerate(values):
            valuesBuilder.addStyledText(text_styles.stats, value)
            if idx < length - 1:
                valuesBuilder.addStyledText(text_styles.standard, b'/')

        return valuesBuilder.render()


def _convertTarget(target, reason):
    if target == FittingItem.TARGETS.OTHER:
        return FITTING_TYPES.TARGET_OTHER
    if target == FittingItem.TARGETS.IN_INVENTORY:
        if reason in (GUI_ITEM_ECONOMY_CODE.UNDEFINED, GUI_ITEM_ECONOMY_CODE.NOT_ENOUGH_CREDITS):
            return FITTING_TYPES.TARGET_HANGAR
        if reason == GUI_ITEM_ECONOMY_CODE.ITEM_IS_DUPLICATED:
            return FITTING_TYPES.TARGET_HANGAR_DUPLICATE
        return FITTING_TYPES.TARGET_HANGAR_CANT_INSTALL
    if target == FittingItem.TARGETS.CURRENT:
        return FITTING_TYPES.TARGET_VEHICLE
    return


class CommonFittingSelectPopover(FittingSelectPopoverMeta):
    _TAB_IDX = 0
    _TABS = None

    def __init__(self, vehicle, logicProvider, ctx=None):
        super(CommonFittingSelectPopover, self).__init__(ctx)
        data = ctx.get(b'data')
        self._slotType = data.slotType
        self.__vehicle = vehicle
        self._logicProvider = logicProvider
        self.setCurrentTab(self._getInitialTabIndex())
        return

    def showModuleInfo(self, moduleId):
        if self.__vehicle is not None and moduleId is not None and int(moduleId) > 0:
            shared_events.showModuleInfo(moduleId, self.__vehicle.descriptor)
        return

    def setVehicleModule(self, newId, oldId, isRemove):
        self._logicProvider.setModule(newId, oldId, isRemove)
        self.destroy()
        return

    def setCurrentTab(self, tabIndex):
        if tabIndex not in _TAB_IDS:
            return
        self._logicProvider.setTab(tabIndex)
        if tabIndex != self._getInitialTabIndex():
            self._saveTabIndex(tabIndex)
            self.as_updateS(self._prepareInitialData())
        return

    def _saveTabIndex(self, index):
        self.__class__._TAB_IDX = index
        return

    def _getInitialTabIndex(self):
        return self.__class__._TAB_IDX

    def _getVehicle(self):
        return self.__vehicle

    def _populate(self):
        super(CommonFittingSelectPopover, self)._populate()
        self.as_updateS(self._prepareInitialData())
        return

    def _dispose(self):
        self.__vehicle = None
        self._logicProvider.dispose()
        self._logicProvider = None
        super(CommonFittingSelectPopover, self)._dispose()
        return

    def _prepareInitialData(self):
        rendererName, rendererDataClass, width, title = self._getCommonData()
        result = {b'title': (text_styles.highTitle(title)), 
           b'rendererName': rendererName, 
           b'rendererDataClass': rendererDataClass, 
           b'scrollToIndex': (self._logicProvider.getSelectedIdx()), 
           b'selectedIndex': (self._logicProvider.getSelectedIdx()), 
           b'availableDevices': (self._logicProvider.getDevices()), 
           b'width': width}
        result.update(self._getTabsData())
        return result

    def _getTabsData(self):
        if self._TABS is not None:
            return {b'tabData': (self._TABS), b'selectedTab': (self._getInitialTabIndex())}
        else:
            return {}

    def _getDescText(self):
        currencyName = text_styles.main(MENU.FITTINGSELECTPOPOVER_DESCTEXT_CRYSTAL)
        result = text_styles.main(i18n.makeString(MENU.FITTINGSELECTPOPOVER_DESCTEXT, currencyName=currencyName))
        return result

    def _getCommonData(self):
        title = _ms(MENU.MODULEFITS_TITLE, moduleName=getTypeInfoByName(self._slotType)[b'userString'], vehicleName=self.__vehicle.userName if self.__vehicle is not None else b'')
        rendererDataClass = FITTING_TYPES.MODULE_FITTING_RENDERER_DATA_CLASS_NAME
        if self._slotType == FITTING_TYPES.VEHICLE_ENGINE:
            if self.__vehicle.descriptor.hasTurboshaftEngine or self.__vehicle.descriptor.hasRocketAcceleration:
                rendererName = FITTING_TYPES.ENGINE_FITTING_BIG_ITEM_RENDERER
            else:
                rendererName = FITTING_TYPES.ENGINE_FITTING_ITEM_RENDERER
            width = FITTING_TYPES.MEDUIM_POPOVER_WIDTH
        elif self._slotType == FITTING_TYPES.VEHICLE_CHASSIS:
            rendererName = FITTING_TYPES.CHASSIS_FITTING_ITEM_RENDERER
            width = FITTING_TYPES.LARGE_POPOVER_WIDTH
        elif self._slotType == FITTING_TYPES.VEHICLE_RADIO:
            rendererName = FITTING_TYPES.RADIO_FITTING_ITEM_RENDERER
            width = FITTING_TYPES.SHORT_POPOVER_WIDTH
        else:
            rendererName = FITTING_TYPES.GUN_TURRET_FITTING_ITEM_RENDERER
            width = FITTING_TYPES.LARGE_POPOVER_WIDTH
        return (rendererName, rendererDataClass, width, title)


class ModuleFittingSelectPopover(CommonFittingSelectPopover):
    _itemsCache = dependency.descriptor(IItemsCache)

    def __init__(self, ctx=None, customProviderClass=None):
        data_ = ctx[b'data']
        self.__preferredLayout = data_.preferredLayout
        self.__slotIndex = data_.slotIndex
        if g_currentPreviewVehicle.isPresent():
            providerClass = _PreviewLogicProvider
            vehicle = g_currentPreviewVehicle.item
        else:
            providerClass = _HangarLogicProvider
            vehicle = g_currentVehicle.item
        providerClass = customProviderClass or providerClass
        logicProvider = providerClass(data_.slotType, data_.slotIndex)
        super(ModuleFittingSelectPopover, self).__init__(vehicle, logicProvider, ctx)
        if self._slotType is not None and self._slotType not in FITTING_MODULES:
            _logger.error(b'Using ModuleFittingSelectPopover for not module type: %s', self._slotType)
        return

    def _prepareInitialData(self):
        result = super(ModuleFittingSelectPopover, self)._prepareInitialData()
        result[b'preferredLayout'] = self.__preferredLayout
        return result

    def _getSlotIndex(self):
        return self.__slotIndex


class PopoverLogicProvider(object):
    _itemsCache = dependency.descriptor(IItemsCache)
    _settingsCore = dependency.descriptor(ISettingsCore)

    def __init__(self, slotType, slotIndex, vehicle):
        self._slotType = slotType
        self._slotIndex = slotIndex
        self._vehicle = vehicle
        self._tooltipType = b''
        self.__modulesList = None
        self._selectedIdx = -1
        self._tabIndex = 0
        self.__moduleExtenders = fittingSelectModuleExtenders()
        return

    def getSelectedIdx(self):
        if self.__modulesList is None:
            self.__modulesList = self._buildList()
        return self._selectedIdx

    def getDevices(self):
        if self.__modulesList is None:
            self.__modulesList = self._buildList()
        return self.__modulesList

    def setModule(self, newId, oldId, isRemove):
        return NotImplemented

    def setTab(self, tabIndex):
        tabSwitched = self._tabIndex != tabIndex
        self._tabIndex = tabIndex
        if self.__modulesList is not None and tabSwitched:
            self._selectedIdx = -1
            self.__modulesList = self._buildList()
        return

    def dispose(self):
        self._vehicle = None
        return

    def _buildCommonModuleData(self, module, reason):
        return {b'id': (module.intCD), 
           b'type': (self._slotType), 
           b'target': (_convertTarget(module.getTarget(self._vehicle), reason)), 
           b'moduleLabel': (module.getGUIEmblemID()), 
           b'tooltipType': (self._tooltipType), 
           b'status': (_getStatus(reason))}

    def _buildModuleData(self, vehicleModule, isInstalledInSlot, stats):
        return NotImplemented

    def _buildList(self):
        modulesList = []
        if self._vehicle is not None:
            typeId = GUI_ITEM_TYPE_INDICES[self._slotType]
            data = self._getSuitableItems(typeId)
            currXp = self._itemsCache.items.stats.vehiclesXPs.get(self._vehicle.intCD, 0)
            stats = {b'money': (self._itemsCache.items.stats.money), 
               b'exchangeRate': (self._itemsCache.items.shop.exchangeRate), 
               b'currXP': currXp, 
               b'totalXP': (currXp + self._itemsCache.items.stats.freeXP)}
            for idx, vehicleModule in enumerate(data):
                isInstalled = vehicleModule.isInstalled(self._vehicle, self._slotIndex)
                if isInstalled:
                    self._selectedIdx = idx
                moduleData = self._buildModuleData(vehicleModule, isInstalled, stats)
                self.__extendByTypeSpecificData(moduleData, vehicleModule)
                modulesList.append(moduleData)

        return modulesList

    def _getSuitableItems(self, typeId):
        if self._vehicle is None:
            return []
        else:
            criteria = REQ_CRITERIA.VEHICLE.SUITABLE([self._vehicle], [typeId]) | self._getSpecificCriteria(typeId)
            data = self._itemsCache.items.getItems(typeId, criteria).values()
            data.sort(reverse=True, key=self._getItemsSortingKey())
            return data

    def _getItemsSortingKey(self):
        return

    def _getSpecificCriteria(self, typeID):
        return REQ_CRITERIA.EMPTY

    def __extendByTypeSpecificData(self, moduleData, vehicleModule):
        if vehicleModule.itemTypeID in GUI_ITEM_TYPE.VEHICLE_MODULES:
            _extendByModuleData(moduleData, vehicleModule, self._vehicle.descriptor, self.__moduleExtenders)
        return


class _HangarLogicProvider(PopoverLogicProvider):

    def __init__(self, slotType, slotIndex):
        super(_HangarLogicProvider, self).__init__(slotType, slotIndex, g_currentVehicle.item)
        self._tooltipType = TOOLTIPS_CONSTANTS.HANGAR_MODULE
        return

    def setModule(self, newId, oldId, isRemove):
        module = self._itemsCache.items.getItemByCD(int(newId))
        if module.isUnlocked:
            ItemsActionsFactory.doAction(ItemsActionsFactory.BUY_AND_INSTALL_AND_SELL_ITEM, newId, self._vehicle.intCD)
        return

    def _buildModuleData(self, vehicleModule, isInstalledInSlot, stats):
        itemPrice = vehicleModule.buyPrices.itemPrice
        inInventory = vehicleModule.isInInventory
        isInstalled = vehicleModule.isInstalled(self._vehicle)
        isBought = inInventory or isInstalled
        isEnoughMoney, purchaseReason = vehicleModule.mayPurchase(stats[b'money'])
        if isBought:
            isFit, reason = vehicleModule.mayInstall(self._vehicle, self._slotIndex)
            if reason == b'already installed' or isFit:
                isFit, reason = True, GUI_ITEM_ECONOMY_CODE.UNDEFINED
        else:
            isFit, reason = isEnoughMoney, purchaseReason
            if not isFit:
                if GUI_ITEM_ECONOMY_CODE.isCurrencyError(reason):
                    isFit = vehicleModule.mayPurchaseWithExchange(stats[b'money'], stats[b'exchangeRate'])
        if reason != GUI_ITEM_ECONOMY_CODE.UNLOCK_ERROR:
            installReason = _getInstallReason(vehicleModule, self._vehicle, reason, self._slotIndex)
        else:
            installReason = reason
        moduleData = self._buildCommonModuleData(vehicleModule, installReason)
        moduleData.update({b'targetVisible': isBought, 
           b'showPrice': (not isBought), 
           b'isSelected': isInstalledInSlot, 
           b'disabled': (not isFit or isInstalled and not isInstalledInSlot), 
           b'removeButtonLabel': (MENU.MODULEFITS_REMOVENAME), 
           b'removeButtonTooltip': (MENU.MODULEFITS_REMOVETOOLTIP), 
           b'itemPrices': (getItemPricesVOWithReason(reason, itemPrice))})
        return moduleData


class _PreviewLogicProvider(PopoverLogicProvider):

    def __init__(self, slotType, slotIndex):
        super(_PreviewLogicProvider, self).__init__(slotType, slotIndex, g_currentPreviewVehicle.item)
        self._tooltipType = TOOLTIPS_CONSTANTS.PREVIEW_MODULE
        return

    def setModule(self, newId, oldId, isRemove):
        g_currentPreviewVehicle.installComponent(int(newId))
        return

    def _buildModuleData(self, vehicleModule, isInstalledInSlot, _):
        isFit, reason = vehicleModule.mayInstall(self._vehicle, 0)
        moduleData = self._buildCommonModuleData(vehicleModule, reason)
        moduleData.update({b'targetVisible': isInstalledInSlot, 
           b'showPrice': False, 
           b'isSelected': isInstalledInSlot, 
           b'disabled': (not isFit), 
           b'removeButtonLabel': (MENU.MODULEFITS_REMOVENAME), 
           b'removeButtonTooltip': (MENU.MODULEFITS_REMOVETOOLTIP)})
        return moduleData
