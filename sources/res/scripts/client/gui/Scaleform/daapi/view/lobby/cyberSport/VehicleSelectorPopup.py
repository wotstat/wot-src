from account_helpers.AccountSettings import AccountSettings
from constants import VEHICLE_CLASSES, BATTLE_MODE_VEHICLE_TAGS
from gui.Scaleform.daapi.view.lobby.vehicle_selector_base import VehicleSelectorBase
from gui.Scaleform.daapi.view.lobby.rally.vo_converters import makeVehicleVO
from gui.Scaleform.daapi.view.meta.VehicleSelectorPopupMeta import VehicleSelectorPopupMeta
from gui.Scaleform.genConsts.VEHICLE_SELECTOR_CONSTANTS import VEHICLE_SELECTOR_CONSTANTS
from gui.Scaleform.locale.RES_ICONS import RES_ICONS
from gui.Scaleform.locale.TOOLTIPS import TOOLTIPS
from gui.shared.events import CSVehicleSelectEvent, HideWindowEvent
from gui.shared.utils.requesters import REQ_CRITERIA
from helpers import dependency
from skeletons.gui.shared import IItemsCache

class VehicleSelectorPopup(VehicleSelectorPopupMeta, VehicleSelectorBase):
    itemsCache = dependency.descriptor(IItemsCache)

    def __init__(self, ctx=None):
        super(VehicleSelectorPopup, self).__init__()
        self._levelsRange = ctx.get(b'levelsRange', self._levelsRange)
        self.__isMultiSelect = ctx.get(b'isMultiSelect', False)
        self._infoText = ctx.get(b'infoText', b'')
        self.__componentsOffset = ctx.get(b'componentsOffset', 0)
        self._titleText = ctx.get(b'titleText', b'')
        self._selectButton = ctx.get(b'selectButton', b'')
        self._cancelButton = ctx.get(b'cancelButton', b'')
        self._compatibleOnlyLabel = ctx.get(b'compatibleOnlyLabel', b'')
        self.__section = ctx[b'section']
        self._vehicles = ctx.get(b'vehicles')
        self.__selectedVehicles = ctx.get(b'selectedVehicles')
        self.__vehicleTypes = ctx.get(b'vehicleTypes', VEHICLE_CLASSES)
        self._filterVisibility = ctx.get(b'filterVisibility', VEHICLE_SELECTOR_CONSTANTS.VISIBLE_ALL)
        self.showNotReadyVehicles = ctx.get(b'showNotReady', True)
        return

    def _populate(self):
        super(VehicleSelectorPopup, self)._populate()
        self.addListener(HideWindowEvent.HIDE_VEHICLE_SELECTOR_WINDOW, self.onWindowForceClose)
        self.initFilters()
        self.as_setListModeS(self.__isMultiSelect)
        self.as_setTextsS(self._titleText, self._infoText, self._selectButton, self._cancelButton)
        return

    def _dispose(self):
        self.removeListener(HideWindowEvent.HIDE_VEHICLE_SELECTOR_WINDOW, self.onWindowForceClose)
        currentFilters = self.getFilters()
        if currentFilters:
            self.only_ = {b'nation': (currentFilters[b'nation']), b'vehicleType': (currentFilters[b'vehicleType']), b'isMain': (currentFilters[b'isMain']), b'level': (currentFilters[b'level']), b'compatibleOnly': (currentFilters[b'compatibleOnly'])}
            filters = self.only_
            AccountSettings.setFilter(self.__section, filters)
        super(VehicleSelectorPopup, self)._dispose()
        return

    def onWindowForceClose(self, _):
        self.destroy()
        return

    def onWindowClose(self):
        self.destroy()
        return

    def onSelectVehicles(self, items):
        self.fireEvent(CSVehicleSelectEvent(CSVehicleSelectEvent.VEHICLE_SELECTED, items))
        self.onWindowClose()
        return

    def onFiltersUpdate(self, nation, vehicleType, isMain, level, compatibleOnly):
        self._updateFilter(nation, vehicleType, isMain, level, compatibleOnly)
        self.updateData()
        return

    def initFilters(self):
        filters = AccountSettings.getFilter(self.__section)
        filters = self._initFilter(**filters)
        self._updateFilter(filters[b'nation'], filters[b'vehicleType'], filters[b'isMain'], filters[b'level'], filters[b'compatibleOnly'])
        self.as_setFiltersDataS(filters)
        return

    def updateData(self):
        if not self.getFilters().get(b'compatibleOnly', True) or self._vehicles is None:
            criteria = REQ_CRITERIA.INVENTORY
            criteria |= ~REQ_CRITERIA.VEHICLE.HAS_ANY_TAG(BATTLE_MODE_VEHICLE_TAGS)
            criteria |= ~REQ_CRITERIA.VEHICLE.HIDDEN_IN_HANGAR
            vehicleVOs = self._updateData(self.itemsCache.items.getVehicles(criteria))
        else:
            vehicleVOs = self._updateData(self._vehicles)
        if self.__selectedVehicles is not None:
            vehicleGetter = self.itemsCache.items.getItemByCD
            selected = [makeVehicleVO(vehicleGetter(int(item))) for item in self.__selectedVehicles]
        else:
            selected = None
        for vehicleVO in vehicleVOs:
            if self._vehicles is not None and vehicleVO[b'intCD'] not in self._vehicles.keys() and vehicleVO[b'enabled']:
                vehicleVO[b'tooltip'] = TOOLTIPS.CYBERSPORT_VEHICLESELECTOR_BADVEHICLE
                vehicleVO[b'enabled'] = False
                vehicleVO[b'showAlert'] = True
                vehicleVO[b'alertSource'] = RES_ICONS.MAPS_ICONS_LIBRARY_GEAR
                vehicleVO[b'isReadyToFight'] = True

        self.setListData(vehicleVOs, selected)
        return

    def setListData(self, vehicleVOs, selected):
        self.as_setListDataS(vehicleVOs, selected)
        return

    def selectClick(self):
        return

    def _makeVehicleVOAction(self, vehicle):
        vehicleVO = makeVehicleVO(vehicle, self._levelsRange, self.__vehicleTypes)
        if vehicle.isOnlyForEpicBattles:
            vehicleVO[b'enabled'], vehicleVO[b'tooltip'] = False, TOOLTIPS.CYBERSPORT_UNIT_FIGHTBTN_EVENTVEHICLEWRONGMODE
        return vehicleVO
