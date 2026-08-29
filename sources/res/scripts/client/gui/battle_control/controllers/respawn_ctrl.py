from collections import namedtuple, defaultdict
from itertools import izip
import BigWorld, Event
from constants import RESPAWN_TYPES, REQUEST_COOLDOWN
from gui.battle_control.battle_constants import BATTLE_CTRL_ID
from gui.battle_control.view_components import ViewComponentsController
from gui.veh_post_progression.battle_cooldown_manager import BattleCooldownManager
from helpers import dependency
from items import vehicles
from post_progression_common import unpackVehSetupsIndexes
from PlayerEvents import g_playerEvents
from skeletons.gui.battle_session import IBattleSessionProvider
from skeletons.gui.game_control import IVehiclePostProgressionController
_Vehicle = namedtuple(b'_Vehicle', (b'intCD', b'strCD', b'battleAbilities', b'crewDescrs', b'customRoleSlotTypeId', b'settings', b'vehPostProgression', b'vehSetups', b'vehSetupsIndexes', b'disabledSwitchGroupIDs'))
_RespawnInfo = namedtuple(b'_RespawnInfo', (b'vehicleID', b'respawnTime', b'respawnType', b'autoRespawnTime', b'respawnZones', b'chosenRespawnZone', b'vehSetupsIndexes'))

class IRespawnView(object):

    def start(self, vehs, isLimited):
        return

    def show(self, selectedID, vehs, cooldowns, limits=0):
        return

    def hide(self):
        return

    def updateTimer(self, timeLeft, vehs, cooldowns, limits=0):
        return

    def setLimits(self, respawnLimits):
        return

    def setBattleCtx(self, battleCtx):
        return

    def setRespawnInfoExt(self, vehInfo, setupIndexes):
        return


_SWITCH_SETUPS_ACTION = 0

class RespawnsController(ViewComponentsController):
    __slots__ = (b'__weakref__', b'__isUIInited', b'__vehicles', b'__cooldowns', b'__respawnInfo', b'__timerCallback', b'_eManager', b'onRespawnVisibilityChanged', b'onVehicleDeployed', b'onRespawnInfoUpdated', b'onPlayerRespawnLivesUpdated', b'onTeamRespawnLivesRestored', b'onRespawnVehiclesUpdated', b'__isUiShown', b'__isShowUiAllowed', b'__limits', b'__playerRespawnLives', b'__battleCtx', b'__setupsIndexes', b'__cooldownsManager')
    __postProgressionCtrl = dependency.descriptor(IVehiclePostProgressionController)
    __battleSession = dependency.descriptor(IBattleSessionProvider)
    showUiAllowed = property((lambda self: self.__isShowUiAllowed), (lambda self, value: self.__setShowUiAllowed(value)))
    respawnInfo = property((lambda self: self.__respawnInfo))
    playerLives = property((lambda self: self.__playerRespawnLives))
    vehicles = property((lambda self: self.__vehicles))

    def __init__(self, setup):
        super(RespawnsController, self).__init__()
        self.__isUIInited = False
        self.__vehicles = {}
        self.__cooldowns = {}
        self.__limits = {}
        self.__respawnInfo = None
        self.__timerCallback = None
        self.__isUiShown = False
        self.__isShowUiAllowed = False
        self.__playerRespawnLives = -1
        self.__battleCtx = setup.battleCtx
        self.__setupsIndexes = defaultdict(dict)
        self.__cooldownsManager = BattleCooldownManager()
        self._eManager = Event.EventManager()
        self.onRespawnVisibilityChanged = Event.Event(self._eManager)
        self.onVehicleDeployed = Event.Event(self._eManager)
        self.onRespawnInfoUpdated = Event.Event(self._eManager)
        self.onPlayerRespawnLivesUpdated = Event.Event(self._eManager)
        self.onTeamRespawnLivesRestored = Event.Event(self._eManager)
        self.onRespawnVehiclesUpdated = Event.Event(self._eManager)
        return

    def getControllerID(self):
        return BATTLE_CTRL_ID.RESPAWN

    def startControl(self):
        g_playerEvents.onRoundFinished += self.__onRoundFinished
        return

    def stopControl(self):
        g_playerEvents.onRoundFinished -= self.__onRoundFinished
        self.__stopTimer()
        self.clearViewComponents()
        self.__vehicles = None
        self.__cooldowns = None
        self.__respawnInfo = None
        self.__limits = None
        self.__battleCtx = None
        self.__setupsIndexes = None
        self.__cooldownsManager.reset(_SWITCH_SETUPS_ACTION)
        self.__cooldownsManager = None
        return

    def setViewComponents(self, *components):
        super(RespawnsController, self).setViewComponents(*components)
        if not self._viewComponents:
            return
        self.__refresh()
        for viewCmp in self._viewComponents:
            viewCmp.setBattleCtx(self.__battleCtx)

        return

    def respawnPlayer(self):
        BigWorld.player().base.respawnController_performRespawn()
        return

    def chooseVehicleForRespawn(self, intCD):
        self.__updateRespawnInfoExt(intCD)
        BigWorld.player().base.respawnController_chooseVehicleForRespawn(intCD)
        return

    def switchVehSetupsLayout(self, vehCD, groupID, layoutIdx):
        if self.__battleSession.isReplayPlaying:
            return
        if self.__cooldownsManager.isInProcess(_SWITCH_SETUPS_ACTION):
            return
        self.__setupsIndexes[vehCD][groupID] = layoutIdx
        self.__updateRespawnInfoExt(vehCD)
        self.__cooldownsManager.process(_SWITCH_SETUPS_ACTION, REQUEST_COOLDOWN.POST_PROGRESSION_CELL)
        BigWorld.player().base.respawnController_switchSetup(vehCD, groupID, layoutIdx)
        return

    def movingToRespawn(self):
        self.__respawnInfo = None
        self.__stopTimer()
        return

    def spawnVehicle(self, _):
        if BigWorld.player().isVehicleAlive:
            self.__respawnInfo = None
            self.onVehicleDeployed()
        self.__hide()
        return

    def updateRespawnVehicles(self, vehsList):
        self.__vehicles = {}
        battleAbilities = {vehTypeCompDescr: compDescrList for vehTypeCompDescr, compDescrList in izip(BigWorld.player().ammoViews[b'vehTypeCompDescrs'], BigWorld.player().ammoViews[b'compDescrs'])}
        for v in vehsList:
            descr = vehicles.getVehicleType(v[b'compDescr'])
            self.__vehicles[descr.compactDescr] = _Vehicle(descr.compactDescr, v[b'compDescr'], battleAbilities.get(descr.compactDescr, ()), v[b'crewCompactDescrs'], v[b'customRoleSlotTypeId'], v[b'settings'], v[b'vehPostProgression'], v[b'vehSetups'], unpackVehSetupsIndexes(list(v[b'vehSetupsIndexes'])), v[b'vehDisabledSetupSwitches'])

        self.onRespawnVehiclesUpdated(self.__vehicles)
        if self.__respawnInfo is not None and self.__respawnInfo.vehicleID in self.__vehicles:
            self.__updateRespawnInfoExt(self.__respawnInfo.vehicleID)
        return

    def updateRespawnCooldowns(self, cooldowns):
        self.__cooldowns = cooldowns
        return

    def updateRespawnInfo(self, respawnInfo):
        intCD = vehicles.getVehicleTypeCompactDescr(respawnInfo[b'compDescr'])
        self.__respawnInfo = _RespawnInfo(intCD, respawnInfo[b'manualRespawnPiT'], respawnInfo[b'respawnType'], respawnInfo[b'autoRespawnPiT'], respawnInfo[b'respawnZones'], respawnInfo[b'chosenRespawnZone'], unpackVehSetupsIndexes(list(respawnInfo[b'vehSetupsIndexes'])))
        self.__setupsIndexes[intCD].update(self.__respawnInfo.vehSetupsIndexes)
        self.__refresh()
        self.onRespawnInfoUpdated(self.__respawnInfo)
        if self.__vehicles is not None and intCD in self.__vehicles:
            self.__updateRespawnInfoExt(intCD)
        return

    def updateVehicleLimits(self, respawnLimits):
        self.__limits = respawnLimits
        if not self._viewComponents:
            return
        for viewCmp in self._viewComponents:
            viewCmp.setLimits(respawnLimits)

        return

    def updatePlayerRespawnLives(self, respawnLives):
        self.__playerRespawnLives = respawnLives
        self.onPlayerRespawnLivesUpdated(respawnLives)
        return

    def restoredTeamRespawnLives(self, teams):
        self.onTeamRespawnLivesRestored(teams)
        return

    def isRespawnVisible(self):
        return self.__isUiShown

    def getLimits(self):
        return self.__limits

    def _show(self):
        if not self._viewComponents:
            return
        if not self.__isUIInited:
            self.__isUIInited = True
            isLimited = self.__respawnInfo.respawnType == RESPAWN_TYPES.LIMITED
            for viewCmp in self._viewComponents:
                viewCmp.start(self.__vehicles, isLimited)

        for viewCmp in self._viewComponents:
            viewCmp.show(self.__respawnInfo.vehicleID, self.__vehicles, self.__cooldowns, self.__limits)

        self.__isUiShown = True
        self.__startTimer()
        self.onRespawnVisibilityChanged(True)
        self.__startTimer()
        self.__isUiShown = True
        return

    def __setShowUiAllowed(self, value):
        self.__isShowUiAllowed = value
        self.__refresh()
        return

    def __onRoundFinished(self, *args):
        self.__hide()
        return

    def __refresh(self):
        if self.__respawnInfo is None or self._viewComponents is None:
            return
        if self.__respawnInfo is not None and not self.__isUiShown and self.__isShowUiAllowed:
            self._show()
        elif self.__isUiShown and not self.__isShowUiAllowed:
            self.__hide()
        elif self.__isUiShown:
            self.__stopTimer()
            self.__startTimer()
        return

    def __hide(self):
        if not self.__isUiShown:
            return
        self.__stopTimer()
        self.__setupsIndexes.clear()
        self.__cooldownsManager.reset(_SWITCH_SETUPS_ACTION)
        if not self._viewComponents:
            return
        for viewCmp in self._viewComponents:
            viewCmp.hide()
            self.__isUiShown = False
            self.onRespawnVisibilityChanged(False)

        return

    def __startTimer(self):
        self.__timerCallback = None
        if self.__respawnInfo is None:
            return
        else:
            respawnTime = self.__respawnInfo.respawnTime
            timeLeft = max(0, respawnTime - BigWorld.serverTime())
            autoRespawnTime = self.__respawnInfo.autoRespawnTime
            autoTimeLeft = max(0, autoRespawnTime - BigWorld.serverTime())
            for viewCmp in self._viewComponents:
                viewCmp.updateTimer([timeLeft, autoTimeLeft], self.__vehicles, self.__cooldowns, self.__limits)

            if timeLeft > 0 or autoTimeLeft > 0:
                self.__timerCallback = BigWorld.callback(1, self.__startTimer)
            return

    def __stopTimer(self):
        if self.__timerCallback is not None:
            BigWorld.cancelCallback(self.__timerCallback)
            self.__timerCallback = None
        return

    def __updateRespawnInfoExt(self, intCD):
        for component in self._viewComponents:
            component.setRespawnInfoExt(self.__vehicles[intCD], self.__setupsIndexes[intCD])

        return
