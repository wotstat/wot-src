from gui.Scaleform.daapi.view.lobby.event_boards.event_boards_vos import makeFiltersVO, makeVehicleVO
from gui.Scaleform.daapi.view.lobby.event_boards.event_helpers import LEVELS_RANGE
from gui.Scaleform.daapi.view.meta.EventBoardsVehiclesOverlayMeta import EventBoardsVehiclesOverlayMeta
from gui.Scaleform.locale.EVENT_BOARDS import EVENT_BOARDS
from gui.event_boards.event_boards_items import EVENT_TYPE
from gui.shared.formatters.vehicle_filters import packVehicleTypesFilter, packVehicleLevelsFilter, packNationsFilter
from gui.shared.utils.requesters import REQ_CRITERIA
from helpers import int2roman, dependency
from helpers.i18n import makeString as _ms
from skeletons.gui.shared import IItemsCache

class EventBoardsVehiclesOverlay(EventBoardsVehiclesOverlayMeta):
    itemsCache = dependency.descriptor(IItemsCache)
    __lid = None
    __opener = None
    __filters = {b'nation': (-1), 
       b'vehicleType': b'none', 
       b'isMain': False, 
       b'level': (-1), 
       b'compatibleOnly': False}

    def setOpener(self, view):
        self.__opener = view
        eventData = self.__opener.eventData
        if eventData.getType() == EVENT_TYPE.VEHICLE:
            filtersVO = self.__filters.copy()
            filtersVO[b'vehicleTypesDP'] = packVehicleTypesFilter(defaultVehType=b'none')
            filtersVO[b'levelsDP'] = packVehicleLevelsFilter(LEVELS_RANGE)
            filtersVO[b'nationDP'] = packNationsFilter()
            self.as_setFiltersS(filtersVO)
            self.applyFilters(**self.__filters)
        else:
            leaderboards = eventData.getLeaderboards()
            leaderboardID = leaderboards[0][0]
            header = {b'filters': (makeFiltersVO(eventData.getType(), leaderboards, leaderboardID, category=b'vehicles'))}
            self.as_setHeaderS(header)
            self.changeFilter(leaderboardID)
        return

    def changeFilter(self, lid):
        self.__lid = int(lid)
        self._setData()
        return

    def applyFilters(self, nation, vehicleType, level, isMain, compatibleOnly):
        self.__filters = {b'nation': nation, 
           b'vehicleType': vehicleType, 
           b'isMain': isMain, 
           b'level': level, 
           b'compatibleOnly': compatibleOnly}
        self._setData()
        return

    def _setData(self):
        eventData = self.__opener.eventData
        eventType = eventData.getType()
        criteria = REQ_CRITERIA.EMPTY
        if eventType == EVENT_TYPE.VEHICLE:
            vehicleIds = [veh for _, veh in eventData.getLeaderboards()]
            title = _ms(EVENT_BOARDS.VEHICLES_VEHICLE)
            bgPath = None
            if self.__filters[b'nation'] != -1:
                criteria |= REQ_CRITERIA.NATIONS([self.__filters[b'nation']])
            if self.__filters[b'vehicleType'] != b'none':
                criteria |= REQ_CRITERIA.VEHICLE.CLASSES([self.__filters[b'vehicleType']])
            if self.__filters[b'isMain']:
                criteria |= REQ_CRITERIA.VEHICLE.FAVORITE
            if self.__filters[b'level'] != -1:
                criteria |= REQ_CRITERIA.VEHICLE.LEVELS([self.__filters[b'level']])
        else:
            vehicleIds = eventData.getLimits().getVehicles(self.__lid)
            leaderboard = eventData.getLeaderboard(self.__lid)
            if eventType == EVENT_TYPE.NATION:
                title = _ms((b'#menu:nation_tree/title/{}').format(leaderboard))
                bgPath = (b'../maps/icons/eventBoards/flagsOverlay/{}.png').format(leaderboard)
            elif eventType == EVENT_TYPE.LEVEL:
                title = _ms(EVENT_BOARDS.VEHICLES_LEVEL, level=int2roman(leaderboard))
                bgPath = None
            elif eventType == EVENT_TYPE.CLASS:
                title = _ms((b'#quests:classes/{}').format(leaderboard))
                bgPath = None
            else:
                title = None
                bgPath = None
        allVehicles = self.itemsCache.items.getVehicles(REQ_CRITERIA.IN_CD_LIST(vehicleIds))
        vehicles = allVehicles.filter(criteria).values()
        vehicles.sort(key=(lambda v: v.isInInventory), reverse=True)
        vehiclesVO = [makeVehicleVO(vehicle) for vehicle in vehicles]
        data = {b'title': title, 
           b'bgPath': bgPath, 
           b'vehicles': vehiclesVO}
        self.as_setVehiclesS(data)
        return
