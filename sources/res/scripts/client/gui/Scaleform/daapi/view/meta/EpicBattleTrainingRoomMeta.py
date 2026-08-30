from gui.Scaleform.daapi.view.lobby.trainings.TrainingRoomBase import TrainingRoomBase

class EpicBattleTrainingRoomMeta(TrainingRoomBase):

    def onChangeTeamLane(self, accID, team, lane):
        self._printOverrideError(b'onChangeTeamLane')
        return

    def onSwapTeamLane(self, fromTeam, fromLane, toTeam, toLane):
        self._printOverrideError(b'onSwapTeamLane')
        return
