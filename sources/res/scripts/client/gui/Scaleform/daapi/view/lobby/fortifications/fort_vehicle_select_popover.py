from __future__ import absolute_import
from constants import QUEUE_TYPE
from gui import makeHtmlString
from gui.Scaleform import MENU
from gui.Scaleform import getButtonsAssetPath
from gui.Scaleform.daapi.view.lobby.vehicle_compare.formatters import packHeaderColumnData
from gui.Scaleform.daapi.view.lobby.vehicle_selector_base import VehicleSelectorBase
from gui.Scaleform.daapi.view.meta.FortVehicleSelectPopoverMeta import FortVehicleSelectPopoverMeta
from gui.Scaleform.locale.CYBERSPORT import CYBERSPORT
from gui.Scaleform.locale.FORTIFICATIONS import FORTIFICATIONS
from gui.Scaleform.locale.RES_ICONS import RES_ICONS
from gui.Scaleform.locale.TOOLTIPS import TOOLTIPS
from gui.Scaleform.locale.VEH_COMPARE import VEH_COMPARE
from gui.clans.stronghold_event_requester import FrozenVehiclesConstants
from gui.prb_control.entities.base.unit.listener import IUnitListener
from gui.shared.events import CSVehicleSelectEvent, StrongholdEvent
from gui.shared.formatters import text_styles
from gui.shared.gui_items.Vehicle import VEHICLE_TYPES_ORDER, getSmallIconPath, Vehicle, getTypeSmallIconPath
from gui.shared.utils.functions import makeTooltip
from gui.shared.utils.requesters import REQ_CRITERIA
from helpers import dependency
from helpers.i18n import makeString
from skeletons.gui.shared import IItemsCache
_IGNORED_VEHICLE_STATES = (
 Vehicle.VEHICLE_STATE.UNDAMAGED,
 Vehicle.VEHICLE_STATE.IN_PREBATTLE,
 Vehicle.GROUP_STATES)

def convertState(vState):
    if vState in _IGNORED_VEHICLE_STATES:
        return b''
    if vState == Vehicle.VEHICLE_STATE.IN_PREMIUM_IGR_ONLY:
        return makeHtmlString(b'html_templates:lobby', b'inPremiumIgrOnly')
    return makeString(MENU.tankcarousel_vehiclestates(vState))


def getVehicleCriteria(levelsRange, inHangar=False):
    req = REQ_CRITERIA.VEHICLE.LEVELS(levelsRange) | ~REQ_CRITERIA.SECRET | ~REQ_CRITERIA.VEHICLE.EVENT_BATTLE | ~REQ_CRITERIA.VEHICLE.FORBIDDEN_VEHICLE_TO_BATTLE
    if inHangar:
        req |= REQ_CRITERIA.INVENTORY
    return req


class FortVehicleSelectPopover(FortVehicleSelectPopoverMeta, VehicleSelectorBase, IUnitListener):
    itemsCache = dependency.descriptor(IItemsCache)

    def __init__(self, ctx=None):
        super(FortVehicleSelectPopover, self).__init__(ctx)
        self._classFilters = None
        data = ctx.get(b'data', None)
        self._showMainBtn = data.showMainBtn
        self._slotIndex = data.slotIndex
        self._levelsRange = data.levelsRange
        self._selectedVehicles = data.selectedVehicles
        return

    def setVehicleSelected(self, dbID, autoClose):
        super(FortVehicleSelectPopover, self).setVehicleSelected(dbID, autoClose)
        if not autoClose:
            self.updateAddButtonLabel()
        return

    def updateAddButtonLabel(self):
        selectedCount = len(self._vehDP.getSelected())
        buttonState = {b'btnEnabled': (selectedCount > 0)}
        if self._isMultiSelect:
            buttonState[b'btnLabel'] = makeString(FORTIFICATIONS.FORTVEHPOPOVER_BTNSAVE, count=selectedCount)
        else:
            buttonState[b'btnLabel'] = makeString(CYBERSPORT.WINDOW_ROSTERSLOTSETTINGS_VEHICLETAB_SUBMITBTN)
        self.as_setAddButtonStateS(buttonState)
        return

    def applyFilters(self, nation, vehicleType, level, isMain, hangarOnly):
        self._updateFilter(nation, vehicleType, isMain, level, hangarOnly)
        self.updateData()
        return

    def onFilterChange(self, index, value):
        self._classFilters[index] = value
        self.updateData()
        return

    def initFilters(self):
        self._classFilters = [False for _ in VEHICLE_TYPES_ORDER]
        filters = self._initFilter()
        self._updateFilter(filters[b'nation'], filters[b'vehicleType'], filters[b'isMain'], filters[b'level'], filters[b'compatibleOnly'])
        return filters

    def updateData(self):
        vehicleCriteria = getVehicleCriteria(levelsRange=self._levelsRange, inHangar=not self._isMultiSelect)
        vehicles = self._updateData(self.itemsCache.items.getVehicles(vehicleCriteria), compatiblePredicate=(lambda vo: vo[b'inHangar']))
        self._vehDP.buildList(vehicles)
        self._updateSortField()
        return

    def addButtonClicked(self):
        vehicles = self._vehDP.getSelected()
        if not self._isMultiSelect:
            self.fireEvent(CSVehicleSelectEvent(CSVehicleSelectEvent.VEHICLE_SELECTED, list(vehicles)))
        else:
            self.fireEvent(StrongholdEvent(StrongholdEvent.STRONGHOLD_VEHICLES_SELECTED, {b'items': (list(vehicles)), b'slotIndex': (self._slotIndex)}))
        self.onWindowClose()
        return

    def _populate(self):
        super(FortVehicleSelectPopover, self)._populate()
        self.__initControls()
        self._initDP()
        self.updateData()
        self.updateAddButtonLabel()
        return

    def _getHeader(self):
        if self._isMultiSelect:
            return FORTIFICATIONS.STRONGHOLDPOPOVER_COMMANDERHEADER
        return FORTIFICATIONS.STRONGHOLDPOPOVER_HEADER

    def _parseFilters(self):
        nations, _, _ = super(FortVehicleSelectPopover, self)._parseFilters()
        classes = [VEHICLE_TYPES_ORDER[i] for i, v in enumerate(self._classFilters) if v]
        if not classes:
            classes = list(VEHICLE_TYPES_ORDER)
        return (nations, None, classes)

    def _initFilter(self, nation=-1, vehicleType=b'none', isMain=False, level=-1, compatibleOnly=False):
        filtersData = super(FortVehicleSelectPopover, self)._initFilter(nation, vehicleType, isMain, level, compatibleOnly)
        filtersData[b'togglesDP'] = self.__createFilterToggles()
        filtersData[b'nationTooltip'] = makeTooltip(MENU.NATIONS_TITLE, TOOLTIPS.VEHICLESELECTOR_FILTER_NATION)
        if self._showMainBtn:
            entry = b'favorite'
            filtersData[b'mainBtn'] = {b'value': (getButtonsAssetPath(entry)), 
               b'tooltip': (makeTooltip((b'#tank_carousel_filter:tooltip/{}/header').format(entry), makeString((b'#tank_carousel_filter:tooltip/{}/body').format(entry)))), 
               b'selected': False}
        return filtersData

    def _dispose(self):
        super(FortVehicleSelectPopover, self)._dispose()
        self._classFilters = None
        return

    def _makeVehicleVOAction(self, vehicle):
        if self._selectedVehicles:
            checkSelectedFunc = self._isSelected
        else:
            checkSelectedFunc = lambda vo: False
        vState, _ = vehicle.getState()
        isFrozen = False
        if self.prbEntity is not None and self.prbEntity.getQueueType() == QUEUE_TYPE.STRONGHOLD_UNITS:
            frozenVehicles = self.prbEntity.getEventFrozenVehicles()
            isFrozen = frozenVehicles is not None and (frozenVehicles == FrozenVehiclesConstants.ALL_VEHICLES_FROZEN or vehicle.intCD in frozenVehicles)
        return {b'dbID': (vehicle.intCD), 
           b'level': (vehicle.level), 
           b'shortUserName': (vehicle.shortUserName), 
           b'smallIconPath': (getSmallIconPath(vehicle.name)), 
           b'nationID': (vehicle.nationID), 
           b'type': (vehicle.type), 
           b'typeIcon': (getTypeSmallIconPath(vehicle.type, vehicle.isPremium)), 
           b'selected': (checkSelectedFunc(vehicle)), 
           b'inHangar': False, 
           b'isMultiSelect': (self._isMultiSelect), 
           b'isReadyToFight': (vehicle.isReadyToFight), 
           b'enabled': (vehicle.isReadyToFight), 
           b'isFrozen': isFrozen, 
           b'tooltip': (makeTooltip(b'#tooltips:vehicleStatus/%s/header' % vState, b'#tooltips:vehicleStatus/body')), 
           b'state': (b'frozenVehicle' if isFrozen and vehicle.isReadyToFight else convertState(vState))}

    def _isSelected(self, entry):
        return entry.intCD in self._selectedVehicles

    def __initControls(self):
        common = {b'btnHeight': 34, b'enabled': True}
        nameWidth = 200 if self._isMultiSelect else 245
        headers = [
         packHeaderColumnData(b'nations', 43, icon=RES_ICONS.MAPS_ICONS_FILTERS_NATIONS_ALL, tooltip=VEH_COMPARE.ADDVEHPOPOVER_TOOLTIPS_NATION, **common),
         packHeaderColumnData(b'type', 33, icon=RES_ICONS.MAPS_ICONS_FILTERS_TANKS_ALL, tooltip=VEH_COMPARE.ADDVEHPOPOVER_TOOLTIPS_TYPE, **common),
         packHeaderColumnData(b'level', 33, icon=RES_ICONS.MAPS_ICONS_BUTTONS_TAB_SORT_BUTTON_LEVEL, tooltip=VEH_COMPARE.ADDVEHPOPOVER_TOOLTIPS_LEVEL, btnHeight=34, enabled=False),
         packHeaderColumnData(b'name', nameWidth, label=VEH_COMPARE.ADDVEHPOPOVER_VEHICLENAME, tooltip=VEH_COMPARE.ADDVEHPOPOVER_TOOLTIPS_TITLE, direction=b'ascending', **common)]
        if self._isMultiSelect:
            headers.insert(0, packHeaderColumnData(b'check', 45, icon=RES_ICONS.MAPS_ICONS_BUTTONS_ICON_TABLE_COMPARISON_CHECKMARK, **common))
        self.as_setInitDataS({b'tableHeaders': headers, 
           b'filters': (self.initFilters()), 
           b'header': (text_styles.highTitle(makeString(self._getHeader()))), 
           b'btnCancel': (VEH_COMPARE.ADDVEHPOPOVER_BTNCANCEL), 
           b'isMultiSelect': (self._isMultiSelect)})
        return

    def __getAssetPath(self, assetType, extension=b'.png'):
        return (b'').join([b'../maps/icons/filters/tanks/', assetType, extension])

    def __createFilterToggles(self):
        filterToggles = []
        for entry in VEHICLE_TYPES_ORDER:
            filterToggles.append({b'value': (self.__getAssetPath(entry)), 
               b'tooltip': (makeTooltip((b'#menu:carousel_tank_filter/{}').format(entry), b'#tank_carousel_filter:tooltip/vehicleTypes/body')), 
               b'selected': False})

        return filterToggles
