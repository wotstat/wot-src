import math, BigWorld
from gui.Scaleform.daapi.view.meta.EpicMissionsPanelMeta import EpicMissionsPanelMeta
from helpers import dependency
from skeletons.gui.battle_session import IBattleSessionProvider
from helpers import time_utils
from gui.battle_control.controllers.epic_missions_ctrl import PlayerMission
from helpers.CallbackDelayer import CallbackDelayer

class EpicMissionsPanel(EpicMissionsPanelMeta, CallbackDelayer):
    sessionProvider = dependency.descriptor(IBattleSessionProvider)

    def __init__(self):
        EpicMissionsPanelMeta.__init__(self)
        CallbackDelayer.__init__(self)
        self.__nearestHQ = None
        self.__currentEndTime = 0
        self.__currentMission = None
        return

    def start(self):
        return

    def _populate(self):
        EpicMissionsPanelMeta._populate(self)
        ctrl = self.sessionProvider.dynamic.missions
        if ctrl:
            ctrl.onPlayerMissionUpdated += self.__onPlayerMissionUpdated
            ctrl.onPlayerMissionReset += self.__onPlayerMissionReset
            ctrl.onPlayerMissionTimerSet += self.__onPlayerMissionTimerSet
            ctrl.onNearestObjectiveChanged += self.__onNearestObjectiveChanged
        return

    def _dispose(self):
        ctrl = self.sessionProvider.dynamic.missions
        if ctrl:
            ctrl.onPlayerMissionUpdated -= self.__onPlayerMissionUpdated
            ctrl.onPlayerMissionReset -= self.__onPlayerMissionReset
            ctrl.onPlayerMissionTimerSet -= self.__onPlayerMissionTimerSet
            ctrl.onNearestObjectiveChanged -= self.__onNearestObjectiveChanged
        self.__killTimeCallback()
        EpicMissionsPanelMeta._dispose(self)
        CallbackDelayer.destroy(self)
        return

    def __killTimeCallback(self):
        self.stopCallback(self.__tick)
        self.as_setMissionDescriptionValueS(b'')
        return

    def __startCountdownTimer(self):
        self.__killTimeCallback()
        diffTime = self.__currentEndTime - BigWorld.serverTime()
        if diffTime >= 0:
            timeStr = time_utils.getTimeLeftFormat(diffTime)
            self.as_setMissionDescriptionValueS(timeStr)
            self.delayCallback(0, self.__tick)
        return

    def __tick(self):
        diffTime = math.ceil(self.__currentEndTime - BigWorld.serverTime())
        if diffTime >= 0:
            timeStr = time_utils.getTimeLeftFormat(diffTime)
            self.as_setMissionDescriptionValueS(timeStr)
            return 1
        self.as_setMissionDescriptionValueS(b'')
        return -1

    def __onPlayerMissionUpdated(self, mission, additionalDescription=None):
        self.__updatePrimaryMission(mission.generateData())
        if additionalDescription is not None:
            self.as_setMissionDescriptionValueS(additionalDescription)
        return

    def __onPlayerMissionReset(self):
        self.__updatePrimaryMission(PlayerMission().generateData())
        return

    def __updatePrimaryMission(self, newMission):
        if self.__currentMission != newMission:
            self.__currentMission = newMission
            self.as_setPrimaryMissionS(newMission)
        return

    def __onPlayerMissionTimerSet(self, timeStamp):
        if timeStamp > 0:
            self.__currentEndTime = timeStamp
            self.__startCountdownTimer()
        else:
            self.__currentEndTime = 0
            self.__killTimeCallback()
        return

    def __onNearestObjectiveChanged(self, objID, objDistance):
        if self.__nearestHQ != objID:
            self.__nearestHQ = objID
            self.as_setNearestHQS(self.__nearestHQ)
        return
