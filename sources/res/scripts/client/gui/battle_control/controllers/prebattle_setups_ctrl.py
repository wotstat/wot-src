from __future__ import absolute_import
import logging, typing
from future.utils import viewitems
import BigWorld
from account_helpers.settings_core.settings_constants import GAME
from battle_modifiers_common import EXT_DATA_MODIFIERS_KEY
from constants import ARENA_PERIOD, VEHICLE_SIEGE_STATE
from gui.battle_control.arena_info.interfaces import IPrebattleSetupsController
from gui.battle_control.battle_constants import BATTLE_CTRL_ID
from gui.shared.gui_items.Vehicle import Vehicle
from gui.shared.items_parameters.functions import getVehicleFactors
from gui.shared.utils.MethodsRules import MethodsRules
from gui.veh_post_progression.battle_cooldown_manager import BattleCooldownManager
from gui.veh_post_progression.helpers import setFeatures, setDisabledSwitches, getInstalledShells, updateInvInstalled
from gui.veh_post_progression.sounds import playSound, Sounds
from helpers import dependency
from items import vehicles
from items.components.post_progression_components import getActiveModifications
from items.utils import getCircularVisionRadius, getFirstReloadTime
from post_progression_common import EXT_DATA_PROGRESSION_KEY, EXT_DATA_SLOT_KEY, TANK_SETUP_GROUPS, TankSetupLayouts, TankSetups, VehicleState, unpackActionCDs
from shared_utils import CONST_CONTAINER
from skeletons.account_helpers.settings_core import ISettingsCore
from skeletons.gui.battle_session import IBattleSessionProvider
from skeletons.gui.shared.gui_items import IGuiItemsFactory
if typing.TYPE_CHECKING:
    from items.vehicles import VehicleDescr
_logger = logging.getLogger(__name__)
_SWITCH_SETUPS_ACTION = 0
_EXT_ENHANCEMENTS_KEY = b'extEnhancements'
_EXT_PROGRESSION_MODS = b'extActiveProgression'
_EXT_RESPAWN_BOOST = b'respawnReloadTimeFactor'
_EXT_SIEGE_STATE_KEY = b'extSiegeState'
_SETUP_NAME_TO_LAYOUT = {(TankSetups.SHELLS): (TankSetupLayouts.SHELLS), 
   (TankSetups.EQUIPMENT): (TankSetupLayouts.EQUIPMENT), 
   (TankSetups.OPTIONAL_DEVICES): (TankSetupLayouts.OPTIONAL_DEVICES), 
   (TankSetups.BATTLE_BOOSTERS): (TankSetupLayouts.BATTLE_BOOSTERS)}

class _States(CONST_CONTAINER):
    IDLE = 0
    VEHICLE_ID = 1
    CREW = 2
    DYN_SLOT = 4
    ENHANCEMENTS = 8
    PROGRESSION = 32
    RESPAWN = 64
    SETUPS = 128
    SETUPS_INDEXES = 256
    DISABLED_SWITCHES = 512
    INIT_COMPLETE = 1024
    SELECTION_STARTED = 2048
    SELECTION_STOPPED = 4096
    SELECTION_ENDED = 8192
    INIT_READY = VEHICLE_ID | CREW | DYN_SLOT | ENHANCEMENTS | PROGRESSION | RESPAWN | SETUPS | SETUPS_INDEXES | DISABLED_SWITCHES
    SELECTION_AWAIT_HIDING = 16384


class IPrebattleSetupsListener(object):

    def showSetupsView(self, vehicle, isArenaLoaded=False):
        return

    def updateVehicleParams(self, vehicle, factors):
        return

    def updateVehicleSetups(self, vehicle):
        return

    def stopSetupsSelection(self):
        return

    def hideSetupsView(self):
        return

    def onArenaLoaded(self):
        return


class PrebattleSetupsController(MethodsRules, IPrebattleSetupsController):
    __itemsFactory = dependency.descriptor(IGuiItemsFactory)
    __sessionProvider = dependency.descriptor(IBattleSessionProvider)
    __settingsCore = dependency.descriptor(ISettingsCore)
    __slots__ = (b'__state', b'__playerVehicleID', b'__vehicle', b'__invData', b'__extData', b'__hasValidCaps', b'__cooldown', b'__arenaLoaded')

    def __init__(self):
        super(PrebattleSetupsController, self).__init__()
        self.__state = _States.IDLE
        self.__invData = {}
        self.__extData = {}
        self.__playerVehicleID = None
        self.__vehicle = None
        self.__hasValidCaps = False
        self.__cooldown = BattleCooldownManager()
        self.__arenaLoaded = False
        return

    def getControllerID(self):
        return BATTLE_CTRL_ID.PREBATTLE_SETUPS_CTRL

    def getPrebattleSetupsVehicle(self):
        if self.isSelectionStarted():
            return self.__vehicle
        else:
            return

    def getPrebattleVehicleID(self):
        if self.isSelectionStarted():
            return self.__playerVehicleID
        return 0

    def startControl(self, battleCtx, arenaVisitor):
        self.__hasValidCaps = arenaVisitor.bonus.hasSwitchSetups()
        self.__extData[_EXT_SIEGE_STATE_KEY] = VEHICLE_SIEGE_STATE.DISABLED
        self.__extData[EXT_DATA_MODIFIERS_KEY] = arenaVisitor.getArenaModifiers()
        return

    def stopControl(self):
        self.clear(leave=True)
        self.__state = _States.IDLE
        self.__invData.clear()
        self.__extData.clear()
        self.__playerVehicleID = None
        self.__vehicle = None
        self.__hasValidCaps = False
        self.__arenaLoaded = False
        self.__cooldown.reset(_SWITCH_SETUPS_ACTION)
        return

    def isArenaLoaded(self):
        return self.__arenaLoaded

    def isSelectionStarted(self):
        return bool(self.__state & _States.SELECTION_STARTED)

    def isSelectionEnded(self):
        return bool(self.__state & (_States.SELECTION_ENDED | _States.SELECTION_STOPPED))

    @MethodsRules.delayable()
    def setPlayerVehicle(self, vehicleID, vehDescr):
        if self.__isSelectionStopped() or self.__state & _States.VEHICLE_ID:
            return
        self.__playerVehicleID = vehicleID
        self.__vehicle = Vehicle(strCompactDescr=vehDescr.makeCompactDescr())
        self.__onInitStepCompleted(_States.VEHICLE_ID)
        return

    def setPeriodInfo(self, period, endTime, length, additionalInfo):
        self.__updatePeriod(period)
        return

    def stopSelection(self):
        if not self.__isSelectionStopped():
            self.__updateState(_States.SELECTION_STOPPED)
            self.__onFiniStepCompleted()
        return

    @MethodsRules.delayable(b'setPlayerVehicle')
    def setCrew(self, vehicleID, crew):
        if self.__playerVehicleID != vehicleID or self.__isSelectionStopped() or self.__state & _States.CREW:
            return
        self.__invData[b'battleCrewCDs'] = crew
        self.__onInitStepCompleted(_States.CREW)
        return

    @MethodsRules.delayable(b'setPlayerVehicle')
    def setDynSlotType(self, vehicleID, dynSlotTypeID):
        if self.__playerVehicleID != vehicleID or self.__isSelectionStopped() or self.__state & _States.DYN_SLOT:
            return
        self.__extData[EXT_DATA_SLOT_KEY] = dynSlotTypeID
        self.__onInitStepCompleted(_States.DYN_SLOT)
        return

    @MethodsRules.delayable(b'setPlayerVehicle')
    def setEnhancements(self, vehicleID, enhancements):
        if self.__playerVehicleID != vehicleID or self.__isSelectionStopped() or self.__state & _States.ENHANCEMENTS:
            return
        self.__extData[_EXT_ENHANCEMENTS_KEY] = enhancements
        self.__onInitStepCompleted(_States.ENHANCEMENTS)
        return

    @MethodsRules.delayable(b'setPlayerVehicle')
    def setPostProgression(self, vehicleID, itemCDs):
        if self.__playerVehicleID != vehicleID or self.__isSelectionStopped() or self.__state & _States.PROGRESSION:
            return
        vppCache = vehicles.g_cache.postProgression()
        treeID = self.__vehicle.typeDescr.postProgressionTree
        actionCDs = unpackActionCDs(itemCDs, vppCache, treeID)
        self.__extData[_EXT_PROGRESSION_MODS] = getActiveModifications(actionCDs, vppCache, treeID)
        setFeatures(self.__postProgressionState, actionCDs)
        self.__onInitStepCompleted(_States.PROGRESSION)
        return

    @MethodsRules.delayable(b'setPlayerVehicle')
    def setDisabledSwitches(self, vehicleID, groupIDs):
        if self.__playerVehicleID != vehicleID or self.__isSelectionStopped() or self.__state & _States.DISABLED_SWITCHES:
            return
        setDisabledSwitches(self.__postProgressionState, groupIDs)
        self.__onInitStepCompleted(_States.DISABLED_SWITCHES)
        return

    @MethodsRules.delayable(b'setPlayerVehicle')
    def setRespawnReloadFactor(self, vehicleID, reloadFactor):
        if self.__playerVehicleID != vehicleID or self.__isSelectionStopped() or self.__state & _States.RESPAWN:
            return
        self.__extData[_EXT_RESPAWN_BOOST] = reloadFactor
        self.__onInitStepCompleted(_States.RESPAWN)
        return

    @MethodsRules.delayable(b'setPlayerVehicle')
    def setSetups(self, vehicleID, setups):
        if self.__playerVehicleID != vehicleID or self.__isSelectionStopped() or self.__state & _States.SETUPS:
            return
        self.setInvData(setups)
        self.__onInitStepCompleted(_States.SETUPS)
        return

    def setInvData(self, setups):
        self.__invData.update({_SETUP_NAME_TO_LAYOUT[key]: value for key, value in viewitems(setups)})
        return

    @MethodsRules.delayable(b'setPlayerVehicle')
    def setSetupsIndexes(self, vehicleID, setupsIndexes):
        if self.__playerVehicleID != vehicleID or self.__isSelectionStopped():
            return
        self.__invData[b'layoutIndexes'] = setupsIndexes
        updateInvInstalled(self.__invData, setupsIndexes)
        if self.__state & _States.SETUPS_INDEXES:
            self.__updateSetupIndexes()
            return
        self.__onInitStepCompleted(_States.SETUPS_INDEXES)
        return

    def updateLayoutIndexes(self, setupsIndexes):
        self.__invData[b'layoutIndexes'] = setupsIndexes.copy()
        return

    @MethodsRules.delayable(b'setPlayerVehicle')
    def setSiegeState(self, vehicleID, siegeState):
        if self.__playerVehicleID != vehicleID or self.__isSelectionStopped():
            return
        self.__extData[_EXT_SIEGE_STATE_KEY] = siegeState
        if self.__state & _States.SELECTION_STARTED:
            self.__updateSiegeState()
        return

    @MethodsRules.delayable(b'setPlayerVehicle')
    def setVehicleAttrs(self, vehicleID, attrs):
        if not self.isSelectionStarted() or self.__playerVehicleID != vehicleID:
            return
        newFactors = getVehicleFactors(self.__vehicle, isModifySkillProcessors=True)
        newFactors[_EXT_RESPAWN_BOOST] = self.__extData[_EXT_RESPAWN_BOOST]
        newAttrs = dict(attrs)
        newAttrs[b'circularVisionRadius'] = getCircularVisionRadius(self.__vehicle.descriptor, newFactors)
        self.__sessionProvider.shared.feedback.setVehicleAttrs(self.__playerVehicleID, newAttrs)
        return

    def setViewComponents(self, *components):
        if self.__isSelectionStopped():
            return
        self._viewComponents = components
        if self.isSelectionStarted():
            for component in components:
                component.showSetupsView(self.__vehicle, self.__arenaLoaded)

        return

    @MethodsRules.delayable(b'setPlayerVehicle')
    def onCurrentShellUpdate(self, vehicleID):
        if not self.isSelectionStarted() or self.__playerVehicleID != vehicleID:
            return
        self.__updateAmmoCtrlParams(self.__updateGuiVehicle())
        return

    def arenaLoadCompleted(self):
        self.__arenaLoaded = True
        if not self.__settingsCore.getSetting(GAME.SWITCH_SETUPS_IN_LOADING):
            self.__onStartSelection()
        else:
            for component in self._viewComponents:
                component.onArenaLoaded()

            self.__onFiniStepCompleted()
        return

    def invalidatePeriodInfo(self, period, endTime, length, additionalInfo):
        if not self.__isSelectionStopped():
            self.__updatePeriod(period)
        return

    def switchLayout(self, groupID, layoutIdx):
        if self.__sessionProvider.isReplayPlaying:
            return
        else:
            if not self.isSelectionStarted():
                return
            if self.__cooldown.isInProcess(_SWITCH_SETUPS_ACTION):
                return
            if not self.__vehicle.isSetupSwitchActive(groupID):
                return
            if self.__vehicle.postProgression.isPrebattleSwitchDisabled(groupID):
                return
            playerVehicle = BigWorld.entities.get(self.__playerVehicleID)
            if playerVehicle is None:
                return
            self.__cooldown.process(_SWITCH_SETUPS_ACTION)
            playerVehicle.cell.switchSetup(groupID, layoutIdx)
            playSound(Sounds.GAMEPLAY_SETUP_SWITCH)
            return

    def getSlotItem(self, group, layout, slotId):
        if group not in self.__invData:
            return
        else:
            layoutIndex = 0 if not self.__invData[b'layoutIndexes'] else self.__invData[b'layoutIndexes'][layout]
            if layoutIndex < len(self.__invData[group]) and slotId < len(self.__invData[group][layoutIndex]):
                return self.__invData[group][layoutIndex][slotId]
            return

    def __isSelectionAvailable(self):
        if not self.__hasValidCaps:
            return False
        for groupID in TANK_SETUP_GROUPS:
            if self.__vehicle.isSetupSwitchActive(groupID) and not self.__vehicle.postProgression.isPrebattleSwitchDisabled(groupID):
                return True

        return False

    def __isSelectionStopped(self):
        return bool(self.__state & _States.SELECTION_STOPPED)

    def __isSelectionShouldEnded(self):
        if self.__settingsCore.getSetting(GAME.SWITCH_SETUPS_IN_LOADING):
            return self.__arenaLoaded and self.__isSelectionStopped()
        return self.__isSelectionStopped()

    def __isSelectionShouldStarted(self):
        if self.__settingsCore.getSetting(GAME.SWITCH_SETUPS_IN_LOADING):
            return self.__state & _States.INIT_COMPLETE and self.__isSelectionAvailable()
        return self.__state & _States.INIT_COMPLETE and self.__isSelectionAvailable() and self.isArenaLoaded()

    def __onInitStepCompleted(self, stepState):
        if self.__state & _States.INIT_COMPLETE:
            return
        self.__updateState(stepState)
        if self.__state & _States.INIT_READY == _States.INIT_READY:
            shellsCDs = [shell.intCD for shell in self.__vehicle.gun.defaultAmmo]
            shellsLayoutKey = (
             self.__vehicle.turret.intCD, self.__vehicle.gun.intCD)
            self.__invData[b'shells'] = getInstalledShells(shellsCDs, self.__invData[TankSetupLayouts.SHELLS])
            self.__invData[TankSetupLayouts.SHELLS] = {shellsLayoutKey: (self.__invData[TankSetupLayouts.SHELLS])}
            self.__updateGuiVehicle()
            self.__updateState(_States.INIT_COMPLETE)
        self.__onStartSelection()
        return

    def __onFiniStepCompleted(self):
        if self.__state & _States.SELECTION_ENDED:
            return
        if self.__isSelectionShouldEnded():
            self.__updateState(_States.SELECTION_ENDED)
        return

    def __onStartSelection(self):
        if self.__state & _States.SELECTION_STARTED or self.__isSelectionStopped():
            return
        if self.__isSelectionShouldStarted():
            self.__updateState(_States.SELECTION_STARTED)
        return

    def __updateAmmoCtrl(self):
        self.__sessionProvider.shared.ammo.updateForNewSetup(self.__playerVehicleID, self.__vehicle.descriptor, self.__vehicle.shells.installed.getItems())
        return

    def __updateAmmoCtrlParams(self, factors):
        ammoCtrl = self.__sessionProvider.shared.ammo
        quantity = ammoCtrl.getShellsQuantityLeft()
        hasAmmo = any(shell.count for shell in self.__vehicle.shells.installed.getItems())
        reloadTime = getFirstReloadTime(self.__vehicle.descriptor, factors, shellsAmount=quantity) if hasAmmo else 0.0
        ammoCtrl.setGunReloadTime(-1, reloadTime, skipAutoLoader=True)
        return

    def __updateFeedbackParams(self, factors):
        feedbackCtrl = self.__sessionProvider.shared.feedback
        newAttrs = feedbackCtrl.getVehicleAttrs()
        newAttrs[b'circularVisionRadius'] = getCircularVisionRadius(self.__vehicle.descriptor, factors)
        feedbackCtrl.setVehicleAttrs(self.__playerVehicleID, newAttrs)
        return

    def __updateGuiVehicle(self):
        invData, extData = self.__invData.copy(), self.__extData.copy()
        vehicle = self.__vehicle = Vehicle(strCompactDescr=self.__vehicle.strCD, extData=extData, invData=invData)
        vehicle.installPostProgressionItem(self.__itemsFactory.createVehPostProgression(vehicle.compactDescr, self.__extData[EXT_DATA_PROGRESSION_KEY], vehicle.typeDescr))
        vehicle.descriptor.onSiegeStateChanged(self.__extData[_EXT_SIEGE_STATE_KEY])
        vehicle.descriptor.installModifications(self.__extData[_EXT_PROGRESSION_MODS], rebuildAttrs=False)
        vehicle.descriptor.installEnhancements(self.__extData[_EXT_ENHANCEMENTS_KEY], rebuildAttrs=False)
        vehicle.descriptor.installOptDevsSequence(vehicle.optDevices.installed.getIntCDs())
        newFactors = getVehicleFactors(vehicle, isModifySkillProcessors=True)
        newFactors[_EXT_RESPAWN_BOOST] = self.__extData[_EXT_RESPAWN_BOOST]
        return newFactors

    def __updatePeriod(self, period):
        if period >= ARENA_PERIOD.BATTLE:
            self.stopSelection()
        return

    def __updateState(self, addMask):
        if addMask == _States.SELECTION_STARTED:
            for component in self._viewComponents:
                component.showSetupsView(self.__vehicle, self.__arenaLoaded)

            factors = self.__updateGuiVehicle()
            self.__updateAmmoCtrl()
            self.__updateAmmoCtrlParams(factors)
        if addMask == _States.SELECTION_STOPPED and self.isSelectionStarted():
            self.__state |= _States.SELECTION_AWAIT_HIDING
            self.__state &= ~_States.SELECTION_STARTED
            for component in self._viewComponents:
                component.stopSetupsSelection()

        if addMask == _States.SELECTION_ENDED and self.__state & _States.SELECTION_AWAIT_HIDING:
            self.__state &= ~_States.SELECTION_AWAIT_HIDING
            for component in self._viewComponents:
                component.hideSetupsView()

        self.__state |= addMask
        _logger.debug(b'[PrebattleSetupsController] addMask %s modifiedState %s', addMask, self.__state)
        return

    def __updateSetupIndexes(self):
        newFactors = self.__updateGuiVehicle()
        self.__updateAmmoCtrl()
        self.__updateAmmoCtrlParams(newFactors)
        self.__updateFeedbackParams(newFactors)
        for component in self._viewComponents:
            component.updateVehicleParams(self.__vehicle, newFactors)
            component.updateVehicleSetups(self.__vehicle)

        if self.__sessionProvider.isReplayPlaying:
            playSound(Sounds.GAMEPLAY_SETUP_SWITCH)
        return

    def __updateSiegeState(self):
        newFactors = self.__updateGuiVehicle()
        self.__updateAmmoCtrlParams(newFactors)
        self.__updateFeedbackParams(newFactors)
        for component in self._viewComponents:
            component.updateVehicleParams(self.__vehicle, newFactors)

        return

    @property
    def __postProgressionState(self):
        state = self.__extData.get(EXT_DATA_PROGRESSION_KEY)
        if state is None:
            self.__extData[EXT_DATA_PROGRESSION_KEY] = state = VehicleState()
        return state
