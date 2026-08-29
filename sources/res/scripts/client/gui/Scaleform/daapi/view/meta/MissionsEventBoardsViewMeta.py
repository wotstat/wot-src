from gui.Scaleform.daapi.view.lobby.missions.regular.missions_page import ElenMissionView

class MissionsEventBoardsViewMeta(ElenMissionView):

    def openBoardView(self):
        self._printOverrideError(b'openBoardView')
        return

    def participateClick(self, eventID):
        self._printOverrideError(b'participateClick')
        return

    def orderClick(self, eventID):
        self._printOverrideError(b'orderClick')
        return

    def techniqueClick(self, eventID):
        self._printOverrideError(b'techniqueClick')
        return

    def awardClick(self, eventID):
        self._printOverrideError(b'awardClick')
        return

    def registrationClick(self, eventID):
        self._printOverrideError(b'registrationClick')
        return

    def serverClick(self, eventID, server):
        self._printOverrideError(b'serverClick')
        return

    def expand(self, id, value):
        self._printOverrideError(b'expand')
        return

    def as_setMaintenanceS(self, visible, message1, message2, buttonLabel):
        if self._isDAAPIInited():
            return self.flashObject.as_setMaintenance(visible, message1, message2, buttonLabel)
        return

    def as_setPlayFadeInTweenEnabledS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setPlayFadeInTweenEnabled(value)
        return
