from collections import defaultdict
import typing
from helpers.i18n import makeString as _ms
from adisp import adisp_process
from debug_utils import LOG_WARNING, LOG_DEBUG, LOG_ERROR
from gui.Scaleform.daapi import LobbySubView
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
from gui.Scaleform.daapi.view.lobby.shared.fitting_select_popover import FITTING_MODULES
from gui.Scaleform.daapi.view.lobby.shared.fitting_slot_vo import FittingSlotVO
from gui.Scaleform.daapi.view.lobby.vehicle_compare import cmp_helpers
from gui.Scaleform.daapi.view.lobby.vehicle_compare.cmp_configurator_base import VehicleCompareConfiguratorBaseView
from gui.Scaleform.daapi.view.lobby.vehicle_compare.cmp_configurator_parameters import VehicleCompareParameters
from gui.Scaleform.daapi.view.lobby.vehicle_compare.cmp_configurator_vehicle import g_cmpConfiguratorVehicle
from gui.Scaleform.daapi.view.meta.VehicleCompareConfiguratorMainMeta import VehicleCompareConfiguratorMainMeta
from gui.Scaleform.daapi.view.meta.VehicleCompareConfiguratorViewMeta import VehicleCompareConfiguratorViewMeta
from gui.Scaleform.framework import g_entitiesFactories
from gui.Scaleform.framework.managers.loaders import SFViewLoadParams
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS
from gui.Scaleform.genConsts.VEHICLE_COMPARE_CONSTANTS import VEHICLE_COMPARE_CONSTANTS
from gui.Scaleform.locale.VEH_COMPARE import VEH_COMPARE
from gui.SystemMessages import pushMessagesFromResult
from gui.game_control.veh_comparison_basket import PARAMS_AFFECTED_TANKMEN_SKILLS
from gui.impl.gen import R
from gui.impl.lobby.vehicle_compare.interactors import CompareInteractingItem
from gui.shared.event_bus import EVENT_BUS_SCOPE
from gui.shared.gui_items import Tankman, GUI_ITEM_TYPE, vehicle_adjusters, GUI_ITEM_TYPE_NAMES
from gui.shared.gui_items.Tankman import CrewTypes
from gui.shared.gui_items.Vehicle import Vehicle
from gui.shared.gui_items.processors.module import ModuleProcessor
from helpers import dependency
from items import tankmen, vehicles
from items.components.skills_constants import ROLES_BY_SKILLS, ORDERED_ROLES, COMMON_ROLE
from post_progression_common import VehicleState
from shared_utils import findFirst
from skeletons.gui.game_control import IVehicleComparisonBasket
from skeletons.gui.impl import IGuiLoader
from skeletons.gui.shared import IItemsCache
VEHICLE_FITTING_SLOTS = FITTING_MODULES
SKILLS_ORDER = (
 COMMON_ROLE,) + ORDERED_ROLES
_EMPTY_ID = -1

@dependency.replace_none_kwargs(itemsCache=IItemsCache)
def getFittingSlotsData(vehicle, slotsRange, voClass=None, itemsCache=None):
    devices = []
    voClass = voClass or FittingSlotVO
    modulesData = _getVehicleModulesBySlotType(vehicle)
    for slotType in slotsRange:
        devices.append(voClass(modulesData[slotType], vehicle, slotType, tooltipType=TOOLTIPS_CONSTANTS.HANGAR_MODULE))

    return devices


def _getVehicleModulesBySlotType(vehicle):
    modules = {(GUI_ITEM_TYPE_NAMES[GUI_ITEM_TYPE.CHASSIS]): (
                                                    vehicle.chassis,), 
       (GUI_ITEM_TYPE_NAMES[GUI_ITEM_TYPE.TURRET]): (
                                                   vehicle.turret,), 
       (GUI_ITEM_TYPE_NAMES[GUI_ITEM_TYPE.GUN]): (
                                                vehicle.gun,), 
       (GUI_ITEM_TYPE_NAMES[GUI_ITEM_TYPE.ENGINE]): (
                                                   vehicle.engine,), 
       (GUI_ITEM_TYPE_NAMES[GUI_ITEM_TYPE.RADIO]): (
                                                  vehicle.radio,)}
    return modules


def _getSlotDataIndexes(slots):
    index = 0
    indexes = []
    for _ in slots:
        indexes.append((index,))
        index += 1

    return indexes


_SLOT_DATA_INDEXES = _getSlotDataIndexes(VEHICLE_FITTING_SLOTS)

class _CmpOptDeviceRemover(ModuleProcessor):

    def __init__(self, vehicle, item, slotIndex, plugs=tuple()):
        super(_CmpOptDeviceRemover, self).__init__(item, b'remove', plugs)
        self.__vehicle = vehicle
        self.__slotIndex = slotIndex
        return

    def _request(self, callback):
        removed, reason = vehicle_adjusters.removeOptionalDevice(self.__vehicle, self.__slotIndex)
        if removed:
            super(_CmpOptDeviceRemover, self)._request(callback)
        else:
            callback(self._errorHandler(0, reason))
        return

    def _getMsgCtx(self):
        return {b'name': (self.item.userName), b'kind': (self.item.userType), 
           b'money': 0}


class _ConfigFittingSlotVO(FittingSlotVO):

    def __init__(self, modulesData, vehicle, moduleType, tooltipType=None, isDisabledTooltip=False):
        super(_ConfigFittingSlotVO, self).__init__(modulesData, vehicle, moduleType, tooltipType, isDisabledTooltip)
        slotEmpty = self[b'id'] == -1
        self[b'showRemoveBtn'] = not slotEmpty
        self[b'tooltipType'] = b''
        self[b'tooltipType'] = TOOLTIPS_CONSTANTS.COMPARE_MODULE
        return


class _DefaultSkillCompletenessChecker(object):

    def isCompleted(self, levels, crew):
        for lvl in levels:
            if lvl < tankmen.MAX_SKILL_LEVEL:
                return False

        return True


class _FullCrewSkillsCompletenessChecker(_DefaultSkillCompletenessChecker):

    def isCompleted(self, levels, crew):
        isAllSkillsAre100 = super(_FullCrewSkillsCompletenessChecker, self).isCompleted(levels, crew)
        if isAllSkillsAre100:
            return len(levels) == len(crew)
        return False


class _CurrentCrewMonitor(object):
    _DEF_SKILL_CHECKER = _DefaultSkillCompletenessChecker()
    _FULL_CREW_SKILL_CHECKER = _FullCrewSkillsCompletenessChecker()
    itemsCache = dependency.descriptor(IItemsCache)

    def __init__(self, container):
        super(_CurrentCrewMonitor, self).__init__()
        self.__container = container
        self.__increasedTo100Skills = set()
        skillsCheckerStorage = defaultdict((lambda : self._DEF_SKILL_CHECKER))
        skillsCheckerStorage[PARAMS_AFFECTED_TANKMEN_SKILLS[0]] = self._FULL_CREW_SKILL_CHECKER
        skillsCheckerStorage[PARAMS_AFFECTED_TANKMEN_SKILLS[1]] = self._FULL_CREW_SKILL_CHECKER
        skillsCheckerStorage[PARAMS_AFFECTED_TANKMEN_SKILLS[2]] = self._FULL_CREW_SKILL_CHECKER
        vehicleCrew = self.itemsCache.items.getItemByCD(self.__container.getCurrentVehicle().intCD).crew
        levelsBySkills = defaultdict(list)
        for _, tankman in vehicleCrew:
            if tankman is not None:
                for skill in tankman.skills:
                    if skill.name in PARAMS_AFFECTED_TANKMEN_SKILLS:
                        levelsBySkills[skill.name].append(skill.level)

        for skillName, levels in levelsBySkills.iteritems():
            if not skillsCheckerStorage[skillName].isCompleted(levels, vehicleCrew):
                self.__increasedTo100Skills.add(skillName)

        return

    def isIncreasedSkillsSelected(self):
        if self.__container.getCurrentCrewSkillLevel() != CrewTypes.CURRENT:
            return False
        if self.__container.getCurrentCrewSkills().intersection(self.__increasedTo100Skills):
            return True
        return False

    def dispose(self):
        self.__container = None
        return


class _CrewSkillsManager(object):

    def __init__(self, vehicle, crewSkillLevel, selectedSkills):
        super(_CrewSkillsManager, self).__init__()
        self.__vehicle = vehicle
        self.__crewSkillLevel = None
        self.__selectedSkills = selectedSkills
        crewSkills = cmp_helpers.getVehicleCrewSkills(self.__vehicle)
        self.__rolesBySkills = defaultdict(set)
        self.__skillsByRoles = {}
        for idx, (role, skillsSet) in enumerate(crewSkills):
            for skill in skillsSet:
                self.__rolesBySkills[skill].add((idx, role))
                self.__skillsByRoles[role] = skillsSet

        self.changeCrewSkillLevel(crewSkillLevel)
        self.recalculateCrewBonuses()
        return

    def toggleSkill(self, skillName):
        if skillName not in PARAMS_AFFECTED_TANKMEN_SKILLS:
            LOG_WARNING((b'Attempt to set skill not affected on the vehicle parameters: {}').format(skillName))
            return False
        if self.__crewSkillLevel != CrewTypes.SKILL_100 and self.__crewSkillLevel != CrewTypes.CURRENT:
            LOG_WARNING((b'It is forbidden to set skill for {}% level crew!').format(self.__crewSkillLevel))
            return False
        if skillName not in self.__selectedSkills:
            self.__selectedSkills.add(skillName)
        else:
            self.__selectedSkills.remove(skillName)
        return self._applyTankmanSkill(self.__vehicle, self.__getAffectedTankmen((skillName,)), self.__skillsByRoles, self.__selectedSkills)

    def applySkillForTheSameVehicle(self, vehicle, skillName):
        if vehicle.intCD != self.__vehicle.intCD:
            LOG_DEBUG((b'Target vehicle is not the same as current vehicle! Expected {}, received {}').format(self.__vehicle.intCD, vehicle.intCD))
            return False
        if skillName not in PARAMS_AFFECTED_TANKMEN_SKILLS:
            LOG_WARNING((b'Attempt to set skill not affected on the vehicle parameters: {}').format(skillName))
            return False
        selectedSkills = self.__selectedSkills.copy()
        selectedSkills.add(skillName)
        return self._applyTankmanSkill(vehicle, self.__getAffectedTankmen((skillName,)), self.__skillsByRoles, selectedSkills)

    def changeCrewSkillLevel(self, newSkillsLevel):
        success = False
        if self.__crewSkillLevel != newSkillsLevel:
            self.__crewSkillLevel = newSkillsLevel
            skillsByRoles = {}
            if self.__crewSkillLevel == CrewTypes.SKILL_100 or self.__crewSkillLevel == CrewTypes.CURRENT:
                affectedTankmens = self.__getAffectedTankmen(self.__selectedSkills)
                for idx, role in affectedTankmens:
                    skillsByRoles[idx] = self.__skillsByRoles[role].intersection(self.__selectedSkills)

            if self.__crewSkillLevel == CrewTypes.CURRENT:
                levelsByIndexes, nativeVehiclesByIndexes = cmp_helpers.getVehCrewInfo(self.__vehicle.intCD)
                defRoleLevel = None
            else:
                nativeVehiclesByIndexes = None
                levelsByIndexes = None
                defRoleLevel = self.__crewSkillLevel
            self.__vehicle.crew = self.__vehicle.getCrewBySkillLevels(defRoleLevel, skillsByRoles, levelsByIndexes, nativeVehiclesByIndexes, activateBrotherhood=True)
            success = True
        return success

    def getSelectedSkills(self):
        return self.__selectedSkills.copy()

    def getCrewSkillLevel(self):
        return self.__crewSkillLevel

    def dispose(self):
        self.__vehicle = None
        return

    def recalculateCrewBonuses(self):
        crewDescriptors = []
        for _, tman in self.__vehicle.crew:
            crewDescriptors.append(tman.descriptor.makeCompactDescr() if tman else None)

        self.__vehicle.calcCrewBonuses(crewDescriptors, self.__vehicle.itemsCache.items, fromBattle=True)
        for _, tankman in self.__vehicle.crew:
            if tankman is not None:
                tankman.updateBonusesFromVehicle(self.__vehicle)

        return

    @classmethod
    def _applyTankmanSkill(cls, vehicle, affectedTankmens, skillsByRoles, selectedSkills):
        nationID, vehicleTypeID = vehicle.descriptor.type.id
        success = False
        for roleIdx, role in affectedTankmens:
            skills = skillsByRoles[role]
            veh_crew = vehicle.crew
            for idx, (vehCrewRoleIdx, vehCrewRole) in enumerate(veh_crew):
                if vehCrewRoleIdx == roleIdx:
                    prevRoleLevel = vehCrewRole.roleLevel if vehCrewRole is not None else tankmen.MAX_SKILL_LEVEL
                    veh_crew[idx] = (roleIdx,
                     cmp_helpers.createTankman(nationID, vehicleTypeID, role, prevRoleLevel, skills.intersection(selectedSkills), vehicle, vehCrewRoleIdx))
                    success = True
                    break
            else:
                LOG_WARNING((b'Tankmen with role index {} has not been found').format(roleIdx))

        return success

    def __getAffectedTankmen(self, skills):
        affectedTankmen = set()
        for skill in skills:
            affectedTankmen |= self.__rolesBySkills[skill]

        return affectedTankmen


class VehicleCompareConfiguratorView(VehicleCompareConfiguratorViewMeta):
    itemsCache = dependency.descriptor(IItemsCache)

    def __init__(self):
        self.__parametersView = None
        self.__progressionInject = None
        self.__ammoInject = None
        super(VehicleCompareConfiguratorView, self).__init__()
        self.__slotsVoData = [
         None] * (_SLOT_DATA_INDEXES[-1][-1] + 1)
        self.__currentCrewMonitor = None
        return

    def onCloseView(self):
        self._container.closeView()
        return

    def onCamouflageUpdated(self):
        self.__ammoInject.updateCamouflage()
        self.__updateParametersView()
        return

    def onOptDeviceUpdated(self):
        self.__ammoInject.update()
        self.__updateParametersView()
        return

    def onEquipmentUpdated(self):
        self.__ammoInject.update()
        self.__updateParametersView()
        return

    def onBattleBoosterUpdated(self):
        self.__ammoInject.update()
        self.__updateParametersView()
        return

    def onModulesUpdated(self):
        self.__updateSlotsData(FITTING_MODULES)
        self.__updateParametersView()
        self.as_setTopModulesSelectedS(self._container.isTopModulesSelected())
        return

    def onCrewSkillUpdated(self):
        self.__updateParametersView()
        self.__updateCrewAttentionIcon()
        return

    def onCrewLevelUpdated(self, newLvl):
        self.__updateParametersView()
        self.__updateCrewSelectionAvailability(newLvl)
        self.__updateCrewAttentionIcon()
        return

    def onPostProgressionUpdated(self):
        self.__ammoInject.update()
        self.__progressionInject.update()
        self.__updateParametersView()
        return

    def onChangeDynSlot(self):
        self.__ammoInject.update()
        self.__progressionInject.update()
        self.__updateParametersView()
        return

    def onResetToDefault(self):
        self.__updateSkillsData()
        self.__parametersView.init(self._container.getCurrentVehicle())
        self.__updateSlotsData(VEHICLE_FITTING_SLOTS)
        self.as_setTopModulesSelectedS(self._container.isTopModulesSelected())
        self.__updateCrewLvl()
        self.__updateCrewAttentionIcon()
        self.__ammoInject.update()
        self.__progressionInject.update()
        return

    def onBasketParametersChanged(self, basketVehData):
        if self.__parametersView is None or self.__progressionInject is None:
            return
        currentVehicle = self._container.getCurrentVehicle()
        isPostProgressionExists = currentVehicle.isPostProgressionExists
        if not isPostProgressionExists:
            currentVehicle.installPostProgression(basketVehData.getPostProgressionState(), True)
        if not currentVehicle.isRoleSlotExists():
            currentVehicle.optDevices.dynSlotType = basketVehData.getDynSlotType()
        initialVehicle, _ = self._container.getInitialVehicleData()
        self.as_setIsPostProgressionEnabledS(isPostProgressionExists)
        self.__ammoInject.update()
        self.__progressionInject.update()
        self.__parametersView.init(currentVehicle, initialVehicle)
        self.__parametersView.update()
        self.__updateControlBtns()
        return

    def onShellsUpdated(self, updateShells=False, selectedIndex=-1):
        if selectedIndex != -1:
            self.__updateParametersView()
        self.__updateShellSlots()
        self.__updateControlBtns()
        return

    def resetConfig(self):
        self._container.resetToDefault()
        return

    def applyConfig(self):
        self._container.applyNewParameters()
        self.onCloseView()
        return

    def installDevice(self, newId, slotType, slotIndex):
        if slotType == cmp_helpers.OPTIONAL_DEVICE_TYPE_NAME:
            self._container.installOptionalDevice(newId, slotIndex)
        elif slotType == cmp_helpers.EQUIPMENT_TYPE_NAME:
            self._container.installEquipment(newId, slotIndex)
        else:
            LOG_ERROR((b'{} installDevice. Unsupported slotType: {}').format(self, slotType))
        return

    def removeDevice(self, slotType, slotIndex):
        if slotType == cmp_helpers.OPTIONAL_DEVICE_TYPE_NAME:
            self._container.removeOptionalDevice(slotIndex)
        elif slotType == cmp_helpers.EQUIPMENT_TYPE_NAME:
            self._container.removeEquipment(slotIndex)
        elif slotType == cmp_helpers.BATTLE_BOOSTER_TYPE_NAME:
            self._container.removeBattleBooster()
        else:
            LOG_ERROR((b'{} removeDevice. Unsupported slotType: {}').format(self, slotType))
        return

    def toggleTopModules(self, value):
        self._container.selectTopModules(value)
        return

    def showModules(self):
        self._container.as_showViewS(VEHICLE_COMPARE_CONSTANTS.VEHICLE_MODULES_VIEW)
        return

    def skillSelect(self, skillType, slotIndex, selected):
        self._container.selectCrewSkill(skillType, selected)
        return

    def changeCrewLevel(self, crewLevelId):
        self._container.selectCrewLevel(crewLevelId)
        return

    def _onRegisterFlashComponent(self, viewPy, alias):
        super(VehicleCompareConfiguratorView, self)._onRegisterFlashComponent(viewPy, alias)
        if isinstance(viewPy, VehicleCompareParameters):
            self.__parametersView = viewPy
        elif alias == VEHICLE_COMPARE_CONSTANTS.VEHICLE_CONFIGURATOR_EQUIPMENT_WIDGET:
            self.__ammoInject = viewPy
        elif alias == VEHICLE_COMPARE_CONSTANTS.VEHICLE_CONFIGURATOR_MODIFICATIONS_WIDGET:
            self.__progressionInject = viewPy
        return

    def _init(self):
        super(VehicleCompareConfiguratorView, self)._init()
        currentVehicle = self._container.getCurrentVehicle()
        enableCamo = bool(cmp_helpers.getSuitableCamouflage(currentVehicle))
        topModulesFromStock = self._container.isTopModulesFromStock()
        enableTopModules = self._container.isModulesAvailableFromStock()
        isInInventory = self._container.getBasketVehCmpData().isInInventory()
        if isInInventory:
            self.__currentCrewMonitor = _CurrentCrewMonitor(self._container)
        self.as_setInitDataS({b'title': (_ms(VEH_COMPARE.VEHCONF_HEADER, vehName=currentVehicle.userName)), 
           b'resetBtnLabel': (VEH_COMPARE.VEHCONF_RESETBTNLABEL), 
           b'cancelBtnLabel': (VEH_COMPARE.VEHCONF_CANCELBTNLABEL), 
           b'applyBtnLabel': (VEH_COMPARE.VEHCONF_APPLYBTNLABEL), 
           b'resetBtnTooltip': (VEH_COMPARE.VEHCONF_RESETBTNLABEL_TOOLTIP), 
           b'cancelBtnTooltip': (VEH_COMPARE.VEHCONF_CANCELBTNLABEL_TOOLTIP), 
           b'applyBtnTooltip': (VEH_COMPARE.VEHCONF_COMPAREBTNLABEL_TOOLTIP), 
           b'crewLevels': (self.__getCrewLevels(isInInventory)), 
           b'enableTopModules': enableTopModules, 
           b'enableCamo': enableCamo})
        self.as_setIsPostProgressionEnabledS(currentVehicle.isPostProgressionExists)
        self.__updateCrewLvl()
        if currentVehicle.descriptor.type.hasCustomDefaultCamouflage:
            self.as_disableCamoS()
        self.__updateControlBtns()
        topModulesSelected = topModulesFromStock or self._container.isTopModulesSelected()
        self.as_setTopModulesSelectedS(topModulesSelected)
        self.__updateCrewAttentionIcon()
        self.__updateSkillsData()
        self.__updateSlotsData(VEHICLE_FITTING_SLOTS)
        initialVehicle, _ = self._container.getInitialVehicleData()
        self.__parametersView.init(currentVehicle, initialVehicle)
        return

    def _dispose(self):
        if self.__currentCrewMonitor:
            self.__currentCrewMonitor.dispose()
        self.__parametersView = None
        self.__progressionInject = None
        self.__ammoInject = None
        super(VehicleCompareConfiguratorView, self)._dispose()
        return

    def __updateSlotsData(self, slotsTypes):
        newVoData = getFittingSlotsData(self._container.getCurrentVehicle(), slotsTypes, _ConfigFittingSlotVO)
        for slotType in slotsTypes:
            indexesRange = _SLOT_DATA_INDEXES[VEHICLE_FITTING_SLOTS.index(slotType)]
            for idx in indexesRange:
                newSlotData = newVoData.pop(0)
                self.__slotsVoData[idx] = newSlotData

        self.as_setDevicesDataS(self.__slotsVoData)
        self.__updateParametersView()
        return

    def __updateParametersView(self):
        if self.__parametersView is not None:
            self.__updateSkillsData()
            self.__parametersView.update()
            self.__updateControlBtns()
        return

    def __updateCrewSelectionAvailability(self, newLvl):
        self.as_setSkillsBlockedS(newLvl != CrewTypes.SKILL_100 and newLvl != CrewTypes.CURRENT)
        return

    def __updateControlBtns(self):
        self.as_setResetEnabledS(self._container.isDifferentWithInitialBasketVeh())
        self.as_setApplyEnabledS(self._container.isCurrentVehicleModified())
        return

    def __updateSkillsData(self):
        vehicle = self._container.getCurrentVehicle()
        skills = []
        for skillType in PARAMS_AFFECTED_TANKMEN_SKILLS:
            roles = list(ROLES_BY_SKILLS[skillType])
            role = roles[0] if len(roles) == 1 else COMMON_ROLE
            skillLevel = Tankman.crewMemberRealSkillLevel(vehicle, skillType, role)
            skills.append({b'icon': (Tankman.getSkillBigIconPath(skillType)), 
               b'skillType': skillType, 
               b'skillRole': role, 
               b'selected': (skillType in self._container.getCurrentCrewSkills()), 
               b'skillLevel': (max(skillLevel, 0))})

        skills.sort(key=(lambda item: SKILLS_ORDER.index(item[b'skillRole'])))
        self.as_setSkillsS(skills)
        return

    @staticmethod
    def __getCrewLevels(isInHangar):
        items = [
         {b'label': (VEH_COMPARE.VEHICLECOMPAREVIEW_CREW_SKILL100), b'id': (CrewTypes.SKILL_100), b'showAlert': False, 
            b'tooltip': None}, {b'label': (VEH_COMPARE.VEHICLECOMPAREVIEW_CREW_SKILL75), b'id': (CrewTypes.SKILL_75)}, {b'label': (VEH_COMPARE.VEHICLECOMPAREVIEW_CREW_SKILL50), b'id': (CrewTypes.SKILL_50)}]
        if isInHangar:
            items.append({b'label': (VEH_COMPARE.VEHICLECOMPAREVIEW_CREW_CURRENT), b'id': (CrewTypes.CURRENT)})
        return items

    def __updateCrewLvl(self):
        crewLevel = self._container.getCurrentCrewSkillLevel()
        self.as_setCrewLevelIndexS(CrewTypes.ALL.index(crewLevel))
        self.__updateCrewSelectionAvailability(crewLevel)
        return

    def __updateShellSlots(self):
        self.__ammoInject.updateShells()
        return

    def __updateCrewAttentionIcon(self):
        isVisible = False
        if self.__currentCrewMonitor:
            isVisible = self.__currentCrewMonitor.isIncreasedSkillsSelected()
        self.as_setCrewAttentionIconVisibleS(isVisible)
        return


class VehicleCompareConfiguratorMain(LobbySubView, VehicleCompareConfiguratorMainMeta):
    itemsCache = dependency.descriptor(IItemsCache)
    comparisonBasket = dependency.descriptor(IVehicleComparisonBasket)
    uiLoader = dependency.descriptor(IGuiLoader)

    def __init__(self, ctx=None):
        super(VehicleCompareConfiguratorMain, self).__init__(ctx)
        self.__vehIndex = ctx.get(b'index')
        if not isinstance(self.__vehIndex, int):
            raise UserWarning((b'Index of vehicle should be integer: {}').format(self.__vehIndex))
        if self.__vehIndex < 0 or self.__vehIndex >= self.comparisonBasket.getVehiclesCount():
            raise UserWarning((b'Index of vehicle out of range: {} not in (0, {})').format(self.__vehIndex, self.comparisonBasket.getVehiclesCount()))
        self.__backAlias = ctx.get(b'previewAlias', VIEW_ALIAS.VEHICLE_COMPARE)
        self.__vehicle = None
        self.__vehItem = None
        self.__crewSkillsManager = None
        self.__views = {}
        self.__topModules = None
        self.__stockModules = None
        self.__selectedShellIndex = None
        return

    def as_showViewS(self, alias):
        result = super(VehicleCompareConfiguratorMain, self).as_showViewS(alias)
        if alias in self.__views:
            self.__views[alias].onShow()
        return result

    def getCurrentVehicle(self):
        return self.__vehicle

    def getCurrentVehicleItem(self):
        return self.__vehItem

    def getCurrentVehicleCopy(self):
        vehicle = Vehicle(strCompactDescr=self.__vehicle.descriptor.makeCompactDescr())
        vehicle.crew = self.__vehicle.crew[:]
        for i, equipmentIntCD in enumerate(self.__vehicle.consumables.installed.getIntCDs(default=None)):
            vehicle_adjusters.installEquipment(vehicle, equipmentIntCD, i)

        vehicle.descriptor.activeGunShotIndex = self.__vehicle.descriptor.activeGunShotIndex
        vehicle.optDevices.dynSlotType = self.__vehicle.optDevices.dynSlotType
        vehicle.installPostProgression(self.__vehicle.postProgression.getState(), True)
        cmp_helpers.applyCamouflage(vehicle, cmp_helpers.isCamouflageSet(self.__vehicle))
        for battleBooster in self.__vehicle.battleBoosters.installed.getItems():
            vehicle_adjusters.installBattleBoosterOnVehicle(vehicle, battleBooster.intCD)

        return vehicle

    def getInitialVehicleData(self):
        basketVehicle = self.getBasketVehCmpData()
        if basketVehicle.isInInventory():
            strCD = basketVehicle.getInvVehStrCD()
            crewLvl, crewSkills = basketVehicle.getInventoryCrewData()
            equipment = basketVehicle.getInvEquipment()
        else:
            strCD = basketVehicle.getStockVehStrCD()
            crewLvl = basketVehicle.getStockCrewLvl()
            crewSkills = basketVehicle.getStockCrewSkills()
            equipment = basketVehicle.getStockEquipment()
        vehicle = Vehicle(strCD)
        for slotIndex, equipmentSlot in enumerate(equipment):
            vehicle_adjusters.installEquipment(vehicle, equipmentSlot, slotIndex)

        cmp_helpers.applyCamouflage(vehicle, basketVehicle.invHasCamouflage())
        battleBooster = basketVehicle.getBattleBooster()
        if battleBooster is not None:
            vehicle_adjusters.installBattleBoosterOnVehicle(vehicle, battleBooster.intCD)
        postProgressionState = basketVehicle.getInvPostProgressionState()
        vehicle.installPostProgression(postProgressionState, rebuildAttrs=False)
        dynSlotType = basketVehicle.getInvDynSlotType()
        vehicle.optDevices.dynSlotType = dynSlotType
        return (
         vehicle, _CrewSkillsManager(vehicle, crewLvl, crewSkills))

    def getCurrentCrewSkills(self):
        return self.__crewSkillsManager.getSelectedSkills()

    def getCurrentCrewSkillLevel(self):
        return self.__crewSkillsManager.getCrewSkillLevel()

    def getBasketVehCmpData(self):
        return self.comparisonBasket.getVehicleAt(self.__vehIndex)

    def getVehicleWithAppliedSkill(self, skillName):
        vehicle = self.getCurrentVehicleCopy()
        if self.__crewSkillsManager.applySkillForTheSameVehicle(vehicle, skillName):
            return vehicle
        else:
            return

    def getCurrentShellIndex(self):
        return self.__selectedShellIndex

    def isTopModulesFromStock(self):
        topModules = self.__getTopModules()
        stockModules = self.__getStockModules()
        return all(bool(item in stockModules) for item in topModules)

    def isModulesAvailableFromStock(self):
        stockModulesCount = len(self.__getStockModules())
        avalibleModules = cmp_helpers.VehicleAllModules.getVehicleAvailableModules(self.getCurrentVehicleCopy())
        avalibleModulesCount = avalibleModules.getCountAllModules()
        return avalibleModulesCount > stockModulesCount

    def isTopModulesSelected(self):
        topModules = self.__getTopModules()
        selectedModules = cmp_helpers.getVehicleModules(self.__vehicle)
        return all(bool(item in selectedModules) for item in topModules)

    def isCamouflageSet(self):
        return cmp_helpers.isCamouflageSet(self.__vehicle)

    def applyNewParameters(self):
        self.comparisonBasket.applyNewParameters(self.__vehIndex, self.__vehicle, self.getCurrentCrewSkillLevel(), self.getCurrentCrewSkills(), self.getCurrentShellIndex())
        return

    def isDifferentWithInitialBasketVeh(self):
        basketVehicle = self.getBasketVehCmpData()
        if basketVehicle.isInInventory():
            basketVehCrewLvl, basketVehCrewSkills = basketVehicle.getInventoryCrewData()
            equipment = basketVehicle.getInvEquipment()
            strCD = basketVehicle.getInvVehStrCD()
        else:
            basketVehCrewLvl = basketVehicle.getStockCrewLvl()
            basketVehCrewSkills = basketVehicle.getStockCrewSkills()
            equipment = basketVehicle.getStockEquipment()
            strCD = basketVehicle.getStockVehStrCD()
        return self.__isHasDifferences(strCD, equipment, basketVehCrewLvl, basketVehCrewSkills, basketVehicle.getInventoryShellIndex(), basketVehicle.invHasCamouflage(), basketVehicle.getBattleBooster(), basketVehicle.getInvDynSlotType(), basketVehicle.getInvPostProgressionState())

    def isCurrentVehicleModified(self):
        basketVehicle = self.getBasketVehCmpData()
        crewLvl, crewSkills = basketVehicle.getCrewData()
        return self.__isHasDifferences(basketVehicle.getVehicleStrCD(), basketVehicle.getEquipment(), crewLvl, crewSkills, basketVehicle.getSelectedShellIndex(), basketVehicle.hasCamouflage(), basketVehicle.getBattleBooster(), basketVehicle.getDynSlotType(), basketVehicle.getPostProgressionState())

    def setModules(self, modules):
        if modules:
            notFittedReasons = []
            oldGunIntCD = self.__vehicle.gun.intCD
            vehicle_adjusters.installModulesSet(self.__vehicle, list(modules[:]), notFittedReasons)
            self.__checkAndRemoveIncompatibleEquipments()
            if notFittedReasons:
                for notFitReason in notFittedReasons:
                    LOG_DEBUG((b'Module has not been installed properly, reason: {}').format(notFitReason))

            if oldGunIntCD != self.__vehicle.gun.intCD:
                firstShellIndex = 0
                newShellIndex = -1
                if self.__updateSelectedShell(firstShellIndex):
                    newShellIndex = firstShellIndex
                self.__recalculateCrewBonuses()
                self.__notifyViews(b'onShellsUpdated', updateShells=True, selectedIndex=newShellIndex)
            else:
                newGunToInstall = findFirst((lambda module: module.itemTypeID == GUI_ITEM_TYPE.GUN), modules, None)
                if newGunToInstall is not None:
                    self.__vehicle.descriptor.activeGunShotIndex = self.__selectedShellIndex
            self.__recalculateCrewBonuses()
            self.__notifyViews(b'onModulesUpdated')
        return

    def selectTopModules(self, select):
        if select:
            modules = self.__getTopModules()
        else:
            modules = self.__getStockModules()
        self.setModules(modules)
        return

    def selectShell(self, slotIndex):
        if self.__updateSelectedShell(slotIndex):
            self.__recalculateCrewBonuses()
            self.__notifyViews(b'onShellsUpdated', selectedIndex=slotIndex)
        return

    def selectCamouflage(self, select):
        if not self.__vehicle.descriptor.type.hasCustomDefaultCamouflage:
            cmp_helpers.applyCamouflage(self.__vehicle, select)
            self.__recalculateCrewBonuses()
            self.__notifyViews(b'onCamouflageUpdated')
        return

    def resetToDefault(self):
        self.__vehicle, self.__crewSkillsManager = self.getInitialVehicleData()
        self.__vehItem.setItem(self.__vehicle)
        basketVehicle = self.getBasketVehCmpData()
        basketShellIndex = basketVehicle.getInventoryShellIndex()
        self.__updateSelectedShell(basketShellIndex)
        battleBooster = basketVehicle.getBattleBooster()
        if battleBooster is not None:
            self.removeBattleBooster()
        self.__recalculateCrewBonuses()
        self.__notifyViews(b'onResetToDefault')
        return

    def installOptionalDevice(self, newId, slotIndex):
        isInstalled, _ = vehicle_adjusters.installOptionalDevice(self.__vehicle, newId, slotIndex)
        if isInstalled:
            self.__recalculateCrewBonuses()
            self.__notifyViews(b'onOptDeviceUpdated')
        return

    def swapOptionalDevice(self, leftID, rightID):
        isSwapped, _ = vehicle_adjusters.swapOptionalDevice(self.__vehicle, leftID, rightID)
        if isSwapped:
            self.__recalculateCrewBonuses()
            self.__notifyViews(b'onOptDeviceUpdated')
        return

    def removeOptionalDevice(self, slotIndex):
        self.__launchOptDeviceRemoving(slotIndex)
        return

    def installEquipment(self, newId, slotIndex):
        self.__installEquipment(newId, slotIndex)
        self.__recalculateCrewBonuses()
        self.__notifyViews(b'onEquipmentUpdated')
        return

    def removeEquipment(self, slotIndex):
        self.__installEquipment(None, slotIndex)
        self.__recalculateCrewBonuses()
        self.__notifyViews(b'onEquipmentUpdated')
        return

    def swapEquipment(self, leftID, rightID):
        vehicle_adjusters.swapEquipment(self.__vehicle, leftID, rightID)
        self.__recalculateCrewBonuses()
        self.__notifyViews(b'onEquipmentUpdated')
        return

    def installBattleBooster(self, newId):
        self.__installBattleBooster(newId)
        self.__recalculateCrewBonuses()
        self.__notifyViews(b'onBattleBoosterUpdated')
        return

    def removeBattleBooster(self):
        self.__installBattleBooster(None)
        self.__recalculateCrewBonuses()
        self.__notifyViews(b'onBattleBoosterUpdated')
        return

    def installPostProgression(self, state):
        self.__installPostProgression(state)
        self.__recalculateCrewBonuses()
        self.__notifyViews(b'onPostProgressionUpdated')
        return

    def changeDynRoleSlot(self, slotID):
        self.__vehicle.optDevices.dynSlotType = vehicles.g_cache.supplySlots().slotDescrs[slotID] if slotID else None
        self.__recalculateCrewBonuses()
        self.__notifyViews(b'onChangeDynSlot')
        return

    def removePostProgression(self):
        self.__installPostProgression(VehicleState())
        self.__recalculateCrewBonuses()
        self.__notifyViews(b'onPostProgressionUpdated')
        return

    def __recalculateCrewBonuses(self):
        self.__crewSkillsManager.recalculateCrewBonuses()
        return

    def selectCrewSkill(self, skillType, selected):
        savedValue = skillType in self.__crewSkillsManager.getSelectedSkills()
        if selected != savedValue:
            if self.__crewSkillsManager.toggleSkill(skillType):
                self.__recalculateCrewBonuses()
                self.__notifyViews(b'onCrewSkillUpdated')
        else:
            LOG_WARNING((b'Attempt to apply the same value for {} = {}').format(skillType, selected))
        return

    def selectCrewLevel(self, crewLevelId):
        if self.__crewSkillsManager.changeCrewSkillLevel(crewLevelId):
            self.__recalculateCrewBonuses()
            self.__notifyViews(b'onCrewLevelUpdated', crewLevelId)
        return

    def closeView(self, forcedBackAliace=None):
        if self.__canClose():
            event = g_entitiesFactories.makeLoadEvent(SFViewLoadParams(forcedBackAliace or self.__backAlias))
            self.fireEvent(event, scope=EVENT_BUS_SCOPE.LOBBY)
        return

    def _populate(self):
        super(VehicleCompareConfiguratorMain, self)._populate()
        self.comparisonBasket.onSwitchChange += self.__onBasketStateChanged
        self.comparisonBasket.onParametersChange += self.__onBasketParametersChanged
        basketVehicleData = self.getBasketVehCmpData()
        basketVehCrewLvl, basketVehCrewSkills = basketVehicleData.getCrewData()
        self.__vehicle = Vehicle(basketVehicleData.getVehicleStrCD())
        g_cmpConfiguratorVehicle.setVehicle(self.__vehicle)
        self.__vehItem = CompareInteractingItem(self.__vehicle)
        self.__crewSkillsManager = _CrewSkillsManager(self.__vehicle, basketVehCrewLvl, basketVehCrewSkills)
        equipment = basketVehicleData.getEquipment()
        for slotIndex, equipmentSlot in enumerate(equipment):
            self.__installEquipment(equipmentSlot, slotIndex)

        cmp_helpers.applyCamouflage(self.__vehicle, basketVehicleData.hasCamouflage())
        battleBooster = basketVehicleData.getBattleBooster()
        if battleBooster is not None:
            vehicle_adjusters.installBattleBoosterOnVehicle(self.__vehicle, battleBooster.intCD)
        dynSlotType = basketVehicleData.getDynSlotType()
        self.__vehicle.optDevices.dynSlotType = dynSlotType
        postProgressionState = basketVehicleData.getPostProgressionState()
        self.__vehicle.installPostProgression(postProgressionState, True)
        self.__updateSelectedShell(basketVehicleData.getSelectedShellIndex())
        self.__recalculateCrewBonuses()
        self.as_showViewS(VEHICLE_COMPARE_CONSTANTS.VEHICLE_CONFIGURATOR_VIEW)
        self.comparisonBasket.isLocked = True
        return

    def _dispose(self):
        self.comparisonBasket.onSwitchChange -= self.__onBasketStateChanged
        self.comparisonBasket.onParametersChange -= self.__onBasketParametersChanged
        g_cmpConfiguratorVehicle.clear()
        self.__vehItem.clear()
        self.__vehItem = None
        if self.__crewSkillsManager is not None:
            self.__crewSkillsManager.dispose()
            self.__crewSkillsManager = None
        self.__views = None
        self.comparisonBasket.isLocked = False
        super(VehicleCompareConfiguratorMain, self)._dispose()
        return

    def _onRegisterFlashComponent(self, viewPy, alias):
        super(VehicleCompareConfiguratorMain, self)._onRegisterFlashComponent(viewPy, alias)
        if isinstance(viewPy, VehicleCompareConfiguratorBaseView):
            self.__views[alias] = viewPy
            viewPy.setContainer(self)
        return

    def __canClose(self):
        resID = R.views.lobby.tanksetup.VehicleCompareAmmunitionSetup()
        return self.uiLoader.windowsManager.getViewByLayoutID(resID) is None

    @adisp_process
    def __launchOptDeviceRemoving(self, slotIndex):
        installedDevice = self.__vehicle.optDevices.installed[slotIndex]
        if installedDevice is not None:
            result = yield _CmpOptDeviceRemover(self.__vehicle, installedDevice, slotIndex).request()
            if result.success:
                self.__recalculateCrewBonuses()
                self.__notifyViews(b'onOptDeviceUpdated')
            else:
                pushMessagesFromResult(result)
        return

    def __isHasDifferences(self, strCD, equipment, basketVehCrewLvl, basketVehCrewSkills, selShellIndex, hasCamouflage, battleBooster, dynSlotType, postProgressionState):
        if basketVehCrewLvl != self.getCurrentCrewSkillLevel():
            return True
        else:
            if basketVehCrewSkills != self.getCurrentCrewSkills():
                return True
            if not cmp_helpers.isEquipmentSame(equipment, self.__vehicle.consumables.installed.getIntCDs(default=None)):
                return True
            if selShellIndex != self.__selectedShellIndex:
                return True
            currVehHasCamouflage = cmp_helpers.isCamouflageSet(self.__vehicle)
            if hasCamouflage != currVehHasCamouflage:
                return True
            currBoosters = self.__vehicle.battleBoosters.installed
            currBooster = currBoosters[0] if currBoosters.getCapacity() > 0 else None
            if currBooster:
                return True
            if currVehHasCamouflage:
                targetVehicle = Vehicle(self.__vehicle.descriptor.makeCompactDescr())
                cmp_helpers.removeVehicleCamouflages(targetVehicle)
            else:
                targetVehicle = self.__vehicle
            if strCD != targetVehicle.descriptor.makeCompactDescr():
                return True
            if dynSlotType != self.__vehicle.optDevices.dynSlotType:
                return True
            if postProgressionState != self.__vehicle.postProgression.getState(implicitCopy=False):
                return True
            return False

    def __getTopModules(self):
        if self.__topModules is None:
            self.__topModules = cmp_helpers.getVehicleTopModules(self.__vehicle)
        return self.__topModules

    def __getStockModules(self):
        if self.__stockModules is None:
            self.__stockModules = tuple(reversed(cmp_helpers.getVehicleModules(Vehicle(self.getBasketVehCmpData().getStockVehStrCD()))))
        return self.__stockModules

    def __installEquipment(self, intCD, slotIndex):
        vehicle_adjusters.installEquipment(self.__vehicle, intCD, slotIndex)
        return

    def __installBattleBooster(self, intCD):
        vehicle_adjusters.installBattleBoosterOnVehicle(self.__vehicle, intCD)
        return

    def __installPostProgression(self, state):
        vehicle = self.getCurrentVehicle()
        vehicle.installPostProgression(state, True)
        if not vehicle.isRoleSlotExists():
            vehicle.optDevices.dynSlotType = None
        return

    def __updateSelectedShell(self, slotIndex):
        slotIndex = int(slotIndex)
        if self.__selectedShellIndex != slotIndex:
            vehicle_adjusters.changeShell(self.__vehicle, slotIndex)
            self.__selectedShellIndex = slotIndex
            return True
        return False

    def __onBasketStateChanged(self):
        if not self.comparisonBasket.isEnabled():
            self.closeView(VIEW_ALIAS.LOBBY_HANGAR)
        return

    def __onBasketParametersChanged(self, data):
        if self.__vehIndex not in data:
            return
        self.__notifyViews(b'onBasketParametersChanged', self.getBasketVehCmpData())
        return

    def __notifyViews(self, event, *args, **kwargs):
        if self.__views is None:
            return
        else:
            for component in self.__views.itervalues():
                notifier = getattr(component, event, None)
                if notifier and callable(notifier):
                    notifier(*args, **kwargs)

            return

    def __checkAndRemoveIncompatibleEquipments(self):
        for i, equipmentIntCD in enumerate(self.__vehicle.consumables.installed.getIntCDs(default=None)):
            if equipmentIntCD:
                equipment = self.itemsCache.items.getItemByCD(int(equipmentIntCD))
                success, _ = equipment.mayInstall(self.__vehicle, i)
                if not success:
                    self.removeEquipment(i)

        return
