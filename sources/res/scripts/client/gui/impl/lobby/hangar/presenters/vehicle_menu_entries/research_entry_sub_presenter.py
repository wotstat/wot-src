from __future__ import absolute_import
import json
from CurrentVehicle import g_currentVehicle
from gui.impl.gen.view_models.views.lobby.hangar.vehicle_menu_model import VehicleMenuModel
from gui.impl.lobby.hangar.presenters.vehicle_menu_entries.base_menu_entry_sub_presenter import BaseMenuEntrySubPresenter
from gui.prb_control.entities.base.listener import IPrbListener
from gui.shared import EVENT_BUS_SCOPE, events
from gui.shared.event_dispatcher import showVehicleHubModules
from gui.shared.utils.module_upd_available_helper import getResearchInfo
from helpers import dependency
from skeletons.gui.shared import IItemsCache

class ResearchEntrySubPresenter(BaseMenuEntrySubPresenter, IPrbListener):
    __itemsCache = dependency.descriptor(IItemsCache)

    def packEntry(self):
        super(ResearchEntrySubPresenter, self).packEntry()
        menuEntries = self.getViewModel().getMenuEntries()
        entryData = json.loads(menuEntries[self._entryId])
        entryData[b'counter'] = self.__getCounter()
        if self._getMenuEntryState() == VehicleMenuModel.WARNING:
            unviewedModules = self.__getUnviewedResearchModules()
            entryData[b'researchItems'] = unviewedModules
        menuEntries.set(self._entryId, json.dumps(entryData))
        return

    def onNavigate(self):
        showVehicleHubModules(g_currentVehicle.item.intCD)
        return

    def _getListeners(self):
        return (
         (
          events.PrebattleEvent.SWITCHED, self.__onPrbEntitySwitched, EVENT_BUS_SCOPE.LOBBY),)

    def _getEvents(self):
        return (
         (
          self._cameraController.onEnabledChange, self.__onCameraEnabledChange),)

    def _getState(self):
        if g_currentVehicle.isInBattle():
            return VehicleMenuModel.DISABLED
        unviewedModules = self.__getUnviewedResearchModules()
        if unviewedModules:
            return VehicleMenuModel.WARNING
        return VehicleMenuModel.ENABLED

    def __getCounter(self):
        if g_currentVehicle is not None:
            unviewedModules = self.__getUnviewedResearchModules()
            if unviewedModules:
                return len(unviewedModules)
            return 0
        return

    def __getUnviewedResearchModules(self):
        researchInfo = getResearchInfo(vehicle=g_currentVehicle.item)
        if not researchInfo:
            return None
        else:
            researchItems = researchInfo.getUnviewedItems()
            if not researchItems:
                return []
            modules = []
            for item in researchItems:
                module = self.__itemsCache.items.getItemByCD(item)
                if module.itemTypeName == b'vehicle':
                    continue
                if module.itemTypeName == b'vehicleChassis' and module.isWheeledChassis():
                    modules.append(b'vehicleWheels')
                else:
                    modules.append(module.itemTypeName)

            return modules

    def __onPrbEntitySwitched(self, _):
        self.packEntry()
        return

    def __onCameraEnabledChange(self, _):
        self.packEntry()
        return
