from __future__ import absolute_import
from gui.Scaleform.framework.managers.loaders import SFViewLoadParams
from gui.shared.gui_items import GUI_ITEM_TYPE
from gui.shared.items_cache import CACHE_SYNC_REASON
from helpers import dependency
from helpers.i18n import makeString as _ms
from account_helpers.AccountSettings import SELECTED_INTRO_VEHICLES_FIELD
from gui.ClientUpdateManager import g_clientUpdateManager
from gui.shared import events
from gui.shared.gui_items.Vehicle import VEHICLE_CLASS_NAME as _VCN
from gui.shared.events import CSVehicleSelectEvent
from gui.shared.event_bus import EVENT_BUS_SCOPE
from gui.shared.formatters import text_styles
from gui.Scaleform.daapi.view.lobby.rally.vo_converters import makeIntroVehicleVO
from gui.Scaleform.daapi.view.meta.CyberSportIntroMeta import CyberSportIntroMeta
from gui.Scaleform.locale.TOOLTIPS import TOOLTIPS
from gui.Scaleform.locale.CYBERSPORT import CYBERSPORT
from gui.Scaleform.genConsts.CYBER_SPORT_ALIASES import CYBER_SPORT_ALIASES
from nation_change.nation_change_helpers import iterVehTypeCDsInNationGroup
from nation_change_helpers.client_nation_change_helper import getValidVehicleCDForNationChange
from skeletons.gui.shared import IItemsCache
_ACCEPTED_VEH_TYPES = (
 _VCN.LIGHT_TANK, _VCN.MEDIUM_TANK, _VCN.HEAVY_TANK)

class _IntroViewVO(object):

    def __init__(self):
        self.__data = {b'teamDescriptionText': b'', 
           b'isTeamDescriptionTooltip': False, 
           b'teamDescriptionTooltip': b'', 
           b'createBtnLabel': b'', 
           b'createBtnTooltip': b'', 
           b'isCreateBtnEnabled': False, 
           b'isCreateBtnVisible': False, 
           b'isCanCreateBattle': False, 
           b'isCanJoinBattle': False, 
           b'isNeedAddPlayers': False, 
           b'isHaveTeamToShow': False}
        return

    def getData(self):
        return self.__data

    def showCreateButton(self, label, tooltip, enabled=True):
        self.__data[b'isCreateBtnVisible'] = True
        self.__data[b'isCreateBtnEnabled'] = enabled
        self.__data[b'createBtnLabel'] = label
        self.__data[b'createBtnTooltip'] = tooltip
        return

    def moveToTheUnitByCreateButton(self):
        self.__data[b'isCanCreateBattle'] = self.__data[b'isCanJoinBattle'] = True
        return

    def needAddPlayers(self):
        self.__data[b'isNeedAddPlayers'] = True
        return

    def fillDefault(self):
        self.showCreateButton(_ms(CYBERSPORT.INTROVIEW_RIGHTBLOCK_BTNLABEL), b'', enabled=True)
        return


class CyberSportIntroView(CyberSportIntroMeta):
    itemsCache = dependency.descriptor(IItemsCache)

    def showSelectorPopup(self):
        rosterSettings = self.prbEntity.getRosterSettings()
        self._currentVehCD = -1
        self.fireEvent(events.LoadViewEvent(SFViewLoadParams(CYBER_SPORT_ALIASES.VEHICLE_SELECTOR_POPUP_PY), ctx={b'isMultiSelect': False, 
           b'infoText': (CYBERSPORT.WINDOW_VEHICLESELECTOR_INFO_INTRO), 
           b'titleText': (CYBERSPORT.WINDOW_VEHICLESELECTOR_TITLE), 
           b'selectButton': (CYBERSPORT.WINDOW_VEHICLESELECTOR_BUTTONS_SELECT), 
           b'cancelButton': (CYBERSPORT.WINDOW_VEHICLESELECTOR_BUTTONS_CANCEL), 
           b'compatibleOnlyLabel': (CYBERSPORT.WINDOW_VEHICLESELECTOR_FILTERS_MATCHES), 
           b'componentsOffset': 45, 
           b'selectedVehicles': (self.__getSelectedVehicles()), 
           b'section': b'cs_intro_view_vehicle', 
           b'levelsRange': (rosterSettings.getLevelsRange()), 
           b'vehicleTypes': _ACCEPTED_VEH_TYPES}), scope=EVENT_BUS_SCOPE.LOBBY)
        return

    def _populate(self):
        super(CyberSportIntroView, self)._populate()
        self.addListener(CSVehicleSelectEvent.VEHICLE_SELECTED, self.__updateSelectedVehicles)
        self.itemsCache.onSyncCompleted += self.__onCacheResync
        data = {b'titleLblText': (text_styles.promoTitle(CYBERSPORT.WINDOW_INTRO_TITLE)), 
           b'descrLblText': (text_styles.main(CYBERSPORT.WINDOW_INTRO_DESCRIPTION)), 
           b'listRoomTitleLblText': (text_styles.promoSubTitle(CYBERSPORT.WINDOW_INTRO_SEARCH_TITLE)), 
           b'listRoomDescrLblText': (text_styles.main(CYBERSPORT.WINDOW_INTRO_SEARCH_DESCRIPTION)), 
           b'listRoomBtnLabel': (_ms(CYBERSPORT.WINDOW_INTRO_SEARCH_BTN)), 
           b'autoTitleLblText': (text_styles.middleTitle(CYBERSPORT.WINDOW_INTRO_AUTO_TITLE)), 
           b'autoDescrLblText': (text_styles.main(CYBERSPORT.WINDOW_INTRO_AUTO_DESCRIPTION)), 
           b'vehicleBtnTitleTfText': (text_styles.standard(CYBERSPORT.BUTTON_CHOOSEVEHICLES_SELECTED)), 
           b'rightBlockHeader': (text_styles.promoSubTitle(CYBERSPORT.INTROVIEW_RIGHTBLOCK_HEADER)), 
           b'rightBlockDescr': (text_styles.main(CYBERSPORT.INTROVIEW_RIGHTBLOCK_DESCR)), 
           b'rightBlockBtnLbl': (_ms(CYBERSPORT.INTROVIEW_RIGHTBLOCK_BTNLABEL))}
        self.as_setTextsS(data)
        self.__checkSelectedVehicles()
        self.__updateAutoSearchVehicle(self.__getSelectedVehicles())
        return

    def _dispose(self):
        self.removeListener(CSVehicleSelectEvent.VEHICLE_SELECTED, self.__updateSelectedVehicles)
        self.itemsCache.onSyncCompleted -= self.__onCacheResync
        g_clientUpdateManager.removeObjectCallbacks(self)
        super(CyberSportIntroView, self)._dispose()
        return

    def __checkSelectedVehicles(self):
        vehsIntCD = self.__getSelectedVehicles()
        if vehsIntCD:
            vehIntCD = vehsIntCD[0]
            vehicle = self.itemsCache.items.getItemByCD(vehIntCD)
            if not vehicle.activeInNationGroup:
                vehIntCD = getValidVehicleCDForNationChange(vehIntCD)
                self.prbEntity.setSelectedVehicles(SELECTED_INTRO_VEHICLES_FIELD, [vehIntCD])
        return

    def __onCacheResync(self, reason, diff):
        if reason != CACHE_SYNC_REASON.CLIENT_UPDATE:
            return
        else:
            if diff is not None and GUI_ITEM_TYPE.VEHICLE in diff:
                vehDiff = diff[GUI_ITEM_TYPE.VEHICLE]
                for vehIntCD in vehDiff:
                    vehicle = self.itemsCache.items.getItemByCD(vehIntCD)
                    if not vehicle.activeInNationGroup and self._currentVehCD == vehIntCD:
                        itemCD = next(iterVehTypeCDsInNationGroup(vehicle.intCD))
                        self.__setSelectedVehicle(itemCD)

            return

    def __updateSelectedVehicles(self, event):
        if event.ctx:
            vehIntCD = int(event.ctx[0])
            self.__setSelectedVehicle(vehIntCD)
        return

    def __setSelectedVehicle(self, vehIntCD):
        self.prbEntity.setSelectedVehicles(SELECTED_INTRO_VEHICLES_FIELD, [vehIntCD])
        self.__updateAutoSearchVehicle([vehIntCD])
        return

    def __updateAutoSearchVehicle(self, vehsIntCD):
        if vehsIntCD:
            vehIntCD = vehsIntCD[0]
            vehicle = self.itemsCache.items.getItemByCD(vehIntCD)
            levelsRange = self.prbEntity.getRosterSettings().getLevelsRange()
            if vehicle.level not in levelsRange:
                isReadyVehicle = False
                warnTooltip = TOOLTIPS.CYBERSPORT_INTRO_SELECTEDVEHICLEWARN_INCOMPATIBLELEVEL
            elif vehicle.type not in _ACCEPTED_VEH_TYPES:
                isReadyVehicle = False
                warnTooltip = TOOLTIPS.CYBERSPORT_INTRO_SELECTEDVEHICLEWARN_INCOMPATIBLETYPE
            elif vehicle.isOnlyForEpicBattles:
                isReadyVehicle = False
                warnTooltip = TOOLTIPS.CYBERSPORT_UNIT_FIGHTBTN_EVENTVEHICLEWRONGMODE
            else:
                warnTooltip, isReadyVehicle = b'', vehicle.isReadyToPrebattle()
            self._currentVehCD = vehIntCD
            self.as_setSelectedVehicleS(makeIntroVehicleVO(vehicle, isReadyVehicle, warnTooltip))
        else:
            self.as_setNoVehiclesS(TOOLTIPS.CYBERSPORT_NOVEHICLESINHANGAR)
        return

    def __getSelectedVehicles(self):
        return self.prbEntity.getSelectedVehicles(SELECTED_INTRO_VEHICLES_FIELD)
