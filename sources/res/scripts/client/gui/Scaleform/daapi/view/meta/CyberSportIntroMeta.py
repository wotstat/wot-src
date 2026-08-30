from gui.Scaleform.daapi.view.lobby.rally.BaseRallyIntroView import BaseRallyIntroView

class CyberSportIntroMeta(BaseRallyIntroView):

    def requestVehicleSelection(self):
        self._printOverrideError(b'requestVehicleSelection')
        return

    def startAutoMatching(self):
        self._printOverrideError(b'startAutoMatching')
        return

    def showSelectorPopup(self):
        self._printOverrideError(b'showSelectorPopup')
        return

    def showStaticTeamStaff(self):
        self._printOverrideError(b'showStaticTeamStaff')
        return

    def as_setSelectedVehicleS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setSelectedVehicle(data)
        return

    def as_setTextsS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setTexts(data)
        return

    def as_setNoVehiclesS(self, warnTooltip):
        if self._isDAAPIInited():
            return self.flashObject.as_setNoVehicles(warnTooltip)
        return
