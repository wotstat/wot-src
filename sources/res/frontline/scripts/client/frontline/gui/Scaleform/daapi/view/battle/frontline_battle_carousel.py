import logging, weakref, BigWorld, Event
from account_helpers.AccountSettings import EPICBATTLE_CAROUSEL_FILTER_1, EPICBATTLE_CAROUSEL_FILTER_2, EPICBATTLE_CAROUSEL_FILTER_CLIENT_2
from frontline.gui.Scaleform.daapi.view.battle.frontline_battle_carousel_filters import FLRentedCriteriaGroup, FL_RENT
from frontline.gui.Scaleform.daapi.view.meta.BattleTankCarouselMeta import BattleTankCarouselMeta
from frontline.gui.Scaleform.genConsts.FRONTLINE_BATTLE_VIEW_ALIASES import FRONTLINE_BATTLE_VIEW_ALIASES
from gui import GUI_NATIONS_ORDER_INDEX
from gui.filters.carousel_filter import CarouselFilter, FILTER_KEYS
from gui.Scaleform import getButtonsAssetPath
from gui.Scaleform.daapi.view.common.filter_contexts import getFilterSetupContexts
from gui.Scaleform.daapi.view.common.vehicle_carousel.carousel_data_provider import CarouselDataProvider
from gui.Scaleform.locale.RES_ICONS import RES_ICONS
from gui.prb_control.settings import VEHICLE_LEVELS
from gui.shared.gui_items.Vehicle import VEHICLE_TYPES_ORDER_INDICES
from gui.impl.gen import R
from gui.impl import backport
from helpers import dependency
import nations
from skeletons.gui.battle_session import IBattleSessionProvider
from gui.Scaleform.daapi.view.battle.shared.respawn import respawn_utils
from gui.shared.gui_items import ItemsCollection
from skeletons.gui.game_control import IEpicBattleMetaGameController, IVehiclePlaylistsController
from skeletons.gui.shared.gui_items import IGuiItemsFactory
_logger = logging.getLogger(__name__)
_CAROUSEL_FILTERS = (
 FILTER_KEYS.FAVORITE, FILTER_KEYS.PREMIUM)
DEFAULT_VEHICLE_PLAY_LIST = b''

class BattleCarouselFilter(CarouselFilter):
    __epicController = dependency.descriptor(IEpicBattleMetaGameController)
    __vehiclePlaylistsCtrl = dependency.descriptor(IVehiclePlaylistsController)

    def __init__(self):
        super(BattleCarouselFilter, self).__init__()
        self._serverSections = (EPICBATTLE_CAROUSEL_FILTER_1, EPICBATTLE_CAROUSEL_FILTER_2)
        self._clientSections = (EPICBATTLE_CAROUSEL_FILTER_CLIENT_2,)
        return

    def _setCriteriaGroups(self):
        self._criteriesGroups = (FLRentedCriteriaGroup(),)
        return


def getEpicVehicleDataVO(vehicle):
    return {b'vehicleID': (vehicle.intCD), 
       b'vehicleName': (vehicle.shortUserName if vehicle.isPremiumIGR else vehicle.userName), 
       b'flagIcon': (respawn_utils.FLAG_ICON_TEMPLATE % nations.NAMES[vehicle.nationID]), 
       b'vehicleIcon': (vehicle.icon), 
       b'vehicleTypeIcon': ((respawn_utils.VEHICLE_ELITE_TYPE_TEMPLATE if vehicle.isElite else respawn_utils.VEHICLE_TYPE_TEMPLATE) % vehicle.type), 
       b'isElite': (vehicle.isElite), 
       b'isPremium': (vehicle.isPremium), 
       b'vehicleLevelIcon': (RES_ICONS.getLevelIcon(vehicle.level)), 
       b'favorite': (vehicle.isFavorite), 
       b'enabled': True, 
       b'cooldown': b'', 
       b'settings': 0}


class BattleCarouselDataProvider(CarouselDataProvider):
    sessionProvider = dependency.descriptor(IBattleSessionProvider)
    __vehPlaylistsCtrl = dependency.descriptor(IVehiclePlaylistsController)

    def __init__(self, carouselFilter, itemsCache):
        super(BattleCarouselDataProvider, self).__init__(carouselFilter, itemsCache)
        self.__separatorItems = []
        self.__filteredSeparators = []
        self.__availableLevels = []
        self.__indexToScroll = -1
        self.__currentVehicle = None
        self.__vehPlaylistsCtrl.initPlayLists()
        return

    def hasRentedVehicles(self):
        return bool(self._getFilteredVehicles(FL_RENT))

    @property
    def collection(self):
        return self._vehicleItems + self.__separatorItems

    def getCurrentVehiclesCount(self):
        result = super(BattleCarouselDataProvider, self).getCurrentVehiclesCount()
        return result - len(self.__filteredSeparators)

    def setShowStats(self, showVehicleStats):
        self._showVehicleStats = False
        return

    def clear(self):
        super(BattleCarouselDataProvider, self).clear()
        self.__separatorItems = []
        self.__filteredSeparators = []
        self.__availableLevels = []
        self.__indexToScroll = -1
        return

    def getIndexToScroll(self):
        return self.__indexToScroll

    def getAvailableLevels(self):
        return self.__availableLevels

    def applyFilter(self, forceApply=False):
        prevFilteredIndices = self._filteredIndices[:]
        prevSelectedIdx = self._selectedIdx
        self._filteredIndices = []
        self._selectedIdx = -1
        self.__indexToScroll = -1
        isSeparatorsNeeded = self.__isVehicleLevelsFilterNeeded()
        currentVehicleInvID = self.__currentVehicle.invID if self.__currentVehicle is not None else None
        vehLevelsToScroll = self.__getVehLevelsUnlockInBattle()
        visibleVehiclesIntCDs = self.getVisibleVehiclesIntCDs(vehLevelsToScroll)
        sortedVehicleIndices = self._getSortedIndices()
        self.__filteredSeparators = []
        for idx in sortedVehicleIndices:
            vehicle = self._vehicles[idx]
            if vehicle.intCD in visibleVehiclesIntCDs:
                if isSeparatorsNeeded and vehicle.level not in self.__filteredSeparators:
                    separatorIdx = len(self._vehicles) + self.__availableLevels.index(vehicle.level)
                    if vehicle.level in vehLevelsToScroll:
                        self.__indexToScroll = len(self._filteredIndices)
                    self._filteredIndices.append(separatorIdx)
                    self.__filteredSeparators.append(vehicle.level)
                self._filteredIndices.append(idx)
                if currentVehicleInvID == vehicle.invID:
                    self._selectedIdx = len(self._filteredIndices) - 1

        self._filteredIndices += self._getAdditionalItemsIndexes()
        needUpdate = forceApply or bool(not visibleVehiclesIntCDs and self._vehicles) or prevFilteredIndices != self._filteredIndices or prevSelectedIdx != self._selectedIdx
        if needUpdate:
            self._filterByIndices()
        return

    def getVehiclePlayList(self):
        avaliableVehicles = [vehicle.intCD for vehicle in self._vehicles]
        stabPlayListData = {b'lists': [
                    {b'id': b'', 
                       b'label': (backport.text(R.strings.pages.titles.allVehicles())), 
                       b'warning': False, 
                       b'display': b'', 
                       b'total': b''}]}
        selectedList = self.__vehPlaylistsCtrl.getSelectedID()
        for index, (pId, pStrData) in enumerate(self.__vehPlaylistsCtrl.iterPlaylists()):
            playList = self.__vehPlaylistsCtrl.simplePlayListParser(pStrData)
            if playList is not None:
                stabPlayListData[b'lists'].append({b'id': pId, 
                   b'label': (playList.title), 
                   b'warning': (set(playList.list).isdisjoint(avaliableVehicles)), 
                   b'display': (str(sum(1 for item in playList.list if item in avaliableVehicles))), 
                   b'total': (str(len(playList.list)))})
            if selectedList == pId:
                stabPlayListData[b'selectedListIndex'] = index + 1

        return stabPlayListData

    def getVisibleVehiclesIntCDs(self, vehLevelsToScroll):
        filters = self._filter.getFilters()
        switchedLevels = []
        for level in VEHICLE_LEVELS:
            levelStr = b'level_%d' % level
            if filters[levelStr] and level not in vehLevelsToScroll:
                self._filter.switch(levelStr, False)
                switchedLevels.append(levelStr)

        listID = self.__vehPlaylistsCtrl.getSelectedID()
        vehPlayList = self.__vehPlaylistsCtrl.simplePlayListParser(self.__vehPlaylistsCtrl.getPlaylistDataByID(listID)).list if listID else []
        visibleVehiclesIntCDs = []
        for vehicle in self._getCurrentVehicles():
            vehicleIntCD = vehicle.intCD
            if not vehPlayList or vehicleIntCD in vehPlayList:
                visibleVehiclesIntCDs.append(vehicleIntCD)

        for levelStr in switchedLevels:
            self._filter.switch(levelStr, False)

        return visibleVehiclesIntCDs

    def updateVehicleStates(self, slotsStatesData):
        updateIndices = []
        updateVehicles = []
        for data in slotsStatesData:
            for idx, oldVehicle in enumerate(self._vehicles):
                if oldVehicle.intCD == data[b'vehicleID']:
                    curVO = self._vehicleItems[idx]
                    if curVO[b'enabled'] != data[b'enabled'] or curVO[b'cooldown'] != data[b'cooldown']:
                        updateIndices.append(idx)
                        updateVehicles.append(data)
                        self._vehicleItems[idx].update(data)
                    break

        if updateIndices:
            self.flashObject.invalidateItems(updateIndices, updateVehicles)
        return

    def selectVehicle(self, filteredIdx):
        realIdx = self._filteredIndices[filteredIdx]
        vehicle = self._vehicles[realIdx]
        self._selectedIdx = filteredIdx
        self.__currentVehicle = vehicle
        ctrl = self.sessionProvider.dynamic.respawn
        if ctrl is not None:
            ctrl.chooseVehicleForRespawn(vehicle.intCD)
        return self.__currentVehicle.invID

    def getSelectedVehicle(self):
        return self.__currentVehicle

    def selectVehicleByID(self, vehicleID):
        for vehicle in self._vehicles:
            if vehicle.intCD == vehicleID:
                self.__currentVehicle = vehicle
                self._selectedIdx = -1

        self.applyFilter()
        return

    def _buildVehicleItems(self):
        super(BattleCarouselDataProvider, self)._buildVehicleItems()
        self.__calculateCountOfVehicleLevels()
        self.__buildSeparatorItems()
        return

    def _buildVehicle(self, vehicle):
        rawVehicleData = self._itemsCache.getRawVehicleData(vehicle.invID)
        if rawVehicleData:
            vehicle.settings = rawVehicleData.settings
        return getEpicVehicleDataVO(vehicle)

    def _getVehicleStats(self, vehicle):
        return {}

    def _syncRandomStats(self):
        return

    @classmethod
    def _vehicleComparisonKey(cls, vehicle):
        return (
         vehicle.level,
         not vehicle.isFavorite,
         GUI_NATIONS_ORDER_INDEX[vehicle.nationName],
         VEHICLE_TYPES_ORDER_INDICES[vehicle.type],
         vehicle.userName)

    def __isVehicleLevelsFilterNeeded(self):
        return len(self.__availableLevels) > 1

    def __calculateCountOfVehicleLevels(self):
        self.__availableLevels = []
        for vehicle in self._vehicles:
            if vehicle.level not in self.__availableLevels:
                self.__availableLevels.append(vehicle.level)

        self.__availableLevels.sort()
        return

    def __buildSeparatorItems(self):
        self.__separatorItems = []
        if not self.__isVehicleLevelsFilterNeeded():
            return
        for level in self.__availableLevels:
            self.__separatorItems.append({b'levelInfo': {b'level': level, 
                              b'isCollapsed': True, 
                              b'isCollapsible': False, 
                              b'infoText': b''}})

        return

    @staticmethod
    def __getVehLevelsUnlockInBattle():
        arena = getattr(BigWorld.player(), b'arena', None)
        if arena is None:
            _logger.warning(b'Missing arena')
            return []
        else:
            return arena.settings.get(b'epic_config', {}).get(b'unlockableInBattleVehLevels', [])


class VehicleData(object):
    sessionProvider = dependency.descriptor(IBattleSessionProvider)
    itemsFactory = dependency.descriptor(IGuiItemsFactory)

    def __init__(self, carousel):
        self.items = self
        self.__carouselRef = weakref.ref(carousel)
        self.__vehicles = None
        self.__eManager = Event.EventManager()
        self.onSyncCompleted = Event.Event(self.__eManager)
        ctrl = self.sessionProvider.dynamic.respawn
        if ctrl is not None:
            ctrl.onRespawnVehiclesUpdated += self.__updateRespawnVehicles
        return

    def dispose(self):
        ctrl = self.sessionProvider.dynamic.respawn
        if ctrl is not None:
            ctrl.onRespawnVehiclesUpdated -= self.__updateRespawnVehicles
        self.__carouselRef = None
        self.__vehicles = None
        self.__eManager.clear()
        self.__eManager = None
        self.items = None
        return

    def isSynced(self):
        return True

    def getVehicles(self, criteria=None):
        result = ItemsCollection()
        if self.__vehicles:
            for invID, vehicleType in enumerate(self.__vehicles):
                vehicle = self.itemsFactory.createVehicle(typeCompDescr=vehicleType.intCD, inventoryID=invID)
                result[vehicle.intCD] = vehicle

        return result

    def getRawVehicleData(self, invID):
        if invID >= len(self.__vehicles):
            return None
        else:
            return self.__vehicles[invID]

    def __updateRespawnVehicles(self, vehs):
        self.__vehicles = vehs.values()
        carousel = self.__carouselRef()
        if carousel:
            carousel.latePopulate()
        self.onSyncCompleted()
        return


class BattleTankCarousel(BattleTankCarouselMeta):
    _DISABLED_FILTERS = [
     b'bonus']
    sessionProvider = dependency.descriptor(IBattleSessionProvider)
    __vehiclePlaylistsCtrl = dependency.descriptor(IVehiclePlaylistsController)

    def __init__(self):
        super(BattleTankCarousel, self).__init__()
        self._carouselDPCls = BattleCarouselDataProvider
        self._carouselFilterCls = BattleCarouselFilter
        self.__vehicleData = VehicleData(self)
        self.__isUnlockedVehiclesShown = False
        return

    def sortVehicles(self, _):
        self._carouselDP.applyFilter()
        return

    def resetPlaylistAndFilters(self):
        self.__vehiclePlaylistsCtrl.setSelectedID(DEFAULT_VEHICLE_PLAY_LIST)
        self.resetFilters()
        return

    def setFilter(self, idx):
        self.filter.switch(self._usedFilters[idx])
        self.blinkCounter()
        self.applyFilter()
        return

    def updateVehicleStates(self, slotsStatesData):
        self._carouselDP.updateVehicleStates(slotsStatesData)
        return

    def getSelectedVehicle(self):
        if not self._carouselDP:
            return None
        else:
            vehicle = self._carouselDP.getSelectedVehicle()
            if not hasattr(vehicle, b'intCD'):
                return None
            return vehicle

    def getVehiclePlayList(self):
        return self._carouselDP.getVehiclePlayList()

    def selectVehicleByID(self, vehicleID):
        self._carouselDP.selectVehicleByID(vehicleID)
        return

    def latePopulate(self):
        self.updateVehicles(self.__vehicleData.getVehicles())
        self.updateAvailability()
        return

    def getCustomParams(self):
        return {b'vehicleLevelsFilter': (self._carouselDP.getAvailableLevels())}

    def show(self):
        indexToScroll = self._carouselDP.getIndexToScroll()
        if indexToScroll >= 0 and not self.__isUnlockedVehiclesShown:
            self.__isUnlockedVehiclesShown = True
            self.as_scrollToSlotS(indexToScroll)
        return

    def hasRentedVehicles(self):
        return self._carouselDP.hasRentedVehicles()

    def _populate(self):
        super(BattleTankCarousel, self)._populate()
        self.app.loaderManager.onViewLoaded += self.__onViewLoaded
        self.as_useExtendedCarouselS(True)
        self.as_initCarouselFilterS(self._getInitialFilterVO(getFilterSetupContexts(1)))
        return

    def _dispose(self):
        self.app.loaderManager.onViewLoaded -= self.__onViewLoaded
        self.__vehicleData.dispose()
        self.__vehicleData = None
        super(BattleTankCarousel, self)._dispose()
        return

    def _initDataProvider(self):
        self._carouselDPConfig.update({b'carouselFilter': (self._carouselFilterCls()), 
           b'itemsCache': (self.__vehicleData)})
        self._carouselDP = self._carouselDPCls(**self._carouselDPConfig)
        return

    def _getFiltersVisible(self):
        return True

    def _getInitialFilterVO(self, contexts):
        filters = self.filter.getFilters(self._usedFilters)
        filtersVO = {b'mainBtn': {b'value': (getButtonsAssetPath(b'params')), 
                        b'tooltip': b'#tank_carousel_filter:tooltip/params'}, 
           b'hotFilters': [], b'isVisible': (self._getFiltersVisible())}
        for entry in self._usedFilters:
            filtersVO[b'hotFilters'].append(self._makeFilterVO(entry, contexts, filters))

        return filtersVO

    @classmethod
    def _makeFilterVO(cls, filterID, contexts, filters):
        filterVO = super(BattleTankCarousel, cls)._makeFilterVO(filterID, contexts, filters)
        if filterID in cls._DISABLED_FILTERS:
            filterVO[b'enabled'] = False
            filterVO[b'selected'] = False
        return filterVO

    def _getFilters(self):
        return _CAROUSEL_FILTERS

    def __onViewLoaded(self, view, *args):
        if view.settings.alias == FRONTLINE_BATTLE_VIEW_ALIASES.FRONTLINE_CAROUSEL_FILTER_POPOVER:
            view.setTankCarousel(self)
        return
