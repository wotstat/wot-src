from __future__ import absolute_import
import typing
from helpers.time_utils import ONE_MINUTE
import BattleReplay, BigWorld
from gui.Scaleform.daapi.view.battle.pve_base.base.pve_hud_widget import SeveralItemsPveHudWidget
from gui.Scaleform.daapi.view.battle.pve_base.secondary_objectives.settings_model import SecondaryObjectiveServerModel
from gui.Scaleform.daapi.view.battle.pve_base.secondary_objectives.state_machine.machine import SecondaryObjectiveStateMachine
from gui.Scaleform.daapi.view.meta.PveSecondaryObjectivesMeta import PveSecondaryObjectivesMeta
from pve_battle_hud import WidgetType, SecondaryObjectiveState

class PveSecondaryObjectives(SeveralItemsPveHudWidget, PveSecondaryObjectivesMeta):
    MAX_ITEMS_COUNT = 3

    def __init__(self):
        super(PveSecondaryObjectives, self).__init__(widgetType=WidgetType.SECONDARY_OBJECTIVE, stateMachineClass=SecondaryObjectiveStateMachine, serverSettingsModel=SecondaryObjectiveServerModel)
        return

    def addObjective(self, serverSettings, clientSettings):
        hasProgressBar = serverSettings.progress is not None
        newObjective = {b'id': (serverSettings.id), 
           b'icon': (clientSettings.icon), 
           b'isTimerEnable': (bool(serverSettings.timer)), 
           b'title': (clientSettings.getHeader(serverSettings.params)), 
           b'description': (clientSettings.getSubheader()), 
           b'isVisibleProgressBar': hasProgressBar, 
           b'progressBarValue': (serverSettings.progress * 100 if hasProgressBar else 0)}
        self.as_addObjectS(newObjective)
        self.updateProgress(serverSettings.id, serverSettings.progress)
        return

    def removeObjective(self, objectiveId, hideType):
        self.as_removeObjectS(objectiveId, hideType)
        return

    def updateTimer(self, objectiveId, timerValue, isWarning=False):
        timerValue = max(timerValue, 0)
        minutes, seconds = divmod(int(timerValue), ONE_MINUTE)
        formattedTime = (b'{:02d}:{:02d}').format(minutes, seconds)
        self.as_updateTimeS(objectiveId, formattedTime, isWarning)
        return

    def updateProgress(self, objectiveId, progress):
        if progress is not None:
            self.as_setProgressBarValueS(objectiveId, progress * 100)
        return

    def updateTitle(self, objectiveId, title):
        self.as_setTitleS(objectiveId, title)
        return

    def _onPrebattlePeriod(self):
        if BattleReplay.isPlaying():
            self.as_clearS()
        return

    def _getStateToRestore(self, serverSettings):
        serverState = serverSettings.state
        timeLeft = serverSettings.finishTime - BigWorld.serverTime()
        completeStates = [SecondaryObjectiveState.SUCCESS, SecondaryObjectiveState.FAILURE,
         SecondaryObjectiveState.DISAPPEARANCE, SecondaryObjectiveState.HIDDEN]
        if serverState in completeStates or serverSettings.finishTime and timeLeft <= 0:
            return None
        if serverState in [SecondaryObjectiveState.APPEARANCE, SecondaryObjectiveState.REGULAR,
         SecondaryObjectiveState.RESTORED]:
            return SecondaryObjectiveState.RESTORED
        else:
            return serverState
