from gui.Scaleform.daapi.view.lobby.profile.ProfileSection import ProfileSection

class ProfileHofMeta(ProfileSection):

    def showVehiclesRating(self):
        self._printOverrideError(b'showVehiclesRating')
        return

    def showAchievementsRating(self):
        self._printOverrideError(b'showAchievementsRating')
        return

    def changeStatus(self):
        self._printOverrideError(b'changeStatus')
        return

    def as_setStatusS(self, state):
        if self._isDAAPIInited():
            return self.flashObject.as_setStatus(state)
        return

    def as_setBackgroundS(self, source):
        if self._isDAAPIInited():
            return self.flashObject.as_setBackground(source)
        return

    def as_setBtnCountersS(self, counters):
        if self._isDAAPIInited():
            return self.flashObject.as_setBtnCounters(counters)
        return

    def as_showServiceViewS(self, header, description):
        if self._isDAAPIInited():
            return self.flashObject.as_showServiceView(header, description)
        return

    def as_hideServiceViewS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_hideServiceView()
        return

    def as_showWaitingS(self, description):
        if self._isDAAPIInited():
            return self.flashObject.as_showWaiting(description)
        return

    def as_hideWaitingS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_hideWaiting()
        return
