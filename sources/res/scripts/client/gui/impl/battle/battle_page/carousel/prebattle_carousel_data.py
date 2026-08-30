from collections import namedtuple
from account_helpers.AccountSettings import COMP7_CAROUSEL_FILTER_1, COMP7_CAROUSEL_FILTER_2, COMP7_CAROUSEL_FILTER_CLIENT_1, AccountSettings
from gui import GUI_NATIONS_ORDER_INDEX
from gui.Scaleform.daapi.view.common.vehicle_carousel.carousel_data_provider import CarouselDataProvider
from gui.Scaleform.daapi.view.common.vehicle_carousel.carousel_filter import RoleCriteriesGroup, CarouselFilter
from gui.battle_control.gui_vehicle_builder import VehicleBuilder
from gui.shared.gui_items.Vehicle import VEHICLE_TYPES_ORDER_INDICES
from gui.shared.utils.requesters import REQ_CRITERIA
from helpers import dependency
from items.vehicles import getVehicleType
from skeletons.gui.shared.gui_items import IGuiItemsFactory

def getComp7CarouselVehicleDataVO(vehicle):
    return {b'vehicleName': (vehicle.shortUserName), 
       b'favorite': (vehicle.isFavorite), 
       b'enabled': True, 
       b'roleName': (vehicle.roleLabel if vehicle.roleLabel != b'role_SPG' else b'')}


class _InBattleRentedCriteriesGroup(RoleCriteriesGroup):

    def __init__(self, rentedList):
        super(_InBattleRentedCriteriesGroup, self).__init__()
        self.__rentedList = rentedList
        return

    def update(self, filters):
        self._criteria = REQ_CRITERIA.EMPTY
        self._setNationsCriteria(filters)
        self._setClassesCriteria(filters)
        self._setRentedCriteria(filters)
        self._setFavoriteVehicleCriteria(filters)
        self._setVehicleNameCriteria(filters)
        self._setRolesCriteria(filters)
        return

    def _setRentedCriteria(self, filters):
        if not filters[b'rented']:
            self._criteria |= ~REQ_CRITERIA.VEHICLE.SPECIFIC_BY_CD(self.__rentedList)
        return


class PrebattleCarouselFilter(CarouselFilter):

    def __init__(self):
        self.__rentedList = []
        super(PrebattleCarouselFilter, self).__init__()
        self._serverSections = (COMP7_CAROUSEL_FILTER_1, COMP7_CAROUSEL_FILTER_2)
        self._clientSections = (COMP7_CAROUSEL_FILTER_CLIENT_1,)
        return

    def save(self):
        return

    def load(self):
        filters = AccountSettings.getFilterDefaults(self._serverSections)
        for section in self._clientSections:
            filters.update(AccountSettings.getFilterDefault(section))

        self._filters = filters
        self.update(filters, save=False)
        return

    def setRentedList(self, rentedList):
        self.__rentedList = rentedList
        self._setCriteriaGroups()
        self._updateCriteriesGroups()
        return

    def _setCriteriaGroups(self):
        self._criteriesGroups = (_InBattleRentedCriteriesGroup(self.__rentedList), RoleCriteriesGroup())
        return


class PrebattleCarouselDataProvider(CarouselDataProvider):
    _itemsFactory = dependency.descriptor(IGuiItemsFactory)
    _RawVehicleData = namedtuple(b'_RawVehicleData', (b'strCD', b'settings', b'isElite', b'isRented'))

    def __init__(self, carouselFilter, itemsCache):
        super(PrebattleCarouselDataProvider, self).__init__(carouselFilter, itemsCache)
        self.__vehiclesData = {}
        self.__selectedCD = None
        return

    def getSelectedCD(self):
        return self.__selectedCD

    def applyFilter(self, forceApply=False):
        prevFilteredIndices = self._filteredIndices[:]
        prevSelectedIdx = self._selectedIdx
        self._filteredIndices = []
        self._selectedIdx = -1
        visibleVehiclesIntCDs = [vehicle.intCD for vehicle in self._getCurrentVehicles()]
        for idx in self._getSortedIndices():
            if idx >= len(self._vehicles):
                continue
            vehicle = self._vehicles[idx]
            if vehicle.intCD in visibleVehiclesIntCDs:
                self._filteredIndices.append(idx)
                if self.__selectedCD == vehicle.intCD:
                    self._selectedIdx = len(self._filteredIndices) - 1

        needUpdate = forceApply or prevFilteredIndices != self._filteredIndices or prevSelectedIdx != self._selectedIdx
        if needUpdate:
            self._filterByIndices()
        return

    def getVehicleCDByIdx(self, filteredIdx):
        realIdx = self._filteredIndices[filteredIdx]
        vehicle = self._vehicles[realIdx]
        return vehicle.intCD

    def setVehicles(self, vehiclesList):
        self.__vehiclesData = {}
        rentedList = []
        for v in vehiclesList:
            vehData = self._RawVehicleData(v[b'compDescr'], v[b'settings'], bool(v[b'isElite']), bool(v[b'isRent']))
            intCD = getVehicleType(vehData.strCD).compactDescr
            self.__vehiclesData[intCD] = vehData
            if vehData.isRented:
                rentedList.append(intCD)

        self._filter.setRentedList(rentedList)
        self.buildList()
        return

    def setCurrentVehicle(self, vehicleCD):
        if vehicleCD is None:
            return
        else:
            for vehicle in self._vehicles:
                if vehicle.compactDescr == vehicleCD:
                    self.__selectedCD = vehicleCD
                    self.applyFilter()
                    self.refresh()
                    break

            return

    def _buildVehicleItems(self):
        self._vehicles = []
        self._vehicleItems = []
        for vehicleData in self.__vehiclesData.itervalues():
            vehicle = self.__makeGuiVehicle(vehicleData)
            self._vehicles.append(vehicle)

        return

    def getGetFilteredVehiclesCDs(self):
        return {self._vehicles[idx].compactDescr for idx in self._filteredIndices if idx < len(self._vehicles)}

    def getSortedVehicles(self):
        return [self._vehicles[idx] for idx in self._getSortedIndices() if idx < len(self._vehicles)]

    @property
    def collection(self):
        return self._vehicles

    @classmethod
    def _vehicleComparisonKey(cls, vehicle):
        return (
         not vehicle.isFavorite,
         GUI_NATIONS_ORDER_INDEX[vehicle.nationName],
         VEHICLE_TYPES_ORDER_INDICES[vehicle.type],
         vehicle.userName)

    @staticmethod
    def __makeGuiVehicle(vehicleData):
        builder = VehicleBuilder()
        builder.setStrCD(vehicleData.strCD)
        builder.setSettings(vehicleData.settings)
        return builder.getResult()
