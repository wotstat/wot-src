from gui.Scaleform.daapi.view.meta.BaseMissionDetailsContainerViewMeta import BaseMissionDetailsContainerViewMeta

class PersonalMissionDetailsContainerViewMeta(BaseMissionDetailsContainerViewMeta):

    def useSheet(self, eventID):
        self._printOverrideError(b'useSheet')
        return

    def startMission(self, eventID):
        self._printOverrideError(b'startMission')
        return

    def retryMission(self, eventID):
        self._printOverrideError(b'retryMission')
        return

    def discardMission(self, eventID):
        self._printOverrideError(b'discardMission')
        return

    def obtainAward(self, eventID):
        self._printOverrideError(b'obtainAward')
        return

    def onPauseClick(self, eventID):
        self._printOverrideError(b'onPauseClick')
        return
