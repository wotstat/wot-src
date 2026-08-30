from __future__ import absolute_import
from future.utils import lrange, viewvalues
from constants import MIN_VEHICLE_LEVEL, MAX_VEHICLE_LEVEL
from gui.Scaleform.genConsts.VEHICLE_SELECTOR_CONSTANTS import VEHICLE_SELECTOR_CONSTANTS
from gui.shared.formatters.vehicle_filters import packVehicleTypesFilter, packVehicleLevelsFilter, packNationsFilter
from gui.shared.utils.requesters import REQ_CRITERIA

class VehicleSelectorBase(object):

    def __init__(self):
        self.__filters = None
        self._levelsRange = lrange(MIN_VEHICLE_LEVEL, MAX_VEHICLE_LEVEL + 1)
        self.showNotReadyVehicles = True
        self._filterVisibility = VEHICLE_SELECTOR_CONSTANTS.VISIBLE_ALL
        self._compatibleOnlyLabel = b''
        return

    def getFilters(self):
        return self.__filters

    def _updateFilter(self, nation=-1, vehicleType=b'none', isMain=False, level=-1, compatibleOnly=False):
        self.__filters = {b'nation': nation, 
           b'vehicleType': vehicleType, 
           b'isMain': isMain, 
           b'level': level, 
           b'compatibleOnly': compatibleOnly}
        return

    def _updateData(self, allVehicles, compatiblePredicate=(lambda vo: vo.get(b'enabled'))):
        criteria = REQ_CRITERIA.EMPTY | REQ_CRITERIA.VEHICLE.ACTIVE_OR_MAIN_IN_NATION_GROUP
        criteria |= ~REQ_CRITERIA.VEHICLE.EXPIRED_IGR_RENT
        criteria |= ~REQ_CRITERIA.VEHICLE.DISABLED_IN_PREM_IGR
        if not self.showNotReadyVehicles:
            criteria |= REQ_CRITERIA.VEHICLE.READY
        if self.__filters:
            nations, levels, classes = self._parseFilters()
            if nations:
                criteria |= REQ_CRITERIA.NATIONS(nations)
            if classes:
                criteria |= REQ_CRITERIA.VEHICLE.CLASSES(classes)
            if self.__filters[b'isMain']:
                criteria |= REQ_CRITERIA.VEHICLE.FAVORITE
            if levels:
                criteria |= REQ_CRITERIA.VEHICLE.LEVELS(levels)
        filteredVehicles = allVehicles.filter(criteria)
        if self.__filters.get(b'compatibleOnly', True):
            predicate = compatiblePredicate
        else:
            predicate = lambda vo: True
        result = []
        for v in viewvalues(filteredVehicles):
            vo = self._makeVehicleVOAction(v)
            if predicate(vo):
                result.append(vo)

        return result

    def _parseFilters(self):
        nations, levels, classes = (None, None, None)
        if b'nation' in self.__filters and self.__filters[b'nation'] != -1:
            nations = [
             self.__filters[b'nation']]
        if b'level' in self.__filters and self.__filters[b'level'] != -1:
            levels = [
             self.__filters[b'level']]
        if b'vehicleType' in self.__filters and self.__filters[b'vehicleType'] != b'none':
            classes = [
             self.__filters[b'vehicleType']]
        return (nations, levels, classes)

    def _initFilter(self, nation=-1, vehicleType=b'none', isMain=False, level=-1, compatibleOnly=False):
        levelsDP = packVehicleLevelsFilter(self._levelsRange)
        if len(levelsDP) <= 2:
            self._filterVisibility ^= VEHICLE_SELECTOR_CONSTANTS.VISIBLE_LEVEL
        filtersData = {b'vehicleTypesDP': (packVehicleTypesFilter(defaultVehType=b'none')), 
           b'levelsDP': levelsDP, 
           b'nation': nation, 
           b'nationDP': (packNationsFilter()), 
           b'vehicleType': vehicleType, 
           b'isMain': isMain, 
           b'level': level, 
           b'compatibleOnly': compatibleOnly, 
           b'visibility': (self._filterVisibility), 
           b'compatibleOnlyLabel': (self._compatibleOnlyLabel)}
        return filtersData

    def _makeVehicleVOAction(self, vehicle):
        raise NotImplementedError
        return
