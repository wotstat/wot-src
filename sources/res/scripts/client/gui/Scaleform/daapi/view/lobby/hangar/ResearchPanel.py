from __future__ import absolute_import
import typing
from CurrentVehicle import g_currentVehicle
from gui.Scaleform.genConsts.RESEARCH_COUNTER_STATES import RESEARCH_COUNTER_STATES
from gui.veh_post_progression.helpers import needToShowCounter
from items.battle_royale import isBattleRoyale
from constants import IGR_TYPE
from debug_utils import LOG_ERROR
from gui import makeHtmlString
from gui.ClientUpdateManager import g_clientUpdateManager
from gui.Scaleform.daapi.view.lobby.vehicle_compare.formatters import resolveStateTooltip
from gui.Scaleform.daapi.view.meta.ResearchPanelMeta import ResearchPanelMeta
from gui.Scaleform.locale.MENU import MENU
from gui.Scaleform.locale.VEH_COMPARE import VEH_COMPARE
from gui.shared import event_dispatcher as shared_events
from gui.shared.formatters import text_styles
from gui.shared.formatters.time_formatters import getTimeLeftStr
from gui.shared.tutorial_helper import getTutorialGlobalStorage
from gui.shared.utils.module_upd_available_helper import getResearchInfo
from gui.veh_post_progression.models.ext_money import ExtendedMoney
from helpers import i18n, dependency
from nation_change.nation_change_helpers import iterVehiclesWithNationGroupInOrder
from skeletons.gui.game_control import IVehicleComparisonBasket, IIGRController
from skeletons.gui.shared import IItemsCache
from tutorial.control.context import GLOBAL_FLAG
if typing.TYPE_CHECKING:
    from gui.shared.gui_items.Vehicle import Vehicle

class ResearchPanel(ResearchPanelMeta):
    itemsCache = dependency.descriptor(IItemsCache)
    comparisonBasket = dependency.descriptor(IVehicleComparisonBasket)
    igrCtrl = dependency.descriptor(IIGRController)

    def __init__(self):
        super(ResearchPanel, self).__init__()
        self.__isNavigationEnabled = True
        return

    def _populate(self):
        super(ResearchPanel, self)._populate()
        g_clientUpdateManager.addCallbacks({b'stats.vehTypeXP': (self.onVehicleTypeXPChanged), 
           b'stats.eliteVehicles': (self.onVehicleBecomeElite), 
           b'blueprints': (self.__onUpdateBlueprints), 
           b'serverSettings.blueprints_config': (self.__onBlueprintsSettingsChanged)})
        self.onCurrentVehicleChanged()
        self.comparisonBasket.onChange += self.__onCompareBasketChanged
        self.comparisonBasket.onSwitchChange += self.onCurrentVehicleChanged
        return

    def __onBlueprintsSettingsChanged(self, diff):
        self.__onUpdateBlueprints(diff)
        return

    def __onUpdateBlueprints(self, _):
        self.__updateModuleUpdateAvailable()
        return

    def _dispose(self):
        super(ResearchPanel, self)._dispose()
        g_clientUpdateManager.removeObjectCallbacks(self)
        self.comparisonBasket.onChange -= self.__onCompareBasketChanged
        self.comparisonBasket.onSwitchChange -= self.onCurrentVehicleChanged
        return

    def setNavigationEnabled(self, isEnabled):
        if self.__isNavigationEnabled != isEnabled:
            self.as_setNavigationEnabledS(isEnabled)
            self.__isNavigationEnabled = isEnabled
        return

    def goToResearch(self):
        if g_currentVehicle.isPresent() and self.__isNavigationEnabled:
            shared_events.showResearchView(g_currentVehicle.item.intCD)
        else:
            LOG_ERROR(b'Current vehicle is not preset or navigation is disabled')
        return

    def goToPostProgression(self):
        shared_events.showVehPostProgressionView(g_currentVehicle.item.intCD)
        return

    def addVehToCompare(self):
        if g_currentVehicle.isPresent() and not isBattleRoyale(g_currentVehicle.item.tags):
            vehCD = g_currentVehicle.item.intCD
            self.comparisonBasket.addVehicle(vehCD)
        return

    def onCurrentVehicleChanged(self):
        if g_currentVehicle.isPresent():
            xps = self.itemsCache.items.stats.vehiclesXPs
            vehicle = g_currentVehicle.item
            xp = xps.get(vehicle.intCD, 0)
            self.as_updateCurrentVehicleS({b'earnedXP': xp, 
               b'isElite': (vehicle.isElite), 
               b'vehCompareData': (self.__getVehCompareData(vehicle)), 
               b'vehPostProgressionData': (self.__getVehPostProgressionData(vehicle)), 
               b'intCD': (vehicle.intCD)})
        else:
            self.as_updateCurrentVehicleS({b'earnedXP': 0})
        self.__onIgrTypeChanged()
        self.__updateModuleUpdateAvailable()
        return

    def __onIgrTypeChanged(self, *args):
        igrType = self.igrCtrl.getRoomType()
        icon = makeHtmlString(b'html_templates:igr/iconBig', b'premium' if igrType == IGR_TYPE.PREMIUM else b'basic', {})
        label = text_styles.main(i18n.makeString(MENU.IGR_INFO, igrIcon=icon))
        self.as_setIGRLabelS(igrType != IGR_TYPE.NONE, label)
        self.__updateVehIGRStatus()
        return

    def __updateVehIGRStatus(self):
        vehicleIgrTimeLeft = None
        igrType = self.igrCtrl.getRoomType()
        if g_currentVehicle.isPresent() and g_currentVehicle.isPremiumIGR() and igrType == IGR_TYPE.PREMIUM:
            igrActionIcon = makeHtmlString(b'html_templates:igr/iconSmall', b'premium', {})
            localization = b'#menu:vehicleIgr/%s'
            rentInfo = g_currentVehicle.item.rentInfo
            vehicleIgrTimeLeft = getTimeLeftStr(localization, rentInfo.getTimeLeft(), timeStyle=text_styles.stats, ctx={b'igrIcon': igrActionIcon})
        self.as_actionIGRDaysLeftS(vehicleIgrTimeLeft is not None, text_styles.main(vehicleIgrTimeLeft))
        return

    def __updateModuleUpdateAvailable(self):
        status = RESEARCH_COUNTER_STATES.RESEARCH_NOT_AVAILABLE
        if g_currentVehicle.isPresent():
            researchInfo = getResearchInfo(vehicle=g_currentVehicle.item)
            if researchInfo and researchInfo.hasUnviewedItems():
                if researchInfo.hasUnviewedVehicles():
                    status = RESEARCH_COUNTER_STATES.RESEARCH_VEHICLE_AVAILABLE
                else:
                    status = RESEARCH_COUNTER_STATES.RESEARCH_MODULE_AVAILABLE
        self.as_setModuleUpdateAvailableS(status)
        return

    def onVehicleTypeXPChanged(self, xps):
        if g_currentVehicle.isPresent():
            vehCD = g_currentVehicle.item.intCD
            nationGroupVehCDs = set(iterVehiclesWithNationGroupInOrder([vehCD]))
            if nationGroupVehCDs.intersection(xps):
                xp = self.itemsCache.items.stats.vehiclesXPs.get(vehCD, 0)
                self.as_setEarnedXPS(xp)
                self.onCurrentVehicleChanged()
        return

    def onVehicleBecomeElite(self, elite):
        if g_currentVehicle.isPresent():
            vehCD = g_currentVehicle.item.intCD
            if vehCD in elite:
                self.as_setEliteS(True)
        return

    def __onCompareBasketChanged(self, changedData):
        if changedData.isFullChanged:
            self.onCurrentVehicleChanged()
        return

    def __getVehCompareData(self, vehicle):
        state, tooltip = resolveStateTooltip(self.comparisonBasket, vehicle, enabledTooltip=VEH_COMPARE.VEHPREVIEW_COMPAREVEHICLEBTN_TOOLTIPS_ADDTOCOMPARE, fullTooltip=VEH_COMPARE.VEHPREVIEW_COMPAREVEHICLEBTN_TOOLTIPS_DISABLED)
        return {b'modeAvailable': (self.comparisonBasket.isEnabled()), 
           b'btnEnabled': state, 
           b'btnTooltip': tooltip}

    def __getVehPostProgressionData(self, vehicle):
        isHintEnabled = False
        isAvailable = vehicle.postProgressionAvailability(unlockOnly=True).result
        isVisible = vehicle.isPostProgressionExists
        if vehicle.xp > 0 and isAvailable:
            purchasableStep = vehicle.postProgression.getFirstPurchasableStep(ExtendedMoney(xp=vehicle.xp))
            if purchasableStep is not None:
                isHintEnabled = purchasableStep.stepID == vehicle.postProgression.getRawTree().rootStep
        tutorialStorage = getTutorialGlobalStorage()
        if tutorialStorage is not None:
            tutorialStorage.setValue(GLOBAL_FLAG.HANGAR_VEH_POST_PROGRESSION_PURCHASABLE, isHintEnabled)
        return {b'showCounter': (needToShowCounter(vehicle)), 
           b'btnEnabled': isAvailable, 
           b'btnVisible': isVisible}
