from account_helpers.AccountSettings import AccountSettings
from gui.Scaleform.daapi.view.lobby.vehicle_selector_base import VehicleSelectorBase
from gui.Scaleform.daapi.view.lobby.rally.vo_converters import makeVehicleVO, makeFiltersVO, makeVehicleBasicVO
from gui.Scaleform.daapi.view.meta.RosterSlotSettingsWindowMeta import RosterSlotSettingsWindowMeta
from gui.Scaleform.genConsts.CYBER_SPORT_ALIASES import CYBER_SPORT_ALIASES
from gui.Scaleform.locale.CYBERSPORT import CYBERSPORT
from gui.Scaleform.locale.TOOLTIPS import TOOLTIPS
from gui.shared.events import CSRosterSlotSettingsWindow
from gui.shared.formatters import text_styles, icons
from gui.shared.utils.requesters import REQ_CRITERIA
from helpers import dependency
from nation_change.nation_change_helpers import iterVehTypeCDsInNationGroup
from skeletons.gui.shared import IItemsCache
VEHICLE_SELECTOR_TAB_ID = b'vehicleSelectorTab'
RANGE_SELECTOR_TAB_ID = b'rangeSelectorTab'
TAB_ORDER = [
 VEHICLE_SELECTOR_TAB_ID, RANGE_SELECTOR_TAB_ID]
TAB_DATA_MAP = {VEHICLE_SELECTOR_TAB_ID: (
                           CYBER_SPORT_ALIASES.VEHICLE_SELECTOR_VIEW,
                           CYBERSPORT.WINDOW_ROSTERSLOTSETTINGS_TABBTNLBL_VEHICLE), 
   RANGE_SELECTOR_TAB_ID: (
                         CYBER_SPORT_ALIASES.RANGE_ROSTER_SETTINGS_VIEW,
                         CYBERSPORT.WINDOW_ROSTERSLOTSETTINGS_TABBTNLBL_RANGE)}

class RosterSlotSettingsWindow(RosterSlotSettingsWindowMeta, VehicleSelectorBase):
    itemsCache = dependency.descriptor(IItemsCache)

    def __init__(self, ctx=None):
        super(RosterSlotSettingsWindow, self).__init__()
        self._levelsRange = ctx.get(b'levelsRange', self._levelsRange)
        self.__section = ctx[b'section']
        self.__levelsLimits = self.__convertLevelsRange(self._levelsRange)
        self.__vehicleTypes = ctx.get(b'vehicleTypes', None)
        self.__flashSlots = ctx.get(b'settings')
        return

    def updateSlots(self, slots):
        self.__currentSlot, tabID = self.__makeInitialSlotData(slots.pop())
        self.__setSelection(tabID)
        return

    def onFiltersUpdate(self, nation, vehicleType, isMain, level, compatibleOnly):
        self._updateFilter(nation, vehicleType, isMain, level, compatibleOnly)
        self.updateData()
        return

    def updateData(self):
        result = self._updateData(self.itemsCache.items.getVehicles(~REQ_CRITERIA.SECRET))
        self.as_setListDataS(result)
        return

    def requestVehicleFilters(self):
        filters = AccountSettings.getFilter(self.__section)
        filters[b'isMain'] = False
        result = self._initFilter(**filters)
        result.update({b'compatibleOnlyLabel': (CYBERSPORT.WINDOW_VEHICLESELECTOR_FILTERS_MATCHES)})
        self.as_updateVehicleFiltersS(result)
        return

    def submitButtonHandler(self, value):
        self.__currentSlot, _ = self.__makeInitialSlotData(value)
        slotSettins = self.__getSlotsSettings()
        self.fireEvent(CSRosterSlotSettingsWindow(CSRosterSlotSettingsWindow.APPLY_SLOT_SETTINGS, slotSettins))
        if self.__currentSlot is not None and b'intCD' in self.__currentSlot:
            self.__addAditionalSlot(slotSettins)
        self.onWindowClose()
        return

    def cancelButtonHandler(self):
        self.onWindowClose()
        return

    def onWindowClose(self):
        self.destroy()
        return

    def _populate(self):
        super(RosterSlotSettingsWindow, self)._populate()
        self.as_setStaticDataS(self.__packStaticData())
        self.__currentSlot, tabID = self.__makeInitialSlotData(self.__flashSlots.pop())
        self.setLimits()
        self.__setSelection(tabID)
        return

    def setLimits(self):
        self.as_setRosterLimitsS({b'minLevel': (self.__levelsLimits[0]), 
           b'maxLevel': (self.__levelsLimits[1])})
        return

    def _dispose(self):
        currentFilters = self.getFilters()
        if currentFilters:
            filters = {b'nation': (currentFilters[b'nation']), b'vehicleType': (currentFilters[b'vehicleType']), 
               b'isMain': (currentFilters[b'isMain']), 
               b'level': (currentFilters[b'level']), 
               b'compatibleOnly': (currentFilters[b'compatibleOnly'])}
            AccountSettings.setFilter(self.__section, filters)
        self._levelsRange = None
        self.__currentSlot = None
        self.__flashSlots = None
        self.__section = None
        self.__vehicleTypes = None
        super(RosterSlotSettingsWindow, self)._dispose()
        return

    def _makeVehicleVOAction(self, vehicle):
        return makeVehicleBasicVO(vehicle, self._levelsRange, self.__vehicleTypes)

    def __packStaticData(self):
        text = text_styles.main(CYBERSPORT.WINDOW_ROSTERSLOTSETTINGS_VEHICLETAB_HEADERTEXT)
        return {b'windowTitle': (CYBERSPORT.WINDOW_ROSTERSLOTSETTINGS_TITLE), 
           b'headerText': (b'%s %s' % (text, icons.info())), 
           b'headerTextTooltip': (TOOLTIPS.CYBERSPORT_ROSTERSLOTSETTINGS_HEADERTEXT), 
           b'selectedTxt': (text_styles.middleTitle(CYBERSPORT.WINDOW_ROSTERSLOTSETTINGS_BOTTOMRESULT)), 
           b'submitBtnLabel': (CYBERSPORT.WINDOW_ROSTERSLOTSETTINGS_VEHICLETAB_SUBMITBTN), 
           b'cancelBtnLabel': (CYBERSPORT.WINDOW_ROSTERSLOTSETTINGS_VEHICLETAB_CANCELBTN), 
           b'buttonBarItems': (self.__packTabsData())}

    def __packTabsData(self):
        data = []
        for tabID in TAB_ORDER:
            linkage, label = TAB_DATA_MAP[tabID]
            data.append({b'label': label, 
               b'linkage': linkage})

        return data

    def __setSelection(self, tabID):
        if tabID == VEHICLE_SELECTOR_TAB_ID:
            self.as_setVehicleSelectionS(self.__currentSlot)
            self.as_selectTabS(TAB_ORDER.index(tabID))
        elif tabID == RANGE_SELECTOR_TAB_ID:
            self.as_setRangeSelectionS(self.__currentSlot)
            self.as_selectTabS(TAB_ORDER.index(tabID))
        else:
            self.as_resetSelectionS()
            self.as_selectTabS(TAB_ORDER.index(VEHICLE_SELECTOR_TAB_ID))
        return

    def __makeInitialSlotData(self, currentSlotSetting):
        if currentSlotSetting is None:
            return (None, None)
        else:
            if currentSlotSetting.selectedVehicle > 0:
                vehicle = self.itemsCache.items.getItemByCD(int(currentSlotSetting.selectedVehicle))
                return (
                 makeVehicleVO(vehicle, self.__convertLevelsRange(self._levelsRange), self.__vehicleTypes),
                 VEHICLE_SELECTOR_TAB_ID)
            if currentSlotSetting.nationIDRange or currentSlotSetting.vTypeRange or currentSlotSetting.vLevelRange:
                levelsRange = self.__convertLevelsRange(currentSlotSetting.vLevelRange or self._levelsRange)
                return (
                 makeFiltersVO(currentSlotSetting.nationIDRange, currentSlotSetting.vTypeRange, levelsRange),
                 RANGE_SELECTOR_TAB_ID)
            return (None, None)

    def __convertLevelsRange(self, levels):
        return levels[::len(levels) - 1]

    def __getSlotsSettings(self):
        slotsSettings = []
        slotsSettings.extend(self.__flashSlots)
        slotsSettings.append(self.__currentSlot)
        return slotsSettings

    def __addAditionalSlot(self, slotSettins):
        row = slotSettins[0]
        column = slotSettins[1]
        vehicleCD = self.__currentSlot[b'intCD']
        vehicle = self.itemsCache.items.getItemByCD(int(vehicleCD))
        if vehicle.hasNationGroup and vehicle.activeInNationGroup:
            addVehCD = iterVehTypeCDsInNationGroup(vehicleCD).next()
            vehicle = self.itemsCache.items.getItemByCD(addVehCD)
            addSlot = makeVehicleVO(vehicle, self.__convertLevelsRange(self._levelsRange), self.__vehicleTypes)
            slotSettings = [row, 1 - column, addSlot]
            self.fireEvent(CSRosterSlotSettingsWindow(CSRosterSlotSettingsWindow.APPLY_SLOT_SETTINGS, slotSettings))
        return
