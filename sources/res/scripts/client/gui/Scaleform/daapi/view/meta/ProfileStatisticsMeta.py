from gui.Scaleform.daapi.view.lobby.profile.ProfileSection import ProfileSection

class ProfileStatisticsMeta(ProfileSection):

    def getData(self, data):
        self._printOverrideError(b'getData')
        return

    def setSeason(self, seasonId):
        self._printOverrideError(b'setSeason')
        return

    def as_updatePlayerStatsBtnS(self, isVisible):
        if self._isDAAPIInited():
            return self.flashObject.as_updatePlayerStatsBtn(isVisible)
        return
