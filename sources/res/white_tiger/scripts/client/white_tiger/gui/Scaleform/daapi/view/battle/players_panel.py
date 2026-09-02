from __future__ import absolute_import
from typing import TYPE_CHECKING
import BigWorld
from helpers import time_utils
from debug_utils import LOG_ERROR_DEV
from gui.battle_control.arena_info.settings import INVALIDATE_OP
from white_tiger.gui.Scaleform.daapi.view.meta.WhiteTigerPlayersPanelMeta import WhiteTigerPlayersPanelMeta
from white_tiger.gui.wt_event_helpers import isBoss
from white_tiger.cgf_components.wt_helpers import getBattleStateComponent, getPlasmaBonusComponent, isBossBot
from helpers import dependency
from skeletons.gui.battle_session import IBattleSessionProvider
from account_helpers.settings_core import settings_constants
from white_tiger_common.wt_constants import WTGeneratorState
if TYPE_CHECKING:
    from gui.battle_control.arena_info.interfaces import IBattleFieldController

class WhiteTigerPlayersPanel(WhiteTigerPlayersPanelMeta):
    __sessionProvider = dependency.descriptor(IBattleSessionProvider)

    def __init__(self):
        super(WhiteTigerPlayersPanel, self).__init__()
        self.__captureTimePerGenerator = {}
        self.__lastCapturedGeneratorIndex = -1
        return

    def _populate(self):
        super(WhiteTigerPlayersPanel, self)._populate()
        self.as_setIsBossS(self.__isBossPlayer())
        battleStateComponent = getBattleStateComponent()
        if battleStateComponent:
            battleStateComponent.onGeneratorCapture += self.__onGeneratorCapture
            battleStateComponent.onGeneratorStopCapture += self.__onGeneratorStopCapture
            battleStateComponent.onGeneratorLocked += self.__onGeneratorLocked
            battleStateComponent.onGeneratorsLeftInitialize += self.__onGeneratorDestroyed
            battleStateComponent.onGeneratorDestroyed += self.__onGeneratorDestroyed
            battleStateComponent.onUpdateCamp += self.__onUpdateCamp
            battleStateComponent.onShieldDowntime += self.__onShieldDowntime
            battleFieldCtrl = self.guiSessionProvider.dynamic.battleField
            if battleFieldCtrl:
                battleFieldCtrl.onSpottedStatusChanged += self.__updateSpottedStatus
            else:
                LOG_ERROR_DEV(b'WhiteTigerPlayersPanel: _populate: Could not find battleFieldCtrl')
            plasmaComponent = getPlasmaBonusComponent()
            if plasmaComponent:
                plasmaComponent.onPlasmaChanged += self.__onPlasmaChanged
            else:
                LOG_ERROR_DEV(b'WhiteTigerPlayersPanel: _populate: Could not find plasmaBonusComponent')
        self.as_setColorBlindS(self.settingsCore.getSetting(b'isColorBlind'))
        self.settingsCore.onSettingsChanged += self.__onSettingsChanged
        return

    def _dispose(self):
        battleStateComponent = getBattleStateComponent()
        if battleStateComponent:
            battleStateComponent.onGeneratorCapture -= self.__onGeneratorCapture
            battleStateComponent.onGeneratorStopCapture -= self.__onGeneratorStopCapture
            battleStateComponent.onGeneratorLocked -= self.__onGeneratorLocked
            battleStateComponent.onGeneratorDestroyed -= self.__onGeneratorDestroyed
            battleStateComponent.onGeneratorsLeftInitialize -= self.__onGeneratorDestroyed
            battleStateComponent.onUpdateCamp -= self.__onUpdateCamp
            battleStateComponent.onShieldDowntime -= self.__onShieldDowntime
            battleFieldCtrl = self.guiSessionProvider.dynamic.battleField
            if battleFieldCtrl:
                battleFieldCtrl.onSpottedStatusChanged -= self.__updateSpottedStatus
            else:
                LOG_ERROR_DEV(b'WhiteTigerPlayersPanel: _onDispose: Could not find battleFieldCtrl')
            plasmaComponent = getPlasmaBonusComponent()
            if plasmaComponent:
                plasmaComponent.onPlasmaChanged -= self.__onPlasmaChanged
            else:
                LOG_ERROR_DEV(b'WhiteTigerPlayersPanel: _onDispose: Could not find plasmaBonusComponent')
        self.settingsCore.onSettingsChanged -= self.__onSettingsChanged
        super(WhiteTigerPlayersPanel, self)._dispose()
        return

    def updateVehicleHealth(self, vehicleID, newHealth, maxHealth):
        newHealth = max(0, newHealth)
        if isBossBot(vehicleID):
            self.as_updateBossBotHpS(vehicleID, maxHealth, newHealth)
        else:
            super(WhiteTigerPlayersPanel, self).updateVehicleHealth(vehicleID, newHealth, maxHealth)
        return

    def updateDeadVehicles(self, aliveAllies, deadAllies, aliveEnemies, deadEnemies):
        for vehicleID in deadEnemies | deadAllies:
            if vehicleID in aliveAllies | aliveEnemies:
                continue
            if isBossBot(vehicleID):
                arenaDP = self.sessionProvider.getArenaDP()
                vInfo = arenaDP.getVehicleInfo(vehicleID)
                self.as_updateBossBotHpS(vehicleID, vInfo.vehicleType.maxHealth, 0)
            else:
                self.as_setPlayerHPS(vehicleID in deadAllies, vehicleID, 0)

        return

    def __updateSpottedStatus(self, data, arenaDP):
        for flags, vStatsVO in data:
            if flags == INVALIDATE_OP.VEHICLE_STATS:
                vehicleID = vStatsVO.vehicleID
                if isBossBot(vehicleID):
                    self.as_setBossBotSpottedS(vehicleID, vStatsVO.spottedStatus)

        return

    def updateCamp(self, campID, vInfos):
        ctrl = self.sessionProvider.dynamic.battleField
        for vInfo in vInfos:
            currentHealth = vInfo.vehicleType.maxHealth
            if ctrl is not None:
                if vInfo.isAlive():
                    healthInfo = ctrl.getVehicleHealthInfo(vInfo.vehicleID)
                    if healthInfo is not None:
                        currentHealth = healthInfo[0]
                else:
                    currentHealth = 0
            botInfo = {b'typeVehicle': (vInfo.vehicleType.classTag), b'hpMax': (vInfo.vehicleType.maxHealth), 
               b'hpCurrent': currentHealth, 
               b'vehID': (vInfo.vehicleID), 
               b'vehicleIcon': (vInfo.vehicleType.iconName), 
               b'campIndex': campID, 
               b'vehicleGuiName': (vInfo.vehicleType.guiName)}
            self.as_setBossBotInfoS(botInfo)

        return

    def __onUpdateCamp(self, generatorID, vehicleIDs):
        self.destroyCamp(generatorID)
        vInfos = []
        arenaDP = self.__sessionProvider.getArenaDP()
        for vID in vehicleIDs:
            vInfo = arenaDP.getVehicleInfo(vID)
            if vInfo.vehicleID == vID:
                vInfos.append(vInfo)

        self.updateCamp(generatorID, vInfos)
        self.updateCampInfoStatus(generatorID)
        return

    def destroyCamp(self, campID):
        self.as_clearBossBotCampS(campID)
        return

    def updateCampInfoStatus(self, campID):
        self.as_updateCampInfoStatusS(campID)
        return

    def _handleNextMode(self, _):
        return

    def __isBossPlayer(self):
        vInfo = self.sessionProvider.getCtx().getVehicleInfo(BigWorld.player().playerVehicleID)
        tags = vInfo.vehicleType.tags
        return isBoss(tags)

    def __onGeneratorCapture(self, index, progress, timeLeft, numInvaders, isBlocked):
        if self.__captureTimePerGenerator.get(index) is None:
            self.__captureTimePerGenerator[index] = {}
        self.__captureTimePerGenerator[index][b'timeLeft'] = timeLeft
        self.as_updateGeneratorCaptureTimerS(index, timeLeft, progress, numInvaders, 1)
        self.as_updateGeneratorDownTimeS(index, b'')
        return

    def __onGeneratorStopCapture(self, index, state):
        if state == WTGeneratorState.CAPTURED:
            self.as_setIsDestroyedS(index)
            self.__lastCapturedGeneratorIndex = index
            return
        if state == WTGeneratorState.BLOCKED:
            self.as_lockGeneratorS(index, True)
        if not self.__captureTimePerGenerator.get(index):
            return
        self.as_resetGeneratorCaptureTimerS(index)
        return

    def __onShieldDowntime(self, _, remainingTime):
        timeText = time_utils.getTimeLeftFormat(remainingTime)
        self.as_updateGeneratorDownTimeS(self.__lastCapturedGeneratorIndex, timeText)
        return

    def __onGeneratorDestroyed(self, generatorsLeft):
        if generatorsLeft == 0:
            self.as_setAllBossBotCampsOfflineS()
            self.__captureTimePerGenerator.clear()
        return

    def __onGeneratorLocked(self, generatorID, isLocked, _, __, ___):
        self.as_lockGeneratorS(generatorID, isLocked)
        self.updateCampInfoStatus(generatorID)
        return

    def __onSettingsChanged(self, diff):
        if settings_constants.GRAPHICS.COLOR_BLIND in diff:
            self.as_setColorBlindS(self.settingsCore.getSetting(b'isColorBlind'))
        return

    def __onPlasmaChanged(self, plasmaDict):
        for vehId, value in plasmaDict.items():
            self.as_setPlasmaForVehiclesS(vehId, value)

        return
