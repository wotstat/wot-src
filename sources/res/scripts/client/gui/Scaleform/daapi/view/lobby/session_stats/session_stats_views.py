from __future__ import absolute_import
from future.utils import viewitems
from account_helpers.settings_core.settings_constants import SESSION_STATS
from constants import ARENA_BONUS_TYPE
from gui.Scaleform.daapi.view.lobby.session_stats.shared import packLastBattleData, packBattleEfficiencyData, packTotalData, toIntegral, toNiceNumber, getDeltaAsData, getNationIcon
from gui.Scaleform.daapi.view.meta.SessionBattleStatsViewMeta import SessionBattleStatsViewMeta
from gui.Scaleform.daapi.view.meta.SessionVehicleStatsViewMeta import SessionVehicleStatsViewMeta
from gui.impl import backport
from gui.impl.gen import R
from gui.shared.formatters import text_styles
from gui.shared.utils.requesters import REQ_CRITERIA
from helpers import dependency
from skeletons.gui.shared import IItemsCache
_VEH_LIST_LEN = 12

class SessionBattleStatsView(SessionBattleStatsViewMeta):
    itemsCache = dependency.descriptor(IItemsCache)

    def updateData(self):
        self.as_setDataS(self.__makeVO())
        return

    def _populate(self):
        super(SessionBattleStatsView, self)._populate()
        self.as_setDataS(self.__makeVO())
        self.itemsCache.onSyncCompleted += self.__updateViewHandler
        return

    def _dispose(self):
        self.itemsCache.onSyncCompleted -= self.__updateViewHandler
        return

    def __updateViewHandler(self, *_):
        self.as_setDataS(self.__makeVO())
        return

    def __makeVO(self):
        data = self.itemsCache.items.sessionStats.getAccountStats(ARENA_BONUS_TYPE.REGULAR)
        parameters = SESSION_STATS.getAccountEfficiencyBlock()
        return {b'collapseLabel': (text_styles.middleTitle(backport.text(R.strings.session_stats.label.battleEfficiency()))), 
           b'lastBattle': (packLastBattleData(data)), 
           b'total': (packTotalData(data)), 
           b'battleEfficiency': (packBattleEfficiencyData(data, parameters))}


class SessionVehicleStatsView(SessionVehicleStatsViewMeta):
    itemsCache = dependency.descriptor(IItemsCache)

    def updateData(self):
        self.as_setDataS(self.__makeVO)
        return

    def _populate(self):
        super(SessionVehicleStatsView, self)._populate()
        self.itemsCache.items.sessionStats.getVehiclesStats(ARENA_BONUS_TYPE.REGULAR, 0)
        self.as_setDataS(self.__makeVO)
        self.itemsCache.onSyncCompleted += self.__updateViewHandler
        return

    def _dispose(self):
        self.itemsCache.onSyncCompleted -= self.__updateViewHandler
        return

    @property
    def __makeVO(self):
        vehIdList = self.itemsCache.items.sessionStats.getStatsVehList(ARENA_BONUS_TYPE.REGULAR)
        vehiclesDict = self.itemsCache.items.getVehicles(REQ_CRITERIA.IN_CD_LIST(vehIdList))
        vehiclesData = []
        vehiclesSortData = []
        if vehiclesDict:
            for intCD, vehicle in viewitems(vehiclesDict):
                data = self.itemsCache.items.sessionStats.getVehiclesStats(ARENA_BONUS_TYPE.REGULAR, intCD)
                vehiclesSortData.append((
                 intCD, (data.battleCnt, vehicle.level, data.averageDamage.value)))
                vehiclesData.append({b'intCD': intCD, 
                   b'icon': (vehicle.iconSmall), 
                   b'label': (text_styles.main(vehicle.shortUserName)), 
                   b'level': (vehicle.level), 
                   b'nationIcon': (getNationIcon(vehicle.nationID, width=155, height=31)), 
                   b'type': (vehicle.type), 
                   b'total': (text_styles.stats(toNiceNumber(data.battleCnt))), 
                   b'damage': (text_styles.stats(toIntegral(data.averageDamage.value))), 
                   b'wtr': (text_styles.stats(toNiceNumber(data.wtr.value))), 
                   b'delta': (getDeltaAsData(data.wtr.delta))})

        else:
            vehiclesData.append({b'intCD': None, 
               b'icon': (backport.image(R.images.gui.maps.icons.library.empty_veh())), 
               b'total': (text_styles.stats(toNiceNumber(None))), 
               b'damage': (text_styles.stats(toIntegral(None))), 
               b'wtr': (text_styles.stats(toNiceNumber(None)))})
        if vehiclesSortData:
            vehiclesData = self._sortedVehiclesData(vehiclesSortData, vehiclesData)
        vehiclesData = vehiclesData[0:_VEH_LIST_LEN]
        return {b'headerName': (text_styles.mainBig(backport.text(R.strings.menu.inventory.menu.vehicle.name()))), 
           b'headerTotalIcon': (backport.image(R.images.gui.maps.icons.statistic.battles24())), 
           b'headerTotalTooltip': (backport.text(R.strings.session_stats.tooltip.header.battleCount())), 
           b'headerDamageIcon': (backport.image(R.images.gui.maps.icons.statistic.avgDamage24())), 
           b'headerDamageTooltip': (backport.text(R.strings.session_stats.tooltip.header.avgDamage())), 
           b'headerWtrIcon': (backport.image(R.images.gui.maps.icons.library.wtrIcon_24())), 
           b'headerWtrTooltip': (backport.text(R.strings.session_stats.tooltip.header.wtr())), 
           b'vehicles': vehiclesData}

    def _sortedVehiclesData(self, vehiclesSortData, vehiclesData):
        sortedParams = sorted(vehiclesSortData, key=(lambda params: params[1]), reverse=True)
        vehIds = [sortedParam[0] for sortedParam in sortedParams]
        return sorted(vehiclesData, key=(lambda k: vehIds.index(k[b'intCD'])))

    def __updateViewHandler(self, *_):
        self.as_setDataS(self.__makeVO)
        return
