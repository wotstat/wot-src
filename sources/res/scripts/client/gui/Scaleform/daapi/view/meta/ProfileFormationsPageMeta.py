from gui.Scaleform.daapi.view.lobby.profile.ProfileSection import ProfileSection

class ProfileFormationsPageMeta(ProfileSection):

    def showFort(self):
        self._printOverrideError(b'showFort')
        return

    def createFort(self):
        self._printOverrideError(b'createFort')
        return

    def onClanLinkNavigate(self, code):
        self._printOverrideError(b'onClanLinkNavigate')
        return

    def as_setClanInfoS(self, clanInfo):
        if self._isDAAPIInited():
            return self.flashObject.as_setClanInfo(clanInfo)
        return

    def as_setFortInfoS(self, fortInfo):
        if self._isDAAPIInited():
            return self.flashObject.as_setFortInfo(fortInfo)
        return

    def as_setClanEmblemS(self, clanIcon):
        if self._isDAAPIInited():
            return self.flashObject.as_setClanEmblem(clanIcon)
        return
