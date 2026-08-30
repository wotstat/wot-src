from gui.Scaleform.daapi.view.lobby.profile.ProfileSummary import ProfileSummary

class ProfileSummaryWindowMeta(ProfileSummary):

    def openClanStatistic(self):
        self._printOverrideError(b'openClanStatistic')
        return

    def as_setClanDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setClanData(data)
        return

    def as_setClanEmblemS(self, source):
        if self._isDAAPIInited():
            return self.flashObject.as_setClanEmblem(source)
        return
