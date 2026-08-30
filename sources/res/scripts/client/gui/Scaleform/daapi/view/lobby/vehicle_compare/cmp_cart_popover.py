from __future__ import absolute_import
from debug_utils import LOG_ERROR
from gui.Scaleform import getNationsFilterAssetPath
from gui.Scaleform.daapi.view.lobby.vehicle_compare.formatters import packHeaderColumnData
from gui.Scaleform.daapi.view.meta.VehicleCompareCartPopoverMeta import VehicleCompareCartPopoverMeta
from gui.Scaleform.framework.entities.DAAPIDataProvider import SortableDAAPIDataProvider
from gui.Scaleform.locale.RES_ICONS import RES_ICONS
from gui.Scaleform.locale.VEH_COMPARE import VEH_COMPARE
from gui.prb_control.dispatcher import g_prbLoader
from gui.shared.event_dispatcher import showVehicleCompare
from gui.shared.formatters import text_styles
from gui.shared.gui_items.Vehicle import getTypeSmallIconPath
from helpers import dependency
from helpers.i18n import makeString as _ms
from nations import AVAILABLE_NAMES
from skeletons.gui.game_control import IVehicleComparisonBasket
from skeletons.gui.lobby_context import ILobbyContext
from skeletons.gui.shared import IItemsCache

class VehicleCompareCartPopover(VehicleCompareCartPopoverMeta):
    comparisonBasket = dependency.descriptor(IVehicleComparisonBasket)
    lobbyContext = dependency.descriptor(ILobbyContext)

    def remove(self, vehId):
        self.comparisonBasket.removeVehicleByIdx(int(vehId))
        return

    def removeAll(self):
        self.comparisonBasket.removeAllVehicles()
        return

    def onWindowClose(self):
        self.destroy()
        return

    def gotoCompareView(self):
        showVehicleCompare()
        self.destroy()
        return

    def _populate(self):
        super(VehicleCompareCartPopover, self)._populate()
        self._cartDP = _VehicleCompareCartDataProvider()
        self._cartDP.setFlashObject(self.as_getDPS())
        self._cartDP.rebuildList(self.comparisonBasket.getVehiclesCDs())
        self.comparisonBasket.onChange += self.__onBasketChange
        self.comparisonBasket.onSwitchChange += self.__onVehCmpBasketStateChanged
        self.lobbyContext.getServerSettings().onServerSettingsChange += self.__onServerSettingChanged
        self.__initControls()
        return

    def _dispose(self):
        super(VehicleCompareCartPopover, self)._dispose()
        self.comparisonBasket.onChange -= self.__onBasketChange
        self.comparisonBasket.onSwitchChange -= self.__onVehCmpBasketStateChanged
        self.lobbyContext.getServerSettings().onServerSettingsChange -= self.__onServerSettingChanged
        self._cartDP.fini()
        self._cartDP = None
        return

    def __onVehCmpBasketStateChanged(self):
        if not self.comparisonBasket.isEnabled():
            self.onWindowClose()
        else:
            self.__updateButtonsState()
        return

    def __initControls(self):
        headers = [
         packHeaderColumnData(b'nationId', 49, 30, tooltip=VEH_COMPARE.CARTPOPOVER_SORTING_NATION, icon=RES_ICONS.MAPS_ICONS_FILTERS_NATIONS_ALL),
         packHeaderColumnData(b'typeIndex', 45, 30, tooltip=VEH_COMPARE.CARTPOPOVER_SORTING_VEHTYPE, icon=RES_ICONS.MAPS_ICONS_FILTERS_TANKS_ALL),
         packHeaderColumnData(b'level', 45, 30, tooltip=VEH_COMPARE.CARTPOPOVER_SORTING_VEHLVL, icon=RES_ICONS.MAPS_ICONS_BUTTONS_TAB_SORT_BUTTON_LEVEL),
         packHeaderColumnData(b'shortUserName', 140, 30, label=VEH_COMPARE.CARTPOPOVER_SORTING_VEHNAME, tooltip=VEH_COMPARE.CARTPOPOVER_SORTING_VEHNAME_TOOLTIP),
         packHeaderColumnData(b'actions', 1, 30)]
        self.as_setInitDataS({b'title': (text_styles.highTitle(_ms(VEH_COMPARE.CARTPOPOVER_TITLE))), 
           b'tableHeaders': headers})
        self.__updateButtonsState()
        return

    def __onBasketChange(self, _):
        self.__updateButtonsState()
        return

    def __updateButtonsState(self):
        count = self.comparisonBasket.getVehiclesCount()
        buttonsEnabled = count > 0
        if self.comparisonBasket.isFull():
            addBtnTT = VEH_COMPARE.CARTPOPOVER_FULLBASKETCMPBTN_TOOLTIP
            addBtnIcon = RES_ICONS.MAPS_ICONS_LIBRARY_ALERTICON
        else:
            addBtnTT = VEH_COMPARE.CARTPOPOVER_OPENCMPBTN_TOOLTIP
            addBtnIcon = None
        isNavigationEnabled = not g_prbLoader.getDispatcher().getFunctionalState().isNavigationDisabled()
        self.as_updateToCmpBtnPropsS({b'btnLabel': (_ms(VEH_COMPARE.CARTPOPOVER_GOTOCOMPAREBTN_LABEL, value=count)), 
           b'btnTooltip': addBtnTT, 
           b'btnEnabled': (buttonsEnabled and isNavigationEnabled), 
           b'btnIcon': addBtnIcon})
        isBasketLocked = self.comparisonBasket.isLocked
        self.as_updateClearBtnPropsS({b'btnLabel': (VEH_COMPARE.CARTPOPOVER_REMOVEALLBTN_LABEL), 
           b'btnTooltip': (VEH_COMPARE.CARTPOPOVER_REMOVEBTNLOCKED_TOOLTIP if isBasketLocked else VEH_COMPARE.CARTPOPOVER_REMOVEALLBTN_TOOLTIP), 
           b'btnEnabled': (buttonsEnabled and not isBasketLocked)})
        return

    def __onServerSettingChanged(self, diff):
        if b'sessionStats' in diff or (b'sessionStats', b'_r') in diff:
            isSessionStatsEnabled = diff[b'sessionStats'].get(b'isSessionStatsEnabled')
            if isSessionStatsEnabled is not None:
                self.destroy()
        return


class _VehicleCompareCartDataProvider(SortableDAAPIDataProvider):
    itemsCache = dependency.descriptor(IItemsCache)
    comparisonBasket = dependency.descriptor(IVehicleComparisonBasket)

    def __init__(self):
        super(_VehicleCompareCartDataProvider, self).__init__()
        self._list = []
        self._listMapping = {}
        self.__mapping = {}
        self.__selectedID = None
        return

    @property
    def collection(self):
        return self._list

    def emptyItem(self):
        return

    def clear(self):
        self._list = []
        self._listMapping.clear()
        self.__mapping.clear()
        self.__selectedID = None
        return

    def fini(self):
        self.comparisonBasket.onChange -= self.__basketChanged
        self.comparisonBasket.onSwitchChange -= self.__basketChanged
        self.clear()
        self.destroy()
        return

    def getSelectedIdx(self):
        if self.__selectedID in self.__mapping:
            return self.__mapping[self.__selectedID]
        return -1

    def setSelectedID(self, selId):
        self.__selectedID = selId
        return

    def setFlashObject(self, movieClip, autoPopulate=True, setScript=True):
        self.comparisonBasket.onChange += self.__basketChanged
        self.comparisonBasket.onSwitchChange += self.__basketChanged
        return super(_VehicleCompareCartDataProvider, self).setFlashObject(movieClip, autoPopulate, setScript)

    def getVO(self, index):
        vo = None
        if index > -1:
            try:
                vo = self.sortedCollection[index]
            except IndexError:
                LOG_ERROR(b'Item not found', index)

        return vo

    def buildList(self, changedVehsCDs):
        self.clear()
        for idx, vehCD in enumerate(changedVehsCDs):
            self._list.append(self._makeVO(vehCD, idx))

        return

    def rebuildList(self, cache):
        self.buildList(cache)
        self.refresh()
        return

    def pyGetSelectedIdx(self):
        return self.getSelectedIdx()

    def refreshRandomItems(self, indexes, items):
        self.flashObject.invalidateItems(indexes, items)
        return

    def refreshSingleItem(self, index, item):
        self.flashObject.invalidateItem(index, item)
        return

    def _makeVO(self, vehicleCD, index):
        vehicle = self.itemsCache.items.getItemByCD(vehicleCD)
        complectation = _ms(VEH_COMPARE.cartpopover_configurationtype(self.comparisonBasket.getVehicleAt(index).getConfigurationType()))
        basketLocked = self.comparisonBasket.isLocked
        return {b'id': vehicleCD, 
           b'index': index, 
           b'vehicleName': (text_styles.main(vehicle.shortUserName)), 
           b'complectation': complectation, 
           b'nation': (getNationsFilterAssetPath(AVAILABLE_NAMES[vehicle.nationID])), 
           b'level': (vehicle.level), 
           b'typeStr': (getTypeSmallIconPath(vehicle.type, vehicle.isPremium)), 
           b'smallIconPath': (vehicle.iconSmall), 
           b'removeBtnTooltip': (VEH_COMPARE.CARTPOPOVER_REMOVELOCKEDBTN_TOOLTIP if basketLocked else VEH_COMPARE.CARTPOPOVER_REMOVEBTN_TOOLTIP), 
           b'removeBtnEnabled': (not basketLocked)}

    def __basketChanged(self, *args):
        self.rebuildList(self.comparisonBasket.getVehiclesCDs())
        return
